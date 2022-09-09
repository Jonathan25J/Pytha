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
boss_name = ['Woodie', 'Bruzela', 'Menhetten', 'Brahla', 'Owl', 'Dron', 'Trin', 'Demogorgan', 'Mind Flayer', 'Vecna']
boss_url = ['https://i.pinimg.com/originals/e2/5a/8e/e25a8efe00aa1203cfbf320f73e00ad3.jpg',
            'https://static.fandomspot.com/images/11/10321/10-sahuagin-creature-5e-artwork.jpg',
            'https://www.belloflostsouls.net/wp-content/uploads/2022/01/worg-header-image.jpg',
            'https://i0.wp.com/www.hipstersanddragons.com/wp-content/uploads/2020/12/large-monsters-dnd-5e.jpg?resize=629%2C818&ssl=1',
            'https://assets.dicebreaker.com/dnd-5e-rime-of-the-frostmaiden-artwork-closeup.jpg/BROK/resize/1200x1200'
            '%3E/format/jpg/quality/70/dnd-5e-rime-of-the-frostmaiden-artwork-closeup.jpg',
            'https://assets.dicebreaker.com/tashas-cauldron-of-everything-dnd-rpg-artwork-7.jpg/BROK/resize/1200x1200%3E/format/jpg/quality/70/tashas-cauldron-of-everything-dnd-rpg-artwork-7.jpg',
            'https://cdn3.whatculture.com/images/2020/05/793454e0eb98538a-1200x675.jpg',
            'https://i.pinimg.com/originals/b4/8b/8d/b48b8dbd2d8a548f1eda62d5885958a0.jpg',
            'https://br.atsit.in/nl/wp-content/uploads/2022/02/baldurs-gate-3-dd-ontwikkelaar-legt-uit-waarom-je-een-mind-flayer-niet-kunt-kussen.jpg',
            'https://cdn.vox-cdn.com/thumbor/oLNMoIkewJTQLCMpHrwzHG4y3SA=/0x0:3000x2000/1400x933/filters:focal(1208x396:1688x876):no_upscale()/cdn.vox-cdn.com/uploads/chorus_image/image/70741055/irina_nordsol_kuzmina_vecna_nordsol_cropped.0.jpg']
user_advantage = 0


async def getBoss(interaction):
    global user_advantage
    global condition
    global boss_count
    global boss_type
    global boss_level
    global boss_name
    condition = 0
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
    result = random.uniform(0, 3.34) + boss_level + (boss_type / 1.5) - user_advantage - (user_health / 100)

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
                    print(user.health)
                    if user.health <= 0:
                        users.remove(user)
            await interaction.user.send(embed=embed)
            await getBoss(interaction)

        elif condition == 1:
            won = random.randint(0, 2) + boss_type
            embed = discord.Embed(color=0x3455f9)
            embed.set_thumbnail(url=f"{boss_url[boss_type - 1]}")
            embed.add_field(name=f"{boss_name[boss_type - 1]}", value=f"You've won!, you won {won} HP",
                            inline=False)
            from Events.generalCommands import users
            for user in users:
                if user.username == str(interaction.user):
                    user.health += won
                    print(user.health)
            await interaction.user.send(embed=embed)
            await getBoss(interaction)
