# openttd-helpers

[![GitHub License](https://img.shields.io/github/license/OpenTTD/py-helpers)](https://github.com/OpenTTD/py-helpers/blob/main/LICENSE)
[![GitHub Tag](https://img.shields.io/github/v/tag/OpenTTD/py-helpers?include_prereleases&label=stable)](https://github.com/OpenTTD/py-helpers/releases)
[![GitHub commits since latest release](https://img.shields.io/github/commits-since/OpenTTD/py-helpers/latest/main)](https://github.com/OpenTTD/py-helpers/commits/main)

[![GitHub Workflow Status (Testing)](https://img.shields.io/github/workflow/status/OpenTTD/py-helpers/Testing/main?label=main)](https://github.com/OpenTTD/py-helpers/actions?query=workflow%3ATesting)
[![GitHub Workflow Status (Release)](https://img.shields.io/github/workflow/status/OpenTTD/py-helpers/Release?label=release)](https://github.com/OpenTTD/py-helpers/actions?query=workflow%3A%22Release%22)

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
