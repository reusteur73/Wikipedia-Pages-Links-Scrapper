import requests, sys, time
from bs4 import BeautifulSoup

def save_page_links(links):
    """
    Function to save links in text file.
    """
    with open("all_wiki_links.txt", "a", encoding="utf-8") as file:
        for link in links:
            file.write(f"{link}\n")

def main():
    """
    Main function that scrape all Wikipedia pages links.
    """

    # Setup main domain
    main_path = "https://en.wikipedia.org"
    # Initialise first webpage and total links found
    next_page_link = "/wiki/Special:AllPages"
    total_links_found = 0
    iteration = 0
    errors = 0
    start_time = time.time()
    while True:
        try:
            # Initialise links list
            links_found = []

            # Get source of page
            source_code = requests.get(f"{main_path}{next_page_link}").content
            soup = BeautifulSoup(source_code, "html.parser")

            # Get only the mw-allpages-body wich contain all links
            paragraphes = soup.find(class_="mw-allpages-body")

            # Get all <a> tags
            links = paragraphes.find_all("a")

            # Grab href from all <a> tags and add to list
            for link in links:
                wiki_link = link.get("href")
                if "/wiki/" in wiki_link:
                    links_found.append(wiki_link)

            # Find and set next page
            next_page = soup.find(class_="mw-allpages-nav")
            next_page_link = next_page.find("a").get("href")

            # Save all links scrapped in text file
            save_page_links(links_found)

            # Increment to show live stats
            total_links_found += len(links_found)
            iteration += 1
            time_spend = round((time.time() - start_time), 2)
        except:
            errors += 1
            pass

        # Show live stats
        sys.stdout.write(f"Total links founds: {total_links_found} | Iteration: {iteration} | Time spend: {time_spend}s | Errors: {errors}            \r")
        sys.stdout.flush()

main()

    
