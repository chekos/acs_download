from pathlib import Path
from tqdm.autonotebook import tqdm
from zipfile import ZipFile
import requests
import time

def download_acs_data(url: str, 
                      download_path: str = "../data/raw/",
                      extract: bool = True,
                      extract_path: str = "../data/interim/"
                     ):
    """
    Downloads ACS 1-, 3-, or 5- estimates from a US Census Bureau's FTP-server URL.
    """
    
    # Downloads Data
    BASE_URL = "https://www2.census.gov/programs-surveys/acs/data/pums/"
    if not url[:55] == BASE_URL:
        raise ValueError("Census FPT-server url's start with 'https://www2.census.gov/programs-surveys/acs/data/pums/'")

    state = url.split("/")[-1].split(".")[0][-2:]
    
    chunk_size = 1024

    r = requests.get(url, stream = True)
    total_size = int(r.headers['content-length'])

    ### Checks
    download_path = Path(download_path)
    extract_path = Path(extract_path)
    
    if download_path.is_file():
        raise ValueError("You provided a path to a file. You need to provide a path to a directory.")
    # if not download_path.is_dir():
    #     raise ValueError("You need to provide a path to a directory.")
    if not download_path.exists():
        download_path.mkdir()
    
    ### downloads data
    filename = url.split('/')[-1]

    with open(download_path / filename, 'wb') as f:
        print(f"Downloading at {download_path / filename}.")
        for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total_size/chunk_size, unit = 'KB'):
            f.write(data)

    print("Download complete!")
    
    ## Extract file
    if extract:
        year = url.split("/")[7]
        extract_folder = f"ACS_{year}"
        
        final_extraction_folder = extract_path / extract_folder.upper() / state
        
        if extract_path.is_file():
            raise ValueError("You provided a path to a file. You need to provide a path to a directory.")
        # if not extract_path.is_dir():
        #     raise ValueError("You need to provide a path to a directory.")
        if not extract_path.exists():
            extract_path.mkdir()
        
        # remove dir if it exists
        if final_extraction_folder.exists():
            for item in final_extraction_folder.glob("*"):
                item.unlink()
            final_extraction_folder.rmdir()
        
        # create dir
        if not Path(extract_path / extract_folder.upper()).exists():
            Path(extract_path / extract_folder.upper()).mkdir()
        final_extraction_folder.mkdir()
        
        # extracts data
        content_file = ZipFile(download_path / filename)
        
        
        ## for progress bar
        file_size = 0
        for file_info in content_file.infolist():
            file_size += int(file_info.file_size)
        
        extract_folder_size = sum(item.stat().st_size for item in final_extraction_folder.iterdir())
        expected_final_size = extract_folder_size + file_size
        
        ## Start extraction:
        print(f"Extracting to {final_extraction_folder}")
        content_file.extractall(final_extraction_folder)
        while extract_folder_size < expected_final_size:
            extract_folder_size = sum(item.stat().st_size for item in final_extraction_folder.iterdir())
            print(f"Extracting files to {final_extraction_folder}: {(extract_folder_size / file_size) :.2%}", end = '\r')
            time.sleep(.5)
            break
        
        print("Files extracted successfully")