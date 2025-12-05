class Gempa:
    #variabel
    lokasi = ''
    skala = 0
    #constructor
    def __init__(self, daerah, skala):
        self.lokasi = daerah
        self.skala = skala
    #method
    def dampak(self):
        akibat = ''

        if self.skala < 2:
            akibat = 'Tidak Terasa'
        elif self.skala >= 2 and self.skala < 4:
            akibat = 'Bangunan Retak-Retak'
        elif self.skala >= 4 and self.skala < 6:
            akibat = 'Bangunan Roboh'
        else:
            akibat = 'Bangunan Roboh & Tsunami'
        print(
            '\nLokasi Gempa\t:', self.lokasi,
            '\nSkala Gempa\t:', self.skala,
            '\nDampak Gempa\t:', akibat,
            '\n=================================================')
        