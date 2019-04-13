postcodeapi
===========

``postcodeapi`` is an unofficial Python wrapper around the Postcode API
V2.

|PyPI version| |Build Status| |Requirements Status| |Coverage Status|

Installation and usage
----------------------

Installation
~~~~~~~~~~~~

*postcodeapi* can be installed by running ``pip install postcodeapi``.

Usage
~~~~~

Here is an example of how to use the API client. First you initialize a
client with your API key, after that you use one of the four getter
methods to fetch the data you need. They all return the actual JSON
response converted to a Python dictionary.

.. code:: python

   # Import the PostcodeAPIClient
   from postcodeapi.client import PostcodeAPIClient

   # Initialize a client with your API key
   client = PostcodeAPIClient(api_key="YOUR_API_KEY")

   # Fetch a list of addresses (for a given postal_code and number)
   # The postal_code and number parameters are optional
   # The number parameter only works together with postal_code
   data = client.get_all_addresses(postal_code="5038EA", number=19)
   addresses = data["results"] # List of addresses
   next_id = data["next"] # Next ID to search from (used for pagination)

   # Fetch a single address
   address = client.get_address(address_id="0855200000046355")

   # Fetch a list of postal codes (within a specific area)
   # The area parameter is optional
   data = client.get_all_postal_codes(area="5038")
   postal_codes = data["results"] # List of postal codes
   next_postal_code = data["next"] # Next postal code to search from (used for pagination)

   # Fetch a single postal code
   postal_code = client.get_postal_code("5038EA")

Exceptions
~~~~~~~~~~

There are 5 exceptions that can occur:

-  ``NoAccessException``, which occurs when the current account does not
   have the required privileges to perform the action;
-  ``ResourceNotFoundException``, which occurs when the returned
   status_code is 404. Limited to the *get_address* and
   *get_postal_code* methods;
-  ``HouseNumberRequiresPostalCodeException``, which occurs when a
   house_number is given but not a postal_code. Limited to the
   *get_all_addresses* method;
-  ``InvalidPostalCodeException``, which occurs when an invalid postal
   code is given;
-  ``LimitExceededException``, which occurs when there are too many
   network requests or the limit has been exceeded

Documentation
-------------

For more information about the data that is returned, please refer to
the `official API documentation`_. It is written in Dutch.

Running tests
-------------

To run the tests, make sure you install the dev dependencies by running
``pipenv install --dev``, and then run

.. _official API documentation: https://www.postcodeapi.nu/docs/

.. |PyPI version| image:: https://badge.fury.io/py/postcodeapi.svg
   :target: https://badge.fury.io/py/postcodeapi
.. |Build Status| image:: https://travis-ci.org/roedesh/postcodeapi.svg?branch=master
   :target: https://travis-ci.org/roedesh/postcodeapi
.. |Requirements Status| image:: https://requires.io/github/roedesh/postcodeapi/requirements.svg?branch=master
   :target: https://requires.io/github/roedesh/postcodeapi/requirements/?branch=master
.. |Coverage Status| image:: https://coveralls.io/repos/github/roedesh/postcodeapi/badge.svg?branch=master
   :target: https://coveralls.io/github/roedesh/postcodeapi?branch=master
