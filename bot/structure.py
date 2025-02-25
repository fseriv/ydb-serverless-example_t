from functools import partial

from telebot import TeleBot, custom_filters

from bot import handlers as handlers
#from bot import states as bot_states

class Handler:
    def __init__(self, callback, **kwargs):
        self.callback = callback
        self.kwargs = kwargs

def get_start_handlers():
    return [
        Handler(callback=handlers.handle_start, commands=["start"]),
    ]

def create_bot(bot_token):#, pool):
    #state_storage = bot_states.StateYDBStorage(pool)
    bot = TeleBot(bot_token)#, state_storage=state_storage)
    handlers = []
    handlers.extend(get_start_handlers())
    #handlers.extend(get_registration_handlers())
    #handlers.extend(get_show_data_handlers())
    #handlers.extend(get_delete_account_handlers())
    #handlers.extend(get_change_data_handlers())

    for handler in handlers:
        bot.register_message_handler(
            #partial(handler.callback, pool=pool), **handler.kwargs, pass_bot=True
            partial(handler.callback), **handler.kwargs, pass_bot=True
        ) 

    bot.add_custom_filter(custom_filters.StateFilter(bot))
    return bot