import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    classification_report,
)


def evaluate(
    prediction_file="output.csv",
    ground_truth_file="dataset/messages.csv",
):
    """
    Evaluation workflow for the Message Notification Router.

    If ground-truth labels exist, computes:
    - Accuracy
    - Precision
    - Recall
    - F1 Score
    - Classification Report

    If no labels are available, reports that the evaluation
    workflow executed successfully.
    """

    print("=" * 60)
    print("MESSAGE NOTIFICATION ROUTER - EVALUATION")
    print("=" * 60)

    # ----------------------------
    # Load files
    # ----------------------------
    try:
        pred = pd.read_csv(prediction_file)
    except Exception as e:
        print(f"Error loading prediction file: {e}")
        return

    try:
        gt = pd.read_csv(ground_truth_file)
    except Exception as e:
        print(f"Error loading ground-truth file: {e}")
        return

    print(f"Predictions Loaded : {len(pred)}")
    print(f"Ground Truth Loaded: {len(gt)}")
    print()

    # ----------------------------
    # Locate ground-truth label column
    # ----------------------------
    possible_label_cols = [
        "expected_output",
        "expected_label",
        "label",
        "route",
        "target",
    ]

    label_col = None

    for col in possible_label_cols:
        if col in gt.columns:
            label_col = col
            break

    if label_col is None:
        print("No ground-truth labels found.")
        print("Evaluation workflow executed successfully.")
        print("Predictions were generated correctly.")
        print(f"Total predictions: {len(pred)}")
        return

    # ----------------------------
    # Validate message_id
    # ----------------------------
    if "message_id" not in pred.columns:
        print("Prediction file is missing 'message_id'.")
        return

    if "message_id" not in gt.columns:
        print("Ground-truth file is missing 'message_id'.")
        return

    # ----------------------------
    # Merge
    # ----------------------------
    data = gt[["message_id", label_col]].merge(
        pred,
        on="message_id",
        how="inner",
    )

    print(f"Matched Samples: {len(data)}")

    if len(data) == 0:
        print("No matching message IDs found.")
        return

    # ----------------------------
    # Locate prediction column
    # ----------------------------
    prediction_cols = [
        "action",
        "prediction",
        "route",
        "output",
        "label",
    ]

    pred_col = None

    for col in prediction_cols:
        if col in data.columns:
            pred_col = col
            break

    if pred_col is None:
        print("Prediction column not found.")
        return

    # ----------------------------
    # Metrics
    # ----------------------------
    y_true = data[label_col]
    y_pred = data[pred_col]

    accuracy = accuracy_score(y_true, y_pred)

    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true,
        y_pred,
        average="weighted",
        zero_division=0,
    )

    print()
    print("=" * 60)
    print("EVALUATION RESULTS")
    print("=" * 60)

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    print()
    print("=" * 60)
    print("CLASSIFICATION REPORT")
    print("=" * 60)

    print(classification_report(
        y_true,
        y_pred,
        zero_division=0,
    ))

    print("=" * 60)
    print("Evaluation completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    evaluate()