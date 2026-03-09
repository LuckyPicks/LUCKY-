import discord
import asyncio

from scheduler.update_loop import start_scanner

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():

    print("LuckyPicks Bot Online")

    asyncio.create_task(start_scanner())


client.run("https://discord.com/api/webhooks/1480597051816280258/GA_lgQiCSAv7M0UppV8xh6GSdXyhKKusnzqp7Cen1Anc4VOeTTVFKyHWrFILF2EGHn4Y")
