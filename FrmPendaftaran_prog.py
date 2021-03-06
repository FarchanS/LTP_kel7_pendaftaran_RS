import urllib.parse
import urllib.request 
import MySQLdb as mdb
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, QUrl, QUrlQuery
from PyQt5 import QtNetwork
# from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest,QNetworkCookieJar
from PyQt5.QtNetwork import *
from FrmPendaftaran import *
from FrmPasien import *
from FrmPasien_prog import *
from FrmDokter import *
from FrmDokter_prog import *
from FrmUser import *
from FrmUser_prog import *
from FrmLogin import *
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import hashlib

a=1
b=0
iddokter="0"
idpasien=0
kapasitas=0

def signals(self):
    global a

    self.PB_Cari.clicked.connect(self.Cari)
    self.PB_Submit.clicked.connect(self.Submit)
    self.PB_Pasien.clicked.connect(self.Pasien)
    self.PB_Dokter.clicked.connect(self.Dokter)
    self.PB_User.clicked.connect(self.User)
    self.PB_Login.clicked.connect(self.Login)
    self.PB_Logout.clicked.connect(self.Logout)
    self.Cmb_Bidang.currentTextChanged.connect(self.DisplayDokter)
    self.Cmb_NamaDr.currentTextChanged.connect(self.DisplayDetailDokter)
    if a==1:
        a=0
        ui.Lbl_UserRole.setVisible(False)

def login_signals(self):
    self.PB_login.clicked.connect(self.login)
    self.Chk_show_pass.stateChanged.connect(self.show_hide_pass)

def login(self):
    try:
        username = self.Txt_username.text()
        password = hashlib.md5(self.Txt_password.text().encode('utf-8')).hexdigest()

        con = mdb.connect('localhost','root','','ltp_final_project1_db')

        cur = con.cursor()
        cur.execute("SELECT * from users where Nama = '"+username + "'and Password = '"+password+"'")
        result = cur.fetchone()
        # print(hashlib.md5(password.encode('utf-8')).hexdigest())
        
        if result == None:
            pesan(self, QMessageBox.Information,"Failed to Login","Incorrect Email & Password")

        else:
            # self.FrmPendaftaran = QtWidgets.QMainWindow()
            # self.ui_pendaftaran = Ui_FrmPendaftaran()
            # self.ui_pendaftaran.setupUi(self.FrmPendaftaran)
            # self.ui_pendaftaran.signals()
            # self.FrmPendaftaran.show()  
            # self.ui_pendaftaran.Lbl_CurrentUser.setText(username)
            # self.ui_pendaftaran.Lbl_UserRole.setText(result[3])
            # self.ui_pendaftaran.Lbl_UserRole.setVisible(False)
            # self.FrmPendaftaran.show()  
            ui.Lbl_CurrentUser.setText(username)
            ui.Lbl_UserRole.setText(result[3])
            ui.Lbl_UserRole.setVisible(False)
            self.Txt_username.setText("")
            self.Txt_password.setText("")
            FrmLogin.hide()

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Some Error")

def pesan(self, ikon, judul, isipesan):
        msgBox = QMessageBox()
        msgBox.setIcon(ikon)
        msgBox.setText(isipesan)
        msgBox.setWindowTitle(judul)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

