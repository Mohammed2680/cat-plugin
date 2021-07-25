from .. import *
@catub.cat_cmd(pattern="fname")
async def hi(event):
  reply = await event.get_reply_message()
  if not reply:
    await event.edit("𝗥𝗲𝗽𝗹𝘆 𝗮𝗻𝘆 𝘂𝘀𝗲𝗿 𝘁𝗼 𝗴𝗲𝘁 𝗳𝗶𝗿𝘀𝘁 𝗻𝗮𝗺𝗲.")
    return
  a = await bot.get_entity(reply.sender_id)
  b = a.first_name
  await event.respond(b)