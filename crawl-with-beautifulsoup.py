# perform a recursive crawl of the Crawlee website using the beautifulsoup crawler


import asyncio
from crawlee.beautifulsoup_crawler import BeautifulSoupCrawler, BeautifulSoupCrawlingContext
from crawlee import Glob

async def main() -> None:
    # BeautifulSoupCrawler crawls the web using HTTP requests and parses HTML using the BeautifulSoup library.
    crawler = BeautifulSoupCrawler(max_requests_per_crawl=50)

    # Define a request handler to process each crawled page and attach it to the crawler using a decorator.
    @crawler.router.default_handler
    async def request_handler(context: BeautifulSoupCrawlingContext) -> None:
        # Extract relevant data from the page context.
        data = {
            'url': context.request.url,
            'title': context.soup.title.string if context.soup.title else None,
        }
        # Store the extracted data.
        await context.push_data(data)
        # Extract links from the current page and add them to the crawling queue.
        await context.enqueue_links()
        
        # Filter URLs with patterns
        # await enqueue_links(
        #        include=[Glob('https://someplace.com/**/cats')],
        #        exclude=[Glob('https://**/archive/**')],
        #     )

    # Add first URL to the queue and start the crawl.
    await crawler.run(['https://crawlee.dev'])


if __name__ == '__main__':
    asyncio.run(main())