from .. import *
@catub.cat_cmd(pattern="phone")
async def phonee(event):
  a = "+"
  reply = await event.get_reply_message()
  if not reply:
    await event.edit("`Reply any user`")
    return
  b = await bot.get_entity(reply.sender_id)
  c = b.phone
  if not c:
    await event.edit("`This user phone number not found !!`")
    return
  d = c.replace(c, a+c)
  await bot.send_message(event.chat_id,f"Your phone number : {d}")

