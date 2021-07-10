from .. import catub
@catub.cat_cmd(pattern="test ?(.*) (.*)")
async def tedt(event):
  a = event.pattern_match.group(1)
  c = event.pattern_match.group(2)
  await event.edit(f"""
Ultroid Server Speed in 5 sec

Download: {a} TeraBytes
Upload: {c} Terabytes
Ping: 19.764
Internet Service Provider: Microsoft Corporation
ISP Rating: 3.7
""")