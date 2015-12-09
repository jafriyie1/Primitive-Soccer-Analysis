"""Machine Learning Module"""
import pandas 
from sklearn import cross_validation as cv 
from sklearn import metrics 
from sklearn.ensemble import RandomForestClassifier
import numpy as np

def random_forest(x):
	"""This function is the main component of the soc_learn module"""
	#Preprocessing of Data
	data = pandas.read_csv(x)
	data = data.fillna(0)
	data = data.applymap(lambda x: np.nan if isinstance(x, basestring) and x.isspace() else x)
	data = data.drop(data.columns[[0,1]], axis=1)
	#Splitting Data into respective sets and targets
	(train_data, test_data, train_target, test_target) = cv.train_test_split(data, data['Goals'], test_size=0.2)
	#Random Forest Regressor
	forest = RandomForestClassifier(n_estimators=2000)
	forest = forest.fit(train_data, train_target)
	pred = forest.predict(test_data)
	score = metrics.mean_squared_error(pred, test_target)
	#Prints the mean score error (or number of goals) for number of goals
	return score

