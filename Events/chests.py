import discord
import random
from discord.ext import commands
from utils import images_folder, get_image

async def setup(client):
    await client.add_cog(chests(client))


class chests(commands.Cog):

    def __init__(self, client):
        self.client = client


async def getChests(interaction):
    golden_chest = discord.Embed(title="Golden Chest", color=0x499fc0)
    thumbnail = get_image(f'{images_folder}chests\\golden_chest.png')
    golden_chest.set_thumbnail(url=f'attachment://{thumbnail.filename}')
    golden_chest.add_field(name="Bet", value="50 HP", inline=True)
    golden_chest.add_field(name="Win multipliers", value="2x", inline=True)
    golden_chest.add_field(name="Lose chances", value="75%", inline=True)
    view = golden_chest_v()
    await interaction.user.send(embed=golden_chest, view=view, file=thumbnail)

    kingchest = discord.Embed(title="King's Chest", color=0x2e3b67)
    thumbnail = get_image(f'{images_folder}chests\\kings_chest.png')
    kingchest.set_thumbnail(url=f'attachment://{thumbnail.filename}')
    kingchest.add_field(name="Bet", value="100 HP", inline=True)
    kingchest.add_field(name="Win multipliers", value="2x", inline=True)
    kingchest.add_field(name="Lose chances", value="65%", inline=True)
    view = king_chest_v()
    await interaction.user.send(embed=kingchest, view=view, file=thumbnail)

    magical_chest = discord.Embed(title="Magical Chest", color=0xff62ff)
    thumbnail = get_image(f'{images_folder}chests\\magical_chest.png')
    magical_chest.set_thumbnail(url=f'attachment://{thumbnail.filename}')
    magical_chest.add_field(name="Bet", value="150 HP", inline=True)
    magical_chest.add_field(name="Win multipliers", value="2x 3x", inline=True)
    magical_chest.add_field(name="Lose chances", value="55%", inline=True)
    view = magical_chest_v()
    await interaction.user.send(embed=magical_chest, view=view, file=thumbnail)

    mega_lightning_chest = discord.Embed(title="Mega Lightning Chest", color=0x8dc9f7)
    thumbnail = get_image(f'{images_folder}chests\\mega_lightning_chest.png')
    mega_lightning_chest.set_thumbnail(url=f'attachment://{thumbnail.filename}')
    mega_lightning_chest.add_field(name="Bet", value="300 HP", inline=True)
    mega_lightning_chest.add_field(name="Win multipliers", value="2x 3x", inline=True)
    mega_lightning_chest.add_field(name="Lose chances", value="45%", inline=True)
    view = mega_lightning_chest_v()
    await interaction.user.send(embed=mega_lightning_chest, view=view, file=thumbnail)

    legendary_kings_chest = discord.Embed(title="Legendary King's Chest", color=0x6ea3b9)
    thumbnail = get_image(f'{images_folder}chests\\legendary_kings_chest.png')
    legendary_kings_chest.set_thumbnail(url=f'attachment://{thumbnail.filename}')
    legendary_kings_chest.add_field(name="Bet", value="600 HP", inline=True)
    legendary_kings_chest.add_field(name="Win multipliers", value="2x 3x 4x", inline=True)
    legendary_kings_chest.add_field(name="Lose chances", value="40%", inline=True)
    view = legendary_kings_chest_v()
    await interaction.response.send_message(embed=legendary_kings_chest, view=view, file=thumbnail)


class golden_chest_v(discord.ui.View):
    def __int__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Bet", style=discord.ButtonStyle.gray)
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
        from events.generalCommands import users
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
        from events.generalCommands import users
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
        from events.generalCommands import users
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
        from events.generalCommands import users
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
        from events.generalCommands import users
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
