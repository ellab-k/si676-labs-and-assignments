import csv
import glob
import json
import requests
from pathlib import Path

"""
HELPER FUNCTIONS
"""

def rebuild_item_list(collection_csv):
    """
    Rebuilds a list of items in a collection from a CSV.

    Parameters
    -----------
        collection_csv (str) : file path to the csv

    Returns
    -------
        dict : a dictionary containing headers from the csv as keys and the column data as values
    """

    with open(collection_csv, 'r', encoding='utf-8', newline='') as f:
        data = csv.DictReader(f)
        collection_items = [{field : row[field] for field in data.fieldnames if field != 'alt'} for row in data]
    return collection_items

def get_item_data(baseURL, resource_link, params):
    """
    Extracts individual item data from a HTTP request and formats it into a dictionary.

    Parameters
    ----------
        baseURL (str) :
        params (dict) :
        resource_link (str) :

    Returns
    -------
        dict : the item data as a dictionary
    """
    item_response = requests.get(baseURL + resource_link, params=params)
    item_response_json = item_response.json()
    return item_response_json.get('item')

def create_item_json():
    pass


"""
MAIN CODE
"""

def main():
    filename = "/Users/ebk/Documents/UMSI/F2026/SI-676/Labs_and_Assignments/si676-labs-and-assignments/Assignment_03--11_13_2026/collection_item_list.csv"
    data = rebuild_item_list(filename)

    baseURL = 'https://www.loc.gov'
    params = {'fo':'json'}

    resource_test = data[0]['link']

    print(get_item_data(baseURL, resource_test, params))


if __name__ == '__main__':
    main()