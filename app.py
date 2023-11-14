import argparse
import requests
from bs4 import BeautifulSoup
from collections import Counter

def extract_keywords(url, top_n):
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')
        text_content = ' '.join([p.get_text() for p in soup.find_all('p')])

        words = text_content.lower().split()
        word_counts = Counter(words)

        print(f"Top {top_n} Keywords:")
        for word, count in word_counts.most_common(top_n):
            print(f"{word}: {count}")

    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description='Easy SEO Keyword Extractor')
    parser.add_argument('--url', required=True, help='URL of the webpage to analyze')
    parser.add_argument('--top', type=int, default=5, help='Number of top keywords to display')

    args = parser.parse_args()
    extract_keywords(args.url, args.top)

if __name__ == "__main__":
    main()
