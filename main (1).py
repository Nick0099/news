import requests
import json

i = 0
# news type input from user
newstype = input("what kind of news do you want to read?\n")
# enter api key
apikey = ("Enter api key here")
# fetching news from news.org
news = (
    f"https://newsapi.org/v2/everything?q={newstype}&from=2024-06-29&sortBy=popularity&apiKey={apikey}"
)

# Filters the news to make it readable
r = requests.get(news)
khabar = json.loads(r.text)

# Prints all topics given by the user
for topics in khabar["articles"]:
  i = i + 1
  print(f"{i}.\n\n{topics['title']}")

# asks user if they want a specific news
Specific_topic = input(
    "Do you want to read a specific topic?(enter the topic number)\n")

#stores the news in a variable
selected_article = khabar["articles"][int(Specific_topic) - 1]

for j in range(0, len(khabar["articles"])):

  #Prints specific news that the user wants
  if j == int(Specific_topic):
    print(
        f"\n\n{selected_article['title']} \n\n {selected_article['description']}\n\n{selected_article['description']}"
    )
