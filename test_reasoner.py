from prompt_builder import build_prompt
from reasoner import ask_gemini

features = {
    "opened_30d": 45,
    "replied_30d": 10,
    "dismissed_30d": 5,
    "reported_30d": 0,
    "verified_business": True,
    "business_category": "bank",
    "business_reports": 1,
    "group_muted": False,
    "history_count": 18,
    "conversation_type": "business",
    "forwarded_count": 0,
    "text": "Your salary has been credited to your account."
}

prompt = build_prompt(features)

result = ask_gemini(prompt)

print(result)