# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmDokter.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmDokter(object):
    def setupUi(self, FrmDokter):
        FrmDokter.setObjectName("FrmDokter")
        FrmDokter.resize(604, 521)
        self.centralwidget = QtWidgets.QWidget(FrmDokter)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 581, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 60, 581, 392))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(40)
        self.formLayout.setObjectName("formLayout")
        self.idDokterLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.idDokterLabel.setIndent(-1)
        self.idDokterLabel.setObjectName("idDokterLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.idDokterLabel)
        self.Txt_IdDokter = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_IdDokter.setObjectName("Txt_IdDokter")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Txt_IdDokter)
        self.namaLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.namaLabel.setObjectName("namaLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.namaLabel)
        self.Txt_Nama = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_Nama.setObjectName("Txt_Nama")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Txt_Nama)
        self.bidangLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.bidangLabel.setObjectName("bidangLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.bidangLabel)
        self.Cmb_Bidang = QtWidgets.QComboBox(self.formLayoutWidget)
        self.Cmb_Bidang.setObjectName("Cmb_Bidang")
        self.Cmb_Bidang.addItem("")
        self.Cmb_Bidang.addItem("")
        self.Cmb_Bidang.addItem("")
        self.Cmb_Bidang.addItem("")
        self.Cmb_Bidang.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Cmb_Bidang)
        self.jadwalLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.jadwalLabel.setObjectName("jadwalLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.jadwalLabel)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Chk_Senin = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.Chk_Senin.setObjectName("Chk_Senin")
        self.horizontalLayout_3.addWidget(self.Chk_Senin)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.Time1_Buka = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.Time1_Buka.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 2), QtCore.QTime(8, 0, 0)))
        self.Time1_Buka.setObjectName("Time1_Buka")
        self.horizontalLayout_2.addWidget(self.Time1_Buka)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.Time1_Tutup = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.Time1_Tutup.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(12, 0, 0)))
        self.Time1_Tutup.setObjectName("Time1_Tutup")
        self.horizontalLayout.addWidget(self.Time1_Tutup)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Chk_Selasa = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.Chk_Selasa.setObjectName("Chk_Selasa")
        self.horizontalLayout_4.addWidget(self.Chk_Selasa)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.Time2_Buka = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.Time2_Buka.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(8, 0, 0)))
        self.Time2_Buka.setObjectName("Time2_Buka")
        self.horizontalLayout_5.addWidget(self.Time2_Buka)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.Time2_Tutup = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.Time2_Tutup.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(12, 0, 0)))
        self.Time2_Tutup.setObjectName("Time2_Tutup")
        self.horizontalLayout_6.addWidget(self.Time2_Tutup)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Chk_Rabu = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.Chk_Rabu.setObjectName("Chk_Rabu")
        self.horizontalLayout_7.addWidget(self.Chk_Rabu)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.Time3_Buka = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.Time3_Buka.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(8, 0, 0)))
        self.Time3_Buka.setObjectName("Time3_Buka")
        self.horizontalLayout_8.addWidget(self.Time3_Buka)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.Time3_Tutup = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.Time3_Tutup.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(12, 0, 0)))
        self.Time3_Tutup.setObjectName("Time3_Tutup")
        self.horizontalLayout_9.addWidget(self.Time3_Tutup)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Chk_Kamis = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.Chk_Kamis.setObjectName("Chk_Kamis")
        self.horizontalLayout_10.addWidget(self.Chk_Kamis)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.Time4_Buka = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.Time4_Buka.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(8, 0, 0)))
        self.Time4_Buka.setObjectName("Time4_Buka")
        self.horizontalLayout_11.addWidget(self.Time4_Buka)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_12.addWidget(self.label_9)
        self.Time4_Tutup = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.Time4_Tutup.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(12, 0, 0)))
        self.Time4_Tutup.setObjectName("Time4_Tutup")
        self.horizontalLayout_12.addWidget(self.Time4_Tutup)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_12)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.Chk_Jumat = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.Chk_Jumat.setObjectName("Chk_Jumat")
        self.horizontalLayout_13.addWidget(self.Chk_Jumat)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_14.addWidget(self.label_10)
        self.Time5_Buka = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.Time5_Buka.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(8, 0, 0)))
        self.Time5_Buka.setObjectName("Time5_Buka")
        self.horizontalLayout_14.addWidget(self.Time5_Buka)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_15.addWidget(self.label_11)
        self.Time5_Tutup = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.Time5_Tutup.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(12, 0, 0)))
        self.Time5_Tutup.setObjectName("Time5_Tutup")
        self.horizontalLayout_15.addWidget(self.Time5_Tutup)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_15)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.Chk_Sabtu = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.Chk_Sabtu.setObjectName("Chk_Sabtu")
        self.horizontalLayout_16.addWidget(self.Chk_Sabtu)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_17.addWidget(self.label_12)
        self.Time6_Buka = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.Time6_Buka.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(8, 0, 0)))
        self.Time6_Buka.setObjectName("Time6_Buka")
        self.horizontalLayout_17.addWidget(self.Time6_Buka)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_18.addWidget(self.label_13)
        self.Time6_Tutup = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.Time6_Tutup.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(12, 0, 0)))
        self.Time6_Tutup.setObjectName("Time6_Tutup")
        self.horizontalLayout_18.addWidget(self.Time6_Tutup)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_18)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.Chk_Minggu = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.Chk_Minggu.setObjectName("Chk_Minggu")
        self.horizontalLayout_19.addWidget(self.Chk_Minggu)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_20.addWidget(self.label_14)
        self.Time7_Buka = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.Time7_Buka.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(8, 0, 0)))
        self.Time7_Buka.setObjectName("Time7_Buka")
        self.horizontalLayout_20.addWidget(self.Time7_Buka)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_21.addWidget(self.label_15)
        self.Time7_Tutup = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.Time7_Tutup.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(12, 0, 0)))
        self.Time7_Tutup.setObjectName("Time7_Tutup")
        self.horizontalLayout_21.addWidget(self.Time7_Tutup)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_21)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.kapasitasLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.kapasitasLabel.setObjectName("kapasitasLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.kapasitasLabel)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setContentsMargins(-1, -1, 300, -1)
        self.horizontalLayout_23.setSpacing(20)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.Txt_Kapasitas = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_Kapasitas.setObjectName("Txt_Kapasitas")
        self.horizontalLayout_23.addWidget(self.Txt_Kapasitas)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_23.addWidget(self.label_16)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_23)
        self.phoneLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.phoneLabel.setObjectName("phoneLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.phoneLabel)
        self.Txt_Phone = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_Phone.setObjectName("Txt_Phone")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Txt_Phone)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 480, 293, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.PB_add = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_add.setObjectName("PB_add")
        self.horizontalLayout_22.addWidget(self.PB_add)
        self.PB_update = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_update.setObjectName("PB_update")
        self.horizontalLayout_22.addWidget(self.PB_update)
        self.PB_del = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_del.setObjectName("PB_del")
        self.horizontalLayout_22.addWidget(self.PB_del)
        FrmDokter.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrmDokter)
        QtCore.QMetaObject.connectSlotsByName(FrmDokter)
        FrmDokter.setTabOrder(self.Txt_IdDokter, self.Txt_Nama)
        FrmDokter.setTabOrder(self.Txt_Nama, self.Txt_Phone)
        FrmDokter.setTabOrder(self.Txt_Phone, self.Cmb_Bidang)
        FrmDokter.setTabOrder(self.Cmb_Bidang, self.Chk_Senin)
        FrmDokter.setTabOrder(self.Chk_Senin, self.Time1_Buka)
        FrmDokter.setTabOrder(self.Time1_Buka, self.Time1_Tutup)
        FrmDokter.setTabOrder(self.Time1_Tutup, self.Chk_Selasa)
        FrmDokter.setTabOrder(self.Chk_Selasa, self.Time2_Buka)
        FrmDokter.setTabOrder(self.Time2_Buka, self.Time2_Tutup)
        FrmDokter.setTabOrder(self.Time2_Tutup, self.Chk_Rabu)
        FrmDokter.setTabOrder(self.Chk_Rabu, self.Time3_Buka)
        FrmDokter.setTabOrder(self.Time3_Buka, self.Time3_Tutup)
        FrmDokter.setTabOrder(self.Time3_Tutup, self.Chk_Kamis)
        FrmDokter.setTabOrder(self.Chk_Kamis, self.Time4_Buka)
        FrmDokter.setTabOrder(self.Time4_Buka, self.Time4_Tutup)
        FrmDokter.setTabOrder(self.Time4_Tutup, self.Chk_Jumat)
        FrmDokter.setTabOrder(self.Chk_Jumat, self.Time5_Buka)
        FrmDokter.setTabOrder(self.Time5_Buka, self.Time5_Tutup)
        FrmDokter.setTabOrder(self.Time5_Tutup, self.Chk_Sabtu)
        FrmDokter.setTabOrder(self.Chk_Sabtu, self.Time6_Buka)
        FrmDokter.setTabOrder(self.Time6_Buka, self.Time6_Tutup)
        FrmDokter.setTabOrder(self.Time6_Tutup, self.Chk_Minggu)
        FrmDokter.setTabOrder(self.Chk_Minggu, self.Time7_Buka)
        FrmDokter.setTabOrder(self.Time7_Buka, self.Time7_Tutup)
        FrmDokter.setTabOrder(self.Time7_Tutup, self.Txt_Kapasitas)
        FrmDokter.setTabOrder(self.Txt_Kapasitas, self.PB_add)
        FrmDokter.setTabOrder(self.PB_add, self.PB_update)
        FrmDokter.setTabOrder(self.PB_update, self.PB_del)

    def retranslateUi(self, FrmDokter):
        _translate = QtCore.QCoreApplication.translate
        FrmDokter.setWindowTitle(_translate("FrmDokter", "FormDokter"))
        self.label.setText(_translate("FrmDokter", "DOKTER"))
        self.idDokterLabel.setText(_translate("FrmDokter", "IdDokter"))
        self.namaLabel.setText(_translate("FrmDokter", "Nama"))
        self.bidangLabel.setText(_translate("FrmDokter", "Bidang"))
        self.Cmb_Bidang.setItemText(0, _translate("FrmDokter", "Dokter Umum"))
        self.Cmb_Bidang.setItemText(1, _translate("FrmDokter", "Kandungan"))
        self.Cmb_Bidang.setItemText(2, _translate("FrmDokter", "Anak"))
        self.Cmb_Bidang.setItemText(3, _translate("FrmDokter", "Penyakit Dalam"))
        self.Cmb_Bidang.setItemText(4, _translate("FrmDokter", "Bedah"))
        self.jadwalLabel.setText(_translate("FrmDokter", "Jadwal"))
        self.Chk_Senin.setText(_translate("FrmDokter", "Senin"))
        self.label_3.setText(_translate("FrmDokter", "Jam Buka"))
        self.Time1_Buka.setDisplayFormat(_translate("FrmDokter", "h:mm"))
        self.label_2.setText(_translate("FrmDokter", "Jam Tutup"))
        self.Time1_Tutup.setDisplayFormat(_translate("FrmDokter", "h:mm"))
        self.Chk_Selasa.setText(_translate("FrmDokter", "Selasa"))
        self.label_4.setText(_translate("FrmDokter", "Jam Buka"))
        self.Time2_Buka.setDisplayFormat(_translate("FrmDokter", "h:mm"))
        self.label_5.setText(_translate("FrmDokter", "Jam Tutup"))
        self.Time2_Tutup.setDisplayFormat(_translate("FrmDokter", "h:mm"))
        self.Chk_Rabu.setText(_translate("FrmDokter", "Rabu"))
        self.label_6.setText(_translate("FrmDokter", "Jam Buka"))
        self.Time3_Buka.setDisplayFormat(_translate("FrmDokter", "h:mm"))
        self.label_7.setText(_translate("FrmDokter", "Jam Tutup"))
        self.Time3_Tutup.setDisplayFormat(_translate("FrmDokter", "h:mm"))
        self.Chk_Kamis.setText(_translate("FrmDokter", "Kamis"))
        self.label_8.setText(_translate("FrmDokter", "Jam Buka"))
        self.Time4_Buka.setDisplayFormat(_translate("FrmDokter", "h:mm"))
        self.label_9.setText(_translate("FrmDokter", "Jam Tutup"))
        self.Time4_Tutup.setDisplayFormat(_translate("FrmDokter", "h:mm"))
        self.Chk_Jumat.setText(_translate("FrmDokter", "Jumat"))
        self.label_10.setText(_translate("FrmDokter", "Jam Buka"))
        self.Time5_Buka.setDisplayFormat(_translate("FrmDokter", "h:mm"))
        self.label_11.setText(_translate("FrmDokter", "Jam Tutup"))
        self.Time5_Tutup.setDisplayFormat(_translate("FrmDokter", "h:mm"))
        self.Chk_Sabtu.setText(_translate("FrmDokter", "Sabtu"))
        self.label_12.setText(_translate("FrmDokter", "Jam Buka"))
        self.Time6_Buka.setDisplayFormat(_translate("FrmDokter", "h:mm"))
        self.label_13.setText(_translate("FrmDokter", "Jam Tutup"))
        self.Time6_Tutup.setDisplayFormat(_translate("FrmDokter", "h:mm"))
        self.Chk_Minggu.setText(_translate("FrmDokter", "Minggu"))
        self.label_14.setText(_translate("FrmDokter", "Jam Buka"))
        self.Time7_Buka.setDisplayFormat(_translate("FrmDokter", "h:mm"))
        self.label_15.setText(_translate("FrmDokter", "Jam Tutup"))
        self.Time7_Tutup.setDisplayFormat(_translate("FrmDokter", "h:mm"))
        self.kapasitasLabel.setText(_translate("FrmDokter", "Kapasitas"))
        self.label_16.setText(_translate("FrmDokter", "orang / jam"))
        self.phoneLabel.setText(_translate("FrmDokter", "Phone"))
        self.PB_add.setText(_translate("FrmDokter", "Add"))
        self.PB_update.setText(_translate("FrmDokter", "Update"))
        self.PB_del.setText(_translate("FrmDokter", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmDokter = QtWidgets.QMainWindow()
    ui = Ui_FrmDokter()
    ui.setupUi(FrmDokter)
    FrmDokter.show()
    sys.exit(app.exec_())
