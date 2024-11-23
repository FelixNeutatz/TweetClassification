import pandas as pd
from tweetclassification.Tweet import Tweet
from tweetclassification.Conversation import Conversation

def readConversations(file_path):
    df = pd.read_csv(file_path).sort_values(by=['in_response_to_tweet_id'])

    # Display the first few rows of the DataFrame
    matrix = df.values

    maptweets = {}
    id2tweet = {}

    starting_tweets = []

    for i in range(len(matrix)):
        previous_tweet_id = matrix[i, list(df.columns).index("in_response_to_tweet_id")]
        current_tweet_id = matrix[i, list(df.columns).index("tweet_id")]
        id2tweet[current_tweet_id] = i

        if pd.isna(previous_tweet_id):
            starting_tweets.append(int(current_tweet_id))
        else:
            maptweets[int(previous_tweet_id)] = int(current_tweet_id)

    print(starting_tweets)
    # print(maptweets)

    conversations = []

    for tweet_id in starting_tweets:
        conversation = Conversation()
        tweet_raw_id = id2tweet[tweet_id]
        if "author_id" in df.columns:
            user = matrix[tweet_raw_id, list(df.columns).index("author_id")]
        else:
            user = ""

        text = matrix[tweet_raw_id, list(df.columns).index("text")]
        conversation.add_tweet(Tweet(user, text, tweet_id))
        current_id = tweet_id
        while current_id in maptweets:
            current_id = maptweets[current_id]
            tweet_raw_id = id2tweet[current_id]
            if "author_id" in df.columns:
                user = matrix[tweet_raw_id, list(df.columns).index("author_id")]
            else:
                user = ""
            text = matrix[tweet_raw_id, list(df.columns).index("text")]
            conversation.add_tweet(Tweet(user, text, current_id))
        conversations.append(conversation)

    return conversations