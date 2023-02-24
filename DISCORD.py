import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"I am .{bot.user}")

    @bot.command()
    async def ping(ctx):
        await ctx.send ("pong!")
        @bot.command()
        async def partida(ctx):
            await ctx.send ("CHESS GAME")

bot.run("BOT TOKEN")