import os
from sklearn.preprocessing import OneHotEncoder
import numpy as np


corpus = []
for filename in texts.keys():
    with open(filename, "r") as f:
        corpus.append(f.read())

full_text = ' '.join(corpus)

#: Preprocessing - simple split by spaces (you can add better tokenization if needed)
words = full_text.split()

# One-hot encoding
# Unique words
unique_words = list(set(words))

# Reshape for encoder
words_array = np.array(unique_words).reshape(-1, 1)

# Initialize OneHotEncoder
encoder = OneHotEncoder(sparse=False)
one_hot_encoded = encoder.fit_transform(words_array)

# Display results
print("\nSample Word to One-Hot Mapping:")
for word, encoding in zip(unique_words[:10], one_hot_encoded[:10]):
    print(f"{word}: {encoding}")

print("\nTotal unique words:", len(unique_words))
