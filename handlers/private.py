from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# Star Müzik tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://images.app.goo.gl/MTLXTSDCA4MLHScP7",
                caption=(f"""● **Merhaba** {message.from_user.mention} \n\n● **Ben** {bot} !\n\n● **Sesli sohbetlerde müzik çalabilen botum . . !** \n\n● **Ban yetkisiz, Ses yönetim yetkisi verip Asistanı gruba ekleyin . . !**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉 Beni Gruba Ekle 🎉", url=f"https://t.me/Zezecikmusicbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 Komutlar" , callback_data= "herkes"
                    ),
                    InlineKeyboardButton(
                        "🇹🇷 Kanal", url="https://t.me/safkalbim"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧑🏻‍💻 ɢɪᴛʜᴜʙ ᴋᴀʏɴᴀᴋ ᴋᴏᴅᴜ 🧑🏻‍💻", url="https://github.com/MehmetAtes21/music"
                    )
                ]
                
           ]
        ),
    )



@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery)
    await query.edit_message_text(f"""<b>🇹🇷 Tüm Komutlar : \n\n» /vbul => Video indir . \n» /bul => Müzik indir . \n» /oynat => Müzik oynat . \n» /durdur => Müziği durdur . \n» /devam => Müziği sürdür . \n» /atla =>  Müziği atla . \n» /son => Müziği sonlandır . \n» /katil => Asistanı gruba davet etme . \n» /reload => Admin listesini güncelle . \n\n» /auth => Kullanıcının yönetici olmadığı halde komutları kullanmasına izin verir .  \n\n» /unauth => Kullanıcının yönetici olmadığı halde komutları kullanmasını engeller . </b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🇹🇷 Asistan", url="https://t.me/zezecikmusicasistan"
                     ),
                     InlineKeyboardButton(
                         "🧑🏻‍💻 Sahip", url="https://t.me/mizantropistsahip"
                     )
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbstart")
                 ] 
             ]
         )
         )



@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""● **Merhaba** {message.from_user.mention} \n\n● **Ben** {bot} !\n\n● **Sesli sohbetlerde müzik çalabilen botum . . !** \n\n● **Ban yetkisiz, Ses yönetim yetkisi verip Asistanı gruba ekleyin . . !**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉 Beni Gruba Ekle 🎉", url=f"https://t.me/zezecikmusicbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 Komutlar" , callback_data= "herkes"
                    ),
                    InlineKeyboardButton(
                        "🇹🇷 Kanal", url=f"https://t.me/safkalbim"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧑🏻‍💻 ɢɪᴛʜᴜʙ ᴋᴀʏɴᴀᴋ ᴋᴏᴅᴜ 🧑🏻‍💻", url="https://github.com/MehmetAtes21/music"
                    )
                ]
                
           ]
        ),
    )
