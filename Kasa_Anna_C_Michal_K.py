import os  

import datetime

class VirtualStore:
    def __init__(self):
        self.products = {}
        self.basket = {}

    def display_product_list(self):
        os.system('cls' if os.name == 'nt' else 'clear')  
        print("LISTA WSZYSTKICH PRODUKTÓW")
        for code, details in self.products.items():
            print(f"{code} {details['name']} - Cena: {details['price']} PLN")

    def shopping(self):
        total_amount = 0
        total_vat = 0
        receipt_generated = False  

        os.system('cls' if os.name == 'nt' else 'clear')  
        print("\nRozpoczęto zakupy.")

        while not receipt_generated:  
            code = input("KOD KRESKOWY LUB WYDRUK PARAGONU (P): ").upper()
            
            if code == 'P':
                self.generate_receipt()
                receipt_generated = True  
            elif code in self.products:
                product_details = self.products[code]
                name = product_details['name']
                price = product_details['price']
                currency = product_details['currency']
                if code in self.basket:
                    self.basket[code]['quantity'] += 1
                else:
                    self.basket[code] = {'name': name, 'price': price, 'quantity': 1}

                total_amount += price
                total_vat += 0.23 * price

                os.system('cls' if os.name == 'nt' else 'clear')  
                print(f"Zeskanowano: {name} - Cena: {price} PLN")
                print(f"CENA ŁĄCZNA: {total_amount} PLN")
            else:
                print('\x1b[38;2;255;0;0m\x1b0' + 'NIEPRAWIDŁOWY KOD PRODUKTU' + '\x1b[0m')

    def generate_receipt(self):
        os.system('cls' if os.name == 'nt' else 'clear')  
        print("\n---------------------------------")
        print("PARAGON")
        print(f"DATA ZAKUPU: {datetime.date.today().strftime('%d.%m.%Y')}")
        print("---------------------------------")

        for code, item in self.basket.items():
            print(f"\n{item['name']} | {item['price'] * item['quantity']:.2f} zł")

        total_amount = sum(item['price'] * item['quantity'] for item in self.basket.values())
        total_vat = sum(0.23 * item['price'] * item['quantity'] for item in self.basket.values())

        print("\n---------------------------------")
        print(f"DO ZAPŁATY: {total_amount:.2f} zł")
        print(f"W TYM VAT: {round(total_vat, 2):.2f} zł")
        print("---------------------------------")
        
        
        exit()

if __name__ == "__main__":
    store = VirtualStore()
    print("WITAJ W NASZYM SKLEPIE!")

    store.products = {
    '001': {'name': 'Masło Extra', 'price': 8.00, 'currency': 'PLN'},
    '002': {'name': 'Chleb Wiejski', 'price': 4.50, 'currency': 'PLN'},
    '003': {'name': 'Makaron Babuni', 'price': 9.20, 'currency': 'PLN'},
    '004': {'name': 'Dżem Truskawkowy', 'price': 8.10, 'currency': 'PLN'},
    '005': {'name': 'Kiełbasa Myśliwska', 'price': 29.00, 'currency': 'PLN'},
    '006': {'name': 'Szynka Konserwowa', 'price': 22.00, 'currency': 'PLN'},
    '007': {'name': 'Chipsy Paprykowe', 'price': 6.00, 'currency': 'PLN'},
    '008': {'name': 'Serek Wiejski', 'price': 3.50, 'currency': 'PLN'},
    '009': {'name': 'Sól Kuchenna', 'price': 2.70, 'currency': 'PLN'},
    '010': {'name': 'Cukier Kryształ', 'price': 3.20, 'currency': 'PLN'},
    }

    while True:
        print("\nWYBIERZ OPCJĘ:")
        print("\n1 => LISTA WSZYSTKICH PRODUKTÓW")
        print("2 => ZAKUPY")
        print("3 => ZAKOŃCZ PROGRAM")

        choice = input("WYBIERZ 1, 2 LUB 3: ")

        if choice == '1':
            store.display_product_list()
        elif choice == '2':
            store.shopping()
        elif choice == '3':
            print("Zakończono program.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

#Anna Czechowicz
#Michał Korczyński
                        