import discord
from discord.ext import commands
import random
from utils import images_folder, get_image

async def setup(client):
    await client.add_cog(finalboss(client))


class finalboss(commands.Cog):

    def __init__(self, client):
        self.client = client


move = []


async def tarrasque(interaction):
    moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    embed = discord.Embed(title="Tarrasque",
                          description="Win this fight by using the right moves (4), each move cost 500 HP", color=0xd83c3e)
    image = get_image(f'{images_folder}bosses\\final\\tarrasque.jpg')
    embed.set_image(url=f'attachment://{image.filename}')
    index = 0
    while len(move) != 4:
        index += 1
        move.append(moves.pop(random.randint(0, 8 - index)))
    view = moves_v()
    await interaction.response.send_message(embed=embed, view=view, file=image)


class moves_v(discord.ui.View):
    thumbnail_victory = get_image(f'{images_folder}screens\\victory.jpg')
    thumbnail_lost = get_image(f'{images_folder}screens\\lost.png')
    
    def __int__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="🡤", style=discord.ButtonStyle.red, row=1)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        from events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url=f'attachment://{moves_v.thumbnail_lost.filename}')
                    embed.add_field(name="When losing is inevitable", value="You've lost, try when you're stronger",
                                    inline=True)
                    users.remove(user)
                    return await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_lost)
                if 1 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(1)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(url=f'attachment://{moves_v.thumbnail_victory.filename}')
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉", inline=True)
                        await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_victory)
                        users.remove(user)
                    else:
                        await interaction.response.send_message(embed=embed)
                else:
                    embed = discord.Embed(color=0xcd4518)
                    embed.add_field(name="❌", value="You did the wrong move (-500 HP)", inline=False)
                    await interaction.response.send_message(embed=embed)
                    user.health -= 500

    @discord.ui.button(label="🡡", style=discord.ButtonStyle.red, row=1)
    async def button2(self, interaction: discord.Interaction, button: discord.ui.Button):
        from events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url=f'attachment://{moves_v.thumbnail_lost.filename}')
                    embed.add_field(name="When losing is inevitable", value="You've lost, try when you're stronger")
                    users.remove(user)
                    return await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_lost)
                if 2 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(2)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(url=f'attachment://{moves_v.thumbnail_victory.filename}')
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉", inline=True)
                        await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_victory)
                        users.remove(user)
                    else:
                        await interaction.response.send_message(embed=embed)
                else:
                    embed = discord.Embed(color=0xcd4518)
                    embed.add_field(name="❌", value="You did the wrong move (-500 HP)", inline=False)
                    await interaction.response.send_message(embed=embed)
                    user.health -= 500

    @discord.ui.button(label="🡥", style=discord.ButtonStyle.red, row=1)
    async def button3(self, interaction: discord.Interaction, button: discord.ui.Button):
        from events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url=f'attachment://{moves_v.thumbnail_lost.filename}')
                    embed.add_field(name="When losing is inevitable", value="You've lost, try when you're stronger",
                                    inline=True)
                    users.remove(user)
                    return await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_lost)
                if 3 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(3)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(url=f'attachment://{moves_v.thumbnail_victory.filename}')
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉", inline=True)
                        await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_victory)
                        users.remove(user)
                    else:
                        await interaction.response.send_message(embed=embed)
                else:
                    embed = discord.Embed(color=0xcd4518)
                    embed.add_field(name="❌", value="You did the wrong move (-500 HP)", inline=False)
                    await interaction.response.send_message(embed=embed)
                    user.health -= 500

    @discord.ui.button(label="🡠", style=discord.ButtonStyle.red, row=2)
    async def button4(self, interaction: discord.Interaction, button: discord.ui.Button):
        from events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url=f'attachment://{moves_v.thumbnail_lost.filename}')
                    embed.add_field(name="When losing is inevitable", value="You've lost, try when you're stronger",
                                    inline=True)
                    users.remove(user)
                    return await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_lost)
                if 4 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(4)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(url=f'attachment://{moves_v.thumbnail_victory.filename}')
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉", inline=True)
                        await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_victory)
                        users.remove(user)
                    else:
                        await interaction.response.send_message(embed=embed)
                else:
                    embed = discord.Embed(color=0xcd4518)
                    embed.add_field(name="❌", value="You did the wrong move (-500 HP)", inline=False)
                    await interaction.response.send_message(embed=embed)
                    user.health -= 500

    @discord.ui.button(label="○", style=discord.ButtonStyle.red, row=2)
    async def button5(self, interaction: discord.Interaction, button: discord.ui.Button):
        from events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url=f'attachment://{moves_v.thumbnail_lost.filename}')
                    embed.add_field(name="When losing is inevitable", value="You've lost, try when you're stronger",
                                    inline=True)
                    users.remove(user)
                    return await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_lost)
                if 5 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(5)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(url=f'attachment://{moves_v.thumbnail_victory.filename}')
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉", inline=True)
                        await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_victory)
                        users.remove(user)
                    else:
                        await interaction.response.send_message(embed=embed)
                else:
                    embed = discord.Embed(color=0xcd4518)
                    embed.add_field(name="❌", value="You did the wrong move (-500 HP)", inline=False)
                    await interaction.response.send_message(embed=embed)
                    user.health -= 500

    @discord.ui.button(label="🡢", style=discord.ButtonStyle.red, row=2)
    async def button6(self, interaction: discord.Interaction, button: discord.ui.Button):
        from events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url=f'attachment://{moves_v.thumbnail_lost.filename}')
                    embed.add_field(name="When losing is inevitable",
                                    value="You've lost, try when you're stronger",
                                    inline=True)
                    users.remove(user)
                    return await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_lost)
                if 6 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(6)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(url=f'attachment://{moves_v.thumbnail_victory.filename}')
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉",
                                        inline=True)
                        await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_victory)
                        users.remove(user)
                    else:
                        await interaction.response.send_message(embed=embed)
                else:
                    embed = discord.Embed(color=0xcd4518)
                    embed.add_field(name="❌", value="You did the wrong move (-500 HP)", inline=False)
                    await interaction.response.send_message(embed=embed)
                    user.health -= 500

    @discord.ui.button(label="🡧", style=discord.ButtonStyle.red, row=3)
    async def button7(self, interaction: discord.Interaction, button: discord.ui.Button):
        from events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url=f'attachment://{moves_v.thumbnail_lost.filename}')
                    embed.add_field(name="When losing is inevitable", value="You've lost, try when you're stronger",
                                    inline=True)
                    users.remove(user)
                    return await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_lost)
                if 7 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(7)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(url=f'attachment://{moves_v.thumbnail_victory.filename}')
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉", inline=True)
                        await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_victory)
                        users.remove(user)
                    else:
                        await interaction.response.send_message(embed=embed)
                else:
                    embed = discord.Embed(color=0xcd4518)
                    embed.add_field(name="❌", value="You did the wrong move (-500 HP)", inline=False)
                    await interaction.response.send_message(embed=embed)
                    user.health -= 500

    @discord.ui.button(label="🡣", style=discord.ButtonStyle.red, row=3)
    async def button8(self, interaction: discord.Interaction, button: discord.ui.Button):
        from events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url=f'attachment://{moves_v.thumbnail_lost.filename}')
                    embed.add_field(name="When losing is inevitable", value="You've lost, try when you're stronger",
                                    inline=True)
                    users.remove(user)
                    return await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_lost)
                if 8 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(8)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(url=f'attachment://{moves_v.thumbnail_victory.filename}')
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉", inline=True)
                        await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_victory)
                        users.remove(user)
                    else:
                        await interaction.response.send_message(embed=embed)
                else:
                    embed = discord.Embed(color=0xcd4518)
                    embed.add_field(name="❌", value="You did the wrong move (-500 HP)", inline=False)
                    await interaction.response.send_message(embed=embed)
                    user.health -= 500

    @discord.ui.button(label="🡦", style=discord.ButtonStyle.red, row=3)
    async def button9(self, interaction: discord.Interaction, button: discord.ui.Button):
        from events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url=f'attachment://{moves_v.thumbnail_lost.filename}')
                    embed.add_field(name="When losing is inevitable", value="You've lost, try when you're stronger",
                                    inline=True)
                    users.remove(user)
                    return await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_lost)
                if 9 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(9)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(url=f'attachment://{moves_v.thumbnail_victory.filename}')
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉", inline=True)
                        await interaction.response.send_message(embed=embed, file=moves_v.thumbnail_victory)
                        users.remove(user)
                    else:
                        await interaction.response.send_message(embed=embed)
                else:
                    embed = discord.Embed(color=0xcd4518)
                    embed.add_field(name="❌", value="You did the wrong move (-500 HP)", inline=False)
                    await interaction.response.send_message(embed=embed)
                    user.health -= 500

