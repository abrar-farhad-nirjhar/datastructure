import time


class Hashmap:
    def __init__(self):
        self.dictionary = []

    def _find_partition(self, key):
        working_dict = self.dictionary
        for char in key:
            ascii_val = ord(char.upper()) - ord('A') + 1
            for i in range(len(working_dict), ascii_val+1):
                working_dict.append([None])
            working_dict = working_dict[ascii_val]
        return working_dict


    def insert_item(self, key, value):
        partition = self._find_partition(key)
        partition[0] = value

    def retrieve_item(self, key):
        partition = self._find_partition(key)
        return partition[0]

    def remove_item(self, key):
        partition = self._find_partition(key)
        partition[0] = None
    

        

start = time.perf_counter()

d = Hashmap()

d.insert_item("a","a")

d.insert_item("c","c")
d.insert_item("ab","ab")
d.insert_item("aa", "aa")
d.insert_item("prbyfpyvdbiprzwldjhwabzmvvkrfdex", "prbyfpyvdbiprzwldjhwabzmvvkrfdex")

print(d.retrieve_item("a"))
print(d.retrieve_item("c"))
print(d.retrieve_item("ab"))
print(d.retrieve_item("aa"))
print(d.retrieve_item("prbyfpyvdbiprzwldjhwabzmvvkrfdex"))

end = time.perf_counter()

print(end-start)

start = time.perf_counter()

d = dict()

d["a"] = "a"
d["c"] = "c"
d["ab"] = "ab"
d["aa"] = "aa"
d["prbyfpyvdbiprzwldjhwabzmvvkrfdex"] = "prbyfpyvdbiprzwldjhwabzmvvkrfdex"


print(d["a"])
print(d["c"])
print(d["ab"])
print(d["aa"])
print(d["prbyfpyvdbiprzwldjhwabzmvvkrfdex"])

end = time.perf_counter()

print(end-start)
