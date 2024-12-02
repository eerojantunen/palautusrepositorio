KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    

    def tarkasta_koko(self, koko, oletus, error_viesti):
        if koko is None:
            return oletus
        if not isinstance(koko, int) or koko < 0:
            raise Exception(error_viesti)
        return koko




    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self.tarkasta_koko(kapasiteetti, KAPASITEETTI, "Väärä kapasiteetti")
        self.kasvatuskoko = self.tarkasta_koko(kasvatuskoko, OLETUSKASVATUS, "kapasiteetti2")

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, numero):
        return numero in self.ljono
 
    

    def lisaa(self, numero):
        if not self.kuuluu(numero):
            self.ljono[self.alkioiden_lkm] = numero
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.ljono) == 0:
                self.kasvata_listaa()
            return True
        return False

    def kasvata_listaa(self):
        taulukko_old = self.ljono
        self.kopioi_lista(self.ljono, taulukko_old)
        self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(taulukko_old, self.ljono)

    def poista_haluttu_numero(self,numero):
        for indexi in range(0, self.alkioiden_lkm):
            if numero == self.ljono[indexi]:
                self.ljono[kohta] = 0
                return True
        return False

    def poista(self, numero):
        if not self.kuuluu(numero):
            return False
        kohta = self.ljono.index(numero)
        self.ljono[kohta] = 0

        self.siirra_loput(kohta)

        self.alkioiden_lkm = self.alkioiden_lkm - 1
        return True

    def siirra_loput(self, alku):
        for indeksi in range(alku,self.alkioiden_lkm-1):
            self.ljono[indeksi] = self.ljono[indeksi+1]
        self.ljono[self.alkioiden_lkm-1] = 0

    def kopioi_lista(self, vanha_lista, uusi_lista):
        for i in range(0, len(vanha_lista)):
            uusi_lista[i] = vanha_lista[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a_taulu, b_taulu):
        yhdiste_lista = IntJoukko()
        a_taulu = a_taulu.to_int_list()
        b_taulu = b_taulu.to_int_list()

        for numero in a_taulu + b_taulu:
            yhdiste_lista.lisaa(numero)

        return yhdiste_lista

    @staticmethod
    def leikkaus(a_taulu, b_taulu):
        leikkaus_lista = IntJoukko()
        a_taulu = a_taulu.to_int_list()
        b_taulu = b_taulu.to_int_list()
        for numero in a_taulu:
            if numero in b_taulu:
                leikkaus_lista.lisaa(numero)
        return leikkaus_lista

    @staticmethod
    def erotus(a, b):
        erotus_lista = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for numero in a_taulu:
            erotus_lista.lisaa(numero)

        for numero in b_taulu:
            erotus_lista.poista(numero)
            
        return erotus_lista

    def __str__(self):
        return "{" + ", ".join(map(str, self.to_int_list())) + "}"