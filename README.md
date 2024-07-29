# crawlee
 Crawlee is a powerful web scraping and browser automation library for Python.
 There are 2 main crawler classes available in Crawlee :
- BeautifulSoupCrawler
- PlaywrightCrawler

## How crawling works
The process is simple:
- Find new links on the page.
- Filter only those pointing to the same domain.
- Enqueue (add) them to the RequestQueue.
- Visit the newly enqueued links.
- Repeat the process.

## Installation Required
```bash
  pip install crawlee
  ```
```bash
  pip install 'crawlee[beautifulsoup]'
```
  ```bash
  pip install 'crawlee[playwright]'
```
To install dependencies
```bash
  playwright install
```

## crawl-with-beautifulsoup.py
This script performs a recursive crawl of the ```[Crawlee](https://crawlee.dev)``` website, extracting and storing the title and URL of each page using the BeautifulSoupCrawler.

BeautifulSoupCrawler is an HTTP crawler with HTTP2 support, anti-blocking features, and an integrated HTML parser using BeautifulSoup. It's known for being fast, simple, and cost-effective, with minimal dependencies. However, it doesn't support JavaScript rendering, so it won't work for websites that require JavaScript to load content.

![Screenshot 2024-07-30 010442](https://github.com/user-attachments/assets/36c8b1c4-f326-4229-8985-d7e0b06fc0c9)


## crawl-with-playwright.py
This script performs a recursive crawl of the ```[Crawlee](https://crawlee.dev)``` website, extracting and storing the title and URL of each page using the PlaywrightCrawler.

PlaywrightCrawler uses a headless browser controlled by the Playwright library. Playwright supports various browsers such as Chromium, Firefox, and WebKit. It is known for its powerful browser automation capabilities and is considered the successor to Puppeteer. If you need a headless browser for your crawling needs, Playwright is a great choice.

https://github.com/user-attachments/assets/c512df5d-8dc1-4dec-b849-63a818d19b9d


## building-beautifulsoup-crawler.py
This script demonstrates how to set up a web crawler using BeautifulSoupCrawler with a request queue. It extracts the page title from a specified URL. This approach is suitable for simple web scraping tasks where JavaScript rendering is not required.

![Screenshot 2024-07-30 010442](https://github.com/user-attachments/assets/1ab12ee3-f7ad-4fbb-bbcd-06e632be8ba4)


## scrape-warehouse-store
This is a simple project that demonstrate how to use PlaywrightCrawler to crawl a webpage ```https://warehouse-theme-metal.myshopify.com```, to scrape data. It utilizes Playwright's ability to render JavaScript and interact with dynamic content.

### start.py
This script demonstrate how to create a crawler that visits the specified URL and prints the text content of elements with a certain class. here (collection-block-item)

![start2](https://github.com/user-attachments/assets/c9d5bdd9-869b-459d-9c20-e341279ef08e)


### crawl.py
The script is designed to Process different types of pages (start, category, and detail), Handle pagination on category pages (Pagination refers to the process of navigating through multiple pages of content on a website) , Enqueue product detail links from category pages.



https://github.com/user-attachments/assets/ff01c023-6fe5-4983-b55c-35392dd05199



### scrape.py
The script is mainly designed to Process and extract data from product detail pages (URL, Manufacturer, SKU, Title, Current price, Stock available).



https://github.com/user-attachments/assets/c4cf3a18-621c-4b89-b14d-a45d2c471821



### save.py
This is final script that collects data from a website with dynamic content.
![Screenshot 2024-07-30 024347](https://github.com/user-attachments/assets/c07b3427-ba60-4c1f-98d1-e8f7adfaca1b)


