#(c) Adarsh-Goel
import os
import asyncio
from asyncio import TimeoutError
from Adarsh.bot import StreamBot
from Adarsh.utils.database import Database
from Adarsh.utils.human_readable import humanbytes
from Adarsh.vars import Var
from urllib.parse import quote_plus
from pyrogram import filters, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)


MY_PASS = os.environ.get("MY_PASS",None)
pass_dict = {}
pass_db = Database(Var.DATABASE_URL, "ag_passwords")


@StreamBot.on_message((filters.regex("ʟᴏɢɪɴ🔓") | filters.command("login")) , group=4)
async def login_handler(c: Client, m: Message):
    try:
        try:
            ag = await m.reply_text("<b>𝙾𝙺𝙰𝚈. 𝚈𝙾𝚄 𝚂𝙴𝙽𝙳 𝙼𝙴 𝚃𝙷𝙴 𝙿𝙰𝚂𝚂𝚆𝙾𝚁𝙳 𝙽𝙾𝚆…...\n\n𝙳𝙾𝙽'𝚃 𝙺𝙽𝙾𝚆 𝚃𝙷𝙴 𝙿𝙰𝚂𝚂𝚆𝙾𝚁𝙳????\n\n𝙶𝙾 𝚃𝙾 [𝚃𝙷𝙸𝚂 𝙶𝚁𝙾𝚄𝙿](tg://resolve?domain=MD_BOTZ_DISCUSS) 𝙰𝙽𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 \n💁‍♂ <code>Password</code> \n\n(𝙔𝙤𝙪 𝘾𝙖𝙣 𝙐𝙨𝙚 /cancel 𝘾𝙤𝙢𝙢𝙖𝙣𝙙 𝙏𝙤 𝘾𝙖𝙣𝙘𝙚𝙡 𝙏𝙝𝙚 𝙋𝙧𝙤𝙘𝙚𝙨𝙨)</b>\n\n━━━━━━━━━━━━━━━━\n\n<b>💪 ᑭOᗯᗴᖇᗴᗪ ᗷY [ᗰᗪ ᗷOTᘔ](tg://resolve?domain=MD_BOTZ)</b>")
            _text = await c.listen(m.chat.id, filters=filters.text, timeout=90)
            if _text.text:
                textp = _text.text
                if textp=="/cancel":
                   await ag.edit("ℙℝ𝕆ℂ𝔼𝕊𝕊 ℂ𝔸ℕℂ𝔼𝕃𝕃𝔼𝔻 𝕊𝕌ℂℂ𝔼𝕊𝕊𝔽𝕌𝕃𝕃𝕐 ✅")
                   return
            else:
                return
        except TimeoutError:
            await ag.edit("<b>𝗜 𝗖𝗔𝗡'𝗧 𝗪𝗔𝗜𝗧 𝗠𝗢𝗥𝗘 𝗙𝗢𝗥 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗😥, 𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡 💫</b>")
            return
        if textp == MY_PASS:
            await pass_db.add_user_pass(m.chat.id, textp)
            ag_text = "𝔾𝕆𝕆𝔻 👍 𝕋ℍ𝔼 ℙ𝔸𝕊𝕊𝕎𝕆ℝ𝔻 𝕐𝕆𝕌 𝕁𝕌𝕊𝕋 𝔼ℕ𝕋𝔼ℝ𝔼𝔻 𝕀𝕊 ℂ𝕆ℝℝ𝔼ℂ𝕋..! ✅"
        else:
            ag_text = "ℙ𝔸𝕊𝕊𝕎𝕆ℝ𝔻 𝕀𝕊 𝕎ℝ𝕆ℕ𝔾...❌\nℙ𝕃𝔼𝔸𝕊𝔼 𝕋ℝ𝕐 𝔸𝔾𝔸𝕀ℕ ♻️"
        await ag.edit(ag_text)
    except Exception as e:
        print(e)

