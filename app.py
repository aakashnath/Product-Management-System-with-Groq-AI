'''
product management system using python
dictionary with Gen AI (GROQ)

------------------------------------------------

Deliverables/Expectations:

1. add product
2. view product
3. Search product
4. Update product
5. Delete product
6. AI Insights (GROQ)

----------------------------------------

'''

from groq import Groq

# Blank Dictionary object for product storage

products = {}


def load_dummy_data():

    '''
    LOAD SAMPLE DATA
    '''

    products[0] = {"name": "Laptop", "price": 40000}
    products[1] = {"name": "Smartphone", "price": 22000}
    products[2] = {"name": "Tablet", "price": 18000}
    products[3] = {"name": "Smart TV", "price": 55000}
    products[4] = {"name": "Bluetooth Speaker", "price": 3500}
    products[5] = {"name": "Wireless Headphones", "price": 4500}
    products[6] = {"name": "Gaming Mouse", "price": 1800}
    products[7] = {"name": "Mechanical Keyboard", "price": 4200}
    products[8] = {"name": "External Hard Disk", "price": 6200}
    products[9] = {"name": "USB Pen Drive", "price": 850}
    products[10] = {"name": "Webcam", "price": 2700}
    products[11] = {"name": "WiFi Router", "price": 3200}
    products[12] = {"name": "Printer", "price": 9800}
    products[13] = {"name": "Monitor", "price": 14500}
    products[14] = {"name": "Power Bank", "price": 1200}
    products[15] = {"name": "Smart Watch", "price": 6000}
    products[16] = {"name": "Microphone", "price": 2500}
    products[17] = {"name": "Graphics Card", "price": 35000}
    products[18] = {"name": "SSD 1TB", "price": 7500}
    products[19] = {"name": "CPU Cooler", "price": 2800}

    return "20 Dummy Products Loaded Successfully."


def display_products():

    if len(products) == 0:
        return "No products available"

    output = ""

    for pid in products:
        output += f"ID: {pid}, Name : {products[pid]['name']}, Price : {products[pid]['price']}\n"

    return output


def add_product(pid, name, price):
    '''
    ADD PRODUCT
    '''

    pid = int(pid)
    price = float(price)

    if pid in products:
        return "Product ID already exists!!!"

    else:
        products[pid] = {"name": name, "price": price}
        return "Product successfully added..."


def search_product(pid):
    '''
    Search Product
    '''

    pid = int(pid)

    if pid in products:
        return f"ID: {pid}, Name : {products[pid]['name']}, Price : {products[pid]['price']}"

    else:
        return "Product not found..."


def update_product(pid, name, price):
    '''
    Update Product
    '''

    pid = int(pid)
    price = float(price)

    if pid in products:

        products[pid]["name"] = name
        products[pid]["price"] = price

        return "Product Updated..."

    else:
        return "Product not found..."


def delete_product(pid):
    '''
    Delete Product
    '''

    pid = int(pid)

    if pid in products:
        del products[pid]
        return "Product Deleted..."

    else:
        return "Product not found..."


def ai_product_details(query):
    '''
    GROQ API ENGAGEMENT
    '''

    client = Groq(
        api_key='YOUR_NEW_GROQ_API_KEY'
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful product assistant"
            },
            {
                "role": "user",
                "content": query
            }
        ]
    )

    return response.choices[0].message.content


def dashboard():
    '''
    DASHBOARD USING MATCH CASE
    '''

    while True:
        print("\n----------- PRODUCT MANAGEMENT -----------\n")
        print("1. View Products")
        print("2. Add Products")
        print("3. Search Products")
        print("4. Update Products")
        print("5. Delete Products")
        print("6. AI Products Help(GROQ)")
        print("7. Exit")

        choice = int(input("Enter Choice:- "))

        match choice:

            case 1:
                print(display_products())

            case 2:
                pid = input("Enter Product ID : ")
                name = input("Enter Product Name : ")
                price = input("Enter Product Price : ")
                print(add_product(pid, name, price))

            case 3:
                pid = input("Enter Product ID : ")
                print(search_product(pid))

            case 4:
                pid = input("Enter Product ID : ")
                name = input("Enter Product Name : ")
                price = input("Enter Product Price : ")
                print(update_product(pid, name, price))

            case 5:
                pid = input("Enter Product ID : ")
                print(delete_product(pid))

            case 6:
                query = input("Ask anything about products : ")
                print(ai_product_details(query))

            case 7:
                print("TATA BYE BYE")
                break

            case _:
                print("INVALID CHOICE")


def main():
    load_dummy_data()
    dashboard()


if __name__ == "__main__":
    main()