from peewee import *

db = SqliteDatabase('mydatabase.db')

class BaseModel(Model):
    class Meta:
        database = db

class Item(BaseModel):
    name = CharField()
    description = TextField()

db.connect()
db.create_tables([Item])
