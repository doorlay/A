import funcs as f

def main():
    # Some formatting to make stuff look pretty.
    print("-----------------------------------")
    print("Welcome to StockScrape, version 1.2")
    print("-----------------------------------")

    print("Would you like to... \n\n 1. Review portfolio \n 2. Check current prices \n 3. Compare\n")
    q = input(" Type a number from above: ")
    # Creates a flag for the while loop
    flag = False
    # While loop iterate until user types a correct response
    while not flag:
        if q == "1":
            print("-----------------------------")
            f.review()
            flag = True
            break
        if q == "2":
            print("--------------------------")
            f.current()
            flag = True
            break
        if q == "3":
            print("-----------------------------")
            f.compareTotal()
            flag = True
            break
        # if q == "3":
        #     print("exiting")
        #     flag = True
        #     break
        else:
            q = input("You typed neither. Type a number from above: ")

        



print(type(f.getDate()))
