import discord

def create_prop_embed(player, stat, line):

    embed = discord.Embed(
        title="🔥 NBA Prop",
        description=f"{player} {stat} {line}",
        color=0x00ff00
    )

    embed.set_footer(text="LuckyPicks Bot")

    return embed
