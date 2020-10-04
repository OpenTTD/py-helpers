# openttd-helpers

A repository full of small bits of Python code, commonly used in other
projects developed for OpenTTD.

To increase maintainability and to decrease code duplication, this repository
was created.

# Usage

`pip install openttd-helpers`

See `examples/` folder for example use, or look into OpenTTD repositories containing Python code.

# Modules

## click_helper

Helpers to make the use of "click" easier.

- command: by default, add `-h` to the allowed parameters.
- extend: allow extending a `click.command()` in other functions.
- import_module: used in combination with `Choice`, to auto-load modules based on the choice.

## logging_helper

Setup a default logger via a `click.extend()` function.

## sentry_helper

Setup Sentry via a `click.extend()` function.
