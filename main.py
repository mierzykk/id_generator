import time
import json
import random
ok = time.localtime()
year_ = ok.tm_year
miesiac_ = ok.tm_mon
dzien_ = ok.tm_mday
del ok

def liczby(wybory:int, tekst:str):
    wybory = int(wybory)
    while True:
        try:
            pick = int(input(tekst))
            for i in range(1,wybory+1):
                if pick == i:
                    pick = int(pick)
                    return pick
            print("nie ma takiego wyboru")
        except ValueError:
            print("nie ma takiego wyboru")
"""def liczmiesiac(miesiac, wiek, dzien):
    datamiesiac = miesiac
    if (miesiac_ < miesiac) or (miesiac_ == miesiac and dzien_ < dzien):
        datarok = year_ - wiek - 1
    else:
        datarok = year_ - wiek
        
    return datamiesiac, datarok"""

"""def dni(dzien, miesiac):
    if dzien < dzien_:
        if miesiac == 1:
            miesiac = 12
        else:
            miesiac -= 1
        if miesiac == 2:
            dni_w_miesiacu = 28
        elif miesiac == 8:
            dni_w_miesiacu = 31
        elif miesiac < 8:
            dni_w_miesiacu = 31 if miesiac % 2 == 1 else 30
        else:
            dni_w_miesiacu = 31 if miesiac % 2 == 0 else 30
        datadzien = dni_w_miesiacu - dzien_ + dzien
        return datadzien, miesiac
    else:
        datadzien = dzien - dzien_
        return datadzien, miesiac"""

def TrueorFalse(tekst=""):
    while True:
        pick = input(tekst)
        if pick == "y":
            return True
        elif pick == "n":
            return False
        else:
            print("wpisz y/n")

def wagi(pesel):
    tablica_wag = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = 0
    for i in range(10):
        suma += int(pesel[i]) * tablica_wag[i]
    
    ostatnia_cyfra = suma % 10
    cyfra_kontrolna = (10 - ostatnia_cyfra) % 10
    pesel += str(cyfra_kontrolna)
    return pesel

def liczpesel(datadzien,datamiesiac,datarok,plec):
    pesel = ""
    pesel += str(datarok)[-2:]
    m_offset = datamiesiac + (20 if datarok >= 2000 else 0)
    pesel += f"{m_offset:02d}"
    
    pesel += f"{datadzien:02d}"
    
    for i in range(3):
        pesel+= str(random.randint(0,9))
    if plec == "m":
        pesel+= str(random.randint(1,5)*2-1)
    elif plec == "k":
        pesel+= str(random.randint(0,4)*2)
    else:
        pesel+= str(random.randint(0,9))
    pesel = wagi(pesel)
    return pesel
    
