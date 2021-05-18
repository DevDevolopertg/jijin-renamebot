import os
from sample_config import Config

class script(object):
    START_TEXT = """ 💞 Hello,

This is a Telegram Rename Beta ver.2!

<b> Please send me any Telegram file and reply to that file to Rename New Name.mkv

 👉  Do one By One . Otherwise you will get Permenent Ban 

  © @Amal_PM </b>
  
/help for more details.."""

    RENAME_403_ERR = "What Are You Doing? You are Banned"
    UPGRADE_TEXT = "<b>Contact @Amal_PM</b>"
    DOWNLOAD_START = "<b>Trying to Download..📥</b>"
    UPLOAD_START = "<b>Trying to Upload..📤</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**Thank you for Using Me > ©  @Amal_PM **"
    SAVED_THUMB = "**✅ Custom thumbnail saved. This image will be used in the file for 24Hr.**"
    DEL_THUMB = "<b>Thumbnail cleared succesfully!</b>"
    NO_THUMB = "<b>No thumbnails found!</b>"
    SAVED_RECVD_DOC_FILE = "**Document Downloaded Successfully.**"
    CUSTOM_CAPTION_UL_FILE = " "
    CAPTION = "**{}**\n\n" + str(Config.CAPTION)
    HELP_USER = """<b>It's not that complicated😅
    
1. Send me any Telegram File.
2. Choose appropriate option.</b>"""

