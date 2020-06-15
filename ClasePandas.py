import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('car.csv', header=None)
data.columns = ['price', 'maintenance', 'n_doors', 'capacity', 'size_lug', 'safety', 'class']


#print(data.head(5))
#print(data.sample(5))
#print(data.tail(5))
#print(data.shape)
#print(data.size)
#print(data["safety"].head)
#print(data["price"][0:3])
#print(data[["price", "Number of doors", "decision"]][0:5])
#print(data[["price", "Number of doors", "decision"]].sample(5))
#print(data["decision"].value_counts())
#print(data["decision"].value_counts().sort_index(ascending=True))
#Var=data["decision"].value_counts()
#print(Var)
#Var.plot(kind="bar")
#plt.show()                   # Display the plot
#print(data["price"].unique())  #me dice los valores que toma el campo, sin repetir
#data["price"].replace(('vhigh','high','med','low'), (4,3,2,1), inplace=True) #reemplazo string por valores
#print(data["price"].unique())
#print(data.head(5))

#miPrice = data["price"].value_counts()
#colors = ["#DDEE01", "#CC0101", "#FE10D1", "#BCC922"]
#miPrice.plot(kind="bar", color=colors)
#plt.xlabel("Precio")
#plt.ylabel("Autos")
#plt.title("Precio Autos")
#plt.show()

#labels=["caramelos", "chupetines", "anteojos"]
#size=[15,65,46]  
#colors=["yellow", "green", "blue"]
#explode=[0.08,0.08,0.08]
#plt.pie(size, labels=labels, explode=explode, colors=colors, shadow=True, autopct="%.2f%%")
#plt.legend(loc="best")
#plt.show()



data["price"].replace(('vhigh','high','med','low'), (4,3,2,1), inplace=True) #reemplazo string por valores
data["maintenance"].replace(('vhigh','high','med','low'), (4,3,2,1), inplace=True) 
data["n_doors"].replace(('2','3','4','5more'), (1,2,3,4), inplace=True) 
data["capacity"].replace(('2','4','more'), (1,2,3), inplace=True) 
data["size_lug"].replace(('small','med','big'), (1,2,3), inplace=True)
data.safety.replace(('low','med','high'), (1,2,3), inplace=True) #Esta es otra forma de hacer "replace"

data["class"].replace(("unacc", "acc", "good", "vgood"), (1,2,3,4), inplace=True)

print(data["price"].size) #la muestra tiene 1728 filas

dataset = data.values
X = dataset[:, 0:6]
Y = np.asarray(dataset[:,6], dtype = "S6")

from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score 
from sklearn import metrics

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, random_state=0)
tr = tree.DecisionTreeClassifier(max_depth=10)
tr.fit(X_train, Y_train)

score = tr.score(X_test, Y_test)
#print("Precision: %0.4f" % (score))

y_pred = tr.predict(X_test)
#print(y_pred)

#print(data.tail(10))
#print(data.head(10))

#miPrice = data["price"].value_counts()
#colors = ["#DDEE01", "#CC0101", "#FE10D1", "#BCC922"]
#miPrice.plot(kind="bar", color=colors)
limite_inferior = 1728*0.9
clase = data["class"][1555:1728]

plt.figure()
plt.subplot(211)
plt.plot(clase)

plt.subplot(212)
plt.plot(y_pred)
plt.show()

#miPrice.plot(kind="bar", color=colors)
#plt.ylabel("Autos")
#plt.title("Precio Autos")