def auto(wzraca = False):
    # =========================================================================
        # SEKCJA 1: PODSTAWOWE DANE IDENTYFIKACYJNE I DATA URODZENIA
        # =========================================================================
        # {pesel}       -> Zwraca: 11-cyfrowy tekst (string) będący wygenerowanym numerem PESEL.
        #                  Zawiera zakodowaną datę urodzenia, serię losową, cyfrę płci oraz cyfrę kontrolną.
        # {datarok}     -> Zwraca: Liczbę całkowitą (int), np. 1995. Rok, w którym ta osoba się urodziła.
        # {datamiesiac} -> Zwraca: Liczbę całkowitą (int) z zakresu 1-12. Miesiąc urodzenia tej osoby.
        # {datadzien}   -> Zwraca: Liczbę całkowitą (int) z zakresu 1-31. Dzień miesiąca, w którym osoba się urodziła.
        #print(f"dane osobowe:\npesel: {pesel}\nrok urodzenia: {datarok}\nmiesiac urodzenia: {datamiesiac}\ndzien urodzenia: {datadzien}")

        # =========================================================================
        # SEKCJA 2: TOŻSAMOŚĆ, STATUS I WYLOSOWANE PARAMETRY WEJŚCIOWE (WIEK OSOBY)
        # =========================================================================
        # {plec}        -> Zwraca: Tekst (string) "kobieta" lub "meszczyzna". Określa płeć biologiczna osoby.
        # {imie}        -> Zwraca: Tekst (string) zawierający wylosowane z bazy JSON imię pasujące do płci.
        # {nazwisko}    -> Zwraca: Tekst (string) zawierający wylosowane z bazy JSON nazwisko.
        # {emeryt}      -> Zwraca: Wartość logiczną (bool) True lub False. Wynik warunku, czy wiek przekracza próg emerytalny.
        # {wiekdane}    -> Zwraca: Liczbę całkowitą (int). Wylosowany na samym początku, wyjściowy wiek (np. od 18 do 70).
        # {miesiacdane} -> Zwraca: Liczbę całkowitą (int). Wylosowany na samym początku, wyjściowy miesiąc (od 1 do 12).
        # {dziendane}   -> Zwraca: Liczbę całkowitą (int). Wylosowany na samym początku, wyjściowy dzień (od 1 do 28/31).
        #
        # UWAGA LOGICZNA: {wiekdane}, {miesiacdane} i {dziendane} to były parametry "startowe" do obliczeń.
        # Natomiast faktyczna data urodzenia ({datadzien}.{datamiesiac}.{datarok}) powstała dopiero PO przesunięciach kalendarzowych.
        #print(f"plec: {plec}\nimie: {imie}\nnazwisko: {nazwisko}\nczy emeryt: {emeryt}\ndane o dzisiejszym wieku osoby:\nwiek: {wiekdane}\nmiesiac: {miesiacdane}\ndzien: {dziendane}")

        # =========================================================================
        # SEKCJA 3: ZEGAR SYSTEMOWY (STAN CALENDARZA W MOMENCIE URUCHOMIENIA)
        # =========================================================================
        # {year_}       -> Zwraca: Liczbę całkowitą (int). Obecny rok pobrany z systemu operacyjnego (np. 2026).
        # {miesiac_}    -> Zwraca: Liczbę całkowitą (int). Obecny miesiąc pobrany z systemu operacyjnego (np. 5).
        # {dzien_}      -> Zwraca: Liczbę całkowitą (int). Obecny dzień miesiąca pobrany z systemu operacyjnego (np. 30).
        #print(f"dzisiejsza data:\nrok: {year_}\nmiesiac: {miesiac_}\ndzien: {dzien_}")
    with open("imiona.json", encoding="UTF-8") as r:
        dane = json.load(r)
    plec = random.choices(["k","m"])
    plec = plec[0]
    if plec == "m":
        imie = random.choices(dane["imiona"]["meskie"])
    else:
        imie = random.choices(dane["imiona"]["zenskie"])
    nazwisko= random.choices(dane["nazwiska"])
    nazwisko = nazwisko[0]
    imie = imie[0]
    wiek = random.randint(18,70)
    wiekdane = wiek
    miesiac = random.randint(1,12)
    miesiacdane = miesiac
    dzien = random.randint(1,28)
    dziendane = dzien
    if wiek>60:
        emeryt = True
    else:
        emeryt=False
    datadzien = dzien
    datamiesiac = miesiac
    if (miesiac_ < miesiac) or (miesiac_ == miesiac and dzien_ < dzien):
        datarok = year_ - wiek - 1
    else:
        datarok = year_ - wiek
    #print(f"plec: {plec}\nimie: {imie}\nnazwisko: {nazwisko}")
    #print(f"data urodzenia: {datadzien}.{datamiesiac}.{datarok}")
    pesel = liczpesel(datadzien,datamiesiac,datarok,plec)
    if plec == "m":
        plec = "meszczyzna"
    else:
        plec = "kobieta"
    if not wzraca:
        print(f"dane osobowe:\npesel: {pesel}\nrok urodzenia: {datarok}\nmiesiac urodzenia: {datamiesiac}\ndzien urodzenia: {datadzien}")
        print(f"plec: {plec}\nimie: {imie}\nnazwisko: {nazwisko}\nczy emeryt: {emeryt}\ndane o dzisiejszym wieku osoby:\nwiek: {wiekdane}\nmiesiac: {miesiacdane}\ndzien: {dziendane}")
        print(f"dzisiejsza data:\nrok: {year_}\nmiesiac: {miesiac_}\ndzien: {dzien_}")
    else:
        return (
            pesel,           # 1. string: 11-cyfrowy numer PESEL
            datarok,         # 2. int: Faktyczny rok urodzenia (np. 1995)
            datamiesiac,     # 3. int: Faktyczny miesiąc urodzenia (1-12)
            datadzien,       # 4. int: Faktyczny dzień urodzenia (1-31)
            plec,            # 5. string: "kobieta" lub "meszczyzna"
            imie,            # 6. string: Wylosowane/wpisane imię
            nazwisko,        # 7. string: Wylosowane/wpisane nazwisko
            emeryt,          # 8. bool: Status emerytalny (True/False)
            wiekdane,        # 9. int: Wylosowany/wpisany startowy wiek osoby
            miesiacdane,     # 10. int: Wylosowany/wpisany startowy miesiąc
            dziendane,       # 11. int: Wylosowany/wpisany startowy dzień
            year_,           # 12. int: Dzisiejszy rok pobrany z systemu
            miesiac_,        # 13. int: Dzisiejszy miesiąc pobrany z systemu
            dzien_           # 14. int: Dzisiejszy dzień pobrany z systemu
        )
