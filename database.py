from peewee import *


db = SqliteDatabase('test.db')


class Base(Model):
	class Meta:
		database = db


class Record(Base):
	weekday = SmallIntegerField()
	monthday = SmallIntegerField()
	special = SmallIntegerField()
	result = SmallIntegerField()


def initialize_db():
	db.connect()
	db.create_tables([Record], safe=True)


def close_db():
	db.close()
