
import sys
import os
from os.path import exists
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget,QListView,QMessageBox
o_path = os.getcwd()
sys.path.append(o_path)
import Network
import page
import Class

class ListView(QWidget): #列表类
    Ranksong_List = []
    def __init__(self,path, name,flag):
        super().__init__()
        self.name = name
        self.path = path
        self.flag = flag

    def download(self,qModelIndex): #从歌手列表或榜单列表下载歌曲
        if self.flag == 'rank':
            self.qList = [str(ch) for ch in ListView.Ranksong_List[0]]
            self.list = ListView.Ranksong_List[0]
        song_name = self.qList[qModelIndex.row()].split()[0]
        full_name = self.path + song_name +'.mp3'

        if exists(full_name):
            choice = QMessageBox.question(self,'下载提示','该歌曲已存在，要替换它吗？',QMessageBox.Yes |QMessageBox.No)

            if choice == QMessageBox.Yes:
                QMessageBox.information(self,'下载提示','替换成功！')
            else:
                i = 2
                while exists('{}{}({}).mp3'.format(self.path,song_name,i)):
                    i += 1
    
                self.list[self.qList.index(self.qList[qModelIndex.row()])].download(self.path,i)
                QMessageBox.information(self, "下载提示",song_name + '下载成功！下载至' + self.path + song_name + '(' + str(i) +')' + '.mp3')
        else:
            try:
                self.list[self.qList.index(self.qList[qModelIndex.row()])].download(self.path)
                QMessageBox.information(self, "下载提示",song_name + '下载成功！下载至' + full_name)
            except:
                QMessageBox.information(self,'下载提示','下载失败，已经尝试三次，请检查网络连接或代理设置')


    def get_ranksong(self,qModelIndex): #获取所有榜单
        try:
            self.rank_list = Network.fill_rank_list()
            self.qList = [str(ch) for ch in Network.fill_rank_list()]
            ListView.Ranksong_List = Network.search_by_list(self.rank_list[self.qList.index(self.qList[qModelIndex.row()])],page.PageChange.flag)     

        except:
            QMessageBox.information(self,'搜索提示','搜索失败，已经尝试3次，请检查网络连接或代理设置')

    def get_list(self): #获取歌手列表或榜单列表
        #try:
            if self.flag == 'song' and self.name != 'hotword':
                self.list = Network.search(self.name,page.PageChange.flag)[0]
                self.qList = [str(ch) for ch in self.list]
            elif self.name is None:  #获得总榜列表
                self.rank_list = Network.fill_rank_list()
                self.qList = [str(ch) for ch in Network.fill_rank_list()]
            elif self.name == 'hotword':
                hotword = Class.WordCloud()
                hotword.update(Network.fill_rank_list())
                self.qList = hotword.gen_word_list()
            else:
                pass
        #except:
            #QMessageBox.information(self,'搜索提示','搜索失败，已经尝试3次，请检查网络连接或代理设置')
    
    def message(self,qModelIndex):
        rank_name = self.qList[qModelIndex.row()].split()[0]
        QMessageBox.information(self,'搜索提示','你选择了' + rank_name + '!')
        ListView.qModelIndex = qModelIndex
        ListView.Rank_Name = rank_name
    
    def hotword_song(self,qModelIndex):
        word_name  = self.qList[qModelIndex.row()].split()[0]
        QMessageBox.information(self,'搜索提示','你选择了' + word_name + '!')
        ListView.qModelIndex = qModelIndex
        ListView.Hotword_Name = word_name