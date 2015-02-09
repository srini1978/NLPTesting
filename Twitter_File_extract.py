
import re
import nltk
import nltk.classify
#start process_tweet
def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end

#initialize stopWords
stopWords = []

#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end

#start getStopWordList
def getStopWordList(stopWordListFileName):
    #read the stopwords file and build a list
    stopWords = []
    stopWords.append('AT_USER')
    stopWords.append('URL')

    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords
#end

#start getfeatureVector
def getFeatureVector(tweet):
    featureVector = []
    #split tweet into words
    words = tweet.split()
    for w in words:
        #replace two or more with two occurrences
        w = replaceTwoOrMore(w)
        #strip punctuation
        w = w.strip('\'"?,.')
        #check if the word stats with an alphabet
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        #ignore if it is a stop word
        if(w in stopWords or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector
#end

#Read the training data tweets one by one and process it
st = open('stopwords.txt', 'r')
stopWords = getStopWordList('stopwords.txt')

pos_tweets = [('I love this car', 'positive'), 
              ('This view is amazing', 'positive'), 
              ('I feel great this morning', 'positive'), 
             ('I am so excited about the concert', 'positive'), 
              ('He is my best friend', 'positive')] 


neg_tweets = [('I do not like this car', 'negative'), 
              ('This view is horrible', 'negative'), 
              ('I feel tired this morning', 'negative'), 
              ('I am not looking forward to the concert', 'negative'), 
              ('He is my enemy', 'negative')] 


tweets = [] 
for (words, sentiment) in pos_tweets + neg_tweets: 
    processedTweet = processTweet(words)
    featureVector = getFeatureVector(processedTweet)
    tweets.append((featureVector, sentiment));
    # this is the list of features extracted from training set
    print(featureVector)
#end loop

# from this feature list , do a extract of featurs
def extract_features(document): 
    document_words = set(document) 
    features = {} 
    for word in featureVector: 
        features['contains(%s)' % word] = (word in document_words) 
        return features


training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.classify.NaiveBayesClassifier.train(training_set)
tweet = 'Larry is an enemy idiot ' 
result= classifier.classify(extract_features(tweet.split()))
print(result)





#fc = open('twitter_processed_data.txt','w')
#while line:
    #processedTweet = processTweet(line)
   # featureVector = getFeatureVector(processedTweet)
   # print (featureVector)
#for item in featureVector:
 #   fc.write("%s\n" % item)

    #line = fp.readline()
#end loop








