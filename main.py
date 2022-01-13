from logging import Filter
from telegram.ext import updater
import constants as keys
from telegram.ext import *
import responses as r 

print("Bot is running ")

def start_command(update, context):

    msg = """
#      __  ____   __        
#    /   \(_ __ \ /   \      
#    (  0 )/ __/(  0 )    
#    \__/(____) \__/       
                          v1.0
                   

⭕️ Commands:-

/calc1  : شيتات الحسبان سمستر 1
/stats1  : شيتات الاحصاء سمستر 1
/linear1 : شيتات الجبر سمستر 1
/cs1     : شيتات الحاسوب سمستر 1
    """
    update.message.reply_text(msg)

def helpme(update , context):

    msg = """
#      __  ____   __        
#    /   \(_ __ \ /   \      
#    (  0 )/ __/(  0 )    
#    \__/(____) \__/       
                          v1.0
                   

⭕️ Commands:-

/calc1  : شيتات الحسبان سمستر 1
/stats1  : شيتات الاحصاء سمستر 1
/linear1 : شيتات الجبر سمستر 1
/cs1     : شيتات الحاسوب سمستر 1
    """
    update.message.reply_text(msg)

def handle_message(update, context):
    text = update.message.text
    response = r.res(text)
    update.message.reply_text(response)
def error(update , context):
    print(f"Update {update} caused error {context.error}")

# ///////////////////////////////////////////////////////////////////////////

def calc1(update, context):
  update.message.reply_text("جاري ارسال شيتات الحسبان 🗂")
  for i in range(1,10):
    context.bot.sendDocument(update.effective_chat.id , document=open(f"./sheets/calc1/calc{i}.pdf" , 'rb'))

def linear1(update, context):
 update.message.reply_text("جاري ارسال شيتات الجبر 🗂")
 for i in range(1,10):
     context.bot.sendDocument(update.effective_chat.id , document=open(f"./sheets/linear1/{i}.pdf" , 'rb'))
  
def stats1(update, context):
    update.message.reply_text("جاري ارسال شيتات الاحصاء 🗂")
    for i in range(1,10):
     context.bot.sendDocument(update.effective_chat.id , document=open(f"./sheets/stats1/Statistics_lecture{i}.pdf" , 'rb'))

def cs1(update, context):
    update.message.reply_text("جاري ارسال شيتات الحاسوب 🗂")
    for i in range(1,11):
     context.bot.sendDocument(update.effective_chat.id , document=open(f"./sheets/cs1/{i}.pdf" , 'rb'))

 

# ////////////////////////////
def main():
    updater = Updater(keys.api_key, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("helpme", helpme))
    dp.add_handler(CommandHandler("calc1", calc1))
    dp.add_handler(CommandHandler("stats1", stats1))
    dp.add_handler(CommandHandler("linear1", linear1))
    dp.add_handler(CommandHandler("cs1", cs1))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
main()