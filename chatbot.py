from chatbotfunctions import *


theBot = create_bot('Jordan')
train_bot(theBot)


identity = input("State your identitiy please: ")

if (identity == 'Mark'):
    print("Jordan: Welcome, Mark. Happy to have you at home.")
    birthPlace = ["Where was I born?", "You were born in Egypt."]
    favoriteBook = ["What is my favorite book?", 
    "That is easy your favorite book is The Alchemist By Paulo Coelho."]
    favoriteMovie = ["What is my favorite movie?", 
    "You have watched Inglorious Bastards moe times then I can count."]
    favoriteSport = ["What is my favorite sport?", 
    "You have always loved football."]
    custom_train(theBot,birthPlace)
    custom_train(theBot,favoriteBook)
    custom_train(theBot, favoriteMovie)
    custom_train(theBot, favoriteSport )
elif (identity == 'Jane'):
    print('Jordan: Mark is out right now, but you are welcome to the house.')
else:
    print('Jordan: Your access is denied here')
    exit()





start_chatbot(theBot)






