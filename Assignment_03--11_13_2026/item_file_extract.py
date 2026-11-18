import json
import requests
from pathlib import Path

"""
FILE LOCATION CONSTANTS
"""

# assuming script is run from assignment_03 dir
metadata_dir = Path(".", "collection_data/item_metadata")
file_dir = Path(".", "collection_data/item_files")


"""
HELPER FUNCTIONS
"""

def find_fullsize_img(filename):
    with open(filename, "r") as f:
        data = json.loads(f.read())
        try:
            img_url = data["image_url"][-1]
        except KeyError:
            img_url = data["service_medium"]
            img_url = "v".join(img_url.rsplit("r", 1))
    return (data, img_url)

def create_full_item_dict(filename, data, img):
    item = {
        "filename" : "",
        "lccn" : "",
        "img" : "",
    }
    file = str(filename.name)
    item["filename"] = file
    item["lccn"] = file[file.index("_")+1:file.index(".json")]
    item["img"] = img
    return item

def request_img(item: dict):
    img = item["img"]
    lccn = item["lccn"]

    r = requests.get(img)
    img_filename = file_dir / ("item_" + lccn + ".jpg")

    with open(img_filename, "wb") as f:
        f.write(r.content)
        print("wrote", img_filename)

def main():

    item_list = []
    for file in metadata_dir.iterdir():
        data, img = find_fullsize_img(file)
        new_data = create_full_item_dict(file, data, img)
        item_list.append(new_data)

    for item in item_list:
        request_img(item)

if __name__ == "__main__":
    main()