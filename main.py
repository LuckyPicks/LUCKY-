import discord
from discord import app_commands
import os
import asyncio
from datetime import datetime

TOKEN = os.getenv("DISCORD_TOKEN")

# ==============================
# CHANNEL IDS (Your Channels)
# ==============================

NBA_SLATE = 1184196681575714878
NBA_PROPS = 1478284097234276424
NBA_RESULTS = 1478822933869891685
NBA_SLIPS = 1478823161477992640
NBA_EDGES = 1479449082320916643
NBA_ANALYSIS = 1479455075884859442

# ==============================
# DISCORD SETUP
# ==============================

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# ==============================
# HELPER FUNCTION
# ==============================

async def send_message(channel_id, message):

    channel = client.get_channel(channel_id)

    if channel is None:
        print(f"Channel not found: {channel_id}")
        return

    try:
        await channel.send(message)
        print(f"Message sent to {channel.name}")

    except Exception as e:
        print(f"Error sending message: {e}")

# ==============================
# BOT READY EVENT
# ==============================

@client.event
async def on_ready():

    print("================================")
    print(f"Bot Logged In As: {client.user}")
    print("Bot is ONLINE")
    print("================================")

    try:
        synced = await tree.sync()
        print(f"Slash Commands Synced: {len(synced)}")

    except Exception as e:
        print(e)

    # Send startup message
    await send_message(
        NBA_ANALYSIS,
        "🤖 LuckyPicks Bot is now ONLINE!"
    )

# ==============================
# TEST COMMAND
# ==============================

@tree.command(name="testbot", description="Test if bot works")
async def testbot(interaction: discord.Interaction):

    await interaction.response.send_message(
        "✅ Bot is working!"
    )

# ==============================
# POST NBA PROP COMMAND
# ==============================

@tree.command(name="nba_prop", description="Post NBA player prop")
async def nba_prop(
    interaction: discord.Interaction,
    player: str,
    prop: str,
    line: float,
    odds: str
):

    message = f"""
🏀 **NBA PLAYER PROP**

Player: {player}
Prop: {prop}
Line: {line}
Odds: {odds}

Posted: {datetime.now().strftime('%H:%M')}
"""

    await send_message(NBA_PROPS, message)

    await interaction.response.send_message(
        "Prop posted!"
    )

# ==============================
# POST SLIP COMMAND
# ==============================

@tree.command(name="nba_slip", description="Post bet slip")
async def nba_slip(
    interaction: discord.Interaction,
    bet: str
):

    message = f"""
💰 **NBA BET SLIP**

{bet}

Good Luck 🍀
"""

    await send_message(NBA_SLIPS, message)

    await interaction.response.send_message(
        "Slip posted!"
    )

# ==============================
# EDGE ALERT COMMAND
# ==============================

@tree.command(name="edge", description="Post edge alert")
async def edge(
    interaction: discord.Interaction,
    player: str,
    prop: str,
    edge_percent: float
):

    message = f"""
🔥 **EDGE ALERT**

Player: {player}

Prop: {prop}

Edge: +{edge_percent}%
"""

    await send_message(NBA_EDGES, message)

    await interaction.response.send_message(
        "Edge posted!"
    )

# ==============================
# AUTO DAILY POST TASK
# ==============================

async def daily_message():

    await client.wait_until_ready()

    while not client.is_closed():

        now = datetime.now()

        if now.hour == 10 and now.minute == 0:

            await send_message(
                NBA_SLATE,
                "📊 **NBA Slate Posted**"
            )

        await asyncio.sleep(60)

# ==============================
# BACKGROUND TASK START
# ==============================

client.loop.create_task(daily_message())

# ==============================
# START BOT
# ==============================

client.run(TOKEN)