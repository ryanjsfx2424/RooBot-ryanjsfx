"""Module for the Shop cog."""
import asyncio
import contextlib
import logging
import jwt
import json
import math
import random
import time
from datetime import datetime
from typing import Any, Dict, Optional, cast, Iterable, Union, Literal

import discord
from redbot.core import Config, checks, commands, bank
from redbot.core.utils import AsyncIter
from redbot.core.utils.menus import start_adding_reactions
from redbot.core.utils.predicates import MessagePredicate, ReactionPredicate

UNIQUE_ID = 0x6AFE8000

log = logging.getLogger("red.shop")


class Ticket(commands.Cog):
    """Open Tickets"""

    
    
    
    
    def __init__(self, bot):
        super().__init__()

        self.bot = bot
        self.config = Config.get_conf(self, 195375142061211647)
        self.config.register_global(nft1qty = 1)

    @checks.admin_or_permissions(manage_guild=True)        
    @commands.command()
    async def ticketsetup(self, ctx: commands.Context):
        await ctx.send(f"To complete first time ticket setup you must run a few commands. Do not include any parenthesis in commands '( )'. \n1. Set the category for creating tickets inside of using **<ticketcategory (category channel ID)**. \n2. Set the message you would like the bot to listen for reactions using **<ticketmessage (message link)**. \n3. Set the role all Ticket Support Staff will have to gain access to new tickets using **<ticketrole (role id or mention)**. \n4. Now enable the Ticketing System using **<enable**. This can be disabled at any time using **<disable**. \nWhen tickets are finished, staff may use **<close** to delete the ticket channel. If any additional users must gain access to viewing the ticket, they may be added by staff using **<adduser (user mention or ID)**.")
 
    
    @checks.admin_or_permissions(manage_guild=True)        
    @commands.command()
    async def ticketcategory(self, ctx: commands.Context, cate: discord.CategoryChannel):
        """Set ticket opening Category"""
        await self.config.guild(ctx.guild).ticketchannel.set(cate.id)
        await ctx.send(f'Set ticket opening category to {cate.mention}')
        
#    @checks.admin_or_permissions(manage_guild=True)        
#    @commands.command()
#    async def ticketreaction(self, ctx: commands.Context, emoji):
#        """Set reaction emoji for opening Ticket"""
#        
#        await self.config.guild(ctx.guild).ticketemoji.set(emoji)
#        await ctx.send(f'Set ticket emoji to {emoji}')
        
    @checks.admin_or_permissions(manage_guild=True)        
    @commands.command()
    async def ticketmessage(self, ctx: commands.Context, message: discord.Message):
        """Set message for opening ticket"""
        await self.config.guild(ctx.guild).ticketmessagechan.set(message.channel.id)
        await self.config.guild(ctx.guild).ticketmessage.set(message.id)
        await ctx.send(f'Set ticket message to {message.jump_url}')
        #emoji = ctx.guild.fetch_emoji(await self.config.guild(ctx.guild).ticketemoji())
        #await ctx.message.add_reaction(emoji)
        
    @checks.admin_or_permissions(manage_guild=True)        
    @commands.command()
    async def ticketrole(self, ctx: commands.Context, role: discord.Role):
        """Set Mod role for viewing tickets"""
        await self.config.guild(ctx.guild).ticketrole.set(role.id)
        
        await ctx.send(f'Set Ticket Mod role to {role.name}')
        
    @commands.command()
    async def close(self, ctx: commands.Context):  
        """Close current ticket"""
        print(f'test {ctx.author.name}')
        role = ctx.guild.get_role(await self.config.guild(ctx.guild).ticketrole())
        if role in ctx.message.author.roles:
            print(f'role in {ctx.author.name}')
            if ctx.channel.name.startswith('ticket-'):
                await ctx.send('Ticket will now be closed.')
                await asyncio.sleep(5)
                await ctx.channel.delete()
        else:
            print(f'{ctx.author.name} doesnt have {role.name}')
    @commands.command()
    async def adduser(self, ctx: commands.Context, user: discord.User):     
        """Add user to view ticket"""
        role = ctx.guild.get_role(await self.config.guild(paychan.guild).ticketrole())
        if role in ctx.member.roles:
            await ctx.set_permissions(user, read_messages=True, send_messages=True)
            await ctx.send(f"{user.name} has been added to the ticket.")
            
    @commands.command()
    async def enable(self, ctx: commands.Context):   
        await self.config.guild(ctx.guild).ticketenable.set(True)   
        await ctx.send("Tickets now enabled.")  
        
    @commands.command()
    async def disable(self, ctx: commands.Context):   
        await self.config.guild(ctx.guild).ticketenable.set(False)   
        await ctx.send("Tickets now disabled.")
        
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):


        
        paychan = self.bot.get_channel(payload.channel_id)
        enabled = await self.config.guild(paychan.guild).ticketenable()
        if enabled == False or enabled == None:
            return
        else:
            role = paychan.guild.get_role(await self.config.guild(paychan.guild).ticketrole())
            chan = paychan.guild.get_channel(await self.config.guild(paychan.guild).ticketmessagechan())
            message = await chan.fetch_message(await self.config.guild(paychan.guild).ticketmessage())
            emoji = await self.config.guild(paychan.guild).ticketemoji()
            category = paychan.guild.get_channel(await self.config.guild(paychan.guild).ticketchannel())
            print(f'found react in {payload.channel_id}')
            print(f'{chan.id}')
            
            if payload.channel_id == chan.id    :
                print('found react in chan')
                if payload.message_id == message.id:
                    print('found react on message')
                    print(payload.emoji)
                    print(emoji)
                    print('found emoji')
                    ticket = await category.create_text_channel(name=f"ticket-{payload.member.name}")
                    await ticket.set_permissions(paychan.guild.default_role, read_messages=False, send_messages=False)
                    await ticket.set_permissions(role, read_messages=True, send_messages=True)
                    await ticket.set_permissions(payload.member, read_messages=True, send_messages=True)
                    await ticket.send(f"Ticket created by {payload.member.mention}. Use <close to close ticket.")
                  
            