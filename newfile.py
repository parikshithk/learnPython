'''Throughout this interview, we'll pretend we're building a new analytical database. Don't worry about actually building a database though -- these will all be toy problems.
Here's how the database works: all records are represented as maps, with string keys and integer values. The records are contained in an array, in no particular order.
To begin with, the database will support just one function: min_by_key. This function scans the array of records and returns the record that has the minimum value for a specified key. Records that do not contain the specified key are considered to have value 0 for the key. Note that keys may map to negative values!
Here's an example use case: each of your records contains data about a school student. You can use min_by_key to answer questions such as "who is the youngest student?" and "who is the student with the lowest grade-point average?"
Implementation notes
You should handle an empty array of records in an idiomatic way in your language of choice.
If several records share the same minimum value for the chosen key, you may return any of them.'''

[{"key": 0, "key1": -1, "key3": 4}, {"key": 0, "key1": 8, "key3": 4}, ]


# min_by_key return min value - {"key": 0, "key1": -1, "key3": 4}

def min_by_key(records, searchKey: str):
    print(records)
    min = 999
    index = 0
    if not records:
        return None
    for i, record in enumerate(records):
        for key, value in record.items():
            print(key, value)
            if key == searchKey:
                if value < min:
                    min = value
                    index = i
    return records[index]


def first_by_key(records, searchKey: str, sort_order: str):
    if sort_order == 'asc':
        min = float('inf')
        index = 0
        if not records:
            return None
        for i, record in enumerate(records):
            for key, value in record.items():
                print(key, value)
                if key == searchKey:
                    if value < min:
                        min = value
                        index = i
        return records[index]
    max = float('-inf')
    index = 0
    if not records:
        return None
    for i, record in enumerate(records):
        for key, value in record.items():
            print(key, value)
            if key == searchKey:
                if value > max:
                    max = value
                    index = i
    return records[index]


def new_min_by_key(records, searchKey: str):
    return first_by_key(records, searchKey, "desc")


print(new_min_by_key([{"key": 100000}, {"key": 100}], "key"))
