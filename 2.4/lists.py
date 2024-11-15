users = [{"name": "Kamil", "country": "Poland"}, {"name": "John", "country": "USA"}, {"name": "Yeti"}]

usersFromPoland = [x for x in users if 'country' in x and x['country'] == "Poland"]

print(usersFromPoland)
