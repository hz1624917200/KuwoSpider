from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout
from PyQt5.QtCore import QStringListModel,pyqtSignal
from PyQt5.QtGui import QIcon
import listview
import Network
import os

class PageControl(QWidget): #控制列表翻页的类
    control_signal = pyqtSignal(list)
    
    def __init__(self,path, name, flag):
        super().__init__()
        self.listview = listview.ListView(path,name,flag)
        ico_path = os.path.join(os.path.dirname(__file__), '1.ico')
        self.setWindowIcon(QIcon(ico_path)) 
        self.init_ui()

    def init_ui(self):
        self.resize(1200,1000)
        self.setWindowTitle("搜索结果")
        self.listview.layout = QVBoxLayout()
        listView = QListView()
        slm = QStringListModel()

        if self.listview.name is None:
            self.listview.get_list()
            self.qList = self.listview.qList
            listView.clicked.connect(self.listview.message)    
        elif self.listview.flag == 'song' and self.listview.name != 'hotword':
            self.listview.get_list()
            self.qList = self.listview.qList
            listView.clicked.connect(self.listview.download)
        elif self.listview.flag == 'rank':
            self.listview.get_ranksong(listview.ListView.qModelIndex)
            self.qList = [str(ch) for ch in listview.ListView.Ranksong_List[0]]
            listView.clicked.connect(self.listview.download)
        else:
            self.listview.get_list()
            self.qList = self.listview.qList
            listView.clicked.connect(self.listview.hotword_song)
        
        slm.setStringList(self.qList)
        listView.setModel(slm)
        self.listview.layout.addWidget(listView)
        self.setLayout(self.listview.layout)

    def setPageController(self,page,curpage = '1'):
        #自定义页码控制器
        control_layout = QHBoxLayout()
        homePage = QPushButton("首页")
        prePage = QPushButton("<上一页")
        self.curPage = QLabel(curpage)
        nextPage = QPushButton("下一页>")
        finalPage = QPushButton("尾页")
        self.totalPage = QLabel("共" + str(page) + "页")
        skipLable_0 = QLabel("跳到")
        self.skipPage = QLineEdit()
        skipLabel_1 = QLabel("页")
        confirmSkip = QPushButton("确定")
        homePage.clicked.connect(self.__home_page)
        prePage.clicked.connect(self.__pre_page)
        nextPage.clicked.connect(self.__next_page)
        finalPage.clicked.connect(self.__final_page)
        confirmSkip.clicked.connect(self.__confirm_skip)
        control_layout.addStretch(1)
        control_layout.addWidget(homePage)
        control_layout.addWidget(prePage)
        control_layout.addWidget(self.curPage)
        control_layout.addWidget(nextPage)
        control_layout.addWidget(finalPage)
        control_layout.addWidget(self.totalPage)
        control_layout.addWidget(skipLable_0)
        control_layout.addWidget(self.skipPage)
        control_layout.addWidget(skipLabel_1)
        control_layout.addWidget(confirmSkip)
        control_layout.addStretch(1)
        self.listview.layout.addLayout(control_layout)

    def __home_page(self):
        #点击首页信号
        self.control_signal.emit(["home", self.curPage.text()])

    def __pre_page(self):
        #点击上一页信号
        self.control_signal.emit(["pre", self.curPage.text()])
        

    def __next_page(self):
        #点击下一页信号
        self.control_signal.emit(["next", self.curPage.text()])

    def __final_page(self):
        #尾页点击信号
        self.control_signal.emit(["final", self.curPage.text()])    
        
    def __confirm_skip(self):
        #跳转页码确定
        self.control_signal.emit(["confirm", self.skipPage.text()])

    def showTotalPage(self):
        #返回当前总页数
        return int(self.totalPage.text()[1:-1])


class PageChange(QMainWindow):
    step = 0
    flag = 1
    def __init__(self,path,name = None,flag = 'song'):
        super().__init__()
        self.path = path
        self.name = name
        self.flag = flag
        self.listview = listview.ListView(path,name,flag)
        ico_path = os.path.join(os.path.dirname(__file__), '1.ico')
        self.setWindowIcon(QIcon(ico_path)) 
        self.init_ui()
    
    def init_ui(self):
        self.resize(1200, 1000)
        self.setWindowTitle("搜索结果")
        self.table_widget = PageControl(self.path,self.name,self.flag)

        if self.name is None:
            self.table_widget.setPageController(1)
        elif self.flag == 'song':
            self.table_widget.setPageController(Network.search(self.name)[1] // 30 + 1)  # 表格设置页码控制
        else:
            self.table_widget.setPageController(listview.ListView.Ranksong_List[1] // 30 + 1)
        
        self.table_widget.control_signal.connect(self.page_controller)
        self.setCentralWidget(self.table_widget)
    
    def page_controller(self, signal):
        total_page = self.table_widget.showTotalPage()
        if "home" == signal[0]:
            self.table_widget.curPage.setText("1")
            PageChange.flag = 1
            
        elif "pre" == signal[0]:
            if 1 == int(signal[1]):
                QMessageBox.information(self, "提示", "已经是第一页了", QMessageBox.Yes)
                return
            self.table_widget.curPage.setText(str(int(signal[1]) - 1))
            PageChange.flag -= 1
            
        elif "next" == signal[0]:
            if total_page == int(signal[1]):
                QMessageBox.information(self, "提示", "已经是最后一页了", QMessageBox.Yes)
                return
            self.table_widget.curPage.setText(str(int(signal[1]) + 1))
            PageChange.flag += 1
            
        elif "final" == signal[0]:
            self.table_widget.curPage.setText(str(total_page))
            if self.flag == 'song':
                PageChange.flag = Network.search(self.name)[1] // 30 + 1
            else:
                PageChange.flag = listview.ListView.Ranksong_List[1] // 30 + 1
            
        elif "confirm" == signal[0]:
            if signal[1] == '':
                QMessageBox.information(self,'提示','请输入跳转页码')
                return
            if total_page < int(signal[1]) or int(signal[1]) < 0:
                QMessageBox.information(self, "提示", "跳转页码超出范围", QMessageBox.Yes)
                return
            self.table_widget.curPage.setText(signal[1])
            PageChange.flag = int(signal[1])
            

        self.changeTableContent()
    
    def changeTableContent(self):
        #根据当前页改变列表内容
        self.table_widget = PageControl(self.path,self.name,self.flag)  # 实例化表格

        if self.flag == 'song':
            self.table_widget.setPageController(Network.search(self.name)[1] // 30 + 1,str(PageChange.flag))
        else:
            self.table_widget.setPageController(listview.ListView.Ranksong_List[1] // 30 + 1,str(PageChange.flag))

        self.table_widget.control_signal.connect(self.page_controller)
        self.setCentralWidget(self.table_widget)