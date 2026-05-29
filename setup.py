import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Magistrala",
    version="0.0.1",
    author="Magistrala Contributors",
    author_email="info@magistrala.com",
    description="Python SDK for Magistrala",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/absmach/supermq-sdk-py",
    project_urls={
        "Bug Tracker": "https://github.com/absmach/supermq-sdk-py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
