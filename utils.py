import os
import discord

images_folder = 'public\\images\\'

def get_image(image_path):
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), image_path)
    filename = os.path.basename(image_path)
    return discord.File(image_path, filename=filename)