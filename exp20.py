import numpy as np


# ReLU activation function and its derivative
def relu(x):
    return np.maximum(0, x)


def relu_derivative(x):
    return (x > 0).astype(float)


# Sigmoid activation for final output
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


# Initialize weights
def initialize_weights(input_size, hidden1_size, hidden2_size, output_size):
    np.random.seed(42)
    w1 = np.random.randn(input_size, hidden1_size) * np.sqrt(2.0 / input_size)
    b1 = np.zeros((1, hidden1_size))
    w2 = np.random.randn(hidden1_size, hidden2_size) * np.sqrt(2.0 / hidden1_size)
    b2 = np.zeros((1, hidden2_size))
    w3 = np.random.randn(hidden2_size, output_size) * np.sqrt(2.0 / hidden2_size)
    b3 = np.zeros((1, output_size))
    return w1, b1, w2, b2, w3, b3


# Forward pass
def forward_pass(X, w1, b1, w2, b2, w3, b3):
    z1 = np.dot(X, w1) + b1
    a1 = relu(z1)
    z2 = np.dot(a1, w2) + b2
    a2 = relu(z2)
    z3 = np.dot(a2, w3) + b3
    output = sigmoid(z3)  # Output is binary, so use Sigmoid
    return z1, a1, z2, a2, z3, output


# Backward pass
def backward_pass(X, y, z1, a1, z2, a2, z3, output, w1, w2, w3, b1, b2, b3, lr):
    m = X.shape[0]

    dz3 = (output - y) * sigmoid_derivative(output)
    dw3 = np.dot(a2.T, dz3) / m
    db3 = np.sum(dz3, axis=0, keepdims=True) / m

    dz2 = np.dot(dz3, w3.T) * relu_derivative(z2)
    dw2 = np.dot(a1.T, dz2) / m
    db2 = np.sum(dz2, axis=0, keepdims=True) / m

    dz1 = np.dot(dz2, w2.T) * relu_derivative(z1)
    dw1 = np.dot(X.T, dz1) / m
    db1 = np.sum(dz1, axis=0, keepdims=True) / m

    w3 -= lr * dw3
    b3 -= lr * db3
    w2 -= lr * dw2
    b2 -= lr * db2
    w1 -= lr * dw1
    b1 -= lr * db1

    return w1, b1, w2, b2, w3, b3


# Training function
def train(X, y, input_size, hidden1_size, hidden2_size, output_size, epochs, lr):
    w1, b1, w2, b2, w3, b3 = initialize_weights(
        input_size, hidden1_size, hidden2_size, output_size
    )

    for epoch in range(epochs):
        z1, a1, z2, a2, z3, output = forward_pass(X, w1, b1, w2, b2, w3, b3)
        w1, b1, w2, b2, w3, b3 = backward_pass(
            X, y, z1, a1, z2, a2, z3, output, w1, w2, w3, b1, b2, b3, lr
        )

        if epoch % 1000 == 0:
            loss = np.mean((y - output) ** 2)
            print(f"Epoch {epoch}, Loss: {loss}")

    return w1, b1, w2, b2, w3, b3


# Example usage:

# Binary input dataset (e.g., XOR)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Output for XOR
y = np.array([[0], [1], [1], [0]])

# Parameters
input_size = 2
hidden1_size = 4
hidden2_size = 4
output_size = 1
epochs = 10000
learning_rate = 0.01

# Train
w1, b1, w2, b2, w3, b3 = train(
    X, y, input_size, hidden1_size, hidden2_size, output_size, epochs, learning_rate
)

# Final predictions
_, _, _, _, _, final_output = forward_pass(X, w1, b1, w2, b2, w3, b3)
print("Final Output after training:")
print(final_output)