@StreamBot.on_message((filters.private) & (filters.document | filters.video | filters.audio | filters.photo) , group=4)
async def private_receive_handler(c: Client, m: Message):
    if MY_PASS:
        check_pass = await pass_db.get_user_pass(m.chat.id)
        if check_pass== None:
            await m.reply_text("𝙵𝙸𝚁𝚂𝚃 𝙻𝙾𝙶𝙸𝙽 𝚃𝙾 𝚃𝙷𝙴 𝙱𝙾𝚃...\n𝙳𝙾𝙽'𝚃 𝙺𝙽𝙾𝚆 𝚃𝙷𝙴 𝙿𝙰𝚂𝚂𝚆𝙾𝚁𝙳????\n\n𝙶𝙾 𝚃𝙾 [𝚃𝙷𝙸𝚂 𝙶𝚁𝙾𝚄𝙿](tg://resolve?domain=MD_BOTZ_DISCUSS) 𝙰𝙽𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 \n💁‍♂ <code>Password</code> \n\n𝚄𝙽𝙻𝙾𝙲𝙺...𝚁𝙴𝙰𝙳 𝙱𝙴𝙻𝙾𝚆 👇 \n\n𝚂𝙴𝙽𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙵𝙸𝚁𝚂𝚃 /login.\n𝚃𝙷𝙴𝙽 𝙴𝙽𝚃𝙴𝚁 𝚃𝙷𝙴 𝙿𝙰𝚂𝚂𝚆𝙾𝚁𝙳...\n\n━━━━━━━━━━━━━━━━\n\n<b>💪 ᑭOᗯᗴᖇᗴᗪ ᗷY [ᗰᗪ ᗷOTᘔ](tg://resolve?domain=MD_BOTZ)</b>")
            return
        if check_pass != MY_PASS:
            await pass_db.delete_user(m.chat.id)
            return
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await c.send_message(
            Var.BIN_CHANNEL,
            f"<b>𝙽𝙴𝚆 𝚄𝚂𝙴𝚁 𝙹𝙾𝙸𝙽𝙴𝙳</b> : \n\n <b>𝙽𝙰𝙼𝙴</b> : [{m.from_user.first_name}](tg://user?id={m.from_user.id}) <b>𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝚈𝙾𝚄𝚁 𝙱𝙾𝚃 !!</b>"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=m.chat.id,
                    text="<b>ՏOᖇᖇY...! YOᑌ ᗩᖇᗴ ᗷᗩᑎᑎᗴᗪ TO ᑌՏᗴ ᗰᗴ/nᑕOᑎTᗩᑕT [ᗰᗩՏTᗴᖇ](tg://resolve?domain=MD_OWNER)</b>",
                    
                    disable_web_page_preview=True
                )
                return 
        except UserNotParticipant:
            await c.send_photo(
                chat_id=m.chat.id,
                photo="https://telegra.ph/file/f2980c0372b67cd2c1dc8.jpg",
                caption="<b>━━━━━━━━━━━━━━━\n😢 𝑆𝑂𝑅𝑅𝑌 𝐷𝑈𝐷𝐸 𝑌𝑂𝑈𝑅 𝑁𝑂𝑇 𝐽𝑂𝐼𝑁𝐸𝐷 𝑀𝑌 𝐶𝐻𝐴𝑁𝑁𝐸𝐿.\n\n𝑃𝐿𝐸𝐴𝑆𝐸 𝐽𝑂𝐼𝑁 𝑀𝑌 [🍭 ᑌᑭᗪᗩTᗴ ᑕᕼᗩᑎᑎᗴᒪ 🍭](tg://resolve?domain=MD_BOTZ)\n\n𝑇𝑂 𝑈𝑆𝐸 [ᗰᗪ ᖴIᒪᗴ TO ᒪIᑎK ᑭᖇO 💫](tg://resolve?domain=MD_FILE_TO_LINK_BOT) 𝐵𝑂𝑇 🙏\n━━━━━━━━━━━━━━━\n\n🍃 Bᴏᴛ Made Bʏ : @MD_OWNER</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🍭 ᑌᑭᗪᗩTᗴ ᑕᕼᗩᑎᑎᗴᒪ 🍭", url=f"tg://resolve?domain={Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception as e:
            await m.reply_text(e)
            await c.send_message(
                chat_id=m.chat.id,
                text="𝗦𝗢𝗠𝗘𝗧𝗛𝗜𝗡𝗚 𝗪𝗘𝗡𝗧 𝗪𝗥𝗢𝗡𝗚...! 𝗖𝗢𝗡𝗧𝗔𝗖𝗧 [𝗠𝗬 𝗕𝗢𝗦𝗦](tg://resolve?domain=MD_OWNER)",
                
                disable_web_page_preview=True)
            return
    try:

        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        
        online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
       
        
        

        msg_text ="""
<b><u>𝗬𝗼𝘂𝗿 𝗹𝗶𝗻𝗸 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱! 👍</u></b>

<b>𝙵𝙸𝙻𝙴 𝙽𝙰𝙼𝙴 📁 :</b> <code>{}</code>

<b>𝙵𝙸𝙻𝙴 𝚂𝙸𝚉𝙴 🗂 :</b> <code>{}</code>

<b><u>𝗖𝗼𝗽𝘆 𝘁𝗵𝗶𝘀 𝗹𝗶𝗻𝗸 👇</u></b>

━━━━━━━━━━━━━━━
<b>𝘿𝙊𝙒𝙉𝙇𝙊𝘼𝘿 𝙁𝙄𝙇𝙀 📥 :</b> <code>{}</code>

<b>𝙊𝙉𝙇𝙄𝙉𝙀 𝙒𝘼𝙏𝘾𝙃 👩‍💻  :</b> <code>{}</code>
━━━━━━━━━━━━━━━

<b>📝<b><u> 𝗡𝗢𝗧𝗘 </u></b>:\t<b>𝑳𝑰𝑵𝑲 𝑾𝑶𝑵'𝑻 𝑬𝑿𝑷𝑰𝑹𝑬 𝑻𝑰𝑳𝑳 𝑰 𝑫𝑬𝑳𝑬𝑻𝑬</b>\n\n<b>╔═════════════╗\n\t\t\t💪 ᑭOᗯᗴᖇᗴᗪ ᗷY [ᗰᗪ ᗷOTᘔ](tg://resolve?domain=MD_BOTZ)\n╚═════════════╝</b>"""

        await log_msg.reply_text(text=f"**<b>𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙱𝚈 :</b>** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**<b>𝚄𝚂𝙴𝚁 𝙸𝙳 :</b>** `{m.from_user.id}`\n**<b>𝚂𝚃𝚁𝙴𝙰𝙼 𝙻𝙸𝙽𝙺 :</b>** {stream_link}", disable_web_page_preview=True,  quote=True)
        await m.reply_photo(
            photo="https://telegra.ph/file/f2980c0372b67cd2c1dc8.jpg",
            caption=msg_text.format(get_name(log_msg), humanbytes(get_media_file_size(m)), online_link, stream_link),
            quote=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙊𝙉𝙇𝙄𝙉𝙀 𝙒𝘼𝙏𝘾𝙃 👩‍💻", url=stream_link), #Stream Link
                                                InlineKeyboardButton('𝘿𝙊𝙒𝙉𝙇𝙊𝘼𝘿 𝙁𝙄𝙇𝙀 📥', url=online_link)]]) #Download Link
        )
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(chat_id=Var.BIN_CHANNEL, text=f"𝙶𝙾𝚃 𝙵𝙻𝙾𝙾𝙳 𝚆𝙰𝙸𝚃 𝙾𝙵 {str(e.x)}𝚂 𝙵𝚁𝙾𝙼 [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**𝚄𝚂𝙴𝚁 𝙸𝙳 :** `{str(m.from_user.id)}`", disable_web_page_preview=True)


