import click

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


def command(*args, **kwargs):
    """
    Similar to click.command(), but support "-h" by default to show help.
    """

    if "context_settings" not in kwargs:
        kwargs["context_settings"] = CONTEXT_SETTINGS

    return click.command(*args, **kwargs)
