from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
import MySQLdb as mdb
from FrmPendaftaran import *
from FrmPasien import *
from FrmPasien_prog import *
from FrmDokter import *
from FrmDokter_prog import *
from FrmUser import *
from FrmUser_prog import *
from FrmLogin import *
from FrmLogin_prog import *

def signals(self):
    self.PB_Cari.clicked.connect(self.Cari)
    self.PB_Submit.clicked.connect(self.Submit)
    self.PB_Pasien.clicked.connect(self.Pasien)
    self.PB_Dokter.clicked.connect(self.Dokter)
    self.PB_User.clicked.connect(self.User)
    self.PB_Login.clicked.connect(self.Login)
    self.PB_Logout.clicked.connect(self.Logout)
    self.Cmb_Bidang.currentTextChanged.connect(self.DisplayDokter)
    self.Cmb_NamaDr.currentTextChanged.connect(self.DisplayDetailDokter)

def pesan(self, ikon, judul, isipesan):
        msgBox = QMessageBox()
        msgBox.setIcon(ikon)
        msgBox.setText(isipesan)
        msgBox.setWindowTitle(judul)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

def Cari(self):
    try:
        con = mdb.connect('localhost','root','','ltp_final_project1_db')

        id_pasien = self.Txt_KTP.text()

        cur = con.cursor()
        cur.execute("SELECT * FROM pasien WHERE KTP= %s", [id_pasien])

        result = cur.fetchall()
    
        if result == ():
            self.Txt_Nama.setText("")
            self.Txt_Alamat.setText("")
            today = QtCore.QDate.currentDate()
            self.Cal_TanggalLahir.setSelectedDate(today)
            self.Txt_Phone.setText("")
            self.Opt_Kawin_2.setChecked(True)
        else:
            self.Txt_Nama.setText(result[0][1])
            self.Txt_Alamat.setText(result[0][2])
            tanggalan=QDate(result[0][4]).toPyDate()
            self.Cal_TanggalLahir.setSelectedDate(tanggalan)
            self.Txt_Phone.setText(result[0][6])
            if (result[0][7] == "Kawin"):
                self.Opt_Kawin.setChecked(True)
            else:
                self.Opt_Kawin_2.setChecked(True)
        
    except mdb.Error as e:
        self.Txt_Nama.setText("")
        self.Txt_Alamat.setText("")
        today = QtCore.QDate.currentDate()
        self.Cal_TanggalLahir.setSelectedDate(today)
        self.Txt_Phone.setText("")
        self.Opt_Kawin_2.setChecked(True)

def DisplayDokter(self):
    Bidang = self.Cmb_Bidang.currentText()

    try:
        con = mdb.connect('localhost','root','','ltp_final_project1_db')
        
        cur = con.cursor()
        cur.execute("SELECT * FROM dokter WHERE BidangKedokteran like %s", [Bidang])

        result = cur.fetchall()
        print(result)

        if result == ():
            self.Cmb_NamaDr.clear()
            self.Txt_PhoneDokter.setText("")
        else:
            self.Cmb_NamaDr.clear()
            for row_number, row_data in enumerate(result):
                self.Cmb_NamaDr.addItem(str(row_data[1]))
            self.DisplayDetailDokter()
    
    except mdb.Error as e:
        self.Cmb_NamaDr.clear()
        self.Txt_PhoneDokter.setText("")

