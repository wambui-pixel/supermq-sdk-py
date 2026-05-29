## Python SDK

[![Testing](https://github.com/absmach/supermq-sdk-py/actions/workflows/python-testing.yml/badge.svg?branch=main)](https://github.com/absmach/supermq-sdk-py/actions/workflows/python-testing.yml)
[![Check SDK documentation](https://github.com/absmach/supermq-sdk-py/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/absmach/supermq-sdk-py/actions/workflows/docs.yml)

This is the Magistrala Python SDK, a python driver for [Magistrala HTTP API](https://docs.magistrala.io/api/). API reference in the Swagger UI can be found [here](https://api.magistrala.io/).

Does both system administration (provisioning) and messaging.

## Installation

To install magistrala SDK to your system you will need to have pip installed.

1. To install in a virtual environment

```sh
virtualenv magistralaVenv --python=python3
source magistralaVenv/bin/activate
pip install magistrala
```

2. To install system wide

```sh
pip install magistrala
```

## Usage

You can interact with the magistrala API by calling the various Python SDK functions.

First you need to start magistrala in your system by following the guide [here](https://github.com/absmach/magistrala#usage)

```python
from magistrala import sdk

mgsdk = sdk.SDK(users_url="http://localhost:9002")

# Create a user account
resp = mgsdk.users.create(
    user={"credentials": {"identity": "<email>", "secret": "<password>"}},
    token="",
)
if resp.error.status == 0:
    print(resp.value)
else:
    print(resp.error.message)
```

## Documentation

Official documentation for the SDK is hosted at [here](https://github.com/absmach/supermq-sdk-py/tree/main/docs/README.md). Documentation is auto-generated, the instructions to generate one are:

```sh
pip install lazydocs requests
python3 setup.py install
lazydocs --src-base-url="https://github.com/absmach/supermq-sdk-py/blob/main/" --overview-file="README.md" magistrala
```

Please note that lazydocs requires Python version 3.5 or higher.

If you spot an error or a need for corrections, please let us know - or even better: send us a PR.

## Contributing

Thank you for your interest in Magistrala and the desire to contribute!

1. Take a look at our [open issues](https://github.com/absmach/supermq-sdk-py/issues). The [good-first-issue](https://github.com/absmach/supermq-sdk-py/labels/good-first-issue) label is specifically for issues that are great for getting started.
2. Checkout the [contribution guide](CONTRIBUTING.md) to learn more about our style and conventions.
3. Make your changes compatible to our workflow.

## Community

- [Gitter](https://gitter.im/absmach/magistrala)
- [Twitter](https://twitter.com/absmach)

## License

[Apache-2.0](LICENSE)
