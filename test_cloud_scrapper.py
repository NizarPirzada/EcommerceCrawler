import cloudscraper
from bs4 import BeautifulSoup
from scraper import utils
from product_items import CatalogItem, ProductItem
import json
import copy

from data_storage import db
from data_storage import settings as db_settings
from data_storage import enums as db_enums
from data_storage import utils as db_utils

actor_id = db_settings.ACTOR_SETTINGS["id"]
super_catalog = db_enums.SuperCatalog.BH.value

default_catalog_data = {
    "_createdBy": {
        "actorId": actor_id,
        "displayName": None,
        "email": db_settings.ACTOR_SETTINGS["email"],
        "emailVerified": True,
        "isAnonymous": False,
        "photoURL": None,
        "timestamp": None,
        "uid": db_settings.ACTOR_SETTINGS["uid"],
    },
    "_updatedBy": {
        "actorId": actor_id,
        "displayName": None,
        "email": db_settings.ACTOR_SETTINGS["email"],
        "emailVerified": True,
        "isAnonymous": False,
        "photoURL": None,
        "timestamp": None,
        "uid": db_settings.ACTOR_SETTINGS["uid"],
    },
    "actorId": actor_id,
    "actorSchedule": None,
    "brand": None,
    "parentId": None,
    "catalogUrl": "",
    "type": db_enums.CatalogType.Catalog.value,
    "vendor": "",
}


def save_data_to_catalog(brands):
    query_obj = [
        {
            "field": "type",
            "operator": "==",
            "value": db_enums.CatalogType.SuperCatalog.value,
        },
        {
            "field": "actorId",
            "operator": "==",
            "value": actor_id,
        },
        {
            "field": "vendor",
            "operator": "==",
            "value": db_enums.SuperCatalog.BH.value,
        },
    ]
    super_catalog_docs = db.get_data(db_enums.Collections.Catalogs.value, query_obj)
    vendor = parent_id = None
    for super_catalog_doc in super_catalog_docs:
        parent_id = super_catalog_doc.id
        vendor = super_catalog_doc._data["vendor"]
        break

    super_catalog_data = copy.deepcopy(default_catalog_data)
    super_catalog_data["vendor"] = vendor
    super_catalog_data["parentId"] = parent_id
    brands_dic = utils.convert_class_objects_to_list_dic(brands)
    catalog_data_list = []

    for brand in brands_dic:
        query_data = [
            {
                "field": "actorId",
                "operator": "==",
                "value": actor_id,
            },
            {
                "field": "vendor",
                "operator": "==",
                "value": vendor,
            },
            {
                "field": "type",
                "operator": "==",
                "value": db_enums.CatalogType.Catalog.value,
            },
            {
                "field": "brand",
                "operator": "==",
                "value": brand["BrandName"],
            },
        ]
        catalog_data = copy.deepcopy(super_catalog_data)
        catalog_data["_createdBy"]["timestamp"] = db_utils.get_current_time()
        catalog_data["_updatedBy"]["timestamp"] = db_utils.get_current_time()
        catalog_data["actorSchedule"] = db_enums.ActorSchedules.RANDOM.value
        catalog_data["catalogUrl"] = brand["TargetURL"]
        catalog_data["brand"] = brand["BrandName"]
        catalog_data_list.append(catalog_data)

        # db.save_data(db_enums.Collections.Catalogs.value, catalog_data)
        db.save_update_data("test", query_data, catalog_data)
    # db.save_batch_data("test", catalog_data_list)


url = "https://www.bhphotovideo.com/c/browse/Shop-by-Brand/ci/9028/N/4291093803"
domain_url = "https://www.bhphotovideo.com"
count = 1
brands_selector = "sbb_listWrapper"
brand_counter = 0
brands = []
browser_setting = [
    {"browser": "firefox", "platform": "windows", "mobile": False},
    {"browser": "firefox", "platform": "linux", "mobile": False},
    {"browser": "chrome", "platform": "windows", "mobile": False},
]
PROXY_LIST = [
    "179.43.137.230:8800",
    "179.43.137.35:8800",
    "154.37.248.147:8800",
    "185.189.36.146:8800",
]


# request_text = requests.get(url).text
rand_num = utils.get_random_number(0, 2)
scraper = cloudscraper.create_scraper(
    delay=utils.get_random_number(8, 15),
    browser=browser_setting[0],
)
cloud_scraper_text = scraper.get(url).text

soup = BeautifulSoup(cloud_scraper_text, "html5lib")
brand_row_elements = soup.find_all("ul", {"class": brands_selector})
for brand_row_element in brand_row_elements:
    a_tags = brand_row_element.find_all("a")
    for a_tag in a_tags:
        try:
            brand_counter += 1
            item = CatalogItem(
                Item=brand_counter, BrandName=a_tag.text, TargetURL=a_tag["href"]
            )
            brands.append(item)
        except:
            brand_counter -= 1


###########
save_data_to_catalog(brands)


###########
# brands_dic = utils.convert_class_objects_to_list_dic(brands)
# with open(f"Data/Brands/BHBrands.json", "w") as f:
#     json.dump(brands_dic, f)
