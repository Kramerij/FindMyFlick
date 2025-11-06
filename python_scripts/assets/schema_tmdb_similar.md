# TMDB Similar Titles Schema

Source: TMDB /movie/{id}/similar with id=550, language=en-US.

| Field path | Type | Sample value |
|---|---|---|
| `page` | `integer` | 1 |
| `results` | `array` | [{"adult": false, "backdrop_path": "/f37C7qRjHWglB1Yy9f15v0hCdpb.jpg", "genre_ids": [18], "id": 263916, "original_language": "en", "original_title": "The Tower … |
| `results[0]` | `object` | {"adult": false, "backdrop_path": "/f37C7qRjHWglB1Yy9f15v0hCdpb.jpg", "genre_ids": [18], "id": 263916, "original_language": "en", "original_title": "The Tower o… |
| `results[0].adult` | `boolean` | false |
| `results[0].backdrop_path` | `string` | "/f37C7qRjHWglB1Yy9f15v0hCdpb.jpg" |
| `results[0].genre_ids` | `array` | [18] |
| `results[0].genre_ids[0]` | `integer` | 18 |
| `results[0].id` | `integer` | 263916 |
| `results[0].original_language` | `string` | "en" |
| `results[0].original_title` | `string` | "The Tower of Lies" |
| `results[0].overview` | `string` | "After his beloved daughter leaves for the city to pay off his debt, an old farmer goes mad when her letters become less frequent and it is suspected she may be… |
| `results[0].popularity` | `number` | 2.8443 |
| `results[0].poster_path` | `string` | "/e4lgQqdtGlaFJ4xzQmtZfmacglr.jpg" |
| `results[0].release_date` | `string` | "1925-10-10" |
| `results[0].title` | `string` | "The Tower of Lies" |
| `results[0].video` | `boolean` | false |
| `results[0].vote_average` | `number` | 0.0 |
| `results[0].vote_count` | `integer` | 0 |
| `total_pages` | `integer` | 15641 |
| `total_results` | `integer` | 312814 |

_Total unique paths: 20_