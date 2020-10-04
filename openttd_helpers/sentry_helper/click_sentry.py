import click
import logging
import sentry_sdk

from openttd_helpers import click_helper

log = logging.getLogger(__name__)


@click_helper.extend
@click.option("--sentry-dsn", help="Sentry DSN.")
@click.option(
    "--sentry-environment",
    help="Environment we are running in.",
    default="development",
)
def click_sentry(sentry_dsn, sentry_environment):
    """
    Sets up Sentry via a click_helper.extend() method.

    For usage example, see examples/sentry_helper.py.

    @param sentry_dsn: The DSN as given by Sentry.
    @param sentry_environment: The environment to report to Sentry.
    """

    if not sentry_dsn:
        return

    # Release is expected to be in the file '.version'
    with open(".version") as f:
        release = f.readline().strip()

    sentry_sdk.init(sentry_dsn, release=release, environment=sentry_environment)
    log.info(
        "Sentry initialized with release='%s' and environment='%s'",
        release,
        sentry_environment,
    )
