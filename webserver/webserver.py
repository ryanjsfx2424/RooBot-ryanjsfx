"""Module for the Webserver cog."""
from __future__ import annotations
import json
import asyncio
import ssl
from typing import Optional

from aiohttp import web
from redbot.core import commands, bank
from redbot.core.bot import Red
from redbot.core.config import Config





class Webserver(commands.Cog):
    """
    A cog for responding to pings form various uptime monitoring services,
    such as UptimeRobot, Pingdom, Uptime.com, or self-hosted ones like UptimeKuma or Upptime.
    The web server will run in the background whenever the cog is loaded on the specified port.
    It will respond with status code 200 when a request is made to the root URL.
    If you want to use this with an external service, you will need to set up port forwarding.
    Make sure you are aware of the security risk of exposing your machine to the internet.
    """

    __version__ = "1.0.0"
    __author__ = "Vexed#9000"

    def __init__(self, bot: Red) -> None:
        self.bot = bot
        self.config: Config = Config.get_conf(
            self, identifier=418078199982063626, force_registration=True
        )
        self.config.register_global(port=443)

    def cog_unload(self) -> None:
        self.bot.loop.create_task(self.shutdown_webserver())



    async def shutdown_webserver(self) -> None:
        await self.runner.shutdown()
        await self.runner.cleanup()
        print("Web server for UptimeResponder pings has been stopped due to cog unload.")


    async def main_page(self, request: web.Request) -> web.Response:
    
        #print('YO REQUEST')
        auth = request.headers.get('Authorization')
        if auth == "6w9z$C&F)J@NcRfUjXn2r5u7x!A%D*G-KaPdSgVkYp3s6v9y/B?E(H+MbQeThWmZq4t7w!z%C&F)J@NcRfUjXn2r5u8x/A?D(G-KaPdSgVkYp3s6v9y$B&E)H@MbQeTh":
            
            data = await request.json()
            user = data['user']
            guild = self.bot.get_guild(893963935672324118)
            member = guild.get_member(int(user))
            amt = data['amt']
            bal = await bank.get_balance(member)
            newbal = bal + int(amt)
            if newbal > 0:
                if int(amt) > 0:
                    await bank.deposit_credits(member, int(amt))
                    print(f"added {amt} to {member.name}")
                    return web.Response(
                        text='{"newbal": ' + str(newbal) + '}', status=200
                    )
                else:
                    await bank.withdraw_credits(member, abs(int(amt)))
                    print(f"withdrew {abs(int(amt))} from {member.name}")
                    return web.Response(
                        text='{"newbal": ' + str(newbal) + '}', status=200
                    )
            else:
                return web.Response(text='{"error": "NEGBAL"}', status=469)
        else:
            return web.Response(status=401)

    async def start_webserver(self, port: int | None = None) -> None:
        await asyncio.sleep(1)  # let previous server shut down if cog was reloaded

        port = port or await self.config.port()

        app = web.Application()
        app.add_routes([web.patch("/balance", self.main_page)])
        runner = web.AppRunner(app)
        await runner.setup()
        ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        ssl_context.load_cert_chain(r"C:\Users\Administrator\Desktop\Redbot\cogs\Webserver\domain_srv.crt", r"C:\Users\Administrator\Desktop\Redbot\cogs\Webserver\domain_srv.key")
        site = web.TCPSite(runner, port=port, ssl_context=ssl_context)
        await site.start()
        self.runner = runner
