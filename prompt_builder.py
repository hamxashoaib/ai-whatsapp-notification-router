import json


def build_prompt(features, examples=None):
    """
    Build a structured prompt for Gemini.
    """

    few_shot = ""

    if examples:

        few_shot += "\n### Example Decisions\n"

        for ex in examples[:3]:

            few_shot += f"""
Message:
{ex["message_text"]}

Expected Output:
Action: {ex["action"]}
Type: {ex["message_type"]}
Reason: {ex["reason"]}
"""

    prompt = f"""
You are an expert AI Notification Routing Agent for WhatsApp.

Your goal is to classify ONE incoming message.

Think carefully before answering.

==================================================
Reasoning Priority
==================================================

1. User Safety
   - Detect scams
   - Detect phishing
   - Detect spam

2. Urgency
   - Medical
   - Emergency
   - Payment
   - OTP
   - Family emergencies

3. Trust

   Prefer verified businesses over unknown senders.

4. Personalization

   Consider:

   - User notification history
   - User dismissals
   - User reports
   - Previous interactions

5. Notification Fatigue

   Don't notify unless interruption is valuable.

==================================================
Allowed Actions
==================================================

notify
digest
mute

==================================================
Allowed Message Types
==================================================

personal
urgent
event
payment
business_update
promotion
greeting
forward
spam
scam
unknown

==================================================
User
==================================================

Opened Messages:
{features["opened_30d"]}

Replies:
{features["replied_30d"]}

Dismissed:
{features["dismissed_30d"]}

Reported:
{features["reported_30d"]}

==================================================
Business
==================================================

Verified:
{features["verified_business"]}

Category:
{features["business_category"]}

Reports:
{features["business_reports"]}

==================================================
Group
==================================================

Muted:
{features["group_muted"]}

==================================================
History
==================================================

Previous Messages:
{features["history_count"]}

==================================================
Incoming Message
==================================================

Conversation:
{features["conversation_type"]}

Forward Count:
{features["forwarded_count"]}

Text:

{features["text"]}

{few_shot}

==================================================
Return ONLY JSON.

Example:

{{
  "action":"notify",
  "message_type":"payment",
  "reason":"Verified bank payment update.",
  "confidence":0.96
}}

Do not explain anything.
Do not use markdown.
Return valid JSON only.
"""

    return prompt