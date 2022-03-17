import json

from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


keyboard = {
    "one_time": True,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": {"button": "1"},
                "label": "Бот 123🤖"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": {"button": "2"},
                "label": "Развлечения 🎉"
            },
            "color": "negative"
        }]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 211793314)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            text = event.obj.message['text']
            print('Текст:', text)
            vk = vk_session.get_api()
            if "стикер" in text.lower():
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 random_id=random.randint(0, 2 ** 64),
                                 sticker_id=63
                                 )
            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Спасибо, что написали нам. Мы обязательно ответим",
                                 random_id=random.randint(0, 2 ** 64),
                                 keyboard=keyboard)
        if event.type == VkBotEventType.GROUP_JOIN:
            print(f'{event.obj.user_id} вступил в группу!')
        if event.type == VkBotEventType.MESSAGE_TYPING_STATE:
            print(f'Печатает {event.obj.from_id} для {event.obj.to_id}')


if __name__ == '__main__':
    main()