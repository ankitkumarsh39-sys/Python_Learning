#dictionary is mutable and unordered collection of key value pairs
"""info ={
    "name": "Dictionary",
    "type": "mutable",
    "order": "unordered",
    "indexed": "yes",
    "duplicate": "no",
}
print(info)
print(info["name"])
info["name"] = "Ankit"
print(info["name"])"""


student = {
    "name": "Ankit",
    "info": {
        "age": 22,
        "course": "Python"
    }
}
print(student)
print(student["info"] ["course"])

#Methods in dictionary
"""print(student.keys())#key is a method which will return all the keys in the dictionary
print(list(student.keys())) #to convert to list and print keys
print(len(student))"""
print(student.values())
print(list(student.items()))
print(student.get("name"))
student.update({"city": "Ambala"})
print(student)
