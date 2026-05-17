#!/usr/bin/env python3
"""Regenerates the dynamic block in the profile README.

Runs daily via GitHub Actions. Updates the days-on-GitHub counter and
swaps in a seasonal / holiday line where applicable.
"""

from __future__ import annotations

import datetime as dt
import pathlib
import re

JOINED = dt.datetime(2021, 7, 7, 23, 47, 52, tzinfo=dt.timezone.utc)
NY_TZ = dt.timezone(dt.timedelta(hours=-4))

README = pathlib.Path("README.md")
START = "<!-- DYNAMIC:START -->"
END = "<!-- DYNAMIC:END -->"


def nth_weekday(year: int, month: int, weekday: int, n: int) -> dt.date:
    d = dt.date(year, month, 1)
    while d.weekday() != weekday:
        d += dt.timedelta(days=1)
    return d + dt.timedelta(weeks=n - 1)


def occasion(today: dt.date) -> str | None:
    y, m, d = today.year, today.month, today.day

    if (m, d) == (1, 1):
        return "🎆 New year, new ship list."
    if (m, d) == (2, 14):
        return "❤️ Shipping with love today."
    if (m, d) == (3, 14):
        return "🥧 Happy Pi Day — π ≈ 3.14159…"
    if (m, d) == (4, 1):
        return "🃏 No prank commits today, promise."
    if (m, d) == (5, 4):
        return "🛸 May the source be with you."
    if (m, d) == (6, 19):
        return "✊🏾 Juneteenth — reflecting today."
    if (m, d) == (7, 4):
        return "🇺🇸 Happy Fourth — fireworks > merge conflicts."
    if (m, d) == (7, 7):
        years = y - JOINED.year
        return f"🎩 {years} years on GitHub today — joined 2021-07-07."
    if (m, d) == (10, 31):
        return "🎃 Spooky season — only the bugs are scary."
    if today == nth_weekday(y, 11, 3, 4):
        return "🦃 Grateful for everyone shipping alongside me."
    if (m, d) == (12, 25):
        return "🎄 Merry Christmas — `git commit -m 'ho ho ho'`"
    if (m, d) == (12, 31):
        return "🥂 Wrapping the year — onto the next."

    # Hispanic Heritage Month: Sep 15 – Oct 15
    if (m, d) >= (9, 15) and (m, d) <= (10, 15):
        return "🇩🇴 Hispanic Heritage Month — building with pride."

    # Seasons (Northern Hemisphere, NY)
    if (m, d) >= (3, 20) and (m, d) < (6, 21):
        return "🌱 Spring sprint — building in bloom."
    if (m, d) >= (6, 21) and (m, d) < (9, 23):
        return "☀️ Summer ops — shipping under the sun."
    if (m, d) >= (9, 23) and (m, d) < (12, 21):
        return "🍂 Autumn cycles — pruning the tech debt."
    return "❄️ Winter sprints — keep the deploys warm."


def render() -> str:
    now = dt.datetime.now(NY_TZ)
    today = now.date()
    days = (now - JOINED.astimezone(NY_TZ)).days
    weeks, day_rem = divmod(days, 7)
    years = days // 365
    year_rem = days - years * 365
    line = occasion(today) or ""

    return (
        f"{START}\n"
        f"> {line}\n"
        f">\n"
        f"> 📅 **{days:,} days on GitHub** · {years} years, {year_rem} days · {weeks:,} weeks\n"
        f"> _Last updated: {today.isoformat()} (America/New_York)_\n"
        f"{END}"
    )


def main() -> int:
    text = README.read_text()
    block = render()
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if pattern.search(text):
        new_text = pattern.sub(block, text)
    else:
        new_text = text.rstrip() + "\n\n" + block + "\n"
    if new_text == text:
        print("no change")
        return 0
    README.write_text(new_text)
    print("updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
