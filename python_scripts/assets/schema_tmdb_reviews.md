# TMDB Reviews Schema

Source: TMDB /movie/{id}/reviews with id=550, language=en-US.

| Field path | Type | Sample value |
|---|---|---|
| `id` | `integer` | 550 |
| `page` | `integer` | 1 |
| `results` | `array` | [{"author": "Goddard", "author_details": {"name": "", "username": "Goddard", "avatar_path": null, "rating": null}, "content": "Pretty awesome movie.  It shows w… |
| `results[0]` | `object` | {"author": "Goddard", "author_details": {"name": "", "username": "Goddard", "avatar_path": null, "rating": null}, "content": "Pretty awesome movie.  It shows wh… |
| `results[0].author` | `string` | "Goddard" |
| `results[0].author_details` | `object` | {"name": "", "username": "Goddard", "avatar_path": null, "rating": null} |
| `results[0].author_details.avatar_path` | `null` | null |
| `results[0].author_details.name` | `string` | "" |
| `results[0].author_details.rating` | `null` | null |
| `results[0].author_details.username` | `string` | "Goddard" |
| `results[0].content` | `string` | "Pretty awesome movie.  It shows what one crazy person can convince other crazy people to do.  Everyone needs something to believe in.  I recommend Jesus Christ… |
| `results[0].created_at` | `string` | "2018-06-09T17:51:53.359Z" |
| `results[0].id` | `string` | "5b1c13b9c3a36848f2026384" |
| `results[0].updated_at` | `string` | "2021-06-23T15:58:09.421Z" |
| `results[0].url` | `string` | "https://www.themoviedb.org/review/5b1c13b9c3a36848f2026384" |
| `total_pages` | `integer` | 1 |
| `total_results` | `integer` | 10 |

_Total unique paths: 17_