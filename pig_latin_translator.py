with open("pig_latin_translator.txt", "r") as f:
  data = list(f)

del(data[0])

for i in range(len(data)):
  data[i] = data[i].strip()

def translator(input):
  vowelFound = False
  container = ""
  message = ""

  words = input.split(" ")
  for i in range(len(words)):
    letter = [*words[i]]
    if letter[0] == "a" or letter[0] == "e" or letter[0] == "i" or letter[0] == "o" or letter[0] == "u" or letter[0] == "y":
        letter.append("yay")
    while vowelFound == False: 
      if letter[0] == "a" or letter[0] == "e" or letter[0] == "i" or letter[0] == "o" or letter[0] == "u" or letter[0] == "y":
        letter.append("ay")
        vowelFound = True
      else:
        letter.append(letter[0])
        del(letter[0])
    
    vowelFound=False
    message = message + ''.join(letter) + " "
  
  return message

for i in range(len(data)):
  print(translator(data[i]))