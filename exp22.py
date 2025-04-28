import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from spellchecker import SpellChecker


# Function to clean text
def clean_text(text):
    # a. Text cleaning (remove punctuation, numbers, and extra spaces)
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    text = re.sub(r"\d+", "", text)  # Remove numbers
    text = re.sub(r"\s+", " ", text)  # Remove extra white spaces
    return text.strip()


# Function to convert text to lowercase
def to_lowercase(text):
    return text.lower()


# Function to tokenize text
def tokenize_text(text):
    return word_tokenize(text)


# Function to remove stop words
def remove_stop_words(tokens):
    stop_words = set(stopwords.words("english"))
    return [word for word in tokens if word not in stop_words]


# Function to correct misspelled words
def correct_misspellings(tokens):
    spell = SpellChecker()
    corrected_tokens = [spell.correction(word) or word for word in tokens]
    return corrected_tokens


# Read the text from a file
with open("exp22.txt", "r") as file:
    text = file.read()

# Step 1: Text cleaning (remove punctuation, special characters, numbers, and extra white spaces)
print("Step 1: Text Cleaning")
cleaned_text = clean_text(text)
print(cleaned_text)

# Step 2: Convert text to lowercase
print("\nStep 2: Convert to Lowercase")
lowercase_text = to_lowercase(cleaned_text)
print(lowercase_text)

# Step 3: Tokenization
print("\nStep 3: Tokenization")
tokens = tokenize_text(lowercase_text)
print(tokens)

# Step 4: Remove stop words
print("\nStep 4: Remove Stop Words")
filtered_tokens = remove_stop_words(tokens)
print(filtered_tokens)

# Step 5: Correct misspelled words
print("\nStep 5: Correct Misspelled Words")
corrected_tokens = correct_misspellings(filtered_tokens)
print(corrected_tokens)

final_text = " ".join(corrected_tokens)
print("\nFinal Processed Text:")
print(final_text)
