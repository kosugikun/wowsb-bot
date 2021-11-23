# World of Warships Blitz Discord Bot(WoWsb Bot)
# Copyright (C) 2018  WoWsb Japan community , Cosgy Dev
#
# WoWsb Bot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# WoWsb Bot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with WoWsb Bot. If not, see <http://www.gnu.org/licenses/>.

import discord
import asyncio
import json

from discord.ext import commands


def gen_embed(data: dict, shipname: str) -> discord.Embed:
    shipdata = data[shipname]
    embed = discord.Embed(title=shipdata['Title'], description=shipdata['Desc'], color=0xeee657)
    embed.set_author(name=data['Name'], icon_url=data['Flag'])
    embed.set_image(url=shipdata['Image'])

    embed.add_field(name='生存性', value=shipdata['Viability'])
    embed.add_field(name='主砲射程', value=shipdata['MainGunRange'])

    embed.add_field(name='機動性', value=shipdata['Mobility'])
    embed.add_field(name='隠蔽性', value=shipdata['Concealment'])
    embed.add_field(name='推力', value=shipdata['Thrust'])

    return embed


class WoWsb:
    def __init__(self, bot):
        self.bot = bot
        self.data = None
        with(open(self.bot.get_data('shipdata.json'), encoding='utf-8')) as f:
            self.data = json.load(f)

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="WoWsb Bot", description="WoWsb-Bot開発メンバー", color=0xeee657)
        embed.add_field(name="開発リーダー", value="Kosugi_kun")
        embed.add_field(name="プログラマー", value="Episword")
        embed.add_field(name="軍艦の情報入力", value="MT3\nura4316")
        embed.add_field(name="開発協力", value="WoWsb 日本コミュニティ")
        embed.add_field(name="Botバージョン", value=self.bot._version)
        embed.add_field(name="ライセンス", value="GNU General Public License v3.0")
        embed.add_field(name="著作権", value="Copyright (c) 2018 WoWsb Japan community")
        await ctx.send(embed=embed)

    @commands.command()
    async def wows(self, ctx, shipname: str):
        for k in self.data.keys():
            if shipname in ('Flag', 'Name'):
                return
            if shipname in self.data[k]:
                embed = gen_embed(self.data[k], shipname)
                await ctx.send(embed=embed)
                return

        await ctx.send('この軍艦の情報は見つかりませんでした。')

    @commands.command()
    async def wows_list(self, ctx, country: str):
        try:
            data = self.data[country]
        except KeyError:
            await ctx.send('指定された国が見つかりませんでした。')
            return
        embed = discord.Embed()
        embed.set_author(name=data['Name'], icon_url=data['Flag'])
        embed.set_image(url=data['BigFlag'])
        for k, v in data.items():
            if k in ('Flag', 'Name', 'BigFlag'):
                continue
            name = data['Name']
            title = v['Title']
            desc = v['Desc']
            embed.add_field(name=k, value=f'{name} {title} ({desc})')

        await ctx.send(embed=embed)

    @commands.command(name='起床')
    async def get_up(self, ctx):
        voice = await ctx.message.author.voice.channel.connect()
        voice.play(discord.FFmpegPCMAudio('./voice/voice.mp3'))

        counter = 0
        duration = 10  # In seconds
        while not counter >= duration:
            await asyncio.sleep(1)
            counter = counter + 1
        await voice.disconnect()

    @commands.command(name='合戦用意')
    async def battle_ready(self, ctx):
        voice = await ctx.message.author.voice.channel.connect()
        voice.play(discord.FFmpegPCMAudio('./voice/voice2.mp3'))

        counter = 0
        duration = 10  # In seconds
        while not counter >= duration:
            await asyncio.sleep(1)
            counter = counter + 1
        await voice.disconnect()

    @commands.command(name='航空機防御')
    async def aircraft_def(self, ctx):
        voice = await ctx.message.author.voice.channel.connect()
        voice.play(discord.FFmpegPCMAudio('./voice/航空機防御.mp3'))

        counter = 0
        duration = 7  # In seconds
        while not counter >= duration:
            await asyncio.sleep(1)
            counter = counter + 1
        await voice.disconnect()

    @commands.command()
    async def com(self, ctx):
        embed = discord.Embed(title="WoWsb Bot", description="ヘルプ", color=0xeee657)

        embed.add_field(name="!!wowslist <国の名前>", value="軍艦のリストを表示します。\n日本:japan")
        embed.add_field(name="!!wows <軍艦の名前>", value="軍艦のステータスを表示します。\n例: !!wows Yamato")
        embed.add_field(name="!!info", value="WoWsb Botの情報を表示します。")
        await ctx.send(embed=embed)

    @commands.command()
    async def uplog(self, ctx):
        embed = discord.Embed(title='WoWsb Bot', description=f'Version{self.bot._version}', color=0xeee657)

        embed.add_field(name="変更ログ", value=self.bot._uplog)
        embed.set_image(url=self.bot._upimage)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(WoWsb(bot))
