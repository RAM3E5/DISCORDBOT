import discord
from discord.ext import commands
import configparser

cfg = configparser.ConfigParser()
cfg.read("cog_list.ini")

bot = commands.Bot(command_prefix=cfg['GEN']['prefix'])
bot.remove_command('help')

exts = []
for i in range(len(cfg['COGS'])):
	i += 1
	exts.append(cfg['COGS'][f'cog{i}'])

@bot.event
async def on_ready():
	print("online")

for i in exts:

	bot.load_extension(i)

print('Bot by RZ')
bot.run(cfg['GEN']['token'])
