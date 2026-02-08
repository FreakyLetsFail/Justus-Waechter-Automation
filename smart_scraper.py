import json

class SmartScraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def scrape_product(self, product_id):
        # Simulated resilient scraping logic
        return {"id": product_id, "price": 99.99, "currency": "EUR", "stock": "In Stock"}

if __name__ == "__main__":
    scraper = SmartScraper("https://example-shop.com")
    print(json.dumps(scraper.scrape_product("JUSTUS-123"), indent=2))
