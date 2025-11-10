
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
                    Name = "cool movie",
                    Summary = "long string",
                    UserRatings = 9.8,
                    UserWatchStatus = true,
                    Poster = "link",
                    StreamingServices = new List<string> { "netflix", "hulu" },
                    Year = 2012,
                    AgeRating = "pg-13",
                    Genre = new List<string> { "action", "comedy" },
                    Tags = new Tags
                    {
                        PlotTags = new List<TagVote> { new TagVote { TagID = 1, Upvotes = 12, Downvotes = 2 } },
                        TriggerTags = new List<TagVote> { new TagVote { TagID = 1, Upvotes = 12, Downvotes = 2 } },
                        PersonTags = new List<TagVote> { new TagVote { TagID = 1, Upvotes = 12, Downvotes = 2 } }
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
                        PlotTags = new List<TagVote> { new TagVote { TagID = 1, Upvotes = 12, Downvotes = 2 } },
                        TriggerTags = new List<TagVote> { new TagVote { TagID = 1, Upvotes = 12, Downvotes = 2 } },
                        PersonTags = new List<TagVote> { new TagVote { TagID = 1, Upvotes = 12, Downvotes = 2 } }
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
    }
}