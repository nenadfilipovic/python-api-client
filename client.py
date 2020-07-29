import json

import requests


class APIClient:
    def __init__(self, url):
        self.url = url

    def create_item(self):
        item_props = {}
        key_list = ["item_sku", "item_name", "item_price", "item_quantity"]
        for key in key_list:
            print("Please enter value for:", key)
            value = input()
            print(key, " : ", value)
            item_props[key] = value
        print("Sending request...")
        response = requests.post(self.url, data=json.dumps(item_props))
        print(response.json())
        print("Get back to menu? y/n")
        back = input()
        if back == "y":
            self.choise()
        else:
            quit()

    def update_item(self):
        print("Input ID of the item you want to update.")
        item_id = input()
        item_props = {}
        key_list = ["item_sku", "item_name", "item_price", "item_quantity"]
        for key in key_list:
            print("Please enter value for:", key)
            value = input()
            print(key, " : ", value)
            item_props[key] = value
        print("Sending request...")
        response = requests.put((self.url + '?id=' + item_id), data=json.dumps(item_props))
        print(response.json())
        print("Get back to menu? y/n")
        back = input()
        if back == "y":
            self.choise()
        else:
            quit()

    def get_item(self):
        print("Input ID of the item you want to view.")
        item_id = input()
        print("Sending request...")
        response = requests.get(self.url + '?id=' + item_id)
        print(response.json())
        print("Get back to menu? y/n")
        back = input()
        if back == "y":
            self.choise()
        else:
            quit()

    def choise(self):
        print("Hello, select option:")
        print("1. Get all items.")
        print("2. Get specific item.")
        print("3. Create new item.")
        print("4. Update item.")
        print("5. Delete item.")
        print("6. Quit.")
        choise = input()
        if choise == '1':
            self.get_items()
        elif choise == '2':
            self.get_item()
        elif choise == '3':
            self.create_item()
        elif choise == '4':
            self.update_item()
        elif choise == '5':
            self.delete_item()
        elif choise == '6':
            quit()
        else:
            print("That menu item doesnt exist.")
            self.choise()

    def get_items(self):
        print("Listing all items...\n")
        response = requests.get(self.url)
        x = list(response.json())
        for elem in x:
            print(elem)
        print("Get back to menu? y/n")
        back = input()
        if back == "y":
            self.choise()
        else:
            quit()

    def delete_item(self):
        print("Input ID of the item you want to delete.")
        item_id = input()
        print("Sending request...")
        response = requests.delete(self.url + '?id=' + item_id)
        print(response.json())
        print("Get back to menu? y/n")
        back = input()
        if back == "y":
            self.choise()
        else:
            quit()


def start():
    client = APIClient("https://www.nenadfilipovic.site/api/v1/storeItems.php")
    client.choise()


start()
