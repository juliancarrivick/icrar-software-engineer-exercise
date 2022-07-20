import json


def most_abundant_object_type(objects):
    """
    Returns the plural name of the type of the most abundant object in the
    given list. If there are equal numbers of types, then types will be
    prioritised by: star -> galaxy -> supernovae -> frb
    """
    sum_stars = 0
    sum_galaxies = 0
    sum_supernovae = 0
    sum_frbs = 0
    for o in objects:
        if o['type'] == 'star':
            sum_stars += 1
    for o in objects:
        if o['type'] == 'galaxy':
            sum_galaxies += 1
    for o in objects:
        if o['type'] == 'supernovae':
            sum_supernovae += 1
    for o in objects:
        if o['type'] == 'frb':
            sum_frbs += 1
    if sum_stars >= sum_galaxies and sum_stars >= sum_supernovae and sum_stars >= sum_frbs:
        return 'stars'
    if sum_galaxies >= sum_stars and sum_galaxies >= sum_supernovae and sum_galaxies >= sum_frbs:
        return 'galaxies'
    if sum_supernovae >= sum_stars and sum_supernovae >= sum_galaxies and sum_supernovae >= sum_frbs:
        return 'supernovae'
    if sum_frbs >= sum_stars and sum_frbs >= sum_galaxies and sum_frbs >= sum_supernovae:
        return 'frbs'


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
    observed (larger is further away). If no objects are passed then
    None is returned.
    """
    highest_redshift = None
    for o in objects:
        if highest_redshift is None or o["redshift"] > highest_redshift:
            highest_redshift = o["redshift"]
    for o in objects:
        if o["redshift"] == highest_redshift:
            return o


print(furthest_object(json.loads(input)))
