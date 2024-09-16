from pyrogram.types import InlineKeyboardButton
import config
from AviaxMusic import app
from pyrogram.errors import PeerIdInvalid

# Start Panel Function
def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons

# Private Panel Function with Error Handling
def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_5"], callback_data="owner_callback"),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons

# Resolving Peer safely
async def resolve_user(client, user_id):
    try:
        user = await client.resolve_peer(user_id)
        return user
    except PeerIdInvalid:
        print(f"Peer ID invalid for user_id: {user_id}")
        return None  # Handle invalid peer ID gracefully