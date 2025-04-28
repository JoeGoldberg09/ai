import os
import re


def read_files(file_paths):
    text_data = ""
    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8") as file:
            text_data += file.read() + " "  # Add space to separate files
    return text_data


def tokenize(text):
    # Simple split by space and remove punctuation
    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Remove punctuation and special characters
    text = re.sub(r"[^\w\s]", "", text)

    # Remove extra white spaces
    text = re.sub(r"\s+", " ", text).strip()

    text.lower()
    words = text.split()
    return words


def create_vocabulary(words):
    return sorted(list(set(words)))  # unique sorted list


def one_hot_encode(vocab):
    word_to_index = {word: idx for idx, word in enumerate(vocab)}
    one_hot_vectors = {}
    vocab_size = len(vocab)

    for word, idx in word_to_index.items():
        vector = [0] * vocab_size
        vector[idx] = 1
        one_hot_vectors[word] = vector
    return one_hot_vectors


def main():
    # Specify your three text file paths
    file_paths = ["file1.txt", "file2.txt", "file3.txt"]

    # Step 1: Read all files
    text_data = read_files(file_paths)

    # Step 2: Tokenize text
    words = tokenize(text_data)

    # Step 3: Create Vocabulary
    vocabulary = create_vocabulary(words)

    # Step 4: One-Hot Encode Vocabulary
    one_hot_vectors = one_hot_encode(vocabulary)

    # Displaying few one-hot encodings
    print("\nVocabulary Size:", len(vocabulary))
    print("\nSample One-Hot Encodings:")
    for word in list(one_hot_vectors.keys())[:10]:  # showing only first 10 words
        print(f"{word}: {one_hot_vectors[word]}")


if __name__ == "__main__":
    main()
