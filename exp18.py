import numpy as np


def step_function(x):
    """Simple step function that returns 1 if x >= 0, otherwise 0"""
    return np.where(x >= 0, 1, 0)


def initialize_parameters(input_size, hidden_size, output_size):
    """Initialize weights and biases with random values"""
    weights = {
        "W1": np.random.randn(input_size, hidden_size),  # Input to hidden
        "W2": np.random.randn(hidden_size, output_size),  # Hidden to output
    }

    biases = {
        "b1": np.random.randn(hidden_size),  # Hidden layer bias
        "b2": np.random.randn(output_size),  # Output layer bias
    }

    return weights, biases


def forward_propagation(X, weights, biases):
    """Forward propagation through the network"""
    # Hidden layer
    Z1 = np.dot(X, weights["W1"]) + biases["b1"]
    A1 = step_function(Z1)

    # Output layer
    Z2 = np.dot(A1, weights["W2"]) + biases["b2"]
    A2 = step_function(Z2)

    return A2, A1


def predict(X, weights, biases):
    """Make predictions using the current model"""
    output, _ = forward_propagation(X, weights, biases)
    return output


# MLP parameters
input_size = 4  # 4 binary inputs
hidden_size = 3  # Size of the hidden layer
output_size = 2  # 2 binary outputs
num_steps = 10  # Number of steps/epochs

# Initialize parameters
weights, biases = initialize_parameters(input_size, hidden_size, output_size)

# Generate some random binary input data
X = np.random.randint(0, 2, size=(8, input_size))  # 8 sample inputs

# Run for specified number of steps
for step in range(num_steps):
    # Generate new random weights and biases for each step
    weights, biases = initialize_parameters(input_size, hidden_size, output_size)

    # Make predictions
    predictions = predict(X, weights, biases)
    print("predictions ", predictions)

    print(f"Step {step + 1}")

# Display final weights and biases
print("\nFinal Weight Matrices and Bias Values:")
print("W1 (Input → Hidden Layer):")
print(weights["W1"])
print("\nBias b1:")
print(biases["b1"])
print("\nW2 (Hidden Layer → Output):")
print(weights["W2"])
print("\nBias b2:")
print(biases["b2"])
print("\nNumber of Steps:", num_steps)

# Test with a single binary input
test_input = np.array([[1, 0, 1, 0]])  # Example binary input with 4 values
output = predict(test_input, weights, biases)
print("\nPrediction for test input", test_input, ":", output[0])
