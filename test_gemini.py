from config import client, MODEL_NAME

response = client.models.generate_content(
    model=MODEL_NAME,
    contents="Reply with exactly: Gemini Connected Successfully!"
)

print(response.text)