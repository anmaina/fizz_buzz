
def romanToInt(s: str) -> int:
    roman_int_1 = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    roman_int_2 = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,}

    number=0
    listed_s = list(s)

    while len(listed_s)>1:
        if listed_s[0] + listed_s[1] in roman_int_2.keys():
            number += roman_int_2[listed_s[0] + listed_s[1]]
            del listed_s[0]
            del listed_s[0]
        else:
            number += roman_int_1[listed_s[0]]
            del listed_s[0]

    if len(listed_s)>0:
        number += roman_int_1[listed_s[0]]

    return number

print(romanToInt("III"))
print(romanToInt("XX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))     