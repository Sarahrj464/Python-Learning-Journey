# nested dictionaries
# value ku dictionary bna skty

student = {
  "name":"Sarah",
  "subjects":{
    "phy":78,
    "chem":88,
    "math":99
  }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])