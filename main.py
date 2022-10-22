# Python3 program for removing i-th
# indexed character from a string

# Removes character at index i
def remove(string, i):
    # Characters before the i-th indexed
    # is stored in a variable a
    a = string[: i]

    # Characters after the nth indexed
    # is stored in a variable b
    b = string[i + 1:]

    # Returning string after removing
    # nth indexed character.
    return a + b

# Driver Code
if __name__ == '__main__':
    string = str(input("enter the string"))

    # Remove nth index element
    i = int(input("enter i'th number"))

    # Print the new string
    print(remove(string, i))
