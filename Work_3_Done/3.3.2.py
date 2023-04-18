from sklearn.feature_extraction import DictVectorizer

data_dict = [{"green": 4, "blue": 2},
			{"gray": 5, "green": 3},
			{"blue": 2, "gray": 1}]
dictvec = DictVectorizer(sparse = False)
matrix = dictvec.fit_transform(data_dict)
print(matrix)
