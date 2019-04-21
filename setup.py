from setuptools import setup

setup(
    name="postcodeapi",
    version="1.2.1",
    description="An unofficial Python wrapper around the Postcode API v2",
    long_description=open("README.rst").read(),
    url="http://github.com/roedesh/postcodeapi",
    author="Ruud Schroën",
    author_email="schroenruud@gmail.com",
    license="MIT",
    packages=["postcodeapi"],
    install_requires=["requests"],
)
