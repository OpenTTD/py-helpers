import logging

from openttd_helpers import (
    click_helper,
    sentry_helper,
)

log = logging.getLogger(__name__)


@click_helper.command()
@sentry_helper.click_sentry
def main():
    pass


if __name__ == "__main__":
    main()
