using FindMyFlickWebsite.Server.Models;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;
using System.Xml.Linq;

namespace FindMyFlickWebsite.Server.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class MoviesController : ControllerBase
    {
        private readonly List<Movies> _movies;

        public MoviesController()
        {
            //will need to get movie list from api or db here. 

            //generated with copilot using the json schema and DTO 
            // Seed in-memory sample data matching the DTO shape
            _movies = new List<Movies>
            {
                new Movies
                {
                    ID = 123,
                    Name = "cool movie 1",
                    Summary = "long string",
                    UserRatings = 9.8,
                    UserWatchStatus = true,
                    Poster = "link",
                    StreamingServices = new List<string> {"hulu" },
                    Year = 2012,
                    AgeRating = "pg-13",
                    Genre = new List<string> { "action", "comedy" },
                    Tags = new Tags
                    {
                        PlotTags = new List<TagVote> { new TagVote { TagID = 8, Upvotes = 12, Downvotes = 2 } },
                        TriggerTags = new List<TagVote> { new TagVote { TagID = 1, Upvotes = 12, Downvotes = 2 } },
                        PersonTags = new List<TagVote> { new TagVote { TagID = 6, Upvotes = 12, Downvotes = 2 } }
                    }
                },
                new Movies{
                    ID = 3,
                    Name = "cool movie",
                    Summary = "long string",
                    UserRatings = 9.5,
                    UserWatchStatus = true,
                    Poster = "link",
                    StreamingServices = new List<string> { "netflix", "hulu" },
                    Year = 2011,
                    AgeRating = "pg-13",
                    Genre = new List<string> { "action", "comedy", "romance" },
                    Tags = new Tags
                    {
                        PlotTags = new List<TagVote> { new TagVote { TagID = 2, Upvotes = 12, Downvotes = 2 } },
                        TriggerTags = new List<TagVote> { new TagVote { TagID = 1, Upvotes = 12, Downvotes = 2 } },
                        PersonTags = new List<TagVote> { new TagVote { TagID = 4, Upvotes = 12, Downvotes = 2 } }
                    }
                }
            };


        }

        /// 
        /// Get all movies.
        /// 
        [HttpGet]
        [ProducesResponseType(typeof(IEnumerable<Movies>), 200)]
        public ActionResult<IEnumerable<Movies>> GetAll() =>
            Ok(_movies);




        /// <summary>
        /// Advanced search helper that filters a sequence of movies by various optional criteria.
        /// Any null or empty filter parameter is ignored.
        /// - name: substring match (case-insensitive)
        /// - streamingServices: match any (or all if matchAllStreaming true)
        /// - ageRating: exact case-insensitive match
        /// - genres: match any (or all if matchAllGenres true)
        /// - year: exact match
        /// - tagIds: tag id match across Plot/Trigger/Person tags (any or all via matchAllTags)
        /// 
        /// generated using copilot by asking for an advanced search method for the Movies class that filters by multiple optional criteria
        /// create an advanced search function for the movie class that can search via name, streaming services, age rating, genre, year, and tags
        /// </summary>
        public static IEnumerable<Movies> AdvancedSearch(
            IEnumerable<Movies> source,
            string? name = null,
            IEnumerable<string>? streamingServices = null,
            bool matchAllStreaming = false,
            string? ageRating = null,
            IEnumerable<string>? genres = null,
            bool matchAllGenres = false,
            int? year = null,
            IEnumerable<int>? tagIds = null,
            bool matchAllTags = false)
        {
            if (source == null) yield break;

            var svcList = streamingServices?.Where(s => !string.IsNullOrWhiteSpace(s)).ToList();
            var genreList = genres?.Where(g => !string.IsNullOrWhiteSpace(g)).ToList();
            var tagIdList = tagIds?.ToList();

            foreach (var m in source)
            {
                if (m == null) continue;

                // name (substring, case-insensitive)
                if (!string.IsNullOrWhiteSpace(name))
                {
                    if (string.IsNullOrWhiteSpace(m.Name) ||
                        !m.Name.Contains(name, StringComparison.OrdinalIgnoreCase))
                        continue;
                }

                // streaming services
                if (svcList != null && svcList.Any())
                {
                    var hasMatches = svcList.All(s => m.StreamingServices.Any(ms => string.Equals(ms, s, StringComparison.OrdinalIgnoreCase)))
                                     && matchAllStreaming
                        || (!matchAllStreaming && svcList.Any(s => m.StreamingServices.Any(ms => string.Equals(ms, s, StringComparison.OrdinalIgnoreCase))));

                    if (!hasMatches) continue;
                }

                // age rating (exact, case-insensitive)
                if (!string.IsNullOrWhiteSpace(ageRating))
                {
                    if (string.IsNullOrWhiteSpace(m.AgeRating) ||
                        !string.Equals(m.AgeRating, ageRating, StringComparison.OrdinalIgnoreCase))
                        continue;
                }

                // genres
                if (genreList != null && genreList.Any())
                {
                    var hasGenreMatches = matchAllGenres
                        ? genreList.All(g => m.Genre.Any(mg => string.Equals(mg, g, StringComparison.OrdinalIgnoreCase)))
                        : genreList.Any(g => m.Genre.Any(mg => string.Equals(mg, g, StringComparison.OrdinalIgnoreCase)));

                    if (!hasGenreMatches) continue;
                }

                // year
                if (year.HasValue && m.Year != year.Value) continue;

                // tags (check tag IDs across PlotTags, TriggerTags, PersonTags)
                if (tagIdList != null && tagIdList.Any())
                {
                    var movieTagIds = new HashSet<int>(
                        (m.Tags?.PlotTags ?? Enumerable.Empty<TagVote>()).Select(t => t.TagID)
                        .Concat((m.Tags?.TriggerTags ?? Enumerable.Empty<TagVote>()).Select(t => t.TagID))
                        .Concat((m.Tags?.PersonTags ?? Enumerable.Empty<TagVote>()).Select(t => t.TagID)));

                    var tagMatch = matchAllTags
                        ? tagIdList.All(id => movieTagIds.Contains(id))
                        : tagIdList.Any(id => movieTagIds.Contains(id));

                    if (!tagMatch) continue;
                }

                yield return m;
            }
        }

        /// 
        /// Get a single movie by id.
        /// 
        [HttpGet("{id:int}")]
        [ProducesResponseType(typeof(Movies), 200)]
        [ProducesResponseType(404)]
        public ActionResult<Movies> GetById(int id)
        {
            var movie = _movies.FirstOrDefault(m => m.ID == id);
            if (movie is null) return NotFound();
            return Ok(movie);
        }

        /// <summary>
        /// Search movies by multiple optional criteria.
        /// Query example:
        /// GET api/movies/search?name=cool&streamingServices=netflix&streamingServices=hulu&genres=action&year=2012&tagIds=1&matchAllTags=true
        /// 
        /// generate with copilot by asking for an advanced search endpoint for the MoviesController that uses the AdvancedSearch method
        /// use AdvancedSearch as an api get enpoint
        /// </summary>
        [HttpGet("search")]
        [ProducesResponseType(typeof(IEnumerable<Movies>), 200)]
        public ActionResult<IEnumerable<Movies>> Search(
            [FromQuery] string? name = null,
            [FromQuery] List<string>? streamingServices = null,
            [FromQuery] bool matchAllStreaming = false,
            [FromQuery] string? ageRating = null,
            [FromQuery] List<string>? genres = null,
            [FromQuery] bool matchAllGenres = false,
            [FromQuery] int? year = null,
            [FromQuery] List<int>? tagIds = null,
            [FromQuery] bool matchAllTags = false)
        {
            var results = AdvancedSearch(
                _movies,
                name,
                streamingServices,
                matchAllStreaming,
                ageRating,
                genres,
                matchAllGenres,
                year,
                tagIds,
                matchAllTags);

            return Ok(results);
        }
    }
}