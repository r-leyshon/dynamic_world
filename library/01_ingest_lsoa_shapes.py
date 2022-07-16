# ingest the generalised 2011 lsoa shapefiles and write to pickle
import geopandas as gpd
import pandas as pd

from src.make_data.ingest_ONS_geo import get_shapes

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


# Output to suitable format
