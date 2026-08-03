def classify_message(message, user, business):
    """
    Classify a WhatsApp message into:
    notify, digest, or mute
    """

    text = str(message.get("message_text", "")).lower()

    # ==========================================================
    # 1. VERIFIED BUSINESS RULES
    # ==========================================================

    if business is not None:

        # Trusted verified businesses
        if business["verified"] == 1:

            # Banking messages
            if business["category"] == "bank":

                if "otp" not in text and "password" not in text:
                    return (
                        "notify",
                        "payment",
                        "Trusted verified bank notification.",
                        0.97
                    )

            # Delivery / Telecom / Ride booking
            if business["category"] in [
                "ecommerce_delivery",
                "ride_booking",
                "telecom"
            ]:
                return (
                    "digest",
                    "business_update",
                    "Verified business update.",
                    0.90
                )

        # Unverified business with many reports
        if business["verified"] == 0 and business["user_reports_30d"] > 20:
            return (
                "mute",
                "spam",
                "Business has many user reports.",
                0.95
            )

    # ==========================================================
    # 2. SCAM DETECTION
    # ==========================================================

    scam_words = [
        "otp",
        "password",
        "verify account",
        "click here",
        "winner",
        "lottery",
        "claim prize",
        "bank account",
        "gift card",
        "crypto",
        "login code"
    ]

    for word in scam_words:
        if word in text:
            return (
                "mute",
                "scam",
                "Possible phishing or scam message.",
                0.98
            )

    # ==========================================================
    # 3. URGENT PERSONAL MESSAGES
    # ==========================================================

    urgent_words = [
        "urgent",
        "asap",
        "emergency",
        "call me",
        "immediately",
        "hospital",
        "accident"
    ]

    for word in urgent_words:
        if word in text:
            return (
                "notify",
                "urgent",
                "Urgent message requiring immediate attention.",
                0.95
            )

    # ==========================================================
    # 4. PROMOTIONS
    # ==========================================================

    promo_words = [
        "sale",
        "discount",
        "offer",
        "buy now",
        "limited time",
        "cashback",
        "coupon"
    ]

    for word in promo_words:
        if word in text:
            return (
                "digest",
                "promotion",
                "Promotional message.",
                0.85
            )

    # ==========================================================
    # 5. FORWARDED MESSAGES
    # ==========================================================

    if message.get("forwarded_count", 0) >= 5:
        return (
            "mute",
            "forward",
            "Frequently forwarded message.",
            0.88
        )

    # ==========================================================
    # 6. USER BEHAVIOUR
    # ==========================================================

    if user is not None:

        if user["notifications_dismissed_30d"] > 30:
            return (
                "digest",
                "personal",
                "User usually dismisses notifications.",
                0.80
            )

    # ==========================================================
    # 7. DEFAULT
    # ==========================================================

    return (
        "digest",
        "personal",
        "Normal message.",
        0.75
    )