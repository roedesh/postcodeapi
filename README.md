# postcodeapi

`postcodeapi` is a tiny Python wrapper around the Postcode API V2.

[![PyPI version](https://badge.fury.io/py/postcodeapi.svg)](https://badge.fury.io/py/postcodeapi)
[![Build Status](https://travis-ci.org/roedesh/postcodeapi.svg?branch=master)](https://travis-ci.org/roedesh/postcodeapi)
[![Coverage Status](https://coveralls.io/repos/github/roedesh/postcodeapi/badge.svg?branch=master)](https://coveralls.io/github/roedesh/postcodeapi?branch=master)

## Installation and usage

### Installation

*postcodeapi* can be installed by running `pip install postcodeapi`.

### Usage

Here is an example of how to use the API client. First you initialize a client with your API key, after that you use 
one of the four getter methods to fetch the data you need. They all return the actual JSON response converted to a 
Python dictionary.

```python
# Import the PostcodeAPIClient
from postcodeapi.client import PostcodeAPIClient

# Initialize a client with your API key
client = PostcodeAPIClient(api_key="YOUR_API_KEY")

# Fetch a list of addresses (for a given postal_code and number)
# The postal_code and number parameters are optional
# The number parameter only works together with postal_code
data = client.get_all_addresses(postal_code="5038EA", number=19)
addresses = data["_embedded"]["addresses"] # List of addresses

# Fetch a single address
address = client.get_address(address_id="0855200000046355")

# Fetch a list of postal codes (within a specific area) 
# The area parameter is optional
data = client.get_all_postal_codes(area="5038")
postal_codes = data['_embedded']['postcodes'] # List of postal codes

# Fetch a single postal code
postal_code = client.get_postal_code("5038EA")
```

## Documentation
For more information about the data that is returned, please refer to the [official API documentation](https://www.postcodeapi.nu/docs/). It is written in Dutch.

## Running tests
To run the tests, make sure you have the dev dependencies installed, and run `pytest` in the root of the project.

## Issues
If you have any issues with the API wrapper, please post them [here](https://github.com/infoklik/postcodeapi/issues). If you have issues with the actual API, 
please post them in the [official issue tracker](https://github.com/postcodeapi/postcodeapi/issues) of Postcode API.
