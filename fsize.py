from userbot.utils import *
def humanbytes(size):
    """Input size in bytes,
    outputs in a human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"

@bot.on(admin_cmd(pattern="cs"))
async def hi(event):
  ab = await event.get_reply_message()
  if not ab:
    await event.edit("`Reply any file`")
    return
  b = ab.file.size
  a = humanbytes (b)
  await bot.send_message(event.chat_id,f"Your file size = {str(a)}")
