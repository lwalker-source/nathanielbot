import discord
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

# Get token from environment variable
token = os.getenv('DISCORD_BOT_TOKEN')
if not token:
    raise ValueError("DISCORD_BOT_TOKEN environment variable is not set!")

client.run(token)