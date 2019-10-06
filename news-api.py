import pprint

import requests     # 2.19.1

secret = '9d860ff2bedb49af91fd5421012b2dd0'

# Specify the query and number of returns

#https://newsapi.org/v2/everything?q=bitcoin&from=2019-09-03&sortBy=publishedAt&

parameters = {
    'q': 'big data', # query phrase
    'pageSize': 20,  # maximum is 100
    'language': "de",
    'apiKey': secret # your own API key
}
# Define the endpoin t

# url = 'https://newsapi.org/v2/sources?'
#url = 'https://newsapi.org/v2/everything?'
url='https://newsapi.org/v2/sources?apiKey=9d860ff2bedb49af91fd5421012b2dd0'
# Make the request

response = requests.get(url, params=parameters)
# Convert the response to JSON format and pretty print it

response_json = response.json()

pprint.pprint(response_json)

print('******************************')

for i in response_json['articles']:

    print(i['title'])

#from wordcloud import WordCloud

#import matplotlib.pyplot as plt

# Create an empty string

text_combined = ''

# Loop through all the headlines and add them to 'text_combined'

for i in response_json['articles']:

    text_combined += i['title'] + ' ' # add a space after every headline, so the first and last words are not glued together

# Print the first 300 characters to screen for inspection

print("*********************************")   

print(text_combined[0:300])

#wordcloud = WordCloud(max_font_size=40).generate(text_combined)
#
#plt.figure()
#
#plt.imshow(wordcloud, interpolation="bilinear")
#
#plt.axis("off")
#
#plt.show()