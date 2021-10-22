import random
import time

def intro():
    print("Welcome to 'Dream and Graves' a game in which you will you will meet Jim and with his help your rob a bank")
    print("That is if he believes you are up for it")
    print("So do you wish to play?")
    score_reset()

def score_reset():
    global wish_to_play_score
    wish_to_play_score = 0
    do_you_wish_to_play()

def do_you_wish_to_play():
    global wish_to_play_score
    wish_to_play = input("(Yes or no) ")
    if wish_to_play == "Yes" or wish_to_play == "yes" or wish_to_play == "YES" or wish_to_play == "y" or wish_to_play == "Y":
        jim_intro()
    elif wish_to_play == "no" or wish_to_play == "No" or wish_to_play == "NO" or wish_to_play == "n" or wish_to_play == "N":
        are_you_sure()
    else:
        wish_to_play_score += 1
        if wish_to_play_score <= 10:
            print("Please enter either yes or no")
            print("So do you wish to play?")
            do_you_wish_to_play()
        else:
            print("The options were either yes or no why don't you understand that")
            score_reset()

def are_you_sure():
    print("Are you sure you don't want to play, it's fun")
    serious_ans = input("Will you play (Yes/No) ")
    if serious_ans == "yes" or serious_ans == "YES" or serious_ans == "Yes" or serious_ans == "Y" or serious_ans == "y":
        print("There that wasn't so hard now was it")
        jim_intro()
    elif serious_ans == "no" or serious_ans == "No" or serious_ans == "NO" or serious_ans == "n" or serious_ans == "N":
        print("You're just making this harder then it needs to be")
        are_you_sure_two()
    else:
        print("It's a yes or no question, o well I'll just run the game for you, dont worry")
        jim_intro()

def are_you_sure_two():
    print("Well lets make this easier for you")
    serious_answer = input("Do you want to play this game (Yes or Yes) ")
    if serious_answer == "yes" or serious_answer == "YES" or serious_answer == "Yes" or serious_answer == "y" or serious_answer == "Y":
        print("There that wasn't so hard now was it, now lets run the game")
        jim_intro()
    elif serious_answer == "no" or serious_answer == "No" or serious_answer == "NO" or serious_answer == "n" or serious_answer == "N":
        print("Fine then don't play")
        print("I mean you were the one who ran this program in the first place")
        print("It's your lost")
        print("The game is shuting down now")
        for seconds in range (3,0,-1):
            print (seconds)
            time.sleep(1)
    else:
        print("Here let me help you out a bit and just run the game for you")
        jim_intro()

def jim_intro():
    global age_score
    global player_name
    print("On my way back from work, I ran into a stranger in a McDonald's car park")
    print("You alright pal? My name is Jim")
    player_name = input("What is your name? ")
    player_name = player_name.capitalize()
    print(player_name)
    age_score = 0
    player_age()

def player_age():
    global age_score
    age = input("How old are you? ")
    try:
        checker = int(age)
        if checker >= 18:
            print("Nice to meet you!")
            job()
        elif checker < 18:
            print("It's okay then, never mind")
    except ValueError:
        print("Enter your age as a number")
        player_age()

def job():
    global go_a_again_score
    player_job_one = input("What do you do for living? ")
    player_job = input("Does your job pay well? ")
    if player_job == "no" or player_job == "No" or player_job == "NO" or player_job == "n" or player_job == "N":
        print("Would you like to make sum of money with me?")
        print("I can show you how to make more money")
        print("Okay cool")
        print("I have got a nice little plan for us")
        print(f"{player_name} asks Jim What is the plan?")
        planning_heist()
    elif player_job == "yes" or player_job == "YES" or player_job == "Yes" or player_job == "Y" or player_job == "y":
        print("take care mate..")
        print("The end")
        go_a_again_score = 0
        go_a_again()
    else:
        print("Enter yes or no")
        job()

def planning_heist():
    print(f"So {player_name}, here's the plan.")
    print(f"\x1B[3mJim pulls out his phone and shows {player_name} a map of the city\x1B[23m"); 
    print("tomorrow at midday we meet up in the alleyway one block down from the bank.")
    print("\x1B[3mJim points to the backside of the building\x1B[23m");
    print("After we meet up, we'll enter through the building through here, get the money then get out the way we got in.")
    the_choice()

