import re
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams


# Function to clean text
def clean_text(text):
    # Remove punctuation, numbers, and extra white spaces using regular expressions
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    text = re.sub(r"\d+", "", text)  # Remove numbers
    text = re.sub(r"\s+", " ", text)  # Remove extra white spaces
    return text.strip()


# Function to convert text to lowercase
def to_lowercase(text):
    return text.lower()


# Function for stemming
def stemming(tokens):
    ps = PorterStemmer()
    return [ps.stem(word) for word in tokens]


# Function for lemmatization
def lemmatization(tokens):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in tokens]


# Function to create 3 consecutive words (n-grams)
def create_ngrams(tokens, n=3):
    return list(ngrams(tokens, n))


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
tokens = word_tokenize(lowercase_text)

# Step 4: Stemming and Lemmatization
print("\nStep 4: Stemming and Lemmatization")

# Stemming
stemmed_tokens = stemming(tokens)
print("Stemmed Tokens:", stemmed_tokens)

# Lemmatization
lemmatized_tokens = lemmatization(tokens)
print("Lemmatized Tokens:", lemmatized_tokens)

# Step 5: Create 3 consecutive words (n-grams) after lemmatization
print("\nStep 5: Create 3 Consecutive Words (N-grams)")
three_word_ngrams = create_ngrams(lemmatized_tokens, 3)
for ngram in three_word_ngrams:
    print(ngram)
