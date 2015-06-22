#J V Ashrith

import wx , re , struct
from array import array
from sys import byteorder
import os
import json
import ast
from wx.lib.mixins.listctrl import ColumnSorterMixin

THRESHOLD = 500
CHUNK_SIZE = 1024
RATE = 44100



tweets_sort = ''

class SortedListCtrl(wx.ListCtrl, ColumnSorterMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
        ColumnSorterMixin.__init__(self, len(tweets_sort))
        self.itemDataMap = tweets_sort

    def GetListCtrl(self):
        return self

class Example(wx.Frame):
           
    sld1=sld2=sld3=sld4=sld5=sld6=sld7=sld8=sld9=cb1=cb2=cb3=cb4=cb5=cb6=cb7=cb8=cb9=mpbtn1=mpbtn2=mpbtn3=mpbtn4=mpbtn5=stream1=stream2=stream3=array4=array5=array1=array2=array3=recbtn=''

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
	self.select1 = 'No File Chosen'
	self.select2 = 'No File Chosen'
	self.select3 = 'No File Chosen'

        self.trend_selected = ''

        self.InitUI()

    def InitUI(self):   
	
        pnl = wx.Panel(self)
        
	font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD)
	heading = wx.StaticText(pnl, label='Twitter GUI', pos=(300, 10))
	heading.SetFont(font)

	wx.StaticLine(pnl, pos=(0, 50), size=(900,1)) #Line Under Wave Mixer Logo

	#For static boxes
        sb1 = wx.StaticBox(pnl, label='Getting Trends', pos=(15, 250), size=(230, 450))
	sb1.SetBackgroundColour((0,0,0))
#	sb2 = wx.StaticBox(pnl , label='Wave 2' , pos=(285,70) , size=(230,480))
#	sb2.SetBackgroundColour((0,0,0))
#	sb3 = wx.StaticBox(pnl , label='Getting Tweets' , pos=(555,70) , size=(230,480))
#	sb3.SetBackgroundColour((0,0,0))

	#Elements inside the box

        store_tweets = wx.Button(pnl, label="Pplr. Tweets", pos=(40,650), size=(80,-1))
        store_tweets_actual = wx.Button(pnl, label="All Tweets", pos=(140,650), size=(80,-1))

	#Buttons , text after them
        btn1 = wx.Button(pnl, label='Get Trends', pos=(30, 210), size=(100, -1))
#	self.name1 = wx.StaticText(pnl, label=self.select1,pos=(120,110))
#        btn2 = wx.Button(pnl, label='Select File', pos=(300, 100), size=(80, -1))
#	self.name2 = wx.StaticText(pnl, label=self.select2,pos=(390,110))
#	T1 = wx.StaticText(pnl, label='Modulate And Play' ,pos=(15,650))
#	T2 = wx.StaticText(pnl , label='Mix And Play' , pos=(330,650))
#	Yo = wx.Font(18 , wx.DEFAULT, wx.NORMAL, wx.BOLD)
#	T1.SetFont(Yo)
#	T2.SetFont(Yo)

	#Music Player Boxes , buttons , Recording
	global mpbtn1,mpbtn2,mpbtn3,mpbtn4,mpbtn5,recbtn
#       mpbtn1 = wx.Button(pnl, label='Play', pos=(40, 485), size=(80, -1))
#       mpbtn2 = wx.Button(pnl, label='Play', pos=(310, 485), size=(80, -1))
#	mpbtn4 = wx.Button(pnl , label='Play' , pos=(85,600) , size=(80,-1))
#	mpbtn5 = wx.Button(pnl , label='Play' , pos=(355,600) , size=(80,-1))

	#Static Boxes
#        mp1 = wx.StaticBox(pnl, label = '', pos=(30, 465), size=(200, 80))
#	mp1.SetBackgroundColour((0,0,0))
#	mp2 = wx.StaticBox(pnl , label = '' , pos=(300,465) , size=(200,80))
#	mp2.SetBackgroundColour((0,0,0))
#	mp4 = wx.StaticBox(pnl , label = '' , pos=(30,585) , size=(200 , 50))
#	mp4.SetBackgroundColour((0,0,0))
#	mp5 = wx.StaticBox(pnl , label = '' , pos=(300,585) , size=(200,50))
#	mp5.SetBackgroundColour((0,0,0))

	#Checkboxes
	global cb1,cb2,cb3,cb4,cb5,cb6,cb7,cb8,cb9

        self.list_ctrlmain = wx.ListCtrl(pnl, size=(220,150), style=wx.LC_REPORT|wx.BORDER_SUNKEN, pos = (20,50))
        self.list_ctrlmain.InsertColumn(0, 'Pick Location Of Trend', width=320)

        self.list_ctrlmain.InsertStringItem(0, 'India')
        self.list_ctrlmain.InsertStringItem(1, 'Hyderabad')
        self.list_ctrlmain.InsertStringItem(2, 'Global')

