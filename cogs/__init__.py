from discord import AllowedMentions, Bot
from supabase import Client, create_client

from config import SUPABASE_URL, SUPABASE_KEY

bot = Bot(allowed_mentions=AllowedMentions(everyone=True))
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
