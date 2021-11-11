from telethon import events
@bot.on(events.NewMessage(outgoing= True,incoming=True))
async def hi(event):
 text = event.text
 await event.edit(f"{text}")
 await event.reply(str(f""" {text} X 1 = {int(text)*1}
{text} X 2 = {int(text)*2}
{text} X 3 = {int(text)*3}
{text} X 4 = {int(text)*4}
{text} X 5 = {int(text)*5}
{text} X 6 = {int(text)*6}
{text} X 7 = {int(text)*7}
{text} X 8 = {int(text)*8}
{text} X 9 = {int(text)*9}
{text} X 10 = {int(text)*10}
"""))