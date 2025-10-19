# TMDB Movie Core Schema

Source: TMDB /movie/{id} with id=550 (fields listed below are from this single endpoint response)

| Field path | Type | Sample value |
|---|---|---|
| `adult` | `boolean` | false |
| `backdrop_path` | `string` | "/5TiwfWEaPSwD20uwXjCTUqpQX70.jpg" |
| `belongs_to_collection` | `null` | null |
| `budget` | `integer` | 63000000 |
| `genres` | `array` | [{"id": 18, "name": "Drama"}] |
| `genres[0]` | `object` | {"id": 18, "name": "Drama"} |
| `genres[0].id` | `integer` | 18 |
| `genres[0].name` | `string` | "Drama" |
| `homepage` | `string` | "http://www.foxmovies.com/movies/fight-club" |
| `id` | `integer` | 550 |
| `imdb_id` | `string` | "tt0137523" |
| `origin_country` | `array` | ["US"] |
| `origin_country[0]` | `string` | "US" |
| `original_language` | `string` | "en" |
| `original_title` | `string` | "Fight Club" |
| `overview` | `string` | "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with u… |
| `popularity` | `number` | 20.0618 |
| `poster_path` | `string` | "/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg" |
| `production_companies` | `array` | [{"id": 711, "logo_path": "/tEiIH5QesdheJmDAqQwvtN60727.png", "name": "Fox 2000 Pictures", "origin_country": "US"}] |
| `production_companies[0]` | `object` | {"id": 711, "logo_path": "/tEiIH5QesdheJmDAqQwvtN60727.png", "name": "Fox 2000 Pictures", "origin_country": "US"} |
| `production_companies[0].id` | `integer` | 711 |
| `production_companies[0].logo_path` | `string` | "/tEiIH5QesdheJmDAqQwvtN60727.png" |
| `production_companies[0].name` | `string` | "Fox 2000 Pictures" |
| `production_companies[0].origin_country` | `string` | "US" |
| `production_countries` | `array` | [{"iso_3166_1": "DE", "name": "Germany"}] |
| `production_countries[0]` | `object` | {"iso_3166_1": "DE", "name": "Germany"} |
| `production_countries[0].iso_3166_1` | `string` | "DE" |
| `production_countries[0].name` | `string` | "Germany" |
| `release_date` | `string` | "1999-10-15" |
| `revenue` | `integer` | 100853753 |
| `runtime` | `integer` | 139 |
| `spoken_languages` | `array` | [{"english_name": "English", "iso_639_1": "en", "name": "English"}] |
| `spoken_languages[0]` | `object` | {"english_name": "English", "iso_639_1": "en", "name": "English"} |
| `spoken_languages[0].english_name` | `string` | "English" |
| `spoken_languages[0].iso_639_1` | `string` | "en" |
| `spoken_languages[0].name` | `string` | "English" |
| `status` | `string` | "Released" |
| `tagline` | `string` | "Mischief. Mayhem. Soap." |
| `title` | `string` | "Fight Club" |
| `video` | `boolean` | false |
| `vote_average` | `number` | 8.438 |
| `vote_count` | `integer` | 30881 |

_Total unique paths: 42_