
import sys 
import os 
from os.path import expanduser
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget,QListView,QVBoxLayout,QMainWindow,QMessageBox,QLabel
from PyQt5.QtGui import QIcon
import Ui_mainwindow
from functools import partial
import page
import listview

class MainWindows(QMainWindow): #窗体基本设置
    default_download_path = '{}/Music/'.format(expanduser('~'))

    def __init__(self):
        super().__init__()
        self.ui = Ui_mainwindow.Ui_KuwoSpider()
        
    def init_window(self):
        #设置窗体名字，图标及大小
        self.setWindowTitle('酷我音乐爬虫')
        ico_path = os.path.join(os.path.dirname(__file__), '1.ico')
        self.setWindowIcon(QIcon(ico_path)) 
        self.resize(1500,1200)

        #设置按钮功能
        self.ui.singername_button.clicked.connect(partial(self.song_list,self.ui))
        self.ui.rank_button.clicked.connect(partial(self.rank_song,self.ui))
        self.ui.all_button.clicked.connect(partial(self.rank_list,self.ui))
        self.ui.cloud_button.clicked.connect(partial(self.hotword_list,self.ui))
        self.ui.hotword_button.clicked.connect(partial(self.hotword_song,self.ui))

    def get_input(self,ui): #获得文本框的输入信息
        self.singername = str(ui.input_singername.text())
        self.path = str(ui.input_way.text()) if len(str(ui.input_way.text())) else MainWindows.default_download_path

    def song_list(self,ui): #弹出歌手歌曲列表+下载对应歌曲
        self.get_input(self.ui)
        page.PageChange.flag = 1
        if self.singername != '':
            self.page = page.PageChange(self.path,self.singername,'song')
            self.page.show()
        else:
            QMessageBox.information(self,'搜索提示','请输入关键词！')

    def rank_song(self,ui): #弹出榜单歌曲列表+下载对应歌曲
        self.get_input(self.ui)
        try:
            ui.input_rank.setText(listview.ListView.Rank_Name)
            self.page = page.PageChange(self.path,'rank','rank')
            self.page.show()
        except:
            QMessageBox.information(self,'搜索提示','请先点击‘获取榜单列表’！')

    def rank_list(self,ui): #弹出全部榜单列表+进入指定榜单+下载歌曲
        self.get_input(self.ui)
        page.PageChange.flag = 1
        self.page = page.PageControl(self.path,None,'rank')
        self.page.show()
    
    def hotword_list(self,ui):
        page.PageChange.flag = 1
        self.page = page.PageControl(self.path,'hotword','song')
        self.page.show()
    
    def hotword_song(self,ui):
        self.get_input(self.ui)
        try:
            ui.input_hotword.setText(listview.ListView.Hotword_Name)
            self.page = page.PageChange(self.path,listview.ListView.Hotword_Name,'song')
            self.page.show()
        except:
            QMessageBox.information(self,'搜索提示','请先点击‘获取热词列表’！')

if __name__ == '__main__':
    app=QApplication(sys.argv)  
    MainWindow =MainWindows()
    MainWindow.ui.setupUi(MainWindow)
    MainWindow.init_window()  
    MainWindow.get_input(MainWindow.ui)
    MainWindow.show()
    sys.exit(app.exec())