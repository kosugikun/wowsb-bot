# World of Warships Blitz Discord Bot(WoWsb Bot)
# Copyright (C) 2018  WoWsb Japan community
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
from discord.ext import commands
import importlib
import asyncio

import os
import sys
import time
import shlex
import shutil
import random
import inspect
import logging
import asyncio
import pathlib
import traceback
import math
import re

import aiohttp
import discord

from io import BytesIO, StringIO
from functools import wraps
from textwrap import dedent
from datetime import timedelta
from collections import defaultdict

from discord.enums import ChannelType

from version import VERSION as BOTVERSION

from version import MEMBERS
from changes import changes

bot = commands.Bot(command_prefix='!!')
client = discord.Client()

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print('WoWsb-Botバージョン'+ BOTVERSION+'は正常に起動しました。')
    print('—————————————————————')
    print('GNU General Public License v3.0')
    print('Copyright (c) 2018 WoWsb Japan community')
    print('開発メンバー')
    print(MEMBERS)
    print('開発協力')
    print('WoWsb 日本コミュニティ')
print('—————————————————————')
    channel = client.get_channel('420835825983422477')
    voice = await connect(channel)
    await client.change_presence(game=discord.Game(name="!!help", url="https://github.com/MusicBot-JP/wowsb-bot"))

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="WoWsb Bot", description="WoWsb-Bot開発メンバー", color=0xeee657)

    embed.add_field(name="開発リーダー", value="Kosugi_kun")
    embed.add_field(name="軍艦の情報入力", value="MT3\nura4316")
    embed.add_field(name="開発協力", value="WoWsb 日本コミュニティ")
    embed.add_field(name="Botバージョン", value=BOTVERSION)
    embed.add_field(name="ライセンス", value="GNU General Public License v3.0")
    embed.add_field(name="著作権", value="Copyright (c) 2018 WoWsb Japan community")
    await ctx.send(embed=embed)

