#---------------------------------------------------------------------------------
version = "v0.0.1.0"
import discord, json, ctypes, os, random, asyncio
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from random import choice

isthefilethere2 = os.path.isfile('config.json')
if isthefilethere2 == False:
    os.system("cls")
    choice_prefix = input(f"Choose Prefix > ")
    choice_username = input(f"Choose Username > ")
    choice_token = input(f"DC Token > ")
    data = ({
    'prefix': choice_prefix,
    'token': choice_token,
    'username': choice_username,
    })
    with open('config.json', 'w+') as outfile:
        json.dump(data, outfile)

a_file = open("config.json", "r")
json_object = json.load(a_file)
a_file.close()
prefix = json.load(open('config.json'))['prefix']
username = json.load(open('config.json'))['username']
token = json.load(open('config.json'))['token']

logo = "https://cdn.discordapp.com/attachments/765575801122717736/767764156538421268/Out_Standing.png"
#---------------------------------------------------------------------------------

# -= Selfbot client =-
client = commands.Bot(command_prefix = prefix, self_bot = True, intents=discord.Intents().all())
DEINSELFBOT = commands
client.remove_command('help')

ctypes.windll.kernel32.SetConsoleTitleW(f"DEIN SELFBOT {version} : {username}")
os.system("cls")
print( + f''.center(120, "_") )
print("")
print(f" - Prefix                 >>       {prefix}")
print("")
print( + f''.center(120, "_") )

# -= Selfbot Commands =-

class cog1(commands.Cog):
    def __init__(self, client):
      self.client = client

    @DEINSELFBOT.command()
    async def embed(self, ctx, *, message):
      embed = discord.Embed(description=message)
      await ctx.send(embed=embed)

    @DEINSELFBOT.command()
    async def frage(self, ctx, *, message):
        responses = ["ja", "nein"]
        embed = discord.Embed(description=f"Frage: {message}\nAntwort: {choice(responses)}")
        await ctx.send(embed=embed)

    @DEINSELFBOT.command()
    async def spam(self, ctx, message: str):
        for _i in range(10):
            await ctx.send(message)
            await asyncio.sleep(0.1)

client.add_cog(cog1(client))
client.run(token, bot=False)