def the_choice():
    ask = input("It's a pretty good plan right? ")
    if ask == "no" or ask == "No" or ask == "NO" or ask == "n" or ask == "N":
        print(f"Aight well cya {player_name}")
        print("\x1B[3mJim walks off and you never see that strange guy again\x1B[23m")
        print("\x1B[3mYou go back to your apartment and fall asleep, continuing with your normal, average life\x1B[23m")
        print("You got the boring ending")
    elif ask == "yes" or ask == "Yes" or ask == "YES" or ask == "y" or ask == "Y":
        print("Oh really? I-I mean yeah of course you do, it's a flawless plan after all ahaha")
        print("Anyway, I'll see you tomorrow in the alley way, make sure you show up on time!")
        print("\x1B[3mYou both walk off in seperate directions, heading home for the night\x1B[23m")
        print("\x1B[3mBefore sleeping, you prepare your clothes and other things you think you'll need for the heist the next day\x1B[23m")
        bank_heist()
    else:
        print("It's a Yes or No question, dumbass.")
        the_choice()

def bank_heist():
    global three_choices_score
    print("You meet up with Jim the next day in a dark alley near the bank you've planned to break into")
    print("Jim takes the leads and storms into the bank, firing off his gun to scare the customers and workers inside")
    yell = input("What do you yell at the customers. ")
    print(player_name, "yells", yell.upper())
    print("But the customers don't hear you over the sound of gun fire")
    print("Jim goes to one of the workers and demands them to give him all the cash")
    print("He then says to you to keep an eye out for guards or anyone trying to escape")
    three_choices_score = 0
    bank_heist_two()

def bank_heist_two():
    global three_choices_score
    what_to_do = input("Do you A: look around for more guards B: keep an eye on the customers being held hostage or C: go and disable the cameras. ")
    if what_to_do == "A" or what_to_do == "a" or what_to_do == "look around for more guards" or what_to_do == "look around":
        print(player_name, "then finds a hidden guard, but the guard pulls out her gun")
        guard_option()
    elif what_to_do == "B" or what_to_do == "b" or what_to_do == "keep an eye on the customers being held hostage" or what_to_do == "keep an eye on the customers" or what_to_do == "keep an eye on the hostages":
        print(player_name, "and Jim get caught by a hidden guards")
        ending_three()
    elif what_to_do == "C" or what_to_do == "c" or what_to_do == "go and disable the cameras" or what_to_do == "disable the cameras":
        print(player_name, "has zero idea how to disable the cameras and wonders why he tried in the first place")
        ending_three()
    else:
        three_choices_score += 1
        if three_choices_score  <= 6:
            print("Enter A, B or C")
            bank_heist_two()
        else:
            print("You have not entered either a, b or c in time and the hidden guard attacks you")
            ending_three()

def guard_option():
    print(player_name, "is now held at gunpoint by the guard, the guard is telling you to surrender")
    response_to_guard = input("Do you A: surrender or B: fight. ")
    if response_to_guard == "A" or response_to_guard == "a" or response_to_guard == "surrender":
        chance()
    elif response_to_guard == "B" or response_to_guard == "b" or response_to_guard == "fight":
        print(player_name, "knocked her unconscious and grabs the cash")
        ending_two()
    else:
        print("Enter A or B")
        guard_option()

def chance():
    outcome = random.randint(1,3)
    if outcome == 1 or outcome == 2:
        ending_three()
    elif outcome == 3:
        opportunity()
    else:
        print("Error in the code, needs debugging")

def chance_two():
    outcome_two = random.randint(1,100)
    if outcome_two == 1:
        print("When trying to fight the guard shots you in the leg")
        ending_three()
    else:
        ending_two()

def opportunity():
    print("The guard lowers her gun to handcuff you, you then take this opportunity to attack her grab the money and flee.")
    ending_two()

def ending_two():
    print("You are succsesful with robbing the bank and escape safely")
    next = input("What should I do next A: don't spend the money or B: spend the money ")
    if next == "A" or next == "a":
        invisible()
    elif next == "B" or next == "b":
        money()
    else:
        print ("Please enter either A or B")
        ending_two()

def ending_three():
    global go_a_again_score
    print("You are then captured and taken to prison the end")
    go_a_again_score = 0
    go_a_again()

