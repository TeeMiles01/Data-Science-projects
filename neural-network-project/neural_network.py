import numpy as np

# ---------------------------------------------------------
# 1. XOR DATASET
# ---------------------------------------------------------
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([
    [0],
    [1],
    [1],
    [0]
])


# ---------------------------------------------------------
# 2. NETWORK STRUCTURE
# ---------------------------------------------------------
# Input layer: 2 features
# Hidden layer: 4 neurons
# Output layer: 1 neuron

input_size = 2
hidden_size = 4
output_size = 1

learning_rate = 0.5
epochs = 10000


# ---------------------------------------------------------
# 3. INITIALIZE WEIGHTS AND BIASES
# ---------------------------------------------------------
np.random.seed(42)

W1 = np.random.randn(input_size, hidden_size)
b1 = np.zeros((1, hidden_size))

W2 = np.random.randn(hidden_size, output_size)
b2 = np.zeros((1, output_size))


# ---------------------------------------------------------
# 4. ACTIVATION FUNCTIONS
# ---------------------------------------------------------
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


# ---------------------------------------------------------
# 5. TRAINING
# ---------------------------------------------------------
for epoch in range(epochs):

    # -------------------------
    # FORWARD PASS
    # -------------------------

    # Input -> Hidden Layer
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)

    # Hidden -> Output Layer
    z2 = np.dot(a1, W2) + b2
    a2 = sigmoid(z2)

    # -------------------------
    # LOSS CALCULATION
    # -------------------------

    # Binary cross-entropy loss
    loss = -np.mean(
        y * np.log(a2 + 1e-8)
        + (1 - y) * np.log(1 - a2 + 1e-8)
    )

    # -------------------------
    # BACKPROPAGATION
    # -------------------------

    # Output layer error
    error_output = a2 - y

    # Gradient for W2 and b2
    dW2 = np.dot(a1.T, error_output) / len(X)
    db2 = np.mean(error_output, axis=0, keepdims=True)

    # Hidden layer error
    error_hidden = np.dot(error_output, W2.T)

    # Hidden layer gradient
    delta_hidden = error_hidden * sigmoid_derivative(a1)

    # Gradient for W1 and b1
    dW1 = np.dot(X.T, delta_hidden) / len(X)
    db1 = np.mean(delta_hidden, axis=0, keepdims=True)

    # -------------------------
    # WEIGHT UPDATE
    # -------------------------

    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

    # Print loss periodically
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.6f}")


# ---------------------------------------------------------
# 6. MODEL STRUCTURE
# ---------------------------------------------------------
print("\nModel Structure:")
print("Input Layer:  2 features")
print("Hidden Layer: 4 neurons")
print("Output Layer: 1 neuron")
print("Activation:   Sigmoid")


# ---------------------------------------------------------
# 7. FINAL PREDICTIONS
# ---------------------------------------------------------
print("\nFinal Predictions:")

z1 = np.dot(X, W1) + b1
a1 = sigmoid(z1)

z2 = np.dot(a1, W2) + b2
predictions = sigmoid(z2)

for i in range(len(X)):
    predicted_class = 1 if predictions[i] >= 0.5 else 0

    print(
        f"Input: {X[i]} "
        f"Actual: {y[i][0]} "
        f"Prediction: {predictions[i][0]:.4f} "
        f"Class: {predicted_class}"
    )


# ---------------------------------------------------------
# 8. TEST INPUT
# ---------------------------------------------------------
test_input = np.array([[1, 0]])

hidden = sigmoid(np.dot(test_input, W1) + b1)
output = sigmoid(np.dot(hidden, W2) + b2)

print("\nTest Input:")
print("Input:", test_input[0])
print("Predicted probability:", round(output[0][0], 4))
print("Predicted class:", 1 if output[0][0] >= 0.5 else 0)
