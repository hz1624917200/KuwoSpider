# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\learn\大二上\小学期\all\code\spiderui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import picture_rc


class Ui_KuwoSpider(object):
	def setupUi(self, KuwoSpider):
		KuwoSpider.setObjectName("KuwoSpider")
		KuwoSpider.setEnabled(True)
		KuwoSpider.resize(800, 575)
		KuwoSpider.setIconSize(QtCore.QSize(30, 30))
		self.centralwidget = QtWidgets.QWidget(KuwoSpider)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
		self.input_singername = QtWidgets.QLineEdit(self.centralwidget)
		self.input_singername.setObjectName("input_singername")
		self.gridLayout.addWidget(self.input_singername, 1, 2, 1, 1)
		self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
		self.textBrowser_2.setEnabled(False)
		self.textBrowser_2.setObjectName("textBrowser_2")
		self.gridLayout.addWidget(self.textBrowser_2, 0, 0, 1, 5)
		self.input_rank = QtWidgets.QLineEdit(self.centralwidget)
		self.input_rank.setEnabled(False)
		self.input_rank.setText("")
		self.input_rank.setObjectName("input_rank")
		self.gridLayout.addWidget(self.input_rank, 2, 2, 1, 1)
		self.input_way = QtWidgets.QLineEdit(self.centralwidget)
		self.input_way.setObjectName("input_way")
		self.gridLayout.addWidget(self.input_way, 1, 4, 1, 1)
		self.rank_name = QtWidgets.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setFamily("宋体")
		font.setPointSize(10)
		font.setItalic(True)
		self.rank_name.setFont(font)
		self.rank_name.setObjectName("rank_name")
		self.gridLayout.addWidget(self.rank_name, 2, 0, 1, 1)
		self.rank_button = QtWidgets.QPushButton(self.centralwidget)
		self.rank_button.setObjectName("rank_button")
		self.gridLayout.addWidget(self.rank_button, 2, 5, 1, 1)
		self.hotword_name = QtWidgets.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setFamily("宋体")
		font.setPointSize(10)
		self.hotword_name.setFont(font)
		self.hotword_name.setObjectName("hotword_name")
		self.gridLayout.addWidget(self.hotword_name, 3, 0, 1, 1)
		self.url_name = QtWidgets.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setFamily("宋体")
		font.setPointSize(10)
		font.setItalic(True)
		self.url_name.setFont(font)
		self.url_name.setObjectName("url_name")
		self.gridLayout.addWidget(self.url_name, 1, 0, 1, 1)
		self.label = QtWidgets.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setFamily("宋体")
		font.setPointSize(10)
		font.setItalic(True)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.gridLayout.addWidget(self.label, 1, 3, 1, 1)
		self.all_button = QtWidgets.QPushButton(self.centralwidget)
		self.all_button.setObjectName("all_button")
		self.gridLayout.addWidget(self.all_button, 2, 3, 1, 2)
		self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
		self.textBrowser.setEnabled(False)
		self.textBrowser.setObjectName("textBrowser")
		self.gridLayout.addWidget(self.textBrowser, 0, 5, 1, 1)
		self.singername_button = QtWidgets.QPushButton(self.centralwidget)
		self.singername_button.setObjectName("singername_button")
		self.gridLayout.addWidget(self.singername_button, 1, 5, 1, 1)
		self.input_hotword = QtWidgets.QLineEdit(self.centralwidget)
		self.input_hotword.setEnabled(False)
		self.input_hotword.setObjectName("input_hotword")
		self.gridLayout.addWidget(self.input_hotword, 3, 2, 1, 1)
		self.cloud_button = QtWidgets.QPushButton(self.centralwidget)
		self.cloud_button.setObjectName("cloud_button")
		self.gridLayout.addWidget(self.cloud_button, 3, 3, 1, 2)
		self.hotword_button = QtWidgets.QPushButton(self.centralwidget)
		self.hotword_button.setObjectName("hotword_button")
		self.gridLayout.addWidget(self.hotword_button, 3, 5, 1, 1)
		KuwoSpider.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(KuwoSpider)
		self.statusbar.setObjectName("statusbar")
		KuwoSpider.setStatusBar(self.statusbar)

		self.retranslateUi(KuwoSpider)
		QtCore.QMetaObject.connectSlotsByName(KuwoSpider)

	def retranslateUi(self, KuwoSpider):
		_translate = QtCore.QCoreApplication.translate
		KuwoSpider.setWindowTitle(_translate("KuwoSpider", "MainWindow"))
		self.input_singername.setText(_translate("KuwoSpider", "宋东野"))
		self.textBrowser_2.setHtml(_translate("KuwoSpider",
		                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
		                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
		                                      "p, li { white-space: pre-wrap; }\n"
		                                      "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
		                                      "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; font-style:italic;\">酷我音乐爬虫系统</span></p>\n"
		                                      "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">by ZhengHuang and HeQi</span></p>\n"
		                                      "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/picture/2.jpeg\" /></p></body></html>"))
		self.rank_name.setText(_translate("KuwoSpider", "榜单名称"))
		self.rank_button.setText(_translate("KuwoSpider", "获取该榜单歌曲列表"))
		self.hotword_name.setText(_translate("KuwoSpider", "热词名称"))
		self.url_name.setText(_translate("KuwoSpider", "请输入歌手名字"))
		self.label.setText(_translate("KuwoSpider", "请输入下载路径"))
		self.all_button.setText(_translate("KuwoSpider", "获取榜单列表"))
		self.textBrowser.setHtml(_translate("KuwoSpider",
		                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
		                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
		                                    "p, li { white-space: pre-wrap; }\n"
		                                    "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
		                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">欢迎使用酷我音乐爬虫系统！以下为操作说明：</span></p>\n"
		                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">1.输入歌手名字和下载路径（可选），获得该歌手的歌曲列表，点击歌曲下载相应MP3至对应路径。如果要输入路径，请按照.././的格式输入，eg：d:/music/</span></p>\n"
		                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">2.点击‘获取榜单列表’获得所有榜单信息，选择其中一个，之后点击‘获取该榜单歌曲列表’获得对应榜单歌曲列表，下载方式同1（如果要切换榜单，请先点击‘获取榜单列表’）。</span></p>\n"
		                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">3.不知道听点什么好？点击‘获得热词列表’，获取随机榜单的热词排名，选择一个获得含有该排名的歌曲，下载方式同1,具体使用方式同2</span></p></body></html>"))
		self.singername_button.setText(_translate("KuwoSpider", "获得该歌手歌曲列表"))
		self.cloud_button.setText(_translate("KuwoSpider", "获得热词列表"))
		self.hotword_button.setText(_translate("KuwoSpider", "获取该热词歌曲列表"))



