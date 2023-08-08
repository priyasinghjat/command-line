import nltk
nltk.download('punkt')

from nltk.chat.util import Chat, reflections

name = [
    ['my name is (.*)', ['Hi %1, how can I help you today?']],
    ['(hi|hello|hey|yo)', ['Hello, how can I assist you?']],
    ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun!']],
    ['(.*) (help|support)', ['Sure, I\'d be happy to help! How can I assist you today?']],
    ['(quit|bye|goodbye)', ['Goodbye, have a great day!']],
    ['(what\'s|how\'s) the weather', ['The weather is sunny today!']],
    ['(what\'s|how\'s) your day', ['I\'m just a computer program, I don\'t have feelings. But thank you for asking!']],
    ['(what|who) (is|are) you', ['I\'m a chatbot programmed in Python using the NLTK library.']],
    ['(what|who) created you', ['I was created by a human programmer.']],
    ['(how|what) can you help', ['I can assist with a variety of tasks, including answering questions, providing information, and offering support.']],
    ['(tell me|say) a joke', ['Why don\'t scientists trust atoms? Because they make up everything!']],
]


chatbot = Chat(name, reflections)
chatbot.converse()