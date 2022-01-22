import random, sys, time

def dictionary_words():
    num_char = int(sys.argv[1])
    start_time = time.time()
    words = {}
    #user inputs the number of words desired
    

    #generate the desired amount of random line numbers
    for i in range(num_char): 
        #random line numbers need to be within the number of lines in our file
        random_number = random.randint(0, 235886)
        #add random line number as a key in our dictionary
        words[random_number] = ''

    #open the file
    with open('/usr/share/dict/words') as f:
        index = 0
        for line in f:
            #Go through the file, and if the line is one that we want, add the word to our dictionary
            if index in words:
                words[index] = line.strip()
            index += 1

    #join all the values in our dictionary to form a sentence
    sentence = ' '.join(words.values())
    print(sentence)
    end_time = time.time()
    print(f"Code completed in: {end_time-start_time}")


if __name__ == '__main__':  
    dictionary_words()