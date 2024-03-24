##Time travel game

## modules
import time
import random
import datetime

##Thinking

## if map/car_Key doesnt equal 1; display error sequence and don't run map/travel functions

# map = 1


# if map != 1:
#     print("ERROR")
# elif map == 1:
#     print("works")
space = "////////////////////////////////////////////////////////////////////////////"


## Code

## Statuses
global energy
energy = 500
global lives
lives = 5
comments = ["Let's go!", "You can't do this, give up", "Why you so slow", "I love your name"]
random_text = random.choice(comments)
global car_key
car_key = 0
global mapc
mapc = 0
global paintbrush
paintbrush = 0
global battery
battery = 0
global vase
vase = 0
global tokens
tokens = 0
global sequence
sequence = 0
random_bonus = random.randint(1,100)
random_deduct = random.randint(1,3)

## Functions


def endscreen():
    print(space)
    print("As a result of getting killed in this era, you become erased from existence\n")
    time.sleep(1)
    print("You died")
    quit()
def start_screen(): 
    print(space)
    intro = print("Welcome to ---! This game involves your brilliant brain's knowledge on history and common sense. Enjoy!\n")
    time.sleep(5)
    intro = print("You are walking throughout the local library, when you see a haze of yellow transpires across your view\n")
    time.sleep(5)
    intro = print("You become lost and lose yourself, walking through a gap in the shelves you are now travelling down a rabbit hole\n")
    time.sleep(5)
    print(space)
    intro = print("\nYou end up in a carnival in USA'S 80s")
    time.sleep(3)
def map():
    print(space)
    global energy
    print("Hello I am Map. Where would you like to go?")
    travel_to = input("1800s, 1500s or Ancient Egypt ")
    if travel_to == "1800s":
        energy = energy - 100
        print(f"Here is your police box's tank: {energy}/500")
        time.sleep(1)
        print(space)
        screen_1800s()
    elif travel_to == "1500s":
        energy = energy - 100
        print(f"Here is your police box's tank: {energy}/500")
        time.sleep(1)
        print("An ad break from Doc () services")
        ##create ad breaks
        print(space)
        time.sleep(3)
        screen_1500s()
    elif travel_to == "Ancient Egypt":
        energy = energy - 100
        print(f"Here is your police box's tank: {energy}/500")
        time.sleep(1)
        print(space)
        screen_ancientegypt()
    else:
        print("ERROR")
        time.sleep(2)
        print("Try again")
        travel_to
def character_80():
    print(space)
    global tokens
    print("Hello, what a day this is!")
    time.sleep(1)
    enjoy = input("Are you enjoying the carnival? ")
    if enjoy == "yes":
        print("Yay, I hope you stay")
    elif enjoy == "no":
        print("Sorry about that")
    print("\nI have a question for you.")
    answer_80c = input("Who is the president of USA in 1980? ")
    if answer_80c == "Jimmy Carter":
        print("You are correct! Jimmy Carter was president from 1977-1981. Here is a reward for answering this difficult question\n")
        time.sleep(1)
        random_bonus = random.randint(1,100)
        tokens = tokens + random_bonus 
        print(f"You have a recieved a bonus of tokens. You now have {tokens}. Collect tokens to spend it on cool things at the end")
    else:
        print("No silly. This is a difficult question though, especially kids who don't consume politics. Am i right? Jimmy Carter was the president in 1980.\n")
    print(space)
    print("People walk by and you hear a mass of voices")
    time.sleep(1)
    random_text = random.choice(comments)
    print(random_text)
def doc():
    print(space)
    print(f"hello {user}! I am here to guide you on your journey across space and time, aiding you in getting home. My name is Doc\n")
    time.sleep(2)
    print("Doc: I would like to give you a couple of things; a map and a blue police box. Please take good care of her. She means a lot to me\n")
    time.sleep(3)
    global car_key
    car_key = 1
    global mapc
    mapc = 1
    print("Car key: 1\n")
    print("Map: 1\n")
    print("Doc: The map will be a directory to the places you need to go")
    time.sleep(2)
    print("Doc: Your aim is to collect objects from different eras. This is to create a snazzy invention that will lead you home\nHowever, you must also find a piece of paper that will tell you the sequence you must put the objects in to manifest this glorious thing")
    time.sleep(1)
    print("Doc: Good luck")
    time.sleep(2)
