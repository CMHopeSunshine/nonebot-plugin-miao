import contextlib
import random
from typing import Dict, Any

from nonebot.adapters import Bot

from .config import config


@Bot.on_calling_api
async def handle_miao(bot: Bot, api: str, data: Dict[str, Any]):
    with contextlib.suppress(Exception):
        if api not in ['send_msg', 'send_message']:
            return
        if len(data['message']) != 1 or data['message'][0].type != 'text':
            return
        count = 0
        word = random.choice(config.miao_words)
        text = str(data['message'][0].data['text'])
        while count < config.miao_count and random.random() < config.miao_probability:
            if config.miao_position == 'start':
                text = word + text
            elif config.miao_position == 'end':
                text += word
            elif config.miao_position == 'random':
                pos = random.randint(0, len(text))
                text = text[:pos] + word + text[pos:]
            count += 1
            data['message'] = text
