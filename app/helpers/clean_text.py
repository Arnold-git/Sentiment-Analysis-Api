import re
import string


# emoji removal function
emoji_pattern = re.compile("["
         u"\U0001F600-\U0001F64F"  # emoticons
         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
         u"\U0001F680-\U0001F6FF"  # transport & map symbols
         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
         u"\U00002702-\U000027B0"
         u"\U000024C2-\U0001F251"
         "]+", flags=re.UNICODE)


def clean_text(text):   
    ''' Helper function to clean text, remove text in square barcket, remove link
        remove punctuation and remove words containing numbers

        Returns:
            [string] clean text
    '''
    text = str(text).lower()
    text = re.sub('#[A-Za-z0-9_]+', '', text) #remove hashtag
    text = emoji_pattern.sub(r'', text) # remove emoji
    text = re.sub('\[.*?\]', '', text) 
    text = text.replace('/[^a-zA-Z0-9]/g', '') #to change all characters except numbers and letters
    text = re.sub('https?://\S+|www\.\S+', '', text) # remove urls
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', 
                  text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)

    return text