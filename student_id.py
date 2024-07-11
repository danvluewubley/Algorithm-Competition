with open("student_id.txt", "r") as f:
  data = list(f)

for i in range(len(data)):
  data[i] = data[i].strip()

trials = data.pop(0)

def modulo(input):
  moduloIsFound = False
  modulo = 2
  hashmap = dict()
  containsDupes = False

  while moduloIsFound == False:
    for i in range(len(input)):
      if int(input[i])%modulo in hashmap.keys():
        containsDupes = True
        break
      else:
        if i == 0:
          hashmap[int(input[i])%modulo] = int(input[i])%modulo
        else:
          hashmap[int(input[i])%modulo] = int(input[i])%modulo
          containsDupes = False
    if containsDupes == False:
      break
    modulo+=1
    hashmap=dict()
    if modulo > 1000:
      break
  
  return modulo
    
print(trials)
for i in range(len(data)):
  main = data[i].split(" ")
  del(main[0])
  print(modulo(main))