def Cari(self):
    global idpasien
    try:
        con = mdb.connect('localhost','root','','ltp_final_project1_db')
        id_pasien = self.Txt_KTP.text()

        cur = con.cursor()
        cur.execute("SELECT * FROM pasien WHERE KTP= %s", [id_pasien])

        result = cur.fetchall()
    
        if result == ():
            idpasien=0
            self.Txt_Nama.setText("")
            self.Txt_Alamat.setText("")
            today = QtCore.QDate.currentDate()
            self.Cal_TanggalLahir.setSelectedDate(today)
            self.Txt_Phone.setText("")
            self.Opt_Kawin_2.setChecked(True)
        else:
            idpasien=result[0][0]
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
        idpasien=0
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
    global iddokter
    global kapasitas

    NamaDokter = self.Cmb_NamaDr.currentText()

    try:
        con = mdb.connect('localhost','root','','ltp_final_project1_db')
        
        cur = con.cursor()
        cur.execute("SELECT * FROM dokter WHERE Nama like %s", [NamaDokter])

        result = cur.fetchall()
        # print(result)

        if result == ():
            iddokter="0"
            kapasitas=0
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
            iddokter=result[0][0]
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
            kapasitas=int(result[0][25])
        # print(kapasitas)

    except mdb.Error as e:
        iddokter="0"
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
    global idpasien
    global iddokter
    global kapasitas

    if (self.Lbl_CurrentUser.text()!="Guest"):
        tanggal=self.Cal_TanggalDatang.selectedDate().toPyDate()
        jam=self.TimeDatang.time().toString("HH")
        jam1=self.TimeDatang.time().toString("HH:mm")
        bidang=self.Cmb_Bidang.currentText()
 
        tahun=self.Cal_TanggalDatang.selectedDate().toString("yyyy")
        bulan=self.Cal_TanggalDatang.selectedDate().toString("MM")
        tgl=self.Cal_TanggalDatang.selectedDate().toString("dd")
        
        date_string = tahun+", "+bulan+", "+tgl

        date = datetime.strptime(date_string, "%Y, %m, %d")
        hari=date.weekday()
        b=0
        
        if hari == 0:
            jam_min = self.Time1_Buka.time().toString("HH:mm")
            jam_max = self.Time1_Tutup.time().toString("HH:mm")
        elif hari == 1:
            jam_min = self.Time2_Buka.time().toString("HH:mm")
            jam_max = self.Time2_Tutup.time().toString("HH:mm")
        elif hari == 2:
            jam_min = self.Time3_Buka.time().toString("HH:mm")
            jam_max = self.Time3_Tutup.time().toString("HH:mm")
        elif hari == 3:
            jam_min = self.Time4_Buka.time().toString("HH:mm")
            jam_max = self.Time4_Tutup.time().toString("HH:mm")
        elif hari == 4:
            jam_min = self.Time5_Buka.time().toString("HH:mm")
            jam_max = self.Time5_Tutup.time().toString("HH:mm")
        elif hari == 5:
            jam_min = self.Time6_Buka.time().toString("HH:mm")
            jam_max = self.Time6_Tutup.time().toString("HH:mm")
        elif hari == 6:
            jam_min = self.Time7_Buka.time().toString("HH:mm")
            jam_max = self.Time7_Tutup.time().toString("HH:mm")
        
        if ((jam1<jam_min) or (jam1>=jam_max)):
                b=1
        
        try:
            if (b==0):

                con = mdb.connect('localhost','root','','ltp_final_project1_db')
                
                cur = con.cursor()
                cur.execute("SELECT COUNT(KTP) FROM kedatangan WHERE IdDokter = %s AND DatangTgl = %s AND HOUR(DatangJam) = %s",(iddokter, date, jam))
                result = cur.fetchall()

                if result[0][0] >= kapasitas:
                    pesan(self, QMessageBox.Information,"Info","Antrian melebihi kapasitas, mohon untuk memilih hari yang lain")
                else:
                    cur.execute("INSERT INTO kedatangan(No, KTP, IdDokter, BidangKedokteran, DatangTgl, DatangJam) VALUES(%s, %s, %s, %s, %s, %s)",('',idpasien,iddokter,bidang,tanggal,jam1))
                    con.commit()    
                    pesan(self, QMessageBox.Information,"Info","Kedatangan sudah di simpan")

                    isisms = 'Pasien yth, anda terdaftar akan mengunjungi dr. '+self.Cmb_NamaDr.currentText()+', pada tanggal ' + self.Cal_TanggalDatang.selectedDate().toString("dd/MM/yyyy") + ' jam ' + self.TimeDatang.time().toString("HH:mm")+ '. Mohon datang 1 jam sebelum jadwal. Terima kasih.'
                    # print(isisms)
                    apisms = urllib.request.urlopen('https://websms.co.id/api/smsgateway?token=93916b1da58f544ddf99a2d3511117d3&to='+self.Txt_Phone.text()+'&msg=' +urllib.parse.quote_plus(isisms))
                    apisms_response = apisms.read()

                    print(apisms) 

                con.close()
            else:
                pesan(self, QMessageBox.Information,"Info","Permintaan diluar waktu kerja dokter, mohon untuk memilih jam yang lain")

        except mdb.Error as e:
            pesan(self,QMessageBox.Information,"Error","Failed")
    else:
        pesan(self,QMessageBox.Information,"Warning","you dont have authorisation, Please contact Admin")

def Pasien(self):
    # print(self.Lbl_CurrentUser.text())
    if (self.Lbl_CurrentUser.text()!="Guest"):
        self.FrmPasien = QtWidgets.QMainWindow()
        self.ui_pasien = Ui_FrmPasien()
        self.ui_pasien.setupUi(self.FrmPasien)
        self.ui_pasien.signals()
        self.FrmPasien.show()
    else:
        pesan(self,QMessageBox.Information,"Warning","you dont have authorization, Please contact Admin")

def Dokter(self):
    if (self.Lbl_UserRole.text()=='Admin'):
        self.FrmDokter = QtWidgets.QMainWindow()
        self.ui_dokter = Ui_FrmDokter()
        self.ui_dokter.setupUi(self.FrmDokter)
        self.ui_dokter.signals()
        self.FrmDokter.show()
    else:
        pesan(self,QMessageBox.Information,"Warning","you dont have authorization, Please contact Admin")

