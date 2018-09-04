import discord
import json

from discord.ext import commands


class WoWsb():
    def __init__(self, bot):
        self.bot = bot
        self.data = None

        with(open(self.bot.get_data('shipinfo.json'), encoding='utf-8')) as f:
            self.data = json.load(f)

    @commands.command(pass_context=True)
    async def botinfo(self, ctx):
        embed = discord.Embed(title="WoWsb Bot", description="WoWsb-Bot開発メンバー", color=0xeee657)

        embed.add_field(name="開発リーダー", value="Kosugi_kun")
        embed.add_field(name="軍艦の情報入力", value="MT3\nura4316")
        embed.add_field(name="開発協力", value="WoWsb 日本コミュニティ")
        embed.add_field(name="Botバージョン", value=self.bot._version)
        embed.add_field(name="ライセンス", value="GNU General Public License v3.0")
        embed.add_field(name="著作権", value="Copyright (c) 2018 WoWsb Japan community")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def shipinfo(self, ctx, shipname: str):
        for k in self.data.keys():
            if shipname in ('Flag', 'Name'):
                return
            if shipname in self.data[k]:
                embed = self.gen_embed(self.data[k], shipname)
                await ctx.send(embed=embed)
                return

        await ctx.send('この艦船の情報は見つかりませんでした。')

    @commands.command(pass_context=True)
    async def shiplist(self, ctx, country: str):
        try:
            data = self.data[country]
        except KeyError:
            await ctx.send('指定された国が見つかりませんでした。')
            return
        embed = discord.Embed()
        embed.set_author(name=data['Name'], icon_url=data['Flag'])
        for k, v in data.items():
            if k in ('Flag', 'Name'):
                continue
            name = data['Name']
            title = v['Title']
            desc = v['Desc']
            embed.add_field(name=k, value=f'{name} {title} ({desc})')

        await ctx.send(embed=embed)

    def gen_embed(self, data: dict, shipname: str) -> discord.Embed:
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

    
def setup(bot):
    bot.add_cog(WoWsb(bot))