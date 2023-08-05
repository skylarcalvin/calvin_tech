from django import forms
import pandas as pd
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class getSentimentForm(forms.Form):
    message = forms.CharField(label='Say something positive or negative.', widget=forms.Textarea())

def getSentiment(df):
    '''
    Function assigns sentiment to each document in the corpus and adds them as a new row on the dataframe.
    '''
    
    # Build sentiment analyzer.
    analyzer = SentimentIntensityAnalyzer()
    sentiment = [analyzer.polarity_scores(i) for i in df['input']]
    
    # build new dataframe around detected sentiment.
    df1 = pd.DataFrame(sentiment)
    df1['input'] = df['input']
    
    # Label the rows using the compound sentiment score.
    sents = []
    
    for i in range(len(df1)):
        
        if df1['compound'][i] > 0.05:
            
            if df1['compound'][i] > 0.5:
                
                x = 'very positive'
                
            else:
                
                x = 'positive'
            
        elif df1['compound'][i] < -0.05:
            
            if df1['compound'][i] < -0.5:
                
                x = 'very negative'
                
            else:
                
                x = 'negative'
            
        else:
            
            x = 'neutral'
            
        sents.append(x)
        
    df1['sentiment'] = pd.Series(sents)
    
    return df1