"""Verify if staked n shit"""
from .verify import Verify
from discord import app_commands
import discord

async def setup(bot):
    """Load Verify."""
    

    if not hasattr(bot, "tree"):
        bot.tree = app_commands.CommandTree(bot)
    await bot.add_cog(Verify(bot))
    await bot.tree.sync(guild=discord.Object(id=893963935672324118))
    print('synced shit')
