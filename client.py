import discord
import asyncio
import os
import logging
from discord import Embed, app_commands
from discord.ext import commands
from dotenv import load_dotenv

# Bot listens to all Discord events and responds to commands with an '!'
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load variables from .env file
load_dotenv()

async def load_extensions():
    for filename in os.listdir('./events'):
        if filename.endswith('.py') and filename != '__init__.py':
            await client.load_extension(f'events.{filename[:-3]}')


@client.event
async def on_connect():
    logging.info("Connected!")
    client.tree.copy_global_to(guild=discord.Object(id=817021838311292978))
    await client.tree.sync()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Minecraft'))
    logging.info(f"Logged in as {client.user}")


async def main():
    try: 
        async with client:
            logging.info("Loading extensions..")
            await load_extensions()
            await client.start(os.getenv("BOT_TOKEN"))
    except Exception as e:
        logging.exception("An error occurred while starting the bot", exc_info=e)

asyncio.run(main())
