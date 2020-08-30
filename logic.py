import requests
import MCUuid


def logic(item):
    prices = []

    num_pages = requests.get("https://api.hypixel.net/skyblock/auctions?page=2").json()
    num_pages = num_pages["totalPages"]

    pages = [] * num_pages

    for i in range(0, num_pages):
        pages.append(requests.get("https://api.hypixel.net/skyblock/auctions?page=" + i.__str__()).json())
        if not pages[i]["success"]:
            print(pages[i]["success"])
            pass
    print("1")
    for i in range(0, len(pages)):
        for j in range(0, len(pages[i]["auctions"])):
            if pages[i]["auctions"][j]["item_name"] == item:
                # if pages[i]["auctions"][j]["highest_bid_amount"] != 0:
                if pages[i]["auctions"][j]["end"] - pages[i]["lastUpdated"] <= 2800000:
                    prices.append(int(pages[i]["auctions"][j]["highest_bid_amount"]))
                    print("adding to list")

    if len(prices) == 0:
        print("brak itemów lub zła nazwa")
        return "no items or wrong name"

    averagePrice = MCUuid.Average(prices)

    print(averagePrice)
    print(prices)

    prices = []

    for i in range(0, len(pages)):
        for j in range(0, len(pages[i]["auctions"])):
            if pages[i]["auctions"][j]["item_name"] == item:
                # if pages[i]["auctions"][j]["highest_bid_amount"] != 0:
                if pages[i]["auctions"][j]["end"] - pages[i]["lastUpdated"] <= 1800000:
                    if pages[i]["auctions"][j]["highest_bid_amount"] < averagePrice:
                        prices.append(pages[i]["auctions"][j])

    if len(prices) == 0:
        print("no items")
        return "no items or wrong name"

    oldPrice = 50000000000000

    if len(prices) > 1:
        for i in range(len(prices)):
            if prices[i]["highest_bid_amount"] < oldPrice:
                oldPrice = prices[i]["highest_bid_amount"]
                bestPriceName = MCUuid.getName(prices[i]["auctioneer"])
                return bestPriceName
    else:
        print(prices[0]["uuid"])
        return MCUuid.getName(pages[0]["auctioneer"])
