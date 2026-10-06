# Problem: Count occurrences and find if an element exists in O(1) time
items = ["apple", "banana", "apple", "orange", "banana", "apple"]

# 1. Building the Hash Map
hash_map = {}
for item in items:
    if item in hash_map:
        hash_map[item] += 1
    else:
        hash_map[item] = 1

print("Frequency Map:", hash_map)
# Output: {'apple': 3, 'banana': 2, 'orange': 1}

# 2. O(1) Instant Lookup (Hashing in action)
target = "banana"
if target in hash_map:
    print(f"'{target}' exists with count {hash_map[target]}")