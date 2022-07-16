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


class Shop(commands.Cog):
    """buy shiz"""

    
    default_item_settings = {"amt": "0"}
    default_shop_settings = default_item_settings
    
    
    def __init__(self, bot):
        super().__init__()

        self.bot = bot
        self.config = Config.get_conf(self, 195375142061211648)
        self.config.register_global(nft1qty = 1, nft2qty = 5, nft3qty = 3, nft4qty = 3, nft5qty = 3, nft1name = "Crypto Coral Tribe NFT", nft2name = "Crypto Coral Tribe NFT", nft3name = "Crypto Coral Tribe NFT", nft4name = "Crypto Coral Tribe NFT",
        nft5name = "Crypto Coral Tribe NFT", nft1price = 1000000, nft2price = 500000, nft3price = 100000, nft4price = 0, nft5price = 0, shopamount = 3, nft1desc = "Grants a free Coral Tribe NFT airdrop", nft2desc = "A print from our artist João's work sent to your location of choice", 
        nft3desc = "None", nft4desc = "none", nft5desc = "none", nft1role = 970095869288407050, nft2role = 970096289138212915, nft3role = 970095445718220890, nft4role = 970096763224612914, nft5role = 970096763224612914, nft1url = "https://images-ext-2.discordapp.net/external/LMFrdX1s8eqM29RRfnl-MupAsNbyCuzpzUVZFgOyNe0/https/i.imgur.com/OYzP9uw.png", nft2url = "https://images-ext-2.discordapp.net/external/BQnd0Gld8fJg9csuyTFFx9xI0U_-kh6vJmNFfz-p97Y/https/i.imgur.com/P0yC7O2.png", nft3url = "https://images-ext-1.discordapp.net/external/dHuISVL1IWVcIhDlOP83ifRwc6foPLdVLqIcJTtQGgI/https/i.imgur.com/ZtN7kLt.png", 
        nft4url = 970096763224612914, nft5url = 970096763224612914, )
    @checks.admin_or_permissions(manage_guild=True)        
    @commands.command()
    async def setqty(self, ctx: commands.Context, num: int, *, qty):
        if num == 1:
            await self.config.nft1qty.set(qty)
        elif num == 2:
            await self.config.nft2qty.set(qty)
        elif num == 3:
            await self.config.nft3qty.set(qty)
        elif num == 4:
            await self.config.nft4qty.set(qty)
        elif num == 5:
            await self.config.nft5qty.set(qty)
        else:
            await ctx.send('Please select item 1-5')
        await ctx.send(f'set item qty to {qty}')
        
    @checks.admin_or_permissions(manage_guild=True)        
    @commands.command()
    async def setprice(self, ctx: commands.Context, num: int, *, qty: int):

        if num == 1:
            await self.config.nft1price.set(qty)
        elif num == 2:
            await self.config.nft2price.set(qty)
        elif num == 3:
            await self.config.nft3price.set(qty)
        elif num == 4:
            await self.config.nft4price.set(qty)
        elif num == 5:
            await self.config.nft5price.set(qty)
        else:
            await ctx.send('Please select item 1-5')
        await ctx.send(f'set item price to {qty}')
        
    @checks.admin_or_permissions(manage_guild=True)        
    @commands.command()
    async def setname(self, ctx: commands.Context, num: int, *, qty: str):
        if num == 1:
            await self.config.nft1name.set(qty)
        elif num == 2:
            await self.config.nft2name.set(qty)
        elif num == 3:
            await self.config.nft3name.set(qty)
        elif num == 4:
            await self.config.nft4name.set(qty)
        elif num == 5:
            await self.config.nft5name.set(qty)
        else:
            await ctx.send('Please select item 1-5')
        await ctx.send(f'set item name to {qty}')
        
    @checks.admin_or_permissions(manage_guild=True)        
    @commands.command()
    async def setimageurl(self, ctx: commands.Context, num: int, *, qty: str):
        if num == 1:
            await self.config.nft1url.set(qty)
        elif num == 2:
            await self.config.nft2url.set(qty)
        elif num == 3:
            await self.config.nft3url.set(qty)
        elif num == 4:
            await self.config.nft4url.set(qty)
        elif num == 5:
            await self.config.nft5url.set(qty)
        else:
            await ctx.send('Please select item 1-5')
        await ctx.send(f'set item url to {qty}')
        
    @checks.admin_or_permissions(manage_guild=True)        
    @commands.command()
    async def setdescription(self, ctx: commands.Context, num: int, *, qty: str):
        if num == 1:
            await self.config.nft1desc.set(qty)
        elif num == 2:
            await self.config.nft2desc.set(qty)
        elif num == 3:
            await self.config.nft3desc.set(qty)
        elif num == 4:
            await self.config.nft4desc.set(qty)
        elif num == 5:
            await self.config.nft5desc.set(qty)
        else:
            await ctx.send('Please select item 1-5')
        await ctx.send(f'set item description to {qty}')
    @checks.admin_or_permissions(manage_guild=True)        
    @commands.command()
    async def setrole(self, ctx: commands.Context, num: int, *, role: discord.Role):
        if num == 1:
            await self.config.nft1role.set(role.id)
        elif num == 2:
            await self.config.nft2role.set(role.id)
        elif num == 3:
            await self.config.nft3role.set(role.id)
        elif num == 4:
            await self.config.nft4role.set(role.id)
        elif num == 5:
            await self.config.nft5role.set(role.id)
        else:
            await ctx.send('Please select item 1-5')
        await ctx.send(f'set item role to {role.name}')
    @checks.admin_or_permissions(manage_guild=True)        
    @commands.command()
    async def setamount(self, ctx: commands.Context, num: int):
        await self.config.shopamount.set(num)
        await ctx.send(f"Set amount of items shown in shop to {num}")
    
    @checks.admin_or_permissions(manage_guild=True)    
    @commands.command()
    async def buildshop(self, ctx: commands.Context):
        """Verify if you're staked."""
        nft1name = await self.config.nft1name()
        nft2name = await self.config.nft2name()
        nft3name = await self.config.nft3name()
        nft4name = await self.config.nft4name()
        nft5name = await self.config.nft5name()
        nft1price = await self.config.nft1price()
        nft2price = await self.config.nft2price()
        nft3price = await self.config.nft3price()
        nft4price = await self.config.nft4price()
        nft5price = await self.config.nft5price()
        nft1desc = await self.config.nft1desc()
        nft2desc = await self.config.nft2desc()
        nft3desc = await self.config.nft3desc()
        nft4desc = await self.config.nft4desc()
        nft5desc = await self.config.nft5desc()
        
        embed = discord.Embed(color=0x5EC6FF)
        title = "**Discord Currency Shop**"
        options = f"<:one:944725515720335411>           ***{nft1name}***                    **QTY:** {await self.config.nft1qty()}                    **\nCOST:** {nft1price} \n**'{nft1desc}'**"
        options2 = f"<:two:944725716325527562>           ***{nft2name}***                    **QTY:** {await self.config.nft2qty()}                    **\nCOST:** {nft2price} \n**'{nft2desc}'**"
        options3 = f"<:three:970084899040141332>           ***{nft3name}***                    **QTY:** {await self.config.nft3qty()}                    **\nCOST:** {nft3price}\n**'{nft3desc}'**"
        options4 = f"4️⃣           ***{nft4name}***                    **QTY:** {await self.config.nft4qty()}                    **\nCOST:** {nft4price}\n**'{nft4desc}'**"
        options5 = f"5️⃣           ***{nft5name}***                    **QTY:** {await self.config.nft5qty()}                    **\nCOST:** {nft5price}\n**'{nft5desc}'**"
        shopamt = await self.config.shopamount()
        if shopamt == 1:
            embed.add_field(name=title, value=options, inline=False)
            embed.set_thumbnail(url=await self.config.nft1url())
            my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
            with open(my_filename2, "rb") as fh2:
                f2 = discord.File(fh2, filename=my_filename2)
            #embed.set_image(url="attachment://test.png")
            msg = await ctx.send(embed=embed)
            await msg.add_reaction("\u0031\uFE0F\u20E3")

        elif shopamt == 2:
            embed.add_field(name=title, value=options, inline=False)
            embed.set_thumbnail(url=await self.config.nft1url())
            my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
            with open(my_filename2, "rb") as fh2:
                f2 = discord.File(fh2, filename=my_filename2)
            #embed.set_image(url="attachment://test.png")
            await ctx.send(embed=embed)
            embed2 = discord.Embed(color=0x5EC6FF)
            embed2.set_thumbnail(url=await self.config.nft2url())
            embed2.add_field(name="\u200b", value=options2, inline=False)
            msg = await ctx.send(embed=embed2)
            await msg.add_reaction("\u0031\uFE0F\u20E3")
            await msg.add_reaction("\u0032\uFE0F\u20E3")
            
        elif shopamt == 3:
            embed.add_field(name=title, value=options, inline=False)
            embed.set_thumbnail(url=await self.config.nft1url())
            my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
            with open(my_filename2, "rb") as fh2:
                f2 = discord.File(fh2, filename=my_filename2)
            #embed.set_image(url="attachment://test.png")
            await ctx.send(embed=embed)
            embed2 = discord.Embed(color=0x5EC6FF)
            embed2.set_thumbnail(url=await self.config.nft2url())
            embed2.add_field(name="\u200b", value=options2, inline=False)
            await ctx.send(embed=embed2)
            embed3 = discord.Embed(color=0x5EC6FF)
            embed3.set_thumbnail(url=await self.config.nft3url())
            embed3.add_field(name="\u200b", value=options3, inline=False)
            msg = await ctx.send(embed=embed3)
            await msg.add_reaction("\u0031\uFE0F\u20E3")
            await msg.add_reaction("\u0032\uFE0F\u20E3")
            await msg.add_reaction("\u0033\uFE0F\u20E3")
        elif shopamt == 4:
            embed.add_field(name=title, value=options, inline=False)
            embed.set_thumbnail(url=await self.config.nft1url())
            my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
            with open(my_filename2, "rb") as fh2:
                f2 = discord.File(fh2, filename=my_filename2)
            #embed.set_image(url="attachment://test.png")
            await ctx.send(embed=embed)
            embed2 = discord.Embed(color=0x5EC6FF)
            embed2.set_thumbnail(url=await self.config.nft2url())
            embed2.add_field(name="\u200b", value=options2, inline=False)
            await ctx.send(embed=embed2)
            embed3 = discord.Embed(color=0x5EC6FF)
            embed3.set_thumbnail(url=await self.config.nft3url())
            embed3.add_field(name="\u200b", value=options3, inline=False)
            await ctx.send(embed=embed3)
            embed4 = discord.Embed(color=0x5EC6FF)
            embed4.set_thumbnail(url=await self.config.nft4url())
            embed4.add_field(name="\u200b", value=options4, inline=False)
            msg = await ctx.send(embed=embed4)
            await msg.add_reaction("\u0031\uFE0F\u20E3")
            await msg.add_reaction("\u0032\uFE0F\u20E3")
            await msg.add_reaction("\u0033\uFE0F\u20E3")
            await msg.add_reaction("\u0034\uFE0F\u20E3")
        elif shopamt == 5:
            embed.add_field(name=title, value=options, inline=False)
            embed.set_thumbnail(url=await self.config.nft1url())
            my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
            with open(my_filename2, "rb") as fh2:
                f2 = discord.File(fh2, filename=my_filename2)
            #embed.set_image(url="attachment://test.png")
            await ctx.send(embed=embed)
            embed2 = discord.Embed(color=0x5EC6FF)
            embed2.set_thumbnail(url=await self.config.nft2url())
            embed2.add_field(name="\u200b", value=options2, inline=False)
            await ctx.send(embed=embed2)
            embed3 = discord.Embed(color=0x5EC6FF)
            embed3.set_thumbnail(url=await self.config.nft3url())
            embed3.add_field(name="\u200b", value=options3, inline=False)
            await ctx.send(embed=embed3)
            embed4 = discord.Embed(color=0x5EC6FF)
            embed4.set_thumbnail(url=await self.config.nft4url())
            embed4.add_field(name="\u200b", value=options4, inline=False)
            msg = await ctx.send(embed=embed4)
            embed5 = discord.Embed(color=0x5EC6FF)
            embed5.set_thumbnail(url=await self.config.nft5url())
            embed5.add_field(name="\u200b", value=options5, inline=False)
            msg = await ctx.send(embed=embed5)
            await msg.add_reaction("\u0031\uFE0F\u20E3")
            await msg.add_reaction("\u0032\uFE0F\u20E3")
            await msg.add_reaction("\u0033\uFE0F\u20E3")
            await msg.add_reaction("\u0034\uFE0F\u20E3")
            await msg.add_reaction("\u0035\uFE0F\u20E3")

        
    @commands.Cog.listener("on_message")
    async def message_sent(self, message):
        if message.channel.id == 970049701351153714:
            if message.author.id != 936809874027843624:
                await message.delete()

           
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        chan = 970049701351153714
        paychan = self.bot.get_channel(payload.channel_id)
        role1 = paychan.guild.get_role(await self.config.nft1role())
        role2 = paychan.guild.get_role(await self.config.nft2role())
        role3 = paychan.guild.get_role(await self.config.nft3role())
        role4 = paychan.guild.get_role(await self.config.nft4role())
        role5 = paychan.guild.get_role(await self.config.nft5role())
        role6 = paychan.guild.get_role(970096763224612914)
        ctx = paychan
        nft1name = await self.config.nft1name()
        nft2name = await self.config.nft2name()
        nft3name = await self.config.nft3name()
        nft4name = await self.config.nft4name()
        nft5name = await self.config.nft5name()
        nft1price = await self.config.nft1price()
        nft2price = await self.config.nft2price()
        nft3price = await self.config.nft3price()
        nft4price = await self.config.nft4price()
        nft5price = await self.config.nft5price()
        nft1desc = await self.config.nft1desc()
        nft2desc = await self.config.nft2desc()
        nft3desc = await self.config.nft3desc()
        nft4desc = await self.config.nft4desc()
        nft5desc = await self.config.nft5desc()
        nft1qty = await self.config.nft1qty()
        nft2qty = await self.config.nft2qty()
        nft3qty = await self.config.nft3qty()
        nft4qty = await self.config.nft4qty()
        nft5qty = await self.config.nft5qty()
        
        if payload.channel_id == chan or payload.channel_id == 936648412756074506:
            print(payload.emoji.name)
            if payload.member.name == "Coral Keeper":
                return
            else:
                if payload.emoji.name == "1️⃣":
                    
                    if int(nft1qty) <= 0:
                        print('no qty')
                        return
                    elif role1 in payload.member.roles:
                        print('no role')
                        return
                    else:
                        bal = await bank.get_balance(payload.member)
                       # nft1pric = await self.config.nft1price
                        if int(bal) >= int(nft1price):
                            message = await self.bot.get_channel(payload.channel_id).send(f"{payload.member.mention} are you sure you would like to purchase 1 {nft1name} for {nft1price}CC? Reply 'yes' to confirm.")
                            try:
                                resp = await self.bot.wait_for(
                            "message",
                            timeout=60,
                            check=lambda m: (m.author == payload.member and m.channel == self.bot.get_channel(payload.channel_id)),
                        )
                                
                                if resp.clean_content == "yes" or resp.clean_content == "Yes" or resp.clean_content == "YES":
                                    #role = self.bot.get_guild(payload.guild_id).get_role(930839052519890964)
                                    
                                    then = await bank.get_balance(payload.member)
                                    now = int(then) - int(nft1price)
                                    await bank.set_balance(payload.member, now)
                                    await payload.member.add_roles(role1)
                                    await payload.member.add_roles(role6)
                                    thenc = await self.config.nft1qty()
                                    nowc = int(thenc) - 1
                                    await self.config.nft1qty.set(nowc)
                                    try:
                                        async for msg in paychan.history(limit=10):
                                            await msg.delete()
                                    except Exception as e:
                                        print(e)
                                    embed = discord.Embed(color=0x5EC6FF)
                                    title = "**Crypto Coral Shop**"
                                    options = f"<:one:944725515720335411>           ***{nft1name}***                                        **QTY:** {await self.config.nft1qty()}                                             **\nCOST:** {nft1price}CC \n**'{nft1desc}'**"
                                    options2 = f"<:two:944725716325527562>           ***{nft2name}***                **QTY:** {await self.config.nft2qty()}                                         **\nCOST:** {nft2price}CC \n**'{nft2desc}'**"
                                    options3 = f"<:three:970084899040141332>           ***{nft3name}***                                        **QTY:** {await self.config.nft3qty()}                                         **\nCOST:** {nft3price}CC\n**'{nft3desc}'**"
                                    options4 = f"4️⃣           ***{nft4name}***                                        **QTY:** {await self.config.nft4qty()}                                         **\nCOST:** {nft4price}CC\n**'{nft4desc}'**"
                                    options5 = f"5️⃣           ***{nft5name}***                                        **QTY:** {await self.config.nft5qty()}                                         **\nCOST:** {nft5price}CC\n**'{nft5desc}'**"
                                    shopamt = await self.config.shopamount()
                                    if shopamt == 1:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                    
                                    elif shopamt == 2:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        
                                    elif shopamt == 3:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        embed3 = discord.Embed(color=0x5EC6FF)
                                        embed3.set_thumbnail(url=await self.config.nft3url())
                                        embed3.add_field(name="\u200b", value=options3, inline=False)
                                        await ctx.send(embed=embed3)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        await msg.add_reaction("\u0033\uFE0F\u20E3")
                                    elif shopamt == 4:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        embed3 = discord.Embed(color=0x5EC6FF)
                                        embed3.set_thumbnail(url=await self.config.nft3url())
                                        embed3.add_field(name="\u200b", value=options3, inline=False)
                                        await ctx.send(embed=embed3)
                                        embed4 = discord.Embed(color=0x5EC6FF)
                                        embed4.set_thumbnail(url=await self.config.nft4url())
                                        embed4.add_field(name="\u200b", value=options4, inline=False)
                                        msg = await ctx.send(embed=embed4)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        await msg.add_reaction("\u0033\uFE0F\u20E3")
                                        await msg.add_reaction("\u0034\uFE0F\u20E3")
                                    elif shopamt == 5:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        embed3 = discord.Embed(color=0x5EC6FF)
                                        embed3.set_thumbnail(url=await self.config.nft3url())
                                        embed3.add_field(name="\u200b", value=options3, inline=False)
                                        await ctx.send(embed=embed3)
                                        embed4 = discord.Embed(color=0x5EC6FF)
                                        embed4.set_thumbnail(url=await self.config.nft4url())
                                        embed4.add_field(name="\u200b", value=options4, inline=False)
                                        msg = await ctx.send(embed=embed4)
                                        embed5 = discord.Embed(color=0x5EC6FF)
                                        embed5.set_thumbnail(url=await self.config.nft5url())
                                        embed5.add_field(name="\u200b", value=options5, inline=False)
                                        msg = await ctx.send(embed=embed5)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        await msg.add_reaction("\u0033\uFE0F\u20E3")
                                        await msg.add_reaction("\u0034\uFE0F\u20E3")
                                        await msg.add_reaction("\u0035\uFE0F\u20E3")
                                    await paychan.guild.get_channel(970103229180436520).send(f'<@&978612091269292062>, {payload.member.mention} just bought {nft1name}')
                                else:
                                    deel = await self.bot.get_channel(payload.channel_id).send("Cancelled.")
                                    await asyncio.sleep(3)
                                    async for msg in paychan.history(limit=8):
                                        if msg.author.id != 936809874027843624:
                                            await msg.delete()
                                    try:
                                        await deel.delete()
                                    except Exception as e:
                                        print(e)
                                    try:
                                        await message.delete()
                                    except Exception as e:
                                        print(e)
                                    return
                            except asyncio.TimeoutError:
                                msg = await ctx.send(("You took too long to respond."))
                                await asyncio.sleep(5)
                                await msg.delete()
                                await message.delete()
                                return
                        else:
                            msg = await self.bot.get_channel(payload.channel_id).send("Insufficient CC.")
                            await asyncio.sleep(3)
                            #async for msg in paychan.history(limit=1):
                            await msg.delete()
                            return
                        
                elif payload.emoji.name == "2️⃣":
                    shopamt = await self.config.shopamount()
                    if shopamt <= 1:

                        return
                    if int(nft2qty) <= 0:
                        print('2 no qty')
                        return
                    elif role2 in payload.member.roles:
                        print('role in person 2')
                        return
                    else:
                        bal = await bank.get_balance(payload.member)
                        #nft2pric = await self.config.nft2price
                        if int(bal) >= int(nft2price):
                            message = await self.bot.get_channel(payload.channel_id).send(f"{payload.member.mention} are you sure you would like to purchase 1 {nft2name} for {nft2price}CC? Reply 'yes' to confirm.")
                            try:
                                resp = await self.bot.wait_for(
                            "message",
                            timeout=60,
                            check=lambda m: (m.author == payload.member and m.channel == self.bot.get_channel(payload.channel_id)),
                        )
                                if resp.clean_content == "yes" or resp.clean_content == "Yes" or resp.clean_content == "YES":
                                    #role = self.bot.get_guild(payload.guild_id).get_role(930839052519890964)
                                    
                                    then = await bank.get_balance(payload.member)
                                    now = int(then) - int(nft2price)
                                    await bank.set_balance(payload.member, now)
                                    await payload.member.add_roles(role2)
                                    await payload.member.add_roles(role6)
                                    thenc = await self.config.nft2qty()
                                    nowc = int(thenc) - 1
                                    await self.config.nft2qty.set(nowc)
                                    try:
                                        async for msg in paychan.history(limit=10):
                                            await msg.delete()
                                    except Exception as e:
                                        print(e)
                                    embed = discord.Embed(color=0x5EC6FF)
                                    title = "**Crypto Coral Shop**"
                                    options = f"<:one:944725515720335411>           ***{nft1name}***                                        **QTY:** {await self.config.nft1qty()}                                             **\nCOST:** {nft1price}CC \n**'{nft1desc}'**"
                                    options2 = f"<:two:944725716325527562>           ***{nft2name}***                **QTY:** {await self.config.nft2qty()}                                         **\nCOST:** {nft2price}CC \n**'{nft2desc}'**"
                                    options3 = f"<:three:970084899040141332>           ***{nft3name}***                                        **QTY:** {await self.config.nft3qty()}                                         **\nCOST:** {nft3price}CC\n**'{nft3desc}'**"
                                    options4 = f"4️⃣           ***{nft4name}***                                        **QTY:** {await self.config.nft4qty()}                                         **\nCOST:** {nft4price}CC\n**'{nft4desc}'**"
                                    options5 = f"5️⃣           ***{nft5name}***                                        **QTY:** {await self.config.nft5qty()}                                         **\nCOST:** {nft5price}CC\n**'{nft5desc}'**"
                                    
                                    if shopamt == 1:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                    
                                    elif shopamt == 2:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        
                                    elif shopamt == 3:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        embed3 = discord.Embed(color=0x5EC6FF)
                                        embed3.set_thumbnail(url=await self.config.nft3url())
                                        embed3.add_field(name="\u200b", value=options3, inline=False)
                                        await ctx.send(embed=embed3)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        await msg.add_reaction("\u0033\uFE0F\u20E3")
                                    elif shopamt == 4:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        embed3 = discord.Embed(color=0x5EC6FF)
                                        embed3.set_thumbnail(url=await self.config.nft3url())
                                        embed3.add_field(name="\u200b", value=options3, inline=False)
                                        await ctx.send(embed=embed3)
                                        embed4 = discord.Embed(color=0x5EC6FF)
                                        embed4.set_thumbnail(url=await self.config.nft4url())
                                        embed4.add_field(name="\u200b", value=options4, inline=False)
                                        msg = await ctx.send(embed=embed4)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        await msg.add_reaction("\u0033\uFE0F\u20E3")
                                        await msg.add_reaction("\u0034\uFE0F\u20E3")
                                    elif shopamt == 5:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        embed3 = discord.Embed(color=0x5EC6FF)
                                        embed3.set_thumbnail(url=await self.config.nft3url())
                                        embed3.add_field(name="\u200b", value=options3, inline=False)
                                        await ctx.send(embed=embed3)
                                        embed4 = discord.Embed(color=0x5EC6FF)
                                        embed4.set_thumbnail(url=await self.config.nft4url())
                                        embed4.add_field(name="\u200b", value=options4, inline=False)
                                        msg = await ctx.send(embed=embed4)
                                        embed5 = discord.Embed(color=0x5EC6FF)
                                        embed5.set_thumbnail(url=await self.config.nft5url())
                                        embed5.add_field(name="\u200b", value=options5, inline=False)
                                        msg = await ctx.send(embed=embed5)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        await msg.add_reaction("\u0033\uFE0F\u20E3")
                                        await msg.add_reaction("\u0034\uFE0F\u20E3")
                                        await msg.add_reaction("\u0035\uFE0F\u20E3")
                                    await paychan.guild.get_channel(970103229180436520).send(f'<@&978612091269292062>, {payload.member.mention} just bought {nft2name}')
                                else:
                                    deel = await self.bot.get_channel(payload.channel_id).send("Cancelled.")
                                    await asyncio.sleep(3)
                                    async for msg in paychan.history(limit=8):
                                        if msg.author.id != 936809874027843624:
                                            await msg.delete()
                                    try:
                                        await deel.delete()
                                    except Exception as e:
                                        print(e)
                                    try:
                                        await message.delete()
                                    except Exception as e:
                                        print(e)
                                    return
                            except asyncio.TimeoutError:
                                msg = await ctx.send(("You took too long to respond."))
                                await asyncio.sleep(5)
                                await msg.delete()
                                await message.delete()
                                return
                        else:
                            msg = await self.bot.get_channel(payload.channel_id).send("Insufficient CC.")
                            await asyncio.sleep(3)
                            #async for msg in paychan.history(limit=1):
                            await msg.delete()
                            return
                   
                elif payload.emoji.name == "3️⃣":
                    shopamt = await self.config.shopamount()
                    if shopamt <= 2:
                        return
                    if int(nft3qty) <= 0:
                        print('no qty 3')
                        return
                    elif role3 in payload.member.roles:
                        return
                    else:
                       # nft3pric = await self.config.nft3price
                        bal = await bank.get_balance(payload.member)
                        if int(bal) >= int(nft3price):
                            message = await self.bot.get_channel(payload.channel_id).send(f"{payload.member.mention} are you sure you would like to purchase 1 {nft3name} for {nft3price}CC? Reply 'yes' to confirm.")
                            try:
                                resp = await self.bot.wait_for(
                            "message",
                            timeout=60,
                            check=lambda m: (m.author == payload.member and m.channel == self.bot.get_channel(payload.channel_id)),
                        )
                                if resp.clean_content == "yes" or resp.clean_content == "Yes" or resp.clean_content == "YES":
                                    #role = self.bot.get_guild(payload.guild_id).get_role(930839052519890964)
                                    
                                    then = await bank.get_balance(payload.member)
                                    now = int(then) - int(nft3price)
                                    await bank.set_balance(payload.member, now)
                                    await payload.member.add_roles(role3)
                                    await payload.member.add_roles(role6)
                                    thenc = await self.config.nft3qty()
                                    nowc = int(thenc) - 1
                                    await self.config.nft3qty.set(nowc)
                                    try:
                                        async for msg in paychan.history(limit=10):
                                            await msg.delete()
                                    except Exception as e:
                                        print(e)
                                    embed = discord.Embed(color=0x5EC6FF)
                                    title = "**Crypto Coral Shop**"
                                    options = f"<:one:944725515720335411>           ***{nft1name}***                                        **QTY:** {await self.config.nft1qty()}                                             **\nCOST:** {nft1price}CC \n**'{nft1desc}'**"
                                    options2 = f"<:two:944725716325527562>           ***{nft2name}***                **QTY:** {await self.config.nft2qty()}                                         **\nCOST:** {nft2price}CC \n**'{nft2desc}'**"
                                    options3 = f"<:three:970084899040141332>           ***{nft3name}***                                        **QTY:** {await self.config.nft3qty()}                                         **\nCOST:** {nft3price}CC\n**'{nft3desc}'**"
                                    options4 = f"4️⃣           ***{nft4name}***                                        **QTY:** {await self.config.nft4qty()}                                         **\nCOST:** {nft4price}CC\n**'{nft4desc}'**"
                                    options5 = f"5️⃣           ***{nft5name}***                                        **QTY:** {await self.config.nft5qty()}                                         **\nCOST:** {nft5price}CC\n**'{nft5desc}'**"
                                    shopamt = await self.config.shopamount()
                                    if shopamt == 1:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                    
                                    elif shopamt == 2:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        
                                    elif shopamt == 3:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        embed3 = discord.Embed(color=0x5EC6FF)
                                        embed3.set_thumbnail(url=await self.config.nft3url())
                                        embed3.add_field(name="\u200b", value=options3, inline=False)
                                        await ctx.send(embed=embed3)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        await msg.add_reaction("\u0033\uFE0F\u20E3")
                                    elif shopamt == 4:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        embed3 = discord.Embed(color=0x5EC6FF)
                                        embed3.set_thumbnail(url=await self.config.nft3url())
                                        embed3.add_field(name="\u200b", value=options3, inline=False)
                                        await ctx.send(embed=embed3)
                                        embed4 = discord.Embed(color=0x5EC6FF)
                                        embed4.set_thumbnail(url=await self.config.nft4url())
                                        embed4.add_field(name="\u200b", value=options4, inline=False)
                                        msg = await ctx.send(embed=embed4)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        await msg.add_reaction("\u0033\uFE0F\u20E3")
                                        await msg.add_reaction("\u0034\uFE0F\u20E3")
                                    elif shopamt == 5:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        embed3 = discord.Embed(color=0x5EC6FF)
                                        embed3.set_thumbnail(url=await self.config.nft3url())
                                        embed3.add_field(name="\u200b", value=options3, inline=False)
                                        await ctx.send(embed=embed3)
                                        embed4 = discord.Embed(color=0x5EC6FF)
                                        embed4.set_thumbnail(url=await self.config.nft4url())
                                        embed4.add_field(name="\u200b", value=options4, inline=False)
                                        msg = await ctx.send(embed=embed4)
                                        embed5 = discord.Embed(color=0x5EC6FF)
                                        embed5.set_thumbnail(url=await self.config.nft5url())
                                        embed5.add_field(name="\u200b", value=options5, inline=False)
                                        msg = await ctx.send(embed=embed5)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        await msg.add_reaction("\u0033\uFE0F\u20E3")
                                        await msg.add_reaction("\u0034\uFE0F\u20E3")
                                        await msg.add_reaction("\u0035\uFE0F\u20E3")
                                    await paychan.guild.get_channel(970103229180436520).send(f'<@&978612091269292062>, {payload.member.mention} just bought {nft3name}')
                                else:
                                    deel = await self.bot.get_channel(payload.channel_id).send("Cancelled.")
                                    await asyncio.sleep(3)
                                    async for msg in paychan.history(limit=8):
                                        if msg.author.id != 936809874027843624:
                                            await msg.delete()
                                    try:
                                        await deel.delete()
                                    except Exception as e:
                                        print(e)
                                    try:
                                        await message.delete()
                                    except Exception as e:
                                        print(e)
                                    return
                            except asyncio.TimeoutError:
                                msg = await ctx.send(("You took too long to respond."))
                                await asyncio.sleep(5)
                                await msg.delete()
                                await message.delete()
                                return
                        else:
                            msg = await self.bot.get_channel(payload.channel_id).send("Insufficient CC.")
                            await asyncio.sleep(3)
                            #async for msg in paychan.history(limit=1):
                            await msg.delete()
                            return
                            
                elif payload.emoji.name == "4️⃣":
                    shopamt = await self.config.shopamount()
                    if shopamt <= 3:
                        return
                    if int(nft4qty) <= 0:
                        print(f'no qty 4')
                        return
                    elif role4 in payload.member.roles:
                        print(f'{role4.name} already has 4')
                        return
                    else:
                        #nft4pric = await self.config.nft4price
                        bal = await bank.get_balance(payload.member)
                        if int(bal) >= int(nft4price):
                            message = await self.bot.get_channel(payload.channel_id).send(f"{payload.member.mention} are you sure you would like to purchase 1 {nft4name} for {nft4price}CC? Reply 'yes' to confirm.")
                            try:
                                resp = await self.bot.wait_for(
                            "message",
                            timeout=60,
                            check=lambda m: (m.author == payload.member and m.channel == self.bot.get_channel(payload.channel_id)),
                        )
                                if resp.clean_content == "yes" or resp.clean_content == "Yes" or resp.clean_content == "YES":
                                    #role = self.bot.get_guild(payload.guild_id).get_role(930839052519890964)
                                    
                                    then = await bank.get_balance(payload.member)
                                    now = int(then) - int(nft4price)
                                    await bank.set_balance(payload.member, now)
                                    await payload.member.add_roles(role4)
                                    await payload.member.add_roles(role6)
                                    thenc = await self.config.nft4qty()
                                    nowc = int(thenc) - 1
                                    await self.config.nft4qty.set(nowc)
                                    try:
                                        async for msg in paychan.history(limit=10):
                                            await msg.delete()
                                    except Exception as e:
                                        print(e)
                                    embed = discord.Embed(color=0x5EC6FF)
                                    title = "**Crypto Coral Shop**"
                                    options = f"<:one:944725515720335411>           ***{nft1name}***                                        **QTY:** {await self.config.nft1qty()}                                             **\nCOST:** {nft1price}CC \n**'{nft1desc}'**"
                                    options2 = f"<:two:944725716325527562>           ***{nft2name}***                **QTY:** {await self.config.nft2qty()}                                         **\nCOST:** {nft2price}CC \n**'{nft2desc}'**"
                                    options3 = f"<:three:970084899040141332>           ***{nft3name}***                                        **QTY:** {await self.config.nft3qty()}                                         **\nCOST:** {nft3price}CC\n**'{nft3desc}'**"
                                    options4 = f"4️⃣           ***{nft4name}***                                        **QTY:** {await self.config.nft4qty()}                                         **\nCOST:** {nft4price}CC\n**'{nft4desc}'**"
                                    options5 = f"5️⃣           ***{nft5name}***                                        **QTY:** {await self.config.nft5qty()}                                         **\nCOST:** {nft5price}CC\n**'{nft5desc}'**"
                                    shopamt = await self.config.shopamount()
                                    if shopamt == 1:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                    
                                    elif shopamt == 2:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        
                                    elif shopamt == 3:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        embed3 = discord.Embed(color=0x5EC6FF)
                                        embed3.set_thumbnail(url=await self.config.nft3url())
                                        embed3.add_field(name="\u200b", value=options3, inline=False)
                                        await ctx.send(embed=embed3)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        await msg.add_reaction("\u0033\uFE0F\u20E3")
                                    elif shopamt == 4:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        embed3 = discord.Embed(color=0x5EC6FF)
                                        embed3.set_thumbnail(url=await self.config.nft3url())
                                        embed3.add_field(name="\u200b", value=options3, inline=False)
                                        await ctx.send(embed=embed3)
                                        embed4 = discord.Embed(color=0x5EC6FF)
                                        embed4.set_thumbnail(url=await self.config.nft4url())
                                        embed4.add_field(name="\u200b", value=options4, inline=False)
                                        msg = await ctx.send(embed=embed4)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        await msg.add_reaction("\u0033\uFE0F\u20E3")
                                        await msg.add_reaction("\u0034\uFE0F\u20E3")
                                    elif shopamt == 5:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        embed3 = discord.Embed(color=0x5EC6FF)
                                        embed3.set_thumbnail(url=await self.config.nft3url())
                                        embed3.add_field(name="\u200b", value=options3, inline=False)
                                        await ctx.send(embed=embed3)
                                        embed4 = discord.Embed(color=0x5EC6FF)
                                        embed4.set_thumbnail(url=await self.config.nft4url())
                                        embed4.add_field(name="\u200b", value=options4, inline=False)
                                        msg = await ctx.send(embed=embed4)
                                        embed5 = discord.Embed(color=0x5EC6FF)
                                        embed5.set_thumbnail(url=await self.config.nft5url())
                                        embed5.add_field(name="\u200b", value=options5, inline=False)
                                        msg = await ctx.send(embed=embed5)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        await msg.add_reaction("\u0033\uFE0F\u20E3")
                                        await msg.add_reaction("\u0034\uFE0F\u20E3")
                                        await msg.add_reaction("\u0035\uFE0F\u20E3")
                                    await paychan.guild.get_channel(970103229180436520).send(f'<@&978612091269292062>, {payload.member.mention} just bought {nft4name}')
                                else:
                                    deel = await self.bot.get_channel(payload.channel_id).send("Cancelled.")
                                    await asyncio.sleep(3)
                                    async for msg in paychan.history(limit=8):
                                        if msg.author.id != 936809874027843624:
                                            await msg.delete()
                                    try:
                                        await deel.delete()
                                    except Exception as e:
                                        print(e)
                                    try:
                                        await message.delete()
                                    except Exception as e:
                                        print(e)
                                    return
                            except asyncio.TimeoutError:
                                msg = await ctx.send(("You took too long to respond."))
                                await asyncio.sleep(5)
                                await msg.delete()
                                await message.delete()
                                return
                        else:
                            msg = await self.bot.get_channel(payload.channel_id).send("Insufficient CC.")
                            await asyncio.sleep(3)
                            #async for msg in paychan.history(limit=1):
                            await msg.delete()
                            return
                            
                elif payload.emoji.name == "5️⃣":
                    shopamt = await self.config.shopamount()
                    if shopamt <= 4:
                        print(f'{shopamt} no amt')
                        return
                    if int(nft5qty) <= 0:
                        print('5 no qty')
                        return
                    elif role5 in payload.member.roles:
                        print(f'{role5.name} already has')
                        return
                    else:
                        bal = await bank.get_balance(payload.member)
                        #nft5pric = await self.config.nft5price
                        if int(bal) >= int(nft5price):
                            message = await self.bot.get_channel(payload.channel_id).send(f"{payload.member.mention} are you sure you would like to purchase 1 {nft5name} for {nft5price}CC? Reply 'yes' to confirm.")
                            try:
                                resp = await self.bot.wait_for(
                            "message",
                            timeout=60,
                            check=lambda m: (m.author == payload.member and m.channel == self.bot.get_channel(payload.channel_id)),
                        )
                                if resp.clean_content == "yes" or resp.clean_content == "Yes" or resp.clean_content == "YES":
                                    #role = self.bot.get_guild(payload.guild_id).get_role(930839052519890964)
                                    
                                    then = await bank.get_balance(payload.member)
                                    now = int(then) - int(nft5price)
                                    await bank.set_balance(payload.member, now)
                                    await payload.member.add_roles(role5)
                                    await payload.member.add_roles(role6)
                                    thenc = await self.config.nft5qty()
                                    nowc = int(thenc) - 1
                                    await self.config.nft5qty.set(nowc)
                                    try:
                                        async for msg in paychan.history(limit=10):
                                            await msg.delete()
                                    except Exception as e:
                                        print(e)
                                    embed = discord.Embed(color=0x5EC6FF)
                                    title = "**Crypto Coral Shop**"
                                    options = f"<:one:944725515720335411>           ***{nft1name}***                                        **QTY:** {await self.config.nft1qty()}                                             **\nCOST:** {nft1price}CC \n**'{nft1desc}'**"
                                    options2 = f"<:two:944725716325527562>           ***{nft2name}***                **QTY:** {await self.config.nft2qty()}                                         **\nCOST:** {nft2price}CC \n**'{nft2desc}'**"
                                    options3 = f"<:three:970084899040141332>           ***{nft3name}***                                        **QTY:** {await self.config.nft3qty()}                                         **\nCOST:** {nft3price}CC\n**'{nft3desc}'**"
                                    options4 = f"4️⃣           ***{nft4name}***                                        **QTY:** {await self.config.nft4qty()}                                         **\nCOST:** {nft4price}CC\n**'{nft4desc}'**"
                                    options5 = f"5️⃣           ***{nft5name}***                                        **QTY:** {await self.config.nft5qty()}                                         **\nCOST:** {nft5price}CC\n**'{nft5desc}'**"
                                    shopamt = await self.config.shopamount()
                                    if shopamt == 1:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                    
                                    elif shopamt == 2:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        
                                    elif shopamt == 3:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        embed3 = discord.Embed(color=0x5EC6FF)
                                        embed3.set_thumbnail(url=await self.config.nft3url())
                                        embed3.add_field(name="\u200b", value=options3, inline=False)
                                        await ctx.send(embed=embed3)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        await msg.add_reaction("\u0033\uFE0F\u20E3")
                                    elif shopamt == 4:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        embed3 = discord.Embed(color=0x5EC6FF)
                                        embed3.set_thumbnail(url=await self.config.nft3url())
                                        embed3.add_field(name="\u200b", value=options3, inline=False)
                                        await ctx.send(embed=embed3)
                                        embed4 = discord.Embed(color=0x5EC6FF)
                                        embed4.set_thumbnail(url=await self.config.nft4url())
                                        embed4.add_field(name="\u200b", value=options4, inline=False)
                                        msg = await ctx.send(embed=embed4)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        await msg.add_reaction("\u0033\uFE0F\u20E3")
                                        await msg.add_reaction("\u0034\uFE0F\u20E3")
                                    elif shopamt == 5:
                                        embed.add_field(name=title, value=options, inline=False)
                                        embed.set_thumbnail(url=await self.config.nft1url())
                                        my_filename2 = r"C:\Users\Administrator\Downloads\test.png"
                                        with open(my_filename2, "rb") as fh2:
                                            f2 = discord.File(fh2, filename=my_filename2)
                                        #embed.set_image(url="attachment://test.png")
                                        await ctx.send(embed=embed)
                                        embed2 = discord.Embed(color=0x5EC6FF)
                                        embed2.set_thumbnail(url=await self.config.nft2url())
                                        embed2.add_field(name="\u200b", value=options2, inline=False)
                                        await ctx.send(embed=embed2)
                                        embed3 = discord.Embed(color=0x5EC6FF)
                                        embed3.set_thumbnail(url=await self.config.nft3url())
                                        embed3.add_field(name="\u200b", value=options3, inline=False)
                                        await ctx.send(embed=embed3)
                                        embed4 = discord.Embed(color=0x5EC6FF)
                                        embed4.set_thumbnail(url=await self.config.nft4url())
                                        embed4.add_field(name="\u200b", value=options4, inline=False)
                                        msg = await ctx.send(embed=embed4)
                                        embed5 = discord.Embed(color=0x5EC6FF)
                                        embed5.set_thumbnail(url=await self.config.nft5url())
                                        embed5.add_field(name="\u200b", value=options5, inline=False)
                                        msg = await ctx.send(embed=embed5)
                                        await msg.add_reaction("\u0031\uFE0F\u20E3")
                                        await msg.add_reaction("\u0032\uFE0F\u20E3")
                                        await msg.add_reaction("\u0033\uFE0F\u20E3")
                                        await msg.add_reaction("\u0034\uFE0F\u20E3")
                                        await msg.add_reaction("\u0035\uFE0F\u20E3")
                                    await paychan.guild.get_channel(970103229180436520).send(f'<@&978612091269292062>, {payload.member.mention} just bought {nft5name}')
                                else:
                                    deel = await self.bot.get_channel(payload.channel_id).send("Cancelled.")
                                    await asyncio.sleep(3)
                                    async for msg in paychan.history(limit=8):
                                        if msg.author.id != 936809874027843624:
                                            await msg.delete()
                                    try:
                                        await deel.delete()
                                    except Exception as e:
                                        print(e)
                                    try:
                                        await message.delete()
                                    except Exception as e:
                                        print(e)
                                    return
                            except asyncio.TimeoutError:
                                msg = await ctx.send(("You took too long to respond."))
                                await asyncio.sleep(5)
                                await msg.delete()
                                await message.delete()
                                return
                        else:
                            msg = await self.bot.get_channel(payload.channel_id).send("Insufficient CC.")
                            await asyncio.sleep(3)
                            #async for msg in paychan.history(limit=1):
                            await msg.delete()
                            return