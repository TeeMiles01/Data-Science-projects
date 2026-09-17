import numpy as np
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers

tf.random.set_seed(42)
np.random.seed(42)

# Load data
iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = keras.Sequential([
    layers.Input(shape=(4,)),
    layers.Dense(10, activation='relu'),
    layers.Dense(8, activation='relu'),
    layers.Dense(3, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=8,
    validation_split=0.1,
    verbose=0
)

for epoch in [0, 9, 19, 29, 39, 49]:
    print(f"Epoch {epoch+1}: loss={history.history['loss'][epoch]:.4f}, acc={history.history['accuracy'][epoch]:.4f}")

test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"\nTest Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_acc:.4f}")

preds = model.predict(X_test[:5], verbose=0)
pred_classes = np.argmax(preds, axis=1)
print("\nSample predictions:", pred_classes)
print("Actual labels:     ", y_test[:5])
""" The learning process, in brief: Forward propagation pushes each flower's measurements through the weighted connections and ReLU activations '
'layer by layer until softmax outputs three class probabilities. The error is computed by comparing those probabilities to the true label with '
'cross-entropy loss — a single number that's large when the network is confidently wrong. Backpropagation then works backward through the network 
using the chain rule to figure out how much each individual weight contributed to that error (the gradient)."""
