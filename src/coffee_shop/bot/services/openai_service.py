from openai import AsyncOpenAI, OpenAI
from coffee_shop.bot.config import settings

from pathlib import Path

from coffee_shop.bot.services.redis_service import add_message, get_history

BASE_DIR = Path(__file__).resolve().parent.parent

COFFEE_INFO = (
    BASE_DIR / "prompts" / "coffee_info.txt"
).read_text(encoding="utf-8")

SYSTEM_PROMPT = (
    BASE_DIR / "prompts" / "system_prompt.txt"
).read_text(encoding="utf-8")

client = AsyncOpenAI(
    api_key=settings.openai_api_key,
    base_url=settings.base_url
)

async def generate_response(user_id: int, message: str) -> str:
    history = await get_history(user_id)

    prompt = SYSTEM_PROMPT.format(
        coffee_info=COFFEE_INFO
    )

    completion = await client.chat.completions.create(
        model=settings.model_name,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            *history,
            {
                "role": "user",
                "content": message,
            },
        ],
    )

    answer = completion.choices[0].message.content or ""

    await add_message(user_id, "user", message)
    await add_message(user_id, "assistant", answer)

    return answer

