from asyncio.log import logger

from cogs import bot
from cogs.solana import Solana
from config import DISCORD_BOT_TOKEN


@bot.event
async def on_ready() -> None:
    """Initial setup for discord bot"""
    logger.info(f"{bot.user} successfully logged in!")


if __name__ == "__main__":
    bot.add_cog(Solana(bot))
    bot.run(DISCORD_BOT_TOKEN)
