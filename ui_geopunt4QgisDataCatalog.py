# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_geopunt4QgisDataCatalog.ui'
#
# Created: Tue Jul 15 22:25:17 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_geopunt4QgisDataCatalogDlg(object):
    def setupUi(self, geopunt4QgisDataCatalogDlg):
        geopunt4QgisDataCatalogDlg.setObjectName(_fromUtf8("geopunt4QgisDataCatalogDlg"))
        geopunt4QgisDataCatalogDlg.resize(537, 400)
        geopunt4QgisDataCatalogDlg.setMinimumSize(QtCore.QSize(360, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntDataCatalogusSmall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        geopunt4QgisDataCatalogDlg.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(geopunt4QgisDataCatalogDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.zoekTxt = QtGui.QLineEdit(geopunt4QgisDataCatalogDlg)
        self.zoekTxt.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.zoekTxt.setObjectName(_fromUtf8("zoekTxt"))
        self.horizontalLayout.addWidget(self.zoekTxt)
        self.zoekBtn = QtGui.QPushButton(geopunt4QgisDataCatalogDlg)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/magnifyingGlass.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoekBtn.setIcon(icon1)
        self.zoekBtn.setCheckable(False)
        self.zoekBtn.setAutoDefault(False)
        self.zoekBtn.setDefault(True)
        self.zoekBtn.setFlat(False)
        self.zoekBtn.setObjectName(_fromUtf8("zoekBtn"))
        self.horizontalLayout.addWidget(self.zoekBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter = QtGui.QSplitter(geopunt4QgisDataCatalogDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setMinimumSize(QtCore.QSize(120, 0))
        self.widget.setBaseSize(QtCore.QSize(200, 0))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.resultView = QtGui.QListView(self.widget)
        self.resultView.setMinimumSize(QtCore.QSize(100, 0))
        self.resultView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.resultView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.resultView.setAlternatingRowColors(True)
        self.resultView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.resultView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.resultView.setObjectName(_fromUtf8("resultView"))
        self.verticalLayout_2.addWidget(self.resultView)
        self.pagingWgt = QtGui.QWidget(self.widget)
        self.pagingWgt.setObjectName(_fromUtf8("pagingWgt"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.pagingWgt)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_2 = QtGui.QPushButton(self.pagingWgt)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pageLbl = QtGui.QLabel(self.pagingWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageLbl.sizePolicy().hasHeightForWidth())
        self.pageLbl.setSizePolicy(sizePolicy)
        self.pageLbl.setText(_fromUtf8(""))
        self.pageLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.pageLbl.setObjectName(_fromUtf8("pageLbl"))
        self.horizontalLayout_3.addWidget(self.pageLbl)
        self.pageNextBtn = QtGui.QPushButton(self.pagingWgt)
        self.pageNextBtn.setObjectName(_fromUtf8("pageNextBtn"))
        self.horizontalLayout_3.addWidget(self.pageNextBtn)
        self.verticalLayout_2.addWidget(self.pagingWgt)
        self.descriptionText = QtGui.QTextBrowser(self.splitter)
        self.descriptionText.setOpenExternalLinks(True)
        self.descriptionText.setObjectName(_fromUtf8("descriptionText"))
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.addWMSbtn = QtGui.QPushButton(geopunt4QgisDataCatalogDlg)
        self.addWMSbtn.setEnabled(False)
        self.addWMSbtn.setMinimumSize(QtCore.QSize(0, 0))
        self.addWMSbtn.setAutoDefault(False)
        self.addWMSbtn.setObjectName(_fromUtf8("addWMSbtn"))
        self.horizontalLayout_2.addWidget(self.addWMSbtn)
        self.addWFSbtn = QtGui.QPushButton(geopunt4QgisDataCatalogDlg)
        self.addWFSbtn.setEnabled(False)
        self.addWFSbtn.setAutoDefault(False)
        self.addWFSbtn.setObjectName(_fromUtf8("addWFSbtn"))
        self.horizontalLayout_2.addWidget(self.addWFSbtn)
        self.DLbtn = QtGui.QPushButton(geopunt4QgisDataCatalogDlg)
        self.DLbtn.setEnabled(False)
        self.DLbtn.setObjectName(_fromUtf8("DLbtn"))
        self.horizontalLayout_2.addWidget(self.DLbtn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(geopunt4QgisDataCatalogDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.addWMSaction = QtGui.QAction(geopunt4QgisDataCatalogDlg)
        self.addWMSaction.setObjectName(_fromUtf8("addWMSaction"))
        self.Download_action = QtGui.QAction(geopunt4QgisDataCatalogDlg)
        self.Download_action.setObjectName(_fromUtf8("Download_action"))
        self.addWFSaction = QtGui.QAction(geopunt4QgisDataCatalogDlg)
        self.addWFSaction.setObjectName(_fromUtf8("addWFSaction"))

        self.retranslateUi(geopunt4QgisDataCatalogDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), geopunt4QgisDataCatalogDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), geopunt4QgisDataCatalogDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(geopunt4QgisDataCatalogDlg)

    def retranslateUi(self, geopunt4QgisDataCatalogDlg):
        geopunt4QgisDataCatalogDlg.setWindowTitle(_translate("geopunt4QgisDataCatalogDlg", "Datacatalogus", None))
        self.zoekBtn.setText(_translate("geopunt4QgisDataCatalogDlg", "Zoek", None))
        self.pushButton_2.setText(_translate("geopunt4QgisDataCatalogDlg", "<", None))
        self.pageNextBtn.setText(_translate("geopunt4QgisDataCatalogDlg", ">", None))
        self.addWMSbtn.setText(_translate("geopunt4QgisDataCatalogDlg", "WMS toevoegen", None))
        self.addWFSbtn.setText(_translate("geopunt4QgisDataCatalogDlg", "WFS toevoegen", None))
        self.DLbtn.setText(_translate("geopunt4QgisDataCatalogDlg", "Downloaden", None))
        self.addWMSaction.setText(_translate("geopunt4QgisDataCatalogDlg", "WMS toevoegen", None))
        self.Download_action.setText(_translate("geopunt4QgisDataCatalogDlg", "Downloadpagina openen", None))
        self.addWFSaction.setText(_translate("geopunt4QgisDataCatalogDlg", "WFS toevoegen", None))

import resources_rc