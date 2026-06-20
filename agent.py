from dotenv import load_dotenv
import os

from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, cli
from livekit.plugins import openai, deepgram, cartesia, silero

from prompts import FUNNY_FRIEND_PROMPT

load_dotenv()


class FunnyFriend(Agent):
    def __init__(self):
        super().__init__(
            instructions=FUNNY_FRIEND_PROMPT
        )


async def entrypoint(ctx: JobContext):
    session = AgentSession(
        stt=deepgram.STT(),

        # OpenRouter AI Brain
        llm=openai.LLM(
            model="openai/gpt-4o-mini",
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
        ),

        tts=cartesia.TTS(),
        vad=silero.VAD.load(),
    )

    await session.start(
        room=ctx.room,
        agent=FunnyFriend()
    )


if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(entrypoint_fnc=entrypoint)
    )