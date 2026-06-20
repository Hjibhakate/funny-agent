from dotenv import load_dotenv
from livekit.plugins import google
from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, cli
# from livekit.plugins import openai, deepgram, cartesia, silero
from livekit.plugins import google, deepgram, cartesia, silero

load_dotenv()

class FunnyFriend(Agent):
    def __init__(self):
        super().__init__(
            instructions="""
            You are a funny AI friend.
            Keep answers very short: 1-2 sentences only.
            Talk casually like a close friend.
            Crack small jokes sometimes.
            Ask simple follow-up questions.
            """
        )

async def entrypoint(ctx: JobContext):
    session = AgentSession(
        stt=deepgram.STT(),
        # llm=openai.LLM(model="gpt-4o-mini"),
        llm=google.LLM(model="gemini-2.5-flash"),
        tts=cartesia.TTS(),
        vad=silero.VAD.load(),
    )

    await session.start(
        room=ctx.room,
        agent=FunnyFriend()
    )

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))