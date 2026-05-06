# Dictionary ---- work in pairs
# contain key:value pairs
# unordered, mutable, don't allow duplicate keys

# string, list, tuple ---> ordered (contain indexes)
# dict ----> unordered


# list and dict --> mutable
# tuple --> immutable


dict = {
  "key":"value",
  "name":"Sarah",
  "subjects":["python","c++","java"],
  "marks":(78,90,99,70,67),
  "learning":"python",
  "age":22,
  "is_Adult":True,
  # 120:50,
}
print(dict)
print(type(dict))
print(dict["name"])
print(dict["age"])
print(dict["marks"])

dict["name"]="Amirah"
dict["cgpa"]=4.0

# overwrite old name key
# dict["name"]=20
print(dict)


null_dict = {}
null_dict["semester"]="6th"
print(null_dict)