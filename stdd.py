import asyncio
import random, re
import datetime
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telegraph import Telegraph
from telethon import events
#from ub.events import *
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP
from .. import *
from userbot.utils import admin_cmd
#from var import Var
telegraph = Telegraph()
mee = telegraph.create_account(short_name="yohohehe")

@catub.cat_cmd(pattern="std ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Reply to any Sticker**")
        return
    reply_message = await event.get_reply_message()
    chat = "@Stickerdownloadbot"
    reply_message.sender
    await event.edit("**Making zip file...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=220255550)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please restart me (@Stickerdownloadbot) u Nigga```")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )
  

        

