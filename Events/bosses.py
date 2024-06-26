import discord
from discord import app_commands
from discord.ext import commands
import random


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

    boss_name_1 = ['Woodie', 'Bruzela', 'Menhetten', 'Brahla', 'Owl', 'Dron', 'Trin', 'Demogorgan', 'Mind Flayer',
                   'Vecna']
    boss_url_1 = ['https://i.pinimg.com/originals/e2/5a/8e/e25a8efe00aa1203cfbf320f73e00ad3.jpg',
                  'https://static.fandomspot.com/images/11/10321/10-sahuagin-creature-5e-artwork.jpg',
                  'https://www.belloflostsouls.net/wp-content/uploads/2022/01/worg-header-image.jpg',
                  'https://i0.wp.com/www.hipstersanddragons.com/wp-content/uploads/2020/12/large-monsters-dnd-5e.jpg'
                  '?resize=629%2C818&ssl=1',
                  'https://assets.dicebreaker.com/dnd-5e-rime-of-the-frostmaiden-artwork-closeup.jpg/BROK/resize/1200x1200%3E/format/jpg/quality/70/dnd-5e-rime-of-the-frostmaiden-artwork-closeup.jpg',
                  'https://assets.dicebreaker.com/tashas-cauldron-of-everything-dnd-rpg-artwork-7.jpg/BROK/resize'
                  '/1200x1200%3E/format/jpg/quality/70/tashas-cauldron-of-everything-dnd-rpg-artwork-7.jpg',
                  'https://cdn3.whatculture.com/images/2020/05/793454e0eb98538a-1200x675.jpg',
                  'https://i.pinimg.com/originals/b4/8b/8d/b48b8dbd2d8a548f1eda62d5885958a0.jpg',
                  'https://br.atsit.in/nl/wp-content/uploads/2022/02/baldurs-gate-3-dd-ontwikkelaar-legt-uit-waarom'
                  '-je-een-mind-flayer-niet-kunt-kussen.jpg',
                  'https://cdn.vox-cdn.com/thumbor/oLNMoIkewJTQLCMpHrwzHG4y3SA=/0x0:3000x2000/1400x933/filters:focal(1208x396:1688x876):no_upscale()/cdn.vox-cdn.com/uploads/chorus_image/image/70741055/irina_nordsol_kuzmina_vecna_nordsol_cropped.0.jpg']

    boss_name_2 = ['Flumphs', 'Ghost', 'Dragon turtle', 'Moonstone Dragon', 'Bandit', 'Ghost Knight', 'Vampire',
                   'Shadow Dragon', 'Gelatinious Cube', 'Kraken']
    boss_url_2 = [
        'https://static1.cbrimages.com/wordpress/wp-content/uploads/2022/05/flumph-dnd.jpg?q=50&fit=crop&dpr=1.5',
        'https://static1.cbrimages.com/wordpress/wp-content/uploads/2022/05/dnd-ghost.jpg?q=50&fit=crop&dpr=1.5',
        'https://www.gamersdecide.com/sites/default/files/authors/u149103/dragon_turtle.jpg',
        'https://static1.cbrimages.com/wordpress/wp-content/uploads/2022/05/moonstone-dragon-dnd.jpg?q=50&fit=crop'
        '&dpr=1.5',
        'https://static1.cbrimages.com/wordpress/wp-content/uploads/2021/05/DnD-Rogue.jpg?q=50&fit=crop&dpr=1.5',
        'https://static1.cbrimages.com/wordpress/wp-content/uploads/2022/04/DDUnleashed--PossessObjectSpell('
        '1p0)-Cropped.jpg?q=50&fit=crop&dpr=1.5',
        'https://img00.deviantart.net/62be/i/2016/046/a/8/curse_of_strahd_by_daarken-d9rvuc5.jpg',
        'https://explorednd.com/wp-content/uploads/2022/07/shadow_dragon_5e_guide-950x650.png',
        'https://static0.gamerantimages.com/wordpress/wp-content/uploads/2020/11/Gelatinous-Cube.jpg?q=50&fit=crop'
        '&dpr=1.5',
        'https://static.wikia.nocookie.net/forgottenrealms/images/b/b6/Kraken_4e.jpg/revision/latest?cb=20200226101018']


    boss_name_3 = ['Almiraj','Sprite','Modrons','Kobold','Skeletons','Beholder','Dracolich','Earth Elemental','Pit Fiend','Ancient Red Dragon']
    boss_url_3 = ['https://pbs.twimg.com/media/Ej87DibWoAEVfd3.jpg',
                  'https://www.dndbeyond.com/avatars/thumbnails/0/115/1000/1000/636252746444973630.jpeg',
                  'https://1.bp.blogspot.com/-Xn83uR4LNo8/WuOQBR2CtYI/AAAAAAAAJUs/HxTA8CA8EtIrZD9_cpqnk0oSqLXeGBNtACLcBGAs/s1600/18.jpg',
                  'https://static1.cbrimages.com/wordpress/wp-content/uploads/2022/01/Kobold-Rime-of-Frostmaiden-Three-Hiding-in-Coat.jpeg?q=50&fit=crop&dpr=1.5',
                  'https://angrygolem-games.com/wp-content/uploads/2021/09/Skeleton-Tactics-1024x603.jpg',
                  'https://i0.wp.com/consciencianerd.com/wp-content/uploads/2020/10/10-coisas-que-voce-precisa-saber-sobre-os-Beholders-destaque.jpg?fit=850%2C446&ssl=1&resize=1280%2C720',
                  'https://i.pinimg.com/originals/ab/27/6d/ab276da6a71682d341415f5f4394414f.jpg',
                  'https://i.imgur.com/hHPPXOP.jpg',
                  'https://myotakuworld.com/wp-content/uploads/2022/04/Pit-Fiend-5e-1024x795-1.webp',
                  'https://i0.wp.com/onlyontuesdays27.com/wp-content/uploads/2019/12/d9kytw1-6f890970-fc75-4bfc-a2ce-14179d5fd0ed.jpg?fit=1100%2C642&ssl=1']
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
    from Events.generalCommands import users
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
        embed.set_image(
            url=f"https://external-preview.redd.it/fzyr40Wt_IQ51YQIgXjePUiM5yQVbH06nN7qX_77Ywc.jpg"
                f"?auto=webp&s=84cf73d6ee7b60d6440c25d01a8adc5c828c8ed3")
        embed.add_field(name="You Died!", value=f"Try again next time", inline=False)
        await interaction.response.send_message(embed=embed)
    boss_color = [0x0db537, 0x0db537, 0x0db537, 0x0db537, 0xfbff00, 0xfbff00, 0xfbff00, 0xec4109,
                  0xec4109, 0xec4109]
    result = random.uniform(0, 3.34) + boss_level + (boss_type / 1.5) - user_advantage - (user_health / 400)
    if result < 13.34:
        condition = 1
    embed = discord.Embed(title=f'{boss_name[boss_type - 1]}', color=boss_color[boss_level - 1])
    embed.set_image(url=f"{boss_url[boss_type - 1]}")
    embed.add_field(name="Level", value=f"{boss_level}", inline=False)
    embed.add_field(name=f"Strength", value=f"{boss_type}", inline=False)
    view = mechanics()
    return await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


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
        embed.set_thumbnail(url=f"{boss_url[boss_type - 1]}")
        embed.add_field(name=f"{boss_name[boss_type - 1]}", value=f"You defended yourself, the boss ran away",
                        inline=False)

        await interaction.user.send(embed=embed)
        await getBoss(interaction)

    @discord.ui.button(label="Attack", style=discord.ButtonStyle.green)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):

        if condition == 0:
            lost = random.randint(0, 2) + boss_type + 15
            embed = discord.Embed(color=0xbfbaba)
            embed.set_thumbnail(url=f"{boss_url[boss_type - 1]}")
            embed.add_field(name=f"{boss_name[boss_type - 1]}", value=f"You've lost, you lost {lost} HP",
                            inline=False)
            from Events.generalCommands import users
            for user in users:
                if user.username == str(interaction.user):
                    user.health -= lost
                    if user.health <= 0:
                        users.remove(user)
            await interaction.user.send(embed=embed)
            await getBoss(interaction)

        elif condition == 1:
            if boss_type <= 7:
                won = random.randint(0, 3) + boss_type
            else:
                won = random.randint(3, 6) + boss_type
            embed = discord.Embed(color=0x3455f9)
            embed.set_thumbnail(url=f"{boss_url[boss_type - 1]}")
            embed.add_field(name=f"{boss_name[boss_type - 1]}", value=f"You've won!, you won {won} HP",
                            inline=False)
            from Events.generalCommands import users
            for user in users:
                if user.username == str(interaction.user):
                    user.health += won
            await interaction.user.send(embed=embed)
            await getBoss(interaction)
