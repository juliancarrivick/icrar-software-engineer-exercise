import unittest

from object_analysis import most_abundant_object_type, furthest_object


class TestMostAbundantObjectType(unittest.TestCase):
    object_index = 0

    def test_empty_objects(self):
        # Is this correct behaviour? I would expect since there is nothing,
        # then None would be returned but we don't have enough context to
        # determine if this is correct or not. Then again, there are a lot
        # of stars and this follows the prioritisation of type (even if
        # every thing is 0)
        self.assert_most_abundant('stars', [])

    def test_unknown_object_types_are_ignored(self):
        self.assert_most_abundant("stars", ["unknown", "unknown", "star"])

    def test_missing_type_throws(self):
        self.assertRaises(KeyError, lambda: most_abundant_object_type([{}]))

    def test_mapping_of_return_value(self):
        self.assert_most_abundant("stars", ["star"])
        self.assert_most_abundant("galaxies", ["galaxy"])
        self.assert_most_abundant("supernovae", ["supernovae"])
        self.assert_most_abundant("frbs", ["frb"])

    def test_prioritisation_of_type(self):
        self.assert_most_abundant("stars", ["star", "galaxy"])
        self.assert_most_abundant("stars", ["star", "supernovae"])
        self.assert_most_abundant("stars", ["star", "frbs"])
        self.assert_most_abundant("stars", ["galaxy", "star"])
        self.assert_most_abundant("galaxies", ["galaxy", "supernovae"])
        self.assert_most_abundant("galaxies", ["galaxy", "frbs"])
        self.assert_most_abundant("stars", ["supernovae", "star"])
        self.assert_most_abundant("galaxies", ["supernovae", "galaxy"])
        self.assert_most_abundant("supernovae", ["supernovae", "frb"])
        self.assert_most_abundant("stars", ["frb", "star"])
        self.assert_most_abundant("galaxies", ["frb", "galaxy"])
        self.assert_most_abundant("supernovae", ["frb", "supernovae"])

    def assert_most_abundant(self, expected: str, object_types: list):
        self.assertEqual(expected, most_abundant_object_type(
            [self.create_object(type) for type in object_types]))

    def create_object(self, type: str):
        self.object_index += 1
        return {
            "type": type,
            "name": f"{type}{self.object_index}",
            "redhift": 0,
        }


class TestFurthestObject(unittest.TestCase):
    def test_no_objects(self):
        self.assertEqual(None, furthest_object([]))

    def test_highest_redshift_object_is_returned(self):
        objects = self.create_redshifted_objects(2, 3, 1)
        self.assertIs(objects[1], furthest_object(objects))

    def test_first_instance_of_highest_redshift_is_returned(self):
        objects = self.create_redshifted_objects(1, 2, 2)
        self.assertIs(objects[1], furthest_object(objects))

    def test_missing_redshift_throws(self):
        self.assertRaises(AssertionError, lambda: furthest_object([{}]))

    def create_redshifted_objects(self, *redshifts):
        return [self.create_redshifted_object(r) for r in redshifts]

    def create_redshifted_object(self, redshift: int):
        return {
            "type": "Dummy",
            "name": "Dummy",
            "redshift": redshift,
        }
