using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json.Serialization;

namespace FindMyFlickWebsite.Server.Models
{
    // generated with copilot using the json schema that I previously created
    public class Movies
    {
        //generated with copilot using the json schema that I previously created
        private static readonly List<string> list = new List<string>();

        [JsonPropertyName("id")]
        public int ID { get; set; }

        [JsonPropertyName("Year")]
        public int Year { get; set; }

        [JsonPropertyName("summary")]
        public string? Summary { get; set; }

        [JsonPropertyName("user ratings")]
        public double UserRatings { get; set; }

        [JsonPropertyName("userWatchStatus")]
        public bool UserWatchStatus { get; set; }

        [JsonPropertyName("poster")]
        public string? Poster { get; set; }

        [JsonPropertyName("streaming services")]
        public List<string> StreamingServices { get; set; } = new List<string>();

        [JsonPropertyName("age rating")]
        public string? AgeRating { get; set; }

        [JsonPropertyName("name")]
        public string? Name { get; set; }

        [JsonPropertyName("genre")]
        public List<string> Genre { get; set; } = new List<string>();

        [JsonPropertyName("Tags")]
        public Tags Tags { get; set; } = new();

      
    }

    public class TagVote
    {
        [JsonPropertyName("tagID")]
        public int TagID { get; set; }

        [JsonPropertyName("upvotes")]
        public int Upvotes { get; set; }

        [JsonPropertyName("downvotes")]
        public int Downvotes { get; set; }
    }
}
