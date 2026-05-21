import os
import string
import requests
from bs4 import BeautifulSoup
from typing import List, Dict


class ArticleParseError(Exception):
    """Custom exception for handling network requests or HTML parsing failures."""
    pass


class NatureWebScraper:
    """
    Description:
    A multipage web scraper for nature.com. It identifies articles of a
    specific category, navigates to their individual pages, extracts
    the core content, and saves them as sanitized text files.

    Parameters:
    (No parameters for initialization)

    Returns:
    None: Articles are saved to local directories named 'Page_X'.
    """

    def __init__(self) -> None:
        self.base_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page={}"
        self.domain = "https://www.nature.com"
        self.headers = {'Accept-Language': 'en-US,en;q=0.5'}

    @staticmethod
    def sanitize_name(title: str) -> str:
        """
        Removes punctuation and replaces spaces with underscores
        to create a valid and clean filesystem name.
        """
        translator = str.maketrans('', '', string.punctuation)
        cleaned = title.translate(translator)
        cleaned = cleaned.replace(' ', '_')
        while '__' in cleaned:
            cleaned = cleaned.replace('__', '_')
        return cleaned.strip('_')

    def fetch_html(self, url: str) -> str:
        """Executes a GET request and returns the raw HTML content."""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
        except requests.RequestException as e:
            raise ArticleParseError(f"Request failed: {e}")

        if response.status_code != 200:
            raise ArticleParseError(f"HTTP {response.status_code}")

        return response.text

    def get_articles(self, page_url: str, article_type: str) -> List[Dict[str, str]]:
        """
        Scans a search results page for articles matching the 'article_type'
        metadata and returns their titles and absolute URLs.
        """
        html = self.fetch_html(page_url)
        soup = BeautifulSoup(html, 'html.parser')

        articles = []
        for article in soup.find_all('article'):
            type_span = article.find('span', {'data-test': 'article.type'})
            if not type_span or type_span.text.strip() != article_type:
                continue

            link_tag = article.find('a', {'data-track-action': 'view article'})
            if not link_tag or not link_tag.get('href'):
                continue

            rel_link = link_tag['href']
            abs_link = self.domain + rel_link if rel_link.startswith('/') else rel_link

            title = link_tag.text.strip()
            if not title:
                heading = article.find('h3') or article.find('h2')
                if heading:
                    title = heading.text.strip()

            if title:
                articles.append({'title': title, 'link': abs_link})

        return articles

    def extract_article_body(self, article_url: str) -> str:
        """
        Navigates to an article's page and attempts to locate the main text
        body using several common CSS selectors used by Nature.
        """
        html = self.fetch_html(article_url)
        soup = BeautifulSoup(html, 'html.parser')

        possible_selectors = [
            'div.c-article-body',
            'div.article__content',
            'div[class*="article-body"]',
            'div[class*="body"]',
            'main.article-main',
        ]

        for selector in possible_selectors:
            body_div = soup.select_one(selector)
            if body_div:
                text = ' '.join(body_div.stripped_strings)
                if text:
                    return text

        meta_desc = soup.find('meta', {'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            return meta_desc['content']

        raise ArticleParseError("No article body found with any known selector")

    def save_article(self, title: str, body: str, output_dir: str) -> str:
        """Saves the article content to a .txt file in UTF-8 encoding."""
        name = self.sanitize_name(title)
        filename = f"{name}.txt"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'wb') as f:
            f.write(body.encode('utf-8'))

        return filepath

    def run(self) -> None:
        """
        Main execution logic: Iterates through pages, creates directories,
        and orchestrates the fetching/saving process.
        """
        try:
            num_pages = int(input("> ").strip())
            article_type = input("> ").strip()
        except ValueError:
            print("Invalid input.")
            return

        for page_num in range(1, num_pages + 1):
            page_url = self.base_url.format(page_num)
            dir_name = f"Page_{page_num}"
            os.makedirs(dir_name, exist_ok=True)

            try:
                articles = self.get_articles(page_url, article_type)
            except ArticleParseError:
                continue

            for art in articles:
                try:
                    body = self.extract_article_body(art['link'])
                    self.save_article(art['title'], body, dir_name)
                except ArticleParseError:
                    pass

        print("Saved all articles.")


if __name__ == "__main__":
    scraper = NatureWebScraper()
    scraper.run()