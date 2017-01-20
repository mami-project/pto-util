#!/usr/bin/env python3

# script to download all data from a measurment campaign

import os
import sys
import requests

campaign = sys.argv[1]
file_format = sys.argv[2]
api_key = sys.argv[3]

if len(sys.argv) >= 5:
    filename_contains = sys.argv[4]
else:
    filename_contains = None

url = 'https://observatory.mami-project.eu/hdfs/fs/{cmd}/{campaign}/{file_format}'

def get_remote_file_list(filterexp):
    ls_url = url.format(cmd='ls', campaign=campaign, file_format=file_format)
    headers = {'X-API-KEY': api_key}
    response = requests.get(ls_url, headers=headers, verify=False)
    
    filenames = response.text.strip().strip('[]').split(',')
    filenames = [x.strip('"') for x in filenames]

    if filterexp:
        filenames = filter(lambda x: str(x).find(filterexp) >= 0, filenames)

    return set(filenames)

def get_local_file_list():    
    return set(os.listdir(campaign))

def fetch_file(filename):
    bin_url = url.format(cmd='bin', campaign=campaign, file_format=file_format)
    bin_url = bin_url+ '/' + filename
    headers = {'X-API-KEY': api_key}

    response = requests.get(bin_url, headers=headers, verify=False)

    with open(campaign + '/' + filename, 'wb') as destination_file:
        destination_file.write(response.content)

if __name__ == "__main__":
    remote_files = get_remote_file_list(filename_contains)
    local_files = get_local_file_list()
    
    missing_files = remote_files.difference(local_files)

    print("---> Goodmorning! I have to fetch {} new files".format(
            len(missing_files)))

    for missing_file in missing_files:
        print("---> fetching: {}".format(missing_file))
        fetch_file(missing_file)

    print("---> Goodnight!")
