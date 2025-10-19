# TMDB Watch Providers (US) — Filtered Schema

Source: TMDB /movie/{id}/watch/providers with id=550, region=US. Only `flatrate` (subscription) and `ads` (free with ads) providers are included; `rent` and `buy` are excluded.

| Field path | Type | Sample value |
|---|---|---|
| `ads` | `array` | [] |
| `flatrate` | `array` | [{"logo_path": "/9BgaNQRMDvVlji1JBZi6tcfxpKx.jpg", "provider_id": 257, "provider_name": "fuboTV", "display_priority": 10}] |
| `flatrate[0]` | `object` | {"logo_path": "/9BgaNQRMDvVlji1JBZi6tcfxpKx.jpg", "provider_id": 257, "provider_name": "fuboTV", "display_priority": 10} |
| `flatrate[0].display_priority` | `integer` | 10 |
| `flatrate[0].logo_path` | `string` | "/9BgaNQRMDvVlji1JBZi6tcfxpKx.jpg" |
| `flatrate[0].provider_id` | `integer` | 257 |
| `flatrate[0].provider_name` | `string` | "fuboTV" |
| `link` | `string` | "https://www.themoviedb.org/movie/550-fight-club/watch?locale=US" |

_Total unique paths: 8_