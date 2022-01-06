#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K & PR0FESS0R-99

import os
from config import Config
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", 12345))
API_HASH = os.environ.get("API_HASH", "")
CAPTION = os.environ.get("CAPTION", "@Mo_Tech_YT @Mo_Tech_Group")
BUTTON_TEXT = os.environ.get("BUTTON", "🔻Join Channel🔻")
URL_LINK = os.environ.get("LINK", "T.ME/MO_TECH_YT")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "")


CAPTION_TEXT=Config.CAPTION
BUTTON_TEXT=Config.BUTTON_TEXT
URL_LINK=Config.URL_LINK


@Client.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    kopp, _ = get_file_id(message)
    await message.edit(f"<b>{kopp.file_name}</b>\n\n{CAPTION_TEXT}",
          reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(f"{BUTTON_TEXT}", url=f"{URL_LINK}")
              ]]
        ))

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker"
        ):
            obj = getattr(msg, message_type)
            if obj:
                return obj, obj.file_id
