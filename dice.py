import random
print("Welcome to Rolling Dice Stimulator")
choice = input("DO you want to roll the dice ? (yes/no) ")
while(choice=='yes'):
    num = random.randint(1,6)

    if num==1:
        print("|---------|")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("|---------|")

    elif num == 2:
            print("|---------|")
            print("|         |")
            print("|   0 0   |")
            print("|         |")
            print("|---------|")

    elif num == 3:
                print("|---------|")
                print("|         |")
                print("| 0  0  0 |")
                print("|         |")
                print("|---------|")

    elif num == 4:
                    print("|---------|")
                    print("|  0   0  |")
                    print("|         |")
                    print("|  0   0  |")
                    print("|---------|")

    elif num == 5:
                        print("|---------|")
                        print("|  0   0  |")
                        print("|    0    |")
                        print("|  0   0  |")
                        print("|---------|")

    else:
                            print("|---------|")
                            print("|  0   0  |")
                            print("|  0   0  |")
                            print("|  0   0  |")
                            print("|---------|")

    choice = input("DO you want to roll the dice ? (yes/no) ")

    if choice == 'no':
        exit()


