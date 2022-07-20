import unittest

from object_analysis import aboundant, farthest


class TestAboundant(unittest.TestCase):
    object_index = 0

    def test_empty_objects(self):
        # Is this correct behaviour? I would expect since there is nothing,
        # then None would be returned but we don't have enough context to
        # determine if this is correct or not. Then again, there are a lot
        # of stars and this follows the prioritisation of type (even if
        # every thing is 0)
        self.assert_aboundant('stars', [])

    def test_unknown_object_types_are_ignored(self):
        self.assert_aboundant("stars", ["unknown", "unknown", "star"])

    def test_missing_type_throws(self):
        self.assertRaises(KeyError, lambda: aboundant([{}]))

    def test_mapping_of_return_value(self):
        self.assert_aboundant("stars", ["star"])
        self.assert_aboundant("galaxies", ["galaxy"])
        self.assert_aboundant("supernovae", ["supernovae"])
        self.assert_aboundant("frbs", ["frb"])

    def test_prioritisation_of_type(self):
        self.assert_aboundant("stars", ["star", "galaxy"])
        self.assert_aboundant("stars", ["star", "supernovae"])
        self.assert_aboundant("stars", ["star", "frbs"])
        self.assert_aboundant("stars", ["galaxy", "star"])
        self.assert_aboundant("galaxies", ["galaxy", "supernovae"])
        self.assert_aboundant("galaxies", ["galaxy", "frbs"])
        self.assert_aboundant("stars", ["supernovae", "star"])
        self.assert_aboundant("galaxies", ["supernovae", "galaxy"])
        self.assert_aboundant("supernovae", ["supernovae", "frb"])
        self.assert_aboundant("stars", ["frb", "star"])
        self.assert_aboundant("galaxies", ["frb", "galaxy"])
        self.assert_aboundant("supernovae", ["frb", "supernovae"])

    def assert_aboundant(self, expected: str, object_types: list):
        self.assertEqual(expected, aboundant(
            [self.create_object(type) for type in object_types]))

    def create_object(self, type: str):
        self.object_index += 1
        return {
            "type": type,
            "name": f"{type}{self.object_index}",
            "redhift": 0,
        }


class TestFarthest(unittest.TestCase):
    def test_no_objects(self):
        self.assertEqual(None, farthest([]))

    def test_highest_redshift_object_is_returned(self):
        objects = self.create_redshifted_objects(2, 3, 1)
        self.assertIs(objects[1], farthest(objects))

    def test_first_instance_of_highest_redshift_is_returned(self):
        objects = self.create_redshifted_objects(1, 2, 2)
        self.assertIs(objects[1], farthest(objects))

    def test_missing_redshift_throws(self):
        self.assertRaises(KeyError, lambda: farthest([{}]))

    def create_redshifted_objects(self, *redshifts):
        return [self.create_redshifted_object(r) for r in redshifts]

    def create_redshifted_object(self, redshift: int):
        return {
            "type": "Dummy",
            "name": "Dummy",
            "redshift": redshift,
        }
