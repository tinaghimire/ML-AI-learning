# HINT: This code is to form a string of length exactly 140

# My code
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""

count = 0
for head in headlines:
    if count + len(head) <= 140:
        count += len(head) + 1 
        news_ticker += head 
        news_ticker += ' '
        print(len(news_ticker))
        print(news_ticker)
    elif count + len(head) > 140:
        left = 140 - count
        print(len(news_ticker))
        print(news_ticker)
        for i in range(left):
            count += 1
            news_ticker += head[i]
    elif count == 140:
        break    

print(len(news_ticker))
print(news_ticker)

# Better solution
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)

