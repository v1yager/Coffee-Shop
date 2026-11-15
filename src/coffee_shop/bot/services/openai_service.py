from openai import AsyncOpenAI, OpenAI
from coffee_shop.bot.config import settings

from pathlib import Path

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

async def generate_response(message: str) -> str:
    prompt = SYSTEM_PROMPT.format(
        coffee_info=COFFEE_INFO
    )

    completion = await client.chat.completions.create(
        model="qwen/qwen3-4b-2507",
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": message,
            },
        ],
    )

    return completion.choices[0].message.content

