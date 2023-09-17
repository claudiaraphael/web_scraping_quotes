from bs4 import BeautifulSoup
# crawling is the predecessor of web scraping
import requests
import csv

page_to_scrape = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# cria uma lista pras quotes e authors encontrados
quotes = soup.findAll("span", attrs={"class": "text"})
authors = soup.findAll("small", attrs={"class": "author"})

# cria um arquivo csv pra colocar as quotes e authors
file = open('scraped_quotes.csv', 'w')
writer = csv.writer(file)

# adiciona os nomes das colunas 
writer.writerow(["QUOTES", "AUTHORS"])

# percorre as listas de quotes e autores
# printa os dados scrapados
# coloca os dados no arquivo csv
for quote, author in zip(quotes, authors):
	print(quote.text + " - " + author.text)
	writer.writerow([quote.text, author.text])

file.close()