from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from .. import catub
@catub.cat_cmd(pattern="ara ?(.*)")
async def adr(event):
  rank = event.pattern_match.group(1)
  r = ChatAdminRights(add_admins=True, invite_users=True, change_info=True)
  await event.client(EditAdminRequest(event.chat_id, reply.sender_id, r ,rank))