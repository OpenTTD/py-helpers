# openttd-helpers

[![GitHub License](https://img.shields.io/github/license/OpenTTD/py-helpers)](https://github.com/OpenTTD/py-helpers/blob/main/LICENSE)

A repository full of small bits of Python code, commonly used in other
projects developed for OpenTTD.

To increase maintainability and to decrease code duplication, this repository
was created.

# Usage

`pip install openttd-helpers`

See `examples/` folder for example use, or look into OpenTTD repositories containing Python code.

# Modules

## asyncio_helper

Helpers to make the user of `ayncio` easier.

- task: `enable_strong_referenced_tasks()` makes returned tasks from `ayncio.create_task` strong, so they are not garbage collected unexpectedly.

## click_helper

Helpers to make the use of `click` easier.

- command: by default, add `-h` to the allowed parameters.
- extend: allow extending a `click.command()` in other functions.
- import_module: used in combination with `Choice`, to auto-load modules based on the choice.

## logging_helper

Setup a default logger via a `click.extend()` function.

## sentry_helper

Setup Sentry via a `click.extend()` function.
