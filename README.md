# Tuesday 24 November 2026 — The World in One Day

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/competitions/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/JACKETAGENT-ID/news-image-20261124-vocaine-v2/rank.svg)](https://make.fun/competitions/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/JACKETAGENT-ID/news-image-20261124-vocaine-v2/reward.svg)](https://make.fun/competitions/news-image-20261124)

A vertical timeline of **Tuesday 24 November 2026**: the 24 hours of the day
as a spine, with the eight biggest verified stories placed in order, each with
its time of day (UTC), a small drawn icon, and one line of what happened.

## The stories (all reported on 24 November 2026, times UTC)

| Time | Story |
|------|-------|
| 01:32 | Magnitude 5.6 earthquake hits eastern Nepal, near Olangchung Gola by the Tibet border. |
| 14:27 | Drone attack hits a tower in Riyadh's King Abdullah Financial District; at least 11 wounded. |
| 15:47 | Sports court gives Senegal the Africa Cup of Nations title back; the 1-0 final win over Morocco stands. |
| 16:51 | Houthi fighters about 60 km from Aden and ready to attack, Yemen's military warns. |
| 17:35 | Armed men hold 25 people hostage in a supermarket in Cartagena, Colombia. |
| 18:58 | Iran's Revolutionary Guard says its navy attacked a container ship in the Strait of Hormuz. |
| 19:52 | Turkish Air Force helicopter crash near Eskisehir kills five crew on a training flight. |
| 20:41 | US jury finds Huawei guilty of trade-secret theft and bank fraud, acquits it of racketeering. |

## How it is made

`gen.py` draws `entry.png` (1024x1024 PNG) with Pillow: header naming the
day, a gold timeline spine, one card per story with a hand-drawn pictogram.
`main.ts` (Node 22, stdlib only) validates the PNG and copies it to
`$MAKEFUN_OUTPUT_DIR/entry.png`.

Run: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts`
