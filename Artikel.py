# Klasse Artikel zum Zweck der einfachen Bestandsfuehrung

from socketserver import BaseRequestHandler
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

    def set_bezeichnung(self, bezeichnung,):
        self.__bezeichnung = bezeichnung
        if bezeichnung is None or bezeichnung.replace(" ", "").len(bezeichnung) == 0:
            raise Exception(Artikel.ARTIKELBEZEICHNUNG)

    def set_bestand(self, bestand):
        self.__bezeichnung = bestand

    def set_preis(self, preis):
        self.__preis = preis
    
    def bucheZugang(self, zugang):
        if zugang < Artikel.MIN_ZUGANG:
            raise Exception(Artikel.ZUGANG_NEGATIV)
        self.__bestand += zugang

    def bucheAbgang(self, abgang):
        if abgang < Artikel.MIN_ABGANG:
            raise Exception(Artikel.ABGANG_NEGATIV)
        if self.__bestand - abgang < Artikel.MIN_BESTAND:
            raise Exception(Artikel.ABGANG_ZU_HOCH)
        self.__bestand -= abgang
    
    def setProzent(self, prozent):
        if prozent < Artikel.MIN_PROZENT:
            raise Exception(Artikel.PROZENT_ZU_NIEDRIG)
        self.__preis -= self.__preis * (100.0 - prozent) / 100.0

    def __eq__(self, other):
        return self.__artikelNr == other.__artikelNr 
    
    def __str__(self):
        return( "Artikel: " + Artikel.get_artikelNr + 
                "Bezeichnung: " + Artikel.get_bezeichnung + 
                "Bestand: " + Artikel.get_bestand +
                "Preis: " + Artikel.get_bestand)