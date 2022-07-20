import sys
import json

from object_analysis import furthest_object, most_abundant_object_type

# Usage `python3 example.py [sample.json]`

file_path = sys.argv[1] if len(sys.argv) > 1 else "sample.json"
with open(file_path) as file:
    sample_json = json.load(file)

    print("Most abundant object type:")
    print(most_abundant_object_type(sample_json))

    print("Furthest object:")
    print(furthest_object(sample_json))
