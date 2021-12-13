from settings import *
from helper_scripts import *
import discord, asyncio

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$last_bounty"):
        bounty = get_last_bounty()
        min = string_bounty_data(bounty)
        await message.channel.send(min)

    if message.content.startswith("$init"):
        await retrieve_bounties(message)


async def retrieve_bounties(message):
    last_bounty = get_last_bounty()
    while True:
        bounties = get_bounties()
        new_bounties = compare_bounties(bounties, last_bounty)
        if len(new_bounties) > 0:
            for i in new_bounties:
                bounty = string_bounty_data(i)
                await message.channel.send(bounty)
            last_bounty = new_bounties[0]
        await asyncio.sleep(360)


client.run(os.getenv("BOTTOKEN"))
