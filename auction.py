bids = []
while True:
    name = input("What is your name: \n")
    price = int(input("What is your price: \n"))

    bid = {
        "name" : name,
        "price" : price
    }
    bids.append(bid)
    nextOne = input("Anyone else ? Yes/No \n").lower()
    if nextOne != "yes":
        break
highest_price = max(bids, key = lambda x : x["price"])
print("This is the Auction Winner: \n")
print(f"Name : {highest_price["name"]}, Price : {highest_price["price"]}")