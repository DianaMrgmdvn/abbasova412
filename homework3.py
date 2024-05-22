person = {
    "name": "John",
    "age": 18,
    "last_name": "Johnson",
    "address": {
      "city": "Durand",
      "state": "Michigan(MI)",
      "zip": 48429,
      "street": "Mount Street"
    },
    "phone": "",
    "employees": {
        "company": {
            "name": "Google",
            "address": {
                "city": "",
                "state": "",
            },
        }
    }
  }

result = {}
for key, v in person.items():
    if type(v)==dict:
        for k1, v1 in v.items():
            if type(v1)==dict:
                for k2,v2 in v1.items():
                    if type(v2)==dict:
                        for k2, v3 in v2.items():
                            pass
                    else:
                        result.setdefault(f'{key}.{k1}.{k2}', v2)
            else: 
                result.setdefault(f'{key}.{k1}', v1)
    else:
        result.setdefault(key, v)

# print(result)

def tree_dict(items, parent_k=None):
    result = {}
    
    for key, value in items.items():
        if parent_k is None:
            new_key = f'{key}'
        else:
            new_key = f'{parent_k}.{key}'

        if type(value)==dict:
            r = tree_dict(value, new_key)
            result.update(r)
        else:
            result.setdefault(new_key, value)

    return result


print(
    tree_dict(person)
)