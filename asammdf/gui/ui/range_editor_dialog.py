# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'range_editor_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RangeDialog(object):
    def setupUi(self, RangeDialog):
        RangeDialog.setObjectName("RangeDialog")
        RangeDialog.resize(834, 485)
        RangeDialog.setSizeGripEnabled(True)
        RangeDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(RangeDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.ranges = MinimalListWidget(RangeDialog)
        self.ranges.setObjectName("ranges")
        self.gridLayout.addWidget(self.ranges, 0, 0, 7, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 271, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.reset_btn = QtWidgets.QPushButton(RangeDialog)
        self.reset_btn.setObjectName("reset_btn")
        self.gridLayout.addWidget(self.reset_btn, 3, 1, 1, 1)
        self.cancel_btn = QtWidgets.QPushButton(RangeDialog)
        self.cancel_btn.setObjectName("cancel_btn")
        self.gridLayout.addWidget(self.cancel_btn, 6, 1, 1, 1)
        self.apply_btn = QtWidgets.QPushButton(RangeDialog)
        self.apply_btn.setObjectName("apply_btn")
        self.gridLayout.addWidget(self.apply_btn, 5, 1, 1, 1)
        self.insert_btn = QtWidgets.QPushButton(RangeDialog)
        self.insert_btn.setObjectName("insert_btn")
        self.gridLayout.addWidget(self.insert_btn, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setRowStretch(4, 1)

        self.retranslateUi(RangeDialog)
        QtCore.QMetaObject.connectSlotsByName(RangeDialog)
        RangeDialog.setTabOrder(self.ranges, self.apply_btn)
        RangeDialog.setTabOrder(self.apply_btn, self.cancel_btn)

    def retranslateUi(self, RangeDialog):
        _translate = QtCore.QCoreApplication.translate
        RangeDialog.setWindowTitle(_translate("RangeDialog", "Edit value range colors"))
        self.reset_btn.setText(_translate("RangeDialog", "Reset"))
        self.cancel_btn.setText(_translate("RangeDialog", "Cancel"))
        self.apply_btn.setText(_translate("RangeDialog", "Apply"))
        self.insert_btn.setText(_translate("RangeDialog", "Insert range"))
from asammdf.gui.widgets.list import MinimalListWidget
