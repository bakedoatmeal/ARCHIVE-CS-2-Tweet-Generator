import random

def getOneWord(hist):
  words = list(hist.keys())
  return random.choice(words)

def getWeightedWord(hist):
  totalWords = 0
  for number in hist.values(): 
    totalWords += number
  print(f"Total words: {totalWords}")

  choice = random.randint(1, totalWords)
  print(f"Number: {choice}")

  #find word 
  current = 0
  for key in hist.keys(): 
    if current + hist[key] >= choice: 
      return key
    else: 
      current += hist[key]

if __name__ == '__main__':  
  hist = {
    'one': 1,
    'two': 1, 
    'red': 1,
    'blue': 1, 
    'fish': 4
    }
  
  print(getWeightedWord(hist))