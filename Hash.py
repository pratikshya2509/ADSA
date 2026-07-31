def createHashTable():
    size = int(input("Enter size of hash table: "))

    table = []

    for i in range(size):
        table.append([])

    print("\nHash Table Before Insertion")
    print("----------------------------")
    print("Index\tValues")

    for i in range(size):
        print(i, "\t", table[i])

    n = int(input("\n no. of keys : "))

    for i in range(n):
        ch = input("Enter alphabet: ")

        asciiValue = ord(ch[0])
        print("ASCII Value =", asciiValue)

        index = asciiValue % size
        print("Hash Index =", index)

        table[index].append(ch)

    return table


def displayTable(table):
    print("\nFinal Hash Table")
    print("----------------------------")
    print("Index\tValues")

    for i in range(len(table)):
        print(i, "\t", end="")

        if table[i] == []:
            print("Empty")
        else:
            for value in table[i]:
                print(value, end=" ")
            print()


hashTable = createHashTable()
displayTable(hashTable)
