from .. import catub
@catub.cat_cmd(pattern="dpic ?(.*) (.*)")
async def hello(event):
  a = event.pattern_match.group(1)
  b = event.pattern_match.group(2)
  if not b:
    await event.edit("Type : $dpic username anything")
    return
  if not a:
    await event.edit("Type : $dpic username anything")
    return
  for c in await bot.inline_query(a, b):
    await c.click(event.chat_id)




@catub.cat_cmd(pattern="click ?(.*)")
async def hell(event):
  a = event.pattern_match.group(1)
  ab = await event.get_reply_message()
  if not a:
    return
  b = a.strip().split(" ", 1)
  if not b[1]:
    return
  c = await bot.inline_query(b[0], b[1])
  await c[0].click(event.chat_id)