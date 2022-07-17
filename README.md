# `dynamic_world`

investigating land use classification with Google Dynamic World

```{warning}
Where this documentation refers to the root folder we mean where this README.md is
located.
```

## Getting started

To start using this project, [first make sure your system meets its
requirements](#requirements).

To be added.

### Requirements

```{note} Requirements for contributors
[Contributors have some additional requirements][contributing]!
```

- Python 3.6.1+ installed
- a `.secrets` file with the [required secrets and
  credentials](#required-secrets-and-credentials)
- [load environment variables][docs-loading-environment-variables] from `.envrc`

To install the Python requirements, open your terminal and enter:

```shell
pip install -r requirements.txt
```

## Required secrets and credentials

To run this project, you will need:

- the service Email for your GCP application service account, stored in a toml file under: `.git_ignore/ee.toml`
- your GCP application key json file stored within a gitignored `.git_ignore` directory.



| Secret/credential | Environment variable name | Description                                |
|-------------------|---------------------------|--------------------------------------------|
| Secret 1          | `SERVICE_EMAIL`       | Email associated with service account for application. See [Google Earth Engine Service Account Documentation](https://developers.google.com/earth-engine/guides/service_account) for full details.     |
| Secret 2      | `ee-lsoa-land-use-02b30d7b328b.json`   | Secret credential key value pari in JSON file format. |

Once you've added, use the `toml` package to reference `SERVICE_EMAIL`. `ee.ServiceAccountCredentials()` has native support for secret json encoding.

## Licence

Unless stated otherwise, the codebase is released under the MIT License. This covers
both the codebase and any sample code in the documentation. The documentation is ©
Crown copyright and available under the terms of the Open Government 3.0 licence.

## Contributing

[If you want to help us build, and improve `dynamic_world`, view our
contributing guidelines][contributing].

## Acknowledgements

[This project structure is based on the `govcookiecutter` template
project][govcookiecutter].

[contributing]: ./docs/contributor_guide/CONTRIBUTING.md
[govcookiecutter]: https://github.com/best-practice-and-impact/govcookiecutter
[docs-loading-environment-variables]: ./docs/user_guide/loading_environment_variables.md
[docs-loading-environment-variables-secrets]: ./docs/user_guide/loading_environment_variables.md#storing-secrets-and-credentials