def recznie():
    imie = input("wpisz imie>")
    nazwisko = input("wpisz nazwisko>")
    if imie.endswith("a"):
        pick = TrueorFalse("czy plec to kobieta?>")
        if pick:
            plec = "k"
        else:
            plec = "m"
    else:
        pick = TrueorFalse("czy plec to meszczyzna?>")
        if pick:
            plec = "m"
        else:
            plec = "k"
    wiek = int(input("wiek (liczba)>"))
    wiekdane = wiek
    if wiek>60:
        emeryt = True
    else:
        emeryt=False
    pick = TrueorFalse("chcesz wybrac miesiac i rok?>")
    if pick:
        while True:
            miesiac = int(input("wybierz miesiac (liczba)"))
            if miesiac>12 or miesiac<1:
                print("wybierz od 1 do 12")
            else:
                break
        while True:
            dzien = int(input("wybierz dzien (liczba)"))
            if dzien>31 or dzien<1:
                print("wybierz od 1 do 31")
            else:
                break
    else:
        miesiac = random.randint(1,12)
        dzien = random.randint(1,28)#28 zeby nie bylo np 30 lutego
    dziendane = dzien
    miesiacdane = miesiac
    datadzien = dzien
    datamiesiac = miesiac
    if (miesiac_ < miesiac) or (miesiac_ == miesiac and dzien_ < dzien):
        datarok = year_ - wiek - 1
    else:
        datarok = year_ - wiek
    print(f"data urodzenia {datadzien}.{datamiesiac}.{datarok}")
    pesel=liczpesel(datadzien,datamiesiac,datarok,plec)
    print(f"dane osobowe:\npesel: {pesel}\nrok urodzenia: {datarok}\nmiesiac urodzenia: {datamiesiac}\ndzien urodzenia: {datadzien}")
    print(f"plec: {plec}\nimie: {imie}\nnazwisko: {nazwisko}\nczy emeryt: {emeryt}\ndane o dzisiejszym wieku osoby:\nwiek: {wiekdane}\nmiesiac: {miesiacdane}\ndzien: {dziendane}")
    print(f"dzisiejsza data:\nrok: {year_}\nmiesiac: {miesiac_}\ndzien: {dzien_}")
    
        
if __name__ == "__main__":
    pick = liczby(4,"1.wybierz recznie dane\n2.wylosuj automatycznie\n3.ai ma dobrac (niestabilne)\n4.wyjdz\n>")
    if pick == 1:
        recznie()
    elif pick ==2:
        auto()