class Penduduk():
    def __init__(self,nama,jk,peran,alamat,ttl,status):
        self.nama = nama
        self.jeniskelamin = jk
        self.peran = peran
        self.alamat = alamat
        self.tetalahir = ttl
        self.status = status
    
    def get_nama(self):
        return self.nama
    
    def get_jk(self):
        return self.jeniskelamin

    def get_peran(self):
        return self.peran

    def get_alamat(self):
        return self.alamat

    def get_ttl(self):
        return self.tetalahir

    def get_status(self):
        return self.status

    def get_summary(self):
        return "Penduduk bernama " + self.nama + ", merupakan " + self.jeniskelamin + ", sebagai " + self.peran + ", beralamat di " + self.alamat + ", lahir di " + self.tetalahir + ", dengan status " + self.status     