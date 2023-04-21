
import numpy as np

def sigmoid(x):
	return 1 / (1 + np.exp(-x))
	

class Neuron1:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
    def feedforward (self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)
        
print("Даныне нейросети: \n - три входа (x1, x2, x3)\n "
"- три нейрона в скрытых слоях(h1, h2, h3)\n - выход(О1)")
print("Ответ:")
class OurNeuralNetwork:
    def __init__(self):
        weights = np.array([0.5, 0.5, 0.5]) # Веса
        bias = 0 # Пороги
        self.h1 = Neuron1(weights, bias)
        self.h2 = Neuron1(weights, bias)
        self.h3 = Neuron1(weights, bias)
        self.o1 = Neuron1(weights, bias)
    def feedforward(self, x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)
        out_h3 = self.h3.feedforward(x)
        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2, out_h3]))
        #Два выхода
        return out_o1
    
network = OurNeuralNetwork()
x = np.array ([2, 3, 4])
print(network.feedforward(x), "\n")


print("Даныне нейросети: \n - два входа (x1, x2)\n "
"- два нейрона в скрытых слоях(h1, h2)\n - два выхода(О1, О2)")
print("Ответ:")
class OurNeuralNetwork:
    def __init__(self):
        weights = np.array([1,0])
        bias = 1
        
        self.h1 = Neuron1(weights, bias)
        self.h2 = Neuron1(weights, bias)
        self.o1 = Neuron1(weights, bias)
        self.o2 = Neuron1(weights, bias)
    def feedforward(self, x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)
        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))
        out_o2 = self.o2.feedforward(np.array([out_h1, out_h2]))
        return out_o1, out_o2
    
network = OurNeuralNetwork()
x = np.array ([2, 3])
print (network.feedforward(x))

print("Нейроны имеют идентичные веса и пороги")
print("- w = [1, 0]\n - b = 1")

