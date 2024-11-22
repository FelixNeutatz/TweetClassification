import pandas as pd
from tweetclassification.Tweet import Tweet
from tweetclassification.Conversation import Conversation

file_path = "/home/felix/Desktop/AI-Case-Data/training_data.csv"

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
#print(maptweets)

conversations = []

for tweet_id in starting_tweets:
    conversation = Conversation()
    tweet_raw_id = id2tweet[tweet_id]
    user = matrix[tweet_raw_id, list(df.columns).index("author_id")]
    text = matrix[tweet_raw_id, list(df.columns).index("text")]
    conversation.add_tweet(Tweet(user, text))
    current_id = tweet_id
    while current_id in maptweets:
        current_id = maptweets[current_id]
        tweet_raw_id = id2tweet[current_id]
        user = matrix[tweet_raw_id, list(df.columns).index("author_id")]
        text = matrix[tweet_raw_id, list(df.columns).index("text")]
        conversation.add_tweet(Tweet(user, text))
    print(conversation.get_text())
    conversations.append(conversation)

from autogluon.text import TextPredictor
from sklearn.preprocessing import LabelEncoder

train_x = []
train_y = []
for conversation in conversations:
    train_x.append(conversation.get_text())
    train_y.append(conversation.get_label())

y = LabelEncoder().fit_transform(y=train_y)

train_data = pd.DataFrame({'sentence': train_x, 'label': y})

import os
os.environ["AUTOGLUON_TEXT_TRAIN_WITHOUT_GPU"] = "1"

predictor = TextPredictor(label='label', eval_metric='balanced_accuracy', path='./ag_sst')
predictor.fit(train_data, time_limit=60)
print(predictor.predict("good job amazon"))



''''
print(conversations)
print(len(conversations))

label_distribution = {}

for conversation in conversations:
    if not conversation.get_label() in label_distribution:
        label_distribution[conversation.get_label()] = 0
    label_distribution[conversation.get_label()] += 1

print(label_distribution)
print(len(label_distribution))
'''

'''



test_file_path = "/home/felix/Desktop/AI-Case-Data/prod_data_cleaned_new.csv"

test_df = pd.read_csv(test_file_path)

# Display the first few rows of the DataFrame
print(test_df.head())
'''