def ferris():
    print(space)
    print("You go on the ferris wheel\n")
    print("🎡")
    time.sleep(1)
    print("The ferris wheel starts to waver. CLATTER CLATTER! You start to freak out. What do you do?")
    answer_f = input("Do you put a wedge on the pole, fly out of infrastructure or do you scream and panic? ")
    if answer_f == "put a wedge on the pole":
        print("You saved the day!") 
        
        global tokens
        random_bonus = random.randint(1,100)
        tokens = tokens + random_bonus
        print(f"You have a total of b{tokens} tokens")
        time.sleep(3)
        print(f"You have received a bonus of {random_bonus}")
        print(f"Tokens: {tokens}")
        doc()
    elif answer_f == "fly out of infrastrusture": ## global variables
        global lives
        lives = lives - 1
        print(f"Lives: {lives}")
        time.sleep(1)
        print("You get hurt as a result of falling on top of a spike on the merry go round")    
    else:
        lives = lives - 1 
        print(f"Lives: {lives}")
        print("You get hurt as a result of failling to escape from the ferris wheel")
        time.sleep(1)
def screen_1800s():
    print("Welcome to the 1800s\n")
    time.sleep(1)
    print("Where would you like to go?")
    time.sleep(1)
    to_go1800s = input("Meet Napoleon Bonaparte or object finding ")
    if to_go1800s == "Meet Napoleon Bonaparte":
        print("This is Napoleon Bonaparte")
        time.sleep(1)
        napoleon = {
        "Date of Birth": "15th of August, 1769",
        "Nationality": "French",
        "Known for": "One of the most successful generals of the French revolutionary armies and the Emperor of France from 1804 - 1814."
        }
        print(napoleon)
        time.sleep(5)
        print("\nNapoleon Bonaparte: Hello young one. My name is Napoleon. I have a question for you.")
        time.sleep(3) 
        print("Napoleon Bonaparte: True or False: I wrote a science fiction book")
        time.sleep(1)
        true_false = input("\n\nTrue or False: ")
        if true_false == "False":
            print("Napoleon Bonaparte: You are correct! I didn't write a science fiction book. Instead I wrote a romance novel called 'Clisson et Eugenie'.")
            time.sleep(5)
            print("Napoleon Bonaparte: It was a pleasure to meet you. Au revoir")
            time.sleep(3)
            print(space)
            global energy
            energy = energy + 150
            print(f"You have earned 150 energy. You now have {energy}")
            print(space)
        elif true_false == "True":
            print("Napoleon Bonaparte: I didn't write a science fiction book! That would be absurd!")
            time.sleep(3)
            print("Napoleon Bonaparte: It sadly wasn't a pleasure to meet you. Au revoir")
            time.sleep(1)
            print(space)
            energy = energy - 100
            print(f"You have been deducted 100 energy. You now have {energy}")
            print(space)
        else:
            print("Napoleon Bonaparte: I do not understand what you are saying. I know my English isn't very good, but still")
            time.sleep(3)
            print("Napoleon Bonaparte: I must deduct a hefty fee from you")
            time.sleep(3)
            global tokens
            tokens = tokens - 100
            print(f"You have been deducted 100 tokens. You now have {tokens}")
            time.sleep(1)
            print(f"Napoleon Bonaparte: Au revoir {user}")
            print(space)
            time.sleep(3)
        ## problem
        print("You are thrown into battle")
        time.sleep(3)
        print("You get bombed at")
        print("💣")
        time.sleep(3)
        print("Oh no, you have died!")
        global lives
        lives = 0
        endscreen()
    elif to_go1800s == "object finding":
        print("LETS GO OBJECT FINDING. You are looking for an influential object from that era. Suddenly you come across 2 items. A shriveled up paper is seen")
        print("It asks 'what important object was invented in the 1800s; the human brain or the battery'")
        ques_obj18 = input("What object was it? ")
        while ques_obj18 == "the human brain":
            print("You are stupid, try again\n")
            lives = lives - 1
            print(f" You now have {lives} lives\n")
            ques_obj18 = input("What object was it? ")
        if ques_obj18 == "the battery":
            print("\nCORRECT\n")
            global battery
            battery = 1
            print("Battery: 1\n")
            print("🪫\n")
            print("Doc: Now that you have successfully gained this object, let's travel to the 1500s!\n")
        else:
            print("ERROR")
