def word_frequency(words):
    
    word_freq = {}

    # Counting the frequency of each word in the input
    for word in words:
        # get() method used to get value associated to key in he dictionary; 0 is the default value to get if word isn't present in the dict
        current_freq = word_freq.get(word, 0)
        word_freq[word] = current_freq + 1

    # Sort the dictionary by keys alphanumerically
    sorted_word_freq = dict(sorted(word_freq.items()))

    return sorted_word_freq

def main():
    input_text = input("Enter string:\n")
    words = input_text.split()
    result = word_frequency(words)

    # Displaying the sorted word frequencies
    for word, freq in result.items():
        print(f"{word}: {freq}")

if __name__=="__main__":
    main()