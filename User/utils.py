import requests
from django.conf import settings

def send_to_telegram(contact):
    message = f"""
📩 Yangi API request:\n
🆔 ID: {contact.id}
-------------------
👤 Ism: {contact.name}
-------------------
📧 Email: {contact.email}
-------------------
📱 Phone: {contact.phone}
-------------------
💡 Fikr: {contact.project_opinion}
"""
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url,data={"chat_id": settings.TELEGRAM_CHAT_ID,"text": message})