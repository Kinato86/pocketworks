"""Generate public/<slug>.html for every project.

Plain static site, no build step required: the generated pages are committed.
Run this after editing PROJECTS below, then commit the output:

    python tools/build_projects.py
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"

PROJECTS = [
    {
        "slug": "mtg-journal",
        "name": "MTG Journal",
        "icon": "mtg-journal.png",
        "kicker": "Android app · Magic: The Gathering",
        "tagline": "A Commander life counter and game journal. One phone runs the whole table, and every finished game becomes history the playgroup can dig through.",
        "tags": ["React Native", "Expo", "Android", "Supabase"],
        "features": [
            ("One phone, whole table", "Life totals, commander damage, poison counters and eliminations for every seat, all on a single shared device passed around the table."),
            ("A journal, not just a counter", "When a game ends it is saved with players, commanders and result, so the group builds up a history instead of forgetting who won last month."),
            ("Analytics", "Win rates per player, per commander and per color identity, straight from the games you actually played."),
            ("Shared history", "Finished games are uploaded to a shared database the whole playgroup reads. Only the game in progress and games waiting to upload stay on the phone."),
        ],
        "under_the_hood": "Built with Expo and React Native on Android, pinned to the SDK the store version of Expo Go runs. Game history lives in Supabase; the live game is local so a dropped connection never interrupts play.",
    },
    {
        "slug": "magicscanner",
        "name": "MagicScanner",
        "icon": "magicscanner.png",
        "kicker": "Android app · Card collection",
        "tagline": "Point your camera at a Magic card and it is in your collection. Recognition runs on the phone, Scryfall fills in the details, and a local database keeps track of what you own.",
        "tags": ["React Native", "TypeScript", "Computer vision", "SQLite"],
        "features": [
            ("On-device recognition", "A perceptual-hash engine finds the card in the camera frame, straightens it and matches it against a bundled index. No cloud, no per-scan cost."),
            ("Set-agnostic matching", "The engine identifies the card name rather than the exact printing, which keeps the index small and the match forgiving of lighting and wear."),
            ("Scryfall for the details", "Once a name is recognised, Scryfall supplies the printing, price, oracle text and image."),
            ("Your collection stays yours", "Everything is stored in a local SQLite database, with JSON export and import, plus import of CSV exports from other scanner apps."),
            ("Deck recommendations", "A companion web app loads your export and asks Claude which cards from your own collection fit a deck you describe."),
        ],
        "under_the_hood": "The recognition engine is pure, dependency-free TypeScript shared between the Expo app and the tooling that builds the reference index from Scryfall. The web companion is a Next.js app that runs the Claude Agent SDK server-side so credentials never reach the browser.",
    },
    {
        "slug": "remind-me",
        "name": "Remind Me",
        "icon": "remind-me.png",
        "kicker": "Android app · Reminders",
        "tagline": "A reminders app that goes beyond “tomorrow at 9”: flexible recurrence, offline voice input, place-based triggers and reminders that wait for the right weather.",
        "tags": ["React Native", "Expo", "Offline-first", "TypeScript"],
        "features": [
            ("Recurrence that fits real life", "One-time, daily, every N days, weekly on any set of weekdays, every N weeks, monthly or yearly, with optional end dates and the ability to pause."),
            ("Voice input, fully offline", "Say “remind me every Monday at 9 to take out the trash”. On-device speech recognition and a local parser pre-fill the editor, and you confirm before saving."),
            ("Done and Snooze from the notification", "Notifications carry Done and Snooze actions and are scheduled over a rolling two-week horizon that rebuilds whenever data changes."),
            ("Place-based reminders", "Trigger a reminder when you arrive somewhere, using geofencing with an address search or your current location and a configurable radius."),
            ("Weather-gated reminders", "Limit a reminder to rain or snow expected today, a temperature threshold, or a dry spell of N days. Watering the garden resets the dry-spell counter."),
            ("Calendar and history", "A month view with per-day category dots, overdue tracking on the home screen, and a history of done, dismissed and missed occurrences."),
        ],
        "under_the_hood": "Expo and React Native with TypeScript. Forecasts come from Open-Meteo with no API key, evaluated by a periodic background task. All persistence goes through a small storage adapter interface so the backend can be swapped without touching the rest of the app.",
    },
    {
        "slug": "motivate",
        "name": "Motivate",
        "icon": "motivate.png",
        "kicker": "Android app · Habits and planning",
        "tagline": "Plan your week from reusable activity templates, check things off on a calendar, set weekly goals and earn badges for streaks and consistency.",
        "tags": ["React Native", "Expo", "TypeScript", "Local-first"],
        "features": [
            ("Activity library", "Around thirty seeded activities across music, sports, fitness, mind, creative, learning and lifestyle. Add your own with a custom icon and color."),
            ("Weekly templates", "Build a repeatable week out of activity blocks and apply it to any week in one tap. Editing an applied template asks whether to update pending activities too."),
            ("Calendar", "A week view to check off, edit or delete individual instances without touching the template, plus a month view with per-day activity dots."),
            ("Goals", "Several weekly goals at once: total hours, total activities, or hours and sessions for one specific activity, with optional weekly check-in reminders."),
            ("Achievements", "Twenty badges for streaks, hours, completions, variety, planning, early bird and night owl habits, and goal wins."),
            ("Nudges", "Local notifications before each activity with a configurable lead time."),
        ],
        "under_the_hood": "Expo and React Native with TypeScript. Everything is stored on the device behind a swappable storage adapter, so a backend can be added later without rewriting the app.",
    },
    {
        "slug": "boardgame-tester",
        "name": "Boardgame Tester",
        "icon": "boardgame-tester.svg",
        "kicker": "Simulation engine · Playtesting",
        "tagline": "A game-agnostic simulation engine for playtesting board games. Scripted players run thousands of games, and a dashboard shows who wins, where the points come from, and how rule variants shift the balance.",
        "tags": ["TypeScript", "Node.js", "Simulation", "Vite"],
        "features": [
            ("Thousands of games in minutes", "Seeded, reproducible runs across worker threads. Agents rotate seats between games so seat position and agent strength can be told apart."),
            ("A bench of agents", "Random, greedy one-ply lookahead, a Monte Carlo Tree Search agent with hidden-information determinisation, and game-specific heuristics."),
            ("Rule variants as flags", "Override any rule from the command line and label the run, then compare two runs side by side in the dashboard."),
            ("Every game recorded", "Each run writes an aggregate summary plus one record per game with every action, event and final board."),
            ("Play it yourself", "A browser version lets one person play District 44 against the same bots the simulator uses, with the bots running in a Web Worker."),
        ],
        "under_the_hood": "A pnpm monorepo in TypeScript. The engine knows nothing about a specific game; District 44, a city-building game by a board game designer, is the first game plugged in. The browser app is a static Vite site with no framework.",
    },
    {
        "slug": "camping-journal",
        "name": "Camping Journal",
        "icon": "camping-journal.svg",
        "kicker": "Android app · Dutch · Data project",
        "tagline": "A Dutch-language app built around a handwritten journal of 63 campsite visits. Every page was transcribed verbatim, nothing guessed, every doubt logged.",
        "tags": ["Android", "JavaScript", "SQLite", "MapLibre"],
        "features": [
            ("Sixty-three visits, fifty-nine campsites", "Photos of every handwritten page were transcribed word for word into one file per page, with the structured data pulled out alongside the full text."),
            ("Nothing guessed", "If a year, price or name was not on the page, the field stays empty. Two hundred and fifty uncertain points are logged and can be ticked off inside the app."),
            ("Rating dimensions counted, not invented", "The fifteen dimensions come from how often the journal itself talks about cycling, quiet, forest, space, walking, showers and so on, and that frequency sets their weight."),
            ("Suggestions with evidence", "The old text has no scores but clear verdicts. Those became 328 suggested ratings, each with its literal quote, to accept or reject one by one."),
            ("A sharp map", "Vector tiles from OpenFreeMap drawn by MapLibre, so labels stay crisp at any zoom. Addresses are geocoded through Nominatim, and a pin can be placed by hand when the journal has no street name."),
        ],
        "under_the_hood": "An Expo app with SQLite storage and a MapLibre GL map. The extraction pipeline lives next to the app, so the data can be re-derived from the page transcripts at any time.",
    },
    {
        "slug": "dnd-table",
        "name": "DnD Table",
        "icon": "dnd-table.svg",
        "kicker": "Local web app · Tabletop RPG",
        "tagline": "Run a D&D session where you sit at the table as GM or player and every other seat is an AI with its own personality.",
        "tags": ["TypeScript", "React", "Hono", "AI", "MCP"],
        "features": [
            ("Take any seat", "Be the game master with AI players, or be a player while an AI runs the game. Each AI seat has its own personality and only sees what that character would see."),
            ("More than one rule system", "D&D 5e SRD and Pathfinder 1e are each a single ruleset file, with character builders for both."),
            ("Scenarios from PDFs", "Drop an adventure's PDF into a scenario folder, ingest it, and the table plays through it. Or pick freeform play with no scenario at all."),
            ("Hear the table", "Speech reads the table aloud and music sets the scene, so a session feels like a session rather than a chat log."),
            ("Claude Code as the brain", "An MCP server lets Claude Code dispatch each AI seat to its own subagent, with no configuration beyond starting it in the repo."),
        ],
        "under_the_hood": "A pnpm workspace: a game engine package with no HTTP, a shared API contract, a Hono server with SQLite and server-sent events, a React and Vite frontend, and a stdio MCP server. The server binds to localhost only, since nothing in the API authenticates.",
    },
    {
        "slug": "score-keeper",
        "name": "Score Keeper",
        "icon": "score-keeper.png",
        "kicker": "Android app · Office games",
        "tagline": "Keeps score for the games we play at work and turns the results into per-sport Elo leaderboards, team standings and head-to-head rivalries.",
        "tags": ["React Native", "Expo", "Android", "SQLite"],
        "features": [
            ("Five sports and counting", "Table tennis including round-the-table, fussball, jeu de boules, shuffleboard, and darts in 301, 501 and Tactics."),
            ("Only finished games count", "Record a match after it is over: sport, who stood on each side, what it was played to, and the score. An impossible score is refused with a reason."),
            ("Leaderboards", "A per-sport Elo rating, doubles and triples pairings, and rivalries with the full head-to-head record."),
            ("History", "Every match is listed and can be opened for details, a note, or deletion."),
        ],
        "under_the_hood": "Expo and React Native, local-only on Android with SQLite. The rating and validation logic is pure TypeScript tested with Vitest, and the database layer runs its tests on Node's own SQLite.",
    },
]

HEADER = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{name} — Pocketworks</title>
  <meta name="description" content="{description}">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/styles.css">
  <script>
    try {{
      var t = localStorage.getItem('theme');
      if (t === 'light' || t === 'dark') document.documentElement.setAttribute('data-theme', t);
    }} catch (e) {{}}
  </script>
  <meta property="og:title" content="{name} — Pocketworks">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="https://pocketworks.dev/{slug}">
  <meta property="og:image" content="https://pocketworks.dev/projects/{icon}">
  <meta property="og:type" content="article">
</head>
<body>
  <header class="site-header">
    <nav class="wrap">
      <a class="brand" href="/">pocketworks<span class="accent">.dev</span></a>
      <div class="nav-right">
        <div class="nav-links">
          <a href="/#projects">Projects</a>
          <a href="/#about">About</a>
          <a href="/#contact">Contact</a>
        </div>
        <button class="theme-toggle" type="button" aria-label="Switch to light theme" title="Toggle theme">
          <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>
          <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3a7 7 0 0 0 9.79 9.79z"/></svg>
        </button>
      </div>
    </nav>
  </header>
"""

