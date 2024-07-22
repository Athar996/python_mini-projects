import nltk #natural language tool kit
from nltk.chat.util import Chat, reflections

pairs = [
    ['I am (.*)', ['Hi %1']],
    ['my name is (.*)', ['Hi %1']],
    ['hi|hello|hey', ['Hello!', 'Hi there!']],
    ['what can you do', ['I can chat with you!']],
    ['(.*)', ['Invalid Input']],
    ['quit|exit|break|bye|see you later', ['Bye-bye!', 'See you later!']]
]

chatbot = Chat(pairs, reflections)

print("Hi, I'm Chatbot. What's your name?")

while True:
    try        user_input = input('user: ')
        response = chatbot.respond(user_input)
        print("Chatbot:"+ response)
        if response == 'Bye-bye!' or response == 'See you later!':
            exit        
    except (KeyboardInterrupt, EOFError, SystemExit):
        break