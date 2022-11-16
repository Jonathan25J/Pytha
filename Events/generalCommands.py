import discord
from discord import app_commands
from discord.ext import commands

from Events.gameCommands import begin


class User():
    def __init__(self, character: str, username: str, health: int, strength: int):
        self.character = character
        self.username = username
        self.health = health
        self.strength = strength

    def hpGet(self, amount: int):
        self.health += amount

    def hpLost(self, amount: int):
        self.health -= amount

    def __repr__(self):
        return f"User(character={self.character}, username={self.username}, health={self.health}, " \
               f"strength={self.strength})"


users = []


class generalCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @app_commands.command(name="register", description="A new adventure!")
    async def slash(self, interaction: discord.Interaction) -> None:
        if isinstance(interaction.channel, discord.TextChannel):
            embed = discord.Embed(color=0xf3a216)
            embed.add_field(name="Registration", value="You have been registered!", inline=False)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            embed1 = discord.Embed(color=0x2bb8d4)
            embed1.set_thumbnail(
                url="https://mir-s3-cdn-cf.behance.net/project_modules/1400/f5643096750899.5eb54f3381b8f.png")
            embed1.add_field(name="Pytha", value="Welcome I am Pytha", inline=False)
            await interaction.user.send(embed=embed1)

        else:
            embed2 = discord.Embed(description=":)", color=0x2bb8d4)
            embed2.set_thumbnail(
                url="https://mir-s3-cdn-cf.behance.net/project_modules/1400/f5643096750899.5eb54f3381b8f.png")
            await interaction.response.send_message(embed=embed2)

    @app_commands.command(name="start", description="Start the game")
    async def start(self, interaction: discord.Interaction) -> None:
        if isinstance(interaction.channel, discord.TextChannel):
            await auto_respond(interaction)

        else:
            embed = discord.Embed(description="Select your build", color=0x2d7d46)
            embed.set_thumbnail(
                url="https://www.wargamer.com/wp-content/sites/wargamer/2022/02/dnd-dragons-rulebook-cover.jpg")
            embed.add_field(name="Tank", value="HP:80", inline=True)
            embed.add_field(name="Strength", value="HP: 40", inline=True)
            embed.add_field(name="Sorcery", value="HP: 20", inline=True)
            embed.add_field(name="ㅤ ", value="Strength: 20", inline=True)
            embed.add_field(name="ㅤ ", value="Strength: 35", inline=True)
            embed.add_field(name="ㅤ ", value="Strength: 55", inline=True)
            embed.add_field(name="ㅤ ", value="Luck: 0.3", inline=True)
            embed.add_field(name="ㅤ ", value="Luck: 0.5", inline=True)
            embed.add_field(name="ㅤ  ", value="Luck: 0.8", inline=True)
            view = startMenu()
            await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

    @app_commands.command(name="stats", description="Check stats")
    async def stats(self, interaction: discord.Interaction) -> None:
        if isinstance(interaction.channel, discord.TextChannel):
            await auto_respond(interaction)
        else:
            for user in users:
                if user.username == str(interaction.user):
                    embed = discord.Embed(color=0x3994db)
                    embed.set_thumbnail(url="https://i.ytimg.com/vi/w-DIJq3ZYpI/maxresdefault.jpg")
                    embed.add_field(name="Stats", value=str(f"build: {user.character}"), inline=False)
                    embed.add_field(name="ㅤ ", value=str(f"HP: {user.health}"), inline=False)
                    embed.add_field(name="ㅤ ", value=str
                    (f"Strength: {user.strength}"), inline=False)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                    break
            else:
                embed1 = discord.Embed(title="No user found",
                                       description="You don't have stored any stats, start the game with /start",
                                       color=0xa04b4b)
                embed1.set_author(name="Pytha-respond",
                                  icon_url="https://mir-s3-cdn-cf.behance.net/project_modules/1400/f5643096750899"
                                           ".5eb54f3381b8f.png")
                embed1.set_thumbnail(
                    url="https://mir-s3-cdn-cf.behance.net/project_modules/1400/f5643096750899.5eb54f3381b8f.png")
                await interaction.response.send_message(embed=embed1, ephemeral=True)

    @app_commands.command(name="reset", description="Resets your game")
    async def reset(self, interaction: discord.Interaction) -> None:
        if isinstance(interaction.channel, discord.TextChannel):
            await auto_respond(interaction)
        else:
            for user in users:
                if user.username == str(interaction.user):
                    users.remove(user)
                    embed = discord.Embed(color=0x7cf1f3)
                    embed.add_field(name="Reset", value="Your stats has been reset!", inline=True)
                    await interaction.response.send_message(embed=embed)
                    break
            else:
                embed = discord.Embed(color=0x7cf1f3)
                embed.add_field(name="Reset", value="No user has been found", inline=True)
                await interaction.response.send_message(embed=embed)


class startMenu(discord.ui.View):
    def __int__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Tank", style=discord.ButtonStyle.green)
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
        for user in users:
            if user.username == str(interaction.user):
                embed = discord.Embed(color=0xf3a216)
                embed.add_field(name="Pytha", value="You have already selected a build!", inline=False)
                await interaction.response.send_message(embed=embed)
                break
        else:
            embed = discord.Embed(color=0xf3a216)
            embed.add_field(name="Pytha", value="You have selected the Tank build", inline=False)
            users.append(User("Tank", str(interaction.user), 80, 20))
            await interaction.user.send(embed=embed)
            await begin(interaction)

    @discord.ui.button(label="Strength", style=discord.ButtonStyle.green)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        for user in users:
            if user.username == str(interaction.user):
                embed = discord.Embed(color=0xf3a216)
                embed.add_field(name="Pytha", value="You have already selected a build!", inline=False)
                await interaction.response.send_message(embed=embed)
                break
        else:
            embed1 = discord.Embed(color=0xf3a216)
            embed1.add_field(name="Pytha", value="You have selected the Strength build", inline=False)
            users.append(User("Strength", str(interaction.user), 40, 35))
            await interaction.user.send(embed=embed1)
            await begin(interaction)

    @discord.ui.button(label="Sorcery", style=discord.ButtonStyle.green)
    async def button2(self, interaction: discord.Interaction, button: discord.ui.Button):
        for user in users:
            if user.username == str(interaction.user):
                embed = discord.Embed(color=0xf3a216)
                embed.add_field(name="Pytha", value="You have already selected a build!", inline=False)
                await interaction.response.send_message(embed=embed)
                break
        else:
            embed2 = discord.Embed(color=0xf3a216)
            embed2.add_field(name="Pytha", value="You have selected the Sorcery build", inline=False)
            users.append(User("Sorcery", str(interaction.user), 20, 55))
            await interaction.user.send(embed=embed2)
            await begin(interaction)


async def auto_respond(interaction):
    if isinstance(interaction.channel, discord.TextChannel):
        embed = discord.Embed(title="TextChannel", description="You can only use this command in DM",
                              color=0xa04b4b)
        embed.set_author(name="Pytha-respond",
                         icon_url="https://mir-s3-cdn-cf.behance.net/project_modules/1400/f5643096750899"
                                  ".5eb54f3381b8f.png")
        embed.set_thumbnail(
            url="https://mir-s3-cdn-cf.behance.net/project_modules/1400/f5643096750899.5eb54f3381b8f.png")

        return await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(client):
    await client.add_cog(generalCommands(client))