def go_a_again():
    global go_a_again_score
    play_again = input ("Would you like to play again? (Y/N) ")
    if play_again == "y" or play_again == "yes" or play_again == "Y" or play_again == "Yes" or play_again == "YES" or play_again == "ye" or play_again == "YE" or play_again == "Ye":
        print ("Restarting the game now")
        for seconds in range (3,0,-1):
            print (seconds)
            time.sleep(1)
        intro()
    elif play_again == "n" or play_again == "no" or play_again == "N" or play_again == "No" or play_again == "NO":
        print("Fine then, dont play again")
    else:
        go_a_again_score += 1
        if go_a_again_score <= 10:
            print("Please enter either yes or no")
            go_a_again()
        else:
            print("You have not entered yes and so the game will end here I hope you have enjoyed the game")

def invisible():
    print(f"{player_name} decided to go to work next day as normal..")
    print("after a few days, dug a big hole in his kitchen floor and hides his cash there and has not spent a penny from it so far..")
    print(f"{player_name} ended up telling his girlfriend a story about his bank heist. However she wasn't impressed as he had a history of cheating on her")
    bank_heist_two_two()

def bank_heist_two_two():
    what_to_do = input("Choose your fate enter either A, B or C ")
    if what_to_do == "A" or what_to_do == "a":
        print("She told the police and you then get arrested")
        print("The End")
    elif what_to_do == "B" or what_to_do == "b":
        print("she cheated on him in revenge")
        print("The End")
    elif what_to_do == "C" or what_to_do == "c":
        print("after his arrest he was released. The money was never recovered as he did not tell anyone where he put it.")
        print("The End")
    else:
        print("Enter A, B or C")
        bank_heist_two_two()

def money():
    print("A few days pass after the big heist, the thought crosses your mind")
    print("\x1B[3mWhat should I spend this money on..\x1B[23m")
    print("\x1B[3mOooo maybe a yacht..? Or a mansion?\x1B[23m")
    choice = input("But which one first? A or B? ")
    if choice == "a" or choice == "A":
        print(f"\x1B[3m{player_name} makes his way down to the dock and meet up with a boat salesmen\x1B[23m")
        yacht_tl(player_name)
    elif choice == "b" or choice == "B":
        print(f"\x1B[3m{player_name} travels out of town to an estate agent\x1B[23m")
        mansion_tl(player_name)
    else:
        print("Just type A or B man.")
        money()

def yacht_tl(player_name):
    boat = input("Hello! Welcome to Boats R Us. I've heard you're interested in buying a Yacht yes? ")
    if boat == "yes" or boat == "Yes" or boat == "YES":
        yacht_two(player_name)
    elif boat == "no" or boat == "No" or boat == "NO":
        print("Oh um, alright well take care.")
    else:
        print("It's a yes or no question mate.")
        yacht_tl(player_name)

def yacht_two(player_name):
    yacht = input("Have you got the money with you? We can get you out on the ocean today if you do. ")
    if yacht == "yes" or yacht == "Yes" or yacht == "YES":
            print("Alright follow me, we'll take you straight to our selection of yachts")
            print("\x1B[3mAfter the shop owner takes you around the boat yard, you stop at a luxurious 30ft yacht\x1B[23m")
            yacht_three(player_name)
    elif yacht == "no" or yacht == "No" or yacht == "NO":
            print("O-oh okay well come back when you have the money please")
    else:
            print("Mate.. It's yes or no..")
            yacht_two(player_name)

def yacht_three(player_name):
    yacht = input ("I think this'd be a perfect boat for someone like you, wouldn't you agree? ")
    if yacht == "yes" or yacht == "Yes" or yacht == "YES":
        print("Of course you do, you're a man of culture after all.")
        print("Well since you've already paid. \x1B[3mHe spins around to you and throws a set of keys to you\x1B[23m")
        print("It's all yours.")
        print("\x1B[3mThe next day you come back to your yacht with all your belongings and money from the bank heist and live out the rest of your life travelling the world via your yacht")
    elif yacht == "no" or yacht == "No" or yacht == "NO":
        print("Well.. we don't have any other yachts currently for sale that fit what you want so you'll have to go elsewhere\x1B[23m")
    else:
        print("Is it really that difficult to say yes or no?")
        yacht_three(player_name)
    
