from validator import validate_prediction

bad = {
    "action": "hello",
    "message_type": "xyz",
    "reason": "",
    "confidence": 9.5
}

print(validate_prediction(bad))