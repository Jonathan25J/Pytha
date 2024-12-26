import discord
import random
import os
from discord import app_commands
from discord.ext import commands
from utils import get_image


async def setup(client):
    await client.add_cog(bosses(client))


condition = 0
boss_count = 10
boss_type = 0
boss_level = 0
boss_name = []
boss_url = []
user_advantage = 0


async def getBoss(interaction):
    global user_advantage
    global condition
    global boss_count
    global boss_type
    global boss_level
    global boss_name
    global boss_url

    boss_name_1 = [
        "Woodie",
        "Bruzela",
        "Menhetten",
        "Brahla",
        "Owl",
        "Dron",
        "Trin",
        "Demogorgan",
        "Mind Flayer",
        "Vecna",
    ]

    boss_url_1 = [
        ["bosses", "level", "1", "woodie.jpg"],
        ["bosses", "level", "1", "bruzela.jpg"],
        ["bosses", "level", "1", "menhetten.jpg"],
        ["bosses", "level", "1", "brahla.jpg"],
        ["bosses", "level", "1", "owl.jpg"],
        ["bosses", "level", "1", "dron.jpg"],
        ["bosses", "level", "1", "trin.jpg"],
        ["bosses", "level", "1", "demogorgan.jpg"],
        ["bosses", "level", "1", "mind-flayer.jpg"],
        ["bosses", "level", "1", "vecna.jpg"],
    ]

    boss_name_2 = [
        "Flumphs",
        "Ghost",
        "Dragon turtle",
        "Moonstone Dragon",
        "Bandit",
        "Ghost Knight",
        "Vampire",
        "Shadow Dragon",
        "Gelatinious Cube",
        "Kraken",
    ]

    boss_url_2 = [
        ["bosses", "level", "2", "flumphs.jpg"],
        ["bosses", "level", "2", "ghost.jpg"],
        ["bosses", "level", "2", "dragon_turtle.jpg"],
        ["bosses", "level", "2", "moonstone_dragon.jpg"],
        ["bosses", "level", "2", "rogue.jpg"],
        ["bosses", "level", "2", "ghost_knight.jpg"],
        ["bosses", "level", "2", "vampire.jpg"],
        ["bosses", "level", "2", "shadow_dragon.png"],
        ["bosses", "level", "2", "gelatinous_cube.jpg"],
        ["bosses", "level", "2", "kraken.jpg"],
    ]

    boss_name_3 = [
        "Almiraj",
        "Sprite",
        "Modrons",
        "Kobold",
        "Skeletons",
        "Beholder",
        "Dracolich",
        "Earth Elemental",
        "Pit Fiend",
        "Ancient Red Dragon",
    ]

    boss_url_3 = [
        ["bosses", "level", "3", "almiraj.jpg"],
        ["bosses", "level", "3", "sprite.jpeg"],
        ["bosses", "level", "3", "modrons.jpg"],
        ["bosses", "level", "3", "kobold.jpg"],
        ["bosses", "level", "3", "skeletons.jpg"],
        ["bosses", "level", "3", "beholder.jpg"],
        ["bosses", "level", "3", "dracolich.jpg"],
        ["bosses", "level", "3", "earth_elemental.jpeg"],
        ["bosses", "level", "3", "pit_fiend.jpg"],
        ["bosses", "level", "3", "ancient_red_dragon.jpg"],
    ]

    condition = 0
    boss_name = random.choice([boss_name_1, boss_name_2, boss_name_3])
    if boss_name[0] == "Woodie":
        boss_url = boss_url_1
    elif boss_name[0] == "Flumphs":
        boss_url = boss_url_2
    elif boss_name[0] == "Almiraj":
        boss_url = boss_url_3
    boss_type = random.randint(1, boss_count)
    if boss_type <= 5:
        boss_level = random.randint(1, 10)
    else:
        boss_level = random.randint(6, 10)
    user_advantage = 0
    user_health = 0
    from events.generalCommands import users

    for user in users:
        if user.username == str(interaction.user):
            user_health += user.health
            if user.character == "Tank":
                user_advantage += 0.3
            elif user.character == "Strength":
                user_advantage += 0.5
            elif user.character == "Sorcery":
                user_advantage += 0.8
            else:
                continue
    if user_health == 0:
        embed = discord.Embed(color=0xB65A43)
        image = get_image('screens', 'dead.jpg')
        embed.set_image(url=f"attachment://{image.filename}")
        embed.add_field(name="You Died!", value=f"Try again next time", inline=False)
        await interaction.response.send_message(embed=embed, file=image)
    boss_color = [
        0x0DB537,
        0x0DB537,
        0x0DB537,
        0x0DB537,
        0xFBFF00,
        0xFBFF00,
        0xFBFF00,
        0xEC4109,
        0xEC4109,
        0xEC4109,
    ]
    result = (
        random.uniform(0, 3.34)
        + boss_level
        + (boss_type / 1.5)
        - user_advantage
        - (user_health / 400)
    )
    if result < 13.34:
        condition = 1
    embed = discord.Embed(
        title=f"{boss_name[boss_type - 1]}", color=boss_color[boss_level - 1]
    )
    image = get_image(*boss_url[boss_type - 1])
    embed.set_image(url=f"attachment://{image.filename}")
    embed.add_field(name="Level", value=f"{boss_level}", inline=False)
    embed.add_field(name=f"Strength", value=f"{boss_type}", inline=False)
    view = mechanics()
    return await interaction.response.send_message(
        embed=embed, view=view, ephemeral=True, file=image
    )


class bosses(commands.Cog):

    def __init__(self, client):
        self.client = client


class mechanics(discord.ui.View):
    def __int__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Defense", style=discord.ButtonStyle.green)
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(color=0xE1A90E)
        thumbnail = get_image(*boss_url[boss_type - 1])
        embed.set_thumbnail(url=f"attachment://{thumbnail.filename}")
        embed.add_field(
            name=f"{boss_name[boss_type - 1]}",
            value=f"You defended yourself, the boss ran away",
            inline=False,
        )

        await interaction.user.send(embed=embed)
        await getBoss(interaction)

    @discord.ui.button(label="Attack", style=discord.ButtonStyle.green)
    async def button1(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):

        if condition == 0:
            lost = random.randint(0, 2) + boss_type + 15
            embed = discord.Embed(color=0xBFBABA)
            thumbnail = get_image(*boss_url[boss_type - 1])
            embed.set_thumbnail(url=f"attachment://{thumbnail.filename}")
            embed.add_field(
                name=f"{boss_name[boss_type - 1]}",
                value=f"You've lost, you lost {lost} HP",
                inline=False,
            )
            from events.generalCommands import users

            for user in users:
                if user.username == str(interaction.user):
                    user.health -= lost
                    if user.health <= 0:
                        users.remove(user)
            await interaction.user.send(embed=embed, file=thumbnail)
            await getBoss(interaction)

        elif condition == 1:
            if boss_type <= 7:
                won = random.randint(0, 3) + boss_type
            else:
                won = random.randint(3, 6) + boss_type
            embed = discord.Embed(color=0x3455F9)
            thumbnail = get_image(*boss_url[boss_type - 1])
            embed.set_thumbnail(url=f"attachment://{thumbnail.filename}")
            embed.add_field(
                name=f"{boss_name[boss_type - 1]}",
                value=f"You've won!, you won {won} HP",
                inline=False,
            )
            from events.generalCommands import users

            for user in users:
                if user.username == str(interaction.user):
                    user.health += won
            await interaction.user.send(embed=embed, file=thumbnail)
            await getBoss(interaction)
