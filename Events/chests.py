import discord
from discord.ext import commands
import random


async def setup(client):
    await client.add_cog(chests(client))


class chests(commands.Cog):

    def __init__(self, client):
        self.client = client


async def getChests(interaction):
    golden_chest = discord.Embed(title="Golden Chest", color=0x499fc0)
    golden_chest.set_thumbnail(
        url="https://images-ext-2.discordapp.net/external/7fgMPYAXw0eoEyL-ttynfi4mtIFNL3gM1zdmH3Grhjo/%3Fcb"
            "%3D20201020025220/https/static.wikia.nocookie.net/clashroyale/images/8/8b/GoldenChest.png/revision"
            "/latest")
    golden_chest.add_field(name="Bet", value="50 HP", inline=True)
    golden_chest.add_field(name="Win multipliers", value="2x", inline=True)
    golden_chest.add_field(name="Lose chances", value="75%", inline=True)
    view = golden_chest_v()
    await interaction.user.send(embed=golden_chest, view=view)

    kingchest = discord.Embed(title="King's Chest", color=0x2e3b67)
    kingchest.set_thumbnail(
        url="https://static.wikia.nocookie.net/clashroyale/images/5/51/Kings_Chest.png/revision/latest/scale-to-width"
            "-down/120?cb=20171211182109")
    kingchest.add_field(name="Bet", value="100 HP", inline=True)
    kingchest.add_field(name="Win multipliers", value="2x", inline=True)
    kingchest.add_field(name="Lose chances", value="65%", inline=True)
    view = king_chest_v()
    await interaction.user.send(embed=kingchest, view=view)

    magical_chest = discord.Embed(title="Magical Chest", color=0xff62ff)
    magical_chest.set_thumbnail(
        url="https://static.wikia.nocookie.net/clashroyale/images/9/93/MagicalChest.png/revision/latest?cb=20160312171354")
    magical_chest.add_field(name="Bet", value="150 HP", inline=True)
    magical_chest.add_field(name="Win multipliers", value="2x 3x", inline=True)
    magical_chest.add_field(name="Lose chances", value="55%", inline=True)
    view = magical_chest_v()
    await interaction.user.send(embed=magical_chest, view=view)

    mega_lightning_chest = discord.Embed(title="Mega Lightning Chest", color=0x8dc9f7)
    mega_lightning_chest.set_thumbnail(
        url="https://www.deckshop.pro/img/chests/mlc.png")
    mega_lightning_chest.add_field(name="Bet", value="300 HP", inline=True)
    mega_lightning_chest.add_field(name="Win multipliers", value="2x 3x", inline=True)
    mega_lightning_chest.add_field(name="Lose chances", value="45%", inline=True)
    view = mega_lightning_chest_v()
    await interaction.user.send(embed=mega_lightning_chest, view=view)

    legendary_kings_chest = discord.Embed(title="Legendary King's Chest", color=0x6ea3b9)
    legendary_kings_chest.set_thumbnail(
        url="https://static.wikia.nocookie.net/clashroyale/images/4/42/Legendary_Kings_Chest.png/revision/latest?cb"
            "=20171215191757")
    legendary_kings_chest.add_field(name="Bet", value="600 HP", inline=True)
    legendary_kings_chest.add_field(name="Win multipliers", value="2x 3x 4x", inline=True)
    legendary_kings_chest.add_field(name="Lose chances", value="40%", inline=True)
    view = legendary_kings_chest_v()
    await interaction.response.send_message(embed=legendary_kings_chest, view=view)


class golden_chest_v(discord.ui.View):
    def __int__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Bet", style=discord.ButtonStyle.gray)
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
        from Events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health >= 50:
                    chance = random.uniform(0.0, 1)
                    if chance <= 0.25:
                        embed = discord.Embed(color=0x499fc0)
                        embed.add_field(name="Golden Chest", value="You've won you earned 100HP", inline=True)
                        await interaction.response.send_message(embed=embed)
                        user.health += 100
                    else:
                        user.health -= 50
                        embed = discord.Embed(color=0x499fc0)
                        embed.add_field(name="Golden Chest", value="You've lost", inline=True)
                        await interaction.response.send_message(embed=embed)
                else:
                    embed = discord.Embed(color=0x499fc0)
                    embed.add_field(name="Golden Chest", value="You don't have enough HP", inline=True)
                    await interaction.response.send_message(embed=embed)


