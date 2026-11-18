import json
import re
import pprint as pp
from pathlib import Path


metadata_dir = Path("/Users/ebk/Documents/UMSI/F2026/SI-676/Labs_and_Assignments/si676-labs-and-assignments/Assignment_03--11_13_2026/collection_data/item_metadata").resolve()



for file in metadata_dir.iterdir():
    with open(file, "r") as f:
        data = json.load(f)

        aka = data['aka']
        for item in aka:
            x = re.search("(http)(s){0,1}:\\/\\/www.loc.gov\\/item\\/\\(d*)\\/", item)
            if x:
                print(x.group(2))




