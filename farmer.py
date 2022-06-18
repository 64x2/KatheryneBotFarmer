import discord
from discord.ext.commands import Bot
from discord.ext import commands
import time

#TOKEN
TOKEN = "token here"

client = discord.Client()
b = Bot(command_prefix = ".", self_bot=True)
b.remove_command("help")

@b.event
async def on_ready():
    print("Katheryne bot farmer by xofo")
    print("For use, type .wish (banner) in any channel \n")
    print("Alse see .wishburst (banner) for faster wishing, with a delay! \n")

@b.command()
async def wish(ctx, arg):
    time.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    print("Sent gwish command")
    time.sleep(17)
    print("Repeating process...")
    await ctx.send(f".wish {arg}")
   
@b.command()
async def wishburst(ctx, arg):
    time.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    time.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    time.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    time.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    time.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    time.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    time.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    time.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    time.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    time.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    print("Burst complete, sleeping for 180 seconds...")
    time.sleep(180)
    print("Repeating process...")
    await ctx.send(f".wishburst {arg}")

b.run(TOKEN, bot = False)
