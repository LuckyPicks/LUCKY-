import discord
from discord.ext import commands, tasks
import random
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

# CHANNEL IDS
NBA_SLATE = 1184196681575714878
NBA_PROPS = 1478284097234276424
NBA_RESULTS = 1478822933869891685
NBA_SLIPS = 1478823161477992640
NBA_EDGES = 1479449082320916643
NBA_ANALYSIS = 1479455075884859442

# SAMPLE PLAYER PROPS
props = [
    "LeBron James OVER 7.5 Assists",
    "Steph Curry OVER 4.5 Threes",
    "Luka Doncic OVER 29.5 Points",
    "Giannis OVER 11.5 Rebounds",
    "Jayson Tatum OVER 3.5 Threes",
    "Nikola Jokic OVER 9.5 Assists"
]

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")
    post_props.start()

@tasks.loop(hours=6)
async def post_props():

    channel = bot.get_channel(NBA_PROPS)

    pick = random.choice(props)

    message = f"""
🔥 **NBA PLAYER PROP**

🎯 Pick: **{pick}**

📊 Edge: Model Value
💰 Bet Size: 1 Unit

#LuckyPicks 🍀
"""

    if channel:
        await channel.send(message)

@bot.command()
async def prop(ctx):

    pick = random.choice(props)

    await ctx.send(f"🔥 **Player Prop Pick:** {pick}")

bot.run(TOKEN)