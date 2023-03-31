import sys
import pickle
import implicit
from operator import itemgetter

with open("src\\model.pkl", "rb") as f:
    model = pickle.load(f)
with open("src\\title_encode.pkl", "rb") as f:
    title_encode = pickle.load(f)
with open("src\\title_decode.pkl", "rb") as f:
    title_decode = pickle.load(f)
artist = input("Исполнитель: ")
if title_encode.get(artist) == None:
    print('Такого исполнителя нет')
else:
    ids,scores = model.similar_items(title_encode.get(artist)-1, N = 5, filter_items = [title_encode.get(artist)-1])
    print("Похожие исполнители:",", ".join(itemgetter(*(ids+1))(title_decode)))
