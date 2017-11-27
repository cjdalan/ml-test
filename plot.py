import numpy as np
from database import Record


def get_training_data():
	x_train = []
	y_train = []

	for record in Record.select():
		x_train.append(
			[record.weekday, record.monthday, record.special])
		y_train.append(record.result)

	return (np.array(x_train), y_train)

def dist(x, y):
	return np.sqrt(np.sum((x - y) ** 2))


def get_result(weekday, monthday, special):
	x_test = [weekday, monthday, special]
	x_train, y_train = get_training_data()

	num = len(x_train)
	distance = np.zeros(num)

	for i in range(num):
		distance[i] = dist(x_train[i], x_test)

	min_index = np.argmin(distance)

	if y_train[min_index] == 1:
		return True
	return False


