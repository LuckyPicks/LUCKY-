import discord
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} is online!")
    for guild in client.guilds:
        for channel in guild.text_channels:
            try:
                await channel.send("🤖 LuckyPicks bot is now online!")
                return
            except:
                pass

client.run(TOKEN)