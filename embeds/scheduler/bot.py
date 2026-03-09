import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is online")

client.run("YOUR_DISCORD_BOT_TOKEN")
