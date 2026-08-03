from loader import load_data
from evidence import get_evidence

data = load_data()

message = data["messages"].iloc[0]

history = data["message_history"][
    data["message_history"]["user_id"] == message["user_id"]
]

print("Current Message:")
print(message["message_text"])

print("\nEvidence:")
print(get_evidence(message, history))