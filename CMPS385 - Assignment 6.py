TABLE_SIZE = 907
hash_table = [None] * TABLE_SIZE
DELETED = "__DELETED__"

def HashInsertion(key):
    for i in range(TABLE_SIZE):
        index = (key % TABLE_SIZE + i) % TABLE_SIZE
        if hash_table[index] is None or hash_table[index] == DELETED:
            hash_table[index] = key
            return 1  # Success
        elif hash_table[index] == key:
            return -1  # Duplicate key
    return -1  # Table full

def HashDeletion(key):
    for i in range(TABLE_SIZE):
        index = (key % TABLE_SIZE + i) % TABLE_SIZE
        if hash_table[index] is None:
            return -1  # Key not found
        elif hash_table[index] == key:
            hash_table[index] = DELETED
            return 1  # Success
    return -1  # Key not found

print(HashInsertion(1000))  # Should print 1
print(HashInsertion(1000))  # Should print -1 (duplicate)
print(HashDeletion(1000))   # Should print 1
print(HashDeletion(1000))   # Should print -1 (already deleted)