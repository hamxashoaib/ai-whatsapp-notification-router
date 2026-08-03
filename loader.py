import pandas as pd


def load_data():
    """
    Load all datasets into a dictionary.
    """

    data = {
        "messages": pd.read_csv("dataset/messages.csv"),
        "users": pd.read_csv("dataset/users.csv"),
        "groups": pd.read_csv("dataset/groups.csv"),
        "group_members": pd.read_csv("dataset/group_members.csv"),
        "business_accounts": pd.read_csv("dataset/business_accounts.csv"),
        "user_business_history": pd.read_csv("dataset/user_business_history.csv"),
        "message_history": pd.read_csv("dataset/message_history.csv"),
        "message_events": pd.read_csv("dataset/message_events.csv"),
        "sample_messages": pd.read_csv("dataset/sample_messages.csv"),
        "images": pd.read_csv("dataset/images.csv"),
        "voice_notes": pd.read_csv("dataset/voice_notes.csv"),
    }

    return data