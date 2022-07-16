# ingest the generalised 2011 lsoa shapefiles and write to pickle

from src.make_data.ingest_ONS_geo import get_shapes

# this resource is limited to 50 records at a time, pagination required
cont_loop = True
resp_strings = []
offset = 0

while cont_loop:
    cont = get_shapes(params={"resultOffset": offset, "resultRecordCount": 50})
    resp_strings.append(cont)
    # Update the offset to scroll through 50 records
    offset += 50
    print(f"next record batch starts at {offset}")
    cont_loop = "exceededTransferLimit" in cont
