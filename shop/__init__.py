"""buy shiz"""
from .shop import Shop


async def setup(bot):
    """Load Shop."""
    await bot.add_cog(Shop(bot))
