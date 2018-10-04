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
import version
import traceback
import os
import changes

from discord.ext import commands
from discord.ext.commands import Bot

_initial_extensions = (
    'cogs.wowsb',
)


class WoWsbBot(Bot):
    def __init__(self, formatter=None, description=None, pm_help=False, **options):
        self._version = version.VERSION
        self._members = version.MEMBERS
        self._uplog = changes.CHANGES
        self._upimage = changes.UPIMAGE

        super().__init__('!!', formatter, description, pm_help, **options)
        for extension in _initial_extensions:
            try:
                self.load_extension(extension)
            except Exception:
                print(traceback.format_exc())

    async def on_ready(self):
        print(self.user.name)
        print(self.user.id)
        print(f'WoWsb-Botバージョン{self._version}は正常に起動しました。')
        await self.change_presence(activity=discord.Game(name='!!com | {} servers'.format(len(self.guilds))))
        print('—————————————————————')
        print('GNU General Public License v3.0')
        print('Copyright (c) 2018 WoWsb Japan community')
        print('開発メンバー')
        print(self._members)
        print('開発協力')
        print('WoWsb 日本コミュニティ')
        print('—————————————————————')

    def get_data(self, filename):
        return os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data', filename)


if __name__ == '__main__':

    bot = WoWsbBot()
    bot.remove_command('help')
    bot.run('トークン')