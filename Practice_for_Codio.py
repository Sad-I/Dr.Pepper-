def Continue():
    pass

def SadiStoryPartTwo():
    print("AI voice: “Cyber activated”. David what did you do this time… well let me see the control board. A single flashing light is flickering on the control board. So, you clicked on a link huh David, well must have been just an accident. YOU CLICKED A LINK FOR HOT SINGLE WOMAN IN YOUR AREA?! OHH COME ON DAIVD, that is the oldest trick in the book. I mean honestly this is even low for you, and not just because you're married. Well, let me quickly activate the firewall and fix the problem like I always do, there and that’s done. AI voice: “Firewall deactivated”. What?! That can’t be possible I just activated the firewa… oh my god, how is this possible? The firewall is accessed and controlled by someone else?! Multiple flashing lights spontaneously pop up on the control board. No, no, no, this can’t be possible, this thing duplicating itself and actively attacking David’s OS files making it unstable. AI voice: “System failure at 15%”. Ok I need to quickly reset the system and reboot before it can spread any further, wait what’s happing? Ground starts to vibrate and shake immensely. David stop shaking the PC it won’t fix the problem! AI voice “Warning, infected system directed large scale distribution denial of service. DDOS attack imminent”. I need to reset right now before the attack happens… come on, I can do this… so close…. just a few more steps….aandd THERE DONE! Phew, that was close. All the sudden the red emergency lights turn on. Cyber quickly looks up at the control panel and is in complete disbelief. I…. I…. I just lost complete control.")
    print("----------------------------------------------------------")
    print("Please press enter to continue the story: ")
    while True:
        user = input()
        try:
            if user == "":
                Continue()
            else:
                print("it didn't work")
        except:
            continue

def UserGuess():
    print()
    list = ['A. Papaya  ', 'B. Password  ', 'C. Peter']
    while True:
         print("----------------------------------------------------------")
         print(*list, sep='')
         print("Please enter your choice: ")
         user = input()   
         try:
             if user == "B":
                 print()
                 print("----------------------------------------------------------")
                 print("My password is ‘password’, that’s clever if you ask me. Would you look at that, an email from an unknow sender that I don’t know with a link that isn’t suspicious in anyway. I’m feeling quite risky and fly today, and I deserve to have fun too. Anyways what could possibly go wrong……… Click!")
                 SadiStoryPartTwo()
                 break;
             elif user == "A":
                 print()
                 print("----------------------------------------------------------")
                 print("Right Papaya is my favourite food, surely this must be my password. No that didn't work.")
             elif user == "C":
                 print()
                 print("----------------------------------------------------------")
                 print("My grandson is a can go to hell!")
         except: 
             continue



def SadiStoryPartOne():
    print("Power up…. Beep…. Beep. Okay finally it’s on. Where is my mouse? Ah, there it is. Now I just need to find my email on the cloud or the internet, either way it’s all magic to me anyway. There that’s my email, and my password is…? Uhm what was my password again, it started with the letter ‘P’. ")
    UserGuess()

def Guide():
    print("Welcome to the guide!")
    print("When choosing option A, you will be given options to choose from where you can decide how the story will lead.")
    print("Please press enter to return to the main menu: ")
    while True:
        user = input()
        try:
            if user == "":
                print("**********************************************************")
                Menu()
                break;
            else:
                print("invalid option.")
        except:
            continue

def Characters():
    print("Welcome to the Characters!")
    print("Cyber, Dave")
    print("Please press enter to return to the main menu: ")
    while True:
        user = input()
        try:
            if user == "":
                print("**********************************************************")
                Menu()
                break;
            else:
                print("invalid option.")
        except:
            continue

def Authors():
    print("Welcome to the authors!")
    print("The legendary Aishah, The python master Konstantinos, The fabulous Sue, sadi")
    print("Please press enter to return to the main menu: ")
    while True:
        user = input()
        try:
            if user == "":
                print("**********************************************************")
                Menu()
                break;
            else:
                print("invalid option.")
        except:
            continue



def Menu():
    print("Welcome to Cyber's story, please input the following character: \n**********************************************************")
    list = ['A. Story', 'B. Guide', 'C. Characters', '     D. Authors', "     E. something", "F. something \n**********************************************************"]
    for n,i in enumerate(list[:3]):
        print(i,list[n+3])
    while True:
        UserInput = input()
        try:
            if UserInput == "A":
                print()
                print("The start of the story: \n----------------------------------------------------------")
                SadiStoryPartOne()
            elif UserInput == "B":
                print("The Guide: \n**********************************************************")
                Guide()
            elif UserInput == "C":
                print("The Characters: \n**********************************************************")
                Characters()
            elif UserInput == "D":
                print("The Authors: \n********************************************")
                Authors()

                break;
            else:
                print("Invalid option, please try again.")
        except:
            continue

Menu()
    
