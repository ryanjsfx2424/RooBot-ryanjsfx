"""Sticky - Sticky messages to a channel."""
from .serverage import serverage


def setup(bot):
    """Load Sticky."""
    bot.add_cog(serverage(bot))
