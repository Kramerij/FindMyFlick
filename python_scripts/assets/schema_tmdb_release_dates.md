# TMDB Release Dates (US Region)

Source: TMDB /movie/{id}/release_dates for id=550 (restricted to region=US)

| Field path | Type | Sample value |
|---|---|---|
| `iso_3166_1` | `string` | "US" |
| `release_dates` | `array` | [{"certification": "", "descriptors": [], "iso_639_1": "", "note": "CMJ Film Festival", "release_date": "1999-09-21T00:00:00.000Z", "type": 1}] |
| `release_dates[0]` | `object` | {"certification": "", "descriptors": [], "iso_639_1": "", "note": "CMJ Film Festival", "release_date": "1999-09-21T00:00:00.000Z", "type": 1} |
| `release_dates[0].certification` | `string` | "" |
| `release_dates[0].descriptors` | `array` | [] |
| `release_dates[0].iso_639_1` | `string` | "" |
| `release_dates[0].note` | `string` | "CMJ Film Festival" |
| `release_dates[0].release_date` | `string` | "1999-09-21T00:00:00.000Z" |
| `release_dates[0].type` | `integer` | 1 |

_Total unique paths: 9_