#	cb1 = wx.CheckBox(pnl, label='Time Reversal', pos=(30, 375))
#	cb2 = wx.CheckBox(pnl, label='Time Reversal', pos=(300, 375))
#	cb4 = wx.CheckBox(pnl, label='Select for Modulation', pos=(30, 410))
#	cb5 = wx.CheckBox(pnl, label='Select for Modulation', pos=(300, 410))
#	cb7 = wx.CheckBox(pnl, label='Select for Mixing', pos=(30, 445))
#	cb8 = wx.CheckBox(pnl, label='Select for Mixing', pos=(300, 445))

	#Sliders
	global sld1,sld2,sld3,sld4,sld5,sld6,sld7,sld8,sld9
#	sld1 = wx.Slider(pnl, value=10, minValue=0, maxValue=50, pos=(30, 180), size=(200, -1), style=wx.SL_HORIZONTAL)     
#	self.txt1 = wx.StaticText(pnl, label='1.0', pos=(30, 200))
#	sld2 = wx.Slider(pnl, value=10, minValue=0, maxValue=50, pos=(300, 180), size=(200, -1), style=wx.SL_HORIZONTAL)     
#	self.txt2 = wx.StaticText(pnl, label='1.0', pos=(300, 200))
#	sld4 = wx.Slider(pnl, value=0, minValue=0, maxValue=50, pos=(30, 255), size=(200, -1), style=wx.SL_HORIZONTAL)     
#	self.txt4 = wx.StaticText(pnl, label='0.0', pos=(30, 275))
#	sld5 = wx.Slider(pnl, value=0, minValue=0, maxValue=50, pos=(300, 255), size=(200, -1), style=wx.SL_HORIZONTAL)     
#	self.txt5 = wx.StaticText(pnl, label='0.0', pos=(300, 275))
#	sld7 = wx.Slider(pnl, value=10, minValue=0, maxValue=80, pos=(30, 330), size=(200, -1), style=wx.SL_HORIZONTAL)     
#	self.txt7 = wx.StaticText(pnl, label='1.0', pos=(30, 350))
#	sld8 = wx.Slider(pnl, value=10, minValue=0, maxValue=80, pos=(300, 330), size=(200, -1), style=wx.SL_HORIZONTAL)     
#	self.txt8 = wx.StaticText(pnl, label='1.0', pos=(300, 350))

	#Text for sliders
#	tsum = wx.StaticText(pnl , label='Amplitude', pos=(30, 150))
#	tsum = wx.StaticText(pnl , label='Amplitude' , pos=(300,150))
#	tsum = wx.StaticText(pnl , label='Time Shift' , pos=(30,225))
#	tsum = wx.StaticText(pnl , label='Time Shift' , pos=(300,225))
#	tsum = wx.StaticText(pnl , label='Time Scaling' , pos=(30,300))
#	tsum = wx.StaticText(pnl , label='Time Scaling' , pos=(300,300))
	
	#Funcs for selecting files  , playing files , record too
        store_tweets.Bind(wx.EVT_BUTTON, self.store_tweet)
        store_tweets_actual.Bind(wx.EVT_BUTTON, self.store_tweet_actual)

	btn1.Bind(wx.EVT_BUTTON , self.get_trends)
#	btn2.Bind(wx.EVT_BUTTON , self.load2)

#	mpbtn1.Bind(wx.EVT_BUTTON , self.play1)
#	mpbtn2.Bind(wx.EVT_BUTTON , self.play2)
#	mpbtn4.Bind(wx.EVT_BUTTON , self.play4)
#	mpbtn5.Bind(wx.EVT_BUTTON , self.play5)


	#Funcs for checkboxes
#	cb1.Bind(wx.EVT_CHECKBOX , self.check1)
#	cb2.Bind(wx.EVT_CHECKBOX , self.check2)
#	cb4.Bind(wx.EVT_CHECKBOX , self.check4)
#	cb5.Bind(wx.EVT_CHECKBOX , self.check5)
#	cb7.Bind(wx.EVT_CHECKBOX , self.check7)
#	cb8.Bind(wx.EVT_CHECKBOX , self.check8)

	#Funcs for sliders
