from retriever import retrieve_context
from features import build_features
from rules import classify_message
from prompt_builder import build_prompt
from reasoner import ask_gemini
from validator import validate_prediction
from evidence import get_evidence


def predict(data):

    predictions = []

    messages = data["messages"]
    sample_messages = data["sample_messages"]

    # Use first 3 examples as few-shot examples
    examples = sample_messages.head(3).to_dict("records")

    for _, message in messages.iterrows():

        # -------------------------------------------------
        # Retrieve Context
        # -------------------------------------------------

        context = retrieve_context(message, data)

        # -------------------------------------------------
        # Build Features
        # -------------------------------------------------

        features = build_features(context)

        # -------------------------------------------------
        # Fast Rule Engine
        # -------------------------------------------------

        action, message_type, reason, confidence = classify_message(
            context["message"],
            context["user"],
            context["business"]
        )

        # -------------------------------------------------
        # If confidence is low, ask Gemini
        # -------------------------------------------------

        if confidence < 0.90:

            prompt = build_prompt(features, examples)

            ai_result = ask_gemini(prompt)

            ai_result = validate_prediction(ai_result)

            action = ai_result["action"]
            message_type = ai_result["message_type"]
            reason = ai_result["reason"]
            confidence = ai_result["confidence"]

        # -------------------------------------------------
        # Evidence Retrieval
        # -------------------------------------------------

        evidence = get_evidence(
            context["message"],
            context["history"]
        )

        # -------------------------------------------------
        # Save Prediction
        # -------------------------------------------------

        predictions.append({

            "message_id": message["message_id"],

            "action": action,

            "message_type": message_type,

            "reason": reason,

            "confidence": confidence,

            "evidence_message_ids": evidence

        })

    return predictions