# -*- coding: utf-8 -*-

"""Console script for acs_download."""
import sys
import click

import acs_download as acs

@click.command()
@click.option("--year", default = 2017, show_default=True, type=click.IntRange(min=2000, max=2017, clamp=True))
@click.option("--state", default = "Alaska", show_default=True, type=click.STRING)
@click.option("--survey", default = "1-year", type=click.Choice(choices=("1-year", "5-year"), case_sensitive=False))
@click.option("--person-or-household", default="person", type=click.Choice(choices=("person", "household")), show_default=True)
@click.option("--download-path", default="../data/raw/", type=click.Path(exists=True, file_okay=False, writable=True))
@click.option("--extract", default=True, type=click.BOOL)
@click.option("--extract-path", default="../data/interim/", type=click.Path(exists=True, file_okay=False, writable=True))
def main(year, state, survey, person_or_household, download_path, extract, extract_path):
    """Console script for acs_download."""
    acs.get_data(year=year, state=state, survey=survey, person_or_household=person_or_household, download_path=download_path, extract=extract, extract_path=extract_path)

    return print("done!")

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
                                                                        
