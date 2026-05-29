## Python SDK

[![Testing](https://github.com/absmach/supermq-sdk-py/actions/workflows/python-testing.yml/badge.svg?branch=main)](https://github.com/absmach/supermq-sdk-py/actions/workflows/python-testing.yml)
[![Check SDK documentation](https://github.com/absmach/supermq-sdk-py/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/absmach/supermq-sdk-py/actions/workflows/docs.yml)

This is the Magistrala Python SDK, a python driver for [Magistrala HTTP API](https://docs.magistrala.io/api/) API reference in the Swagger UI can be found [here](https://api.magistrala.io/).

Does both system administration (provisioning) and messaging.

## Installation

To install magistrala SDK to your system you will need to have pip installed.
To install magistrala SDK to your system you will need to have pip installed.

1. To install in a virtual environment

```sh
virtualenv magistralaVenv --python=python3.8
source magistralaVenv/bin/activate
pip install magistrala
virtualenv magistralaVenv --python=python3.8
source magistralaVenv/bin/activate
pip install magistrala
```

2. To install system wide

```sh
pip install magistrala
pip install magistrala
```

## Usage

You can interact with the magistrala API by calling the various Python SDK functions.
You can interact with the magistrala API by calling the various Python SDK functions.

First you need to start magistrala in your system by following the guide [here](https://github.com/absmach/magistrala#usage)

```python
from magistrala import SDK
from magistrala import SDK

default_url = "http://localhost"

sdk = SDK()

# Example to create an account
resp = sdk.users.create({"credentials": {"identity": "<user_email>", "secret": "<user_password>"}}, token="")
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

## Professional Support

There are many companies offering professional support for the Magistrala system.
There are many companies offering professional support for the Magistrala system.

If you need this kind of support, best is to reach out to [@drasko](https://github.com/drasko) directly, and he will point you out to the best-matching support team.

## Contributing

Thank you for your interest in Magistrala and the desire to contribute!
Thank you for your interest in Magistrala and the desire to contribute!

1. Take a look at our [open issues](https://github.com/absmach/supermq-sdk-py/issues). The [good-first-issue](https://github.com/absmach/supermq-sdk-py/labels/good-first-issue) label is specifically for issues that are great for getting started.
2. Checkout the [contribution guide](CONTRIBUTING.md) to learn more about our style and conventions.
3. Make your changes compatible to our workflow.

## Community

- [Google group](https://groups.google.com/forum/#!forum/magistrala)
- [Gitter](https://gitter.im/magistrala/magistrala?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
- [Twitter](https://twitter.com/magistrala)
- [Google group](https://groups.google.com/forum/#!forum/magistrala)
- [Gitter](https://gitter.im/magistrala/magistrala?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
- [Twitter](https://twitter.com/magistrala)

## License

[Apache-2.0](LICENSE)
