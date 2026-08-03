import pandas as pd


def get_evidence(message, history):
    """
    Find similar historical messages for evidence.
    Returns semicolon-separated message IDs.
    """

    if history.empty:
        return "none"

    text = str(message.get("message_text", "")).lower().strip()

    if text == "":
        return "none"

    matches = []

    for _, row in history.iterrows():

        old_text = str(row.get("message_text", "")).lower()

        # Exact match
        if text == old_text:
            matches.append(row["message_id"])
            continue

        # Partial match
        words = text.split()

        overlap = 0

        for word in words:
            if len(word) > 3 and word in old_text:
                overlap += 1

        if overlap >= 2:
            matches.append(row["message_id"])

        if len(matches) == 3:
            break

    if len(matches) == 0:
        return "none"

    return ";".join(matches)