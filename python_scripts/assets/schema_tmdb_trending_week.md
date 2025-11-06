# TMDB Trending (Movies, Week) Schema

Source: TMDB /trending/movie/week • language=en-US.

| Field path | Type | Sample value |
|---|---|---|
| `page` | `integer` | 1 |
| `results` | `array` | [{"adult": false, "backdrop_path": "/qwK9soQmmJ7kRdjLZVXblw3g7AQ.jpg", "id": 7451, "title": "xXx", "original_title": "xXx", "overview": "Xander Cage is your sta… |
| `results[0]` | `object` | {"adult": false, "backdrop_path": "/qwK9soQmmJ7kRdjLZVXblw3g7AQ.jpg", "id": 7451, "title": "xXx", "original_title": "xXx", "overview": "Xander Cage is your stan… |
| `results[0].adult` | `boolean` | false |
| `results[0].backdrop_path` | `string` | "/qwK9soQmmJ7kRdjLZVXblw3g7AQ.jpg" |
| `results[0].genre_ids` | `array` | [28] |
| `results[0].genre_ids[0]` | `integer` | 28 |
| `results[0].id` | `integer` | 7451 |
| `results[0].media_type` | `string` | "movie" |
| `results[0].original_language` | `string` | "en" |
| `results[0].original_title` | `string` | "xXx" |
| `results[0].overview` | `string` | "Xander Cage is your standard adrenaline junkie with no fear and a lousy attitude. When the US Government \"recruits\" him to go on a mission, he's not exactly … |
| `results[0].popularity` | `number` | 113.6971 |
| `results[0].poster_path` | `string` | "/xeEw3eLeSFmJgXZzmF2Efww0q3s.jpg" |
| `results[0].release_date` | `string` | "2002-08-09" |
| `results[0].title` | `string` | "xXx" |
| `results[0].video` | `boolean` | false |
| `results[0].vote_average` | `number` | 5.966 |
| `results[0].vote_count` | `integer` | 4620 |
| `total_pages` | `integer` | 500 |
| `total_results` | `integer` | 10000 |

_Total unique paths: 21_