import logic

with open("BotToken.txt", "r") as keyfile:
    TOKEN = keyfile.read()
    keyfile.close()

from discord.ext import commands

bot = commands.Bot(command_prefix='ah? ')


@bot.command()
async def ping(ctx, *item):
    await ctx.author.send("I will contact you in a minute!")
    goodAH = logic.logic(" ".join(item[:]))
    if goodAH != "no items or wrong name":
        await ctx.author.send("Good " + " ".join(item[:]) + " at /ah " + goodAH)
    else:
        await ctx.author.send("No items or wrong name")


bot.run(TOKEN)


