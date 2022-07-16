"""Module for the Sticky cog."""
import asyncio
import contextlib
import logging
from datetime import datetime
from typing import Any, Dict, Optional, cast

import discord
from redbot.core import Config, checks, commands
from redbot.core.utils.menus import start_adding_reactions
from redbot.core.utils.predicates import MessagePredicate, ReactionPredicate
from redbot.core.utils.chat_formatting import humanize_number

log = logging.getLogger("red.sticky")


class serverage(commands.Cog):
    """Sticky messages to your channels."""


    def __init__(self, bot):
        super().__init__()

        self.bot = bot
    @checks.mod_or_permissions(manage_messages=True)
    @commands.guild_only()
    @commands.group(invoke_without_command=True)
    async def serverage(self, ctx: commands.Context):
        """Sticky a message to this channel."""
        guild = self.bot.get_guild(889031115480907827)
        while True:
            human1 = int(datetime.now().timestamp())
            print(human1)
            human2 = int(ctx.guild.created_at.timestamp())
            print(human2)
            seconds = human1 - human2
            print(seconds)
            minutes = seconds / 60
            print(minutes)
            hours = minutes / 60
            print(hours)
            days = hours / 24
            print(days)
            day = round(days)
            print(day)
            channel = ctx.guild.get_channel(899155252283047946)
            count = str(day)
            print(count)
            try:
                print('trying...')
                await channel.edit(reason="InfoChannel update", name="Server Age: " + str(day) + " Days")
                print('Success?' + str(day) + str(count))
            except Exception as e:
                print(e)
            print('headin to sleep for 12 hours')
            await asyncio.sleep(43200)
            print('Done sleepin')
