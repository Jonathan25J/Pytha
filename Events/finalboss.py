import discord
from discord.ext import commands
import random


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
    embed.set_image(
        url="https://static1.cbrimages.com/wordpress/wp-content/uploads/2018/10/adam-vehige-tarrasque-jl.jpg?q=50&fit"
            "=crop&dpr=1.5")
    index = 0
    while len(move) != 4:
        index += 1
        move.append(moves.pop(random.randint(0, 8 - index)))
    view = moves_v()
    await interaction.response.send_message(embed=embed, view=view)


class moves_v(discord.ui.View):
    def __int__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="🡤", style=discord.ButtonStyle.red, row=1)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        from Events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url="https://miro.medium.com/max/1000/1*zZeXwvkxhKstvjBjK32ZVg.png")
                    embed.add_field(name="When losing is inevitable", value="You've lost, try when you're stronger",
                                    inline=True)
                    users.remove(user)
                    return await interaction.response.send_message(embed=embed)
                if 1 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(1)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(
                            url="https://cdnb.artstation.com/p/assets/images/images/025/668/731/large/elena-kaeva-564656.jpg?1586541184")
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉", inline=True)
                        await interaction.response.send_message(embed=embed)
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
        from Events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url="https://miro.medium.com/max/1000/1*zZeXwvkxhKstvjBjK32ZVg.png")
                    embed.add_field(name="When losing is inevitable", value="You've lost, try when you're stronger")

                    users.remove(user)
                    return await interaction.response.send_message(embed=embed)
                if 2 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(2)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(
                            url="https://cdnb.artstation.com/p/assets/images/images/025/668/731/large/elena-kaeva-564656.jpg?1586541184")
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉", inline=True)
                        await interaction.response.send_message(embed=embed)
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
        from Events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url="https://miro.medium.com/max/1000/1*zZeXwvkxhKstvjBjK32ZVg.png")
                    embed.add_field(name="When losing is inevitable", value="You've lost, try when you're stronger",
                                    inline=True)
                    users.remove(user)
                    return await interaction.response.send_message(embed=embed)
                if 3 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(3)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(
                            url="https://cdnb.artstation.com/p/assets/images/images/025/668/731/large/elena-kaeva-564656.jpg?1586541184")
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉", inline=True)
                        await interaction.response.send_message(embed=embed)
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
        from Events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url="https://miro.medium.com/max/1000/1*zZeXwvkxhKstvjBjK32ZVg.png")
                    embed.add_field(name="When losing is inevitable", value="You've lost, try when you're stronger",
                                    inline=True)
                    users.remove(user)
                    return await interaction.response.send_message(embed=embed)
                if 4 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(4)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(
                            url="https://cdnb.artstation.com/p/assets/images/images/025/668/731/large/elena-kaeva-564656.jpg?1586541184")
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉", inline=True)
                        await interaction.response.send_message(embed=embed)
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
        from Events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url="https://miro.medium.com/max/1000/1*zZeXwvkxhKstvjBjK32ZVg.png")
                    embed.add_field(name="When losing is inevitable", value="You've lost, try when you're stronger",
                                    inline=True)
                    users.remove(user)
                    return await interaction.response.send_message(embed=embed)
                if 5 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(5)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(
                            url="https://cdnb.artstation.com/p/assets/images/images/025/668/731/large/elena-kaeva-564656.jpg?1586541184")
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉", inline=True)
                        await interaction.response.send_message(embed=embed)
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
        from Events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url="https://miro.medium.com/max/1000/1*zZeXwvkxhKstvjBjK32ZVg.png")
                    embed.add_field(name="When losing is inevitable",
                                    value="You've lost, try when you're stronger",
                                    inline=True)
                    users.remove(user)
                    return await interaction.response.send_message(embed=embed)
                if 6 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(6)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(
                            url="https://cdnb.artstation.com/p/assets/images/images/025/668/731/large/elena-kaeva-564656.jpg?1586541184")
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉",
                                        inline=True)
                        await interaction.response.send_message(embed=embed)
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
        from Events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url="https://miro.medium.com/max/1000/1*zZeXwvkxhKstvjBjK32ZVg.png")
                    embed.add_field(name="When losing is inevitable", value="You've lost, try when you're stronger",
                                    inline=True)
                    users.remove(user)
                    return await interaction.response.send_message(embed=embed)
                if 7 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(7)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(
                            url="https://cdnb.artstation.com/p/assets/images/images/025/668/731/large/elena-kaeva-564656.jpg?1586541184")
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉", inline=True)
                        await interaction.response.send_message(embed=embed)
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
        from Events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url="https://miro.medium.com/max/1000/1*zZeXwvkxhKstvjBjK32ZVg.png")
                    embed.add_field(name="When losing is inevitable", value="You've lost, try when you're stronger",
                                    inline=True)
                    users.remove(user)
                    return await interaction.response.send_message(embed=embed)
                if 8 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(8)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(
                            url="https://cdnb.artstation.com/p/assets/images/images/025/668/731/large/elena-kaeva-564656.jpg?1586541184")
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉", inline=True)
                        await interaction.response.send_message(embed=embed)
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
        from Events.generalCommands import users
        for user in users:
            if user.username == str(interaction.user):
                if user.health <= 0:
                    embed = discord.Embed(color=0xf891d2)
                    embed.set_image(url="https://miro.medium.com/max/1000/1*zZeXwvkxhKstvjBjK32ZVg.png")
                    embed.add_field(name="When losing is inevitable", value="You've lost, try when you're stronger",
                                    inline=True)
                    users.remove(user)
                    return await interaction.response.send_message(embed=embed)
                if 9 in move:
                    embed = discord.Embed(color=0x18cd5e)
                    embed.add_field(name="✅", value="You did the right move (-500 HP)", inline=False)
                    move.remove(9)
                    user.health -= 500
                    if len(move) == 0:
                        embed = discord.Embed(color=0x007bff)
                        embed.set_image(
                            url="https://cdnb.artstation.com/p/assets/images/images/025/668/731/large/elena-kaeva-564656.jpg?1586541184")
                        embed.add_field(name="Tarrasque has been defeated!",
                                        value="You've defeated Tarrasque and won the game🎉", inline=True)
                        await interaction.response.send_message(embed=embed)
                        users.remove(user)
                    else:
                        await interaction.response.send_message(embed=embed)
                else:
                    embed = discord.Embed(color=0xcd4518)
                    embed.add_field(name="❌", value="You did the wrong move (-500 HP)", inline=False)
                    await interaction.response.send_message(embed=embed)
                    user.health -= 500

