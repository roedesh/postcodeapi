from tests.mock_generic import MockResponse


def mock_all_postal_codes(*args, **kwargs):
    """
    This method returns a successful mock response which contains a collection of postal codes.
    Not all postal codes have been included in this response to keep it shorter.
    """
    return MockResponse(
        status_code=200,
        text="""
    {
        "_embedded": {
            "postcodes": [
                {
                    "city": {
                        "id": "3560",
                        "label": "Apeldoorn"
                    },
                    "geo": {
                        "center": {
                            "wgs84": {
                                "type": "Point",
                                "coordinates": [
                                    5.9550706,
                                    52.2202707
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
                        "streets": [
                            "LOOLAAN",
                            "KONINKLIJK PARK"
                        ],
                        "postcode": "7315 AA"
                    },
                    "postcode": "7315AA",
                    "province": {
                        "id": "25",
                        "label": "Gelderland"
                    },
                    "streets": [
                        "Loolaan",
                        "Koninklijk Park"
                    ],
                    "municipality": {
                        "id": "0200",
                        "label": "Apeldoorn"
                    },
                    "_links": {
                        "self": {
                            "href": "https://api.postcodeapi.nu/v2/postcodes/7315AA/"
                        }
                    }
                }
            ]
        },
        "_links": {
            "self": {
                "href": "https://api.postcodeapi.nu/v2/postcodes/"
            },
            "next": {
                "href": "https://api.postcodeapi.nu/v2/postcodes/?from%5Bpostcode%5D=7315BA&from%5BpostcodeArea%5D=7315"
            }
        }
    }
    """,
    )


def mock_all_postal_codes_area(*args, **kwargs):
    """
    This method returns a successful mock response which contains a collection of postal codes in the
    7313 area. Not all postal codes have been included in this response to keep it shorter.
    """
    return MockResponse(
        status_code=200,
        text="""
    {
        "_embedded": {
            "postcodes": [
                {
                    "city": {
                        "id": "1145",
                        "label": "Enschede"
                    },
                    "geo": {
                        "center": {
                            "wgs84": {
                                "type": "Point",
                                "coordinates": [
                                    6.8819886,
                                    52.2204943
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
                        "streets": [
                            "STADSMATENSTRAAT"
                        ],
                        "postcode": "7513 AA"
                    },
                    "postcode": "7513AA",
                    "province": {
                        "id": "23",
                        "label": "Overijssel"
                    },
                    "streets": [
                        "Stadsmatenstraat"
                    ],
                    "municipality": {
                        "id": "0153",
                        "label": "Enschede"
                    },
                    "_links": {
                        "self": {
                            "href": "https://api.postcodeapi.nu/v2/postcodes/7513AA/"
                        }
                    }
                }
            ]
        },
        "_links": {
            "self": {
                "href": "https://api.postcodeapi.nu/v2/postcodes/?postcodeArea=7513"
            },
            "next": {
                "href": "https://api.postcodeapi.nu/v2/postcodes/?postcodeArea=7513&from%5Bpostcode%5D=7513BK&from%5BpostcodeArea%5D=7513"
            }
        }
    }
    """,
    )


def mock_postal_code(*args, **kwargs):
    """
    This method returns a successful mock response which contains data of a single postal code.
    """
    return MockResponse(
        status_code=200,
        text="""
    {
        "city": {
            "id": "3560",
            "label": "Apeldoorn"
        },
        "geo": {
            "center": {
                "wgs84": {
                    "type": "Point",
                    "coordinates": [
                        5.9497093,
                        52.2256089
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
            "streets": [
                "LOOLAAN"
            ],
            "postcode": "7315 AD"
        },
        "postcode": "7315AD",
        "province": {
            "id": "25",
            "label": "Gelderland"
        },
        "streets": [
            "Loolaan"
        ],
        "municipality": {
            "id": "0200",
            "label": "Apeldoorn"
        },
        "_links": {
            "self": {
                "href": "https://api.postcodeapi.nu/v2/postcodes/7315AD/"
            }
        }
    }
    """,
    )
