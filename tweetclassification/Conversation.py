from tweetclassification.Tweet import Tweet

class Conversation:
    def __init__(self):
        """
        Initialize a Conversation object with an empty list of tweets.
        """
        self.tweets = []

    def add_tweet(self, tweet):
        """
        Add a Tweet object to the conversation.

        Args:
        tweet (Tweet): The tweet to add to the conversation.
        """
        if isinstance(tweet, Tweet):
            self.tweets.append(tweet)
        else:
            raise ValueError("Only Tweet objects can be added to the conversation.")

    def display(self):
        """
        Display all tweets in the conversation in order.
        """
        print("Conversation:")
        for tweet in self.tweets:
            tweet.display()

    def __len__(self):
        """
        Return the number of tweets in the conversation.
        """
        return len(self.tweets)

    def __repr__(self):
        """
        Provide a string representation of the Conversation object.
        """
        my_str = ""
        for tweet in self.tweets:
            my_str += tweet.text + " "
        my_str = my_str[:-1] + " label: " + str(self.get_label())
        return my_str

    def get_text(self):

        my_str = ""
        for tweet in self.tweets:
            if tweet.user.isdigit():
                my_str += "user: "
            else:
                my_str += "system: "
            tokens = tweet.text.replace("\n", " ").split(" ")
            for t in tokens:
                if not (t.startswith("@") or
                        t.startswith("http") or
                        t.startswith("/") or
                        t.startswith("-") or
                        t.startswith("*") or
                        t.startswith("^") or
                        t.startswith("~") or
                        t.startswith(".@") or
                        t.startswith(":http")
                ):
                    my_str += self.removeStrings(t) + " "
            my_str = my_str[:-1] + "\n"
        return my_str

    def removeStrings(self, text):
        to_be_removed = ['😡', "😶", "😂", "😍", "😠", ":)", ":(", "😥", "🗣🙃", "😅", "😆", "😎", "✈", "😊",
                         "❤️", "😉", ":/", "☹️", "😓", "🙃", "🙈😢", "😃", "😘💙", ":-(", ":-)", "😵", "😄", "😋",
                         "😭", "⚾️", "😞", "😁", "😔", "😑", "😇", "😰", "😒", "😩", "😢", "🤷‍♂️", "😱", "😖", "😀",
                         "😘", "😜", "(4/4)","2/2", "1/2", "1/3", "3/3", "1/4", "😻", "😳", "😏", "😌", "😣", "😕", "❤"]
        for remove_str in to_be_removed:
            text = text.replace(remove_str, "")
        return text

    def get_label(self):
        for tweet in self.tweets:
            if not tweet.user.isdigit():
                return tweet.user