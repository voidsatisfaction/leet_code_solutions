from typing import List

class Twitter:
  def __init__(self):
    # TODO: it should be encapsulized
    self._Users = { "byId": {}, "allIds": [] } # userId
    self._Following = { "byId": {}, "allIds": [] } # followerId, followeeId
    self._UserTweets = [] # userId, tweetId, createdAt
    self._createdAt = 0

  def postTweet(self, userId: int, tweetId: int) -> None:
    # FIXME: this method should not know the inner structure of Users, UserTweets, ...
    # use interface only
    if self._Users["byId"].get(userId) is None:
      self._Users["byId"][userId] = None
      self._Users["allIds"].append(userId)
    
    # this should be transaction
    # multithreading environment, it is not safe
    self._UserTweets.append({ "userId": userId, "tweetId": tweetId, "createdAt": self._createdAt })
    self._createdAt += 1

  def getNewsFeed(self, userId: int) -> List[int]:
    allFollowees = self._getAllFollowees(userId)

    return self._getRecent10TweetIds(allFollowees)

  def follow(self, followerId: int, followeeId: int) -> None:
    if self._Following["byId"].get(followerId) is None:
      self._Following["byId"][followerId] = []
      self._Following["allIds"].append(followerId)
    
    self._Following["byId"].get(followerId).append(followeeId)

  def unfollow(self, followerId: int, followeeId: int) -> None:
    if followerId == followeeId:
      return

    allFollowees = set()
    if self._Following["byId"].get(followerId):
      allFollowees = set(self._Following["byId"].get(followerId))

    if followeeId in allFollowees:
      self._Following["byId"].get(followerId).remove(followeeId)

  def _getAllFollowees(self, followerId: int) -> List[int]:
    # including me
    if self._Following["byId"].get(followerId) is None:
      return [followerId]
    
    return [followerId] + self._Following["byId"].get(followerId)

  def _getRecent10TweetIds(self, userIds: List[int]) -> List[int]:
    userIds = set(userIds)
    tweetIds = []
    count = 0

    for tweet in self._UserTweets[::-1]:
      userId = tweet["userId"]
      if userId in userIds:
        tweetIds.append(tweet["tweetId"])
        count += 1

      if count >= 10:
        return tweetIds

    return tweetIds


twitter = Twitter()
twitter.postTweet(1, 2)
twitter.getNewsFeed(1)
twitter.postTweet(2, 3)
twitter.follow(1, 2)
twitter.postTweet(3, 8)
twitter.follow(1, 3)
print(twitter.getNewsFeed(1))
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(3))

print(twitter._Users)
print(twitter._Following)
print(twitter._UserTweets)
print(twitter._Following)
print(twitter._createdAt)