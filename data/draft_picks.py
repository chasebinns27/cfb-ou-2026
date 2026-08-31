"""
Baked-in results of the 2026 CFB Win Total snake draft.

Source: the "2026 CFB Win Total Draft" Google Sheet (Draft Board + Team Pool
tabs), which itself was built from ../2026-cfb-win-totals-betmgm.md
(BetMGM lines, Aug 18 2026). The draft is final (63/63 picks made), so this
is a static snapshot rather than a live Google Sheets read.
"""

DRAFTERS = ["Nick", "Chase", "John", "Ben", "Zach", "Charles", "Jason"]

# Every team on the BetMGM board: conference, preseason win total line, and
# American-odds prices for the Over/Under (None where BetMGM didn't publish
# a price, e.g. Northwestern).
TEAMS = {
    "Notre Dame":        {"conference": "Independent", "line": 11.5, "over_odds": 150,  "under_odds": -200, "hold_pct": 6.7},

    "Miami (FL)":        {"conference": "ACC", "line": 10.5, "over_odds": -125, "under_odds": 100,  "hold_pct": 5.6},
    "SMU":               {"conference": "ACC", "line": 8.5,  "over_odds": -140, "under_odds": 115,  "hold_pct": 4.8},
    "Louisville":        {"conference": "ACC", "line": 8.5,  "over_odds": 120,  "under_odds": -145, "hold_pct": 4.6},
    "Clemson":           {"conference": "ACC", "line": 7.5,  "over_odds": -145, "under_odds": 120,  "hold_pct": 4.6},
    "Pittsburgh":        {"conference": "ACC", "line": 7.5,  "over_odds": -145, "under_odds": 120,  "hold_pct": 4.6},
    "Virginia":          {"conference": "ACC", "line": 7.5,  "over_odds": -145, "under_odds": 120,  "hold_pct": 4.6},
    "NC State":          {"conference": "ACC", "line": 7.5,  "over_odds": 100,  "under_odds": -120, "hold_pct": 4.5},
    "Virginia Tech":     {"conference": "ACC", "line": 6.5,  "over_odds": -175, "under_odds": 145,  "hold_pct": 4.5},
    "California":        {"conference": "ACC", "line": 6.5,  "over_odds": 110,  "under_odds": -135, "hold_pct": 5.1},
    "Georgia Tech":      {"conference": "ACC", "line": 6.5,  "over_odds": 115,  "under_odds": -140, "hold_pct": 4.8},
    "Florida State":     {"conference": "ACC", "line": 6.5,  "over_odds": 165,  "under_odds": -200, "hold_pct": 4.4},
    "Duke":              {"conference": "ACC", "line": 5.5,  "over_odds": -135, "under_odds": 110,  "hold_pct": 5.1},
    "Wake Forest":       {"conference": "ACC", "line": 5.5,  "over_odds": -130, "under_odds": 110,  "hold_pct": 4.1},
    "Syracuse":          {"conference": "ACC", "line": 4.5,  "over_odds": -115, "under_odds": -105, "hold_pct": 4.7},
    "North Carolina":    {"conference": "ACC", "line": 4.5,  "over_odds": -115, "under_odds": -105, "hold_pct": 4.7},
    "Stanford":          {"conference": "ACC", "line": 3.5,  "over_odds": -125, "under_odds": 105,  "hold_pct": 4.3},
    "Boston College":    {"conference": "ACC", "line": 3.5,  "over_odds": 115,  "under_odds": -140, "hold_pct": 4.8},

    "Indiana":           {"conference": "Big Ten", "line": 10.5, "over_odds": 110,  "under_odds": -130, "hold_pct": 4.1},
    "Oregon":            {"conference": "Big Ten", "line": 10.5, "over_odds": 100,  "under_odds": -120, "hold_pct": 4.5},
    "Ohio State":        {"conference": "Big Ten", "line": 9.5,  "over_odds": -175, "under_odds": 145,  "hold_pct": 4.5},
    "Penn State":        {"conference": "Big Ten", "line": 9.5,  "over_odds": 125,  "under_odds": -150, "hold_pct": 4.4},
    "USC":               {"conference": "Big Ten", "line": 8.5,  "over_odds": 110,  "under_odds": -135, "hold_pct": 5.1},
    "Michigan":          {"conference": "Big Ten", "line": 8.5,  "over_odds": 130,  "under_odds": -155, "hold_pct": 4.3},
    "Washington":        {"conference": "Big Ten", "line": 7.5,  "over_odds": -160, "under_odds": 125,  "hold_pct": 6.0},
    "Iowa":              {"conference": "Big Ten", "line": 7.5,  "over_odds": -145, "under_odds": 110,  "hold_pct": 6.8},
    "Illinois":          {"conference": "Big Ten", "line": 7.5,  "over_odds": 130,  "under_odds": -170, "hold_pct": 6.4},
    "Wisconsin":         {"conference": "Big Ten", "line": 6.5,  "over_odds": -135, "under_odds": 105,  "hold_pct": 6.2},
    "UCLA":              {"conference": "Big Ten", "line": 6.5,  "over_odds": 100,  "under_odds": -125, "hold_pct": 5.6},
    "Nebraska":          {"conference": "Big Ten", "line": 6.5,  "over_odds": 120,  "under_odds": -155, "hold_pct": 6.2},
    "Minnesota":         {"conference": "Big Ten", "line": 6.5,  "over_odds": 130,  "under_odds": -170, "hold_pct": 6.4},
    "Northwestern":      {"conference": "Big Ten", "line": 5.5,  "over_odds": None, "under_odds": None, "hold_pct": None},
    "Maryland":          {"conference": "Big Ten", "line": 4.5,  "over_odds": -185, "under_odds": 140,  "hold_pct": 6.6},
    "Rutgers":           {"conference": "Big Ten", "line": 4.5,  "over_odds": -155, "under_odds": 120,  "hold_pct": 6.2},
    "Michigan State":    {"conference": "Big Ten", "line": 4.5,  "over_odds": 145,  "under_odds": -190, "hold_pct": 6.3},
    "Purdue":            {"conference": "Big Ten", "line": 3.5,  "over_odds": 115,  "under_odds": -145, "hold_pct": 5.7},

    "Texas Tech":        {"conference": "Big 12", "line": 10.5, "over_odds": -220, "under_odds": 170,  "hold_pct": 5.8},
    "BYU":               {"conference": "Big 12", "line": 8.5,  "over_odds": -155, "under_odds": 130,  "hold_pct": 4.3},
    "Utah":              {"conference": "Big 12", "line": 8.5,  "over_odds": -135, "under_odds": 105,  "hold_pct": 6.2},
    "Kansas State":      {"conference": "Big 12", "line": 8.5,  "over_odds": 100,  "under_odds": -120, "hold_pct": 4.5},
    "Houston":           {"conference": "Big 12", "line": 8.5,  "over_odds": 120,  "under_odds": -145, "hold_pct": 4.6},
    "Arizona":           {"conference": "Big 12", "line": 7.5,  "over_odds": 110,  "under_odds": -135, "hold_pct": 5.1},
    "TCU":               {"conference": "Big 12", "line": 6.5,  "over_odds": -175, "under_odds": 145,  "hold_pct": 4.5},
    "Arizona State":     {"conference": "Big 12", "line": 6.5,  "over_odds": -120, "under_odds": 100,  "hold_pct": 4.5},
    "Oklahoma State":    {"conference": "Big 12", "line": 6.5,  "over_odds": 100,  "under_odds": -130, "hold_pct": 6.5},
    "Baylor":            {"conference": "Big 12", "line": 6.5,  "over_odds": 160,  "under_odds": -190, "hold_pct": 4.0},
    "West Virginia":     {"conference": "Big 12", "line": 5.5,  "over_odds": -175, "under_odds": 145,  "hold_pct": 4.5},
    "UCF":               {"conference": "Big 12", "line": 5.5,  "over_odds": -155, "under_odds": 130,  "hold_pct": 4.3},
    "Kansas":            {"conference": "Big 12", "line": 5.5,  "over_odds": -150, "under_odds": 125,  "hold_pct": 4.4},
    "Cincinnati":        {"conference": "Big 12", "line": 5.5,  "over_odds": 130,  "under_odds": -155, "hold_pct": 4.3},
    "Iowa State":        {"conference": "Big 12", "line": 4.5,  "over_odds": -145, "under_odds": 120,  "hold_pct": 4.6},
    "Colorado":          {"conference": "Big 12", "line": 4.5,  "over_odds": 125,  "under_odds": -150, "hold_pct": 4.4},

    "Georgia":           {"conference": "SEC", "line": 10.5, "over_odds": 140,  "under_odds": -165, "hold_pct": 3.9},
    "Texas":             {"conference": "SEC", "line": 9.5,  "over_odds": 115,  "under_odds": -140, "hold_pct": 4.8},
    "Alabama":           {"conference": "SEC", "line": 8.5,  "over_odds": -130, "under_odds": 110,  "hold_pct": 4.1},
    "LSU":               {"conference": "SEC", "line": 8.5,  "over_odds": -110, "under_odds": -118, "hold_pct": 6.5},
    "Texas A&M":         {"conference": "SEC", "line": 8.5,  "over_odds": 100,  "under_odds": -120, "hold_pct": 4.5},
    "Ole Miss":          {"conference": "SEC", "line": 8.5,  "over_odds": 130,  "under_odds": -155, "hold_pct": 4.3},
    "Oklahoma":          {"conference": "SEC", "line": 7.5,  "over_odds": -155, "under_odds": 130,  "hold_pct": 4.3},
    "Tennessee":         {"conference": "SEC", "line": 7.5,  "over_odds": -120, "under_odds": 100,  "hold_pct": 4.5},
    "Florida":           {"conference": "SEC", "line": 7.5,  "over_odds": 130,  "under_odds": -155, "hold_pct": 4.3},
    "Auburn":            {"conference": "SEC", "line": 6.5,  "over_odds": -125, "under_odds": 105,  "hold_pct": 4.3},
    "Missouri":          {"conference": "SEC", "line": 6.5,  "over_odds": -115, "under_odds": -105, "hold_pct": 4.7},
    "South Carolina":    {"conference": "SEC", "line": 6.5,  "over_odds": 110,  "under_odds": -135, "hold_pct": 5.1},
    "Vanderbilt":        {"conference": "SEC", "line": 5.5,  "over_odds": -145, "under_odds": 120,  "hold_pct": 4.6},
    "Kentucky":          {"conference": "SEC", "line": 4.5,  "over_odds": -155, "under_odds": 130,  "hold_pct": 4.3},
    "Mississippi State": {"conference": "SEC", "line": 4.5,  "over_odds": -120, "under_odds": 100,  "hold_pct": 4.5},
    "Arkansas":          {"conference": "SEC", "line": 3.5,  "over_odds": -155, "under_odds": 130,  "hold_pct": 4.3},
}

