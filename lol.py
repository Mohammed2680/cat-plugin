from telethon import *
@bot.on(events.NewMessage(outgoing=True, incoming=True, pattern=".lol"))
async def hi(event):
  ab = await event.get_reply_message()
  await ab.reply("""
😂😂😂😂😂😂🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣😂😂😂😂😂🤣🤣🤣😂😂😂🤣🤣🤣🤣🤣😂😂😂😂😂🤣🤣🤣😂😂😂🤣🤣🤣🤣🤣😂😂😂😂😂🤣🤣🤣😂😂😂🤣🤣🤣🤣🤣😂😂😂😂😂🤣🤣🤣😂😂😂🤣🤣🤣🤣🤣😂😂😂😂😂🤣🤣🤣😂😂😂🤣🤣🤣🤣🤣😂😂😂😂😂🤣🤣🤣😂😂😂🤣🤣🤣🤣🤣😂😂😂😂😂🤣🤣🤣😂😂😂🤣🤣🤣🤣🤣🤣🤣🤣😂😂😂🤣🤣🤣""")