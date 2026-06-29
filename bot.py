import os
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

MY_USER_ID = 709421928208924682  # Replace with your Discord User ID

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author.bot:
        return

    # If someone mentions YOU
    if any(user.id == MY_USER_ID for user in message.mentions):
        await message.reply(
            "🐟 Cá đang lặn. Vui lòng đợi cá trồi lên lấy oxy rồi sẽ rep nhé!"
        )


client.run(TOKEN)