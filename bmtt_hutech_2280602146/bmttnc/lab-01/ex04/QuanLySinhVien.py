from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhvien = []
    def generateID(self):
        maxId = 1
        if(self.soLuongSinhVien()>0):
            maxId = self.listSinhvien[0]._id
            for sv in self.listSinhvien:
                if(maxId < sv._id):
                    maxId = sv._id
            maxId = maxId +1
        return maxId
    def soLuongSinhVien(self):
        return self.listSinhvien.__len__()
    
    def nhapSinhVien(self):
        svId = self.generateID()
        name =input("Nhap ten sinh vien")
        sex = input("Nhap gioi tinh tinh duc")
        major = input("Nhap chuyen nganh cua sinh vien ")
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svId,name,sex, major,diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhvien.append(sv)
        
    def updateSinhVien(self, ID):
        sv:SinhVien = self.findByID(ID)
        if(sv != None):
            name =input("Nhap ten sinh vien")
            sex = input("Nhap gioi tinh tinh duc")
            major = input("Nhap chuyen nganh cua sinh vien ")
            diemTB = float(input("Nhap diem cua sinh vien: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co Id = {} khong ton tai." .format(ID))
    
    def sortByID(self):
        self.listSinhvien.sort(key=lambda x: x._id, reverse=False)
    
    def sortByName(self):
         self.listSinhvien.sort(key=lambda x: x._name, reverse=False)
    
    def sortByDiemTB(self):
         self.listSinhvien.sort(key=lambda x: x._diemTB, reverse=False)
         
    def findByID(self,ID):
        searchResult = None
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSinhvien:
                if (sv._id ==ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword):
        listSV = []
        if(self.soLuongSinhVien()>0):
            for sv in self.listSinhvien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    
    def deleteById(self,ID ):
        isDeleted = False
        sv = self.findByID(ID)
        if(sv != None):
            self.listSinhvien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc(self, sv:SinhVien):
        if(sv._diemTB >=8):
            sv._hocLuc = " Gioi"
        elif (sv._diemTB >=6.5):
            sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "trung binh"
        else:
            sv._hocLuc ="Yeu"
            
    def showSinhVien(self, listSV):
        print("{:<18} {:<8} {:<8}{:<8} {:<8} "
              .format("ID" , "Name", "Sex", "Major", "DiemTb", "HocLuc"))
        if len(listSV) > 0:
            for sv in listSV:      
                print("{:<18} {:<8} {:<8}{:<8} {:<8} "
                    .format(sv._id, sv._name, sv._sex,sv._major, sv._diemTB, sv._hocLuc))
        print("\n")
        
    def getListSinhVien(self):
        return self.listSinhvien