# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from pyrogram import Client as ren
from pyrogram import *
from pyrogram.types import *

@ren.on_message(filters.command("start") & filters.private)
async def start_bot(c: Client, m: Message):
    start_welcome = f"Hey What's Up! {m.from_user.mention}\n\nWelcome to GPT-3.5-turbo AI! Send me any message (via /ask command ) and I will use the Open A.I API to generate the response & solve the query for you.\n\nExample `/ask hello what's your version?`"
    start_button = InlineKeyboardMarkup([[InlineKeyboardButton("➕ADD ME to Ur Group➕", url=f"https://t.me/{c.me.username}?startgroup=True")]])
    start_button = InlineKeyboardMarkup([[InlineKeyboardButton("🔖Bot Lists🔖", url=f"https://t.me/mdisk_bots")
await m.reply_text(start_welcome, reply_markup=start_button)
