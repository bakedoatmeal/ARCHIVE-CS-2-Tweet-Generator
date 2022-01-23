def histogram(source_text):
    f = open(source_text, 'r')
    text = f.read()
    f.close()
    text = text.lower()
    print(text)
    all_words = text.split()
    print(all_words)
    histogram = {}

    for word in all_words:
        if word in histogram:
            histogram[word] += 1
        else: 
            histogram[word] = 1
    
    #return histogram as a dictionary
    return histogram

def unique_words(histogram):
    #return the count of unique words
    return len(histogram.keys())

def frequency(word, histogram):
    #return the number of times that word appears in a text
    return histogram[word.lower()]

if __name__ == '__main__':
    hist = histogram('sampletext.txt') #dictionary {'one':1...}
    print(hist)
    words = unique_words(hist)
    print(words)
    count = frequency('Red', hist)
    print(count)
    
