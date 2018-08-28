import discord
from discord.ext import commands
import glob
import sys
import os.path
import importlib
import re
import asyncio

from version import VERSION as BOTVERSION

bot = commands.Bot(command_prefix='!!')
client = discord.Client()

@bot.event
async def on_ready():
    print('ロード中')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print('{0.user}にログインしました。'.format(client))
    print('WoWsb-Botバージョン'+ BOTVERSION+'は正常に起動しました。')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="WoWsb Bot", description="WoWsb-Bot開発メンバー", color=0xeee657)

    embed.add_field(name="開発リーダー", value="Kosugi_kun")
    embed.add_field(name="軍艦の情報入力", value="MT3\nura4316")
    embed.add_field(name="開発協力", value="WoWsb 日本コミュニティ")
    embed.add_field(name="Botバージョン", value=BOTVERSION)
    embed.add_field(name="ライセンス", value="MIT License")
    embed.add_field(name="著作権", value="Copyright (c) 2018 WoWsb Japan community")
    await ctx.send(embed=embed)

#日本巡洋艦

@bot.command()
async def hashidate(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier I Hashidate (橋立)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/Hashidate.jpg")

    # give info about you here
    embed.add_field(name="生存性", value="**継戦能力**\n9858\n**抗堪性**\n･防郭防御5.00％･火災浸水耐性10.00％･装甲5.60％･対水雷防御4.50％\n**装甲**\n ･装甲6mm-30mm･防郭 6mm-30mm･艦首/艦尾 6mm･装甲甲板 10mm")
    embed.add_field(name="主砲射程", value="7.80km")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="機動性", value="**最大速力** 18.76ノット[kt]\n**転舵速度** 8.28度/秒\n**転舵所要時間** 3.90秒 ")
    embed.add_field(name="隠蔽性", value="8.40km")
    embed.add_field(name="推力", value="4600馬力")

    await ctx.send(embed=embed)

@bot.command()
async def chikuma(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier II Chikuma (筑摩型防護巡洋艦)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/Chikuma.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n11990\n**抗堪性**\n･防郭防御7.50％･火災浸水耐性10.00％･装甲5.00％･対水雷防御4.50％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="8.22km")
    embed.add_field(name="機動性", value="**最大速力** 24.73ノット[kt]\n**転舵速度** 6.20度/秒\n**転舵所要時間** 15.10秒 ")
    embed.add_field(name="隠蔽性", value="6.72km")
    embed.add_field(name="推力", value="22500馬力")

    await ctx.send(embed=embed)

