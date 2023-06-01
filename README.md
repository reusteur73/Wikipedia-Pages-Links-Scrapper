# Wikipedia-Pages-Links-Scrapper
A powerful Python script for scraping Wikipedia links. It scrapes all available links and is one of the fastest ways to map Wikipedia. The scraped links are saved in a text file.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- requests library
- BeautifulSoup library

You can install the required libraries using pip:

`pip install requests beautifulsoup4`


## Usage

1. Clone the repository or download the source code files.

2. Run the script by executing the following command:

`python scraper.py` 


3. The script will start scraping all Wikipedia pages' links. The links will be saved in a file named `all_wiki_links.txt` in the same directory.

4. Monitor the live stats displayed in the console, including the total number of links found, iteration count, time spent, and any errors encountered during scraping.

5. Once the script finishes, you will have a text file containing all the scraped Wikipedia links.

## Notes

- If you encounter any errors during scraping, the script will continue to the next page. The number of errors encountered will be displayed in the live stats.

- Please be respectful when using this script and comply with Wikipedia's terms of service.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgements

- This script utilizes the [requests](https://docs.python-requests.org/) library for making HTTP requests and the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library for parsing HTML.

- Special thanks to the open-source community for their contributions and support.

