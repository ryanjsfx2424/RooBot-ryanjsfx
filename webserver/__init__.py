"""Webserver"""
import json
from pathlib import Path
from .webserver import Webserver
#from discord import app_commands
import discord

async def setup(bot):
    """Load Webserver."""
    cog = Webserver(bot)
   # await out_of_date_check("uptimeresponder", cog.__version__)

    r = bot.add_cog(cog)
    if r is not None:
        await r

    await cog.start_webserver()

    #await bot.add_cog(Webserver(bot))

