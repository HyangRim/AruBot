#Coding "UTF-8"

import discord

class Help:
    def create_help_embed(self):
        embed = discord.Embed(title= "엣센스의 명령어입니다!",description = " ", color = 0xb4151c)
        embed.add_field(name = "!명령어", value = "엣센스에 있는 명령어를 보여줍니다.",inline=False)
        embed.add_field(name = "!엣센스", value = "엣센스에 대한 정보를 보여줍니다.",inline=False)
        embed.add_field(name = "!주사위", value = "1~6사이의 랜덤한 수를 보여줍니다.",inline=False)
        #이 밑은 구현해야할 것들. 
        embed.add_field(name = "!검색 [키워드]", value = "구글에서 검색해 가장 위에 있는 사진을 보여줍니다.")
        embed.add_field(name = "!음악 [링크]", value = "링크에 있는 음악을 재생합니다.",inline=False)
        embed.add_field(name = "!유튜브 [검색키워드]", value = "유튜브에서 검색 키워드로 검색한 후, 가장 위에 있는 재생목록을 재생합니다.")
        embed.add_field(name = "!큐", value = "현재 재생목록을 보여줍니다.")
        #여기까지 명령어 리스트. 
        embed.set_author(name="엣센스", icon_url="https://66.media.tumblr.com/c1470f46dd017ae05f62ee293ddd7763/tumblr_pcyms5yBw21x2q4f4o7_250.jpg")
        embed.set_image(url = "https://i.imgur.com/Vi9tUCl.png")
        embed.set_footer(text = "Ver.2020-01-14")
        return embed

    def Create_Bot_description(self):
        embed = discord.Embed(title = "환영합니다!", description = "엣센스에 대한 모든 정보",color = 0xb4151c)
        embed.add_field(name="안내", value="기본 접수사는 ![명령어]이며, !도움말로 기본 명령어를 확인해주세요! 숨겨진 명령어도 있습니다!")
        embed.add_field(name="문의",value = "메일 : eyiuta1@gmail.com 디스코드 : 향림#1522 트위터 : https://twitter.com/H_Rim_D")
        return embed