def screen_1500s():
    print(space)
    print("Welcome to the 1500s\n\n A time of great progress; inventions and cultural () have grown and ()")
    to_go1500s = input("Where do you want to go to? 14th century London, see the stars or meet Leondardo da Vinci ")
    if to_go1500s == "14th century London":
        print(space)
        print("You travel to 16th century London and stumble across ()")
    elif to_go1500s == "see the stars":
        print(space)
        print("You decide to camp outside\n \n While you look up at the sky a shooting star goes past")
        print("You wish for your dream to come true; going back home")
        time.sleep(3)
        print("Out comes a shooting star\n")
        time.sleep(1)
        ## add in cute module/image
        print("💫\n")
        global tokens
        random_bonus = random.randint(1,100)
        tokens = tokens + random_bonus
        print(f"Star: My magicalness has granted you {random_bonus} tokens. You now have {tokens} tokens")
        time.sleep(3)
        print(space)
        print("Write how you feel?")
        ##continue to look at stars until you type in I (dialogue)
        feelings = input("How do you feel? ")
        while feelings != "good":
            print(random_text)
            time.sleep(3)
            feelings = input("How do you feel? ")
        print("Doc: It is always good to self reflect\n")
    elif to_go1500s == "meet Leonardo da Vinci":
        print("You decide to go and meet the influential, all knowing inventor and artist.\n")
        time.sleep(1)
        print("Leondaro da Vinci: dialogue\n")
        time.sleep(3)
        print("He gives you a paintbrush")
        global paintbrush
        paintbrush = 1
        print("Paintbrush: 1")
    else:
        print("ERROR")
def screen_ancientegypt():
    print(space)
    print("You find yourself dazed in a place where it could only be the 'Black Land or Kemet' ")
    print("Tutankhamun: dialogue")
    print("You are given 3 choices; see the Nile river, looking for object, go to the pyraminds ")
    to_goAncienteEypt = input("Where would you like to go? ")
    if to_goAncienteEypt == "see the Nile river":
        print("Ask question")
        print("Where would you like to go now? ")
    elif to_goAncienteEypt == "looking for object":
        print("You decide to go find the object ()")
        ## find object
        print("Debrief")
        ## find invention paper
        global sequence
        sequence = 1
        print("Advice of paper")
        ##gain the paper
        to_goAncient2 = input("What would you like to do? Map or create invention ")
        if to_goAncient2 == "Map":
            map()
        elif to_goAncient2 == "create invention":
            create_invention()
            

    elif to_goAncienteEypt == "go to the pyraminds":
        print("You decide that you want to go into the pyramids\n out of knowhere debris comes tubbling down from the ()")
        object_while = input("you are given 2 desicions. What do you do? run or stay")
        while object_while != "run": 
            random_deduct = random.randint(1,3)
            lives = lives - random_deduct
            print("HELP")
            print(f"Lives: {lives}")
            object_while = input("ENTER ANSWER ")
            time.sleep(2)
        print("You have escaped the pyramids")       
def create_invention():
    if vase == 1 and paintbrush == 1 and battery == 1:
        print("Doc: You have all the necessary items needed to proceed in creating the invention to get home\n")
        time.sleep(1)
        print("The sequence: 'bruinpaths save the tyre tar'\n")
        print("Doc: What is the sequence?\n Where vase = a, paintbrush = b and battery = c")
        time.sleep(2)
        print("Doc: Input your answer as 'answer-answer-answer' form\n")
        time.sleep(1)
        answer_sequence = input("Your answer: ")
        if answer_sequence == "b-a-c":
            ##correct
            print("\nThe invention comes together")
            time.sleep(1)
            print("🖌️⚱️🪫")
            time.sleep(1)
            print(f"Doc: {user}, you have successfully created the key to getting back home!\n")
            time.sleep(1)
            print("🗝️")
            time.sleep(1)
            print("Doc: You have braved the challenges on your path...")
            time.sleep(1)
            print("Doc: Used brain and braun to collect () items and")
            time.sleep(1)
            print("Doc: ()\n")
            time.sleep(1)
            feeling = input("Doc: How do you feel? ")
            print(f"Doc: I am happy that you feel {feeling}")
            time.sleep(2)
            print("Doc: Now get that key, scurry of to that police box and get home")
            time.sleep(1)
            print(space)
            time.sleep(3)
            print("You get into the classic blue police box and drive that key into a switch where you somehow knew where it was supposed to be ")
            time.sleep(1)
            print("You say {} to the police box. Noice and fluster builds up in the time machine and you start to hesitant if this will work")
            time.sleep(1)
            print("🫧")
            print("Bang!")
            time.sleep(1)
            print("Everything drops, you pause")
            time.sleep(2)
            print("You look to the door of the box and walk out")
            time.sleep(1)
            print("You are back in the library where you got lost\n\n")
            time.sleep(1)
            print(space)
            time.sleep(2)
            print(f"Thankyou {user} for playing ---!\n")
            time.sleep(1)
            print("🥰")
            time.sleep(2)
            print(f"----You finished with {lives} lives and {energy} energy in the tank\n----")
            time.sleep(1)
            print("But most importantly, you earned ...")
            time.sleep(1)
            print("Drumroll please")
            time.sleep(1)
            print("🥁")
            time.sleep(1)
            print("🥁")
            time.sleep(1)
            print("🥁")
            time.sleep(1)
            print(f"You earned {tokens} tokens!")
            time.sleep(1)
            print("You will be placed into a ranking system using the tokens you earned\n")
            time.sleep(2)
            print(space)
            print("Thankyou for playing ---!")
            time.sleep(1)
            print("BYE")
            print("👋")
            time.sleep(2)
            quit()

            


        else:
            # WRONG ANSWER
            print("Doc: Oh no! What is happening\n")
            print("😱\n")
            time.sleep(1)
            print("Doc: You did it wrong. Now you will become stuck in time!\n")
            time.sleep(1)
            print("You start to shake and then reality crashes into one another")
            time.sleep(1)
            print("Everything pauses")
            time.sleep(2)
            print("Your eyes are infinitely estranged into looking at the one plane")
            time.sleep(2)
            print("The ()")
            quit()
    else:
        print("You don't have all the required items\n")
        time.sleep(1)
        print("Here are the items you do have:")
        time.sleep(1)
        print(f"Ancient Egypt: {vase} ")
        print(f"1500s: {paintbrush}")
        print(f"1800s: {battery} ")
        time.sleep(3)
        print("\nGo back to map to find those objects you don't have")
        time.sleep(1)
        print(space)
        map()
