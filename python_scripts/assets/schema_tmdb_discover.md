# TMDB Discover (Movies) Schema

Source: TMDB /discover/movie • language=en-US, region=US, include_adult=false, sort_by=popularity.desc, page=1.

| Field path | Type | Sample value |
|---|---|---|
| `page` | `integer` | 1 |
| `results` | `array` | [{"adult": false, "backdrop_path": "/tLf5hjuO4gx62lVojPiHsIzCroh.jpg", "genre_ids": [53, 28], "id": 1025527, "original_language": "fr", "original_title": "Six j… |
| `results[0]` | `object` | {"adult": false, "backdrop_path": "/tLf5hjuO4gx62lVojPiHsIzCroh.jpg", "genre_ids": [53, 28], "id": 1025527, "original_language": "fr", "original_title": "Six jo… |
| `results[0].adult` | `boolean` | false |
| `results[0].backdrop_path` | `string` | "/tLf5hjuO4gx62lVojPiHsIzCroh.jpg" |
| `results[0].genre_ids` | `array` | [53] |
| `results[0].genre_ids[0]` | `integer` | 53 |
| `results[0].id` | `integer` | 1025527 |
| `results[0].original_language` | `string` | "fr" |
| `results[0].original_title` | `string` | "Six jours" |
| `results[0].overview` | `string` | "11 years ago, inspector Malik couldn’t solve a kidnapping case and a little girl died. Now with only a few days before the crime gets classified, he decides to… |
| `results[0].popularity` | `number` | 379.5005 |
| `results[0].poster_path` | `string` | "/1LMMSf17jD8bqvoLYC0qBJDWOBd.jpg" |
| `results[0].release_date` | `string` | "2024-12-11" |
| `results[0].title` | `string` | "Abyss" |
| `results[0].video` | `boolean` | false |
| `results[0].vote_average` | `number` | 6.066 |
| `results[0].vote_count` | `integer` | 53 |
| `total_pages` | `integer` | 53503 |
| `total_results` | `integer` | 1070051 |

_Total unique paths: 20_