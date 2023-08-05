
from django.shortcuts import render
from .getSentiment import getSentimentForm, getSentiment
import pandas as pd
import numpy as np

def Sentiment_Analyzer(request):

    # if this is a POST request we need to process the form data.
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request:
        form = getSentimentForm(request.POST)

        # Check whether it's valid.
        if form.is_valid():

            # Put the user imput into a dataframe and pull sentiment.
            data = pd.DataFrame([request.POST['message']], columns=['input'])
            sentiment = getSentiment(data)
            
            output = 'You have submitted a ' + sentiment['sentiment'][0] + ' sentence or paragragh.'


    else: 
        
        form = getSentimentForm()
        output = "You haven't submitted anything for analysis."

    return render(request, 'sentiment_analyzer.html', {'form': form, 'output': output})