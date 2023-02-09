import discord
from discord.ext import commands


#import all of the cogs
from music_cog import music_cog

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

#remove the default help command so that we can write out own
#bot.remove_command('help')

@bot.event
async def on_ready(): 
       await bot.add_cog(music_cog(bot))
       print('Bot is Ready!')
#start the bot with our token

bot.run("MTA3MzAyNzY0NDgwMDY0MzEzMw.GBJS-k.yw8ZNBkUO-2i3a7zI_BGHhqcDTO-drrB3avtXs")

