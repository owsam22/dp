#mining text and web using application experiment in data mining

pip install requests beautifulsoup4 nltk

import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import nltk

# download NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# web mining
url = 'https://en.wikipedia.org/wiki/Data_mining'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/118.0 Safari/537.36"
}
response = requests.get(url, headers=headers)

# parse HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# extract all paragraph text
paragraphs = soup.find_all('p')
text = ' '.join([p.get_text() for p in paragraphs])

print("=== sample of extracted text ===")
print(text[:500])  # show first 500 characters

# text mining
if text.strip():
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    filtered_words = [w for w in words if w.isalpha() and w not in stop_words]

    # count word frequency
    word_freq = Counter(filtered_words)

    # display 10 most common words
    print("\n=== top 10 most common words ===")
    for word, freq in word_freq.most_common(10):
        print(f"{word}: {freq}")
else:
    print("⚠️ No text extracted — try adjusting headers or URL.")
