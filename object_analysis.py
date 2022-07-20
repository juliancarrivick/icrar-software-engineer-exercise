import json
from collections import OrderedDict


def most_abundant_object_type(objects):
    """
    Returns the plural name of the type of the most abundant object in the
    given list. If there are equal numbers of types, then types will be
    prioritised by: star -> galaxy -> supernovae -> frb
    """
    # OrderedDict uses a little more memory and may not be faster than just
    # having a list with our four known types. Benchmarking may be required
    # in future, but we're not too concerned with performance right now -
    # especially since we're using Python!
    types = OrderedDict()
    types["frb"] = {"count": 0, "plural": "frbs"}
    types["supernovae"] = {"count": 0, "plural": "supernovae"}
    types["galaxy"] = {"count": 0, "plural": "galaxies"}
    types["star"] = {"count": 0, "plural": "stars"}

    for o in objects:
        if o["type"] in types:
            types[o["type"]]["count"] += 1

    most_abundant_type = None
    for type in types.values():
        # Use >= since later entries in the types dict have greater prioritisation
        # over earlier ones if they have equal counts
        if most_abundant_type is None or type["count"] >= most_abundant_type["count"]:
            most_abundant_type = type

    return most_abundant_type["plural"]


input = """
[
    {
        "type": "star",
        "name": "alpha-centaurus",
        "redshift": 0
    },
    {
        "type": "nebula",
        "name": "crab",
        "redshift": 0
    },
    {
        "type": "galaxy",
        "name": "sombrero",
        "redshift": 0
    }
]
"""

print(most_abundant_object_type(json.loads(input)))


def furthest_object(objects):
    """
    Returns the furthest object as determined by the amount of redshift
    observed (larger is further away). If a single object is passed then it
    is returned. If no objects are passed then None is returned.
    """
    furthest_object = None
    for o in objects:
        # If we have a single element in the list that doesn't have a redshift
        # property then it will automatically becomes the furthest object
        # (which makes no sense). So force this check to ensure our objects are
        # valid
        assert "redshift" in o

        if furthest_object is None or o["redshift"] > furthest_object["redshift"]:
            furthest_object = o

    return furthest_object


print(furthest_object(json.loads(input)))
