#write a program that let the user know about what to eat in the morning beakfast!
def A():
    print("Welcome to the Breakfast Menu of Whole WEEK!")
    a = input("Enter the day:-")
    a = a.upper()
    if a == "MONDAY":
        print("EAT FRUITS")
        print("You can have Watermelon, Honey melon, Berries, Raspberries, Blueberries, Mango, Papaya.")
        print("This Breakfast will help you to maintain glow of your SKIN!")
        br=input('Press A to continue and Q to quit')
        br=br.upper()
        if br == "A":
            A()
    elif a == "TUESDAY":
        print("EAT SALADS")
        print("You can have Carrots, Beetroot, Cucumber, Tomatoes, Onion, Capsicum, Reddish.")
        print("This Breakfast will help you to care of your HAIR PROBLEMS!")
        br=input('Press A to continue and Q to quit')
        br=br.upper()
        if br == "A":
            A()
    elif a == "WEDNESDAY":
        print("EAT SPROUTS")
        print("You have to take Mung beans, Moth beans, Chickpeas.")
        print("This Breakfast will take care of your muscles!")
        br=input('Press A to continue and Q to quit')
        br=br.upper()
        if br == "A":
            A()
    elif a == "Thursday":
        print("14 TYPES OF DRY FRUITS")
        print('''You can have Cashew, Almond, Pista, Walnut, Dates, Anjir, Kishmish, Blueberry, Cranberry, Apricot,"
            Maccadenia nuts, Hassal nuts, IN TOTAL(28 PIECES).''')
        print("This Breakfast will take care of your all body ORGANS!")
        br=input('Press A to continue and Q to quit')
        br=br.upper()
        if br == "A":
            A()
    elif a == "FRIDAY":
        print("MILK SHAKE")
        print("You can have Mango Milkshake OR Banana Milkshake, OR Custard Apple Shake!")
        print("This Breakfast will Full fill Vitamin D!")
        br=input('Press A to continue and Q to quit')
        br=br.upper()
        if br == "A":
            A()
    elif a == "SATURDAY":
        print("VEGITABLE JUICE")
        print("You can have Carrot, Beetroot, Tomato, Green Leafy OR ABC (Apple Beetroot Carrot).")
        print("This Breakfast will reduce the SKIN DISEASES!")
        br=input('Press A to continue and Q to quit')
        br=br.upper()
        if br == "A":
            A()
    elif a == "SUNDAY":
        print("EAT YOUR CHOICE OF BREAKFAST")
        print("You can have ANYTHING.")
        print("This Breakfast will help you to maintain the taste of your TONGUE!")
        br=input('Press A to continue and Q to Quit')
        br=br.upper()
        if br == "A":
            A()
        elif br == "Q":
            exit()
    else:
        print("Check the spelling")
A()