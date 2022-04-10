from typing import List

from discord import AutocompleteContext

from cogs import supabase


async def get_nft_suggestions(ctx: AutocompleteContext) -> List[str]:
    """
    Retrieve nft collection name suggestions.

    :param ctx: Discord AutoComplete Context
    :return: list of collection name suggestions
    """
    column = "symbol"
    pattern = f"{ctx.value.lower()}%"

    return [
        query_result[column]
        for query_result in supabase.table("nftcollection")
        .select(column)
        .like(column, pattern)
        .execute()
        .data
    ]
