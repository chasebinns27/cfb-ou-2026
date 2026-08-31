import pandas as pd
import streamlit as st

from data.draft_picks import DRAFTERS, UNDRAFTED_TEAMS, picks_with_team_info
from lib import cfbd, calc

st.set_page_config(page_title="2026 CFB Win Total Draft Tracker", layout="wide")

STATUS_COLORS = {
    "Correct": "background-color: #1e7d34; color: white",
    "Incorrect": "background-color: #b3261e; color: white",
    "Pending": "background-color: #4b4b4b; color: white",
}


@st.cache_data(ttl=cfbd.CACHE_TTL_SECONDS, show_spinner=False)
def load_records():
    return cfbd.fetch_team_records()


def build_picks_df(records: dict, records_ok: bool) -> pd.DataFrame:
    rows = []
    for pick in picks_with_team_info():
        record = cfbd.get_record_for_team(records, pick["team"]) if records_ok else {"wins": 0, "games_played": 0}
        evaluation = calc.evaluate_pick(
            wins=record["wins"],
            games_played=record["games_played"],
            line=pick["line"],
            pick=pick["pick"],
        )
        rows.append({**pick, **evaluation})
    return pd.DataFrame(rows)


def render_leaderboard(df: pd.DataFrame):
    st.subheader("Leaderboard")
    st.caption(
        "Locked = the pick has already mathematically clinched Over or Under. "
        "Projected Correct = Locked Correct plus each drafter's still-pending picks, "
        "using the projection described below. Tiebreaker = each drafter's 9 picks' "
        "projected margins (projection vs. line, signed toward their pick) summed "
        "together — whoever's picks are collectively projected further in their own "
        "favor ranks higher when Projected Correct ties."
    )

    summary = (
        df.groupby("drafter")
        .apply(lambda g: pd.Series({
            "Locked Correct": (g["outcome"] == "Correct").sum(),
            "Locked Incorrect": (g["outcome"] == "Incorrect").sum(),
            "Projected Correct": (g["projected_outcome"] == "Correct").sum(),
            "Tiebreaker": g["projected_margin"].sum(),
        }), include_groups=False)
        .reset_index()
        .rename(columns={"drafter": "Drafter"})
        .assign(**{"Tiebreaker": lambda d: d["Tiebreaker"].round(2)})
        .sort_values(["Projected Correct", "Tiebreaker"], ascending=False)
        .reset_index(drop=True)
    )
    summary.index = summary.index + 1

    if not summary.empty:
        leader = summary.iloc[0]
        st.metric(
            "Currently projected to win",
            leader["Drafter"],
            help=f"{int(leader['Projected Correct'])} projected correct picks out of 9",
        )

    st.dataframe(summary, width="stretch")


def render_draft_board(df: pd.DataFrame):
    st.subheader("Draft Board")
    st.caption("Snake draft order, mirroring the original sheet. Colored by live status.")

    display = pd.DataFrame(index=range(1, 10), columns=DRAFTERS, dtype=object)
    status = pd.DataFrame(index=range(1, 10), columns=DRAFTERS, dtype=object)

    for _, pick in df.iterrows():
        record = f"{int(pick['wins'])}-{int(pick['games_played'] - pick['wins'])}"
        display.loc[pick["round"], pick["drafter"]] = (
            f"{pick['team']} ({pick['pick']}, line {pick['line']}) — {record}"
        )
        status.loc[pick["round"], pick["drafter"]] = pick["outcome"]

    display.index.name = "Round"

    styler = display.style.apply(
        lambda _: status.map(lambda s: STATUS_COLORS.get(s, "")),
        axis=None,
    )
    st.dataframe(styler, width="stretch", height=380)


def render_all_picks(df: pd.DataFrame):
    st.subheader("All Picks")

    table = df.copy()
    table["record"] = table["wins"].astype(int).astype(str) + "-" + (
        table["games_played"] - table["wins"]
    ).astype(int).astype(str)

    table = table.rename(columns={
        "overall_pick": "Pick #",
        "round": "Round",
        "drafter": "Drafter",
        "team": "Team",
        "conference": "Conference",
        "line": "Line",
        "pick": "Pick",
        "record": "Record",
        "status": "Status",
        "outcome": "Outcome",
        "projected_final_wins": "Projected Final Wins",
        "projected_outcome": "Projected Outcome",
    })

    columns = [
        "Pick #", "Round", "Drafter", "Team", "Conference", "Line", "Pick",
        "Record", "Status", "Outcome", "Projected Final Wins", "Projected Outcome",
    ]
    st.dataframe(
        table[columns].sort_values("Pick #").reset_index(drop=True),
        width="stretch",
        height=560,
    )

    with st.expander(f"Undrafted teams ({len(UNDRAFTED_TEAMS)})"):
        st.write(", ".join(UNDRAFTED_TEAMS))


def main():
    st.title("2026 CFB Win Total Draft Tracker")
    st.caption(
        "Tracking all 63 picks from the snake draft against BetMGM's preseason win totals. "
        "Every team's season is treated as a fixed 12 games, matching how the lines were set; "
        "settlement is based on regular-season games only. Data refreshes at most every 15 minutes."
    )

    records, records_ok = {}, True
    try:
        records = load_records()
    except Exception as exc:
        records_ok = False
        st.warning(f"Couldn't refresh live team records right now ({exc}). Showing preseason data only.")

    df = build_picks_df(records, records_ok)

    tab_leaderboard, tab_board, tab_all_picks = st.tabs(["Leaderboard", "Draft Board", "All Picks"])
    with tab_leaderboard:
        render_leaderboard(df)
    with tab_board:
        render_draft_board(df)
    with tab_all_picks:
        render_all_picks(df)


if __name__ == "__main__":
    main()
