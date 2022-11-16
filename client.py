import discord
from discord import Embed, app_commands
import os
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


async def load_extensions():
    for filename in os.listdir('../Pytha/Events'):
        if filename.endswith('.py') and filename != '__init__.py':
            await client.load_extension(f'Events.{filename[:-3]}')


@client.event
async def on_connect():
    print("Connected!")
    client.tree.copy_global_to(guild=discord.Object(id=817021838311292978))
    await client.tree.sync()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Minecraft'))
    print(f"logged in as {client.user}")


async def main():
    async with client:
        print("Loading extensions..")
        await load_extensions()
        await client.start(TOKEN)


TOKEN = 'MTAxNjY3MzE3ODkyOTYwMjY5MA.G1sVVC.8XlfRe64P9cGQoC2mwyNuFLyM1a2uuV1qtHFEs'

asyncio.run(main())
