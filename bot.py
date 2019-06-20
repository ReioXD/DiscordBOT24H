import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!")
client.remove_command("help")


@client.command()
@commands.has_role("Admin")
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f" 'Users modification executed' banned {member}, {reason}")

@ban.error
async def ban(ctx, error):
    await ctx.send(f"Some error happened [{error}]")

@client.command()
@commands.has_role("Admin")
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"' Users modification executed ' kicked {member}, {reason}")

@kick.error
async def kick(ctx, error):
    await ctx.send(f"Some error happened [{error}]")
    


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("Assisting our buyers and non-buyers"))
    print("Ready!")
 
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms :smile: ')

@client.command()
@commands.has_role("Non-Buyer")
async def buy(ctx):
    await ctx.author.send("1) Goto https://www.paypal.me/memzhub/5 and pay this amount 2)While paid dm owner with your paypal name 3)While owner checked and everything then you're receieve a 'Buyer' role.")
    await ctx.send("Check dms!")

@buy.error
async def buy(ctx, error):
    await ctx.send("But you already have it :)")

@client.command()
@commands.has_role("Buyer")
async def getscript(ctx):
    await ctx.send("Check dms!")
    await ctx.author.send("loadstring(game:HttpGet('https://pastebin.com/raw/ExR2fxN5', true))() -- Enjoy our 12H+ work")

@getscript.error
async def getscript(ctx, error):
    await ctx.send("Buy first >3")

@client.command()
async def help(ctx):
  await ctx.send("!getscript,!buy")

    
    

client.run("NTkxMjY3MDUwNzkwMzIyMTg2.XQuSYg.ie0bhqIbhjP6iY3fTg4UZGJ3mus")
