from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

# Replace with your actual Telegram bot token
BOT_TOKEN = "6434489869:AAEL-vNKtN3fgDmnh3O8k0pALTfRyX54EAw"

# Initialize the bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Logging middleware to see bot's requests and responses in console
dp.middleware.setup(LoggingMiddleware())


# Echo handler
@dp.message_handler()
async def echo(message: types.Message):
    # Echo the received message back
    await message.reply(message.text)


# Start the bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
