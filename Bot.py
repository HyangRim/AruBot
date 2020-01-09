import discord

client = discord.Client()
token = "NTQzMDU5ODQ2MTE5ODE3MjE2.XheW3Q.dGXK9j_ym9KOfkkKlVnM8olu5No"
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
    
    if message.content == "!Commend" or message.content == "!commend":
        embed = discord.Embed(title="!Commend",description="AruBot Commend.\n",color = 0xb4151c)
        embed.set_footer(text = "Ver.2020.01.10")
        embed.set_image(url="https://i.imgur.com/Vi9tUCl.png")
        #embed.add_field(name="링크", value="개인정보 처리방침 : https://develable.xyz/post/67\n이용약관 : https://develable.xyz/post/75\n루탑봇 웹패널 : https://rpanel.develable.xyz/")
        #embed.add_field(name="문의", value="공식 홈페이지 : https://develable.xyz\n공식 지원서버 : https://invite.gg/develable\n디스코드 : HwaHyang - Official#8283\n공식 페이스북 : https://cutr.es/uwXnJ")
        await message.channel.send(embed=embed)
        #await client.send_message(message.chnnel, embed=embed)
    
    if message.content == "!Bot" or message.content == "!bot":
        embed = discord.Embed(title="Arubot", description="What is Arubot?.\n",color = 0xb4151c)
client.run(token)

