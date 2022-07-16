from .ticket import Ticket


async def setup(bot):
    await bot.add_cog(Ticket(bot))
