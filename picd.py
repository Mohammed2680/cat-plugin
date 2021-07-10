from userbot.utils import *
import asyncio
@bot.on(admin_cmd(pattern="pd"))
async def ppd(event):
  ab = await event.get_reply_message()
  if not ab:
    await event.edit("`Reply any message`")
    return
  b = await bot.download_profile_photo(ab.sender_id)
  if not b:
    await event.edit("`This user has no any profile pic`")
    return
  await event.edit("`Sending profile pic`")
  await asyncio.sleep(2)
  await event.reply(file=b)