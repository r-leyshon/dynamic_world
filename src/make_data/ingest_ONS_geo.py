# Ingest 2011 shapefiles from ONS geoportal

import toml
from pyprojroot import here
import os
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import requests


def get_shapes(
    endpoint=toml.load(os.path.join(here(), "library", "01_ingest_lsoa_shapes.toml"))[
        "ONS_GEO"
    ]["LSOA_ENDPOINT"],
    retry_strategy=Retry(
        total=3,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS"],
        raise_on_status=False,
        backoff_factor=1,
    ),
    headers={
        "Accept": "application/json",
        "user-agent": toml.load(os.path.join(here(), ".secrets.toml"))["REMOTES"][
            "USER_AGENT"
        ],
    },
    params={"resultOffset": 0, "resultRecordCount": 50},
):
    """
    Request the LSOA shapefiles from ONS geoportal
    """
    # prep requests session
    resource_adapter = HTTPAdapter(max_retries=retry_strategy)
    req_session = requests.Session()
    req_session.mount("https://", resource_adapter)
    req_session.mount("http://", resource_adapter)
    req_session.headers.update(headers)
    resp = req_session.get(endpoint, params=params)
    # handle the response
    if resp.ok is not True:
        raise ValueError(f"Response returned {resp.status_code}.")

    elif "application/json" not in resp.headers["Content-Type"]:
        raise ValueError(
            f"Response not as expected, {resp.headers.get('content-type')} returned."
        )

    else:
        content = resp.json()
        return content
