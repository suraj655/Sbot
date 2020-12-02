from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
# Creating ChatBot Instance
chatbot = ChatBot('CoronaBot')

 # Training with Personal Ques & Ans 
conversation = [
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Bot , i am created by suraj',
    'how are you ?',
    'I am doing great these days',
    'In which city you live ?',
    'I live in jodhpur',
    'In which language you talk?',
    ' I mostly talk in english',
    'Could you hear me?',
    'Yes I can',
    'You are beautiful',
    'Thank you very much',
    'How old are you',
    'Im too young as you have created me yesterday only!'
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 
