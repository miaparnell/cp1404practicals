import wikipedia

# Note: I was unable to properly test this code because no matter what the search string was, I always got a
# warning about the BeautifulSoup package
search_string = input("Enter a page title or phrase to search by: ")
while search_string != "":
    try:
        article = wikipedia.page(search_string)
        print(article.title)
        print(article.url)
        print(article.summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
        print("Please enter another title or phrase to search by.")
    search_string = input("Enter a page title or phrase to search by: ")
print("Thank you for searching today!")
