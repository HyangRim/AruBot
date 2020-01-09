import discord

client = discord.Client()
token = "NTQzMDU5ODQ2MTE5ODE3MjE2.XgRr8Q.NRY8pXJegYyucgkMZi0UQKywO34"
game = discord.Game("Arururung")
@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))
    await client.change_presence(status = discord.Status.idle, activity=game)
    print("Running Bot...")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
client.run(token)

