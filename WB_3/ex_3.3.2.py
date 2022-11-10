"""Определите набор признаков человека, по аналогии из РТ 1, – например,
цвет глаз и конвертируйте его в матрицу признаков."""

from sklearn.feature_extraction import DictVectorizer

data_dict = [
    {'пол': 'мужской', 'цвет глаз': 'глубой'},
    {'пол': 'мужской', 'цвет глаз': 'серый'},
    {'пол': 'женский', 'цвет глаз': 'карий'},
    {'пол': 'мужской', 'цвет глаз': 'зеленый'},
    {'пол': 'женский', 'цвет глаз': 'глубой'},
]

dict_vect = DictVectorizer(sparse=False)
features = dict_vect.fit_transform(data_dict)
print(features)
