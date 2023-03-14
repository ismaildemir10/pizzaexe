import csv
from datetime import datetime

class pizza:
    def __init__(self, description, cost):
     description = self.description
     cost = self.cost
    def get_discription(self):
        return self.description
    def get_cost(self):
        return self.cost
#pizza alt sınıfları
class Klasik_pizza(pizza):
    def __init__(self):
        super().__init__('klasik pizza', 10)
class Margarita_pizza(pizza):
    def __init__(self):
        super().__init__('margarita pizza(mozarella peynirli)', 11)
class Turk_pizza(pizza):
    def __init__(self):
        super().__init__('turk pizza(içerisinde sucuk sosis pastırma bulunur) ', 12)
class Sade_pizza(pizza):
    def __init__(self):
        super().__init__('sade pizza', 13)
#sos sınıfı
class decorator(pizza):
    def __init__(self, description, cost):
        description = self.description
        cost = self.cost
#alt sınıfı
class Zeytin(decorator):
    def __init__(self):
        super().__init__('Extram Zeytin', 1)
class Mantar(decorator):
    def __init__(self):
        super().__init__('Extra Mantar', 1)
class Keci_peyniri(decorator):
    def __init__(self):
        super().__init__('Extra Keci Peyniri', 1)
class Et(decorator):
    def __init__(self):
        super().__init__('Extra Et',3)
class Sogan(decorator):
    def __init__(self):
        super().__init__('Soğan', 0.5)
class Misir(decorator):
    def __init__(self):
        super().__init__('Mısır', 0.5)
def csv_yaz(isim, TC, Kart, pizzas, sos,sifre):
    date_time = datetime.datetime.now()
    with open('Orders_Database.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f"ADI= {isim}, kimlik no= {TC}, KART NUMARASI= {Kart}, PIZZASI= {pizzas}, SOSU= {sos}, UCRETI= {fiyat}, TARIHI= {date_time.strftime('%Y-%m-%d %H:%M:%S')}"
def main():
    dosya = open("menü.txt", "w", encoding='utf-8')
    dosya.write("*Lütfen bir pizza tabani seçiniz\n 1: Klasik\n 2: Margarita\n 3: Türk Pizza\n 4: Sade Pizza\n * Lütfen Sos seçiniz\n 11: Zeytin\n 12: Mantar\n 13: Keçi Peyniri\n 14: Et\n 15: Soğan\n  16: Mısır\n * Bizi seçtiğiniz için teşekkürler")
    dosya = open ("menü.txt", "r", encoding='utf-8')
    menu = dosya.read()
    print(menu)
pizzas = None
pizzas = int(input('\nLutfen pizza seciniz: '))
if pizzas == 1:
   pizzas = Klasik_pizza()
elif pizzas == 2:
   pizzas = Margarita_pizza()
elif pizzas == 3:
   pizzas = Turk_pizza()
elif pizzas == 4:
    pizzas = Sade_pizza()

sos = int(input('\nLutfen sosunuzu seciniz: '))
if sos == 11:
        pizzas = Zeytin(pizza)
elif sos == 12:
        pizzas = Mantar(pizza)
elif sos == 13:
        pizzas = Keci_peyniri(pizza)
elif sos == 14:
        pizzas = Et(pizza)
elif sos == 15:
        pizzas = Sogan(pizza)
elif sos == 16:
        pizzas = Misir(pizza)
fiyat = pizzas + sos
print("ödeyeceğiniz tutar = " fiyat)

isim =(input('1Lutfen isminizi girin: '))
TC = int(input(('Lutfen TC girin: ')))
Kart = int(input('Lutfen kart numaranizi girin: '))
sifre = int(input('Lutfen kredi karti sifrenizi girin: '))
