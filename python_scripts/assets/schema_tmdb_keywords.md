# TMDB Movie Keywords Schema

Source: TMDB /movie/{id}/keywords with id=550 (keywords are language-agnostic)

| Field path | Type | Sample value |
|---|---|---|
| `id` | `integer` | 550 |
| `keywords` | `array` | [{"id": 851, "name": "dual identity"}] |
| `keywords[0]` | `object` | {"id": 851, "name": "dual identity"} |
| `keywords[0].id` | `integer` | 851 |
| `keywords[0].name` | `string` | "dual identity" |

_Total unique paths: 5_