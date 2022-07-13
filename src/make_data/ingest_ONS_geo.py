# Ingest 2011 shapefiles from ONS geoportal

import toml
from pyprojroot import here
import os


def get_shapes(
    endpoint=toml.load(os.path.join(here(), "lib", "01_ingest_lsoa_shapes.toml"))[
        "ONS_GEO"
    ]["LSOA_ENDPOINT"],
    retry_strategy=None,
    headers={
        "Accept": "application/json",
        "user-agent": toml.load(os.path.join(here(), ".secrets.toml"))["REMOTES"][
            "USER_AGENT"
        ],
    },
):
    """
    Request the LSOA shapefiles from ONS geoportal
    """

    print(endpoint)

    print(headers)
