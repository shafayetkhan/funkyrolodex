#!/usr/bin/python

import unittest
from funkyrolodex.funkyrolodex import FunkyRolodex, format_phonenumber


class TestFunkyRolodex(unittest.TestCase):
    """Unit testing with given formats"""

    def setUp(self):
        self.parser = FunkyRolodex()

    def tearDown(self):
        pass

    def test_format_A(self):
        """Testing the first format"""
        rv = self.parser.map_entry('Humperdink, Englebert G., (826)-738-4224, gray, 65528')
        result = {'color': 'gray', 'firstname': 'Englebert G.',
                  'lastname': 'Humperdink', 'phonenumber': '826-738-4224', 'zipcode': '65528'}
        self.assertEqual(rv, result)

    def test_format_B(self):
        """Testing the second format"""
        rv = self.parser.map_entry('James Murphy, chrysochlorous greenish gold, 83880, 018 154 6474')
        result = {'color': 'chrysochlorous greenish gold', 'firstname': 'James', 'lastname': 'Murphy',
                  'phonenumber': '018-154-6474', 'zipcode': '83880'}
        self.assertEqual(rv, result)

    def test_format_C(self):
        """Testing the third format"""
        rv = self.parser.map_entry('Booker T., Washington, 87360, 373 781 7380, yellow')
        result = {'color': 'yellow', 'firstname': 'Booker T.', 'lastname': 'Washington',
                  'phonenumber': '373-781-7380', 'zipcode': '87360'}
        self.assertEqual(rv, result)

    def test_format_Error1(self):
        """Testing an invalid entry"""
        rv = self.parser.map_entry('Chandler, Kerri, (623)-668-9293, pink, 123123121')
        result = {'error': 'Chandler, Kerri, (623)-668-9293, pink, 123123121'}
        self.assertEqual(rv, result)

    def test_format_Error2(self):
        rv = self.parser.map_entry('asdfawefawea')
        result = {'error': 'asdfawefawea'}
        self.assertEqual(rv, result)


    def test_invalid_phonenumber(self):
        """Testing an entry with invalid phone number"""
        rv = self.parser.map_entry('James Murphy, chrysochlorous greenish gold, 83880, 018 154 64749')
        result = {'error': 'James Murphy, chrysochlorous greenish gold, 83880, 018 154 64749'}
        self.assertEqual(rv, result)

    def test_format_phonenumber(self):
        """Testing normalization of a few different phone number formats"""
        test_numbers = ('(508)-494-2545', '707 742 3404', '911 529 62349')
        rv = tuple([format_phonenumber(num) for num in test_numbers])
        result = ('508-494-2545', '707-742-3404', 'invalid number')
        self.assertEqual(rv, result)


if __name__ == '__main__':
    unittest.main()
