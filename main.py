#input a word or sentences
string = input("pleases enter your own string")


string2 = ("")
#loop for printing in reverse
for i in string:
    string2 = i + string2

print("\nThe original string = ", string)
print("The Reverse string = ", string2)