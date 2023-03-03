import csv
import json
import os

import pandas
import requests
from tqdm import tqdm

countries = pandas.read_csv(
    os.path.join(os.path.dirname(__file__), "..", "notes", "countries.csv")
)
events = []

for iso_a3 in tqdm(countries.GID_0):
    url = f"https://global-flood-database.cloudtostreet.ai/collection/{iso_a3}"
    local_filename = os.path.join(
        os.path.dirname(__file__), "..", "cloudtostreet", f"events_{iso_a3}.json"
    )

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)

    with open(local_filename, "r") as f:
        country_events = json.load(f)
        for event in country_events:
            events.append(
                (event.replace("projects/global-flood-db/gfd_v4/", ""), iso_a3)
            )

events_fname = local_filename = os.path.join(
    os.path.dirname(__file__), "..", "cloudtostreet", f"country_events.csv"
)
with open(events_fname, "w") as fh:
    w = csv.writer(fh)
    w.writerow(("DFO", "ISO_A3"))
    for event in events:
        w.writerow(event)
