with open("roman_numerals.txt") as f:
    data = list(f)

for i in range(len(data)):
    data[i] = data[i].strip()

def num_to_roman(input):
    roman_numerals = ""
    value = int(input)

    if value >= 1000:
        repeat = value//1000
        roman_numerals = roman_numerals + "M"*repeat
        value = value - value//1000 * 1000
    if value%1000 >= 900:
        roman_numerals = roman_numerals + "CM"
        value = value - 900
    if value >= 500:
        repeat = value//500
        roman_numerals = roman_numerals + "D"*repeat
        value = value - value//500 * 500
    if value%1000 >= 400:
        roman_numerals = roman_numerals + "CD"
        value = value - 400
    if value >= 100:
        repeat = value//100
        roman_numerals = roman_numerals + "C"*repeat
        value = value - value//100 * 100
    if value%100 >= 90:
        roman_numerals = roman_numerals + "XC"
        value = value - 90
    if value >= 50:
        repeat = value//50
        roman_numerals = roman_numerals + "L"*repeat
        value = value - value//50 * 50
    if value%100 >= 40:
        roman_numerals = roman_numerals + "XL"
        value = value - 40
    if value >= 10:
        repeat = value//10
        roman_numerals = roman_numerals + "X"*repeat
        value = value - value//10 * 10
    if value%10 == 9:
        roman_numerals = roman_numerals + "IX"
        value = value - 9
    if value >= 5:
        repeat = value//5
        roman_numerals = roman_numerals + "V"*repeat
        value = value - value//5 * 5
    if value%10 == 4:
        roman_numerals = roman_numerals + "IV"
        value = value - 4
    else:
        roman_numerals = roman_numerals + "I"*value
    return roman_numerals
        
def roman_to_num(input):
    string = [*input]
    value = 0

    for i in range(len(string)):
        if i == 0:
            if string[i] == "M":
                value += 1000
            if string[i] == "D":
                value += 500
            if string[i] == "C":
                if string[i+1] == "D":
                    value += 400
                    continue
                if string[i+1] == "M":
                    value += 900
                    continue
                else:
                    value += 100
            if string[i] == "L":
                value += 50
            if string[i] == "X":
                if string[i+1] == "L":
                    value += 40
                    continue
                if string[i+1] == "C":
                    value += 90
                    continue
                else:
                    value += 10
            if string[i] == "V":
                value += 5
            if string[i] == "I":
                if string[i+1] == "V":
                    value += 4
                    continue
                if string[i+1] == "X":
                    value += 9
                    continue
                else:
                    value += 1
        if i < len(string) - 1 and i != 0:
            if string[i] == "M":
                if string[i-1] == "C":
                    continue
                else:
                    value += 1000
            if string[i] == "C":
                if string[i-1] == "X":
                    continue
                elif string[i+1] == "M":
                    value += 900
                elif string[i+1] == "D":
                    value += 400                    
                else:
                    value += 100
            if string[i] == "X":
                if string[i+1] == "C":
                    value += 90 
                elif string[i+1] == "L":
                    value += 40
                else:
                    value += 10
            if string[i] == "I":
                if string[i+1] == "X":
                    value += 9
                    continue                    
                elif string[i+1] == "V":
                    value += 4              
                else:
                    value += 1
            if string[i] == "V":
                if string[i-1] == "I":
                    continue
                else:
                    value += 5
            if string[i] == "L":
                if string[i-1] == "X":
                    continue
                else:
                    value += 50
        if i == len(string)-1:
            if string[i] == "M":
                if string[i-1] == "C":
                    continue
                value += 1000
            if string[i] == "D":
                if string[i-1] == "C":
                    continue
                value += 500
            if string[i] == "C":
                if string[i-1] == "X":
                    continue
                value += 100
            if string[i] == "L":
                if string[i-1] == "X":
                    continue
                value += 50
            if string[i] == "X":
                if string[i-1] == "I":
                    continue
                value += 10
            if string[i] == "V":
                if string[i-1] == "I":
                    continue
                value += 5
            if string[i] == "I":
                value += 1
    return value

for i in range(len(data)):
    if data[i].isdigit():
        print(num_to_roman(data[i]))
    else:
        print(roman_to_num(data[i]))