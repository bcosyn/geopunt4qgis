# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_geopunt4QgisDataCatalog.ui'
#
# Created: Wed Jul 23 15:32:10 2014
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
        geopunt4QgisDataCatalogDlg.resize(571, 534)
        geopunt4QgisDataCatalogDlg.setMinimumSize(QtCore.QSize(360, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntDataCatalogusSmall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        geopunt4QgisDataCatalogDlg.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(geopunt4QgisDataCatalogDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.zoekTxt = QtGui.QComboBox(geopunt4QgisDataCatalogDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoekTxt.sizePolicy().hasHeightForWidth())
        self.zoekTxt.setSizePolicy(sizePolicy)
        self.zoekTxt.setEditable(True)
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
        self.filterBox = QtGui.QGroupBox(geopunt4QgisDataCatalogDlg)
        self.filterBox.setCheckable(True)
        self.filterBox.setChecked(False)
        self.filterBox.setObjectName(_fromUtf8("filterBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.filterBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.filterWgt = QtGui.QWidget(self.filterBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterWgt.sizePolicy().hasHeightForWidth())
        self.filterWgt.setSizePolicy(sizePolicy)
        self.filterWgt.setObjectName(_fromUtf8("filterWgt"))
        self.gridLayout = QtGui.QGridLayout(self.filterWgt)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.bronLbl = QtGui.QLabel(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bronLbl.sizePolicy().hasHeightForWidth())
        self.bronLbl.setSizePolicy(sizePolicy)
        self.bronLbl.setObjectName(_fromUtf8("bronLbl"))
        self.gridLayout.addWidget(self.bronLbl, 6, 0, 2, 1)
        self.INSPIREthemaCbx = QtGui.QComboBox(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INSPIREthemaCbx.sizePolicy().hasHeightForWidth())
        self.INSPIREthemaCbx.setSizePolicy(sizePolicy)
        self.INSPIREthemaCbx.setSizeIncrement(QtCore.QSize(0, 0))
        self.INSPIREthemaCbx.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.INSPIREthemaCbx.setFrame(True)
        self.INSPIREthemaCbx.setObjectName(_fromUtf8("INSPIREthemaCbx"))
        self.gridLayout.addWidget(self.INSPIREthemaCbx, 5, 3, 1, 1)
        self.GDIThemaCbx = QtGui.QComboBox(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GDIThemaCbx.sizePolicy().hasHeightForWidth())
        self.GDIThemaCbx.setSizePolicy(sizePolicy)
        self.GDIThemaCbx.setSizeIncrement(QtCore.QSize(0, 0))
        self.GDIThemaCbx.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.GDIThemaCbx.setFrame(True)
        self.GDIThemaCbx.setObjectName(_fromUtf8("GDIThemaCbx"))
        self.gridLayout.addWidget(self.GDIThemaCbx, 4, 1, 1, 1)
        self.organisatiesCbx = QtGui.QComboBox(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.organisatiesCbx.sizePolicy().hasHeightForWidth())
        self.organisatiesCbx.setSizePolicy(sizePolicy)
        self.organisatiesCbx.setSizeIncrement(QtCore.QSize(0, 0))
        self.organisatiesCbx.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.organisatiesCbx.setFrame(True)
        self.organisatiesCbx.setObjectName(_fromUtf8("organisatiesCbx"))
        self.gridLayout.addWidget(self.organisatiesCbx, 5, 1, 1, 1)
        self.organisatiesLbl = QtGui.QLabel(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.organisatiesLbl.sizePolicy().hasHeightForWidth())
        self.organisatiesLbl.setSizePolicy(sizePolicy)
        self.organisatiesLbl.setObjectName(_fromUtf8("organisatiesLbl"))
        self.gridLayout.addWidget(self.organisatiesLbl, 5, 0, 1, 1)
        self.GDIthemalbl = QtGui.QLabel(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GDIthemalbl.sizePolicy().hasHeightForWidth())
        self.GDIthemalbl.setSizePolicy(sizePolicy)
        self.GDIthemalbl.setObjectName(_fromUtf8("GDIthemalbl"))
        self.gridLayout.addWidget(self.GDIthemalbl, 4, 0, 1, 1)
        self.bronCbx = QtGui.QComboBox(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bronCbx.sizePolicy().hasHeightForWidth())
        self.bronCbx.setSizePolicy(sizePolicy)
        self.bronCbx.setSizeIncrement(QtCore.QSize(0, 0))
        self.bronCbx.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bronCbx.setFrame(True)
        self.bronCbx.setObjectName(_fromUtf8("bronCbx"))
        self.gridLayout.addWidget(self.bronCbx, 6, 1, 1, 1)
        self.INSPIREthemaLbl = QtGui.QLabel(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INSPIREthemaLbl.sizePolicy().hasHeightForWidth())
        self.INSPIREthemaLbl.setSizePolicy(sizePolicy)
        self.INSPIREthemaLbl.setObjectName(_fromUtf8("INSPIREthemaLbl"))
        self.gridLayout.addWidget(self.INSPIREthemaLbl, 5, 2, 1, 1)
        self.INSPIREannexLbl = QtGui.QLabel(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INSPIREannexLbl.sizePolicy().hasHeightForWidth())
        self.INSPIREannexLbl.setSizePolicy(sizePolicy)
        self.INSPIREannexLbl.setObjectName(_fromUtf8("INSPIREannexLbl"))
        self.gridLayout.addWidget(self.INSPIREannexLbl, 4, 2, 1, 1)
        self.INSPIREannexCbx = QtGui.QComboBox(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INSPIREannexCbx.sizePolicy().hasHeightForWidth())
        self.INSPIREannexCbx.setSizePolicy(sizePolicy)
        self.INSPIREannexCbx.setSizeIncrement(QtCore.QSize(0, 0))
        self.INSPIREannexCbx.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.INSPIREannexCbx.setFrame(True)
        self.INSPIREannexCbx.setObjectName(_fromUtf8("INSPIREannexCbx"))
        self.gridLayout.addWidget(self.INSPIREannexCbx, 4, 3, 1, 1)
        self.INSPIREserviceLbl = QtGui.QLabel(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INSPIREserviceLbl.sizePolicy().hasHeightForWidth())
        self.INSPIREserviceLbl.setSizePolicy(sizePolicy)
        self.INSPIREserviceLbl.setObjectName(_fromUtf8("INSPIREserviceLbl"))
        self.gridLayout.addWidget(self.INSPIREserviceLbl, 6, 2, 1, 1)
        self.INSPIREserviceCbx = QtGui.QComboBox(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INSPIREserviceCbx.sizePolicy().hasHeightForWidth())
        self.INSPIREserviceCbx.setSizePolicy(sizePolicy)
        self.INSPIREserviceCbx.setSizeIncrement(QtCore.QSize(0, 0))
        self.INSPIREserviceCbx.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.INSPIREserviceCbx.setFrame(True)
        self.INSPIREserviceCbx.setObjectName(_fromUtf8("INSPIREserviceCbx"))
        self.gridLayout.addWidget(self.INSPIREserviceCbx, 6, 3, 1, 1)
        self.typeCbx = QtGui.QComboBox(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeCbx.sizePolicy().hasHeightForWidth())
        self.typeCbx.setSizePolicy(sizePolicy)
        self.typeCbx.setSizeIncrement(QtCore.QSize(0, 0))
        self.typeCbx.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.typeCbx.setFrame(True)
        self.typeCbx.setObjectName(_fromUtf8("typeCbx"))
        self.gridLayout.addWidget(self.typeCbx, 8, 1, 1, 1)
        self.typeLbl = QtGui.QLabel(self.filterWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeLbl.sizePolicy().hasHeightForWidth())
        self.typeLbl.setSizePolicy(sizePolicy)
        self.typeLbl.setObjectName(_fromUtf8("typeLbl"))
        self.gridLayout.addWidget(self.typeLbl, 8, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.filterWgt)
        self.verticalLayout.addWidget(self.filterBox)
        self.splitter = QtGui.QSplitter(geopunt4QgisDataCatalogDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.resultWgt = QtGui.QFrame(self.splitter)
        self.resultWgt.setMinimumSize(QtCore.QSize(120, 0))
        self.resultWgt.setBaseSize(QtCore.QSize(200, 0))
        self.resultWgt.setFrameShape(QtGui.QFrame.Panel)
        self.resultWgt.setFrameShadow(QtGui.QFrame.Sunken)
        self.resultWgt.setObjectName(_fromUtf8("resultWgt"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.resultWgt)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.resultView = QtGui.QListView(self.resultWgt)
        self.resultView.setMinimumSize(QtCore.QSize(100, 0))
        self.resultView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.resultView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.resultView.setAlternatingRowColors(True)
        self.resultView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.resultView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.resultView.setObjectName(_fromUtf8("resultView"))
        self.verticalLayout_2.addWidget(self.resultView)
        self.pagingWgt = QtGui.QWidget(self.resultWgt)
        self.pagingWgt.setObjectName(_fromUtf8("pagingWgt"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.pagingWgt)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pagePrvBtn = QtGui.QPushButton(self.pagingWgt)
        self.pagePrvBtn.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/previous.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pagePrvBtn.setIcon(icon2)
        self.pagePrvBtn.setIconSize(QtCore.QSize(12, 12))
        self.pagePrvBtn.setObjectName(_fromUtf8("pagePrvBtn"))
        self.horizontalLayout_3.addWidget(self.pagePrvBtn)
        self.pageLbl = QtGui.QLabel(self.pagingWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageLbl.sizePolicy().hasHeightForWidth())
        self.pageLbl.setSizePolicy(sizePolicy)
        self.pageLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.pageLbl.setObjectName(_fromUtf8("pageLbl"))
        self.horizontalLayout_3.addWidget(self.pageLbl)
        self.pageNextBtn = QtGui.QPushButton(self.pagingWgt)
        self.pageNextBtn.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/Next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pageNextBtn.setIcon(icon3)
        self.pageNextBtn.setIconSize(QtCore.QSize(12, 12))
        self.pageNextBtn.setObjectName(_fromUtf8("pageNextBtn"))
        self.horizontalLayout_3.addWidget(self.pageNextBtn)
        self.verticalLayout_2.addWidget(self.pagingWgt)
        self.modelFilter = QtGui.QFrame(self.resultWgt)
        self.modelFilter.setFrameShape(QtGui.QFrame.NoFrame)
        self.modelFilter.setFrameShadow(QtGui.QFrame.Sunken)
        self.modelFilter.setObjectName(_fromUtf8("modelFilter"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.modelFilter)
        self.horizontalLayout_6.setMargin(1)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label = QtGui.QLabel(self.modelFilter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.modelFilterCbx = QtGui.QComboBox(self.modelFilter)
        self.modelFilterCbx.setObjectName(_fromUtf8("modelFilterCbx"))
        self.modelFilterCbx.addItem(_fromUtf8(""))
        self.modelFilterCbx.addItem(_fromUtf8(""))
        self.modelFilterCbx.addItem(_fromUtf8(""))
        self.modelFilterCbx.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.modelFilterCbx)
        self.verticalLayout_2.addWidget(self.modelFilter)
        self.descriptionText = QtGui.QTextBrowser(self.splitter)
        self.descriptionText.setFrameShape(QtGui.QFrame.StyledPanel)
        self.descriptionText.setFrameShadow(QtGui.QFrame.Sunken)
        self.descriptionText.setOpenExternalLinks(True)
        self.descriptionText.setObjectName(_fromUtf8("descriptionText"))
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.addWMSbtn = QtGui.QPushButton(geopunt4QgisDataCatalogDlg)
        self.addWMSbtn.setEnabled(False)
        self.addWMSbtn.setMinimumSize(QtCore.QSize(0, 0))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/Wms.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addWMSbtn.setIcon(icon4)
        self.addWMSbtn.setAutoDefault(False)
        self.addWMSbtn.setObjectName(_fromUtf8("addWMSbtn"))
        self.horizontalLayout_2.addWidget(self.addWMSbtn)
        self.addWFSbtn = QtGui.QPushButton(geopunt4QgisDataCatalogDlg)
        self.addWFSbtn.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/Wfs.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addWFSbtn.setIcon(icon5)
        self.addWFSbtn.setAutoDefault(False)
        self.addWFSbtn.setObjectName(_fromUtf8("addWFSbtn"))
        self.horizontalLayout_2.addWidget(self.addWFSbtn)
        self.DLbtn = QtGui.QPushButton(geopunt4QgisDataCatalogDlg)
        self.DLbtn.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/zip.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DLbtn.setIcon(icon6)
        self.DLbtn.setObjectName(_fromUtf8("DLbtn"))
        self.horizontalLayout_2.addWidget(self.DLbtn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.msgLbl = QtGui.QLabel(geopunt4QgisDataCatalogDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msgLbl.sizePolicy().hasHeightForWidth())
        self.msgLbl.setSizePolicy(sizePolicy)
        self.msgLbl.setText(_fromUtf8(""))
        self.msgLbl.setObjectName(_fromUtf8("msgLbl"))
        self.horizontalLayout_4.addWidget(self.msgLbl)
        self.buttonBox = QtGui.QDialogButtonBox(geopunt4QgisDataCatalogDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Help)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_4.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.addWMSaction = QtGui.QAction(geopunt4QgisDataCatalogDlg)
        self.addWMSaction.setObjectName(_fromUtf8("addWMSaction"))
        self.Download_action = QtGui.QAction(geopunt4QgisDataCatalogDlg)
        self.Download_action.setObjectName(_fromUtf8("Download_action"))
        self.addWFSaction = QtGui.QAction(geopunt4QgisDataCatalogDlg)
        self.addWFSaction.setObjectName(_fromUtf8("addWFSaction"))

        self.retranslateUi(geopunt4QgisDataCatalogDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), geopunt4QgisDataCatalogDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), geopunt4QgisDataCatalogDlg.reject)
        QtCore.QObject.connect(self.filterBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.filterWgt.setVisible)
        QtCore.QMetaObject.connectSlotsByName(geopunt4QgisDataCatalogDlg)

    def retranslateUi(self, geopunt4QgisDataCatalogDlg):
        geopunt4QgisDataCatalogDlg.setWindowTitle(_translate("geopunt4QgisDataCatalogDlg", "Datacatalogus", None))
        self.zoekBtn.setText(_translate("geopunt4QgisDataCatalogDlg", "Zoek", None))
        self.filterBox.setTitle(_translate("geopunt4QgisDataCatalogDlg", "Filters", None))
        self.bronLbl.setText(_translate("geopunt4QgisDataCatalogDlg", "Bron catalogus:", None))
        self.organisatiesLbl.setText(_translate("geopunt4QgisDataCatalogDlg", "Organisatie:", None))
        self.GDIthemalbl.setText(_translate("geopunt4QgisDataCatalogDlg", "GDI-thema: ", None))
        self.INSPIREthemaLbl.setText(_translate("geopunt4QgisDataCatalogDlg", "INSPIRE thema:", None))
        self.INSPIREannexLbl.setText(_translate("geopunt4QgisDataCatalogDlg", "INSPIRE annex:", None))
        self.INSPIREserviceLbl.setText(_translate("geopunt4QgisDataCatalogDlg", "INSPIRE-servicetype:", None))
        self.typeLbl.setText(_translate("geopunt4QgisDataCatalogDlg", "Type:", None))
        self.pageLbl.setText(_translate("geopunt4QgisDataCatalogDlg", "0-0/0", None))
        self.label.setText(_translate("geopunt4QgisDataCatalogDlg", "Toon lagen met:", None))
        self.modelFilterCbx.setItemText(0, _translate("geopunt4QgisDataCatalogDlg", "Alle lagen", None))
        self.modelFilterCbx.setItemText(1, _translate("geopunt4QgisDataCatalogDlg", "WMS", None))
        self.modelFilterCbx.setItemText(2, _translate("geopunt4QgisDataCatalogDlg", "WFS", None))
        self.modelFilterCbx.setItemText(3, _translate("geopunt4QgisDataCatalogDlg", "Download", None))
        self.addWMSbtn.setText(_translate("geopunt4QgisDataCatalogDlg", "WMS toevoegen", None))
        self.addWFSbtn.setText(_translate("geopunt4QgisDataCatalogDlg", "WFS toevoegen", None))
        self.DLbtn.setText(_translate("geopunt4QgisDataCatalogDlg", "Downloaden", None))
        self.addWMSaction.setText(_translate("geopunt4QgisDataCatalogDlg", "WMS toevoegen", None))
        self.Download_action.setText(_translate("geopunt4QgisDataCatalogDlg", "Downloadpagina openen", None))
        self.addWFSaction.setText(_translate("geopunt4QgisDataCatalogDlg", "WFS toevoegen", None))

import resources_rc
