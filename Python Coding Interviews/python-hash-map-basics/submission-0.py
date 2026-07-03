from typing import List, Dict


def build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]:
    return dict(zip(keys, values))

# assume all keys in the list exist in the hashmap
# order of the values in the output list should match the order of the keys in the input list
def get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]:
    output_list = []
    for key, value in hash_map.items():
        if key in keys:
            output_list.append(value)
    return output_list


# do not modify below this line
print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(build_hash_map(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(build_hash_map(["Doug", "Bob", "Tommy"], [80, 90, 100]))

print(get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"]))
print(get_values({"Jane": 25, "Charlie": 60, "Carol": 100, }, ["Jane", "Carol"]))
print(get_values({"X": 205, "Y": 78, "Z": 100}, ["Y"]))
