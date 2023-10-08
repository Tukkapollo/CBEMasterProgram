from numpy import exp, array, random, dot
from flask import Flask

app = Flask(__name__)

@app.route("/redcolor/<float:red>/<float:green>/<float:blue>")
def hello(red, green, blue):
	result= think(array([float(red),float(green),float(blue)]))
	return {"result": result[0]}

random.seed(1)

# 3 inputs, one output neural node
synaptic_weights = 2 * random.random((3, 1)) - 1

# Sigmoid (activation function)
def sigmoid(x):
    return 1 / (1 + exp(-x))

# Derivative of the Sigmoid function, used to adjust error
def sigmoid_derivative(x):
    return x * (1 - x)

# Training the Neural net with a set of inputs with known outputs
def train(train_inputs, train_outputs, iterations):
    global synaptic_weights
    for iteration in range(iterations):
        output = think(train_inputs) # training: multiply the weights with the inputs
        error = train_outputs - output # see what the error is
        adjustment = dot(train_inputs.T, error * sigmoid_derivative(output)) # calculate the adjustments
        synaptic_weights = synaptic_weights + adjustment # modify the weights with these adjustments

# Tinking: multiply inputs with weights
def think(inputs):
    return sigmoid(dot(inputs, synaptic_weights))

# Training data
train_inputs = array([[0.9, 0.1, 0.1], [0.1, 0.6, 0.2], [0.4, 0.1, 0.1], [0.6, 0.8, 0.1], [0.1, 0.1, 0.9]])
train_outputs = array([[1, 0, 1, 0, 0]]).T

train(train_inputs, train_outputs, 10000)
