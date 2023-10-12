import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

nltk.download('vader_lexicon')
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)['compound']

    if sentiment_score >= 0.05:
        return 'Positive'
    elif sentiment_score <= -0.05:
        return 'Отрицательный'
    else:
        return 'Neutral'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am a chatbot for analyzing the sentiment of text. Just send me a message and I will tell you what his mood is.')

def analyze_text(update: Update, context: CallbackContext) -> None:
    user_text = update.message.text
    sentiment_result = analyze_sentiment(user_text)
    update.message.reply_text(f'text tone: {sentiment_result}')

def main() -> None:
    updater = Updater("token")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, analyze_text))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
