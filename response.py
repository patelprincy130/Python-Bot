import random
import discord
import requests
import json


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return 'This is a help message that you can modify.'

    if p_message.startswith('!category'):
        import requests

        category = p_message[10:]
        api_url = 'https://api.api-ninjas.com/v1/hobbies?category={}&hobby'.format(category)
        response = requests.get(api_url + category, headers={'X-Api-Key': 'Snk9iGvtZCyim0CNGMkiZg==8VNs7apyzGXKGmPb'})
        if response.status_code == requests.codes.ok:
            data = response.json()
            return json.dumps(data, indent=2)
        return f'No data found for category: {category}'

    return 'I didn\'t understand what you wrote. Try typing "!help".'
