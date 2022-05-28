import requests
import json
import os

application_id = 'client id бота'
token_user = 'токен аккаунта на котором бот'

reset_token = requests.post(f'https://discord.com/api/v9/applications/{application_id}/bot/reset', headers={'Authorization': token_user,'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'})

os.environ["TOKEN"] = json.loads(reset_token.text)['token']
print(os.environ["TOKEN"])
