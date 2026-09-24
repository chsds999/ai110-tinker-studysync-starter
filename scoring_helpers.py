"""
Target file for Tinker 1B, Part 2.

Move `apply_streak_bonus(combined_score, streak_days)` here from scoring.py,
then update the import at the top of scoring.py so `run_demo()` and the
Session Scorer tab still work exactly as before.
"""

def apply_streak_bonus(combined_score: int, streak_days: int) -> int:
    # Calculate the boosted score.
    # Every streak day adds 2 points to the original combined score.
    boosted = combined_score + streak_days * 2

    # Return the boosted score, but never allow it to go above 100.
    return min(boosted, 100)