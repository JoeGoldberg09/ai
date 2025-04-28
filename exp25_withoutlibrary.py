import re


# Function to read and combine text from multiple files
def read_files(file_list):
    text = ""
    for file_name in file_list:
        with open(file_name, "r") as file:
            text += file.read() + " "
    return text


# Function to clean the text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\d+", "", text)  # Remove numbers
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    return text


# Function to tokenize the text
def tokenize(text):
    return text.split()


# Function to build the Bag of Words
def bag_of_words(tokens):
    bow = {}
    for word in tokens:
        if word in bow:
            bow[word] += 1
        else:
            bow[word] = 1
    return bow


# Main function
def main():
    filenames = ["file1.txt", "file2.txt", "file3.txt"]
    text_data = read_files(filenames)
    cleaned_text = clean_text(text_data)
    tokens = tokenize(cleaned_text)
    bow = bag_of_words(tokens)

    print("Bag of Words (word frequencies):")
    print(bow)  # prints whole dictionary
    for word, count in bow.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
