lst = list(map(int, input("Enter list elements: ").split()))

while True:
    print("\n1.Maximum")
    print("2.Minimum")
    print("3.Slice")
    print("4.Count occurrence")
    print("5.First occurrence")
    print("6.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        print("Maximum:", max(lst))

    elif ch == 2:
        print("Minimum:", min(lst))

    elif ch == 3:
        start = int(input("Start index: "))
        end = int(input("End index: "))
        print(lst[start:end])

    elif ch == 4:
        item = int(input("Enter item: "))
        print(lst.count(item))

    elif ch == 5:
        item = int(input("Enter item: "))
        if item in lst:
            print(lst.index(item))
        else:
            print("Item not found")

    elif ch == 6:
        break
