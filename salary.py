import csv

class Pracownik:
    def __init__(self, imie, nazwisko, pensja_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja_brutto = pensja_brutto

    def __str__(self):
        return f"Pracownik: {self.imie} {self.nazwisko}"

    def oblicz_netto(self):
        skladki_emerytalne = self.pensja_brutto * 0.0976
        skladki_rentowe = self.pensja_brutto * 0.015
        skladki_chorobowe = self.pensja_brutto * 0.0245
        koszt_uzyskania_przychodu = 250
        zaliczka_na_podatek_dochodowy = 32.4
        podstawa_opodatkowania = self.pensja_brutto - skladki_emerytalne - skladki_rentowe - skladki_chorobowe - koszt_uzyskania_przychodu
        podatek = podstawa_opodatkowania * 0.18
        skladka_zdrowotna = (self.pensja_brutto - skladki_emerytalne - skladki_rentowe - skladki_chorobowe - podatek) * 0.09
        netto = self.pensja_brutto - skladki_emerytalne - skladki_rentowe - skladki_chorobowe - podatek - skladka_zdrowotna - zaliczka_na_podatek_dochodowy
        return round(netto, 2)

    def oblicz_koszty_pracodawcy(self):
        skladki_emerytalne = self.pensja_brutto * 0.0976
        skladki_rentowe = self.pensja_brutto * 0.065
        skladki_wypadkowe = self.pensja_brutto * 0.0167
        fundusz_pracy = self.pensja_brutto * 0.0245
        fgsp = self.pensja_brutto * 0.001
        koszty_pracodawcy = self.pensja_brutto + skladki_emerytalne + skladki_rentowe + skladki_wypadkowe + fundusz_pracy + fgsp
        return round(koszty_pracodawcy, 2)

    def wygeneruj_raport(self):
        skladki_emerytalne = self.pensja_brutto * 0.0976
        skladki_rentowe = self.pensja_brutto * 0.065
        skladki_wypadkowe = self.pensja_brutto * 0.0167
        fundusz_pracy = self.pensja_brutto * 0.0245
        fgsp = self.pensja_brutto * 0.001

        print("Koszty pracodawcy składają się z:")
        print(f"Skladki emerytalne: {round(skladki_emerytalne, 2)}")
        print(f"Skladki rentowe: {skladki_rentowe}")
        print(f"Skladki wypadkowe: {skladki_wypadkowe}")
        print(f"Fundusz pracy: {fundusz_pracy}")
        print(f"FGŚP: {fgsp}")

# Testy dla klasy Pracownik
pracownik = Pracownik("Ania", "Wal", 4000)
assert str(pracownik) == "Pracownik: Ania Wal"
assert round(pracownik.oblicz_netto(), 2) == 2584.13
assert pracownik.oblicz_koszty_pracodawcy() == 4819.2

# Pętla wczytująca dane z pliku pracownicy.csv
with open('pracownicy.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Pominięcie nagłówka pliku
    for row in reader:
        imie = row[0]
        nazwisko = row[1]
        pensja_brutto = float(row[2])

        pracownik = Pracownik(imie, nazwisko, pensja_brutto)
        print(pracownik)
        print("Netto:", pracownik.oblicz_netto())
        print("Koszty pracodawcy:", pracownik.oblicz_koszty_pracodawcy())
        pracownik.wygeneruj_raport()