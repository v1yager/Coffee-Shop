import json

import redis.asyncio as redis
from coffee_shop.bot.config import settings

redis_client = redis.Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    password=settings.redis_password,
    decode_responses=True,
    db=0
)

async def add_message(user_id: int, role: str, content: str) -> None:
    key = f"chat:{user_id}"

    message = {
        "role": role,
        "content": content
    }

    await redis_client.rpush(
        key,
        json.dumps(message, ensure_ascii=False)
    )

    await redis_client.ltrim(key, -6, 1)


async def get_history(user_id: int) -> list[dict[str, str]]:
    key = f"chat:{user_id}"

    messages = await redis_client.lrange(key, 0, -1)

    return [json.loads(message) for message in messages]
