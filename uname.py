from .. import *
@catub.cat_cmd(pattern="uname")
async def hi(event):
  reply = await event.get_reply_message()
  if not reply:
    await event.edit("𝗥𝗲𝗽𝗹𝘆 𝗮𝗻𝘆 𝘂𝘀𝗲𝗿 𝘁𝗼 𝗴𝗲𝘁 𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲.")
    return
  a = reply.sender.username
  b = "@"
  await event.respond(b+a)