import re
import csv
import json
import requests

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
        baseURL (str): the baseURL for the link
        params (dict): the parameters for the link
        resource_link (str): the piece of the direct link to the resource not already represented by baseURL

    Returns
    -------
        dict: the item data as a dictionary
    """
    item_response = requests.get(baseURL + resource_link, params=params)
    item_response_json = item_response.json()
    return item_response_json.get('item')

def create_item_json(output_dir, item_data):
    """
    Creates a json data file for the provided item saved to the provided directory.

    Parameters
    ----------
        output_dir (str): the path to the directory to output files to
        item_data (dict): a dictionary of the data from a particular item.

    Returns
    -------
        json file: a json file with the item data dict. name follows format 'item_{internal_item_id}_metadata'
    """
    try:
        aka = item_data['aka']
        for item in aka:
            x = re.search("https?://www\\.loc\\.gov/item/([0-9]+)/", item)
            if x:
                item_lccn = x.group(1)
                break
            elif not x:
                x = re.search("https?://www\\.loc\\.gov/item/(.+)/", item)
                if x:
                    item_lccn = x.group(1)
                    break
    except KeyError:
        item_lccn = item_data["link"]
        item_lccn = item_lccn.split("/")[-2]

    item_lccn = item_lccn.replace(".", "-")

    try:
        if int(item_lccn) and len(item_lccn) < 10:
            item_lccn = "00" + item_lccn
    except ValueError:
        pass

    item_filename = output_dir + '/item_' + item_lccn + '.json'
    with open(item_filename, 'w', encoding='utf-8') as f:
        json.dump(item_data, f, indent=4)
        print('wrote ' + item_filename)

def main():
    filename = "/Users/ebk/Documents/UMSI/F2026/SI-676/Labs_and_Assignments/si676-labs-and-assignments/Assignment_03--11_13_2026/collection_item_list.csv"
    data = rebuild_item_list(filename)

    baseURL = 'https://www.loc.gov'
    params = {'fo':'json'}
    metadata_dir = "/Users/ebk/Documents/UMSI/F2026/SI-676/Labs_and_Assignments/si676-labs-and-assignments/Assignment_03--11_13_2026/collection_data/item_metadata"

    i = 0
    for i in range(len(data)):
        create_item_json(metadata_dir, get_item_data(baseURL, data[i]['link'], params))
        i+=1


if __name__ == '__main__':
    main()