def build_features(context):
    """
    Convert retrieved context into AI-friendly features.
    """

    message = context["message"]
    user = context["user"]
    business = context["business"]
    membership = context["membership"]
    history = context["history"]
    user_business = context["user_business"]

    features = {}

    # ======================
    # MESSAGE
    # ======================

    features["message_id"] = message["message_id"]
    features["user_id"] = message["user_id"]
    features["conversation_type"] = message["conversation_type"]

    features["text"] = (
        str(message["message_text"])
        if message["message_text"] == message["message_text"]
        else ""
    )

    features["forwarded_count"] = int(message["forwarded_count"])

    # ======================
    # USER
    # ======================

    if user is not None:

        features["opened_30d"] = int(user["messages_opened_30d"])
        features["replied_30d"] = int(user["messages_replied_30d"])
        features["dismissed_30d"] = int(user["notifications_dismissed_30d"])
        features["reported_30d"] = int(user["messages_reported_30d"])

    else:

        features["opened_30d"] = 0
        features["replied_30d"] = 0
        features["dismissed_30d"] = 0
        features["reported_30d"] = 0

    # ======================
    # BUSINESS
    # ======================

    if business is not None:

        features["verified_business"] = bool(business["verified"])
        features["business_category"] = business["category"]
        features["business_reports"] = int(
            business["user_reports_30d"]
        )

    else:

        features["verified_business"] = False
        features["business_category"] = None
        features["business_reports"] = 0

    # ======================
    # GROUP
    # ======================

    if membership is not None:

        features["group_muted"] = bool(
            membership["group_muted_by_user"]
        )

    else:

        features["group_muted"] = False

    # ======================
    # HISTORY
    # ======================

    features["history_count"] = len(history)

    # ======================
    # USER BUSINESS
    # ======================

    if user_business is not None:

        features["business_activity"] = int(
            user_business["activity_count_180d"]
        )

        features["allows_promotions"] = bool(
            user_business["allows_promotions"]
        )

    else:

        features["business_activity"] = 0
        features["allows_promotions"] = False

    return features