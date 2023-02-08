from datetime import datetime
from scraper.super_catalogs import *
from data_storage import enums
from data_storage import utils as db_utils
from data_storage.data_storage import DataStorage

super_catalog_urls = {
    enums.SuperCatalog.Adorama.value: "https://www.adorama.com/brands",
    enums.SuperCatalog.BH.value: "https://www.bhphotovideo.com/c/browse/Shop-by-Brand/ci/9028/N/4291093803",
    enums.SuperCatalog.CCI.value: "https://www.ccisolutions.com/StoreFront/category/shop-by-brand",
    enums.SuperCatalog.CDW.value: "https://www.cdw.com/content/cdw/en/brand.html",
    enums.SuperCatalog.EmpirePro.value: "https://www.empirepro.com/catalog/category/view/s/pro-brands/id/8/",
    enums.SuperCatalog.FullCompass.value: "https://www.fullcompass.com/brands_show_all.php",
    enums.SuperCatalog.OneSourceVideo.value: "https://1sourcevideo.com/shop/index.php/brands",
    enums.SuperCatalog.StageLightingStore.value: "https://www.stagelightingstore.com/shop-by-brand",
    enums.SuperCatalog.SweetWater.value: "https://www.sweetwater.com/store/manufacturer/all",
    enums.SuperCatalog.TecNec.value: "https://www.tecnec.com/shop-by-brand",
}


def scraper(data):
    super_catalog_name = data.get("super_catalog")
    class_name = enums.SuperCatalog(super_catalog_name).name
    constructor = globals()[class_name]
    scraper_obj = constructor()

    scraper_obj.process()
    vendor_info = settings.SUPER_CATALOG_TEMPLATES[enums.SuperCatalog.TecNec.value]["vendor_info"]
    data_storage = DataStorage(vendor_info["website"])
    data_storage.set_items(scraper_obj.items)
    data_storage.save_items()
    scraper_obj.end_process()


def process_super_catalog(data={}):
    vendor_name = data.get("vendor_name")
    catalog_url = data.get("catalog_url")
    class_name = enums.SuperCatalog(vendor_name).name
    constructor = globals()[class_name]
    scraper_obj = constructor()

    scraper_obj.process_brands(catalog_url)

    vendor_info = settings.SUPER_CATALOG_TEMPLATES[enums.SuperCatalog.TecNec.value]["vendor_info"]
    data_storage = DataStorage(vendor_info["website"])

    data_storage.set_catalogs(scraper_obj.brands)
    # data_storage.set_items(scraper_obj.items)
    data_storage.save_catalogs()


def process_catalog(data={}):
    vendor_name = data.get("vendor_name")
    catalog_url = data.get("catalog_url")
    class_name = enums.SuperCatalog(vendor_name).name
    constructor = globals()[class_name]
    scraper_obj = constructor()

    scraper_obj.process_listing(catalog_url)
    vendor_info = settings.SUPER_CATALOG_TEMPLATES[enums.SuperCatalog.TecNec.value]["vendor_info"]
    data_storage = DataStorage(vendor_info["website"])
    data_storage.set_items(scraper_obj.items)
    data_storage.save_items(catalog_url)


def main(data={}):
    is_success = 1
    error_details = ""
    catalog_type = data['catalog_type']
    if catalog_type == db_enums.CatalogType.SuperCatalog.value:
        process_super_catalog(data)
    elif catalog_type == db_enums.CatalogType.Catalog.value:
        process_catalog(data)

    return is_success, error_details


