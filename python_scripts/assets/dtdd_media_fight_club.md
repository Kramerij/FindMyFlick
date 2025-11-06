# DTDD Media Schema

Source: /dddsearch?q='Fight Club' → /media/9593

| Field path | Type | Sample value |
|---|---|---|
| `allGroups` | `array` | [{"name": "Your Triggers", "topics": [{"topicItemId": 378845, "newsletterDate": null, "yesSum": 3, "noSum": 111, "numComments": 1, "TopicId": 153, "ItemId": 959… |
| `allGroups[0]` | `object` | {"name": "Your Triggers", "topics": [{"topicItemId": 378845, "newsletterDate": null, "yesSum": 3, "noSum": 111, "numComments": 1, "TopicId": 153, "ItemId": 9593… |
| `allGroups[0].name` | `string` | "Your Triggers" |
| `allGroups[0].topics` | `array` | [{"topicItemId": 378845, "newsletterDate": null, "yesSum": 3, "noSum": 111, "numComments": 1, "TopicId": 153, "ItemId": 9593, "RatingId": 7458752, "commentUserI… |
| `allGroups[0].topics[0]` | `object` | {"topicItemId": 378845, "newsletterDate": null, "yesSum": 3, "noSum": 111, "numComments": 1, "TopicId": 153, "ItemId": 9593, "RatingId": 7458752, "commentUserId… |
| `allGroups[0].topics[0].ItemId` | `integer` | 9593 |
| `allGroups[0].topics[0].RatingId` | `integer` | 7458752 |
| `allGroups[0].topics[0].TopicCategory` | `object` | {"id": 2, "name": "Animal", "createdAt": "2020-04-03T12:22:40.000Z", "updatedAt": "2020-04-03T12:22:40.000Z"} |
| `allGroups[0].topics[0].TopicCategory.createdAt` | `string` | "2020-04-03T12:22:40.000Z" |
| `allGroups[0].topics[0].TopicCategory.id` | `integer` | 2 |
| `allGroups[0].topics[0].TopicCategory.name` | `string` | "Animal" |
| `allGroups[0].topics[0].TopicCategory.updatedAt` | `string` | "2020-04-03T12:22:40.000Z" |
| `allGroups[0].topics[0].TopicId` | `integer` | 153 |
| `allGroups[0].topics[0].UserId` | `integer` | 133193 |
| `allGroups[0].topics[0].comment` | `string` | "There are no dogs in the movie :)" |
| `allGroups[0].topics[0].commentUserIds` | `string` | "133193" |
| `allGroups[0].topics[0].comments` | `array` | [{"id": 7458752, "voteSum": 12, "comment": "There are no dogs in the movie :)", "index1": -1, "index2": -1, "User": {"id": 133193, "displayName": "Hamarhemmo"}}… |
| `allGroups[0].topics[0].comments[0]` | `object` | {"id": 7458752, "voteSum": 12, "comment": "There are no dogs in the movie :)", "index1": -1, "index2": -1, "User": {"id": 133193, "displayName": "Hamarhemmo"}} |
| `allGroups[0].topics[0].comments[0].User` | `object` | {"id": 133193, "displayName": "Hamarhemmo"} |
| `allGroups[0].topics[0].comments[0].User.displayName` | `string` | "Hamarhemmo" |
| `allGroups[0].topics[0].comments[0].User.id` | `integer` | 133193 |
| `allGroups[0].topics[0].comments[0].comment` | `string` | "There are no dogs in the movie :)" |
| `allGroups[0].topics[0].comments[0].id` | `integer` | 7458752 |
| `allGroups[0].topics[0].comments[0].index1` | `integer` | -1 |
| `allGroups[0].topics[0].comments[0].index2` | `integer` | -1 |
| `allGroups[0].topics[0].comments[0].voteSum` | `integer` | 12 |
| `allGroups[0].topics[0].doesName` | `string` | "Does the dog die" |
| `allGroups[0].topics[0].hasUserComment` | `boolean` | false |
| `allGroups[0].topics[0].index1` | `integer` | -1 |
| `allGroups[0].topics[0].index2` | `integer` | -1 |
| `allGroups[0].topics[0].isAnonymous` | `integer` | 0 |
| `allGroups[0].topics[0].isFavorite` | `boolean` | true |
| `allGroups[0].topics[0].itemBackgroundImage` | `string` | "hZkgoQYus5vegHoetLkCJzb17zJ.jpg" |
| `allGroups[0].topics[0].itemCleanName` | `string` | "fight club" |
| `allGroups[0].topics[0].itemId` | `null` | null |
| `allGroups[0].topics[0].itemName` | `string` | "Fight Club" |
| `allGroups[0].topics[0].itemPosterImage` | `string` | "jSziioSwPVrOy9Yow3XhWIBDjq1.jpg" |
| `allGroups[0].topics[0].itemTypeId` | `integer` | 15 |
| `allGroups[0].topics[0].itemTypeIndex1` | `null` | null |
| `allGroups[0].topics[0].itemTypeIndex2` | `null` | null |
| `allGroups[0].topics[0].itemTypeName` | `string` | "Movie" |
| `allGroups[0].topics[0].itemTypeSlug` | `string` | "movies" |
| `allGroups[0].topics[0].newsletterDate` | `null` | null |
| `allGroups[0].topics[0].noSum` | `integer` | 111 |
| `allGroups[0].topics[0].numComments` | `integer` | 1 |
| `allGroups[0].topics[0].ratingIndex1` | `integer` | -1 |
| `allGroups[0].topics[0].ratingIndex2` | `integer` | -1 |
| `allGroups[0].topics[0].releaseYear` | `string` | "1999" |
| `allGroups[0].topics[0].slug` | `string` | "does-the-dog-die" |
| `allGroups[0].topics[0].topic` | `object` | {"id": 153, "name": "a dog dies", "notName": "no dogs die", "survivesName": "the dog survives", "keywords": "Dog death, canine death, pet dog death, puppy dies"… |
| `allGroups[0].topics[0].topic.TopicCategory` | `object` | {"id": 2, "name": "Animal", "createdAt": "2020-04-03T12:22:40.000Z", "updatedAt": "2020-04-03T12:22:40.000Z"} |
| `allGroups[0].topics[0].topic.TopicCategory.createdAt` | `string` | "2020-04-03T12:22:40.000Z" |
| `allGroups[0].topics[0].topic.TopicCategory.id` | `integer` | 2 |
| `allGroups[0].topics[0].topic.TopicCategory.name` | `string` | "Animal" |
| `allGroups[0].topics[0].topic.TopicCategory.updatedAt` | `string` | "2020-04-03T12:22:40.000Z" |
| `allGroups[0].topics[0].topic.TopicCategoryId` | `integer` | 2 |
| `allGroups[0].topics[0].topic.createdAt` | `string` | "2017-06-22T18:20:34.000Z" |
| `allGroups[0].topics[0].topic.demandOrder` | `integer` | 1 |
| `allGroups[0].topics[0].topic.description` | `string` | "This trigger is for people who are upset by the death of a canine companion. Dogs are often portrayed as loyal friends in films, and their death can be very tr… |
| `allGroups[0].topics[0].topic.doesName` | `string` | "Does the dog die" |
| `allGroups[0].topics[0].topic.id` | `integer` | 153 |
| `allGroups[0].topics[0].topic.image` | `string` | "dog" |
| `allGroups[0].topics[0].topic.isSensitive` | `boolean` | false |
| `allGroups[0].topics[0].topic.isSpoiler` | `boolean` | false |
| `allGroups[0].topics[0].topic.isVisible` | `boolean` | true |
| `allGroups[0].topics[0].topic.keywords` | `string` | "Dog death, canine death, pet dog death, puppy dies" |
| `allGroups[0].topics[0].topic.legacyId` | `integer` | 25 |
| `allGroups[0].topics[0].topic.listName` | `string` | "where the dog dies" |
| `allGroups[0].topics[0].topic.name` | `string` | "a dog dies" |
| `allGroups[0].topics[0].topic.notName` | `string` | "no dogs die" |
| `allGroups[0].topics[0].topic.ordering` | `integer` | 100 |
| `allGroups[0].topics[0].topic.smmwDescription` | `string` | "dogs dying" |
| `allGroups[0].topics[0].topic.subtitle` | `string` | "" |
| `allGroups[0].topics[0].topic.subtitleText` | `null` | null |
| `allGroups[0].topics[0].topic.subtitleUrl` | `null` | null |
| `allGroups[0].topics[0].topic.supporters` | `integer` | 1 |
| `allGroups[0].topics[0].topic.survivesName` | `string` | "the dog survives" |
| `allGroups[0].topics[0].topic.updatedAt` | `string` | "2024-07-30T20:37:08.000Z" |
| `allGroups[0].topics[0].topicItemId` | `integer` | 378845 |
| `allGroups[0].topics[0].username` | `string` | "Hamarhemmo" |
| `allGroups[0].topics[0].voteSum` | `integer` | 12 |
| `allGroups[0].topics[0].yesSum` | `integer` | 3 |
| `index1` | `integer` | -1 |
| `index2` | `integer` | -1 |
| `item` | `object` | {"id": 9593, "name": "Fight Club", "cleanName": "fight club", "cleanNameArticles": "fight club", "altName": null, "genre": "drama", "releaseYear": "1999", "lega… |
| `item.ItemTypeId` | `integer` | 15 |
| `item.UserId` | `integer` | 12972 |
| `item.adult` | `boolean` | false |
| `item.altName` | `null` | null |
| `item.art` | `null` | null |
| `item.backgroundImage` | `string` | "hZkgoQYus5vegHoetLkCJzb17zJ.jpg" |
| `item.backgroundVerified` | `boolean` | true |
| `item.cleanName` | `string` | "fight club" |
| `item.cleanNameArticles` | `string` | "fight club" |
| `item.createdAt` | `string` | "2017-06-22T18:20:34.000Z" |
| `item.genre` | `string` | "drama" |
| `item.id` | `integer` | 9593 |
| `item.imdbId` | `string` | "tt0137523" |
| `item.isPurchased` | `boolean` | false |
| `item.itemType` | `object` | {"id": 15, "name": "Movie", "picture": "clapperboard", "slug": "movies", "verb": "watch", "pastTenseVerb": "watched", "index1": null, "index2": null, "position1… |
| `item.itemType.createdAt` | `string` | "2019-02-19T13:02:35.000Z" |
| `item.itemType.id` | `integer` | 15 |
| `item.itemType.index1` | `null` | null |
| `item.itemType.index2` | `null` | null |
| `item.itemType.name` | `string` | "Movie" |
| `item.itemType.overviewName` | `null` | null |
| `item.itemType.pastTenseVerb` | `string` | "watched" |
| `item.itemType.picture` | `string` | "clapperboard" |
| `item.itemType.position1` | `string` | "hour" |
| `item.itemType.position2` | `string` | "minute" |
| `item.itemType.position3` | `string` | "second" |
| `item.itemType.sectionName` | `null` | null |
| `item.itemType.slug` | `string` | "movies" |
| `item.itemType.updatedAt` | `string` | "2019-02-19T13:02:35.000Z" |
| `item.itemType.verb` | `string` | "watch" |
| `item.legacyId` | `integer` | 1167 |
| `item.legacyItemType` | `string` | "movie" |
| `item.legacyUserId` | `integer` | 28 |
| `item.name` | `string` | "Fight Club" |
| `item.numRatings` | `integer` | 8241 |
| `item.overview` | `string` | "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with u… |
| `item.posterImage` | `string` | "jSziioSwPVrOy9Yow3XhWIBDjq1.jpg" |
| `item.posterVerified` | `boolean` | false |
| `item.releaseYear` | `string` | "1999" |
| `item.review` | `null` | null |
| `item.tmdbId` | `integer` | 550 |
| `item.tmdbResult` | `null` | null |
| `item.umId` | `null` | null |
| `item.updatedAt` | `string` | "2025-11-04T11:45:44.000Z" |
| `item.verified` | `boolean` | false |
| `item.verifyAttempts` | `integer` | 100 |
| `numNo` | `integer` | 129 |
| `numYes` | `integer` | 70 |
| `smartPageDescription` | `null` | null |
| `smartPageTitle` | `null` | null |
| `topicItemStats` | `array` | [{"topicItemId": 378845, "newsletterDate": null, "yesSum": 3, "noSum": 111, "numComments": 1, "TopicId": 153, "ItemId": 9593, "RatingId": 7458752, "commentUserI… |
| `topicItemStats[0]` | `object` | {"topicItemId": 378845, "newsletterDate": null, "yesSum": 3, "noSum": 111, "numComments": 1, "TopicId": 153, "ItemId": 9593, "RatingId": 7458752, "commentUserId… |
| `topicItemStats[0].ItemId` | `integer` | 9593 |
| `topicItemStats[0].RatingId` | `integer` | 7458752 |
| `topicItemStats[0].TopicCategory` | `object` | {"id": 2, "name": "Animal", "createdAt": "2020-04-03T12:22:40.000Z", "updatedAt": "2020-04-03T12:22:40.000Z"} |
| `topicItemStats[0].TopicCategory.createdAt` | `string` | "2020-04-03T12:22:40.000Z" |
| `topicItemStats[0].TopicCategory.id` | `integer` | 2 |
| `topicItemStats[0].TopicCategory.name` | `string` | "Animal" |
| `topicItemStats[0].TopicCategory.updatedAt` | `string` | "2020-04-03T12:22:40.000Z" |
| `topicItemStats[0].TopicId` | `integer` | 153 |
| `topicItemStats[0].UserId` | `integer` | 133193 |
| `topicItemStats[0].comment` | `string` | "There are no dogs in the movie :)" |
| `topicItemStats[0].commentUserIds` | `string` | "133193" |
| `topicItemStats[0].comments` | `array` | [{"id": 7458752, "voteSum": 12, "comment": "There are no dogs in the movie :)", "index1": -1, "index2": -1, "User": {"id": 133193, "displayName": "Hamarhemmo"}}… |
| `topicItemStats[0].comments[0]` | `object` | {"id": 7458752, "voteSum": 12, "comment": "There are no dogs in the movie :)", "index1": -1, "index2": -1, "User": {"id": 133193, "displayName": "Hamarhemmo"}} |
| `topicItemStats[0].comments[0].User` | `object` | {"id": 133193, "displayName": "Hamarhemmo"} |
| `topicItemStats[0].comments[0].User.displayName` | `string` | "Hamarhemmo" |
| `topicItemStats[0].comments[0].User.id` | `integer` | 133193 |
| `topicItemStats[0].comments[0].comment` | `string` | "There are no dogs in the movie :)" |
| `topicItemStats[0].comments[0].id` | `integer` | 7458752 |
| `topicItemStats[0].comments[0].index1` | `integer` | -1 |
| `topicItemStats[0].comments[0].index2` | `integer` | -1 |
| `topicItemStats[0].comments[0].voteSum` | `integer` | 12 |
| `topicItemStats[0].doesName` | `string` | "Does the dog die" |
| `topicItemStats[0].hasUserComment` | `boolean` | false |
| `topicItemStats[0].index1` | `integer` | -1 |
| `topicItemStats[0].index2` | `integer` | -1 |
| `topicItemStats[0].isAnonymous` | `integer` | 0 |
| `topicItemStats[0].isFavorite` | `boolean` | true |
| `topicItemStats[0].itemBackgroundImage` | `string` | "hZkgoQYus5vegHoetLkCJzb17zJ.jpg" |
| `topicItemStats[0].itemCleanName` | `string` | "fight club" |
| `topicItemStats[0].itemId` | `null` | null |
| `topicItemStats[0].itemName` | `string` | "Fight Club" |
| `topicItemStats[0].itemPosterImage` | `string` | "jSziioSwPVrOy9Yow3XhWIBDjq1.jpg" |
| `topicItemStats[0].itemTypeId` | `integer` | 15 |
| `topicItemStats[0].itemTypeIndex1` | `null` | null |
| `topicItemStats[0].itemTypeIndex2` | `null` | null |
| `topicItemStats[0].itemTypeName` | `string` | "Movie" |
| `topicItemStats[0].itemTypeSlug` | `string` | "movies" |
| `topicItemStats[0].newsletterDate` | `null` | null |
| `topicItemStats[0].noSum` | `integer` | 111 |
| `topicItemStats[0].numComments` | `integer` | 1 |
| `topicItemStats[0].ratingIndex1` | `integer` | -1 |
| `topicItemStats[0].ratingIndex2` | `integer` | -1 |
| `topicItemStats[0].releaseYear` | `string` | "1999" |
| `topicItemStats[0].slug` | `string` | "does-the-dog-die" |
| `topicItemStats[0].topic` | `object` | {"id": 153, "name": "a dog dies", "notName": "no dogs die", "survivesName": "the dog survives", "keywords": "Dog death, canine death, pet dog death, puppy dies"… |
| `topicItemStats[0].topic.TopicCategory` | `object` | {"id": 2, "name": "Animal", "createdAt": "2020-04-03T12:22:40.000Z", "updatedAt": "2020-04-03T12:22:40.000Z"} |
| `topicItemStats[0].topic.TopicCategory.createdAt` | `string` | "2020-04-03T12:22:40.000Z" |
| `topicItemStats[0].topic.TopicCategory.id` | `integer` | 2 |
| `topicItemStats[0].topic.TopicCategory.name` | `string` | "Animal" |
| `topicItemStats[0].topic.TopicCategory.updatedAt` | `string` | "2020-04-03T12:22:40.000Z" |
| `topicItemStats[0].topic.TopicCategoryId` | `integer` | 2 |
| `topicItemStats[0].topic.createdAt` | `string` | "2017-06-22T18:20:34.000Z" |
| `topicItemStats[0].topic.demandOrder` | `integer` | 1 |
| `topicItemStats[0].topic.description` | `string` | "This trigger is for people who are upset by the death of a canine companion. Dogs are often portrayed as loyal friends in films, and their death can be very tr… |
| `topicItemStats[0].topic.doesName` | `string` | "Does the dog die" |
| `topicItemStats[0].topic.id` | `integer` | 153 |
| `topicItemStats[0].topic.image` | `string` | "dog" |
| `topicItemStats[0].topic.isSensitive` | `boolean` | false |
| `topicItemStats[0].topic.isSpoiler` | `boolean` | false |
| `topicItemStats[0].topic.isVisible` | `boolean` | true |
| `topicItemStats[0].topic.keywords` | `string` | "Dog death, canine death, pet dog death, puppy dies" |
| `topicItemStats[0].topic.legacyId` | `integer` | 25 |
| `topicItemStats[0].topic.listName` | `string` | "where the dog dies" |
| `topicItemStats[0].topic.name` | `string` | "a dog dies" |
| `topicItemStats[0].topic.notName` | `string` | "no dogs die" |
| `topicItemStats[0].topic.ordering` | `integer` | 100 |
| `topicItemStats[0].topic.smmwDescription` | `string` | "dogs dying" |
| `topicItemStats[0].topic.subtitle` | `string` | "" |
| `topicItemStats[0].topic.subtitleText` | `null` | null |
| `topicItemStats[0].topic.subtitleUrl` | `null` | null |
| `topicItemStats[0].topic.supporters` | `integer` | 1 |
| `topicItemStats[0].topic.survivesName` | `string` | "the dog survives" |
| `topicItemStats[0].topic.updatedAt` | `string` | "2024-07-30T20:37:08.000Z" |
| `topicItemStats[0].topicItemId` | `integer` | 378845 |
| `topicItemStats[0].username` | `string` | "Hamarhemmo" |
| `topicItemStats[0].voteSum` | `integer` | 12 |
| `topicItemStats[0].yesSum` | `integer` | 3 |

_Total unique paths: 214_