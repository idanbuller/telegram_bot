from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram_directory.message_manager

mm = telegram_directory.message_manager.MessageManager()
jobsDict = {}


def start(bot, update):
    if update.message.chat_id not in jobsDict:
        jobsDict[update.message.chat_id] = job_q.run_repeating(myJob, context=update.message.chat_id, interval=15,
                                                               first=0)
        bot.send_message(chat_id=update.message.chat_id, text="Metal suggestions are on")


def stopLoop(bot, update):
    jobsDict[update.message.chat_id].schedule_removal()
    del jobsDict[update.message.chat_id]
    bot.send_message(chat_id=update.message.chat_id, text="Metal suggestions are off")


def msg(bot, update):
    if "" in update.message.text:
        mm.SaveMsg(update.message.text)
        bot.send_message(chat_id=update.message.chat_id, text=f"{update.message.text.upper()} \m/")



updater = Updater('API')


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('stop', stopLoop))

updater.dispatcher.add_handler(MessageHandler(Filters.text, msg))

job_q = updater.job_queue

updater.start_polling()
updater.idle()
