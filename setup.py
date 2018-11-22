from setuptools import setup

setup(
    name="postcodeapi",
    version="1.0.1",
    description="A tiny wrapper around the Postcode API v2",
    long_description=open("README.md").read(),
    url="http://github.com/roedesh/postcodeapi",
    author="Ruud Schroën",
    author_email="schroenruud@gmail.com",
    license="MIT",
    packages=["postcodeapi"],
    install_requires=["requests"],
)