@bot.command()
async def uplog(ctx):
    embed = discord.Embed(title="WoWsb Bot", description="Version"+BOTVERSION+"", color=0xeee657)

    embed.add_field(name="変更ログ", value=changes)
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

    embed.add_field(name="生存性", value="**継戦能力**\n11990\n**抗堪性**\n･防郭防御7.50％･火災浸水耐性10.00％･装甲5.00％･対水雷防御4.50％")
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

    embed.add_field(name="生存性", value="**継戦能力**\n13952\n**抗堪性**\n･防郭防御7.50％･火災浸水耐性10.00％")
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

    embed.add_field(name="生存性", value="**継戦能力**\n16530\n**抗堪性**\n･防郭防御7.50％･火災浸水耐性11.00％･装甲5.60％･対水雷防御4.50％")
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

    embed.add_field(name="生存性", value="**継戦能力**\n21546\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性11.00％･装甲8.00％･対水雷防御6.90％")
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

    embed.add_field(name="生存性", value="**継戦能力**\n23868\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性11.00％･装甲8.80％･対水雷防御7.50％")
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

    embed.add_field(name="生存性", value="**継戦能力**\n24500\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性10.00％･装甲9.00％･対水雷防御7.50％")
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

    embed.add_field(name="生存性", value="**継戦能力**\n27400\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性10.00％･装甲9.00％･対水雷防御7.50％")
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

    embed.add_field(name="生存性", value="**継戦能力**\n28600\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性10.00％･装甲9.00％･対水雷防御9.00％")
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

    embed.add_field(name="生存性", value="**継戦能力**\n36179\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性12.50％･装甲9.60％･対水雷防御10.50％")
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

    embed.add_field(name="生存性", value="**継戦能力**\n27233\n**抗堪性**\n ･防郭防御10.00%･火災浸水耐性11.00%･装甲11.20%･対水雷防御12.08%\n**装甲**\n ･装甲 6mm〜301mm")
    embed.add_field(name="主砲射程", value="10.35km")

    embed.add_field(name="機動性", value="**最大速力**  18.89ノット[kt]\n**転舵速度**  4.90度/秒\n**転舵所要時間**  12.30秒 ")
    embed.add_field(name="隠蔽性", value=" 10.08km")
    embed.add_field(name="推力", value=" 25000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def ishizuchi(ctx):
    embed = discord.Embed(title="戦艦Tier IV Ishizuchi ", description="石鎚型巡洋戦艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Ishizuchi.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n29904\n**抗堪性**\n ･防郭防御10.00％･火災浸水耐性11.00％･装甲11.20％･対水雷防御10.50％\n**装甲**\n ･装甲13mm-203mm･防郭 19mm-203mm･艦首/艦尾 19mm-76mm･砲郭 13mm-152mm･装甲甲板 19mm-38mm")
    embed.add_field(name="主砲射程", value="11.13km")

    embed.add_field(name="機動性", value="**最大速力** 24.31ノット[kt]\n**転舵速度**  4.80度/秒\n**転舵所要時間**  13.80秒 ")
    embed.add_field(name="隠蔽性", value=" 11.22km")
    embed.add_field(name="推力", value=" 45000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def kongo(ctx):
    embed = discord.Embed(title="戦艦Tier V Kongo", description="金剛型巡洋戦艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Kongo.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n37605\n**抗堪性**\n･防郭防御10.00％･火災浸水耐性13.75％･装甲12.80％･対水雷防御14.49％\n**装甲**\n・装甲25-203mm・防郭 102-203mm・艦首/艦尾 25-76mm・砲郭 152mm・装甲甲板 38-120mm")
    embed.add_field(name="主砲射程", value="12.21km")

    embed.add_field(name="機動性", value="**最大速力**  29.31ノット[kt]\n**転舵速度** 5.60度/秒\n**転舵所要時間**  13.80秒 ")
    embed.add_field(name="隠蔽性", value="11.34km")
    embed.add_field(name="推力", value="64000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def fuso(ctx):
    embed = discord.Embed(title="戦艦Tier VI Fuso ", description="扶桑型戦艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Fuso.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 41234\n**抗堪性**\n ･防郭防御10.00％･火災浸水耐性13.75％･装甲12.80％･対水雷防御15.25％\n**装甲**\n ･装甲 25mm-305mm･防郭 76mm-305mm･艦首/艦尾 25mm-102mm･砲郭 152mm-203mm･装甲甲板 35mm-99mm")
    embed.add_field(name="主砲射程", value="12.88km")

    embed.add_field(name="機動性", value="**最大速力** 23.90ノット[kt]\n**転舵速度** 4.60度/秒\n**転舵所要時間**  14.70秒 ")
    embed.add_field(name="隠蔽性", value=" 12.36km")
    embed.add_field(name="推力", value="40000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def nagato(ctx):
    embed = discord.Embed(title="戦艦Tier VII Nagato ", description="長門型戦艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Nagato.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n43585\n**抗堪性**\n ･防郭防御12.50％･火災浸水耐性13.75％･装甲14.40％･対水雷防御17.25％")
    embed.add_field(name="主砲射程", value="13.67km")
    embed.add_field(name="副砲射程", value="6.08km")

    embed.add_field(name="機動性", value="**最大速力**  24.87ノット[kt]\n**転舵速度**  22.28度/秒\n**転舵所要時間**  15.90秒 ")
    embed.add_field(name="隠蔽性", value="11.76km")
    embed.add_field(name="推力", value="80000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def amagi(ctx):
    embed = discord.Embed(title="戦艦Tier VIII Amagi", description="天城型巡洋戦艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Amagi.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 49211\n**抗堪性**\n •防郭防御12.50％•火災浸水耐性12.50％•装甲13.60％•対水雷防御15.90％")
    embed.add_field(name="主砲射程", value="14.42km")
    embed.add_field(name="副砲射程", value="6.21km")

    embed.add_field(name="機動性", value="**最大速力** 29.47ノット[kt]\n**転舵速度** 4.80度/秒\n**転舵所要時間**  15.27秒 ")
    embed.add_field(name="隠蔽性", value="12.36km")
    embed.add_field(name="推力", value="131200馬力")

    await ctx.send(embed=embed)

@bot.command()
async def izumo(ctx):
    embed = discord.Embed(title="戦艦Tier IX Izumo", description="出雲型戦艦(大和型戦艦計画案A-140J2)", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Izumo.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 54979\n**抗堪性**\n ･防郭防御12.50％･火災浸水耐性12.50％･装甲14.40％･対水雷防御19.08％")
    embed.add_field(name="主砲射程", value="15.17km")
    embed.add_field(name="副砲射程", value="6.90km")

    embed.add_field(name="機動性", value="**最大速力** 28.88ノット[kt]\n**転舵速度** 4.60度/秒\n**転舵所要時間**  16.91秒 ")
    embed.add_field(name="隠蔽性", value="12.42km")
    embed.add_field(name="推力", value="153000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def yamato(ctx):
    embed = discord.Embed(title="戦艦Tier X Yamato", description="大和型戦艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://wikiwiki.jp/warships/?plugin=attach&refer=Yamato&openfile=Yamato%28a%292.png")

    embed.add_field(name="生存性", value="**継戦能力**\n 62920\n**装甲**\n 18mm-410mm･防郭 80mm-410mm･艦首/艦尾 32mmm･砲郭 25mm･装甲甲板 18mm-200mm")
    embed.add_field(name="主砲射程", value="16.41km")

    embed.add_field(name="機動性", value="**最大速力** 26.67ノット[kt]\n**転舵速度** 4.6度/秒\n**転舵所要時間**  19.20秒 ")
    embed.add_field(name="隠蔽性", value="12.60km")
    embed.add_field(name="推力", value="153,553馬力")

    await ctx.send(embed=embed)


######################
#大日本帝国海軍の駆逐艦#
######################

@bot.command()
async def umikaze(ctx):
    embed = discord.Embed(title="駆逐艦Tier II Umikaze", description="海風型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://wikiwiki.jp/warships/?plugin=attach&refer=Umikaze&openfile=20180306_020153_0.png")

    embed.add_field(name="生存性", value="**継戦能力**\n 7992\n**抗堪性**\n ･防郭防御5.00％･火災浸水耐性10.00％･装甲3.20％･対水雷防御3.00％")
    embed.add_field(name="主砲射程", value="	6.30km")

    embed.add_field(name="機動性", value="**最大速力** 32.23ノット[kt]\n**転舵速度**  8.60度/秒\n**転舵所要時間**  3.30秒 ")
    embed.add_field(name="隠蔽性", value="4.98km")
    embed.add_field(name="推力", value="20500馬力")

    await ctx.send(embed=embed)

@bot.command()
async def wakatake(ctx):
    embed = discord.Embed(title="駆逐艦Tier III Wakatake", description="若竹型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Wakatake.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n9156\n**抗堪性**\n ･防郭防御5.00％･火災浸水耐性10.00％･装甲3.20％･対水雷防御3.00％")
    embed.add_field(name="主砲射程", value="6.58km")

    embed.add_field(name="機動性", value="**最大速力** 35.01ノット[kt]\n**転舵速度** 10.70度/秒\n**転舵所要時間**  3.30秒 ")
    embed.add_field(name="隠蔽性", value="5.22km")
    embed.add_field(name="推力", value="21500馬力")

    await ctx.send(embed=embed)

@bot.command()
async def isokaze(ctx):
    embed = discord.Embed(title="駆逐艦 Tier IV Isokaze", description="磯風型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Isokaze.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 8900\n**抗堪性**\n ･防郭防御5.00％･火災浸水耐性10.00％･装甲4.00％･対水雷防御3.00％")
    embed.add_field(name="主砲射程", value=" 6.30km")

    embed.add_field(name="機動性", value="**最大速力** 34.18ノット[kt]\n**転舵速度** 8.90度/秒\n**転舵所要時間**  3.30秒 ")
    embed.add_field(name="隠蔽性", value="5.10km")
    embed.add_field(name="推力", value="27000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def mutsuki(ctx):
    embed = discord.Embed(title="駆逐艦 Tier V Mutsuki", description="睦月型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Mutsuki.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 9700\n**抗堪性**\n ･防郭防御5.00％･火災浸水耐性10.00％･装甲4.00％･対水雷防御3.00％")
    embed.add_field(name="主砲射程", value="6.30km")

    embed.add_field(name="機動性", value="**最大速力** 36.12ノット[kt]\n**転舵速度** 9.20度/秒\n**転舵所要時間**  2.70秒 ")
    embed.add_field(name="隠蔽性", value="5.40km")
    embed.add_field(name="推力", value="38500馬力")

    await ctx.send(embed=embed)

@bot.command()
async def fubuki(ctx):
    embed = discord.Embed(title="駆逐艦 Tier VI Fubuki", description="吹雪型駆逐艦(特I型駆逐艦)", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Fubuki.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n11000\n**抗堪性**\n ･防郭防御5.00％･火災浸水耐性10.00％･装甲4.80％･対水雷防御3.00％")
    embed.add_field(name="主砲射程", value="6.90km")

    embed.add_field(name="機動性", value="**最大速力** 35.01ノット[kt]\n**転舵速度** 7.90度/秒\n**転舵所要時間**  3.90秒 ")
    embed.add_field(name="隠蔽性", value="6.36km")
    embed.add_field(name="推力", value="50000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def akatsuki(ctx):
    embed = discord.Embed(title="駆逐艦 Tier VII Akatsuki", description="暁型駆逐艦(特III型駆逐艦)1番艦暁", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://wikiwiki.jp/warships/?plugin=attach&refer= https://mcpenano.net/WoWsB/Akatsuki.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 11800\n**抗堪性**\n ･防郭防御5.00％･火災浸水耐性10.00％･装甲4.80％･対水雷防御3.00％")
    embed.add_field(name="主砲射程", value="6.90km")

    embed.add_field(name="機動性", value="**最大速力** 38.62ノット[kt]\n**転舵速度** 8.70度/秒\n**転舵所要時間**  3.30秒 ")
    embed.add_field(name="隠蔽性", value="6.24km")
    embed.add_field(name="推力", value="50000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def kagero(ctx):
    embed = discord.Embed(title="駆逐艦 Tier VIII Kagero", description="陽炎型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Kagero.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n13500\n**抗堪性**\n ･防郭防御5.00％･火災浸水耐性10.00％･装甲4.80％･対水雷防御3.00％")
    embed.add_field(name="主砲射程", value="7.20km")

    embed.add_field(name="機動性", value="**最大速力** 34.18ノット[kt]\n**転舵速度** 8.20度/秒\n**転舵所要時間**  3.00秒 ")
    embed.add_field(name="隠蔽性", value="6.00km")
    embed.add_field(name="推力", value="52000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def yugumo(ctx):
    embed = discord.Embed(title="駆逐艦 Tier IX Yugumo", description="夕雲型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Yugumo.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 14300\n**抗堪性**\n ･防郭防御5.00％･火災浸水耐性10.00％･装甲4.80％･対水雷防御3.00％")
    embed.add_field(name="主砲射程", value="7.20km")

    embed.add_field(name="機動性", value="**最大速力** 35.01ノット[kt]\n**転舵速度** 8.10度/秒\n**転舵所要時間**  3.90秒 ")
    embed.add_field(name="隠蔽性", value=" 6.12km")
    embed.add_field(name="推力", value=" 52000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def shimakaze(ctx):
    embed = discord.Embed(title="駆逐艦 Tier X Shimakaze", description="島風型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Shimakaze.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 15200\n**抗堪性**\n･防郭防御5.00％･火災浸水耐性10.00％･装甲4.80％･対水雷防御3.00％")
    embed.add_field(name="主砲射程", value="7.20km")

    embed.add_field(name="機動性", value="**最大速力** 39.46ノット[kt]\n**転舵速度**  8.50度/秒\n**転舵所要時間**  3.60秒 ")
    embed.add_field(name="隠蔽性", value="6.48km")
    embed.add_field(name="推力", value="	80000馬力")

    await ctx.send(embed=embed)

###########
#駆逐艦分岐#
###########

@bot.command()
async def minekaze(ctx):
    embed = discord.Embed(title="駆逐艦 Tier V Minekaze", description="峯風型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Minekaze.jpg")

    embed.add_field(name="WoWsb v1.8.0で追加予定の駆逐艦です。", value="WoWsbのアップデートが来ていないため情報がありません。:(")

    # embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
   # embed.add_field(name="主砲射程", value=" <数値> km")

    # embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    # embed.add_field(name="隠蔽性", value=" <数値>km")
    # embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def hatsuharu(ctx):
    embed = discord.Embed(title="駆逐艦 Tier VI Hatsuharu", description="初春型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Hatsuharu.jpg")

    embed.add_field(name="WoWsb v1.8.0で追加予定の駆逐艦です。", value="WoWsbのアップデートが来ていないため情報がありません。:(")

    #embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    #embed.add_field(name="主砲射程", value=" <数値> km")

    #embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    #embed.add_field(name="隠蔽性", value=" <数値>km")
    #embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def shiratsuyu(ctx):
    embed = discord.Embed(title="駆逐艦 Tier VII Shiratsuyu", description="白露型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://wikiwiki.jp/warships/?plugin=attach&refer= https://mcpenano.net/WoWsB/Shiratsuyu.jpg")

    embed.add_field(name="WoWsb v1.8.0で追加予定の駆逐艦です。", value="WoWsbのアップデートが来ていないため情報がありません。:(")

    #embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    #embed.add_field(name="主砲射程", value=" <数値> km")

    #embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    #embed.add_field(name="隠蔽性", value=" <数値>km")
    #embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def akizuki(ctx):
    embed = discord.Embed(title="駆逐艦 Tier VIII Akizuki", description="秋月型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Akizuki.jpg")

    embed.add_field(name="WoWsb v1.8.0で追加予定の駆逐艦です。", value="WoWsbのアップデートが来ていないため情報がありません。:(")

    #embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    #embed.add_field(name="主砲射程", value=" <数値> km")

    #embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    #embed.add_field(name="隠蔽性", value=" <数値>km")
    #embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def kitakaze(ctx):
    embed = discord.Embed(title="駆逐艦 Tier IX Kitakaze", description="北風型駆逐艦（改秋月型駆逐艦）", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Kitakaze.jpg")

    embed.add_field(name="WoWs(PC)版のみで実装されている駆逐艦です。", value="WoWsbで追加されていないため情報がありません。:(")

    #embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    #embed.add_field(name="主砲射程", value=" <数値> km")

    #embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    #embed.add_field(name="隠蔽性", value=" <数値>km")
    #embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

@bot.command()
async def harugumo(ctx):
    embed = discord.Embed(title="駆逐艦 Tier X Harugumo", description="春雲型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Harugumo.jpg")

    embed.add_field(name="WoWs(PC)版のみで実装されている駆逐艦です。", value="WoWsbで追加されていないため情報がありません。:(")

    #embed.add_field(name="生存性", value="**継戦能力**\n情報\n**抗堪性**\n･防郭防御 <数値>％･火災浸水耐性 <数値>％･装甲 <数値>％･対水雷防御 <数値>％\n**装甲**\n ･装甲 <数値> mm- <数値> mm･防郭  <数値> mm- <数値> mm･艦首/艦尾  <数値> mm･装甲甲板  <数値> mm")
    #embed.add_field(name="主砲射程", value=" <数値> km")

    #embed.add_field(name="機動性", value="**最大速力**  <数値>ノット[kt]\n**転舵速度**  <数値>度/秒\n**転舵所要時間**  <数値>秒 ")
    #embed.add_field(name="隠蔽性", value=" <数値>km")
    #embed.add_field(name="推力", value=" <数値>馬力")

    await ctx.send(embed=embed)

########################
#大日本帝国海軍の航空母艦#
#######################

@bot.command()
async def hosho(ctx):
    embed = discord.Embed(title="航空母艦 Tier IV Hosho", description="鳳翔型航空母艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Hosho.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 17024\n**抗堪性**\n ･防郭防御5.00％･火災浸水耐性11.00％･装甲4.40％･対水雷防御6.00％\n**装甲**\n 装甲13mm～20mm")
    embed.add_field(name="主砲射程", value="6.30km")

    embed.add_field(name="機動性", value="**最大速力** 24.45ノット[kt]\n**転舵速度** 4.60度/秒\n**転舵所要時間**  7.30秒 ")
    embed.add_field(name="隠蔽性", value=" 7.20km")
    embed.add_field(name="推力", value="30000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def zuiho(ctx):
    embed = discord.Embed(title="航空母艦 Tier V Zuiho", description="瑞鳳型航空母艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Zuiho.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 19152\n**抗堪性**\n ･防郭防御5.00％･火災浸水耐性11.00％･装甲4.40％･対水雷防御7.42％\n**装甲**\n 13mm～25mm")
    embed.add_field(name="主砲射程", value="6.60km")

    embed.add_field(name="機動性", value="**最大速力** 28.62ノット[kt]\n**転舵速度**  4.40度/秒\n**転舵所要時間**  9.90秒 ")
    embed.add_field(name="隠蔽性", value=" 7.86km")
    embed.add_field(name="推力", value="52000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def ryujo(ctx):
    embed = discord.Embed(title="航空母艦 Tier VI Ryujo", description="龍驤型航空母艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Ryujo.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 23322\n**抗堪性**\n ･防郭防御5.00％･火災浸水耐性11.00％･装甲6.40％･対水雷防御6.30％\n**装甲**\n 13mm～25mm")
    embed.add_field(name="主砲射程", value="6.60km")

    embed.add_field(name="機動性", value="**最大速力** 28.62ノット[kt]\n**転舵速度** 5.20度/秒\n**転舵所要時間**  10.20秒 ")
    embed.add_field(name="隠蔽性", value=" 7.22km")
    embed.add_field(name="推力", value="65000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def hiryu(ctx):
    embed = discord.Embed(title="航空母艦 Tier VII Hiryu", description="飛龍型航空母艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://wikiwiki.jp/warships/?plugin=attach&refer= https://mcpenano.net/WoWsB/Hiryu.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 00000\n**抗堪性**\n ･防郭防御10.00％･火災浸水耐性11.00％･装甲6.40％･対水雷防御11.00％")
    embed.add_field(name="主砲射程", value="7.2km")

    embed.add_field(name="機動性", value="**最大速力**  33.2ノット[kt]\n**転舵速度** 4.6度/秒\n**転舵所要時間** 11.4秒 ")
    embed.add_field(name="隠蔽性", value="9.3km")
    embed.add_field(name="推力", value="153000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def shokaku(ctx):
    embed = discord.Embed(title="航空母艦 Tier VIII Shokaku", description="翔鶴型航空母艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Shokaku.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 25200\n**抗堪性**\n ･防郭防御10.00％･火災浸水耐性10.00％･装甲7.50％･対水雷防御10.50％")
    embed.add_field(name="主砲射程", value="7.20km")

    embed.add_field(name="機動性", value="**最大速力** 33.20ノット[kt]\n**転舵速度** 4.30度/秒\n**転舵所要時間**  13.20秒 ")
    embed.add_field(name="隠蔽性", value="9.72km")
    embed.add_field(name="推力", value="160000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def taiho(ctx):
    embed = discord.Embed(title="航空母艦 Tier IX Taiho", description="大鳳型航空母艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Taiho.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 34116\n**抗堪性**\n ･防郭防御10.00％･火災浸水耐性12.50％･装甲9.60％･対水雷防御10.50％")
    embed.add_field(name="主砲射程", value="7.20km")

    embed.add_field(name="機動性", value="**最大速力** 32.23ノット[kt]\n**転舵速度** 4.10度/秒\n**転舵所要時間**  13.09秒 ")
    embed.add_field(name="隠蔽性", value="8.77km")
    embed.add_field(name="推力", value="160000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def hakuryu(ctx):
    embed = discord.Embed(title="航空母艦 Tier X Hakuryu", description="白龍型航空母艦(G15/改大鳳型航空母艦)", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Hakuryu.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n38507\n**抗堪性**\n ･防郭防御10.00％･火災浸水耐性12.50％･装甲9.60％･対水雷防御10.50％")
    embed.add_field(name="主砲射程", value="7.20km")

    embed.add_field(name="機動性", value="**最大速力** 33.20ノット[kt]\n**転舵速度** 3.80度/秒\n**転舵所要時間**  16.20秒 ")
    embed.add_field(name="隠蔽性", value="9.49km")
    embed.add_field(name="推力", value="153000馬力")

    await ctx.send(embed=embed)

#################
#日本プレミアム艦#
################

@bot.command()
async def mikasa(ctx):
    embed = discord.Embed(title="戦艦Tier II Mikasa", description="敷島型戦艦 四番艦 三笠", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Mikasa.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 24939\n**抗堪性**\n ･防郭防御10.00％･火災浸水耐性11.00％･装甲8.00％･対水雷防御9.54％\n**装甲**\n ･装甲13mm-229mm･防郭 25mm-229mm･艦首/艦尾 16mm-127mm･砲郭 13mm-152mm･装甲甲板 32mm-51mm")
    embed.add_field(name="主砲射程", value="10.11km")

    embed.add_field(name="機動性", value="**最大速力** 18.67ノット[kt]\n**転舵速度** 5.10度/秒\n**転舵所要時間**  10.20秒 ")
    embed.add_field(name="隠蔽性", value="9.54km")
    embed.add_field(name="推力", value="15000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def katori(ctx):
    embed = discord.Embed(title="巡洋艦 Tier III Katori", description="香取型練習巡洋艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Katori.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 15151\n**抗堪性**\n ･防郭防御7.50％･火災浸水耐性10.00％･装甲5.60％･対水雷防御4.50％\n**装甲**\n •装甲6-51mm•防郭 10-6mm•艦首•艦尾 6mm•砲郭 6mm•装甲甲板 6-51mm")
    embed.add_field(name="主砲射程", value="8.53km")

    embed.add_field(name="機動性", value="**最大速力** 19.31ノット[kt]\n**転舵速度** 8.20度/秒\n**転舵所要時間**  5.70秒 ")
    embed.add_field(name="隠蔽性", value="6.30km")
    embed.add_field(name="推力", value="8000馬力")

    await ctx.send(embed=embed)

@bot.command()
async def yubari(ctx):
    embed = discord.Embed(title="巡洋艦 Tier IV Yubari", description="夕張型軽巡洋艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Yubari.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 15904\n**抗堪性**\n ･防郭防御7.50％･火災浸水耐性10.00％･装甲5.60％･対水雷防御4.50％\n**装甲**\n 装甲10mm-57mm･防郭 25mm-57mm･艦首/艦尾 10mm･装甲甲板 25mm")
    embed.add_field(name="主砲射程", value="8.65km")

    embed.add_field(name="機動性", value="**最大速力** 33.20ノット[kt]\n**転舵速度** 8.60度/秒\n**転舵所要時間**  4.20秒")
    embed.add_field(name="隠蔽性", value="6.24km")
    embed.add_field(name="推力", value="57900馬力")

    await ctx.send(embed=embed)

@bot.command()
async def kamikaze(ctx):
    embed = discord.Embed(title="駆逐艦 Tier V Kamikaze", description="神風型駆逐艦", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
    embed.set_image(url="https://mcpenano.net/WoWsB/Kamikaze.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n 10304\n**抗堪性**\n ･防郭防御5.00％･火災浸水耐性10.00％･装甲4.00％･対水雷防御3.00％\n**装甲**\n ･装甲10mm-14mm･艦首/艦尾 10mm･砲郭 10mm-14mm･装甲甲板 14mm")
    embed.add_field(name="主砲射程", value="6.68km")

    embed.add_field(name="機動性", value="**最大速力** 38.62ノット[kt]\n**転舵速度** 9.60度/秒\n**転舵所要時間**  3.30秒 ")
    embed.add_field(name="隠蔽性", value="5.70km")
    embed.add_field(name="推力", value="38500馬力")

    await ctx.send(embed=embed)


#ここからヘルプ
bot.remove_command('help')
#大日本帝国海軍ヘルプ

@bot.command()
async def japan2(ctx):
    embed = discord.Embed(title="WoWsb Bot", description="大日本帝国海軍のコマンドのリストを表示します。", color=0xeee657)
    embed.set_author(name="大日本帝国海軍", icon_url="https://mcpenano.net/WoWsB/jp.png")
#日本航空母艦ヘルプ
    embed.add_field(name="———航空母艦———", value="ここから航空母艦", inline=False)

    embed.add_field(name="!!hakuryu", value="大日本帝国海軍 航空母艦Tier X Hakuryu (白龍型航空母艦)", inline=False)
    embed.add_field(name="!!taiho", value="大日本帝国海軍 航空母艦Tier IX Taiho (大鳳型航空母艦)", inline=False)
    embed.add_field(name="!!shokaku", value="大日本帝国海軍 航空母艦Tier VIII Shokaku (翔鶴型航空母艦)", inline=False)
    embed.add_field(name="!!hiryu", value="大日本帝国海軍 航空母艦 Tier VII Hiryu (飛龍型航空母艦)", inline=False)
    embed.add_field(name="!!ryujo", value="大日本帝国海軍 航空母艦 Tier VI Ryujo (龍驤型航空母艦)", inline=False)
    embed.add_field(name="!!zuiho", value="大日本帝国海軍 航空母艦 Tier V Zuiho (瑞鳳型航空母艦)", inline=False)
    embed.add_field(name="!!hosho", value="大日本帝国海軍 航空母艦 Tier IV Hosho (鳳翔型航空母艦)", inline=False)

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

    embed.add_field(name="———プレミア艦———", value="ここからプレミアム艦", inline=False)

    embed.add_field(name="!!kamikaze", value="大日本帝国海軍 駆逐艦Tier V Kamikaze (神風型駆逐艦)", inline=False)
    embed.add_field(name="!!yubari", value="大日本帝国海軍 巡洋艦Tier IV Yubari (夕張型軽巡洋艦)", inline=False)
    embed.add_field(name="!!katori", value="大日本帝国海軍 巡洋艦Tier III Katori (香取型練習巡洋艦)", inline=False)
    embed.add_field(name="!!mikasa", value="大日本帝国海軍 戦艦Tier II Mikasa (敷島型戦艦 四番艦 三笠)", inline=False)

    await ctx.send(embed=embed)

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

    embed.add_field(name="!!harugumo", value="大日本帝国海軍 駆逐艦Tier X Harugumo (春雲型駆逐艦)", inline=False)
    embed.add_field(name="!!kitakaze", value="大日本帝国海軍 駆逐艦Tier IX Kitakaze (北風型駆逐艦(改秋月型駆逐艦))", inline=False)
    embed.add_field(name="!!akizuki", value="大日本帝国海軍 駆逐艦Tier VIII Akizuki (秋月型駆逐艦)", inline=False)
    embed.add_field(name="!!shiratsuyu", value="大日本帝国海軍 駆逐艦Tier VII Shiratsuyu (白露型駆逐艦)", inline=False)
    embed.add_field(name="!!hatsuharu", value="大日本帝国海軍 駆逐艦Tier VI Hatsuharu (初春型駆逐艦)", inline=False)
    embed.add_field(name="!!minekaze", value="大日本帝国海軍 駆逐艦Tier V Minekaze (峯風型駆逐艦)", inline=False)


    
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

    await ctx.send(embed=embed)


#普通のヘルプ
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="WoWsb Bot", description="船の数が多いので国別のヘルプになります。", color=0xeee657)
    embed.add_field(name="!!info", value="このBotの開発者などを表示します。", inline=False)
    embed.add_field(name="!!help", value="ヘルプを表示します。", inline=False)
    embed.add_field(name="!!japan", value="大日本帝国海軍の軍艦一覧を表示します。(駆逐艦、戦艦)", inline=False)
    embed.add_field(name="!!japan2", value="大日本帝国海軍の軍艦一覧を表示します。(巡洋艦、空母、プレミアム艦)", inline=False)

    await ctx.send(embed=embed)


@bot.command()
async def test(channel, guild, voice_channel):
    player = voice.create_ffmpeg_player('voice.mp3')
    player.start()

# channel = message.author.voice.voice_channel
#    voice = await client.join_voice_channel(channel)

bot.run('NDgzMTE2NzU3MDM3MzUwOTEy.DmVBtw.7Dh32aJ6otGuxB543CviSzU3W28')
