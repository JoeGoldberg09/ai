import numpy as np

def step_function(x):
    return np.where(x >= 0, 1, 0)


def initialize_parameters(input_size, hidden1_size, hidden2_size, output_size):
    """Initialize weights and biases with random values"""
    weights = {
        "W1": np.random.randn(input_size, hidden1_size),
        "W2": np.random.randn(hidden1_size, hidden2_size),
        "W3": np.random.randn(hidden2_size, output_size),
    }

    biases = {
        "b1": np.random.randn(hidden1_size),
        "b2": np.random.randn(hidden2_size),
        "b3": np.random.randn(output_size),
    }

    return weights, biases


def forward_propagation(X, weights, biases):
    """Forward propagation through the network"""
    # First hidden layer
    Z1 = np.dot(X, weights["W1"]) + biases["b1"]
    A1 = step_function(Z1)

    # Second hidden layer
    Z2 = np.dot(A1, weights["W2"]) + biases["b2"]
    A2 = step_function(Z2)

    # Output layer
    Z3 = np.dot(A2, weights["W3"]) + biases["b3"]
    A3 = step_function(Z3)

    return A3, A2, A1


def predict(X, weights, biases):
    """Make predictions using the current model"""
    output, _, _ = forward_propagation(X, weights, biases)
    return output


# Example usage
input_size = 5  # N binary inputs, can be changed
hidden1_size = 4
hidden2_size = 3
output_size = 1
num_steps = 10

# Initialize parameters
weights, biases = initialize_parameters(
    input_size, hidden1_size, hidden2_size, output_size
)

# Generate some random binary input data
X = np.random.randint(0, 2, size=(1, input_size))  # 10 sample inputs

# Run for specified number of steps
for step in range(num_steps):
    # Generate new random weights and biases for each step
    weights, biases = initialize_parameters(
        input_size, hidden1_size, hidden2_size, output_size
    )

    # Make predictions
    predictions = predict(X, weights, biases)

    print("predictions", predictions)
    print(f"Step {step + 1}")

# Display final weights and biases
print("\nFinal Weight Matrices and Bias Values:")
print("W1 (Input → Hidden Layer 1):")
print(weights["W1"])
print("\nBias b1:")
print(biases["b1"])
print("\nW2 (Hidden Layer 1 → Hidden Layer 2):")
print(weights["W2"])
print("\nBias b2:")
print(biases["b2"])
print("\nW3 (Hidden Layer 2 → Output):")
print(weights["W3"])
print("\nBias b3:")
print(biases["b3"])
print("\nNumber of Steps:", num_steps)
