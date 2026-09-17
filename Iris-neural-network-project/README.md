# Iris Neural Network Classifier

A simple feedforward neural network built with **Keras (TensorFlow)** that classifies flowers in the classic Iris dataset by species, demonstrating forward propagation, loss computation, backpropagation, and weight updates in practice.

## What it does

The script/notebook loads the Iris dataset (150 samples, 4 numeric features, 3 species), splits it into training and test sets, standardizes the features, and trains a small neural network to predict the species from the four measurements.

**Architecture:**
- Input layer: 4 features (sepal length, sepal width, petal length, petal width)
- Hidden layer 1: 10 neurons, ReLU activation
- Hidden layer 2: 8 neurons, ReLU activation
- Output layer: 3 neurons, Softmax activation (one probability per species)

**Training setup:**
- Loss function: Sparse categorical cross-entropy
- Optimizer: Adam
- Epochs: 50
- Batch size: 8

## Files

| File | Description |
|---|---|
| `iris_nn_training.py` | Standalone Python script version |
| `Iris_NN_Training.ipynb` | Jupyter notebook version with markdown explanations and saved outputs |

## Setup

This project requires Python 3.9–3.12 and the following packages:

```bash
pip install tensorflow scikit-learn numpy
```

**Recommended:** use a dedicated virtual environment (venv or conda) rather than installing into your base/system Python, to avoid dependency conflicts:

```bash
conda create -n irisenv python=3.10 -y
conda activate irisenv
pip install tensorflow scikit-learn numpy
```

## Usage

Run the script directly:

```bash
python3 iris_nn_training.py
```

Or open `Iris_NN_Training.ipynb` in Jupyter, JupyterLab, VS Code, or [Google Colab](https://colab.research.google.com) and run all cells.

## Example output

```
Epoch 1: loss=1.1865, acc=0.2315
Epoch 10: loss=0.8836, acc=0.8333
Epoch 20: loss=0.6391, acc=0.8426
Epoch 30: loss=0.4443, acc=0.8704
Epoch 40: loss=0.3380, acc=0.8796
Epoch 50: loss=0.2386, acc=0.9167

Test Loss: 0.3166
Test Accuracy: 0.8333

Sample predictions: [0 2 1 1 0]
Actual labels:      [0 2 1 1 0]
```

> **Note:** Exact numbers will vary slightly between runs and machines due to random weight initialization, the train/test split, and differences in TensorFlow versions or hardware — this is normal for neural network training. Results in the 80–97% test accuracy range are typical for this dataset and architecture.

## How the network learns

1. **Forward propagation** — Each flower's four measurements pass through the network's weighted connections and ReLU activations, layer by layer, until the output layer produces three raw scores that softmax converts into class probabilities.
2. **Error computation** — The predicted probabilities are compared to the true species label using cross-entropy loss, producing a single number that is large when the prediction is confidently wrong and small when it's close to correct.
3. **Backpropagation** — Working backward from the loss, the network uses the chain rule to compute the gradient: how much each individual weight in every layer contributed to the error.
4. **Weight updates** — The Adam optimizer nudges each weight slightly in the direction that reduces the loss, scaled by a learning rate. Repeating this forward/backward cycle over many epochs gradually tunes the weights so predictions get closer to the true labels.

## License

For educational use.
