import datetime
import logging

from openttd_helpers import (
    click_helper,
    logging_helper,
)

log = logging.getLogger(__name__)


# We force the time to 2020-01-01, 00:00:01, to ensure regression can run
# with the same output every single time.
def fix_time(self, record, datefmt=None):
    return datetime.datetime(2020, 1, 1, 0, 0, 1).strftime("%Y-%m-%d %H:%M:%S")


logging.Formatter.formatTime = fix_time


@click_helper.command()
@logging_helper.click_logging
def main():
    log.info("Testing")
    log.warning("Warning")


if __name__ == "__main__":
    main()
