from setuptools import setup

setup(
    name="dbalum_get",
    version="0.1.0",
    author="huzi",
    packages=[
        "dbalum_get",
    ],
    scripts=["dbalum_get/dbalum_get"],
    #    url='http://pypi.python.org/pypi/PackageName/',
    description="An awesome package that does something",
    long_description=open("README.md").read(),
    install_requires=[
        "beautifulsoup4 >= 4",
    ],
)
