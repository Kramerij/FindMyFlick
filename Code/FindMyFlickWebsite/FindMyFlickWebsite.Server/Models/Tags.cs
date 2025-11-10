using System.Text.Json.Serialization;

namespace FindMyFlickWebsite.Server.Models
{
    public class Tags
    {
        [JsonPropertyName("Plot tags")]
        public List<TagVote> PlotTags { get; set; } = [];

        [JsonPropertyName("Trigger tags")]
        public List<TagVote> TriggerTags { get; set; } = [];

        [JsonPropertyName("Person tags")]
        public List<TagVote> PersonTags { get; set; } = [];
    }
}
