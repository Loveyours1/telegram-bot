import urllib.parse
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8758252887:AAF3bhqtdBtwNg3KtqG9btpBnmdxB0cg06w"

cached_video_id = None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global cached_video_id
    chat_id = update.effective_chat.id
    
    caption_text = (
        "The next phase of ETH staking. Private validator nodes, "
        "early access now open. See the proof, then join the waitlist."
    )
    
    # Direct user link WITH prefilled message text
    raw_text = "Hi, I'm interested in the ETH Node Validator program. Please send me the details."
    encoded_text = urllib.parse.quote(raw_text)
    contact_link = f"https://t.me/galaxydigitalstake?text={encoded_text}"
    
    keyboard = [
        [InlineKeyboardButton("Get Early Access", url=contact_link)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if cached_video_id:
        await context.bot.send_video(
            chat_id=chat_id,
            video=cached_video_id,
            caption=caption_text,
            reply_markup=reply_markup
        )
    else:
        with open("video.mp4.MOV", "rb") as video_file:
            msg = await context.bot.send_video(
                chat_id=chat_id,
                video=video_file,
                caption=caption_text,
                reply_markup=reply_markup
            )
            cached_video_id = msg.video.file_id

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
