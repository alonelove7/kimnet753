import os

class Config:
    API_ID = int( os.getenv("api_id","12158050") )
    API_HASH = os.getenv("api_hash","e7e2e7f23c51a465f62067d8644f34ae")
    CHANNEL = int( os.getenv("channel_files_chat_id","-1001526486348") )
    CHANNEL_USERNAME = os.getenv("channel_username","King_network7")
    TOKEN = os.getenv("token","2045343811:AAFK6hL7f1YmjXNcQJSFxZmOmnVYPgwuHaI")
    DOMAIN  = os.getenv("domain","https://d4.kimo.vip")
