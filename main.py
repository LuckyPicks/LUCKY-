import discord
import asyncio
import os
from discord.ext import commands, tasks

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

# CHANNEL IDS
NBA_PROPS = 1478284097234276424
NBA_RESULTS = 1478822933869891685
NBA_SLIPS = 1478823161477992640
NBA_EDGES = 1479449082320916643
NBA_ANALYSIS = 1479455075884859442


# BOT READY
@bot.event
async def on_ready():
    print(f"✅ Bot online: {bot.user}")
    auto_post.start()


# AUTO POST LOOP
@tasks.loop(minutes=60)
async def auto_post():

    props_channel = bot.get_channel(NBA_PROPS)
    edges_channel = bot.get_channel(NBA_EDGES)
    analysis_channel = bot.get_channel(NBA_ANALYSIS)

    if props_channel:
        await props_channel.send(
            "🔥 **NBA PLAYER PROP**\n"
            "Player: Example Player\n"
            "Prop: Over 22.5 Points\n"
            "Edge: +7%\n"
            "Confidence: High 💰"
        )

    if edges_channel:
        await edges_channel.send(
            "📊 **EDGE FOUND**\n"
            "Market: Points\n"
            "Projection: 25.3\n"
            "Sportsbook Line: 22.5\n"
            "Edge: +2.8"
        )

    if analysis_channel:
        await analysis_channel.send(
            "🧠 **AI ANALYSIS**\n"
            "Strong matchup advantage tonight.\n"
            "Defense ranks bottom 5 vs position."
        )


# TEST COMMAND
@bot.command()
async def test(ctx):
    await ctx.send("✅ Bot working.")


bot.run(TOKEN)