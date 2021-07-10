@bot.on(admin_cmd(pattern="ftag", outgoing= True, incoming=True))
async def hi(event):
  ab = await event.get_reply_message()
  if not ab:
    await event.edit("Please reply message")
    return
  await event.edit("Processing..")
  await asyncio.sleep(1)
  await ab.forward_to(event.chat_id)
  
 
from userbot.utils import admin_cmd
import asyncio
@bot.on(admin_cmd(pattern="rtag", outgoing= True, incoming=True))
async def hi(event):
  a = await event.get_reply_message()
  b = a.media
  await bot.send_message(event.chat_id, file=b)