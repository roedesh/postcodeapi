from tests.mock_generic import MockResponse


def mock_address(*args, **kwargs):
    """
    This method returns a successful response which contains data of a single address.
    """
    return MockResponse(
        status_code=200,
        text="""
    {
        "purpose": "kantoorfunctie",
        "postcode": "5038EA",
        "surface": 978,
        "municipality": {
            "id": "0855",
            "label": "Tilburg"
        },
        "city": {
            "id": "1043",
            "label": "Tilburg"
        },
        "letter": null,
        "geo": {
            "center": {
                "rd": {
                    "type": "Point",
                    "coordinates": [
                        133891.872,
                        396794.828
                    ],
                    "crs": {
                        "type": "name",
                        "properties": {
                            "name": "urn:ogc:def:crs:EPSG::28992"
                        }
                    }
                },
                "wgs84": {
                    "type": "Point",
                    "coordinates": [
                        5.0828098,
                        51.5597043
                    ],
                    "crs": {
                        "type": "name",
                        "properties": {
                            "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                        }
                    }
                }
            },
            "exterior": {
                "wgs84": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                5.0826017,
                                51.559667
                            ],
                            [
                                5.0828017,
                                51.5596223
                            ],
                            [
                                5.0828853,
                                51.5597703
                            ],
                            [
                                5.0827114,
                                51.5598075
                            ],
                            [
                                5.0827055,
                                51.5598015
                            ],
                            [
                                5.0826401,
                                51.559815
                            ],
                            [
                                5.0825628,
                                51.5596756
                            ],
                            [
                                5.0826017,
                                51.559667
                            ]
                        ]
                    ],
                    "crs": {
                        "type": "name",
                        "properties": {
                            "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                        }
                    }
                }
            }
        },
        "nen5825": {
            "postcode": "5038 EA",
            "street": "STATIONSSTRAAT"
        },
        "number": 5,
        "addition": null,
        "year": 1905,
        "province": {
            "id": "30",
            "label": "Noord-Brabant"
        },
        "id": "0855200000046355",
        "type": "Verblijfsobject",
        "street": "Stationsstraat",
        "_links": {
            "self": {
                "href": "https://api.postcodeapi.nu/v2/addresses/0855200000046355/"
            }
        }
    }
    """,
    )


def mock_all_addresses(*args, **kwargs):
    """
    This method returns a successful response which contains a collection of addresses.
    """
    return MockResponse(
        status_code=200,
        text="""
    {
        "_embedded": {
            "addresses": [
                {
                    "purpose": "kantoorfunctie",
                    "postcode": "5038EA",
                    "surface": 978,
                    "municipality": {
                        "id": "0855",
                        "label": "Tilburg"
                    },
                    "city": {
                        "id": "1043",
                        "label": "Tilburg"
                    },
                    "letter": null,
                    "geo": {
                        "center": {
                            "rd": {
                                "type": "Point",
                                "coordinates": [
                                    133891.872,
                                    396794.828
                                ],
                                "crs": {
                                    "type": "name",
                                    "properties": {
                                        "name": "urn:ogc:def:crs:EPSG::28992"
                                    }
                                }
                            },
                            "wgs84": {
                                "type": "Point",
                                "coordinates": [
                                    5.0828098,
                                    51.5597043
                                ],
                                "crs": {
                                    "type": "name",
                                    "properties": {
                                        "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                                    }
                                }
                            }
                        }
                    },
                    "nen5825": {
                        "postcode": "5038 EA",
                        "street": "STATIONSSTRAAT"
                    },
                    "addition": null,
                    "number": 5,
                    "year": 1905,
                    "province": {
                        "id": "30",
                        "label": "Noord-Brabant"
                    },
                    "id": "0855200000046355",
                    "type": "Verblijfsobject",
                    "street": "Stationsstraat",
                    "_links": {
                        "self": {
                            "href": "https://api.postcodeapi.nu/v2/addresses/0855200000046355/"
                        }
                    }
                }
            ]
        },
        "_links": {
            "self": {
                "href": "https://api.postcodeapi.nu/v2/addresses/?postcode=5038EA"
            }
        }
    }
    """,
    )


def mock_postal_code_missing(*args, **kwargs):
    """
    This method returns a error response which occurs when a postal code is missing.
    """
    return MockResponse(
        status_code=400,
        text="""
    {
        "error": "Query parameter 'number' can only be used in conjunction with 'postcode'."
    }
    """,
    )
