import logging

from openttd_helpers import click_helper


@click_helper.extend
def click_logging():
    """
    Sets up a default logging via a click_helper.extend() method.

    For usage example, see examples/logging_helper.py.
    """

    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s [%(name)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO
    )
