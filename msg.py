from .. import *
import asyncio
@catub.cat_cmd(pattern="msg")
async def hi(event):
  a = await event.get_reply_message()
  b = a.text
  await bot.send_message(event.chat_id,f"`{b}`")
  await asyncio.sleep(3)
  await event.delete()


