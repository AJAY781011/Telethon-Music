import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6025896713:AAG4HsKECe2DTUgawQnnhvk_q8_9iRDnRnU)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOHABuzs9HQojyqBq3BDbzesxG3x49NWCpRLQigQZjBfDcBqDkFpWxB7EGM19LS3u8tC20cCQJmLxqHxend55qjm9aHVxL3JQqGvhuSxvmvj0IN2qrdA34rrJjeGKs3uPIVmUkoQJfgQymw1EPfah1iwGiEJTsLKEYZnsCMtHfFl7qkMB4Ctp0Tk9OmUXoe2go_lVKe3ykvANv3MYOZ9Mt9Cv0VJyjR7QQbl18Yii_j0TL_f7i4pgwpviC79rU3ut5lqGCvcgsENgnVfY1xztHgkDvYOoH1JMtS72wXWSkaXDCmomcgfToHowXO18PbeMjSaxyaK5DZA6Ye0Df3R25se0D6c=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
