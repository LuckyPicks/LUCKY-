import discord
import asyncio

from scheduler.update_loop import start_scanner

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():

    print("LuckyPicks Bot Online")

    asyncio.create_task(start_scanner())


client.run("MTQ4MDYyNDc2MTAzNjg2OTcyOA.GmIvGE.SpylxSQPYpnL3pqtqkXMEYzlJ_QelbGESsLf6w")
