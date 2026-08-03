import pandas as pd


def load_images():
    """
    Load image metadata.
    """
    try:
        return pd.read_csv("dataset/images.csv")
    except Exception:
        return pd.DataFrame()


def load_voice_notes():
    """
    Load voice note metadata.
    """
    try:
        return pd.read_csv("dataset/voice_notes.csv")
    except Exception:
        return pd.DataFrame()


def get_image(message_id, images):
    """
    Retrieve image for a message.
    """
    result = images[
        images["message_id"] == message_id
    ]

    if result.empty:
        return None

    return result.iloc[0]


def get_voice(message_id, voices):
    """
    Retrieve voice note for a message.
    """
    result = voices[
        voices["message_id"] == message_id
    ]

    if result.empty:
        return None

    return result.iloc[0]