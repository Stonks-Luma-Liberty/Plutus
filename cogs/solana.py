from discord import ApplicationContext, Bot, Embed, option
from discord.commands import slash_command
from discord.ext import commands
from magicpyden import MagicEdenApi
from magicpyden.constants import LAMPORTS_PER_SOL

from cogs import supabase
from cogs.auto_complete import get_nft_suggestions
from config import logger, GUILD_IDS
from utils.colors import Color


class Solana(commands.Cog):
    def __init__(self, bot: Bot):
        """
        Pycord Cog instance for solana nft marketplaces.

        :param bot: Discord Bot instance
        """
        self.bot = bot

    @slash_command(guild_ids=GUILD_IDS)
    @option(
        "collection_name",
        description="Enter token symbol",
        autocomplete=get_nft_suggestions,
    )
    async def nft_stats(self, ctx: ApplicationContext, collection_name: str) -> None:
        """
        Retrieve nft stats of specified Solana NFT project.

        :param ctx: Discord application context
        :param collection_name: Solana NFT collection name
        """
        logger.info(f"Looking up floor price for {collection_name}")
        title = collection_name.replace("_", " ").title()
        embed_message = Embed(
            title=f"MagicEden Stats: {title}",
            colour=Color.screamin_green.value,
        )

        async with MagicEdenApi() as api:
            collection = await api.get_collection_stats(collection_name=collection_name)
            floor_price = collection.floor_price / LAMPORTS_PER_SOL
            volume_all = collection.volume_all / LAMPORTS_PER_SOL
            embed_message.add_field(
                name="Floor", value=f"{floor_price:,.2f} SOL", inline=False
            )
            embed_message.add_field(
                name="Listed", value=f"{collection.listed_count:,.2f}", inline=True
            )
            embed_message.add_field(
                name="Volume", value=f"{volume_all:,.2f} SOL", inline=True
            )
        await ctx.respond(embed=embed_message)

        symbol = collection.symbol
        collection_exists = (
            supabase.table("nftcollection")
            .select("symbol")
            .like(column="symbol", pattern=symbol)
            .execute()
            .data
        )

        if not collection_exists:
            supabase.table("nftcollection").insert(
                {"symbol": symbol, "marketplace": "MagicEden"}
            ).execute()
