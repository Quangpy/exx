from vd1 import Student
sv=[]
while True:
    print('''vui long chon chuc nang
    0.thoat
    1.xem danh sach sinh vien
    2.them sinh vien
    3. xoa sinh vien
    4. sua sinh vien ''')
    chon=input('ban chon di:')
    if chon.isdigit():
        chon=int(chon)
        if chon==0:
            break
        elif chon ==1:
            if len(sv)==0:
                print('hien chua co sinh vien nao')
            else:
                for i in sv:
                    i.show()
        elif chon == 2:
            id=input('nhap ID sinh vien:')
            name=input('nhap name sinh vien:')
            sv.append(Student(id,name))
        elif chon==3:
            id = input('nhap ID sinh vien can xoa: ')
            for i in sv:
                if i.id==id:
                    sv.remove(i)
        elif chon==4:
            id = input('nhap ID sinh vien can sua: ')
            for i in sv:
                if i.id==id:
                    i.set_name(input('nhap ten muon sua:'))







    else:
        print('chon lai di:')

