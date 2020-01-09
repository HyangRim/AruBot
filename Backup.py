import discord

client = discord.Client()
token = "NTQzMDU5ODQ2MTE5ODE3MjE2.XgRr8Q.NRY8pXJegYyucgkMZi0UQKywO34"
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run(token)