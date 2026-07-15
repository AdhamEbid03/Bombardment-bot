import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio
import random

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intent = discord.Intents.default()
intent.message_content = True

bot = commands.Bot(
    command_prefix='/', 
    intents=intent,
    max_messages = 20
    )

@bot.event
async def on_ready():
    #Output when you run the code
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):

    #Simple message to check if the bot is online
    if message.author == bot.user:
        return
    
    if "wake up bomb" in message.content.lower():
        await message.channel.send(f"Ughhh, What do YOU want?")

    await bot.process_commands(message)

async def random_sound_loop(ctx):
    while ctx.voice_client is not None:

        #Time Interval between sounds playing
        wait_time = random.randint(5, 20)
        await asyncio.sleep(wait_time)

        if ctx.voice_client is None:
            break

        sound_folder = "sounds"

        sound_files = [
            f for f in os.listdir(sound_folder)
            if f.endswith(".mp3") or f.endswith(".wav") or f.endswith(".ogg")
        ]

        if not sound_files:
            await ctx.send("No sound files found in the sounds folder.")
            break

        random_sound = random.choice(sound_files)
        sound_path = os.path.join(sound_folder, random_sound)

        if ctx.voice_client.is_playing():
            continue

        
        audio_src = discord.FFmpegOpusAudio(sound_path)

        ctx.voice_client.play(audio_src)

@bot.command()
async def join(ctx):
    
    #Command to make the bot join voice chat, with the command /join
    if ctx.author.voice is None:
        await ctx.send("Get in a room, pretty boy")
        return
    
    channel = ctx.author.voice.channel

    if ctx.voice_client is not None:
        await ctx.send("I already joined, genius")
        return

    await channel.connect()

    bot.loop.create_task(random_sound_loop(ctx))

@bot.command()
async def leave(ctx):

    #Command to make the bot leave voice chat, with the command /leave
    if ctx.voice_client is None:
        await ctx.send("I'm not even in lmao")
        return
    
    await ctx.voice_client.disconnect()
    await ctx.send("Aight, Imma head out...")

#Handles logging, for monitoring and debugging
bot.run(token, log_handler=handler, log_level=logging.DEBUG)