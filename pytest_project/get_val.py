def get_val(collection=None, key=None, default=None):
    if collection:
      print(collection[key])  
      return collection[key]
    else:
      print(default)
      return default

#get_val({"hello": "world"}, "hello")
#get_val({ "hello": "world" }, "hello", "python")
#get_val({}, "hello", "python")