def mansion_tl(player_name):
    mansion = input("Hello! Welcome to Mansions R Us, what kind of mansion are you looking for today? One in the city? A remote mansion off on an island or more of a holiday home? ")
    if mansion == "a" or mansion == "A":
        print("One in the city? Perfect, I've got a great mansion that fits that request.")
        mansion_one(player_name)
    elif mansion == "b" or mansion == "B":
        print("A remote mansion? I've got the perfect place just for you.")
        mansion_two(player_name)
    elif mansion == "c" or mansion == "C":
        print("A holiday home? I have the perfect house for you!")
        mansion_three(player_name)
    else:
        print("\x1B[3mType A for the city, B for remote, C for holoday friend.\x1B[23m")
        mansion_tl(player_name)

def mansion_one(player_name):
    print("This mansion is in the heart of the city, you'll be overlooking the entire place from your new mansion, of course because of this it's the most expensive out of the three options but it's very worth the price.")
    mansion = input("So, do you wanna go with this option? ")
    if mansion == "yes" or mansion == "Yes" or mansion == "YES":
        print("Amazing! Here are the keys to your new mansion and you'll be able to move into it tomorrow!")
        print("\x1B[3mYou immediately rush home after getting your keys and start packing your things, ready to move into your new house in the city.\x1B[23m")
        print("\x1B[3mThe next day you rush out of your house with all your things and move into your new house in the heart of the city\x1B[23m")
        print("\x1B[3mAfter a few days of living in the city, you hear a loud bang on your door, before you're able to say anything the police bust down your door and pin you to the floor, you ask what you did to deserve this and plea your innocence but they say nothing and take you away to prison\x1B[23m")
    elif mansion == "no" or mansion == "No" or mansion == "NO":
        other = input("Would you like to look at the other options instead then? ")
        if other == "yes" or other == "Yes" or other == "YES":
            mansion_tl(player_name)
        elif other == "no" or other == "No" or other == "NO":
            print("Alright well cya.")
        else:
            print("..I'm just gonna say everything again and hope you say yes or no this time..")
            mansion_two(player_name)
    else:
        print("..I'm just gonna say everything again and hope you say yes or no this time..")
        mansion_two(player_name)

def mansion_two(player_name):
    print("This mansion is the perfect place to live out your life in peace, surronded by amazing wildlife and beautiful nature")
    mansion = input("So, do you wanna go with this option? ")
    if mansion == "yes" or mansion == "Yes" or mansion == "YES":
        print("Perfect! you'll get to move into your new mansion within the next few days then!")
        print("\x1B[3mYou take the keys to your new mansion from the estate agent and head home for the day, packing your things to prepare for tomorrow\x1B[23m")
        print("\x1B[3mYou live out the rest of your peaceful life on the outskirts of the city, free to do whatever you please\x1B[23m")    
    elif mansion == "no" or mansion == "No" or mansion == "NO":
        other = input("Would you like to look at the other options instead then? ")
        if other == "yes" or other == "Yes" or other == "YES":
            mansion_tl(player_name)
        elif other == "no" or other == "No" or other == "NO":
            print("Alright well, hopefully see you another time.")
        else:
            print("..I'm just gonna repeat what I said again and hope you say yes or no.")
            mansion_two(player_name)
    else:
        print("..I'm just gonna repeat what I said again and hope you say yes or no.")
        mansion_two(player_name)

def mansion_three(player_name):
    print("This mansion will be an amazing getaway for you, an escape from your daily, boring life in the city.")
    mansion = input("So, do you wanna go with this option? ")
    if mansion == "yes" or mansion == "Yes" or mansion == "YES":
        print("Perfect! you'll get to move into your new mansion within the next few days then!")
        print("\x1B[3mYou take the keys to your new mansion from the estate agent and head home for the day, packing your things to prepare for tomorrow\x1B[23m")
        print("\x1B[3mThe following day you take your things and rush out of the door, using your new holiday home as a place to hide while things cool down in the city.\x1B[23m")
    elif mansion == "no" or mansion == "No" or mansion == "NO":
        other = input("Would you like to look at the other options instead then? ")
        if other == "yes" or other == "Yes" or other == "YES":
            mansion_tl(player_name)
        elif other == "no" or other == "No" or other == "NO":
            print("Alright well, we got nothing else for you here.")
        else:
            print("..I'm just gonna say what I said again, this time say yes or no.")
            mansion_two(player_name)
    else:
        print("..I'm just gonna say what I said again, this time say yes or no.")
        mansion_two(player_name)

intro()