FOOTER = """
  <footer class="site-footer">
    <div class="wrap">
      <p>© <span id="year">2026</span> Paul van Dronkelaar · pocketworks.dev</p>
    </div>
  </footer>

  <script>
    document.getElementById('year').textContent = new Date().getFullYear();

    (function () {
      var root = document.documentElement;
      var btn = document.querySelector('.theme-toggle');
      var mq = window.matchMedia('(prefers-color-scheme: light)');

      function current() {
        var t = root.getAttribute('data-theme');
        if (t === 'light' || t === 'dark') return t;
        return mq.matches ? 'light' : 'dark';
      }

      function updateLabel() {
        var next = current() === 'dark' ? 'light' : 'dark';
        btn.setAttribute('aria-label', 'Switch to ' + next + ' theme');
      }

      btn.addEventListener('click', function () {
        var next = current() === 'dark' ? 'light' : 'dark';
        root.setAttribute('data-theme', next);
        try { localStorage.setItem('theme', next); } catch (e) {}
        updateLabel();
      });

      mq.addEventListener('change', updateLabel);
      updateLabel();
    })();
  </script>
</body>
</html>
"""


def render(p, prev, nxt):
    e = escape
    tags = "".join(f"<span>{e(t)}</span>" for t in p["tags"])
    features = "\n".join(
        f"        <li><strong>{e(title)}</strong>{e(text)}</li>" for title, text in p["features"]
    )
    body = f"""
  <main>
    <section class="hero wrap project-hero">
      <a class="back-link" href="/#projects">&larr; All projects</a>
      <div class="project-head">
        <img class="project-icon" src="/projects/{p['icon']}" alt="{e(p['name'])} icon" width="96" height="96">
        <div>
          <p class="kicker">{e(p['kicker'])}</p>
          <h1>{e(p['name'])}</h1>
        </div>
      </div>
      <p class="lede">{e(p['tagline'])}</p>
      <p class="tags">{tags}</p>
    </section>

    <section class="wrap">
      <h2>What it does</h2>
      <ul class="feature-list">
{features}
      </ul>
    </section>

    <section class="wrap">
      <h2>Under the hood</h2>
      <p>{e(p['under_the_hood'])}</p>
    </section>

    <section class="wrap project-nav">
      <a class="prev" href="/{prev['slug']}"><small>Previous project</small>{e(prev['name'])}</a>
      <a class="next" href="/{nxt['slug']}"><small>Next project</small>{e(nxt['name'])}</a>
    </section>
  </main>
"""
    head = HEADER.format(
        name=e(p["name"]), slug=p["slug"], icon=p["icon"], description=e(p["tagline"])
    )
    return head + body + FOOTER


def main():
    n = len(PROJECTS)
    for i, p in enumerate(PROJECTS):
        prev, nxt = PROJECTS[(i - 1) % n], PROJECTS[(i + 1) % n]
        out = PUBLIC / f"{p['slug']}.html"
        out.write_text(render(p, prev, nxt), encoding="utf-8", newline="\n")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
