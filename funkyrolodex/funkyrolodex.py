#!/usr/local/bin/env python

import re, json
from operator import itemgetter
from .constants import FORMATS



class FunkyRolodex(object):
    """The FunkyRolodex object holds the formats based on which the parser
       normalizes entries of personal information. It is passed a default
       tuple of formats which are simply pairs of regex patterns and keys.
       It also holds a list of dictionaries generated from the sample file
       and a list of indices for possible errors after processing is complete.
    """

    def __init__(self, formats=FORMATS):
        self.formats = formats
        self.entries = []
        self.errors = []


    def map_entry(self, entry):
        """Builds and returns a dict object for a given entry and
        does most of the heavy lifting by iterating through each formats
        and finding a match on the given pattern using regular expressions.
        A set of predefined keys are used to map the elements in proper order"""
        rv = {}
        for frmt in self.formats:
            matched = re.match(frmt.pattern, entry)
            if matched:
                for index, key in enumerate(frmt.keys):
                    if key == 'phonenumber':
                        rv[key] = format_phonenumber(
                            matched.group(index + 1)).strip()
                    else:
                        rv[key] = matched.group(index + 1).strip()
                break
        else:
            rv['error'] = entry

        return rv


    def process_entries(self, file_name):
        """Processes each entry in the input file and append resulting dict
        objects to either the list of entries or the list of errors."""
        with open(file_name, 'r') as in_file:
            for index, record in enumerate(in_file.readlines()):
                entry = self.map_entry(record)
                if 'error' in entry:
                    self.errors.append(index)
                else:
                    self.entries.append(entry)


    def jsonify(self, file_name):
        """Serializes list of entries and list of errors to a JSON
        format after sorting entries in ascending alphabetical order
        by last name and first name."""
        with open(file_name, 'w') as out_file:
            #itemgetter has faster performance
            sorted_entries = sorted(self.entries,
                                    key=itemgetter('lastname', 'firstname'))
            data = {'entries': sorted_entries, 'errors': self.errors}

            json.dump(data, out_file, indent=2, sort_keys=True)


"""
Helper functions
~~~~~~~~~~~~~~~~
"""


def format_phonenumber(number):
    # Using set to take advantage of O(1) in membership testing
    number_set = set(number)
    replace_chars = set()
    if '(' in number_set and ')' in number_set and '-' in number_set:
        for char in ['(', ')', '-']:
            replace_chars.add(char)
    if ' ' in number_set:
        replace_chars.add(' ')

    for char in replace_chars:
        number = number.replace(char, '')
    if len(number) == 10:
        number = '%s-%s-%s' % (number[:3], number[3:6], number[6:])
        return number
    else:
        return 'invalid number'


if __name__ == '__main__':
    parser = FunkyRolodex()
    parser.process_entries('sample-shafayet.in')
    parser.jsonify('result.out')
