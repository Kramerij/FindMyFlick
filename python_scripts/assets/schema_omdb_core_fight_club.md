# OMDb Movie Schema (core fields)

Source: OMDb by title ('Fight Club', year '1999')

| Field path | Type | Sample value |
|---|---|---|
| `Actors` | `string` | "Brad Pitt, Edward Norton, Meat Loaf" |
| `Awards` | `string` | "Nominated for 1 Oscar. 12 wins & 38 nominations total" |
| `BoxOffice` | `string` | "$37,030,102" |
| `Country` | `string` | "United States, Germany" |
| `DVD` | `string` | "N/A" |
| `Director` | `string` | "David Fincher" |
| `Genre` | `string` | "Crime, Drama, Thriller" |
| `Language` | `string` | "English" |
| `Metascore` | `string` | "67" |
| `Plot` | `string` | "A nameless first person narrator (Edward Norton) attends support groups in attempt to subdue his emotional state and relieve his insomniac state. When he meets… |
| `Poster` | `string` | "https://m.media-amazon.com/images/M/MV5BOTgyOGQ1NDItNGU3Ny00MjU3LTg2YWEtNmEyYjBiMjI1Y2M5XkEyXkFqcGc@._V1_SX300.jpg" |
| `Production` | `string` | "N/A" |
| `Rated` | `string` | "R" |
| `Ratings` | `array` | [{"Source": "Internet Movie Database", "Value": "8.8/10"}] |
| `Ratings[0]` | `object` | {"Source": "Internet Movie Database", "Value": "8.8/10"} |
| `Ratings[0].Source` | `string` | "Internet Movie Database" |
| `Ratings[0].Value` | `string` | "8.8/10" |
| `Released` | `string` | "15 Oct 1999" |
| `Response` | `string` | "True" |
| `Runtime` | `string` | "139 min" |
| `Title` | `string` | "Fight Club" |
| `Type` | `string` | "movie" |
| `Website` | `string` | "N/A" |
| `Writer` | `string` | "Chuck Palahniuk, Jim Uhls" |
| `Year` | `string` | "1999" |
| `imdbID` | `string` | "tt0137523" |
| `imdbRating` | `string` | "8.8" |
| `imdbVotes` | `string` | "2,518,290" |

_Total unique paths: 28_