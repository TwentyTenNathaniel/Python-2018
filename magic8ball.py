import random
import time

name = "Chief"
choices=["Yes ", "Nah " , "I don't know " , "Maybe " , "Most Definitely " , "Not Right Now " , "I'm too tired " , "It's Not gonna happen "]
while True:
    user_input = input("Ask a question, or type exit to leave the program? ")
    if user_input == 'exit':
        user_input == input("Goodbye Chief")

    print(random.choice(choices) + "%s" % name   )
   

    
        
