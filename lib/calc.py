"""
Pure settlement + projection math for one team's Over/Under pick.
No I/O here on purpose, so this is easy to reason about and test in isolation.
"""

REGULAR_SEASON_GAMES = 12  # standard FBS length; also how BetMGM set these lines


def games_remaining(games_played: int, games_total: int = REGULAR_SEASON_GAMES) -> int:
    return max(games_total - games_played, 0)


def settlement_status(wins: int, games_played: int, line: float,
                       games_total: int = REGULAR_SEASON_GAMES) -> str:
    """Has this team's win total already clinched Over, clinched Under, or is it still live?"""
    remaining = games_remaining(games_played, games_total)
    max_possible_wins = wins + remaining
    if wins > line:
        return "Over"
    if max_possible_wins < line:
        return "Under"
    return "Pending"


def projected_final_wins(wins: int, games_played: int, line: float,
                          games_total: int = REGULAR_SEASON_GAMES) -> float:
    """
    Blend actual wins so far with the preseason line's implied win rate for
    the games not yet played (regress unplayed games to what the market
    expected, not to noisy early-season pace).
    """
    remaining = games_remaining(games_played, games_total)
    return wins + line * (remaining / games_total)


def projected_result(wins: int, games_played: int, line: float,
                      games_total: int = REGULAR_SEASON_GAMES) -> str | None:
    """
    None means "no real signal yet" — projected_final_wins exactly ties the
    line, which (given lines are all X.5) only happens when no games have
    been played, so there's nothing to project from besides the line itself.
    """
    proj = projected_final_wins(wins, games_played, line, games_total)
    if proj == line:
        return None
    return "Over" if proj > line else "Under"


def projected_margin(wins: int, games_played: int, line: float, pick: str,
                      games_total: int = REGULAR_SEASON_GAMES) -> float:
    """
    Signed distance between the projection and the line, from the drafter's
    point of view: positive means the projection currently favors their
    pick, negative means it favors the other side. Summed across a
    drafter's 9 picks, this is the tiebreaker when two drafters have the
    same Projected Correct count — whoever's picks are collectively
    projected further in their own favor ranks higher.
    """
    margin = projected_final_wins(wins, games_played, line, games_total) - line
    return margin if pick == "Over" else -margin


def pick_outcome(status: str | None, pick: str) -> str:
    """status/pick are each 'Over' or 'Under'; status may also be 'Pending' or None."""
    if status in ("Pending", None):
        return "Pending"
    return "Correct" if status == pick else "Incorrect"


def evaluate_pick(wins: int, games_played: int, line: float, pick: str,
                   games_total: int = REGULAR_SEASON_GAMES) -> dict:
    """Everything the UI needs for one pick, given that team's current record."""
    status = settlement_status(wins, games_played, line, games_total)
    proj_final = projected_final_wins(wins, games_played, line, games_total)
    proj_result = projected_result(wins, games_played, line, games_total)
    effective_result = proj_result if status == "Pending" else status
    return {
        "wins": wins,
        "games_played": games_played,
        "games_remaining": games_remaining(games_played, games_total),
        "status": status,
        "outcome": pick_outcome(status, pick),
        "projected_final_wins": round(proj_final, 2),
        "projected_result": effective_result or "Pending",
        "projected_outcome": pick_outcome(effective_result, pick),
        "projected_margin": round(projected_margin(wins, games_played, line, pick, games_total), 3),
    }
