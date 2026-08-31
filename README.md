# 2026 CFB Win Total Draft Tracker

Streamlit app tracking a 7-person snake draft of 2026 college football win
totals (BetMGM lines). Each drafter took 9 teams and called Over or Under on
that team's preseason win total; this app tracks which picks have already
clinched, which are still live, and who's projected to finish with the most
correct picks.

The 63 draft picks are baked into [data/draft_picks.py](data/draft_picks.py)
(the draft is final, so there's no live Google Sheets dependency). Current
team records are pulled live from the
[College Football Data API](https://collegefootballdata.com/).

## How settlement works

Every team's season is treated as a fixed 12 games (standard FBS length, and
how BetMGM set these lines), using regular-season games only.

- A pick **clinches Over** once the team's wins exceed the line.
- A pick **clinches Under** once the team can no longer reach the line even
  by winning out.
- Otherwise it's **Pending**.

**Projected final wins** for a pending pick blends actual wins so far with
the preseason line's implied win rate for the games not yet played:

```
projected_final_wins = wins + line * (games_remaining / 12)
```

This regresses the *unplayed* games to what the market expected preseason,
rather than extrapolating from noisy early-season pace.

## Local setup

```bash
pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# then edit .streamlit/secrets.toml and paste in your real CFBD_API_KEY
streamlit run app.py
```

Open http://localhost:8501.

## Deploying to Posit Connect

```bash
pip install rsconnect-python
rsconnect deploy streamlit . \
  --entrypoint app.py \
  --server <your-connect-url> \
  --api-key <your-connect-api-key>
```

On Connect, set `CFBD_API_KEY` as an **environment variable** on the
content item's settings page — the app reads `CFBD_API_KEY` from the
environment first, falling back to `.streamlit/secrets.toml` only for local
dev. Don't upload `secrets.toml` to Connect.

## Project structure

```
app.py                  Streamlit entrypoint (Leaderboard / Draft Board / All Picks tabs)
data/draft_picks.py      baked-in draft results (teams, lines, picks)
lib/cfbd.py              live CFBD API fetch + caching
lib/calc.py              settlement + projection math (pure functions)
```
