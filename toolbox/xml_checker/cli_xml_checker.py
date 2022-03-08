import grobid_xml_checker

import click


@click.group()
def group():
    """
    CLI for validating XML files with an XSD
    """


@group.command("validate")
@click.argument("rootdir", type=str)
def run(rootdir):
    """
    Validate an XML if a root directory is provided.
    """
    grobid_xml_checker.validate_with_xsd(rootdir)


if __name__ == "__main__":
    group()
