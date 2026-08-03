def retrieve_context(message, data):
    """
    Retrieve all useful context for a single message.
    """

    context = {}

    # -----------------------
    # Message
    # -----------------------
    context["message"] = message

    # -----------------------
    # User
    # -----------------------
    user = data["users"][
        data["users"]["user_id"] == message["user_id"]
    ]

    context["user"] = user.iloc[0] if not user.empty else None

    # -----------------------
    # Business
    # -----------------------
    business = None

    if message["conversation_type"] == "business":

        business = data["business_accounts"][
            data["business_accounts"]["business_id"]
            == message["business_id"]
        ]

        if not business.empty:
            business = business.iloc[0]
        else:
            business = None

    context["business"] = business

    # -----------------------
    # Group
    # -----------------------
    group = None

    if message["conversation_type"] == "group":

        group = data["groups"][
            data["groups"]["group_id"]
            == message["group_id"]
        ]

        if not group.empty:
            group = group.iloc[0]
        else:
            group = None

    context["group"] = group

    # -----------------------
    # Group Member
    # -----------------------
    membership = None

    if message["conversation_type"] == "group":

        membership = data["group_members"][
            (data["group_members"]["group_id"] == message["group_id"])
            &
            (data["group_members"]["user_id"] == message["user_id"])
        ]

        if not membership.empty:
            membership = membership.iloc[0]
        else:
            membership = None

    context["membership"] = membership

    # -----------------------
    # User Business History
    # -----------------------
    ub = None

    if message["conversation_type"] == "business":

        ub = data["user_business_history"][
            (data["user_business_history"]["user_id"] == message["user_id"])
            &
            (data["user_business_history"]["business_id"] == message["business_id"])
        ]

        if not ub.empty:
            ub = ub.iloc[0]
        else:
            ub = None

    context["user_business"] = ub

    # -----------------------
    # Message History
    # -----------------------
    history = data["message_history"][
        data["message_history"]["user_id"] == message["user_id"]
    ]

    context["history"] = history

    # -----------------------
    # Message Events
    # -----------------------
    events = data["message_events"][
        data["message_events"]["user_id"] == message["user_id"]
    ]

    context["events"] = events

    return context