class king_chest_v(discord.ui.View):
    def __int__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Bet", style=discord.ButtonStyle.gray)
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
        from Events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health >= 100:
                    chance = random.uniform(0.0, 1)
                    if chance <= 0.35:
                        embed = discord.Embed(color=0x2e3b67)
                        embed.add_field(name="King's Chest", value="You've won you earned 200HP", inline=True)
                        await interaction.response.send_message(embed=embed)
                        user.health += 200
                    else:
                        user.health -= 100
                        embed = discord.Embed(color=0x2e3b67)
                        embed.add_field(name="King's' Chest", value="You've lost", inline=True)
                        await interaction.response.send_message(embed=embed)
                else:
                    embed = discord.Embed(color=0x2e3b67)
                    embed.add_field(name="King's Chest", value="You don't have enough HP", inline=True)
                    await interaction.response.send_message(embed=embed)


class magical_chest_v(discord.ui.View):
    def __int__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Bet", style=discord.ButtonStyle.gray)
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
        from Events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health >= 150:
                    chance = random.uniform(0.0, 1)
                    if chance <= 0.45:
                        multiplier = random.randint(2, 3)
                        result = 150 * multiplier
                        embed = discord.Embed(color=0xff62ff)
                        embed.add_field(name="Magical Chest",
                                        value=f"You've won ({multiplier}x) you earned {result}HP", inline=True)
                        await interaction.response.send_message(embed=embed)
                        user.health += result
                    else:
                        user.health -= 150
                        embed = discord.Embed(color=0xff62ff)
                        embed.add_field(name="Magical Chest", value="You've lost", inline=True)
                        await interaction.response.send_message(embed=embed)
                else:
                    embed = discord.Embed(color=0xff62ff)
                    embed.add_field(name="Magical Chest", value="You don't have enough HP", inline=True)
                    await interaction.response.send_message(embed=embed)


class mega_lightning_chest_v(discord.ui.View):
    def __int__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Bet", style=discord.ButtonStyle.gray)
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
        from Events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health >= 300:
                    chance = random.uniform(0.0, 1)
                    if chance <= 0.55:
                        multiplier = random.uniform(0.0, 1)
                        if multiplier <= 0.75:
                            multiplier = 2
                        else:
                            multiplier = 3
                        result = 300 * multiplier
                        embed = discord.Embed(color=0x8dc9f7)
                        embed.add_field(name="Mega Lightning Chest",
                                        value=f"You've won ({multiplier}x) you earned {result}HP", inline=True)
                        await interaction.response.send_message(embed=embed)
                        user.health += result
                    else:
                        user.health -= 300
                        embed = discord.Embed(color=0x8dc9f7)
                        embed.add_field(name="Mega Lightning Chest", value="You've lost", inline=True)
                        await interaction.response.send_message(embed=embed)
                else:
                    embed = discord.Embed(color=0x8dc9f7)
                    embed.add_field(name="Mega Lightning Chest", value="You don't have enough HP", inline=True)
                    await interaction.response.send_message(embed=embed)


class legendary_kings_chest_v(discord.ui.View):
    def __int__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Bet", style=discord.ButtonStyle.gray)
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
        from Events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health >= 600:
                    chance = random.uniform(0.0, 1)
                    if chance <= 0.60:
                        multiplier = random.uniform(0.0, 1)
                        if multiplier <= 0.40:
                            multiplier = 2
                        elif 0.41 <= multiplier <= 0.80:
                            multiplier = 3
                        else:
                            multiplier = 4
                        result = 600 * multiplier
                        embed = discord.Embed(color=0x6ea3b9)
                        embed.add_field(name="Legendary King's Chest",
                                        value=f"You've won ({multiplier}x) you earned {result}HP", inline=True)
                        await interaction.response.send_message(embed=embed)
                        user.health += result
                    else:
                        user.health -= 600
                        embed = discord.Embed(color=0x6ea3b9)
                        embed.add_field(name="Legendary King's Chest", value="You've lost", inline=True)
                        await interaction.response.send_message(embed=embed)
                else:
                    embed = discord.Embed(color=0x6ea3b9)
                    embed.add_field(name="Legendary King's Chest", value="You don't have enough HP", inline=True)
                    await interaction.response.send_message(embed=embed)
