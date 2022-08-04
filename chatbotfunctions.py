from chatterbot import ChatBot



def create_bot(name):


    newBot = ChatBot(name,
    read_only = False,
    logic_adapters = ['chatterbot.logic.BestMatch', 'chatterbot.logic.TimeLogicAdapter', 'chatterbot.logic.MathematicalEvaluation'],
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter')
    

    return newBot

def train_bot(Bot):
    from chatterbot.trainers import ChatterBotCorpusTrainer
    corpus_trainer = ChatterBotCorpusTrainer(Bot)
    corpus_trainer.train("chatterbot.corpus.english")

def custom_train(Bot, rulebasedList):
    from chatterbot.trainers import ListTrainer
    trainer = ListTrainer(Bot)
    trainer.train(rulebasedList)


def start_chatbot(Bot):
    print('\033c')
    print ('Hello I am Jordan, How can I help you?')
    bye_list = ['bye', 'bye Jordan', 'Goodbye Jordan', 'Goodbye']


    while (True):
        user_input = input("me: ")

        if (user_input.lower() in bye_list):
            print("Jordan: Goodbye and have a blessed day")
            break

        response = Bot.get_response(user_input)
        print("Jordan: ", response)












    
