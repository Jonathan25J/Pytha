import discord
import random
import os
from discord import app_commands
from discord.ext import commands
from utils import images_folder, get_image


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
    boss_filepath= f'{images_folder}bosses\\level'

    boss_name_1 = ['Woodie', 'Bruzela', 'Menhetten', 'Brahla', 'Owl', 'Dron', 'Trin', 'Demogorgan', 'Mind Flayer',
                   'Vecna']
    
    boss_url_1 = [f'{boss_filepath}\\1\\woodie.jpg',
                  f'{boss_filepath}\\1\\bruzela.jpg',
                  f'{boss_filepath}\\1\\menhetten.jpg',
                  f'{boss_filepath}\\1\\brahla.jpg',
                  f'{boss_filepath}\\1\\owl.jpg',
                  f'{boss_filepath}\\1\\dron.jpg',
                  f'{boss_filepath}\\1\\trin.jpg',
                  f'{boss_filepath}\\1\\demogorgan.jpg',
                  f'{boss_filepath}\\1\\mind-flayer.jpg',
                  f'{boss_filepath}\\1\\vecna.jpg']

    boss_name_2 = ['Flumphs', 'Ghost', 'Dragon turtle', 'Moonstone Dragon', 'Bandit', 'Ghost Knight', 'Vampire',
                   'Shadow Dragon', 'Gelatinious Cube', 'Kraken']
    
    boss_url_2 = [f'{boss_filepath}\\2\\flumphs.jpg',
                  f'{boss_filepath}\\2\\ghost.jpg',
                  f'{boss_filepath}\\2\\dragon_turtle.jpg',
                  f'{boss_filepath}\\2\\moonstone_dragon.jpg',
                  f'{boss_filepath}\\2\\rogue.jpg',
                  f'{boss_filepath}\\2\\ghost_knight.jpg',
                  f'{boss_filepath}\\2\\vampire.jpg',
                  f'{boss_filepath}\\2\\shadow_dragon.png',
                  f'{boss_filepath}\\2\\gelatinious-cube.jpg',
                  f'{boss_filepath}\\2\\kraken.jpg']


    boss_name_3 = ['Almiraj','Sprite','Modrons','Kobold','Skeletons','Beholder','Dracolich','Earth Elemental','Pit Fiend','Ancient Red Dragon']
    
    boss_url_3 = [f'{boss_filepath}\\3\\almiraj.jpg',
                  f'{boss_filepath}\\3\\sprite.jpeg',
                  f'{boss_filepath}\\3\\modrons.jpg',
                  f'{boss_filepath}\\3\\kobold.jpg',
                  f'{boss_filepath}\\3\\skeletons.jpg',
                  f'{boss_filepath}\\3\\beholder.jpg',
                  f'{boss_filepath}\\3\\dracolich.jpg',
                  f'{boss_filepath}\\3\\earth_elemental.jpeg',
                  f'{boss_filepath}\\3\\pit-fiend.jpg',
                  f'{boss_filepath}\\3\\ancient_red_dragon.jpg']
        
    condition = 0
    boss_name = random.choice([boss_name_1, boss_name_2, boss_name_3])
    if boss_name[0] == 'Woodie':
        boss_url = boss_url_1
    elif boss_name[0] == 'Flumphs':
        boss_url = boss_url_2
    elif boss_name[0] == 'Almiraj':
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
            if user.character == 'Tank':
                user_advantage += 0.3
            elif user.character == 'Strength':
                user_advantage += 0.5
            elif user.character == 'Sorcery':
                user_advantage += 0.8
            else:
                continue
    if user_health == 0:
        embed = discord.Embed(color=0xb65a43)
        image = get_image(f'{images_folder}screens\\dead.jpg')
        embed.set_image(url=f"attachment://{image.filename}")
        embed.add_field(name="You Died!", value=f"Try again next time", inline=False)
        await interaction.response.send_message(embed=embed, file=image)
    boss_color = [0x0db537, 0x0db537, 0x0db537, 0x0db537, 0xfbff00, 0xfbff00, 0xfbff00, 0xec4109,
                  0xec4109, 0xec4109]
    result = random.uniform(0, 3.34) + boss_level + (boss_type / 1.5) - user_advantage - (user_health / 400)
    if result < 13.34:
        condition = 1
    embed = discord.Embed(title=f'{boss_name[boss_type - 1]}', color=boss_color[boss_level - 1])
    image = get_image(f'{boss_url[boss_type - 1]}')
    embed.set_image(url=f"attachment://{image.filename}")
    embed.add_field(name="Level", value=f"{boss_level}", inline=False)
    embed.add_field(name=f"Strength", value=f"{boss_type}", inline=False)
    view = mechanics()
    return await interaction.response.send_message(embed=embed, view=view, ephemeral=True, file=image)
class bosses(commands.Cog):

    def __init__(self, client):
        self.client = client


class mechanics(discord.ui.View):
    def __int__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Defense", style=discord.ButtonStyle.green)
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(color=0xe1a90e)
        thumbnail = get_image(f'{boss_url[boss_type - 1]}')
        embed.set_thumbnail(url=f"attachment://{thumbnail.filename}")
        embed.add_field(name=f"{boss_name[boss_type - 1]}", value=f"You defended yourself, the boss ran away",
                        inline=False)

        await interaction.user.send(embed=embed)
        await getBoss(interaction)

    @discord.ui.button(label="Attack", style=discord.ButtonStyle.green)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):

        if condition == 0:
            lost = random.randint(0, 2) + boss_type + 15
            embed = discord.Embed(color=0xbfbaba)
            thumbnail = get_image(f'{boss_url[boss_type - 1]}')
            embed.set_thumbnail(url=f"attachment://{thumbnail.filename}")
            embed.add_field(name=f"{boss_name[boss_type - 1]}", value=f"You've lost, you lost {lost} HP",
                            inline=False)
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
            embed = discord.Embed(color=0x3455f9)
            thumbnail = get_image(f'{boss_url[boss_type - 1]}')
            embed.set_thumbnail(url=f"attachment://{thumbnail.filename}")
            embed.add_field(name=f"{boss_name[boss_type - 1]}", value=f"You've won!, you won {won} HP",
                            inline=False)
            from events.generalCommands import users
            for user in users:
                if user.username == str(interaction.user):
                    user.health += won
            await interaction.user.send(embed=embed, file=thumbnail)
            await getBoss(interaction)
