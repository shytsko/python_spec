import json
from pprint import pprint

# with open("users.json", 'r', encoding='utf-8') as data_file:
#     data = json.load(data_file)

# pprint(data)
#
# with open("users.json", 'r', encoding='utf-8') as data_file:
#     data_text = data_file.read()
#
# data = json.loads(data_text)
# pprint(data)

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование",
                "путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}

with open("new.json", 'w', encoding='utf-8') as f:
    json.dump(my_dict, f)

with open("new2.json", 'w', encoding='utf-8') as f:
    json.dump(my_dict, f, ensure_ascii=False)

json_text = json.dumps(my_dict)
pprint(json_text)

json_text = json.dumps(my_dict, ensure_ascii=False)
pprint(json_text)


