# Storing AI Voice Agent Transcripts in Upstash Redis

## Goal

Store both:

* User transcripts (what the user says)
* AI responses (what the AI replies)

inside Upstash Redis for conversation history and memory.

---

# Conversation Flow

```text
User Speaks
↓
Deepgram (Speech → Text)
↓
Store User Transcript → Upstash Redis
↓
Gemini/OpenAI (Generate Response)
↓
Store AI Response → Upstash Redis
↓
Cartesia/ElevenLabs (Speak Response)
```

---

# Step 1: Install Upstash Redis

```bash
pip install upstash-redis
```

---

# Step 2: Add Credentials to .env

```env
UPSTASH_REDIS_REST_URL=your_upstash_url
UPSTASH_REDIS_REST_TOKEN=your_upstash_token
```

---

# Step 3: Create Redis Client

Create a file named `redis_client.py`

```python
from upstash_redis import Redis
from dotenv import load_dotenv
import os

load_dotenv()

redis = Redis(
    url=os.getenv("UPSTASH_REDIS_REST_URL"),
    token=os.getenv("UPSTASH_REDIS_REST_TOKEN"),
)
```

---

# Step 4: Create Transcript Storage Helper

Create a file named `transcript_store.py`

```python
from redis_client import redis
from datetime import datetime

def save_message(role: str, text: str):
    redis.rpush(
        "conversation",
        {
            "role": role,
            "text": text,
            "timestamp": datetime.utcnow().isoformat()
        }
    )
```

---

# Step 5: Save User Messages

Whenever the user speaks:

```python
save_message("user", user_text)
```

---

# Step 6: Save AI Responses

Whenever the AI responds:

```python
save_message("assistant", ai_response)
```

---

# Better Approach: Store Data by Room

Instead of one global conversation key, use room-specific keys.

```python
key = f"conversation:{room_name}"
```

Example:

```python
redis.rpush(
    f"conversation:{room_name}",
    {
        "role": "user",
        "text": user_text
    }
)
```

Benefits:

* Supports multiple users
* Supports multiple rooms
* Easier transcript retrieval

---

# Example Stored Data

```json
[
  {
    "role": "user",
    "text": "Hello"
  },
  {
    "role": "assistant",
    "text": "Hey! How's your day going?"
  },
  {
    "role": "user",
    "text": "I'm good"
  }
]
```

---

# Best Practice: Store Complete Conversation Turns

Instead of saving messages separately, save a full interaction.

```python
conversation = {
    "user": user_text,
    "assistant": ai_text,
    "timestamp": datetime.utcnow().isoformat()
}

redis.rpush(
    f"conversation:{room_name}",
    conversation
)
```

Benefits:

* Easier analytics
* Easier reporting
* Cleaner conversation history

---

# Recommended Production Architecture

* LiveKit → Voice orchestration
* Deepgram → Speech-to-Text (STT)
* Gemini/OpenAI → LLM (AI Brain)
* Cartesia/ElevenLabs → Text-to-Speech (TTS)
* Upstash Redis → Session memory and transcripts
* PostgreSQL/MongoDB → Long-term storage and analytics

---

# One-Line Summary

Use Upstash Redis to store user transcripts and AI responses in real time, enabling conversation history, session memory, analytics, and future retrieval.
