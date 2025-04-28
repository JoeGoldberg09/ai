import os
from sklearn.feature_extraction.text import CountVectorizer

# List of text files in your directory
filenames = ["file1.txt", "file2.txt", "file3.txt"]

# Step 1: Read all files and combine their content
corpus = []
for filename in filenames:
    with open(filename, "r", encoding="utf-8") as file:
        corpus.append(file.read())

# Step 2: Initialize CountVectorizer (Bag of Words model)
vectorizer = CountVectorizer()

# Step 3: Fit and transform the corpus
X = vectorizer.fit_transform(corpus)

# Step 4: Get feature names (unique words)
feature_names = vectorizer.get_feature_names_out()

# Step 5: Show the Bag of Words
print("Vocabulary (Unique Words):")
print(feature_names)

print("\nBag of Words Matrix (Document-Term Matrix):")
print(X.toarray())

# Optional: Display in a nicer format
import pandas as pd

df_bow = pd.DataFrame(X.toarray(), columns=feature_names)
print("\nBag of Words as DataFrame:")
print(df_bow)