def r_Usure():
    print("Are you sure you want to leave this game?")
    ## future self dialogue
    question = input("ARE YOU REALLY SURE YOU WANT TO LEAVE THIS GAME!!??")
    while question == "yes":
        print("I don't know why you would want to")
        time.sleep(2)
        question = input("ARE YOU REALLY SURE YOU WANT TO LEAVE THIS GAME!!??")   
    print("SENDING YOU BACK ON PATH")
    time.sleep(3)
def meeting_80s():
    print("You are in the hustle and bustle of noise, laughter and lavishing smells\n You see a mysterious character go by, what do you do?")
    answer_80 = input("Follow the mysterious character or Go on the ferris wheel ")
    if answer_80 == "Follow the mysterious character":
        print("You follow the mysterious character")
        time.sleep(2)
        doc()
    else:
        ferris()
def back_onPath():
    print("Dialogue from future self")
    time.sleep(1)
    print(space)
    print("You follow the mysterious character")
    time.sleep(1)
    print(space)
    doc()
    print("Doc: Lets go back in time")
    time.sleep(1)
    print(space)
    screen_1800s()

##Introdcution
if lives == 0:
    print(endscreen) 
if energy == 0:
    print("hhkj")
user = input("What is your name? ")
start_screen()

##The 80s
meeting_80s()
character_80()

## 1800s - Napoleon
print(space)
go_back = input("\nDo you want to go back to the 1800s ")
print("Is it going to work")
if go_back == "yes" and car_key == 1:
    print(f"Enjoy your trip {user}")
    energy = energy - 100
    time.sleep(1)
    print(f"Here is your police box's tank: {energy}/500")
    time.sleep(3)
    print(space)
    screen_1800s()
elif go_back == "no" and mapc == 1:
        print ("here are your choices")
        time.sleep(2)
        tim_stats = input("Choose to see stats or map")
        if tim_stats == "map":
            map()
        elif tim_stats == "stats":
            print(f"Here is your police box's tank: {energy}/500")
            print(f"Amount of lives: {lives}")
            map()
else: 
    print("You don't have the required items to see your stats and go time travelling")
    time.sleep(1)
    print("Go back and follow the mysterious character to find out more")
    time.sleep(1)
    pit_stop = input("Do you follow the mysterious character or forfeit and exit ")
    if pit_stop == "follow the mysterious character":
        back_onPath()
    else:
        r_Usure()
        back_onPath()

## 1500s
time.sleep(2)
energy = energy - 100
print(f"Here is your police box's tank: {energy}/500\n")
screen_1500s()
print(f"Doc: Hey {user}, I hope you are enjoying your time. Where would you like to go? ")
to_go1500s2 = input("Back to the start in the 1500s, use the map or see your stats ")
if to_go1500s2 == "Back to the start in the 1500s":
    screen_1500s()
elif to_go1500s2 == "use the map":
    map()
elif to_go1500s2 == "see your stats":
    print(f"Here is your police box's tank: {energy}/500\n")
    print(f"Amount of lives: {lives}\n")
    print(space)
    time.sleep(1)
    print("What would you like to do now?")
    to_go1500s2 = input("Back to the start in the 1500s or use the map ")
    if to_go1500s2 == "Back to the start in the 1500s":
        screen_1500s()
    elif to_go1500s2 == "use the map":
        map()
map()
