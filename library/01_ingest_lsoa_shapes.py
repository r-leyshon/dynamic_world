# ingest the generalised 2011 lsoa shapefiles and write to pickle
import geopandas as gpd
import pandas as pd
import os
from pyprojroot import here
import toml

from src.make_data.ingest_ONS_geo import get_shapes

# config deps
CONF_VARS = toml.load(os.path.join(here(), "library", "01_ingest_lsoa_shapes.toml"))

# define the target file name & only run ingestion if it doesn't exist already
target_path = os.path.join(here(), "data", "external", "lsoa_2011_shapefile.geojson")

# wrap the expensive part of this pipeline in an if statement
if os.path.exists(target_path):
    all_shapes = gpd.read_file(target_path)
else:
    # this resource is limited to 50 records at a time, pagination required
    cont_loop = True
    resp_strings = []
    offset = 0
    # the output of this loop will be a list of json content
    while cont_loop:
        cont = get_shapes(params={"resultOffset": offset, "resultRecordCount": 50})
        resp_strings.append(cont)
        # Update the offset to scroll through 50 records
        offset += 50
        print(f"next record batch starts at {offset}")
        cont_loop = "exceededTransferLimit" in cont

    # Convert to a list of geopandas dfs and the append them together
    gdf_list = []
    for i in resp_strings:
        gdf_list.append(gpd.read_file(i))
    all_shapes = pd.concat(gdf_list, axis=0)

    # check we have the correct number of records
    n_records = get_shapes(
        endpoint=CONF_VARS["ONS_GEO"]["LSOA_RECORD_COUNT"],
        params=None,
        expected_encoding="text/plain",
    )

    if int(n_records.split(":")[-1].replace("}", "")) != len(all_shapes):
        raise ValueError("Number of records ingested is wrong")

    # Output to suitable format
    all_shapes.to_file(target_path, driver="GeoJSON")
