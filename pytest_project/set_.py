
def set_(coll, path, value):
  item = coll
  for key in path[:-1]:
    if key in item:
      item = item[key]
    else:
      item[key] = {}
      item = item[key]
  item[path[-1]] = value
  return coll

  
  #if len(path) == 1:
   # coll[path[0]] = value
   # return coll

  #if path[0] not in coll: 
    #coll[path[0]] = {}

  #set_(coll[path[0]], path[1:], value)

coll = {"a": {"b": {"c":3}}}
set_(coll, ["a", "b", "c"], 4)
print(coll["a"]["b"]["c"])

#4
set_(coll, ["x", "y", "z"], 5)
print(coll["x"]["y"]["z"])
print(coll)
#5
