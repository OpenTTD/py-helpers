import asyncio
import click
import coloredlogs
import logging
import shlex
import sys
import verboselogs
import yaml

log = verboselogs.VerboseLogger(__name__)

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}

current_regression = ""


class RegressionFailure(Exception):
    pass


async def _handle_file(data, coverage=False):
    if coverage:
        command = ["coverage", "run", "-a", "--source", "openttd_helpers"]
    else:
        command = ["python"]

    command.extend(shlex.split(data["execute"]))

    python_proc = await asyncio.create_subprocess_exec(
        command[0],
        *command[1:],
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    await python_proc.wait()

    stdout = []
    while line := await python_proc.stdout.readline():
        stdout.append(line.decode().rstrip())
    if stdout:
        stdout.append("")

    stderr = []
    while line := await python_proc.stderr.readline():
        stderr.append(line.decode().rstrip())
    if stderr:
        stderr.append("")

    if "\n".join(stdout) != data.get("stdout", ""):
        log.info("Expected output: %s", data.get("stdout", "").split("\n"))
        log.info("Got output: %s", stdout)
        raise RegressionFailure("Stdout not as expected")
    if "\n".join(stderr) != data.get("stderr", ""):
        log.info("Expected output: %s", data.get("stderr", "").split("\n"))
        log.info("Got output: %s", stderr)
        raise RegressionFailure("Stderr not as expected")


async def _handle_files(filenames, coverage=False):
    global current_regression

    failed = False

    for filename in filenames:
        current_regression = filename

        try:
            with open(filename, "r") as f:
                data = yaml.safe_load(f)

            await _handle_file(data, coverage=coverage)
            log.success("Regression test passed")
        except RegressionFailure as e:
            log.critical(e.args[0])
            failed = True
        except Exception:
            log.exception("Internal regression error")
            return True

    return failed


class RegressionFilter(logging.Filter):
    @classmethod
    def install(cls, handler):
        handler.addFilter(cls())

    def filter(self, record):
        record.regression = "/".join(current_regression.split("/")[1:])
        return 1


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("regression-file", type=click.Path(exists=True, dir_okay=False), nargs=-1)
@click.option("--coverage", help="Run subprocess via coverage", is_flag=True)
def main(regression_file, coverage):
    max_len = 0
    for filename in regression_file:
        cur_len = len("/".join(filename.split("/")[1:]))
        if cur_len > max_len:
            max_len = cur_len

    coloredlogs.install(
        fmt="%(asctime)s [%(regression)-" + str(max_len) + "s] %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )
    for handler in logging.getLogger().handlers:
        handler.addFilter(RegressionFilter())

    loop = asyncio.get_event_loop()
    failed = loop.run_until_complete(_handle_files(regression_file, coverage=coverage))

    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
