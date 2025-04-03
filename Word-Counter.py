'''sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"Word Count: {len(words)}")
'''

import re

def count_words():
    """Enhanced word counter with punctuation handling and detailed output."""
    sentence = input("Enter a sentence: ").strip()
    
    # Removing unnecessary spaces and handling edge cases
    if not sentence:
        print("No words to count! Please enter a valid sentence.")
        return
    
    # Extracting words using regex to avoid incorrect splits due to punctuation
    words = re.findall(r'\b\w+\b', sentence)
    
    unique_words = set(words)  # Unique word count
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    
    print(f"Total Words: {len(words)}")
    print(f"Unique Words: {len(unique_words)}")
    print(f"Average Word Length: {avg_word_length:.2f} characters")
    
    # Logging to a file for analysis
    with open("word_count_log.txt", "a") as log_file:
        log_file.write(f"Sentence: {sentence}\nTotal Words: {len(words)}, Unique Words: {len(unique_words)}, Average Length: {avg_word_length:.2f}\n\n")

if __name__ == "__main__":
    count_words()
