from userbot.utils import *
import asyncio
@bot.on(admin_cmd(pattern="del"))
async def hi(event):
  ab = await event.get_reply_message()
  if not ab:
    await event.edit("`Reply your message`")
    return
  await ab.delete()
  await event.edit("`Successfully delete message`")
  await asyncio.sleep(2)
  await event.delete()
