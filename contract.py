# contract.py - shared format between detect.py, repair.py, app.py
# Do not change names or function signatures without telling the team lead.

ISSUE_TYPES = [
    "missing",
    "duplicate",
    "bad_email",
    "bad_phone",
    "mixed_date",
    "inconsistent_label",
    "outlier",
]

# One issue found by detect.py:
# {"row": int, "column": str, "issue_type": str, "value": str, "details": str}

# One change made by repair.py:
# {"row": int, "column": str, "old_value": str, "new_value": str,
#  "reason": str, "confidence": float}

CONFIDENCE_THRESHOLD = 0.8  # >= auto-fix, below = needs review

CHANGE_LOG_COLUMNS = ["row", "column", "old_value", "new_value", "reason", "confidence"]

# detect.py : detect_issues(df) -> list of issue dicts
# repair.py : repair(df, issues) -> (clean_df, change_log, needs_review)