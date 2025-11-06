# TMDB Recommendations Schema

Source: TMDB /movie/{id}/recommendations with id=550, language=en-US.

| Field path | Type | Sample value |
|---|---|---|
| `page` | `integer` | 1 |
| `results` | `array` | [{"adult": false, "backdrop_path": "/suaEOtk1N1sgg2MTM7oZd2cfVp3.jpg", "id": 680, "title": "Pulp Fiction", "original_title": "Pulp Fiction", "overview": "A burg… |
| `results[0]` | `object` | {"adult": false, "backdrop_path": "/suaEOtk1N1sgg2MTM7oZd2cfVp3.jpg", "id": 680, "title": "Pulp Fiction", "original_title": "Pulp Fiction", "overview": "A burge… |
| `results[0].adult` | `boolean` | false |
| `results[0].backdrop_path` | `string` | "/suaEOtk1N1sgg2MTM7oZd2cfVp3.jpg" |
| `results[0].genre_ids` | `array` | [53] |
| `results[0].genre_ids[0]` | `integer` | 53 |
| `results[0].id` | `integer` | 680 |
| `results[0].media_type` | `string` | "movie" |
| `results[0].original_language` | `string` | "en" |
| `results[0].original_title` | `string` | "Pulp Fiction" |
| `results[0].overview` | `string` | "A burger-loving hit man, his philosophical partner, a drug-addled gangster's moll and a washed-up boxer converge in this sprawling, comedic crime caper. Their … |
| `results[0].popularity` | `number` | 16.5319 |
| `results[0].poster_path` | `string` | "/vQWk5YBFWF4bZaofAbv0tShwBvQ.jpg" |
| `results[0].release_date` | `string` | "1994-09-10" |
| `results[0].title` | `string` | "Pulp Fiction" |
| `results[0].video` | `boolean` | false |
| `results[0].vote_average` | `number` | 8.487 |
| `results[0].vote_count` | `integer` | 29236 |
| `total_pages` | `integer` | 2 |
| `total_results` | `integer` | 40 |

_Total unique paths: 21_