from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2995170696-z5tNgtrnhR5zc5tT4sB6knKBTrCKHehOljhs1l2"
access_token_secret = "wOcuYhfpvwxFZ6TmNvyPb9fPpEnH1fvfApiEZFnFGUuJk"
consumer_key = "5zvyqirbbnbPxUX67ixXBwQ5G"
consumer_secret = "8iGil6zWJvK7qjGj0z7xguSvaiIbZtpH0Z3UumAVetv88e9xbX"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
