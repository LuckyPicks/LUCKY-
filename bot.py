import discord
import asyncio

from scheduler.update_loop import start_scanner

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():

    print("LuckyPicks Bot Online")

    asyncio.create_task(start_scanner())


import os

client.run(os.getenv("DISCORD_TOKEN"))
