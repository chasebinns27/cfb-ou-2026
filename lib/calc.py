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
                      games_total: int = REGULAR_SEASON_GAMES) -> str:
    proj = projected_final_wins(wins, games_played, line, games_total)
    return "Over" if proj > line else "Under"


def pick_outcome(status: str, pick: str) -> str:
    """status/pick are each 'Over' or 'Under'; status may also be 'Pending'."""
    if status == "Pending":
        return "Pending"
    return "Correct" if status == pick else "Incorrect"


def evaluate_pick(wins: int, games_played: int, line: float, pick: str,
                   games_total: int = REGULAR_SEASON_GAMES) -> dict:
    """Everything the UI needs for one pick, given that team's current record."""
    status = settlement_status(wins, games_played, line, games_total)
    proj_final = projected_final_wins(wins, games_played, line, games_total)
    proj_result = "Over" if proj_final > line else "Under"
    return {
        "wins": wins,
        "games_played": games_played,
        "games_remaining": games_remaining(games_played, games_total),
        "status": status,
        "outcome": pick_outcome(status, pick),
        "projected_final_wins": round(proj_final, 2),
        "projected_result": proj_result,
        "projected_outcome": pick_outcome(proj_result if status == "Pending" else status, pick),
    }
