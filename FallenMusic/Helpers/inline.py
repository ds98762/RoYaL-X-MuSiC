# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="✯ ᴄʟᴏsᴇ ✯", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
        InlineKeyboardButton(
            text="➕ 𝙰𝙳𝙳 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ],
        [
      InlineKeyboardButton(text="🖤 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 🖤", url=f"https://t.me/Night_club_chatting"),
      InlineKeyboardButton(text="🥀 OWNER 🥵", url=f"https://t.me/ll_Her_Boy_ll")
    ],
  ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="✯ 𝐀𝐝𝐝 𝐌𝐞 𝐌𝐨𝐢 𝐋𝐮𝐯 ✯",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="🩸𝙷𝙴𝙻𝙿 𝙰𝙽𝙳 𝙲𝙼𝙳𝚂🩸", callback_data="fallen_help")],
    [
      InlineKeyboardButton(text="🐣 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 🐣", url=f"https://t.me/Night_club_chatting"),
      InlineKeyboardButton(text="🍷 OWNER 🌸", url=f"https://t.me/ll_Her_Boy_ll")
    ],
    [
        InlineKeyboardButton(
            text="🌱 𝚁𝙴𝙿𝙾 🌱", url="https://telegra.ph/file/0fc760cb0777ea04b7dfe.jpg"
        ),
        InlineKeyboardButton(text="🥀𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁🥀", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="⚡ 𝙰𝙳𝙳 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 🌏",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
      InlineKeyboardButton(text="🐣 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 🐣", url=f"https://t.me/Night_club_chatting"),
      InlineKeyboardButton(text="🍷 OWNER 🌸", url=f"https://t.me/ll_Her_Boy_ll")
    ],
    [
        InlineKeyboardButton(
            text="🌱 𝚁𝙴𝙿𝙾 🌱", url="https://telegra.ph/file/0fc760cb0777ea04b7dfe.jpg"
        ),
        InlineKeyboardButton(text="🥀 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 🥀", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="🚩 𝙰𝙳𝙳 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 🎀",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(
            text="❣️ᴇᴠᴇʀʏᴏɴᴇ❣️",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="🥀sᴜᴅᴏ🥀", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="🍁ᴏᴡɴᴇʀ🍁", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="✯ ʙᴀᴄᴋ ✯", callback_data="fallen_home"),
        InlineKeyboardButton(text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"),
    ],
]


help_back = [
    [
        InlineKeyboardButton(
            text="🔥 𝙰𝙳𝙳 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 🥂",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="🖤 𝙶𝚁𝙾𝚄𝙿 🖤", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="✯ ʙᴀᴄᴋ ✯", callback_data="Ronny_support_chats"),
        InlineKeyboardButton(text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"),
    ],
]