@StreamBot.on_message(filters.channel & ~filters.group & (filters.document | filters.video | filters.photo)  & ~filters.forwarded, group=-1)
async def channel_receive_handler(bot, broadcast):
    if MY_PASS:
        check_pass = await pass_db.get_user_pass(broadcast.chat.id)
        if check_pass == None:
            await broadcast.reply_text("𝙵𝙸𝚁𝚂𝚃 𝙻𝙾𝙶𝙸𝙽 𝚃𝙾 𝚃𝙷𝙴 𝙱𝙾𝚃...\n𝙳𝙾𝙽'𝚃 𝙺𝙽𝙾𝚆 𝚃𝙷𝙴 𝙿𝙰𝚂𝚂𝚆𝙾𝚁𝙳????\n\n𝙶𝙾 𝚃𝙾 [𝚃𝙷𝙸𝚂 𝙶𝚁𝙾𝚄𝙿](tg://resolve?domain=MD_BOTZ_DISCUSS) 𝙰𝙽𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 \n💁‍♂ <code>Password</code> \n\n𝚄𝙽𝙻𝙾𝙲𝙺...𝚁𝙴𝙰𝙳 𝙱𝙴𝙻𝙾𝚆 👇 \n\n𝚂𝙴𝙽𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙵𝙸𝚁𝚂𝚃 /login.\n𝚃𝙷𝙴𝙽 𝙴𝙽𝚃𝙴𝚁 𝚃𝙷𝙴 𝙿𝙰𝚂𝚂𝚆𝙾𝚁𝙳...!\n\n━━━━━━━━━━━━━━━━\n\n<b>💪 ᑭOᗯᗴᖇᗴᗪ ᗷY [ᗰᗪ ᗷOTᘔ](tg://resolve?domain=MD_BOTZ)</b>")
            return
        if check_pass != MY_PASS:
            await broadcast.reply_text("ℙ𝔸𝕊𝕊𝕎𝕆ℝ𝔻 𝕀𝕊 𝕎ℝ𝕆ℕ𝔾...❌\nℙ𝕃𝔼𝔸𝕊𝔼 𝕋ℝ𝕐 𝔸𝔾𝔸𝕀ℕ ♻️")
            await pass_db.delete_user(broadcast.chat.id)
            return
    if int(broadcast.chat.id) in Var.BANNED_CHANNELS:
        await bot.leave_chat(broadcast.chat.id)
        return
    try:
        log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}watch/{quote_plus(get_name(log_msg))}/{str(log_msg.id)}?hash={get_hash(log_msg)}"
        online_link = f"{Var.URL}{quote_plus(get_name(log_msg))}/{str(log_msg.id)}?hash={get_hash(log_msg)}"
        await log_msg.reply_text(
            text=f"**ᑕᕼᗩᑎᑎᗴᒪ ᑎᗩᗰᗴ:** `{broadcast.chat.title}`\n**ᑕᕼᗩᑎᑎᗴᒪ Iᗪ:** `{broadcast.chat.id}`\n**ᖇᗴᑫᑌᗴՏT ᑌᖇᒪ:** {stream_link}",
            quote=True,
            parse_mode="Markdown"
        )
        await bot.edit_message_reply_markup(
            chat_id=broadcast.chat.id,
            id=broadcast.id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("𝙊𝙉𝙇𝙄𝙉𝙀 𝙒𝘼𝙏𝘾𝙃 👩‍💻 ", url=stream_link),
                     InlineKeyboardButton('𝘿𝙊𝙒𝙉𝙇𝙊𝘼𝘿 𝙁𝙄𝙇𝙀 📥', url=online_link)] 
                ]
            )
        )
    except FloodWait as w:
        print(f"Sleeping for {str(w.x)}s")
        await asyncio.sleep(w.x)
        await bot.send_message(chat_id=Var.BIN_CHANNEL,
                             text=f"𝙶𝙾𝚃 𝙵𝙻𝙾𝙾𝙳 𝚆𝙰𝙸𝚃 𝙾𝙵 {str(w.x)}𝚂 𝙵𝚁𝙾𝙼 {broadcast.chat.title}\n\n**𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙸𝙳:** `{str(broadcast.chat.id)}`",
                             disable_web_page_preview=True)
    except Exception as e:
        await bot.send_message(chat_id=Var.BIN_CHANNEL, text=f"**#<b>𝗘𝗥𝗥𝗢𝗥_𝗧𝗥𝗔𝗖𝗘𝗕𝗔𝗖𝗞:</b>** `{e}`", disable_web_page_preview=True)
        print(f"𝗖𝗔𝗡𝗧 𝗘𝗗𝗜𝗧 𝗕𝗥𝗢𝗔𝗗𝗖𝗔𝗦𝗧 𝗠𝗘𝗦𝗦𝗔𝗚𝗘...!\n𝗘𝗘𝗥𝗢𝗥:  **𝖦𝖨𝖵𝖤 𝖬𝖤 𝖤𝖣𝖨𝖳 𝖯𝖤𝖱𝖬𝖨𝖲𝖲𝖨𝖮𝖭 𝖨𝖭 𝖴𝖯𝖣𝖠𝖳𝖤𝖲 𝖠𝖭𝖣 𝖡𝖨𝖭 𝖢𝖧𝖠𝖭𝖭𝖤𝖫{e}**")
