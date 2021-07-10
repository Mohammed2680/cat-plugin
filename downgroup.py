from .. import *
from telethon import types
@catub.cat_cmd(pattern="dgp ?(.*)")
async def hi(event):
  a = event.pattern_match.group(1)
  for m in await bot.get_messages(a,
  filter=types.InputMessagesFilterDocument(), 
  limit=4300,
  ):
    await event.edit("`Downloading… `")
    await m.download_media()

