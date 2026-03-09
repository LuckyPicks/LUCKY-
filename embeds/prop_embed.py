import discord

def build_prop_embed(player, stat, line, sportsbook, edge):

    embed = discord.Embed(
        title="🔥 Value Prop Detected",
        color=0x00ff00
    )

    embed.add_field(name="Player", value=player)
    embed.add_field(name="Stat", value=stat)
    embed.add_field(name="Line", value=line)
    embed.add_field(name="Best Book", value=sportsbook)
    embed.add_field(name="Edge", value=f"{round(edge*100,2)}%")

    embed.set_footer(text="LuckyPicks Bot")

    return embed
