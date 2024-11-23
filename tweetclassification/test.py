import pandas as pd
from tweetclassification.Tweet import Tweet
from tweetclassification.Conversation import Conversation
from tweetclassification.FileUtils import readConversations

'''
file_path = "/home/felix/Desktop/AI-Case-Data/training_data.csv"
conversations = readConversations(file_path)


from sklearn.preprocessing import LabelEncoder

train_x = []
train_y = []
for conversation in conversations:
    train_x.append(conversation.get_text())
    train_y.append(conversation.get_label())

print(train_y)

y = LabelEncoder().fit_transform(y=train_y)

train_data = pd.DataFrame({'sentence': train_x, 'label': y})





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

test_file_path = "/home/felix/Desktop/AI-Case-Data/prod_data_cleaned_new.csv"
test_conversations = readConversations(test_file_path)



