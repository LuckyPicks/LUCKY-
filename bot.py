import discord
import asyncio
import os
from discord.ext import commands

from scheduler.update_loop import start_scanner

intents = discord.Intents.default()

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

    print("LuckyPicks Bot Online")

    asyncio.create_task(start_scanner())

client.run(os.getenv("DISCORD_TOKEN"))