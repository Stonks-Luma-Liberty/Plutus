from discord import ApplicationContext, Bot, Embed
from discord.commands import slash_command, Option
from discord.ext import commands
from magicpyden import MagicEdenApi

from config import logger, GUILD_IDS
from utils.colors import Color


class Solana(commands.Cog):
    def __init__(self, bot: Bot):
        """
        Pycord Cog instance for solana nft marketplaces.

        :param bot: Discord Bot instance
        """
        self.bot = bot
        self.lamports_per_sol = 1000000000

    @slash_command(guild_ids=GUILD_IDS)
    async def floor_price(
        self,
        ctx: ApplicationContext,
        collection_name: Option(str, "Enter token symbol"),  # type: ignore
    ) -> None:
        """
        Retrieve floor price of specified Solana NFT project.

        :param ctx: Discord application context
        :param collection_name: Solana NFT collection name
        """
        logger.info(f"Looking up floor price for {collection_name}")
        embed_message = Embed(
            title=f"Floor Price ({collection_name})", colour=Color.screamin_green.value
        )
        async with MagicEdenApi() as api:
            collection = await api.get_collection_stats(collection_name=collection_name)
            floor_price = collection.floor_price / self.lamports_per_sol
            embed_message.add_field(
                name="MagicEden",
                value=f"{floor_price} SOL",
            )

        await ctx.respond(embed=embed_message)
