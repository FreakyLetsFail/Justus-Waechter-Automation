"""
E-Commerce Price Monitor
Automatically tracks product prices across multiple platforms
"""
import json
import time
from datetime import datetime
from typing import Dict, List

class ProductMonitor:
    def __init__(self, products: List[Dict]):
        self.products = products
        self.history = []
    
    def check_prices(self) -> List[Dict]:
        """Simulate price checking across multiple sites"""
        results = []
        
        for product in self.products:
            # In production: use requests + BeautifulSoup/Playwright here
            price_data = {
                "product_id": product["id"],
                "name": product["name"],
                "current_price": product["base_price"] * 0.95,  # Simulated discount
                "original_price": product["base_price"],
                "currency": "EUR",
                "in_stock": True,
                "timestamp": datetime.now().isoformat(),
                "url": product["url"]
            }
            results.append(price_data)
            self.history.append(price_data)
        
        return results
    
    def get_price_drops(self, threshold: float = 0.10) -> List[Dict]:
        """Find products with significant price drops"""
        drops = []
        for product in self.products:
            recent = [h for h in self.history if h["product_id"] == product["id"]]
            if len(recent) >= 2:
                old_price = recent[-2]["current_price"]
                new_price = recent[-1]["current_price"]
                drop_pct = (old_price - new_price) / old_price
                
                if drop_pct >= threshold:
                    drops.append({
                        "product": product["name"],
                        "old_price": old_price,
                        "new_price": new_price,
                        "savings": old_price - new_price,
                        "drop_percentage": f"{drop_pct*100:.1f}%"
                    })
        return drops

# Demo usage
if __name__ == "__main__":
    # Example: Monitor ImmobilienScout24 listings (simulated)
    demo_products = [
        {
            "id": "immo_001",
            "name": "3-Zimmer Wohnung Bonn Zentrum",
            "base_price": 450000,
            "url": "https://www.immobilienscout24.de/expose/123456"
        },
        {
            "id": "immo_002", 
            "name": "Einfamilienhaus Bad Godesberg",
            "base_price": 750000,
            "url": "https://www.immobilienscout24.de/expose/789012"
        }
    ]
    
    monitor = ProductMonitor(demo_products)
    
    print("🔍 E-Commerce Price Monitor - Demo")
    print("=" * 50)
    
    # First check
    print("\n📊 Initial scan...")
    results = monitor.check_prices()
    for r in results:
        print(f"  • {r['name']}: {r['current_price']:,.0f} EUR")
    
    # Simulate price change
    time.sleep(1)
    demo_products[0]["base_price"] = 425000  # Price drop!
    
    # Second check
    print("\n🔄 Re-scanning (after 24h)...")
    results = monitor.check_prices()
    
    # Check for drops
    drops = monitor.get_price_drops(threshold=0.05)
    if drops:
        print("\n🎯 PRICE ALERTS:")
        for drop in drops:
            print(f"  💰 {drop['product']}")
            print(f"     Was: {drop['old_price']:,.0f} EUR → Now: {drop['new_price']:,.0f} EUR")
            print(f"     You save: {drop['savings']:,.0f} EUR ({drop['drop_percentage']})")
    
    print("\n✅ Demo complete! In production, this runs automatically every 6 hours.")
    print("   Results can be sent via email, Telegram, or saved to database.")
