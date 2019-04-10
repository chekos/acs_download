# -*- coding: utf-8 -*-

"""Top-level package for acs_download."""

__author__ = """Sergio Sánchez Zavala"""
__email__ = 'sergio@cimarron.io'
__version__ = '0.1.2'

# -*- coding: utf-8 -*-

"""Main module."""
# imports
from pathlib import Path
from typing import Union
from tqdm.autonotebook import tqdm
from zipfile import ZipFile
import requests
import time
import us

import acs_download
from acs_download.download import download_acs_data
from acs_download.url_builder import build_acs_url
   
def get_data(
    year: Union[int, str] = '2017', 
    survey: Union[str, int] = '1-Year', 
    person_or_household: str = 'person',
    state: str = 'California',
    download_path: str = "../data/raw/",
    extract: bool = True,
    extract_path: str = "../data/interim/",
):
    """
    Builds URL and downloads ACS 1-Year or 5-Year state PUMS estimates into a specified folder (defaults to ../data/raw/).
    """
    
    # builds URL
    URL = build_acs_url(year = year,
                        survey = survey, 
                        person_or_household = person_or_household, 
                        state = state
                 )
    
    # download data
    download_acs_data(
        url = URL, 
        download_path = download_path, 
        extract = extract, 
        extract_path = extract_path
    )
    
    return None

## from realpython.com
def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')
     
    
if __name__ == "__main__":
    get_data()