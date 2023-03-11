import Constants as keys
from telegram.ext import *
import Response as R

print("Bot started...")
def start_command(update, context):
    update.message.reply_text('Type Something random to get started!')

    def help_command(update, context):
    update.message.reply_text('If you need help, go and search google!')
    def handle_message(update, context):
        text = str(update.message.text).lower()
        response = R.sample_responses(text)

        update.message.reply_text(response)

    def error(update, context):
        print(f"Update {update} caused error {context.error}")

        def main ():
            updater = updater(keys.API_KEY, use_context=True)
            dp = updater.dispatcher

            dp.add_handler(CommandHandler("start", start_command))
            dp.add_handler(CommandHandler("start", help_command))

            dp.add_handler(MessageHandler(Filters.text, handle_message))
            dp.add_error_handler(error)

            updater.start_polling(0)
            updater.idle()

            main()