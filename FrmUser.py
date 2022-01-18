# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmUser.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmUser(object):
    def setupUi(self, FrmUser):
        FrmUser.setObjectName("FrmUser")
        FrmUser.resize(324, 297)
        FrmUser.setMaximumSize(QtCore.QSize(324, 297))
        self.centralwidget = QtWidgets.QWidget(FrmUser)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 301, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 24, 0, 0)
        self.formLayout.setHorizontalSpacing(24)
        self.formLayout.setObjectName("formLayout")
        self.idUserLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.idUserLabel.setObjectName("idUserLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.idUserLabel)
        self.Txt_id_user = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_id_user.setObjectName("Txt_id_user")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Txt_id_user)
        self.namaLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.namaLabel.setObjectName("namaLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.namaLabel)
        self.Txt_nama = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_nama.setObjectName("Txt_nama")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Txt_nama)
        self.passwordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.Txt_password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_password.setObjectName("Txt_password")
        self.Txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Txt_password)
        self.roleLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.roleLabel.setObjectName("roleLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.roleLabel)
        self.Cmb_role = QtWidgets.QComboBox(self.formLayoutWidget)
        self.Cmb_role.setEnabled(True)
        self.Cmb_role.setEditable(False)
        self.Cmb_role.setDuplicatesEnabled(False)
        self.Cmb_role.setObjectName("Cmb_role")
        self.Cmb_role.addItem("")
        self.Cmb_role.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Cmb_role)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 250, 301, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PB_add = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.PB_add.setObjectName("PB_add")
        self.horizontalLayout_2.addWidget(self.PB_add)
        self.PB_update = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.PB_update.setObjectName("PB_update")
        self.horizontalLayout_2.addWidget(self.PB_update)
        self.PB_del = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.PB_del.setObjectName("PB_del")
        self.horizontalLayout_2.addWidget(self.PB_del)
        FrmUser.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrmUser)
        QtCore.QMetaObject.connectSlotsByName(FrmUser)

    def retranslateUi(self, FrmUser):
        _translate = QtCore.QCoreApplication.translate
        FrmUser.setWindowTitle(_translate("FrmUser", "User"))
        self.label.setText(_translate("FrmUser", "USER"))
        self.idUserLabel.setText(_translate("FrmUser", "Id User"))
        self.namaLabel.setText(_translate("FrmUser", "Nama"))
        self.passwordLabel.setText(_translate("FrmUser", "Password"))
        self.roleLabel.setText(_translate("FrmUser", "Role"))
        self.Cmb_role.setItemText(0, _translate("FrmUser", "Admin"))
        self.Cmb_role.setItemText(1, _translate("FrmUser", "User"))
        self.PB_add.setText(_translate("FrmUser", "Add"))
        self.PB_update.setText(_translate("FrmUser", "Update"))
        self.PB_del.setText(_translate("FrmUser", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmUser = QtWidgets.QMainWindow()
    ui = Ui_FrmUser()
    ui.setupUi(FrmUser)
    FrmUser.show()
    sys.exit(app.exec_())
