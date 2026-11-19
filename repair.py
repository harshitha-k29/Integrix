# repair.py - owner: Coder 1
from contract import CONFIDENCE_THRESHOLD, CHANGE_LOG_COLUMNS


def repair(df, issues):
    clean_df = df.copy()
    change_log = []
    needs_review = []
    # TODO: for each issue, compute new_value + confidence.
    # confidence >= CONFIDENCE_THRESHOLD -> apply and add to change_log
    # otherwise -> add to needs_review
    return clean_df, change_log, needs_review