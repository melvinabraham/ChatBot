from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot1 = ChatBot('Jon',
    logic_adapters=[
    {

        'import_path':    'chatterbot.logic.BestMatch'
    
    },
    {
        'import_path': 'chatterbot.logic.SpecificResponseAdapter',
        'input_text': 'Help',
        'output_text': 'Sorry if I startled you! You can get more help at www.anokha.edu'
    }
    ],
    #filters=[
    #   'chatterbot.filters.RepetitiveResponseFilter'
    #],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='try1-database'
)
chatbot1.set_trainer(ChatterBotCorpusTrainer)

print "Hello,Welcome to chatbot. Type Help for Help. Otherwise you can keep typing"
# Train based on the english corpus

#chatbot1.train("/home/gautam/Desktop/chatbot/chat-bot-amrita/chatterbot/corpus/data/english/amrita_queries")
chatbot1.train("/home/melvin/Desktop/projects/chat-bot-amrita/chatterbot/corpus/data/english/anokha_queries")
#chatbot1.train("/home/melvin/Desktop/projects/chat-bot-amrita/chatterbot/corpus/data/english/conversations_corpus")
while True:
    try:
        

# Get a response to an input statement
        chatbot1_input=chatbot1.get_response(None)

       # response=chatbot1.get_response("Help!")
       #print response
        


    except(KeyboardInterrupt, EOFError, SystemExit):
                     break
