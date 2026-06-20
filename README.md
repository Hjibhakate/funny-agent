# Funny Voice AI Agent

## Components Used

### LiveKit

* Manages the voice call and real-time communication.
* Connects all services together.

### Google Gemini

* Acts as the AI brain.
* Understands user input and generates responses.

### Deepgram

* Converts user voice into text.
* Speech-to-Text (STT).

### Cartesia

* Converts AI-generated text into voice.
* Text-to-Speech (TTS).

### Silero

* Detects when the user starts and stops speaking.
* Voice Activity Detection (VAD).

---

## Conversation Flow

```text
You Speak
    ↓
Deepgram (Speech → Text)
    ↓
Google Gemini (AI Thinking)
    ↓
Cartesia (Text → Voice)
    ↓
AI Speaks Back
```

### One-Line Summary

You speak → Deepgram hears → Gemini thinks → Cartesia speaks → LiveKit connects everything → Silero knows when it's your turn.

---

## Run the Agent

Start the voice agent using:

```bash
python agent.py console
```

For development mode:

```bash
python agent.py dev
```

---

## Environment Variables

```env
LIVEKIT_URL=your_livekit_url
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret

GOOGLE_API_KEY=your_gemini_api_key

DEEPGRAM_API_KEY=your_deepgram_api_key
CARTESIA_API_KEY=your_cartesia_api_key
```

---

## Features

* Real-time voice conversation
* AI-generated responses
* Funny and friendly personality
* Short responses (1–2 sentences)
* Joke generation
* Automatic speech detection
* Low-latency voice interaction
