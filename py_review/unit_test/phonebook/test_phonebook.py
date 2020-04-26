# $ python3 -m unittest <file-name-or-nothing>

import unittest
from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = PhoneBook()

    # This method is great to set something like write in files or database
    # def tearDown(self):
    #     pass

    def test_lookup_by_name(self):
        self.phonebook.add('Luis', '12345')
        number = self.phonebook.lookup('Luis')
        self.assertEqual('12345', number)

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')

    # @unittest.skip("WIP") -> to skip test
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add('Luis', '12345')
        self.phonebook.add('Vilella', '0012345')
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_entries(self):
        self.phonebook.add('Luis', '12345')
        self.phonebook.add('Felipe', '12345')
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add('Luis', '12345')
        self.phonebook.add('Felipe', '123')
        self.assertFalse(self.phonebook.is_consistent())
