"""
Fetches current-season team records from the College Football Data API
(collegefootballdata.com) and aggregates them into per-team wins / games
played. One request covers every FBS team for the year, which is far
cheaper than one request per team.
"""

import os
import requests
import streamlit as st

CFBD_GAMES_URL = "https://api.collegefootballdata.com/games"
SEASON_YEAR = 2026
CACHE_TTL_SECONDS = 900  # 15 minutes

# Our draft data's team names occasionally differ from CFBD's team names.
TEAM_NAME_ALIASES = {
    "Miami (FL)": "Miami",
}


def get_api_key():
    """Env var wins (how Posit Connect injects secrets); falls back to
    .streamlit/secrets.toml for local dev."""
    key = os.environ.get("CFBD_API_KEY")
    if key:
        return key
    try:
        return st.secrets["CFBD_API_KEY"]
    except Exception:
        return None


def _to_cfbd_name(team: str) -> str:
    return TEAM_NAME_ALIASES.get(team, team)


@st.cache_data(ttl=CACHE_TTL_SECONDS, show_spinner=False)
def fetch_team_records(year: int = SEASON_YEAR) -> dict:
    """
    Returns {cfbd_team_name: {"wins": int, "games_played": int}} for every
    team that has appeared in a completed regular-season game this year.
    """
    api_key = get_api_key()
    if not api_key:
        raise RuntimeError(
            "No CFBD_API_KEY found. Add it to .streamlit/secrets.toml locally, "
            "or as an environment variable on Posit Connect."
        )

    response = requests.get(
        CFBD_GAMES_URL,
        params={"year": year, "seasonType": "regular"},
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=30,
    )
    response.raise_for_status()
    games = response.json()

    records: dict = {}

    def _record(team_name):
        return records.setdefault(team_name, {"wins": 0, "games_played": 0})

    for game in games:
        if not game.get("completed"):
            continue

        home, away = game.get("homeTeam"), game.get("awayTeam")
        home_pts, away_pts = game.get("homePoints"), game.get("awayPoints")
        if home is None or away is None or home_pts is None or away_pts is None:
            continue

        _record(home)["games_played"] += 1
        _record(away)["games_played"] += 1

        if home_pts > away_pts:
            _record(home)["wins"] += 1
        elif away_pts > home_pts:
            _record(away)["wins"] += 1

    return records


def get_record_for_team(records: dict, team: str) -> dict:
    """Looks up one of our draft-board team names in the CFBD records dict."""
    return records.get(_to_cfbd_name(team), {"wins": 0, "games_played": 0})
