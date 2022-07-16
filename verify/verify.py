"""Module for the Verify cog."""
import asyncio
import contextlib
import logging
import jwt
import requests
import json
import math
import random
import io
import time
from datetime import datetime
from typing import Any, Dict, Optional, cast, Iterable, Union, Literal

import discord
from discord import app_commands

from redbot.core import Config, checks, commands
from redbot.core.utils import AsyncIter
from redbot.core.utils.menus import start_adding_reactions
from redbot.core.utils.predicates import MessagePredicate, ReactionPredicate

UNIQUE_ID = 0x6AFE8000

log = logging.getLogger("red.verify")


class Verify(commands.Cog):
    """Verify staking status"""

    REPOST_COOLDOWN = 3
    default_member_settings = {"staked": 'no', "owner": 'no', "rweth": 'no', "timesince": 1646606327}
    default_user_settings = default_member_settings
    
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.config = Config.get_conf(self, 195375142061211648, force_registration=True)
        self.config.register_member(**self.default_member_settings)
        self.config.register_user(**self.default_user_settings)
        

        
        
    @checks.mod_or_permissions(manage_roles=True)   
    @commands.command()
    async def urllist(self, ctx: commands.Context): 
        stream = io.BytesIO()
        channel2 = self.bot.get_channel(929591652744585256)
        async for message in channel2.history(limit=20000):
            for msg in message.content.split():
                if msg.startswith("https://twitter.com"):
                    stream.write(msg.encode("utf-8"))
                    stream.write("\n".encode("utf-8"))
        stream.seek(0)
        return await ctx.send(
            file=discord.File(stream, filename=f"urls.md"),
            delete_after=3000,
        )

    @commands.command()
    async def rarity(self, ctx: commands.Context, joeyid):    
        if ctx.channel.id == 930236283815620668 or ctx.channel.id == 894352684138778654:
            r = requests.get(url =  f"https://rootroop.herokuapp.com/joey/rarity/{joeyid}")
            dr = requests.get(url =  f"https://rootroop.herokuapp.com/joey/{joeyid}")
            
            try:
                data = r.json()
                datad = dr.json()
            except Exception as e:
                print(f'Error on {joeyid} {e}')
                return
            try:
                error = data['error']
                await ctx.send(f'Joey #{joeyid} is not yet matured!')
                return
            except Exception as e:
                score = data['score']
                rank = data['rank']    
                pic = datad['image']
                embed = discord.Embed(color=0x5EC6FF)
                title = f"**Joey #{joeyid}**"
                options = f"**Rarity Score:** {score}\n**Rarity Rank:** {rank}"
                embed.add_field(name=title, value=options, inline=False)
                embed.set_image(url=pic)
                await ctx.send(embed=embed)
        else:
            return
       



    @commands.Cog.listener("on_message")
    async def message_sent(self, message):
        if message.author.id == 894410387716440154 or message.author.id == 936809874027843624:
            return
        pp =  await self.config.user(message.author).timesince()
      #  print(discord.utils.utcnow().timestamp())
      #  print(pp)
        timenow = discord.utils.utcnow().timestamp() - pp
       # print(round(timenow))
        if timenow >= 21600:
            print(f'{timenow} {message.author.name} greater 6 hours')
            
            try:
                if message.guild.id == 893963935672324118:
                    
                    role = message.guild.get_role(894357379326558268)
                    
                    try:
    
                        
                        chann = message.guild.get_channel(899019958451839046)
                        
                        is_staked = await self.config.user(message.author).staked()
                        is_owner = await self.config.user(message.author).owner()
                        if is_staked == 'no' and is_owner == 'no':
                            
                            pass
                        else:
                            await asyncio.sleep(5)
                            await chann.send(f'checking api for {message.author.name}')
                            try:
                                r = requests.get(url =  f"https://api.rootroop.com/verify.php?discordId={message.author.id}")
                            except Exception as e:
                                print(e)
                                return
                            if r.text == "Discord ID not registered":
                                rolee = message.guild.get_role(894357379326558268)
                                role1 = message.guild.get_role(929848280672796692)
                                role2 = message.guild.get_role(930636344559013919)
                                role3 = message.guild.get_role(929848467008942120)
                                role4 = message.guild.get_role(929848579835695134)
                                role5 = message.guild.get_role(929848828797009951)
                                role6 = message.guild.get_role(930623374974132314)
                                role7 = message.guild.get_role(930623720723193906)
                                if rolee in message.author.roles:
                                    print(f"warning {message.author.name}")
                                    #await message.guild.get_channel(930236283815620668).send(f"{message.author.mention} Due to recent upgrades, we are moving all Roo verification, staked or not, to our in-house bot. For information on regaining access to Owner-only channels, please head to <#955628877273759766> or type /verifyroo.")
                                else:
                                    pass
                                await message.author.remove_roles(role3)
                                await message.author.remove_roles(rolee)
                                await message.author.remove_roles(role2)
                                await message.author.remove_roles(role1)
                                await message.author.remove_roles(role4)
                                await message.author.remove_roles(role5)
                                await message.author.remove_roles(role6)
                                await message.author.remove_roles(role7)
                                
                            else:
                                await self.config.user(message.author).timesince.set(discord.utils.utcnow().timestamp())
                                try:
                                    data = r.json() 
                                except Exception as e:
                                    print(e)
                                    return
                                roo = data['ROO']
                                tokens = data['RooTroopNFT']
                                xROO = data['xROO']
                                newxROO = xROO 
                                xrooweth = data['xRooWETH']
                                newxrooweth = xrooweth 
                                newroo = roo 
                                rolee = message.guild.get_role(894357379326558268)
                                role1 = message.guild.get_role(929848280672796692)
                                role2 = message.guild.get_role(930636344559013919)
                                role3 = message.guild.get_role(929848467008942120)
                                role4 = message.guild.get_role(929848579835695134)
                                role5 = message.guild.get_role(929848828797009951)
                                role6 = message.guild.get_role(930623374974132314)
                                role7 = message.guild.get_role(930623720723193906)
                                print(f'{message.author.name} has {tokens} tokens, {roo} roo, {xROO} xroo, {xrooweth} xrooweth')
                                #role11 = message.guild.get_role(8894357379326558268)
                             #   await chann.send(f'{message.author.name} has {roo} roo, {xROO} xROO, {tokens} roo nfts, {xrooweth} xrooweth.')
                                if roo == 0:
                                   # print(f'{message.author.name} 0 roo')
                                    if xROO == 0:
                                        await self.config.user(message.author).staked.set('no')
                                       # print(f'{message.author.name} 0 xroo')
                                        if tokens == 0:
                                            await self.config.user(message.author).owner.set('no')
                                           # print(f'{message.author.name} 0 token')
                                            if xrooweth > 0:
                                                await self.config.user(message.author).staked.set('yes')
                                                
                                                await message.author.add_roles(rolee)
                                               # print(f'{message.author.name} some xrooweth')
                                            else:
                                               # print(f'{message.author.name} 0 rooweth')
                                                await chann.send(f"<@195375142061211648> {message.author.mention} shouldnt have role.")
                                               # await message.author.remove_roles([role, role1, role2, role3, role4, role5, role6, role7])
                                                await self.config.user(message.author).staked.set('no')
                                                await self.config.user(message.author).owner.set('no')
                                                try:
                                                    try:
                                                        await message.author.remove_roles(role1)
                                                    except Exception as e:
                                                        print(f'{message.author.name} fucked some shit {e}')
                                                    try:
                                                        await message.author.remove_roles(role)
                                                    except Exception as e:
                                                        print(f'{message.author.name} fucked some shit {e}')
                                                    try:
                                                        await message.author.remove_roles(role2)
                                                    except Exception as e:
                                                        print(f'{message.author.name} fucked some shit {e}')
                                                    try:
                                                        await message.author.remove_roles(role3)
                                                    except Exception as e:
                                                        print(f'{message.author.name} fucked some shit {e}')
                                                    try:
                                                        await message.author.remove_roles(role4)
                                                    except Exception as e:
                                                        print(f'{message.author.name} fucked some shit {e}')
                                                    try:
                                                        await message.author.remove_roles(role5)
                                                    except Exception as e:
                                                        print(f'{message.author.name} fucked some shit {e}')
                                                    try:
                                                        await message.author.remove_roles(role6)
                                                    except Exception as e:
                                                        print(f'{message.author.name} fucked some shit {e}')
                                                    try:
                                                        await message.author.remove_roles(role7)
                                                    except Exception as e:
                                                        print(f'{message.author.name} fucked some shit {e}')
                                                    
                                                    print(f'removed role from {message.author.name} no owner, no stake')
                                                    await chann.send('successfully removed roles')
                                                    
                                                except Exception as e:
                                                    print(f'{message.author.name} fucked some shit {e}')
                                            
                                        else:
                                            await self.config.user(message.author).owner.set('yes')
                                            await message.author.add_roles(rolee)
                                            owned = tokens 
                                            if round(owned) == 0:
                                                pass
                                            elif round(owned) == 1:
                                                await message.author.add_roles(role1)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 2 and round(owned) <= 4:
                                                await message.author.add_roles(role2)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 5 and round(owned) <= 9:
                                                await message.author.add_roles(role3)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 10 and round(owned) <= 19:
                                                await message.author.add_roles(role4)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 20 and round(owned) <= 34:
                                                await message.author.add_roles(role5)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 35 and round(owned) <= 49:
                                                await message.author.add_roles(role6)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 50:
                                                await message.author.add_roles(role7)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role1)
                                            else:
                                                print("not sure y")
                                            
                                    else:
                                        newxROO = xROO 
                                        await self.config.user(message.author).staked.set('yes')
                                        await message.author.add_roles(rolee)
                                        owned = tokens + newxROO + newroo
                                        if round(owned) == 0:
                                            pass
                                        elif round(owned) == 1:
                                            await message.author.add_roles(role1)
                                            await message.author.remove_roles(role2)
                                            await message.author.remove_roles(role3)
                                            await message.author.remove_roles(role4)
                                            await message.author.remove_roles(role5)
                                            await message.author.remove_roles(role6)
                                            await message.author.remove_roles(role7)
                                        elif round(owned) >= 2 and round(owned) <= 4:
                                            await message.author.add_roles(role2)
                                            await message.author.remove_roles(role1)
                                            await message.author.remove_roles(role3)
                                            await message.author.remove_roles(role4)
                                            await message.author.remove_roles(role5)
                                            await message.author.remove_roles(role6)
                                            await message.author.remove_roles(role7)
                                        elif round(owned) >= 5 and round(owned) <= 9:
                                            await message.author.add_roles(role3)
                                            await message.author.remove_roles(role2)
                                            await message.author.remove_roles(role1)
                                            await message.author.remove_roles(role4)
                                            await message.author.remove_roles(role5)
                                            await message.author.remove_roles(role6)
                                            await message.author.remove_roles(role7)
                                        elif round(owned) >= 10 and round(owned) <= 19:
                                            await message.author.add_roles(role4)
                                            await message.author.remove_roles(role2)
                                            await message.author.remove_roles(role3)
                                            await message.author.remove_roles(role1)
                                            await message.author.remove_roles(role5)
                                            await message.author.remove_roles(role6)
                                            await message.author.remove_roles(role7)
                                        elif round(owned) >= 20 and round(owned) <= 34:
                                            await message.author.add_roles(role5)
                                            await message.author.remove_roles(role2)
                                            await message.author.remove_roles(role3)
                                            await message.author.remove_roles(role4)
                                            await message.author.remove_roles(role1)
                                            await message.author.remove_roles(role6)
                                            await message.author.remove_roles(role7)
                                        elif round(owned) >= 35 and round(owned) <= 49:
                                            await message.author.add_roles(role6)
                                            await message.author.remove_roles(role2)
                                            await message.author.remove_roles(role3)
                                            await message.author.remove_roles(role4)
                                            await message.author.remove_roles(role5)
                                            await message.author.remove_roles(role1)
                                            await message.author.remove_roles(role7)
                                        elif round(owned) >= 50:
                                            await message.author.add_roles(role7)
                                            await message.author.remove_roles(role2)
                                            await message.author.remove_roles(role3)
                                            await message.author.remove_roles(role4)
                                            await message.author.remove_roles(role5)
                                            await message.author.remove_roles(role6)
                                            await message.author.remove_roles(role1)
                                        else:
                                            print("not sure y")    
                                        return                                            
                                        
                                else:
                                    newroo = roo
                                    if newroo > 0.7:
                                        await self.config.user(message.author).staked.set('yes')
                                        
                                        if tokens == 0:
                                            await self.config.user(message.author).owner.set('no')
                                            await message.author.add_roles(rolee)
                                            owned = tokens + newxROO + newroo
                                            if round(owned) == 0:
                                                pass
                                            elif round(owned) == 1:
                                                await message.author.add_roles(role1)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 2 and round(owned) <= 4:
                                                await message.author.add_roles(role2)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 5 and round(owned) <= 9:
                                                await message.author.add_roles(role3)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 10 and round(owned) <= 19:
                                                await message.author.add_roles(role4)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 20 and round(owned) <= 34:
                                                await message.author.add_roles(role5)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 35 and round(owned) <= 49:
                                                await message.author.add_roles(role6)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 50:
                                                await message.author.add_roles(role7)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role1)
                                            else:
                                                print("not sure y")
                                        else:
                                            await self.config.user(message.author).owner.set('yes')
                                            nnewxrooweth = newxrooweth * 3
                                            owned = tokens + newxROO + newroo + nnewxrooweth
                                            await message.author.add_roles(rolee)
                                            if round(owned) == 0:
                                                pass
                                            elif round(owned) == 1:
                                                await message.author.add_roles(role1)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 2 and round(owned) <= 4:
                                                await message.author.add_roles(role2)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 5 and round(owned) <= 9:
                                                await message.author.add_roles(role3)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 10 and round(owned) <= 19:
                                                await message.author.add_roles(role4)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 20 and round(owned) <= 34:
                                                await message.author.add_roles(role5)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 35 and round(owned) <= 49:
                                                await message.author.add_roles(role6)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 50:
                                                await message.author.add_roles(role7)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role1)
                                            else:
                                                print("not sure y")
                                            
                                            
                                            
                                            
                                    else:
                                        await self.config.user(message.author).staked.set('no')
                                        if tokens == 0:
                                            if xROO > 0.5:
                                                newxROO = xROO 
                                                await self.config.user(message.author).staked.set('yes')
                                                owned = tokens + newxROO + newroo
                                                await message.author.add_roles(rolee)
                                                if round(owned) == 0:
                                                    pass
                                                elif round(owned) == 1:
                                                    await message.author.add_roles(role1)
                                                    await message.author.remove_roles(role2)
                                                    await message.author.remove_roles(role3)
                                                    await message.author.remove_roles(role4)
                                                    await message.author.remove_roles(role5)
                                                    await message.author.remove_roles(role6)
                                                    await message.author.remove_roles(role7)
                                                elif round(owned) >= 2 and round(owned) <= 4:
                                                    await message.author.add_roles(role2)
                                                    await message.author.remove_roles(role1)
                                                    await message.author.remove_roles(role3)
                                                    await message.author.remove_roles(role4)
                                                    await message.author.remove_roles(role5)
                                                    await message.author.remove_roles(role6)
                                                    await message.author.remove_roles(role7)
                                                elif round(owned) >= 5 and round(owned) <= 9:
                                                    await message.author.add_roles(role3)
                                                    await message.author.remove_roles(role2)
                                                    await message.author.remove_roles(role1)
                                                    await message.author.remove_roles(role4)
                                                    await message.author.remove_roles(role5)
                                                    await message.author.remove_roles(role6)
                                                    await message.author.remove_roles(role7)
                                                elif round(owned) >= 10 and round(owned) <= 19:
                                                    await message.author.add_roles(role4)
                                                    await message.author.remove_roles(role2)
                                                    await message.author.remove_roles(role3)
                                                    await message.author.remove_roles(role1)
                                                    await message.author.remove_roles(role5)
                                                    await message.author.remove_roles(role6)
                                                    await message.author.remove_roles(role7)
                                                elif round(owned) >= 20 and round(owned) <= 34:
                                                    await message.author.add_roles(role5)
                                                    await message.author.remove_roles(role2)
                                                    await message.author.remove_roles(role3)
                                                    await message.author.remove_roles(role4)
                                                    await message.author.remove_roles(role1)
                                                    await message.author.remove_roles(role6)
                                                    await message.author.remove_roles(role7)
                                                elif round(owned) >= 35 and round(owned) <= 49:
                                                    await message.author.add_roles(role6)
                                                    await message.author.remove_roles(role2)
                                                    await message.author.remove_roles(role3)
                                                    await message.author.remove_roles(role4)
                                                    await message.author.remove_roles(role5)
                                                    await message.author.remove_roles(role1)
                                                    await message.author.remove_roles(role7)
                                                elif round(owned) >= 50:
                                                    await message.author.add_roles(role7)
                                                    await message.author.remove_roles(role2)
                                                    await message.author.remove_roles(role3)
                                                    await message.author.remove_roles(role4)
                                                    await message.author.remove_roles(role5)
                                                    await message.author.remove_roles(role6)
                                                    await message.author.remove_roles(role1)
                                                else:
                                                    print("not sure y")
                                                
                                                
                                            else:
                                                if newxrooweth > 0.01:
                                                    await self.config.user(message.author).staked.set('yes')
                                                
                                                else:
                                                
                                                    await chann.send(f"<@195375142061211648> {message.author.mention} shouldnt have role.")
                                                    await message.author.remove_roles(role1)
                                                    await message.author.remove_roles(role)
                                                    await message.author.remove_roles(role2)
                                                    await message.author.remove_roles(role3)
                                                    await message.author.remove_roles(role4)
                                                    await message.author.remove_roles(role5)
                                                    await message.author.remove_roles(role6)
                                                    await message.author.remove_roles(role7)
                                                   # await message.author.remove_roles([role, role1, role2, role3, role4, role5, role6, role7])
                                                    print(f'removed role from {message.author.name} no owner, no stake')
                                            
                                        else:
                                            await self.config.user(message.author).owner.set('yes')
                                            owned = tokens + newxROO + newroo
                                            await message.author.add_roles(rolee)
                                            if round(owned) == 0:
                                                pass
                                            elif round(owned) == 1:
                                                await message.author.add_roles(role1)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 2 and round(owned) <= 4:
                                                await message.author.add_roles(role2)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 5 and round(owned) <= 9:
                                                await message.author.add_roles(role3)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 10 and round(owned) <= 19:
                                                await message.author.add_roles(role4)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 20 and round(owned) <= 34:
                                                await message.author.add_roles(role5)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 35 and round(owned) <= 49:
                                                await message.author.add_roles(role6)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role1)
                                                await message.author.remove_roles(role7)
                                            elif round(owned) >= 50:
                                                await message.author.add_roles(role7)
                                                await message.author.remove_roles(role2)
                                                await message.author.remove_roles(role3)
                                                await message.author.remove_roles(role4)
                                                await message.author.remove_roles(role5)
                                                await message.author.remove_roles(role6)
                                                await message.author.remove_roles(role1)
                                            else:
                                                print("not sure y")
                                            
                       
                    except Exception as e:
                      #  print(e)
                      #  print(message.author.name)
                        return
                else:
                    pass
            except Exception as e:
              #  print(e)
               # print(message.author.name)
                return
    
    
    
    
    
    
    
    
    
    
    @app_commands.command(name="verifyroo", description="Verify Roo",) 
    @app_commands.guilds(discord.Object(id=893963935672324118))
    async def slash_verify(
        self,
        interaction: discord.Interaction,
    ):    
        curtime = int(time.time())
        exptime = curtime + 3600
        payload_data = {
            "ID": str(interaction.user.id),
            "exp": exptime
            }
            
        token = jwt.encode(
            payload=payload_data,
            key='-KaPdSgVkYp2s5v8y/B?E(H+MbQeThWmZq4t6w9z$C&F)J@NcRfUjXn2r5u8x!A%',
            algorithm='HS512'
            )
        url = "https://verify.rootroop.com?token=" + token
        
        await interaction.response.send_message(url, ephemeral=True)
        
        
    @app_commands.command(name="sync", description="Sync Ownership Status",) 
    @app_commands.guilds(discord.Object(id=893963935672324118))   
    async def slash_sync(self, interaction: discord.Interaction,):
        is_staked = await self.config.member(interaction.user).staked()
        r = requests.get(url =  f"https://api.rootroop.com/verify.php?discordId={interaction.user.id}")
        try:
            data = r.json()
        except Exception as e:
            await interaction.response.send_message("You are not verified. Please type /verify", ephemeral=True)
            return
        roo = data['ROO']
        tokens = data['RooTroopNFT']
        xrooweth = data['xRooWETH']
        newxrooweth = xrooweth 
        xROO = data['xROO']
        newxROO = xROO
        role = interaction.guild.get_role(894357379326558268)
        owned = tokens
        if roo == 0:
            if newxROO < 0.01:
                await self.config.user(interaction.user).staked.set('no')
                if tokens == 0:
                    await self.config.user(interaction.user).owner.set('no')
                 #   if rweh == 0:
                 #       await self.config.user(ctx.author).rweth.set('no')
                 #   else:
                 #       rweth = rweh / 10^18
                 #       if rweth > 0.3:
                    if newxrooweth > 0.01:
                        await self.config.user(interaction.user).staked.set('yes')
                        await interaction.response.send_message("Verified.", ephemeral=True)
                        await interaction.user.add_roles(role)
                    else:
                        await interaction.response.send_message('You are not staked and own no Roo Troop NFTS.', ephemeral=True)
                        return
                else:
                    await self.config.user(interaction.user).owner.set('yes')
                    await interaction.response.send_message("Verified.", ephemeral=True)
                    await interaction.user.add_roles(role)
                    return
            else:
                
                await self.config.user(interaction.user).staked.set('yes')
                await interaction.response.send_message("Verified.", ephemeral=True)
                await interaction.user.add_roles(role)
        else:          
            newroo = roo
            if newroo > 0.7:
                await self.config.user(interaction.user).staked.set('yes')
                await interaction.user.add_roles(role)
                if tokens == 0:
                    await interaction.response.send_message("Verified.", ephemeral=True)
                    return
                else:
                    await self.config.user(interaction.user).owner.set('yes')
                    await interaction.response.send_message("Verified.", ephemeral=True)
                    return
            else:
                await self.config.user(interaction.user).staked.set('no')
                
                if tokens == 0:
                    if newxROO > 0.5:
                        
                        await self.config.user(interaction.user).staked.set('yes')
                        await interaction.response.send_message("Verified.", ephemeral=True)
                        await interaction.user.add_roles(role)
                    else:
                        if newxrooweth > 0.01:
                            await self.config.user(interaction.user).staked.set('yes')
                            await interaction.response.send_message("Verified.", ephemeral=True)
                            await interaction.user.add_roles(role)
                        else:
                           
                            await interaction.response.send_message('You are not staked and own no Roo Troop NFTS.', ephemeral=True)
                            return
                else:
                    await self.config.user(interaction.user).owner.set('yes')
                    await interaction.response.send_message("Verified.", ephemeral=True)
                    return
                return
                
                