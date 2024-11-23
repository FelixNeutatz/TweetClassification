class Tweet:
    def __init__(self, user, text, id):
        """
        Initialize a Tweet object.

        Args:
        user (str): The username of the person posting the tweet.
        text (str): The content of the tweet.
        """
        self.user = user
        self.text = text
        self.id = id


    def __repr__(self):
        """
        Provide a string representation of the Tweet object.
        """
        return f"Tweet(user='{self.user}', text='{self.text}')"