def User(self):
    if (self.Lbl_UserRole.text()=='Admin'):
        self.FrmUser = QtWidgets.QMainWindow()
        self.ui_user = Ui_FrmUser()
        self.ui_user.setupUi(self.FrmUser)
        self.ui_user.signals()
        self.FrmUser.show()
    else:
        pesan(self,QMessageBox.Information,"Warning","you dont have authorization, Please contact Admin")

def Login(self):
    FrmLogin.show()

def show_hide_pass(self):
    if self.Chk_show_pass.checkState() == Qt.Checked:
        self.Txt_password.setEchoMode(QLineEdit.Normal)
    else:
        self.Txt_password.setEchoMode(QLineEdit.Password)

def Logout(self):
    self.Lbl_CurrentUser.setText("Guest")
    self.Lbl_UserRole.setText("")

def handleResponse(self, reply):

        er = reply.error()

        if er == QtNetwork.QNetworkReply.NoError:

            bytes_string = reply.readAll()
            print(str(bytes_string, 'utf-8'))
            pesan(self,QMessageBox.Information,"Info","Terkirim")

        else:
            print("Error occured: ", er)
            print(reply.errorString())
            pesan(self,QMessageBox.Information,"Warning","GAGAL !!")

def scheduling():
    from datetime import timedelta

    global iddokter

    bidang=["Dokter Umum", "Kandungan", "Anak", "Penyakit Dalam", "Bedah"]

    
    today = datetime.today()
    print(today)
    tomorrow = today + timedelta(days = 1)
    tomorrow = tomorrow.strftime("%Y-%m-%d")
    print(tomorrow)

    con = mdb.connect('localhost','root','','ltp_final_project1_db')

    for i in range(0, 5):
        cur = con.cursor()
        cur.execute("SELECT COUNT(KTP) FROM kedatangan WHERE BidangKedokteran = %s and DatangTgl = %s", ([bidang[i]], [tomorrow]))

        result = cur.fetchall()
        jumlahpasien=result[0][0]

        if i == 0:
            pilihandokter = "5053782348:AAFv4Dn-DwiW2kv8gEHcplmv_NWpJeC8Gdk" #dokter umum
            #chatid = "1398822979" #chat id rita
        elif i == 1:
            pilihandokter = "5055872361:AAF7SvlXPItk5S3cS1oYmpFW-zG1xrctS5Q" #spesialis kandungan
            #chatid = "1398822979" 
        elif i == 2:
            pilihandokter = "5012230148:AAFmIRXr2_04IiqUANCkLeduYPsJP_IKqqg" #spesialis anak
        elif i == 3:
            pilihandokter = "5049996996:AAGfd5cGbqjgUvt_jMWrkBldTqIbWAKPkoE" # spesialis penyakit dalam
        elif i == 4:
            pilihandokter = "5033401776:AAG0M26Bwk-XdukgLwP-kCuEx-UtW4Hzs0A" #spesialis bedah
        else:
            pilihandokter = "2070076356:AAHjDS_mB9IE-1sBwoxTDzA8y05TMb3XIi8" #form RS bot

        urlawal = 'https://api.telegram.org/bot' +pilihandokter+ '/sendMessage?chat_id=-784802410&parse_mode=html&text='
        if jumlahpasien == 0:
            pesan1='Besok tidak ada pasien'
        else:
            pesan1='Besok ada ' + str(jumlahpasien) + ' orang pasien yang akan datang dok..'

        url = urlawal+pesan1

        urlfilter = url.replace(" ","%20")


        telegramchat = urllib.request.urlopen(str(urlfilter))
        telegram_response = telegramchat.read()

        print(url)
        print('send')

    con.close()

Ui_FrmLogin.signals=login_signals
Ui_FrmLogin.login = login
Ui_FrmLogin.show_hide_pass=show_hide_pass

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
Ui_FrmPendaftaran.scheduling=scheduling
Ui_FrmPendaftaran.handleResponse=handleResponse


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    FrmPendaftaran = QtWidgets.QMainWindow()
    ui = Ui_FrmPendaftaran()
    ui.setupUi(FrmPendaftaran)
    ui.signals()
    FrmPendaftaran.show()

    FrmLogin = QtWidgets.QMainWindow()
    ui_login = Ui_FrmLogin()
    ui_login.setupUi(FrmLogin)
    ui_login.signals()
        
    scheduler = BackgroundScheduler()
    
    scheduler.add_job(scheduling, 'interval', seconds=60)
    # scheduler.add_job(scheduling, 'interval', minutes=1)
    # scheduler.add_job(scheduling, 'cron', day_of_week='mon-sun', hour='18', minute="56", second="*/4")
    scheduler.start()
    
    sys.exit(app.exec_())