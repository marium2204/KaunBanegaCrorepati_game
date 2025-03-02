def KBC(questions, answers, money_prize, options, prize):
    for i in range(len(questions)):
        print(f"\nQ{i+1}: {questions[i]} for Rs.{money_prize[i]}")
        for j, option in enumerate(options[i],start=1): 
            print(f"{j}.{option}")
        choice=input("\nEnter the correct option OR press q to quit: ")
        if choice.lower() == 'q' or choice.upper() == 'Q':
            break
        elif choice.isdigit():
            choice_num=int(choice)
            if 1 <= choice_num <= len(options[i]):  
                selected_option = options[i][choice_num - 1]
                if selected_option==answers[i]:
                    print(f"\n{answers[i]} is the correct answer!")
                    prize+=money_prize[i]
                else:
                    print(f"\nSorry, the correct answer is {answers[i]}")
                    if prize>0:
                        print("\nYour last earning has been deducted from your prize money!")
                        prize-=money_prize[i-1]
                    else:
                        pass
        elif (i+1)==16:
            if choice==answers[i]:
                print(f"\n{answers[i]} is the correct answer!")
                print("CONGRATULATIONS YOU WON 7 CRORES!!")
                prize+=money_prize[i]
            else:
                print(f"\nSorry, the correct answer is {answers[i]}")
        else:
            print("Invalid Choice!!")              
        if (i + 1) == 5 or (i + 1) == 10:
            print("\nMilestone Achieved!")
        if (i+1)==15:
            print(f"Do you want to play a jackpot question for {money_prize[i+1]}?")
            jackpot=input("Enter y/Y for yes and n/N for No!")
            if jackpot == 'y' or jackpot == 'Y':
                print("\nWELCOME TO THE JACKPOT ROUND!!")              
            else:
                break
        print(f"\nYour prize money is Rs.{prize}")

    print(f"\nCONGRATULATIONS YOU WON RS. {prize}!!")    

questions = [
    "Which one can be used for creating a document?",
    "Who is often credited as the 'Father of the computer'?",
    "When was the first electronic computer developed?",
    "Which company introduced the first personal computer?",
    "Which type of computer memory is non-volatile?",
    "What does CPU stand for?",
    "What does RAM stand for in computer terms?",
    "Which device is used as the standard pointing device in a Graphical User Interface (GUI)?",
    "What is the full form of HTML?",
    "What is the primary funelifction of an operating system?",
    "Which number system is used by computers to perform calculations and store data?",
    "What does IP stand for in networking?",
    "Who is the inventor of the World Wide Web?",
    "What does URL stand for?",
    "Which company created the Windows operating system?",
    "Who is the founder of Microsoft?"
]


answers = [
    "MsWord",               
    "Charles Babbage",      
    "1945",                 
    "IBM",                  
    "ROM",                  
    "Central Processing Unit", 
    "Random Access Memory", 
    "Mouse",                
    "HyperText Markup Language", 
    "To manage hardware and software resources", 
    "Binary",               
    "Internet Protocol",    
    "Tim Berners-Lee",      
    "Uniform Resource Locator", 
    "Microsoft",
    "Bill Gates"            
]

options = [ 
    ["MsPowerpoint", "Command Prompt", "MsWord", "MsExcel"],  
    ["Ada Lovelace", "Charles Babbage", "Alan Turing", "John von Neumann"],  
    ["1936", "1945", "1951", "1960"],  
    ["Microsoft", "IBM", "Apple", "Xerox"],  
    ["RAM", "ROM", "Cache", "Hard Disk"],  
    ["Central Processing Unit", "Computer Peripheral Unit", "Control Processing Unit", "Central Programming Unit"],  
    ["Random Access Memory", "Read-Only Memory", "Rapid Access Memory", "Run-Time Memory"],  
    ["Trackpad", "Joystick", "Mouse", "Stylus"],  
    ["HyperText Makeup Language", "HyperText Markup Language", "HighText Markup Language", "HyperTransfer Markup Language"],  
    ["To process graphics", "To perform calculations", "To manage hardware and software resources", "To store data"],  
    ["Decimal", "Octal", "Binary", "Hexadecimal"],  
    ["Internal Protocol", "Internet Provider", "Internet Protocol", "Information Protocol"],  
    ["Bill Gates", "Tim Berners-Lee", "Steve Jobs", "Larry Page"],  
    ["Universal Resource Locator", "Uniform Resource Link", "Uniform Resource Locator", "Unique Resource Locator"],  
    ["Microsoft", "Apple", "Google", "Linux"],  
    ["Mark Zuckerberg", "Bill Gates", "Harry Styles", "Charles Babbage"]  
]

money_prize=[1000,
             2000,
             3000,
             4000,
             5000,
             10000,
             20000,
             40000,
             80000,
             160000,
             320000,
             640000,
             1250000,
             2500000,
             5000000,
             70000000]

prize=0

KBC(questions, answers, money_prize, options, prize)

print("Thankyou for playing KAUN BANEGA CROREPATI!!")
