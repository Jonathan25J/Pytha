import discord
from discord import app_commands
from discord.ext import commands


async def setup(client):
    await client.add_cog(gameCommands(client))


async def begin(interaction):
    embed = discord.Embed(description="Game-menu",
                          color=0x76c1cb)
    embed.set_thumbnail(url="https://i.pinimg.com/originals/dd/95/b6/dd95b6f83b8320065f88cf8fa0c2aa8c.jpg")
    embed.add_field(name="Go into the woods", value="fight bosses in the woods", inline=False)
    embed.add_field(name="Search chests", value="find chests with possible boosts", inline=False)
    embed.add_field(name="Challenge final boss", value="high stats required", inline=False)
    view = gameMenu()
    return await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


user_found = False


class gameCommands(commands.Cog):
    def __init__(self, client):
        self.synced = False
        self.client = client

    @app_commands.command(name="gamemenu", description="Reveals the game menu")
    async def gameMenu(self, interaction: discord.Interaction) -> None:
        await inGame(interaction)
        if user_found:
            await begin(interaction)


class gameMenu(discord.ui.View):
    def __int__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Go into the woods", style=discord.ButtonStyle.blurple)
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
        from Events.bosses import getBoss
        await getBoss(interaction)

    @discord.ui.button(label="Search chests", style=discord.ButtonStyle.blurple)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        from Events.chests import getChests
        await getChests(interaction)

    @discord.ui.button(label="Challenge final boss", style=discord.ButtonStyle.blurple)
    async def button2(self, interaction: discord.Interaction, button: discord.ui.Button):
        from Events.finalboss import tarrasque
        from Events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health < 2000:
                    embed = discord.Embed(color=0xf9eb48)
                    embed.set_thumbnail(
                        url="https://static.wikia.nocookie.net/forgottenrealms/images/d/df/Monster_Manual_5e_"
                            "-_Tarrasque_-_Cory_Trego-Erdner_-_p287.jpg/revision/latest?cb=20200506174611")
                    embed.add_field(name="Not enough HP", value="You need at least 2000 HP to defeat the final boss",
                                    inline=False)
                    await interaction.response.send_message(embed=embed)
                else:
                    await tarrasque(interaction)


async def inGame(interaction):
    global user_found
    user_found = False
    from Events.generalCommands import users, auto_respond
    if isinstance(interaction.channel, discord.TextChannel):
        return await auto_respond(interaction)
    else:
        for user in users:
            if user.username == str(interaction.user):
                user_found = True
    if not user_found:
        embed = discord.Embed(title="No user found",
                              description="You didn't start the game, start the game with /start",
                              color=0xa04b4b)
        embed.set_author(name="Pytha-respond",
                         icon_url="https://mir-s3-cdn-cf.behance.net/project_modules/1400/f5643096750899"
                                  ".5eb54f3381b8f.png")
        embed.set_thumbnail(
            url="https://mir-s3-cdn-cf.behance.net/project_modules/1400/f5643096750899.5eb54f3381b8f.png")
        return await interaction.response.send_message(embed=embed, ephemeral=True)
