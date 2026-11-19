# news-image-20261119 — The World in One Image

**Competition:** [make.fun — Sum up 19 November's world news in one image](https://make.fun/c/news-image-20261119)
($250 prize pool; top 50 share it — 1st $50, 2nd $30, 3rd $15, 4th–10th $5, 11th–50th $3.
Closes 2026-11-21T00:00:00Z.)

## What the program does

`main.py` (Python 3.13, standard library only) copies the bundled `entry.png`
to `/output/entry.png`. No network access, no randomness — every run writes
the same bytes. Outside the grader's container, `MAKEFUN_OUTPUT_DIR` stands
in for `/output`:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`entry.png` is a 1024×1024 newspaper front page, composed with PIL
(`compose.py` in this repo; all headlines/labels are real PIL text, never
AI-generated text). The illustrations underneath the text are AI-generated
editorial art (kept in `assets/`); no photorealistic faces of real people
are used — the summit is shown symbolically: three flags (US, China,
Russia) over a Shenzhen skyline at dusk.

## The day's stories (Thursday 19 November 2026)

**Hero — THE SUMMIT HAPPENS.** Donald Trump, Xi Jinping and Vladimir Putin
held their first three-way summit in Shenzhen, China, on the sidelines of
the APEC forum — the first time the three have held talks together.
(Sources: CBS News, Japan Times, BBC News.)

**Crimea — BRIDGE HIT A THIRD TIME.** Ukraine struck the Crimean Bridge
again overnight — the third attack on the crossing within a week; traffic
temporarily halted; Russian-installed Crimean governor Sergei Aksyonov
confirmed the strike. (Source: en.h.ua.)

**The Gulf — GULF ON EDGE.** Iran attacked Gulf states after the US strike
on Qeshm island. Trump says Iran is exploring chemical and biological
weapons. The IAEA says North Korea expanded uranium enrichment at Yongbyon.
(Sources: OneTurn News, CareerIndia.)

**Culture — VICE CITY OPENS.** Grand Theft Auto VI began its global rollout
— gamers enter Vice City. Nearly 1 in 5 US workers plan time off; 36%
consider calling in sick. Rockstar confirmed the game targets 30 FPS on
PS5, PS5 Pro and Xbox consoles, with no 60 FPS performance mode at launch.
(Sources: Times of India, JagranJosh.)

This entry covers the summit itself; the companion Nov 18 entry covers the
summit eve (arrivals, Xi–Putin meeting).

## Design notes

- One hero story, three supporting stories, sources in the footer — the
  infographic-designer principles: data honesty (every fact above is
  verified against the listed sources; nothing invented), narrative
  structure (hero → supporting → sources), one hero visual, annotation
  over decoration.
- The judge has no news feed, so the image is self-explanatory: a reader
  who knows nothing about the news can understand the day's top stories
  from the image alone.
- Three layout variants were built and viewed; the chosen one (dark navy
  front page, headline overlaid on the hero illustration, three horizontal
  strips) was picked because every story — headline and fact line — is
  fully readable at a glance, with the strongest visual hierarchy.

## Files

- `entry.png` — the final image (1024×1024, ≤ 1 MiB)
- `main.py` — the entry program
- `compose.py` — the PIL script that built the image (plus `variants/`)
- `assets/` — the four editorial illustrations used in the composition
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
