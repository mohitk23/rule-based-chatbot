# Basic Rule-Based Chatbot (Python)

import time
import datetime

userName = input("Hi, Please enter your Name: ")

presentHour = datetime.datetime.now().hour
if (5 <= presentHour <= 11 ):
    print("Good Morning", userName)
elif (12 <= presentHour <= 17 ):
    print("Good Afternoon", userName)
elif (18 <= presentHour >= 20 ):
    print("Good Evening", userName)
else :
    print("Good Night", userName)
    

print("\nNamste, Welcome to ChatBot")
print("Ask me simple question. Type 'bye', 'exit', 'quit' if you want to quit the chat.")


responses = {
    "hello": f"hello {userName}, How can i help you.",
    "how are you": "I am fine, Thank You",
    "who are you": "I am a smart AI chatbot.",
    "motivate me": "keep going! Every bug you fix makes you a better developer",
    "happy": "great to hear that 😊",
}

def getResponseOfBot(userInput):
     # global checks (loop ke bahar)
    if len(userInput) == 0:
        return "Enter your Question"

    if userInput in ["bye", "exit", "quit"]:
        return f"bye {userName}, call me again"

    for eachRes in responses:
        if eachRes in userInput:
            return responses[eachRes]
        
    return "I am not able to tell that yet."

while True:

    userInput = input("\nAsk to ChatBot: ").strip().lower()
    print(userInput)
    reply = getResponseOfBot(userInput)
    time.sleep(1)
    print("Bot reply: ", reply)
    

    if userInput in ["bye", "exit", "quit"]:
        break

