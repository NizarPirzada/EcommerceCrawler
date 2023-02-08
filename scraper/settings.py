from . import enums
from data_storage import enums as db_enums
from pathlib import Path
import os

BASE_DIRECTORY = os.getcwd()
BROWSER = enums.Browser.CHROME.value
DRIVER_PATH = BROWSER
CHROME_UNDETECTED_VERSION = 104

CAPTCHA_EXTENSION = 0
CAPTCHA_EXTENSION_PATH = os.path.join(BASE_DIRECTORY, "anticaptcha-plugin_v0.59.xpi")
CAPTCHA_EXTENSION_KEY = ""

PROXY = 0
PROXY_LIST = [
  
]

CHROME_PROFILE = 0
CHROME_PROFILE_NAME = "Profile 3"
CHROME_PROFILE_DIR_PATH = (
    "user-data-dir=C:\\Users\\Haider\\AppData\\Local\\Google\\Chrome\\User Data\\"
)

CLOUD_SCRAPER_BROWSER_SETTING = [
    {"browser": "firefox", "platform": "windows", "mobile": False},
    {"browser": "firefox", "platform": "linux", "mobile": False},
    {"browser": "chrome", "platform": "windows", "mobile": False},
]

SUPER_CATALOG_TEMPLATES = {
    db_enums.SuperCatalog.TecNec.value: {
        "currency_code": "USD",
        "vendor_info": {
            "website": "https://www.tecnec.com/"
        },
        "login": {
            "is_required": True,
            "url": "https://www.tecnec.com/",
            "methods": [
                """self.driver_click('xpath', '//*[@id="btnlogin"]')""",
                """self.driver_fill_input('xpath', '//*[@id="Secure_Checkout_Email"]', 'asd')""",
                """self.driver_fill_input('xpath', '//*[@id="Secure_Checkout_Password"]', 'asdm8')""",
                """self.driver_click('xpath', '//*[@id="Secure_Checkout_Login"]')""",
            ]
        },
        "brands": {
            "is_required": True,
            "url": "https://www.tecnec.com/shop-by-brand",
            "methods": [],
            "selector_type": enums.SelectorType.SOUP.value,
            "selector_path": {
                "main": "//div[@class=\"collapse\"]//ul/li/a",
            }
        },
        "items": {
            "is_required": True,
            "methods": [
                """self.driver_click("xpath", '//*[@id="View_Selection_Display"]')""",
                """self.driver_click("xpath", '(//*[@id="display_size"]/option)[last()]')""",
                """utils.random_sleep(5, 10)"""
            ],
            "selector_type": enums.SelectorType.SOUP.value,
            "selector_path": {
                "main": ("div", {"class": "cat_item_desc_container"}),
            }
        },
        "item": {
            "is_required": True,
            "methods": [],
            "selector_type": enums.SelectorType.SOUP.value,
            "selector_path": {
                "main": ".product-desc-container",
                "name": "h1",
                "vendor_sku": ".product_sku > span:nth-of-type(1)",
                "manufacturer_sku": ".product_sku > span:nth-of-type(2)",
                "prices": [".product-listprice", ".product-ourprice"]
            }

        }
    }
}






























