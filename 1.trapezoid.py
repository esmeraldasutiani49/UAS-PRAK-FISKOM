from sklearn.neural_network import MLPClassifier
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**2)*np.exp(-x)

a = 1.0
b = 10.0
n = 10

#Trapezoid
x = np.linspace(a,b,n)
dx = (b-a)/(n-1)

sigma = 0

for i in range (1, n-1):
    sum = sum + f(x)
    
hasil = 0.5*dx*(func(x[0])+2*sigma+func(x[-1]))

print (hasil)

#Database: Gerbang Logika AND
#x = Data, y = Target
x = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 0, 0, 1]

#Training and Classify
clf = MLPClassifier (solver ='lbfgs', alpha=1e-2,
                   hidden_layer_sizes=(10, 5),
                   random_state=1, max_iter=1000,
                   warm_start=True)

clf.fit(x, y)

#Prediksi
print ("Logika AND Metode Artificial Neural Network (ANN)")
print ("Logika = Prediksi")
print ("0 0", clf.predict([[0, 0]]))
print ("0 1", clf.predict([[0, 1]]))
print ("1 0", clf.predict([[1, 0]]))
print ("1 1", clf.predict([[1, 1]]))
