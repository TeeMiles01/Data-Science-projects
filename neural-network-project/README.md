# Basic Neural Network with NumPy

## Project Overview

This project implements a simple neural network from scratch using Python and NumPy.

The purpose of the project is to understand the basic components of a neural network and how it learns through training. The network demonstrates a forward pass, loss calculation, backpropagation, and weight updates.

## Objective

The goal is to build and train a basic neural network that can solve a binary classification problem.

The network includes:

- 2 input features
- 1 hidden layer with 4 neurons
- 1 output neuron
- Sigmoid activation function
- Backpropagation for training
- Binary cross-entropy loss

## Dataset

The project uses the XOR (Exclusive OR) dataset.

| Input 1 | Input 2 | Expected Output |
|--------:|--------:|----------------:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

The XOR dataset is a useful example for demonstrating a neural network because the output depends on the combination of both input features.

## Neural Network Architecture

```text
Input Layer
2 Features
    |
    v
Hidden Layer
4 Neurons
    |
    v
Output Layer
1 Neuron

The network uses the following structure:

2 Inputs → 4 Hidden Neurons → 1 Output
How the Network Works
1. Forward Pass

The input data is passed through the network.

The input is multiplied by the weights and added to the biases:

z1 = np.dot(X, W1) + b1

The sigmoid activation function is then applied:

a1 = sigmoid(z1)

The hidden layer output is passed to the output neuron:

z2 = np.dot(a1, W2) + b2
a2 = sigmoid(z2)

The output represents the predicted probability of the positive class.

2. Loss Calculation

Binary cross-entropy is used to measure the difference between the predicted values and the actual values.

The goal during training is to reduce the loss.

3. Backpropagation

After calculating the loss, the network calculates the error and determines how the weights contributed to that error.

The gradients are calculated and used to update the weights.

4. Weight Updates

The weights are adjusted using the learning rate:

W2 -= learning_rate * dW2
W1 -= learning_rate * dW1

This process is repeated for multiple epochs so that the network can improve its predictions.

Training Results

The model was trained for 10,000 epochs.

The loss decreased during training:

Epoch	Loss
0	0.762777
1,000	0.093909
2,000	0.014728
3,000	0.006595
4,000	0.004031
5,000	0.002847
6,000	0.002180
7,000	0.001757
8,000	0.001467
9,000	0.001257

The reduction in loss shows that the neural network learned the XOR pattern during training.

Final Predictions

After training, the model produced the following predictions:

Input	Actual	Predicted Probability	Predicted Class
[0, 0]	0	0.0005	0
[0, 1]	1	0.9991	1
[1, 0]	1	0.9986	1
[1, 1]	0	0.0016	0

The model correctly classified all four XOR examples.

For an additional test input:

[1, 0]

the model produced:

Predicted probability: 0.9986
Predicted class: 1
Requirements
Python 3
NumPy
Installation

Clone the repository:

git clone https://github.com/YOUR-USERNAME/neural-network-project.git

Navigate into the project folder:

cd neural-network-project

Install NumPy:

python3 -m pip install numpy
Running the Program

Run the Python program with:

python3 neural_network.py

The program will display:

Training loss across epochs
Neural network structure
Final predictions
Test input prediction
Files
neural-network-project/
│
├── neural_network.py
└── README.md
Technologies Used
Python
NumPy
Neural Networks
Backpropagation
Binary Classification
Learning Outcomes

This project demonstrates an understanding of:

Neural network architecture
Forward propagation
Activation functions
Loss functions
Backpropagation
Gradient-based weight updates
Model training
Binary classification
Conclusion

This project demonstrates how a basic neural network can learn a binary classification problem using only Python and NumPy.

By implementing the forward pass, loss calculation, backpropagation, and weight updates manually, the project provides a practical understanding of how neural networks learn from data.
