import logging

from page_info_downloader import download_page
import json
from tqdm import tqdm
import time
from dataset import Dataset
from data_fields import MAL

BASE_URL = "https://myanimelist.net/anime/{}"


def download_next_samples(pages_to_download: int, dataset: Dataset):
    start_id = dataset.check_last_id() + 1
    print(start_id)

    download_range(start_id, start_id + pages_to_download, dataset)


def download_range(start: int, end: int, dataset: Dataset):
    samples = []

    for j in tqdm(range(start, end)):
        info = download_page(BASE_URL.format(j))
        if info:
            info["id"] = j
            samples.append(info)
    dataset.add_samples(samples)
    with open("dataset.json", 'w') as outfile:
        json.dump(dataset.dataset, outfile)


if __name__ == "__main__":
    my_dataset = Dataset("dataset.json", MAL)
    for i in range(50):
        logging.info("round {}".format(i))
        download_next_samples(30, my_dataset)
        time.sleep(100)