# Teams left in the pool once the draft ran out of rounds (9 rounds x 7
# drafters = 63 picks, leaving the 5 lowest lines on the board undrafted).
UNDRAFTED_TEAMS = ["Wake Forest", "Northwestern", "Iowa State", "Kentucky", "North Carolina"]

# The 63 picks in the exact order they happened (snake draft, odd rounds
# 1->7, even rounds 7->1). Mirrors the sheet's "Pick Order Log" tab.
PICKS = [
    (1, 1, "Nick", "Virginia Tech", "Over"),
    (2, 1, "Chase", "Notre Dame", "Under"),
    (3, 1, "John", "Michigan", "Under"),
    (4, 1, "Ben", "Penn State", "Under"),
    (5, 1, "Zach", "Florida", "Under"),
    (6, 1, "Charles", "Duke", "Over"),
    (7, 1, "Jason", "Utah", "Over"),
    (8, 2, "Jason", "Houston", "Over"),
    (9, 2, "Charles", "Florida State", "Under"),
    (10, 2, "Zach", "South Carolina", "Under"),
    (11, 2, "Ben", "Miami (FL)", "Under"),
    (12, 2, "John", "Oregon", "Over"),
    (13, 2, "Chase", "Ohio State", "Over"),
    (14, 2, "Nick", "West Virginia", "Over"),
    (15, 3, "Nick", "Virginia", "Over"),
    (16, 3, "Chase", "Clemson", "Over"),
    (17, 3, "John", "Maryland", "Over"),
    (18, 3, "Ben", "Alabama", "Over"),
    (19, 3, "Zach", "Washington", "Over"),
    (20, 3, "Charles", "NC State", "Over"),
    (21, 3, "Jason", "Georgia", "Over"),
    (22, 4, "Jason", "Texas", "Under"),
    (23, 4, "Charles", "BYU", "Over"),
    (24, 4, "Zach", "Nebraska", "Under"),
    (25, 4, "Ben", "Texas Tech", "Under"),
    (26, 4, "John", "Arkansas", "Over"),
    (27, 4, "Chase", "Texas A&M", "Under"),
    (28, 4, "Nick", "Minnesota", "Under"),
    (29, 5, "Nick", "Oklahoma", "Over"),
    (30, 5, "Chase", "Baylor", "Under"),
    (31, 5, "John", "Rutgers", "Over"),
    (32, 5, "Ben", "Louisville", "Under"),
    (33, 5, "Zach", "Oklahoma State", "Over"),
    (34, 5, "Charles", "LSU", "Under"),
    (35, 5, "Jason", "TCU", "Over"),
    (36, 6, "Jason", "Missouri", "Over"),
    (37, 6, "Charles", "Ole Miss", "Under"),
    (38, 6, "Zach", "Wisconsin", "Over"),
    (39, 6, "Ben", "SMU", "Under"),
    (40, 6, "John", "Illinois", "Under"),
    (41, 6, "Chase", "Kansas State", "Over"),
    (42, 6, "Nick", "Boston College", "Under"),
    (43, 7, "Nick", "California", "Over"),
    (44, 7, "Chase", "Iowa", "Over"),
    (45, 7, "John", "Pittsburgh", "Over"),
    (46, 7, "Ben", "Arizona", "Over"),
    (47, 7, "Zach", "UCF", "Over"),
    (48, 7, "Charles", "Mississippi State", "Under"),
    (49, 7, "Jason", "Arizona State", "Under"),
    (50, 8, "Jason", "Michigan State", "Over"),
    (51, 8, "Charles", "Colorado", "Under"),
    (52, 8, "Zach", "Georgia Tech", "Under"),
    (53, 8, "Ben", "Auburn", "Under"),
    (54, 8, "John", "Tennessee", "Under"),
    (55, 8, "Chase", "Vanderbilt", "Over"),
    (56, 8, "Nick", "Purdue", "Under"),
    (57, 9, "Nick", "Kansas", "Over"),
    (58, 9, "Chase", "Indiana", "Under"),
    (59, 9, "John", "USC", "Under"),
    (60, 9, "Ben", "Cincinnati", "Over"),
    (61, 9, "Zach", "UCLA", "Over"),
    (62, 9, "Charles", "Stanford", "Over"),
    (63, 9, "Jason", "Syracuse", "Under"),
]


def picks_with_team_info():
    """Flatten PICKS into one dict per pick, joined with TEAMS metadata."""
    rows = []
    for overall_pick, round_num, drafter, team, pick in PICKS:
        info = TEAMS[team]
        rows.append({
            "overall_pick": overall_pick,
            "round": round_num,
            "drafter": drafter,
            "team": team,
            "pick": pick,
            "conference": info["conference"],
            "line": info["line"],
            "over_odds": info["over_odds"],
            "under_odds": info["under_odds"],
            "hold_pct": info["hold_pct"],
        })
    return rows
