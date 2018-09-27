from db_table import db_table
users = db_table("test", { "id": "integer PRIMARY KEY", "name": "text", "email": "text NOT NULL UNIQUE" })
users.insert({"name": "Jean Dujardin", "email": "jean.dujardin@whova.com"})
users.insert({"name": "Rene Coti", "email": "rene.coti@whova.com"})
users.insert({"name": "Francis Lalane", "email": "francis.lalane@whova.com"})
print(users.select())
users.update({'name': 'John'}, {'id':2})
users.select(['name', 'email'], {'id': 2})
users.close()