def main_old(data={}):
    data = {
        "super_catalog": enums.SuperCatalog.TecNec.value
    }
    scraper(data)
    return 1
    scraper_obj = TecNec()
    item = CatalogItem(
        name=utils.clean_text("16x9 Inc."),
        catalogUrl="https://www.tecnec.com/brand/16x9-inc",
    )
    scraper_obj.brands.append(item)
    #
    scraper_obj.process_items()

    vendor_info = settings.SUPER_CATALOG_TEMPLATES[enums.SuperCatalog.TecNec.value]["vendor_info"]
    data_storage = DataStorage(vendor_info["website"])
    data_storage.set_items(scraper_obj.items)
    #     data_storage.items = [
    #    {
    #       "itemName": "16x9 NOGA DG9014CA 1/4in-20 Hold-it Articulating Cine Arm",
    #       "itemUrl": "https://www.tecnec.com/product/noga-dg9014ca/16x9-noga-dg9014ca-1-4in-20-hold-it-articulating-cine-arm",
    #       "manufacturerSku": "DG9014CA",
    #       "vendorSku": "NOGA-DG9014CA",
    #       "prices":[
    #          {
    #             "amount":164.00,
    #             "currencyCode": "USD",
    #             "priceType": "MSRP",
    #              "isHistoric": False,
    #              "firstSeen": datetime.utcnow(),
    #              "lastSeen": datetime.utcnow(),
    #          },
    #          {
    #             "amount":133.72,
    #             "currencyCode":"USD",
    #             "priceType":"dealer",
    #              "isHistoric": False,
    #              "firstSeen": datetime.utcnow(),
    #              "lastSeen": datetime.utcnow(),
    #          },
    #          {
    #             "amount":111.72,
    #             "currencyCode":"USD",
    #             "priceType":"discount",
    #              "isHistoric": False,
    #              "firstSeen": datetime.utcnow(),
    #              "lastSeen": datetime.utcnow(),
    #          }
    #       ]
    #    },
    #    {
    #       "itemName":"16x9 ERIG-600-3-A5 EasyRig 3 Gimbal Rig- 600N With 5 Inch Extended Arm for Cameras Weighing 26 - 33 lb. - Standard Vest",
    #       "itemUrl":"https://www.tecnec.com/product/169-erig-600-3a5/16x9-erig-600-3-a5-easyrig-3-gimbal-rig-600n-with-5-inch-extended-arm-for-cameras-weighing-26-33-lb-standard-vest",
    #       "manufacturerSku":"ERIG-600-3-A5",
    #       "vendorSku":"169-ERIG-600-3A5",
    #       "prices":[
    #          {
    #             "amount":4065.00,
    #             "currencyCode":"USD",
    #             "priceType":"MSRP",
    #              "isHistoric": False,
    #              "firstSeen": datetime.utcnow(),
    #              "lastSeen": datetime.utcnow(),
    #          },
    #          {
    #             "amount":3646.68,
    #             "currencyCode":"USD",
    #             "priceType": "dealer",
    #              "isHistoric": False,
    #              "firstSeen": datetime.utcnow(),
    #              "lastSeen": datetime.utcnow(),
    #          }
    #       ]
    #    },
    #    {
    #       "itemName":"16x9 169-HDSF45X-62 EXII 0.45X Super Fisheye 72mm Thread Mount",
    #       "itemUrl":"https://www.tecnec.com/product/169-hdsf45x-72/16x9-169-hdsf45x-62-exii-0-45x-super-fisheye-72mm-thread-mount",
    #       "manufacturerSku":"169-HDSF45X-72",
    #       "vendorSku":"169-HDSF45X-72",
    #       "prices":[
    #          {
    #             "amount":365.00,
    #             "currencyCode":"USD",
    #             "priceType": "MSRP",
    #             "isHistoric": False,
    #             "firstSeen": datetime.utcnow(),
    #             "lastSeen": datetime.utcnow(),
    #          },
    #          {
    #             "amount":297.68,
    #             "currencyCode":"USD",
    #             "priceType":"dealer",
    #             "isHistoric": False,
    #             "firstSeen": datetime.utcnow(),
    #             "lastSeen": datetime.utcnow(),
    #          }
    #       ]
    #    },
    #    {
    #       "itemName":"16x9 169-HDSF45X-62 EXII 0.45X Super Fisheye 77mm Thread Mount",
    #       "itemUrl":"https://www.tecnec.com/product/169-hdsf45x-77/16x9-169-hdsf45x-62-exii-0-45x-super-fisheye-77mm-thread-mount",
    #       "manufacturerSku":"169-HDSF45X-77",
    #       "vendorSku":"169-HDSF45X-77",
    #       "prices":[
    #          {
    #             "amount":365.00,
    #             "currencyCode":"USD",
    #             "priceType":"MSRP",
    #              "isHistoric": False,
    #              "firstSeen": datetime.utcnow(),
    #              "lastSeen": datetime.utcnow(),
    #          },
    #          {
    #             "amount":297.68,
    #             "currencyCode":"USD",
    #             "priceType":"dealer",
    #              "isHistoric": False,
    #              "firstSeen": datetime.utcnow(),
    #              "lastSeen": datetime.utcnow(),
    #          }
    #       ]
    #    },
    #    {
    #       "itemName":"16x9 169-HDSF45X-62 EXII 0.45X Super Fisheye 82mm Thread Mount",
    #       "itemUrl":"https://www.tecnec.com/product/169-hdsf45x-82/16x9-169-hdsf45x-62-exii-0-45x-super-fisheye-82mm-thread-mount",
    #       "manufacturerSku":"169-HDSF45X-82",
    #       "vendorSku":"169-HDSF45X-82",
    #       "prices":[
    #          {
    #             "amount":365.00,
    #             "currencyCode":"USD",
    #             "priceType":"MSRP",
    #              "isHistoric": False,
    #              "firstSeen": datetime.utcnow(),
    #              "lastSeen": datetime.utcnow(),
    #          },
    #          {
    #             "amount":297.68,
    #             "currencyCode":"USD",
    #             "priceType": "dealer",
    #              "isHistoric": False,
    #              "firstSeen": datetime.utcnow(),
    #              "lastSeen": datetime.utcnow(),
    #          }
    #       ]
    #    },
    #    {
    #       "itemName":"16x9 169-HDWA6X-82 EXII 0.6X Wide Attachment - 82mm Thread Mount",
    #       "itemUrl":"https://www.tecnec.com/product/169-hdwa6x-82/16x9-169-hdwa6x-82-exii-0-6x-wide-attachment-82mm-thread-mount",
    #       "manufacturerSku":"169-HDWA6X-82",
    #       "vendorSku":"169-HDWA6X-82",
    #       "prices": [
    #          {
    #             "amount":345.00,
    #             "currencyCode":"USD",
    #             "priceType": "MSRP",
    #              "isHistoric": False,
    #              "firstSeen": datetime.utcnow(),
    #              "lastSeen": datetime.utcnow(),
    #          },
    #          {
    #             "amount":260.47,
    #             "currencyCode":"USD",
    #             "priceType": "dealer",
    #              "isHistoric": False,
    #              "firstSeen": datetime.utcnow(),
    #              "lastSeen": datetime.utcnow(),
    #          }
    #       ]
    #    }
    # ]

    # data_storage.save_items()


