import discord
from discord.ext import commands
import os

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("LuckyPicks bot is online!")

@bot.command()
async def test(ctx):
    await ctx.send("✅ LuckyPicks bot is working!")

bot.run(os.getenv("DISCORD_TOKEN"))