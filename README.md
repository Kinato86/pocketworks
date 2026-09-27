# pocketworks.dev

Personal developer site of Paul van Dronkelaar — projects, experiments, and notes.

Plain static HTML/CSS, no build step. Everything served lives in [`public/`](public/).

## Local preview

Any static file server works, e.g.:

```sh
npx serve public
# or
python3 -m http.server -d public 8000
```

## Deploying to Cloudflare

Two options — pick one:

### Option A: Git integration (recommended)

1. In the [Cloudflare dashboard](https://dash.cloudflare.com), go to
   **Workers & Pages → Create → Pages → Connect to Git** and select
   `Kinato86/pocketworks`.
2. Build settings: no build command, output directory `public`.
3. Every push to `main` deploys automatically.
4. Under the project's **Custom domains**, add `pocketworks.dev`
   (the domain must be on your Cloudflare account; DNS is set up for you).

### Option B: Wrangler CLI

The repo includes a [`wrangler.jsonc`](wrangler.jsonc) that serves `public/`
as static assets on Workers:

```sh
npx wrangler login   # first time only
npx wrangler deploy
```

Then add `pocketworks.dev` as a custom domain to the `pocketworks-dev`
Worker in the dashboard (Worker → Settings → Domains & Routes).

## Structure

```
public/
  index.html        # the home page
  <project>.html    # one page per project, served at /<project> (generated)
  projects/         # project icons
  styles.css        # all styling (dark/light via OS preference or header toggle)
  404.html          # not-found page
  favicon.svg
tools/
  build_projects.py # regenerates the project pages from the data at the top of the file
wrangler.jsonc      # optional CLI deploy config
```

## Project pages

Each project card links to `/<slug>`. Those pages share one template, so they are
generated rather than hand-edited: change the project data in
[`tools/build_projects.py`](tools/build_projects.py), run
`python tools/build_projects.py`, and commit the regenerated HTML. Cloudflare
serves `public/<slug>.html` at `/<slug>` and redirects the `.html` and
trailing-slash forms to the clean URL.

Preview the clean URLs locally with `npx wrangler dev` (no login needed); a
plain static server only knows the `.html` paths.
