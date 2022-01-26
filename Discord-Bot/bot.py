import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    office_quotes = [
        'The reality of being a writer',
        'A tricky artform',
	'Would you rather be feared or loved?',
    ]

    house_quotes = [
        'Its a basic truth of the human condition that everybody lies, The only variable is about what',
        'If you can fake sincerity, you can fake pretty much anything',
        'There is nothing in this universe that can not be explained, eventually',
    ]

    if message.content == 'TV!':
        response = random.choice(office_quotes)
        response = random.choice(house_quotes)
        await message.channel.send(response)

client.run(TOKEN)
