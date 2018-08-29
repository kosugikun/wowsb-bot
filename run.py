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
    embed = discord.Embed(title="巡洋艦Tier I Hashidate ", description="橋立", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Hashidate.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n9858\n**抗堪性**\n･防郭防御5.00％･火災浸水耐性10.00％･装甲5.60％･対水雷防御4.50％\n**装甲**\n ･装甲6mm-30mm･防郭 6mm-30mm･艦首/艦尾 6mm･装甲甲板 10mm")
    embed.add_field(name="主砲射程", value="7.80km")

    embed.add_field(name="機動性", value="**最大速力** 18.76ノット[kt]\n**転舵速度** 8.28度/秒\n**転舵所要時間** 3.90秒 ")
    embed.add_field(name="隠蔽性", value="8.40km")
    embed.add_field(name="推力", value="4600馬力")

    await ctx.send(embed=embed)

@bot.command()
async def chikuma(ctx):
    embed = discord.Embed(title="巡洋艦Tier II Chikuma ", description="筑摩型防護巡洋艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Chikuma.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n11990\n**抗堪性**\n･防郭防御7.50％･火災浸水耐性10.00％･装甲5.00％･対水雷防御4.50％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="8.22km")
    embed.add_field(name="機動性", value="**最大速力** 24.73ノット[kt]\n**転舵速度** 6.20度/秒\n**転舵所要時間** 15.10秒 ")
    embed.add_field(name="隠蔽性", value="6.72km")
    embed.add_field(name="推力", value="22500馬力")

    await ctx.send(embed=embed)

@bot.command()
async def tenryu(ctx):
    embed = discord.Embed(title="巡洋艦Tier III Tenryu ", description="天龍型軽巡洋艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Tenryu.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n13952\n**抗堪性**\n･防郭防御7.50％･火災浸水耐性10.00％･装甲5.60％･対水雷防御4.50％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="8.46km")
    embed.add_field(name="機動性", value="**最大速力** 32.23ノット[kt]\n**転舵速度** 8.20度/秒\n**転舵所要時間** 5.40秒 ")
    embed.add_field(name="隠蔽性", value="6.42km")
    embed.add_field(name="推力", value="51000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def kuma(ctx):
    embed = discord.Embed(title="巡洋艦Tier IV Kuma", description="球磨型軽巡洋艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/kuma.png")

    embed.add_field(name="生存性", value="**継戦能力**\n16530\n**抗堪性**\n･防郭防御7.50％･火災浸水耐性11.00％･装甲5.60％･対水雷防御4.50％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="8.60km")
    embed.add_field(name="機動性", value="**最大速力** 33.2ノット[kt]\n**転舵速度** 7.60度/秒\n**転舵所要時間** 5.7秒")
    embed.add_field(name="隠蔽性", value="6.80km")
    embed.add_field(name="推力", value="51000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def furutaka(ctx):
    embed = discord.Embed(title="巡洋艦Tier V Furutaka", description="古鷹型重巡洋艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/furutaka.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n21546\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性11.00％･装甲8.00％･対水雷防御6.90％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="10.1km")
    embed.add_field(name="機動性", value="**最大速力** 34.2ノット[kt]\n**転舵速度** 6.60度/秒\n**転舵所要時間** 5.7秒 ")
    embed.add_field(name="隠蔽性", value="7.50km")
    embed.add_field(name="推力", value="113340馬力")

    await ctx.send(embed=embed)

@bot.command()
async def aoba(ctx):
    embed = discord.Embed(title="巡洋艦Tier VI Aoba ", description="青葉型重巡洋艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/aoba.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n23868\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性11.00％･装甲8.80％･対水雷防御7.50％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="10.58km")
    embed.add_field(name="機動性", value="**最大速力** 34.18ノット[kt]\n**転舵速度** 7.10度/秒\n**転舵所要時間** 6.00秒 ")
    embed.add_field(name="隠蔽性", value="7.68km")
    embed.add_field(name="推力", value="102000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def myoko(ctx):
    embed = discord.Embed(title="巡洋艦Tier VII Myoko", description="妙高型重巡洋艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Myoko.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n24500\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性10.00％･装甲9.00％･対水雷防御7.50％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="10.38km")
    embed.add_field(name="機動性", value="**最大速力** 34.59ノット[kt]\n**転舵速度** 6.40度/秒\n**転舵所要時間** 7.80秒 ")
    embed.add_field(name="隠蔽性", value="8.10km")
    embed.add_field(name="推力", value="130000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def takao(ctx):
    embed = discord.Embed(title="巡洋艦Tier VIII Takao ", description="高雄型重巡洋艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Takao.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n27400\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性10.00％･装甲9.00％･対水雷防御7.50％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="10.08km")
    embed.add_field(name="機動性", value="**最大速力** 34.59ノット[kt]\n**転舵速度** 6.30度/秒\n**転舵所要時間** 7.80秒 ")
    embed.add_field(name="隠蔽性", value="8.28km")
    embed.add_field(name="推力", value="133000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def ibuki(ctx):
    embed = discord.Embed(title="巡洋艦Tier IX Ibuki ", description="伊吹型重巡洋艦(改鈴谷型重巡洋艦)", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Ibuki.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n28600\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性10.00％･装甲9.00％･対水雷防御9.00％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="10.08km")
    embed.add_field(name="機動性", value="**最大速力** 34.59ノット[kt]\n**転舵速度** 6.50度/秒\n**転舵所要時間** 8.10秒 ")
    embed.add_field(name="隠蔽性", value="8.70km")
    embed.add_field(name="推力", value="154000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def zao(ctx):
    embed = discord.Embed(title="巡洋艦Tier X Zao ", description="蔵王(マル六甲巡)", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Zao.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n36179\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性12.50％･装甲9.60％･対水雷防御10.50％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="11.72km")
    embed.add_field(name="機動性", value="**最大速力** 34.18ノット[kt]\n**転舵速度** 6.03度/秒\n**転舵所要時間** 6.74秒 ")
    embed.add_field(name="隠蔽性", value="8.47km")
    embed.add_field(name="推力", value="152000馬力")

    await ctx.send(embed=embed)

#大日本帝国海軍 戦艦
@bot.command()
async def kawachi(ctx):
    embed = discord.Embed(title="戦艦Tier III Kawachi ", description="河内型戦艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://wikiwiki.jp/warships/?plugin=attach&refer=Kawachi&openfile=shot-17.05.24_14.40.29-0998.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    embed.add_field(name="主砲射程", value=" <数値> km")

    embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    embed.add_field(name="隠蔽性", value=" <数値>km")
    embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def ishizuchi(ctx):
    embed = discord.Embed(title="戦艦Tier IV Ishizuchi ", description="石鎚型巡洋戦艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Ishizuchi.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    embed.add_field(name="主砲射程", value=" <数値> km")

    embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    embed.add_field(name="隠蔽性", value=" <数値>km")
    embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def kongo(ctx):
    embed = discord.Embed(title="戦艦Tier V Kongo", description="金剛型巡洋戦艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Kongo.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    embed.add_field(name="主砲射程", value=" <数値> km")

    embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    embed.add_field(name="隠蔽性", value=" <数値>km")
    embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def fuso(ctx):
    embed = discord.Embed(title="戦艦Tier VI Fuso ", description="扶桑型戦艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Fuso.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    embed.add_field(name="主砲射程", value=" <数値> km")

    embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    embed.add_field(name="隠蔽性", value=" <数値>km")
    embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def nagato(ctx):
    embed = discord.Embed(title="戦艦Tier VII Nagato ", description="長門型戦艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Nagato.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    embed.add_field(name="主砲射程", value=" <数値> km")

    embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    embed.add_field(name="隠蔽性", value=" <数値>km")
    embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def amagi(ctx):
    embed = discord.Embed(title="戦艦Tier VIII Amagi", description="天城型巡洋戦艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Amagi.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    embed.add_field(name="主砲射程", value=" <数値> km")

    embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    embed.add_field(name="隠蔽性", value=" <数値>km")
    embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def izumo(ctx):
    embed = discord.Embed(title="戦艦Tier IX Izumo", description="出雲型戦艦(大和型戦艦計画案A-140J2)", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Izumo.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    embed.add_field(name="主砲射程", value=" <数値> km")

    embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    embed.add_field(name="隠蔽性", value=" <数値>km")
    embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def yamato(ctx):
    embed = discord.Embed(title="戦艦Tier X Yamato", description="大和型戦艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://wikiwiki.jp/warships/?plugin=attach&refer=Yamato&openfile=Yamato%28a%292.png")

    embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    embed.add_field(name="主砲射程", value=" <数値> km")

    embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    embed.add_field(name="隠蔽性", value=" <数値>km")
    embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)


######################
#大日本帝国海軍の駆逐艦#
######################


@bot.command()
async def umikaze(ctx):
    embed = discord.Embed(title="駆逐艦Tier II Umikaze", description="海風型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://wikiwiki.jp/warships/?plugin=attach&refer=Umikaze&openfile=20180306_020153_0.png")

    embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    embed.add_field(name="主砲射程", value=" <数値> km")

    embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    embed.add_field(name="隠蔽性", value=" <数値>km")
    embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def wakatake(ctx):
    embed = discord.Embed(title="駆逐艦Tier III Wakatake", description="若竹型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Wakatake.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    embed.add_field(name="主砲射程", value=" <数値> km")

    embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    embed.add_field(name="隠蔽性", value=" <数値>km")
    embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def isokaze(ctx):
    embed = discord.Embed(title="駆逐艦 Tier IV Isokaze", description="磯風型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Isokaze.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    embed.add_field(name="主砲射程", value=" <数値> km")

    embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    embed.add_field(name="隠蔽性", value=" <数値>km")
    embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def mutsuki(ctx):
    embed = discord.Embed(title="駆逐艦 Tier V Mutsuki", description="睦月型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Mutsuki.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    embed.add_field(name="主砲射程", value=" <数値> km")

    embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    embed.add_field(name="隠蔽性", value=" <数値>km")
    embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def fubuki(ctx):
    embed = discord.Embed(title="駆逐艦 Tier VI Fubuki", description="吹雪型駆逐艦(特I型駆逐艦)", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Fubuki.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    embed.add_field(name="主砲射程", value=" <数値> km")

    embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    embed.add_field(name="隠蔽性", value=" <数値>km")
    embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def akatsuki(ctx):
    embed = discord.Embed(title="駆逐艦 Tier VII Akatsuki", description="暁型駆逐艦(特III型駆逐艦)1番艦暁", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://wikiwiki.jp/warships/?plugin=attach&refer= https://mcpenano.net/WoWsB/Akatsuki.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    embed.add_field(name="主砲射程", value=" <数値> km")

    embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    embed.add_field(name="隠蔽性", value=" <数値>km")
    embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def kagero(ctx):
    embed = discord.Embed(title="駆逐艦 Tier VIII Kagero", description="陽炎型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Kagero.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    embed.add_field(name="主砲射程", value=" <数値> km")

    embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    embed.add_field(name="隠蔽性", value=" <数値>km")
    embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def yugumo(ctx):
    embed = discord.Embed(title="駆逐艦 Tier IX Yugumo", description="夕雲型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Yugumo.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    embed.add_field(name="主砲射程", value=" <数値> km")

    embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    embed.add_field(name="隠蔽性", value=" <数値>km")
    embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def shimakaze(ctx):
    embed = discord.Embed(title="駆逐艦 Tier X Shimakaze", description="島風型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Shimakaze.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    embed.add_field(name="主砲射程", value=" <数値> km")

    embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    embed.add_field(name="隠蔽性", value=" <数値>km")
    embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)


#ここからヘルプ
bot.remove_command('help')
#大日本帝国海軍ヘルプ
@bot.command()
async def japan(ctx):
    embed = discord.Embed(title="WoWsb Bot", description="大日本帝国海軍のコマンドのリストを表示します。", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.add_field(name="———駆逐艦———", value="ここから駆逐艦", inline=False)

    embed.add_field(name="!!shimakaze", value="大日本帝国海軍 駆逐艦Tier X Shimakaze (島風型駆逐艦)", inline=False)
    embed.add_field(name="!!yugumo", value="大日本帝国海軍 駆逐艦Tier IX Yugumo (夕雲型駆逐艦)", inline=False)
    embed.add_field(name="!!kagero", value="大日本帝国海軍 駆逐艦Tier VIII Kagero (陽炎型駆逐艦)", inline=False)
    embed.add_field(name="!!akatsuki", value="大日本帝国海軍 駆逐艦Tier VII Akatsuki (暁型駆逐艦(特III型駆逐艦)1番艦暁)", inline=False)
    embed.add_field(name="!!fubuki", value="大日本帝国海軍 駆逐艦Tier VI Fubuki (吹雪型駆逐艦(特I型駆逐艦))", inline=False)
    embed.add_field(name="!!mutsuki", value="大日本帝国海軍 駆逐艦Tier V Mutsuki (睦月型駆逐艦)", inline=False)
    embed.add_field(name="!!isokaze", value="大日本帝国海軍 駆逐艦Tier IV Isokaze (磯風型駆逐艦)", inline=False)
    embed.add_field(name="!!wakatake", value="大日本帝国海軍 駆逐艦Tier III Wakatake (若竹型駆逐艦)", inline=False)
    embed.add_field(name="!!umikaze", value="大日本帝国海軍 駆逐艦Tier II Umikaze (海風型駆逐艦)", inline=False)


    
#大日本帝国海軍 戦艦ヘルプ
    embed.add_field(name="———戦艦———", value="ここから戦艦", inline=False)
    embed.add_field(name="!!yamato", value="大日本帝国海軍 戦艦Tier X Yamato (大和型戦艦)", inline=False)
    embed.add_field(name="!!izumo", value="大日本帝国海軍 戦艦Tier IX Izumo (出雲型戦艦(大和型戦艦計画案A-140J2))", inline=False)
    embed.add_field(name="!!amagi", value="大日本帝国海軍 戦艦Tier VIII Amagi (天城型巡洋戦艦)", inline=False)
    embed.add_field(name="!!nagato", value="大日本帝国海軍 戦艦Tier VII Nagato (長門型戦艦)", inline=False)
    embed.add_field(name="!!fuso", value="大日本帝国海軍 戦艦Tier VI Fuso (扶桑型戦艦)", inline=False)
    embed.add_field(name="!!kongo", value="大日本帝国海軍 戦艦Tier V Kongo (金剛型巡洋戦艦)", inline=False)
    embed.add_field(name="!!ishizuchi", value="大日本帝国海軍 戦艦Tier IV Ishizuchi (石鎚型巡洋戦艦)", inline=False)
    embed.add_field(name="!!kawachi", value="大日本帝国海軍 戦艦Tier III Kawachi (河内型戦艦)", inline=False)
#日本巡洋艦ヘルプ
    embed.add_field(name="———巡洋艦———", value="ここから巡洋艦", inline=False)

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
