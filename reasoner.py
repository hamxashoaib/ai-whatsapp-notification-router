import json

from config import client, MODEL_NAME


def ask_gemini(prompt):
    """
    Sends prompt to Gemini.
    If Gemini fails (quota/rate limit/etc.), immediately
    returns a fallback prediction so the pipeline never stops.
    """

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        text = response.text.strip()

        # Remove markdown formatting if Gemini returns it
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        return json.loads(text)

    except Exception as e:

        print("\nGemini Error:")
        print(e)
        print("\nUsing fallback prediction...\n")

        # Immediate fallback (no waiting, no retries)
        return {
            "action": "digest",
            "message_type": "unknown",
            "reason": "Fallback because Gemini quota exceeded.",
            "confidence": 0.50
        }