@bot.command()
async def tenryu(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier III Tenryu (天龍型軽巡洋艦)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/Tenryu.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n13952\n**抗堪性**\n･防郭防御7.50％･火災浸水耐性10.00％･装甲5.60％･対水雷防御4.50％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="8.46km")
    embed.add_field(name="機動性", value="**最大速力** 32.23ノット[kt]\n**転舵速度** 8.20度/秒\n**転舵所要時間** 5.40秒 ")
    embed.add_field(name="隠蔽性", value="6.42km")
    embed.add_field(name="推力", value="51000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def kuma(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier IV Kuma (球磨型軽巡洋艦)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/kuma.png")

    embed.add_field(name="生存性", value="**継戦能力**\n16530\n**抗堪性**\n･防郭防御7.50％･火災浸水耐性11.00％･装甲5.60％･対水雷防御4.50％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="8.60km")
    embed.add_field(name="機動性", value="**最大速力** 33.2ノット[kt]\n**転舵速度** 7.60度/秒\n**転舵所要時間** 5.7秒")
    embed.add_field(name="隠蔽性", value="6.80km")
    embed.add_field(name="推力", value="51000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def furutaka(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier V Furutaka (古鷹型重巡洋艦)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/furutaka.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n21546\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性11.00％･装甲8.00％･対水雷防御6.90％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="10.1km")
    embed.add_field(name="機動性", value="**最大速力** 34.2ノット[kt]\n**転舵速度** 6.60度/秒\n**転舵所要時間** 5.7秒 ")
    embed.add_field(name="隠蔽性", value="7.50km")
    embed.add_field(name="推力", value="113340馬力")

    await ctx.send(embed=embed)

@bot.command()
async def aoba(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier VI Aoba (青葉型重巡洋艦)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/aoba.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n23868\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性11.00％･装甲8.80％･対水雷防御7.50％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="10.58km")
    embed.add_field(name="機動性", value="**最大速力** 34.18ノット[kt]\n**転舵速度** 7.10度/秒\n**転舵所要時間** 6.00秒 ")
    embed.add_field(name="隠蔽性", value="7.68km")
    embed.add_field(name="推力", value="102000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def myoko(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier VII Myoko (妙高型重巡洋艦)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/Myoko.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n24500\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性10.00％･装甲9.00％･対水雷防御7.50％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="10.38km")
    embed.add_field(name="機動性", value="**最大速力** 34.59ノット[kt]\n**転舵速度** 6.40度/秒\n**転舵所要時間** 7.80秒 ")
    embed.add_field(name="隠蔽性", value="8.10km")
    embed.add_field(name="推力", value="130000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def takao(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier VIII Takao (高雄型重巡洋艦)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/Takao.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n27400\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性10.00％･装甲9.00％･対水雷防御7.50％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="10.08km")
    embed.add_field(name="機動性", value="**最大速力** 34.59ノット[kt]\n**転舵速度** 6.30度/秒\n**転舵所要時間** 7.80秒 ")
    embed.add_field(name="隠蔽性", value="8.28km")
    embed.add_field(name="推力", value="133000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def ibuki(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier IX Ibuki (伊吹型重巡洋艦(改鈴谷型重巡洋艦))", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/Ibuki.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n28600\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性10.00％･装甲9.00％･対水雷防御9.00％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="10.08km")
    embed.add_field(name="機動性", value="**最大速力** 34.59ノット[kt]\n**転舵速度** 6.50度/秒\n**転舵所要時間** 8.10秒 ")
    embed.add_field(name="隠蔽性", value="8.70km")
    embed.add_field(name="推力", value="154000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def zao(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier X Zao (蔵王(マル六甲巡))", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/Zao.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n36179\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性12.50％･装甲9.60％･対水雷防御10.50％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="11.72km")
    embed.add_field(name="機動性", value="**最大速力** 34.18ノット[kt]\n**転舵速度** 6.03度/秒\n**転舵所要時間** 6.74秒 ")
    embed.add_field(name="隠蔽性", value="8.47km")
    embed.add_field(name="推力", value="152000馬力")

    await ctx.send(embed=embed)

#ここからヘルプ
bot.remove_command('help')
#大日本帝国海軍ヘルプ
@bot.command()
async def japan(ctx):
    embed = discord.Embed(title="WoWsb Bot", description="大日本帝国海軍のコマンドのリストを表示します。", color=0xeee657)

    embed.add_field(name="!!zao", value="大日本帝国海軍 巡洋艦Tier X Zao (蔵王(マル六甲巡))", inline=False)
    embed.add_field(name="!!ibuki", value="大日本帝国海軍 巡洋艦Tier IX Ibuki (伊吹型重巡洋艦(改鈴谷型重巡洋艦))", inline=False)
    embed.add_field(name="!!takao", value="大日本帝国海軍 巡洋艦Tier VIII Takao (高雄型重巡洋艦)", inline=False)
    embed.add_field(name="!!myoko", value="大日本帝国海軍 巡洋艦Tier VII Myoko (妙高型重巡洋艦)", inline=False)
    embed.add_field(name="!!aoba", value="大日本帝国海軍 巡洋艦Tier VI Aoba (青葉型重巡洋艦)", inline=False)
    embed.add_field(name="!!furutaka", value="大日本帝国海軍 巡洋艦Tier V Furutaka (古鷹型重巡洋艦)", inline=False)
    embed.add_field(name="!!kuma", value="大日本帝国海軍 巡洋艦Tier IV Kuma (球磨型軽巡洋艦)", inline=False)
    embed.add_field(name="!!tenryu", value="大日本帝国海軍 巡洋艦Tier III Tenryu (天龍型軽巡洋艦)", inline=False)
    embed.add_field(name="!!chikuma", value="大日本帝国海軍 巡洋艦Tier II chikuma (筑摩型防護巡洋艦)", inline=False)
    embed.add_field(name="!!hashidate", value="大日本帝国海軍 巡洋艦Tier I Hashidate (橋立)", inline=False)


    await ctx.send(embed=embed)

#普通のヘルプ
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="WoWsb Bot", description="船の数が多いので国別のヘルプになります。", color=0xeee657)
    embed.add_field(name="!!info", value="このBotの開発者などを表示します。", inline=False)
    embed.add_field(name="!!help", value="ヘルプを表示します。", inline=False)
    embed.add_field(name="!!japan", value="大日本帝国海軍の軍艦一覧を表示します。", inline=False)


    await ctx.send(embed=embed)

bot.run('bot-token')
