import setuptools
import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openttd-helpers",
    version=version.get_version(),
    author="OpenTTD Dev Team",
    author_email="info@openttd.org",
    description="Small helpers common in most Python applications for OpenTTD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OpenTTD/py-helpers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'click>=7.1.2',
        'sentry_sdk>=0.18.0'
    ],
)
