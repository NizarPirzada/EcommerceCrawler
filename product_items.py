import items


class CatalogItem(items.Item):
    brand = items.Field()
    catalogUrl = items.Field()


class ProductItem(items.Item):
    itemName = items.Field()
    itemUrl = items.Field()
    status = items.Field()
    manufacturerSku = items.Field()
    vendorSku = items.Field()
    prices = items.Field()
