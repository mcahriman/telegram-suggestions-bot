from dotenv import load_dotenv
import os

load_dotenv()

# Bot Data
TOKEN = os.getenv("TOKEN")  # Get your bot token using https://t.me/BotFather

# Support Chat
# To find out your channels ID use: https://t.me/getidsbot
CHAT_ID = os.getenv("CHAT_ID")

# Database Data
HOSTNAME = os.getenv("HOSTNAME")
DATABASE = os.getenv("DATABASE")
USERNAME = os.getenv("USERNAME")
PORT_ID = os.getenv("5432")
DB_PASS = os.getenv("DB_PASS")

# Predefined text to send, you can change its values to customize your own bot
TEXT_MESSAGES = {
    'start':
    'Welcome to Suggestions Bot 👋 \n\n Please, send your message and we will process your request.',
    'message_template':
    '<i>Message from: <b>@{0}</b>.</i>\n\n{1}<b>id: {2}</b>',
    'is_banned':
    '❌ User is banned!',
    'has_banned':
    '✅ User has been successfully banned!',
    'already_banned':
    '❌ User is already banned!',
    'has_unbanned':
    '✅ User has been successfully un-banned!',
    'not_banned':
    '❌ There is no such user in the ban list!',
    'user_banned':
    '🚫 You cannot send messages to this bot!',
    'user_unbanned':
    '🥳 You have proven your innocence, and now you can write to this bot again!',
    'user_reason_banned':
    '🚫 You cannot send messages to this bot due to the reason: <i>{}</i>.',
    'pending':
    'Thank you for your request! We are already into processing it.',
    'unsupported_format':
    '❌ Format of your message is not supported and it will not be forwarded.',
    'message_not_found':
    '❌ It looks like your message was sent more that a day ago. Message to edit was not found!',
    'message_was_not_edited':
    '❌ Unfortunately you cannot edit images/videos themselves.'
    'Please, send a new message.',
    'reply_error':
    '❌ Please, reply with /ban or /unban only on forwarded from user messages!'
}
