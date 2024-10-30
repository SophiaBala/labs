# print("Enter \"end\" to finish program")

def to_lower(letter):
    if 'A' <= letter <= 'Z':
        return chr(ord(letter) + 32)
    return letter

def XO(s):

    count_x = 0
    count_o = 0

    for letter in s:
        letter = to_lower(letter)
        if letter == "x":
            count_x += 1

        elif letter == "o":
            count_o += 1

    # count_x = sum(1 for letter in s if to_lower(letter) == 'x')
    # count_o = sum(1 for letter in s if to_lower(letter) == 'o')

    return count_x == count_o


print(XO("ooxx"))    # => True
print(XO("xooxx"))   # => False
print(XO("ooxXm"))   # => True
print(XO("zpzpzpp")) # => True
print(XO("zzoo"))    # => False



# while True:
#     s = input("Enter letters: ")
#
#     if s == "end":
#         print("Done")
#         break
#
#     print(f"{s}, is = {XO(s)}")