#	sld1.Bind(wx.EVT_SCROLL , self.slide1)
#	sld2.Bind(wx.EVT_SCROLL , self.slide2)
#	sld4.Bind(wx.EVT_SCROLL , self.slide4)
#	sld5.Bind(wx.EVT_SCROLL , self.slide5)
#	sld7.Bind(wx.EVT_SCROLL , self.slide7)
#	sld8.Bind(wx.EVT_SCROLL , self.slide8)

        self.SetSize((800, 750))
        self.SetTitle('Twitter GUI')
        self.Centre()
        self.Show(True)          
	
    def store_tweet(self , e):
	global stream1,cb1,sld1,sld4,sld7,array1,tweets_sort

        choice = self.list_ctrl.GetFocusedItem()

        if choice != -1:
            trend_no = choice
            param = './final_try.sh '+str(trend_no)
#            print param
            os.system(param)

            score_file = open("scores.txt")
            score_file = score_file.readlines()

            temp_file = open("tweets_from_trends.txt")
            temp_file = temp_file.readlines()

            self.index_list1 = 0
            self.list_ctrl1 = wx.ListCtrl(self, size=(460,480), style=wx.LC_REPORT|wx.BORDER_SUNKEN, pos = (285,70))
            self.list_ctrl1.InsertColumn(0, 'ID', width=20)
            self.list_ctrl1.InsertColumn(1, 'User')
            self.list_ctrl1.InsertColumn(2, 'Screen Name')
            self.list_ctrl1.InsertColumn(3, 'Tweet (TEXT)')
            self.list_ctrl1.InsertColumn(4, 'Favorite Count')
            self.list_ctrl1.InsertColumn(5, 'Retweet Count')
            self.list_ctrl1.InsertColumn(6, 'Sentiment Score')

            for counter in range(len(temp_file)):
                temping = ast.literal_eval(temp_file[counter])

                text = temping[u'text']
                favorite = temping[u'favorite_count']
                user = temping[u'user'][u'name']
                screen_name = temping[u'user'][u'screen_name']
                score = str(score_file[counter])
                retweets = temping[u'retweet_count']

                user.encode('utf-8')
                screen_name.encode('utf-8')

                self.list_ctrl1.InsertStringItem(self.index_list1, str(counter+1))
                self.list_ctrl1.SetStringItem(self.index_list1, 1, user)
                self.list_ctrl1.SetStringItem(self.index_list1, 2, screen_name)
                self.list_ctrl1.SetStringItem(self.index_list1, 3, text)
                self.list_ctrl1.SetStringItem(self.index_list1, 4, str(retweets))
                self.list_ctrl1.SetStringItem(self.index_list1, 5, str(favorite))
                self.list_ctrl1.SetStringItem(self.index_list1, 6, score)
                self.index_list1 += 1 


    def store_tweet_actual(self , e):
	global stream1,cb1,sld1,sld4,sld7,array1,tweets_sort

        choice = self.list_ctrl.GetFocusedItem()

        if choice != -1:
            trend_no = choice
            param = 'python count-old-words.py '+str(trend_no)
#            print param
            os.system(param)

            param = 'python complete_analysis.py'
            os.system(param)
#            score_file = open("scores.txt")
#            score_file = score_file.readlines()

#            temp_file = open("alltweets_from_trends.txt")
#            temp_file = temp_file.readlines()

    def get_trends(self , e):
	global stream1,cb1,sld1,sld4,sld7,array1


        choice = self.list_ctrlmain.GetFocusedItem()

        if choice == -1:
            return

        os.system('python get_trends.py ' + str(choice))
        temp_file = open("trends.txt")

        temp_file = temp_file.readlines()

        self.index_list = 0
        self.list_ctrl = wx.ListCtrl(self, size=(220,350), style=wx.LC_REPORT|wx.BORDER_SUNKEN, pos = (20,280))
        self.list_ctrl.InsertColumn(0, 'Trends', width=220)

        for counter in range(len(temp_file)):
            self.list_ctrl.InsertStringItem(self.index_list, temp_file[counter])
            self.index_list += 1

    def load3(self , e):
	global stream3

	openFileDialog = wx.FileDialog(self, "Open", "", "","Wav Files (*.wav)|*.wav",wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
	openFileDialog.ShowModal()
	self.select3=openFileDialog.GetPath()
	a=re.sub(r'.*\/','',self.select3)
	self.name3.SetLabel(str(a))

	stream3 = wave.open(self.select3,"rb")
	sample_rate = stream3.getframerate()
	num_frames = stream3.getnframes()
	t=num_frames/sample_rate
	sld6.SetMax(10.0)
	sld6.SetMin(-10.0)
	sld9.SetMin(1)
	stream3.close()

	openFileDialog.Destroy()

    def check1(self, e):
	sender = e.GetEventObject()
	isChecked = sender.GetValue()

    def slide1(self, e):	        
	obj = e.GetEventObject()
	val = obj.GetValue()
	val = val*1.0/10
	self.txt1.SetLabel(str(val)) 

    def OnClose(self, e):
	self.Close(True)
        
def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    

if __name__ == "__main__":
	main()
