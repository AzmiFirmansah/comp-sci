class mahasiswa:
    def __init__(self, name, nim, prodi):
        self.name = name
        self.nim = nim
        self.prodi = prodi

    def perkenalan (self):
            print('Halo nama saya ' + self.name)

mahasiswa1 = mahasiswa( "Restu", 123, "Comp Sci") 
mahasiswa2 = mahasiswa("Azmi", 321, "Comp Sci") 


mahasiswa1.perkenalan()