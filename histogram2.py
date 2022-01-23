from string import punctuation


def histogram(source_text):
    f = open(source_text, 'r')
    text = f.read()
    f.close()
    punctuation = '''!()-[]{\}\;:'"\,<>./?@#$%^&*_~'''
    text = text.lower()

    for element in text:
        if element in punctuation:
            text = text.replace(element, "")

    print(text)

    all_words = text.split()
    print(all_words)
    histogram = []
    
    #return histogram as a list of lists
    #[['one', 1], ...

    #'one fish two fish red fish blue fish'

    #list[0], list[1]

    for word in all_words:
        #count[0]
        #['word', 1]
        word_found = False
        for minilist in histogram: 
            if minilist[0] == word: 
                minilist[1] += 1
                word_found = True
                break
        if word_found is False: 
            histogram.append([word, 1])

    return histogram

def unique_words(histogram):
    #return the count of unique words
    return len(histogram)

def frequency(word, histogram):
    #return the number of times that word appears in a text
    for minilist in histogram: 
        if minilist[0] == word.lower():
            return minilist[1]
    return 0

if __name__ == '__main__':
    hist = histogram('sampletext.txt') #dictionary {'one':1...}
    print(hist)
    words = unique_words(hist)
    print(words)
    count = frequency('FIsh', hist)
    print(count)
    
