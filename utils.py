import os
import discord

def get_image(*path_components):
    *folders, filename = path_components
    folder_path = os.path.join('public', 'images', *folders)
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), folder_path, filename)
    return discord.File(image_path, filename)