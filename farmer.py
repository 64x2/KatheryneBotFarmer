import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

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
    await asyncio.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    print("Sent gwish command")
    await asyncio.sleep(17)
    print("Repeating process...")
    await ctx.send(f".wish {arg}")
   
@b.command()
async def wishburst(ctx, arg):
    await asyncio.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    await asyncio.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    await asyncio.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    await asyncio.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    await asyncio.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    await asyncio.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    await asyncio.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    await asyncio.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    await asyncio.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    await asyncio.sleep(1)
    await ctx.send(f"gwish {arg} noani")
    print("Burst complete, sleeping for 180 seconds...")
    await asyncio.sleep(180)
    print("Repeating process...")
    await ctx.send(f".wishburst {arg}")

b.run(TOKEN, bot = False)
