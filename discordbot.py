import discord
import os
import certifi
import ssl
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fix SSL certificate issues on macOS
# Set SSL certificate file path
os.environ['SSL_CERT_FILE'] = certifi.where()

# Create custom SSL context
ssl_context = ssl.create_default_context(cafile=certifi.where())

# Patch aiohttp's TCPConnector to use our SSL context
import aiohttp.connector

_original_init = aiohttp.connector.TCPConnector.__init__

def _patched_init(self, *args, ssl=None, **kwargs):
    """Override to use certifi SSL context by default"""
    if ssl is None:
        ssl = ssl_context
    _original_init(self, *args, ssl=ssl, **kwargs)

aiohttp.connector.TCPConnector.__init__ = _patched_init

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return
    
    if message.content.startswith('$hello'):
      await message.channel.send('Hello!')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

# Get token from environment variable
token = os.getenv('DISCORD_BOT_TOKEN')
if not token:
    raise ValueError("DISCORD_BOT_TOKEN environment variable is not set!")

client.run(token)


