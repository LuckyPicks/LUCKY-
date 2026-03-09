import discord
import asyncio

from scheduler.update_loop import start_scanner

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():

    print("LuckyPicks Bot Online")

    asyncio.create_task(start_scanner())

client.run("YOUR_DISCORD_BOT_TOKEN")
