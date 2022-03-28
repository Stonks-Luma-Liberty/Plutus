from discord import ApplicationContext, Bot, Embed
from discord.commands import (
    slash_command, Option
)
from discord.ext import commands
from magicpyden import MagicEdenApi

from config import logger, GUILD_IDS


class Solana(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.lamports_per_sol = 1000000000

    @slash_command(guild_ids=GUILD_IDS)
    async def floor_price(self, ctx: ApplicationContext, collection_name: Option(str, "Enter token symbol")) -> None:
        """
        Retrieve floor price of specified Solana NFT project.

        :param ctx: Discord application context
        :param collection_name: Solana NFT collection name
        """
        logger.info(f"Looking up floor price for {collection_name}")
        embed_message = Embed(title=f"Floor Price ({collection_name})", colour=0x5dfe7b)
        async with MagicEdenApi() as api:
            collection = await api.get_collection_stats(collection_name=collection_name)
            embed_message.add_field(name="MagicEden", value=f"{collection.floor_price / self.lamports_per_sol} SOL")

        await ctx.respond(embed=embed_message)
