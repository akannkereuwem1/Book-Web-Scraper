# Books Web Scraper

A professional Scrapy-based web scraping project for extracting book data from [Books to Scrape](https://books.toscrape.com/), storing results in MongoDB, and supporting robust, scalable data collection.

## Features
- Scrapes book title, price, and URL from all pages of books.toscrape.com
- MongoDB integration with upsert logic to avoid duplicates
- Configurable settings for concurrency, delays, and logging
- Modular, extensible pipeline and item structure

## Project Structure
```
books/
├── scrapy.cfg
└── books/
	 ├── __init__.py
	 ├── items.py
	 ├── middlewares.py
	 ├── pipelines.py
	 ├── settings.py
	 └── spiders/
		  ├── __init__.py
		  └── book.py
```

## Getting Started

### Prerequisites
- Python 3.7+
- [Scrapy](https://scrapy.org/)
- [pymongo](https://pymongo.readthedocs.io/en/stable/)
- MongoDB running locally or accessible remotely

### Installation
1. Clone the repository:
	```bash
	git clone https://github.com/akannkereuwem1/Book-Web-Scraper.git
	cd Web-Scraping/books
	```
2. Install dependencies:
	```bash
	pip install scrapy pymongo
	```
3. Ensure MongoDB is running (default: `mongodb://localhost:27017`)

### Configuration
- Edit `books/settings.py` to adjust MongoDB URI, database name, and other Scrapy settings as needed.

### Running the Spider
From the `books` directory, run:
```bash
scrapy crawl book
```

## Output
- Scraped data is stored in the `books` collection of the `books_db` MongoDB database.
- Logs are written to `book_scraper.log`.

## Customization
- To change scraped fields, edit `books/items.py` and update selectors in `books/spiders/book.py`.
- To modify MongoDB logic, see `books/pipelines.py`.

## Troubleshooting
- If no data appears in MongoDB, check:
  - Scrapy logs for errors
  - MongoDB connection settings
  - That the pipeline is enabled in `settings.py`
- For more verbose logs, set `LOG_LEVEL = "INFO"` in `settings.py`.

## License
MIT License

## Acknowledgments
- [Books to Scrape](https://books.toscrape.com/) for the demo site
- [Scrapy Documentation](https://docs.scrapy.org/)
- [PyMongo Documentation](https://pymongo.readthedocs.io/)

