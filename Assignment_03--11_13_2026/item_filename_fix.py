import json
import re
import pprint as pp
from pathlib import Path


metadata_dir = Path("/Users/ebk/Documents/UMSI/F2026/SI-676/Labs_and_Assignments/si676-labs-and-assignments/Assignment_03--11_13_2026/collection_data/item_metadata").resolve()



for file in metadata_dir.iterdir():
    with open(file, "r") as f:
        data = json.load(f)

        try:
            aka = data['aka']
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
            item_lccn = data["item"]["link"]
            item_lccn = item_lccn.split("/")[-2]





