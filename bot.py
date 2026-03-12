import discord
from discord.ext import commands
import os

intents = discord.Intents.default()

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print("LuckyPicks Bot is online!")

@client.command()
async def test(ctx):
    await ctx.send("✅ LuckyPicks bot is working!")

client.run(os.getenv("DISCORD_TOKEN")))