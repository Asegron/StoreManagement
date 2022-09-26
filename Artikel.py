# Klasse Artikel zum Zweck der einfachen Bestandsfuehrung

import string

class Artikel:

    MIN_BESTAND		    = 0
    MIN_ARTIKELNR		= 1000
    MAX_ARTIKELNR		= 9999
    MIN_ZUGANG			= 1
    MIN_ABGANG			= 1
    MIN_PREIS		    = 0.01
    MIN_PROZENT		    = 0.0
    ARTIKELNUMMER       = "Artikelnummer ist ungueltig, da die Eingabe nicht 4-stellig und positiv ist!"
    ARTIKELBEZEICHNUNG  = "Artikelbezeichnung ist ungueltig, da die Eingabe leer ist!"
    ARTIKELBESTAND      = "Artikelbestand ist ungueltig, da die Eingabe < 0 ist!"
    ZUGANG_NEGATIV      = "Die eingegebene Menge ist ungueltig, da sie <= 0 ist!"
    ABGANG_NEGATIV      = "Die eingegebene Menge ist ungueltig, da sie <= 0 ist!"
    ABGANG_ZU_HOCH      = "Der Abgang ist groesser als die Groesse des Bestandes!"
    PREIS_ZU_NIEDRIG    = "Der angegebene Preis muss mind. " + MIN_PREIS + "sein!"
    PROZENT_ZU_NIEDRIG  = "Die uebergebene Prozentzahl muss mind. " + MIN_PROZENT + "sein!"

    germanEnglishDic = {
    "Artikel" : "article",
    "artikelNr" : "articleNr",
    "bezeichnung" : "description",
    "preis" : "price",
    }

    def __init__(self, artikelNr, bezeichnung, bestand, preis):
        self.__artikelNr = int(artikelNr)
        self.__bezeichnung = string(bezeichnung.replace(" ", ""))
        self.__bestand = int(bestand)
        self.__preis = float(preis)

        if artikelNr < Artikel.MIN_ARTIKELNR or artikelNr > Artikel.MAX_ARTIKELNR:
            raise Exception(Artikel.ARTIKELNUMMER)
        if bezeichnung == None or bezeichnung.replace(" ", "").len(bezeichnung) == 0:
            raise Exception(Artikel.ARTIKELBEZEICHNUNG)
        if bestand < Artikel.MIN_BESTAND:
            raise Exception(Artikel.ARTIKELBESTAND)
        if preis < Artikel.MIN_PREIS:
            raise Exception(Artikel.PREIS_ZU_NIEDRIG)
          
    def __init__(self, artikelNr, bezeichnung):
        self.__artikelNr = int(artikelNr)
        self.__bezeichnung = string(bezeichnung.replace(" ", ""))

    def get_artikelNr(self):
        return self.__artikelNr
    
    def get_bezeichnung(self):
        return self.__bezeichnung

    def get_bestand(self):
        return self.__bestand
    
    def get_preis(self):
        return self.__preis

    def set_bezeichnung(self, bezeichnung):
