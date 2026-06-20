from dotenv import load_dotenv

from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, cli
from livekit.plugins import google, deepgram, cartesia, silero

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
        llm=google.LLM(model="gemini-2.5-flash"),
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