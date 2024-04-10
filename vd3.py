class Nut:
    def __init__(self,gia_tri):
        self.gia_tri=gia_tri
        self.nut_ke_tiep=None

class dslk:
    def __init__(self):
        self.dau=None
        self.duoi=None
    def in_ds(self):
        stt=0
        hien_tai=self.dau
        kq='DS['
        while hien_tai!=None:
            stt+=1
            if stt==1:
                kq+=''+ str(hien_tai.gia_tri)
            else:
                kq+='=>'+str(hien_tai.gia_tri)
                hien_tai=hien_tai.nut_ke_tiep
        kq+=']'
        print(kq)
    def them(self,gia_tri):
        nut=Nut(gia_tri)
        if self.dau==None:
            self.dau=nut
            self.duoi=nut
        else:
            self.duoi.nut_ke_tiep=nut
            self.duoi=nut
    def chen(self,chi_muc,gia_tri):
        nut=Nut(gia_tri)
    def tim(self,gia_tri):
        pass
    def xoa(self,vi_tri):
        pass
    def cap_nhat(self,vi_tri,gia_tri):
        pass
    def xoa_het(self):
        pass
