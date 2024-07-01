import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23066708"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "cdf964453a574b4c71131196f25ca9ca")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://siddhantgaba2003:zpjal2PjED4jKddf@cluster0sid1.ctawkpf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0Sid1")