def rough():
    from bs4 import BeautifulSoup

    ### FOR PRICES
    html_string = """
    <div id="product-pricing"><p class="product-variable">Weight: <span id="Variant0Weight">0.25</span></p><p class="product-listprice"><span id="Variant0ListTitle">List Price:</span> <span id="Variant0ListValue">$299.00</span></p><div id="CustomMessageContainer" style="display:none"><div class="clear">&nbsp;</div><p class="product-availability">Availability: <span id="Variant0Stock" class="instock">3 In Stock</span><span class="instock availability_icon" title="Item is Available for immediate shipping from our warehouse."><img src="https://www.tecnec.com/assets/images/AvbInfo.png" class="infoimg" alt="Availability Information" /></span></p><p class="productmobile-availability">Item is Available for immediate shipping from our warehouse.</p><p class="product-note"></p><p  class="product-warningmsg">California Residents:<br/><img src="https://www.tecnec.com/assets/images/8pt-triangle.png" class="triimg" alt="" /><span><span class="warn">WARNING</span>: Cancer and Reproductive Harm<br/><a href="http://www.p65warnings.ca.gov/" target="_blank">www.P65Warnings.ca.gov</a></span></p></div><div id="ProductDataContainerPart1" ><p class="product-listprice"><span id="Variant0Price1Title">Dealer Price:</span> <span id="Variant0Price1Value" style="text-decoration:line-through;" >$279.00</span></p><p class="product-ourprice"><span id="Variant0Price2Title">Special Price:</span> <span id="Variant0Price2Value" style="color:#cc0000;">$39.00</span></p><div class="product-actions"><div class="cart-item-qty">Quantity:<input type="text" class="qty_input" name="Quantity" id="Quantity" value="1" maxlength="4" onkeypress="javascript:return isNumber(event)" onblur="javascript:return isNumber(event)" /></div><div class="add-to-cart"><input type="button" id="AddToCart" value="Add To Cart" class="btn btn-primary btn-lg gtm_tn_addtocart" /><br /><a id="AddToWishlist" class="wish-list gtm_tn_addtowishlist" href="javascript:AddToWishlist('WI-SE-32','')"> Add to Wish List</a><a id="AddToQuote" class="add_to_link" style="display:none" href="#"> + Add to Quote</a></div></div><div id="ProductDataContainerPart2" ><p class="product-availability">Availability: <span id="Variant0Stock" class="instock stockstatus">3 In Stock</span><span class="instock availability_icon" title="Item is Available for immediate shipping from our warehouse."><img src="https://www.tecnec.com/assets/images/AvbInfo.png" class="infoimg" alt="Availability Information" /></span></p><p class="productmobile-availability">Item is Available for immediate shipping from our warehouse.</p><p class="product-note"></p><p style="display:none" class="product-qty"><span id="Variant0QtyDiscount" class="price_label qty_label"><a class="quantity-pricing" href="javascript:ShowQuantityPricing('WI-SE-32')" rel="nofollow">Quantity Pricing</a></span><div style="display:none" id="QtySummary"></div></p><p  class="product-warningmsg">California Residents:<br/><img src="https://www.tecnec.com/assets/images/8pt-triangle.png" class="triimg" alt="" /><span><span class="warn">WARNING</span>: Cancer and Reproductive Harm<br/><a href="http://www.p65warnings.ca.gov/" target="_blank">www.P65Warnings.ca.gov</a></span></p></div></div></div></div></div>
    """
    soup = BeautifulSoup(html_string)
    prices_path = [".product-listprice", ".product-ourprice"]
    for price_path in prices_path:
        price_elems = soup.select(price_path)

        for price_elem in price_elems:
            price_type, amount = price_elem.text.split(':')[:2]
            price_type = db_utils.clean_text(price_type)
            amount = db_utils.clean_text(amount)
            print(price_type, db_utils.clean_amount(amount))

    ###

    html_string = """
    <p class="product_sku">Item #: <span id="Variant0ItemID">WI-SE-32</span><span id="Variant0VendorId" class="hidden-xs">&nbsp; • &nbsp; MFG #: WI-SE-32</span><span id="Variant0MobVendorId" class="visible-xs">MFG #: WI-SE-32</span></p>
    """
    soup = BeautifulSoup(html_string)
    vendor_sku_path = ".product_sku > span:nth-of-type(1)"
    manufacturer_sku_path = ".product_sku > span:nth-of-type(2)"

    vendor_sku = soup.select_one(vendor_sku_path).text
    vendor_sku = db_utils.clean_text(vendor_sku)

    manufacturer_sku = soup.select_one(manufacturer_sku_path).text
    manufacturer_sku = db_utils.clean_text(manufacturer_sku)
    manufacturer_sku = db_utils.clean_manufacturer_sku(manufacturer_sku)
    print(vendor_sku)
    print(manufacturer_sku)


if __name__ == "__main__":
    # data = {
    #     "catalog_url": "https://www.tecnec.com/shop-by-brand",
    #     "catalog_type": "SuperCatalog",
    #     "firestore_task_id": "/Vendors/9b27bf7ed43d426dbc5b2287b9718e53/Catalogs/58973f23d33d4a77ba1bf70769c63996/Tasks/CmsI0cZY7nqkyzqrKpxP",
    #     "vendor_name": "TecNec"
    # }
    data = {
        "catalog_url": "https://www.tecnec.com/brand/ily-enterprise-inc",
        "catalog_type": "Catalog",
        "firestore_task_id": "/Vendors/9b27bf7ed43d426dbc5b2287b9718e53/Catalogs/58973f23d33d4a77ba1bf70769c63996/Tasks/Z9BSTGuVDir5RWFzjVOz",
        "vendor_name": "TecNec"
    }
    main(data)


    # vendor_info = settings.SUPER_CATALOG_TEMPLATES[enums.SuperCatalog.TecNec.value]["vendor_info"]
    # data_storage = DataStorage(vendor_info["website"])
    # data_storage.update_actor_time("", "actorEndTime")

    # rough()
