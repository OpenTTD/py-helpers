import click

from openttd_helpers import click_helper


@click_helper.extend
@click.option("--parameter", default=1)
@click.option(
    "--mod",
    help="Pick a module.",
    type=click.Choice(["mod-a", "mod-b"], case_sensitive=False),
    callback=click_helper.import_module("mod", "Mod"),
)
@click.option(
    "--mod-multi",
    help="Pick a module.",
    type=click.Choice(["mod-a", "mod-b"], case_sensitive=False),
    multiple=True,
    callback=click_helper.import_module("mod", "Mod"),
)
def click_function(parameter, mod, mod_multi):
    print(f"Parameter has value {parameter}")

    if mod:
        instance = mod()
        print(f"Mod is saying {instance.print()}")

    if mod_multi:
        for mod in mod_multi:
            instance = mod()
            print(f"Mod is saying {instance.print()}")


@click_helper.command()
@click_function
def main():
    pass


if __name__ == "__main__":
    main()
