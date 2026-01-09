import csv
from sklearn.neural_network import MLPClassifier

x = []
y = []

cesta = "3. strojove_uceni\data/bmi.csv"
with open(cesta, "r", encoding="utf-8") as file:
    for line in csv.DictReader(file):
        y.append(int(line["Index"]))
        
        if line["Gender"] == "Female":
            gender = 0
        else:
            gender = 100
            
        height = int(line["Height"])
        weight = int(line["Weight"])
        
        x.append([gender, height, weight])
        
        
        x_train = x[:round(0.8*len(x))]
        y_train = y[:round(0.8*len(y))]
        
        x_test = x[round(0.8*len(x)):]
        y_test = y[round(0.8*len(y)):]
        
        
        
neuronka = MLPClassifier(
    hidden_layer_sizes=(18, 16),
    activation = "relu",
    max_iter=50_000)

neuronka.fit(x_train,y_train)

predikce = neuronka.predict(x_test)
pocet= len(predikce)

spravne = 0
for i in range(pocet):
    if predikce[i] == y_test[i]:
        spravne +=1
        
print(f"Pomer spravne spatne: {spravne} / {pocet} = {spravne / pocet*100}%")
