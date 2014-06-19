#/usr/local/bin/env python

"""
    funkyrolodex.constants
    ~~~~~~~~~~~~~~~~~~~~~~

    constants.py contains a tuple of formats which uses namedtuple's
    named fields for explicit access to the regex pattern and keys.
    Funkyrolodex is extensible in this way as new formats can be
    added to the list.
"""

from collections import namedtuple

Couple = namedtuple('Couple', 'keys pattern')


FORMATS = (
    Couple(('lastname', 'firstname', 'phonenumber', 'color', 'zipcode'),
           r'^([a-zA-Z. ]*?),\s([a-zA-Z. ]*?),\s(\(\d{3}\)-\d{3}-\d{4}),\s([a-zA-Z ]*?),\s(\d{5})$'),
    Couple(('firstname', 'lastname', 'color', 'zipcode', 'phonenumber'),
           r'^([a-zA-Z. ]*?)\s([a-zA-Z. ]*?),\s([a-zA-Z ]*?),\s(\d{5}),\s(\d{3}\s\d{3}\s\d{4})$'),
    Couple(('firstname', 'lastname', 'zipcode', 'phonenumber', 'color'),
            r'^([a-zA-Z. ]*?),\s([a-zA-Z. ]*?),\s(\d{5}),\s(\d{3}\s\d{3}\s\d{4}),\s([a-zA-Z ]*?)$')
)
