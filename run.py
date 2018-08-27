import discord
from discord.ext import commands
import glob
import sys
import os.path
import importlib
import re
import asyncio

bot = commands.Bot(command_prefix='$')
client = discord.Client()

@bot.event
async def on_ready():
    print('ロード中')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print('{0.user}にログインしました。'.format(client))
    print('お知らせBotは、正常に起動しましました。')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="お知らせボット", description="お知らせBotのテスト", color=0xeee657)

    embed.set_image(url="https://xn--0vq403amku.net/wp-content/uploads/2018/08/img_1538.jpg")

    # give info about you here
    embed.add_field(name="オーナー", value="Kosugikun")
    
    
    
    embed.add_field(name="サーバー数", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="招待", value="サーバーの招待リンク")

    await ctx.send(embed=embed)

#日本巡洋艦

@bot.command()
async def hashidate(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier I Hashidate (橋立)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/Hashidate.jpg")

    # give info about you here
    embed.add_field(name="生存性", value="**継戦能力**\n9858\n**抗堪性**\n･防郭防御5.00％･火災浸水耐性10.00％･装甲5.60％･対水雷防御4.50％\n**装甲**\n ･装甲6mm-30mm･防郭 6mm-30mm･艦首/艦尾 6mm･装甲甲板 10mm")
    embed.add_field(name="主砲射程", value="待っててね")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="機動性", value="待っててね")
    embed.add_field(name="隠蔽性", value="待っててね")
    embed.add_field(name="推力", value="待っててね")

    await ctx.send(embed=embed)

@bot.command()
async def chikuma(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier II Chikuma (筑摩型防護巡洋艦)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/Chikuma.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n数値\n**抗堪性**\n･防郭防御<数値>％･火災浸水耐性<数値>％･装甲<数値>％･対水雷防御<数値>％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="<数値>")
    embed.add_field(name="機動性", value="<数値>")
    embed.add_field(name="隠蔽性", value="<数値>")
    embed.add_field(name="推力", value="<数値>")

    await ctx.send(embed=embed)

#ここからヘルプ
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="WoWsb軍艦辞典", description="コマンドのリストを表示します。", color=0xeee657)

    embed.add_field(name="$chikuma", value="大日本帝国海軍 巡洋艦Tier II chikuma (筑摩型防護巡洋艦)", inline=False)
    embed.add_field(name="$hashidate", value="大日本帝国海軍 巡洋艦Tier I Hashidate (橋立)", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run('NDgzMTE2NzU3MDM3MzUwOTEy.DmOzsQ.nvAV1-LyirC6LCeaNAJJjPwVjz8')