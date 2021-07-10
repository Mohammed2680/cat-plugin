from telethon import *
@bot.on(events.NewMessage(pattern=""".ping️ ?(.*)"""))
async def hello(event):
  ab = event.pattern_match.group(1)
  await event.edit(f"""
Pong!
{ab} ms
""")