def DisplayDetailDokter(self):
    NamaDokter = self.Cmb_NamaDr.currentText()

    try:
        con = mdb.connect('localhost','root','','ltp_final_project1_db')
        
        cur = con.cursor()
        cur.execute("SELECT * FROM dokter WHERE Nama like %s", [NamaDokter])

        result = cur.fetchall()
        print(result)

        if result == ():
            self.Txt_PhoneDokter.setText("")
            self.Chk_Senin.setChecked(False)
            self.Chk_Selasa.setChecked(False)
            self.Chk_Rabu.setChecked(False)
            self.Chk_Kamis.setChecked(False)
            self.Chk_Jumat.setChecked(False)
            self.Chk_Sabtu.setChecked(False)
            self.Chk_Minggu.setChecked(False)
            self.Time1_Buka.setTime(QTime(0,0))
            self.Time1_Tutup.setTime(QTime(0,0))
            self.Time2_Buka.setTime(QTime(0,0))
            self.Time2_Tutup.setTime(QTime(0,0))
            self.Time3_Buka.setTime(QTime(0,0))
            self.Time3_Tutup.setTime(QTime(0,0))            
            self.Time4_Buka.setTime(QTime(0,0))
            self.Time4_Tutup.setTime(QTime(0,0))
            self.Time5_Buka.setTime(QTime(0,0))
            self.Time5_Tutup.setTime(QTime(0,0))
            self.Time6_Buka.setTime(QTime(0,0))
            self.Time6_Tutup.setTime(QTime(0,0))
            self.Time7_Buka.setTime(QTime(0,0))
            self.Time7_Tutup.setTime(QTime(0,0))
        else:
            self.Txt_PhoneDokter.setText(result[0][2])
            self.Chk_Senin.setChecked(result[0][4])
            self.Time1_Buka.setTime(QTime(int(JamBuka(result[0][5])), int(MinBuka(result[0][5]))))
            self.Time1_Tutup.setTime(QTime(int(JamTutup(result[0][6])), int(MinTutup(result[0][6]))))
            self.Chk_Selasa.setChecked(result[0][7])
            self.Time2_Buka.setTime(QTime(int(JamBuka(result[0][8])), int(MinBuka(result[0][8]))))
            self.Time2_Tutup.setTime(QTime(int(JamTutup(result[0][9])), int(MinTutup(result[0][9]))))
            self.Chk_Rabu.setChecked(result[0][10])
            self.Time3_Buka.setTime(QTime(int(JamBuka(result[0][11])), int(MinBuka(result[0][11]))))
            self.Time3_Tutup.setTime(QTime(int(JamTutup(result[0][12])), int(MinTutup(result[0][12]))))
            self.Chk_Kamis.setChecked(result[0][13])
            self.Time4_Buka.setTime(QTime(int(JamBuka(result[0][14])), int(MinBuka(result[0][14]))))
            self.Time4_Tutup.setTime(QTime(int(JamTutup(result[0][15])), int(MinTutup(result[0][15]))))
            self.Chk_Jumat.setChecked(result[0][16])
            self.Time5_Buka.setTime(QTime(int(JamBuka(result[0][17])), int(MinBuka(result[0][17]))))
            self.Time5_Tutup.setTime(QTime(int(JamTutup(result[0][18])), int(MinTutup(result[0][18]))))
            self.Chk_Sabtu.setChecked(result[0][19])
            self.Time6_Buka.setTime(QTime(int(JamBuka(result[0][20])), int(MinBuka(result[0][20]))))
            self.Time6_Tutup.setTime(QTime(int(JamTutup(result[0][21])), int(MinTutup(result[0][21]))))
            self.Chk_Minggu.setChecked(result[0][22])
            self.Time7_Buka.setTime(QTime(int(JamBuka(result[0][23])), int(MinBuka(result[0][23]))))
            self.Time7_Tutup.setTime(QTime(int(JamTutup(result[0][24])), int(MinTutup(result[0][24]))))

    
    except mdb.Error as e:
        self.Chk_Senin.setChecked(False)
        self.Chk_Selasa.setChecked(False)
        self.Chk_Rabu.setChecked(False)
        self.Chk_Kamis.setChecked(False)
        self.Chk_Jumat.setChecked(False)
        self.Chk_Sabtu.setChecked(False)
        self.Chk_Minggu.setChecked(False)
        self.Time1_Buka.setTime(QTime(0,0))
        self.Time1_Tutup.setTime(QTime(0,0))
        self.Time2_Buka.setTime(QTime(0,0))
        self.Time2_Tutup.setTime(QTime(0,0))
        self.Time3_Buka.setTime(QTime(0,0))
        self.Time3_Tutup.setTime(QTime(0,0))            
        self.Time4_Buka.setTime(QTime(0,0))
        self.Time4_Tutup.setTime(QTime(0,0))
        self.Time5_Buka.setTime(QTime(0,0))
        self.Time5_Tutup.setTime(QTime(0,0))
        self.Time6_Buka.setTime(QTime(0,0))
        self.Time6_Tutup.setTime(QTime(0,0))
        self.Time7_Buka.setTime(QTime(0,0))
        self.Time7_Tutup.setTime(QTime(0,0))

def Submit(self):
    pass

def Pasien(self):
    if (self.Lbl_UserRole.text()=='Admin'):
        self.FrmPasien = QtWidgets.QMainWindow()
        self.ui_pasien = Ui_FrmPasien()
        self.ui_pasien.setupUi(self.FrmPasien)
        self.ui_pasien.signals()
        self.FrmPasien.show()
    else:
        pesan(self,QMessageBox.Information,"Warning","you dont have authorisation, Please contact Admin")

def Dokter(self):
    if (self.Lbl_UserRole.text()=='Admin'):
        self.FrmDokter = QtWidgets.QMainWindow()
        self.ui_dokter = Ui_FrmDokter()
        self.ui_dokter.setupUi(self.FrmDokter)
        self.ui_dokter.signals()
        self.FrmDokter.show()
    else:
        pesan(self,QMessageBox.Information,"Warning","you dont have authorisation, Please contact Admin")

def User(self):
    if (self.Lbl_UserRole.text()=='Admin'):
        self.FrmUser = QtWidgets.QMainWindow()
        self.ui_user = Ui_FrmUser()
        self.ui_user.setupUi(self.FrmUser)
        self.ui_user.signals()
        self.FrmUser.show()
    else:
        pesan(self,QMessageBox.Information,"Warning","you dont have authorisation, Please contact Admin")

def Login(self):
    self.FrmLogin = QtWidgets.QMainWindow()
    self.ui_login = Ui_FrmLogin()
    self.ui_login.setupUi(self.FrmLogin)
    self.ui_login.signals()
    self.FrmLogin.show()

def Logout(self):
    self.Lbl_CurrentUser.setText("Guest")
    self.Lbl_UserRole.setText("")

Ui_FrmPendaftaran.signals=signals
Ui_FrmPendaftaran.Cari=Cari
Ui_FrmPendaftaran.DisplayDokter=DisplayDokter
Ui_FrmPendaftaran.DisplayDetailDokter=DisplayDetailDokter
Ui_FrmPendaftaran.Submit=Submit
Ui_FrmPendaftaran.Pasien=Pasien
Ui_FrmPendaftaran.Dokter=Dokter
Ui_FrmPendaftaran.User=User
Ui_FrmPendaftaran.Login=Login
Ui_FrmPendaftaran.Logout=Logout

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmPendaftaran = QtWidgets.QMainWindow()
    ui = Ui_FrmPendaftaran()
    ui.setupUi(FrmPendaftaran)
    ui.signals()
    FrmPendaftaran.show()
    sys.exit(app.exec_())