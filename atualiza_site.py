import requests
import hashlib
import time
import json

bot_token = '5832118970:AAFTq6El2tZmc6qYCA4EGPTb1ReUMy9H3AE'
chat_id = '2144944879'
site = 'https://www.betonews.com.br/'

# Obtém o conteúdo do site
site_content = requests.get(site).content

# Cria um hash do conteúdo do site
site_hash = hashlib.md5(site_content).hexdigest()

while True:
    # Obtém o conteúdo do site novamente
    new_site_content = requests.get(site).content

    # Cria um novo hash do conteúdo do site
    new_site_hash = hashlib.md5(new_site_content).hexdigest()

    # Verifica se o hash do site foi alterado
    if new_site_hash != site_hash:
        # Envia uma mensagem via Telegram
        requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text=O site {site} foi atualizado.')

        # Atualiza o hash do site
        site_hash = new_site_hash

    # Aguarda 60 segundos antes de verificar novamente
    time.sleep(60)
