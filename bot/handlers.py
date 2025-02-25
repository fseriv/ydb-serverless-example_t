from bot import keyboards#, states
#from database import model as db_model
from logs import logged_execution
from user_interaction import texts

@logged_execution
def handle_start(message, bot):#, pool):
    bot.send_message(message.chat.id, texts.START, reply_markup=keyboards.EMPTY)
