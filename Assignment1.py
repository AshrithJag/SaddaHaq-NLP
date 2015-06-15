#J V Ashrith
#(201202126)

#On recording an output file named demo.wav gets created.

import wx , re , struct , wave , pyaudio 
from array import array
from sys import byteorder

THRESHOLD = 500
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 44100

class Example(wx.Frame):
           
    sld1=sld2=sld3=sld4=sld5=sld6=sld7=sld8=sld9=cb1=cb2=cb3=cb4=cb5=cb6=cb7=cb8=cb9=mpbtn1=mpbtn2=mpbtn3=mpbtn4=mpbtn5=stream1=stream2=stream3=array4=array5=array1=array2=array3=recbtn=''

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
	self.select1 = 'No File Chosen'
	self.select2 = 'No File Chosen'
	self.select3 = 'No File Chosen'

        self.InitUI()

    def record_to_file(self , e):
	sample_width, data = self.record()
	data = struct.pack('<' + ('h'*len(data)), *data)

	wf = wave.open('demo.wav', 'wb')
	wf.setnchannels(1)
	wf.setsampwidth(sample_width)
	wf.setframerate(RATE)
	wf.writeframes(data)
	print 'Write Finished on File "demo.wav"'
	wf.close()

    def record(self):
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT, channels=1, rate=RATE,
		input=True, output=True,
		frames_per_buffer=CHUNK_SIZE)

	num_silent = 0
	snd_started = False

	r = array('h')

	while 1:
		snd_data = array('h', stream.read(CHUNK_SIZE))
		if byteorder == 'big':
			snd_data.byteswap()
		r.extend(snd_data)

		silent = self.is_silent(snd_data)

		if silent and snd_started:
			num_silent += 1
		elif not silent and not snd_started:
			snd_started = True

		if snd_started and num_silent > 30:
			break

	sample_width = p.get_sample_size(FORMAT)
	stream.stop_stream()
	stream.close()
	p.terminate()

	r = self.normalize(r)
	r = self.trim(r)
	r = self.add_silence(r, 0.5)
	return sample_width, r

    def is_silent(self,snd_data):
	"Returns 'True' if below the 'silent' threshold"
	return max(snd_data) < THRESHOLD

    def normalize(self,snd_data):
	MAXIMUM = 16384
	times = float(MAXIMUM)/max(abs(i) for i in snd_data)
	r = array('h')
	for i in snd_data:
		r.append(int(i*times))
	return r

    def trim(self,snd_data):
	def _trim(snd_data):
		snd_started = False
		r = array('h')

		for i in snd_data:
			if not snd_started and abs(i)>THRESHOLD:
				snd_started = True
				r.append(i)

			elif snd_started:
				r.append(i)
		return r

	# Trim to the left
	snd_data = _trim(snd_data)

	# Trim to the right
	snd_data.reverse()
	snd_data = _trim(snd_data)
	snd_data.reverse()
	return snd_data

    def add_silence(self,snd_data, seconds):
	r = array('h', [0 for i in xrange(int(seconds*RATE))])
	r.extend(snd_data)
	r.extend([0 for i in xrange(int(seconds*RATE))])
	return r

    def wavemorph(self , ampfactor , shf ,scale , rev , inp , number):
	global array1 , array2 , array3
#	print shf
	inp = wave.open(inp,'rb')
	if(number == 1):
		array1 = []
	elif(number == 2):
		array2 = []
	elif(number  == 3):
		array3 = []
	timtemp = shf
	if(shf < 0):
		shf = -1*shf
	shift = inp.getframerate()*shf
	shift = int(shift)
	y = inp.getnframes() - shift
	print y , shift
	if(timtemp > 0 and shift < y):
		for i in range(0 , shift):
			frame = inp.readframes(1)
	elif(timtemp < 0 and shift < y):
		frame = inp.readframes(1)
		for i in range(0 , shift):
			temp = 0
			if(len(frame) == 1):
				frame = struct.pack("<B",temp)
			if(len(frame) == 2):
				frame = struct.pack("<h",temp)
			elif(len(frame) == 4):
				frame = struct.pack("<i",temp)
			if(number == 1):
				array1.append(frame)
			if(number == 2):
				array2.append(frame)
			if(number == 3):
				array3.append(frame)
        for i in range(0 , y):
		frame = inp.readframes(1)
		if(len(frame) == 1):
			data = struct.unpack("<B", frame)
			temp = int(data[0]*ampfactor)
			if(temp > 255):
				temp = 255
			elif (temp < 0):
				temp = 0
			frame = struct.pack("<B", temp)
		if(len(frame) == 2):
			data = struct.unpack("<h", frame)
			temp = int(data[0]*ampfactor)
			if(temp > 32767):
				temp = 32767
			elif (temp < -32767):
				temp = -32767
			frame = struct.pack("<h", temp)
	    	elif(len(frame) == 4):
			data = struct.unpack("<i", frame)
			temp = int(data[0]*ampfactor)
			if(temp > 2147483647):
				temp = 2147483647
			elif (temp < -2147483647):
				temp = -2147483647
			frame = struct.pack("<i", temp)
		if(number == 1):
			array1.append(frame)
		elif(number == 2):
			array2.append(frame)
		elif(number == 3):
			array3.append(frame)
	if(timtemp > 0 and shift < y):
		    for i in range(0 , shift):
			    frame = inp.readframes(1)
			    temp = 0
			    if(len(frame) == 1):
				    frame = struct.pack("<B",temp)
			    elif(len(frame) == 2):
				    frame = struct.pack("<h",temp)
			    elif(len(frame) == 4):
				    frame = struct.pack("<i",temp)
			    if(number == 1):
			            array1.append(frame)
			    elif(number == 2):
			            array2.append(frame)
			    elif(number == 3): 
				    array3.append(frame)

	if rev:
		if(number == 1):
			array1.reverse()
		elif(number == 2):
			array2.reverse()
		elif(number == 3): 
			array3.reverse()

	inp.close()

    def mix(self , a1 , a2 , a3):

	global array4

	array4 = []

	for i in range(0 , len(a3)):
		if(len(a1) > i):
			frame1 = a1[i]
			frame2 = a2[i]
			frame3 = a3[i]	
			data1 = struct.unpack("<h" , frame1)
			data2 = struct.unpack("<h" , frame2)
			data3 = struct.unpack("<h" , frame3)
			print data1 , data2 , data3
			if(len(frame1) == 2 and len(frame2) == 2 and len(frame3) == 2):
				data1 = struct.unpack("<h" , frame1)
				data2 = struct.unpack("<h" , frame2)
				data3 = struct.unpack("<h" , frame3)
				temp = int(data1[0])+int(data2[0])+int(data3[0])
				if(temp > 32767):
					temp = 32767
				elif (temp < -32767):
					temp = -32767
				frame = struct.pack("<h", temp)
	    		elif(len(frame1) == 1 and len(frame2) == 1 and len(frame3)== 1):
				data1 = struct.unpack("<B", frame1)
				data2 = struct.unpack("<B" , frame2)
				data3 = struct.unpack("<B" , frame3)
				temp = int(data1[0])+int(data2[0])+int(data3[0])
				if(temp > 255):
					temp = 255
				elif (temp < 0):
					temp = 0
				frame = struct.pack("<B", temp)
	    		elif(len(frame1) == 4 and len(frame2) == 4 and len(frame3)==4):
				data1 = struct.unpack("<i", frame1)
				data2 = struct.unpack("<i" , frame2)
				data3 = struct.unpack("<i" , frame3)
				temp = int(data1[0])+int(data2[0])+int(data3[0])
				if(temp > 2147483647):
					temp = 2147483647
				elif (temp < -2147483647):
					temp = -2147483647
				frame = struct.pack("<i", temp)
		elif(len(a2) > i):
			frame2 = a2[i]
			frame3 = a3[i]
			if(len(frame2) == 2 and len(frame3) == 2):
				data2 = struct.unpack("<h" , frame2)
				data3 = struct.unpack("<h" , frame3)
				temp = int(data2[0])+int(data3[0])
				if(temp > 32767):
					temp = 32767
				elif (temp < -32767):
					temp = -32767
				frame = struct.pack("<h", temp)
	    		elif(len(frame2) == 1 and len(frame3)== 1):
				data1 = struct.unpack("<B", frame1)
				data2 = struct.unpack("<B" , frame2)
				temp = int(data2[0])+int(data3[0])
				if(temp > 255):
					temp = 255
				elif (temp < 0):
					temp = 0
				frame = struct.pack("<B", temp)
	    		elif(len(frame2) == 4 and len(frame3)==4):
				data1 = struct.unpack("<i", frame1)
				data2 = struct.unpack("<i" , frame2)
				temp = int(data2[0])+int(data3[0])
				if(temp > 2147483647):
					temp = 2147483647
				elif (temp < -2147483647):
					temp = -2147483647
				frame = struct.pack("<i", temp)
		elif(len(a3) > i):
			frame3 = a3[i]
			if(len(frame3) == 2):
				data3 = struct.unpack("<h" , frame3)
				temp = int(data3[0])
				if(temp > 32767):
					temp = 32767
				elif (temp < -32767):
					temp = -32767
				frame = struct.pack("<h", temp)
	    		elif(len(frame3)== 1):
				data3 = struct.unpack("<B" , frame3)
				temp = int(data3[0])
				if(temp > 255):
					temp = 255
				elif (temp < 0):
					temp = 0
				frame = struct.pack("<B", temp)
	    		elif(len(frame3)==4):
				data3 = struct.unpack("<i" , frame3)
				temp = int(data3[0])
				if(temp > 2147483647):
					temp = 2147483647
				elif (temp < -2147483647):
					temp = -2147483647
				frame = struct.pack("<i", temp)
		array4.append(frame)

    def modulate(self , a1 , a2 , a3):

	global array4

	array4 = []

	for i in range(0 , len(a3)):
		if(len(a1) > i):
			frame1 = a1[i]
			frame2 = a2[i]
			frame3 = a3[i]
			if(len(frame1) == 2 and len(frame2) == 2 and len(frame3) == 2):
				data1 = struct.unpack("<h" , frame1)
				data2 = struct.unpack("<h" , frame2)
				data3 = struct.unpack("<h" , frame3)
				temp = int(data1[0])*int(data2[0])*int(data3[0])
				if(temp > 32767):
					temp = 32767
				elif (temp < -32767):
					temp = -32767
				frame = struct.pack("<h", temp)
	    		elif(len(frame1) == 1 and len(frame2) == 1 and len(frame3)== 1):
				data1 = struct.unpack("<B", frame1)
				data2 = struct.unpack("<B" , frame2)
				data3 = struct.unpack("<B" , frame3)
				temp = int(data1[0])*int(data2[0])*int(data3[0])
				if(temp > 255):
					temp = 255
				elif (temp < 0):
					temp = 0
				frame = struct.pack("<B", temp)
	    		elif(len(frame1) == 4 and len(frame2) == 4 and len(frame3)==4):
				data1 = struct.unpack("<i", frame1)
				data2 = struct.unpack("<i" , frame2)
				data3 = struct.unpack("<i" , frame3)
				temp = int(data1[0])*int(data2[0])*int(data3[0])
				if(temp > 2147483647):
					temp = 2147483647
				elif (temp < -2147483647):
					temp = -2147483647
				frame = struct.pack("<i", temp)
		elif(len(a2) > i):
			frame2 = a2[i]
			frame3 = a3[i]
			if(len(frame2) == 2 and len(frame3) == 2):
				data2 = struct.unpack("<h" , frame2)
				data3 = struct.unpack("<h" , frame3)
				temp = int(data2[0])*int(data3[0])
				if(temp > 32767):
					temp = 32767
				elif (temp < -32767):
					temp = -32767
				frame = struct.pack("<h", temp)
	    		elif(len(frame2) == 1 and len(frame3)== 1):
				data1 = struct.unpack("<B", frame1)
				data2 = struct.unpack("<B" , frame2)
				temp = int(data2[0])*int(data3[0])
				if(temp > 255):
					temp = 255
				elif (temp < 0):
					temp = 0
				frame = struct.pack("<B", temp)
	    		elif(len(frame2) == 4 and len(frame3)==4):
				data1 = struct.unpack("<i", frame1)
				data2 = struct.unpack("<i" , frame2)
				temp = int(data2[0])*int(data3[0])
				if(temp > 2147483647):
					temp = 2147483647
				elif (temp < -2147483647):
					temp = -2147483647
				frame = struct.pack("<i", temp)
		elif(len(a3) > i):
			frame3 = a3[i]
			if(len(frame3) == 2):
				data3 = struct.unpack("<h" , frame3)
				temp = int(data3[0])
				if(temp > 32767):
					temp = 32767
				elif (temp < -32767):
					temp = -32767
				frame = struct.pack("<h", temp)
	    		elif(len(frame3)== 1):
				data3 = struct.unpack("<B" , frame3)
				temp = int(data3[0])
				if(temp > 255):
					temp = 255
				elif (temp < 0):
					temp = 0
				frame = struct.pack("<B", temp)
	    		elif(len(frame3)==4):
				data3 = struct.unpack("<i" , frame3)
				temp = int(data3[0])
				if(temp > 2147483647):
					temp = 2147483647
				elif (temp < -2147483647):
					temp = -2147483647
				frame = struct.pack("<i", temp)
		array4.append(frame)


    def InitUI(self):   
	
        pnl = wx.Panel(self)
        
	font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD)
	heading = wx.StaticText(pnl, label='Wave Mixer', pos=(300, 10))
	heading.SetFont(font)

	wx.StaticLine(pnl, pos=(0, 50), size=(900,1)) #Line Under Wave Mixer Logo

	#For static boxes
        sb1 = wx.StaticBox(pnl, label='Wave 1', pos=(15, 70), size=(230, 480))
	sb1.SetBackgroundColour((0,0,0))
	sb2 = wx.StaticBox(pnl , label='Wave 2' , pos=(285,70) , size=(230,480))
	sb2.SetBackgroundColour((0,0,0))
	sb3 = wx.StaticBox(pnl , label='Wave 3' , pos=(555,70) , size=(230,480))
	sb3.SetBackgroundColour((0,0,0))

	#Elements inside the box

	#Buttons , text after them
        btn1 = wx.Button(pnl, label='Select File', pos=(30, 100), size=(80, -1))
	self.name1 = wx.StaticText(pnl, label=self.select1,pos=(120,110))
        btn2 = wx.Button(pnl, label='Select File', pos=(300, 100), size=(80, -1))
	self.name2 = wx.StaticText(pnl, label=self.select2,pos=(390,110))
        btn3 = wx.Button(pnl, label='Select File', pos=(570, 100), size=(80, -1))
	self.name3 = wx.StaticText(pnl, label=self.select3,pos=(660,110))
	T1 = wx.StaticText(pnl, label='Modulate And Play' ,pos=(15,650))
	T2 = wx.StaticText(pnl , label='Mix And Play' , pos=(330,650))
	T3 = wx.StaticText(pnl , label='Record' , pos=(620,650))
	Yo = wx.Font(18 , wx.DEFAULT, wx.NORMAL, wx.BOLD)
	T1.SetFont(Yo)
	T2.SetFont(Yo)
	T3.SetFont(Yo)

	#Music Player Boxes , buttons , Recording
	global mpbtn1,mpbtn2,mpbtn3,mpbtn4,mpbtn5,recbtn
        mpbtn1 = wx.Button(pnl, label='Play', pos=(40, 485), size=(80, -1))
        mpbtn2 = wx.Button(pnl, label='Play', pos=(310, 485), size=(80, -1))
        mpbtn3 = wx.Button(pnl, label='Play', pos=(580, 485), size=(80, -1))
	mpbtn4 = wx.Button(pnl , label='Play' , pos=(85,600) , size=(80,-1))
	mpbtn5 = wx.Button(pnl , label='Play' , pos=(355,600) , size=(80,-1))
	recbtn = wx.Button(pnl , label ='Record', pos = (625 , 600) , size=(80,-1))

	#Static Boxes
        mp1 = wx.StaticBox(pnl, label = '', pos=(30, 465), size=(200, 80))
	mp1.SetBackgroundColour((0,0,0))
	mp2 = wx.StaticBox(pnl , label = '' , pos=(300,465) , size=(200,80))
	mp2.SetBackgroundColour((0,0,0))
	mp3 = wx.StaticBox(pnl , label = '' , pos=(570,465) , size=(200,80))
	mp3.SetBackgroundColour((0,0,0))
	mp4 = wx.StaticBox(pnl , label = '' , pos=(30,585) , size=(200 , 50))
	mp4.SetBackgroundColour((0,0,0))
	mp5 = wx.StaticBox(pnl , label = '' , pos=(300,585) , size=(200,50))
	mp5.SetBackgroundColour((0,0,0))
	mp6 = wx.StaticBox(pnl , label = '' , pos=(570,585) , size=(200,50))
	mp6.SetBackgroundColour((0,0,0))

	#Checkboxes
	global cb1,cb2,cb3,cb4,cb5,cb6,cb7,cb8,cb9
	cb1 = wx.CheckBox(pnl, label='Time Reversal', pos=(30, 375))
	cb2 = wx.CheckBox(pnl, label='Time Reversal', pos=(300, 375))
	cb3 = wx.CheckBox(pnl, label='Time Reversal', pos=(570, 375))
	cb4 = wx.CheckBox(pnl, label='Select for Modulation', pos=(30, 410))
	cb5 = wx.CheckBox(pnl, label='Select for Modulation', pos=(300, 410))
	cb6 = wx.CheckBox(pnl, label='Select for Modulation', pos=(570, 410))
	cb7 = wx.CheckBox(pnl, label='Select for Mixing', pos=(30, 445))
	cb8 = wx.CheckBox(pnl, label='Select for Mixing', pos=(300, 445))
	cb9 = wx.CheckBox(pnl, label='Select for Mixing', pos=(570, 445))

	#Sliders
	global sld1,sld2,sld3,sld4,sld5,sld6,sld7,sld8,sld9
	sld1 = wx.Slider(pnl, value=10, minValue=0, maxValue=50, pos=(30, 180), size=(200, -1), style=wx.SL_HORIZONTAL)     
	self.txt1 = wx.StaticText(pnl, label='1.0', pos=(30, 200))
	sld2 = wx.Slider(pnl, value=10, minValue=0, maxValue=50, pos=(300, 180), size=(200, -1), style=wx.SL_HORIZONTAL)     
	self.txt2 = wx.StaticText(pnl, label='1.0', pos=(300, 200))
	sld3 = wx.Slider(pnl, value=10, minValue=0, maxValue=50, pos=(570, 180), size=(200, -1), style=wx.SL_HORIZONTAL)     
	self.txt3 = wx.StaticText(pnl, label='0.0', pos=(570, 200))
	sld4 = wx.Slider(pnl, value=0, minValue=0, maxValue=50, pos=(30, 255), size=(200, -1), style=wx.SL_HORIZONTAL)     
	self.txt4 = wx.StaticText(pnl, label='0.0', pos=(30, 275))
	sld5 = wx.Slider(pnl, value=0, minValue=0, maxValue=50, pos=(300, 255), size=(200, -1), style=wx.SL_HORIZONTAL)     
	self.txt5 = wx.StaticText(pnl, label='0.0', pos=(300, 275))
	sld6 = wx.Slider(pnl, value=0, minValue=0, maxValue=50, pos=(570, 255), size=(200, -1), style=wx.SL_HORIZONTAL)     
	self.txt6 = wx.StaticText(pnl, label='0.0', pos=(570, 275))
	sld7 = wx.Slider(pnl, value=10, minValue=0, maxValue=80, pos=(30, 330), size=(200, -1), style=wx.SL_HORIZONTAL)     
	self.txt7 = wx.StaticText(pnl, label='1.0', pos=(30, 350))
	sld8 = wx.Slider(pnl, value=10, minValue=0, maxValue=80, pos=(300, 330), size=(200, -1), style=wx.SL_HORIZONTAL)     
	self.txt8 = wx.StaticText(pnl, label='1.0', pos=(300, 350))
	sld9 = wx.Slider(pnl, value=10, minValue=0, maxValue=80, pos=(570, 330), size=(200, -1), style=wx.SL_HORIZONTAL)     
	self.txt9 = wx.StaticText(pnl, label='1.0', pos=(570, 350))

	#Text for sliders
	tsum = wx.StaticText(pnl , label='Amplitude', pos=(30, 150))
	tsum = wx.StaticText(pnl , label='Amplitude' , pos=(300,150))
	tsum = wx.StaticText(pnl , label='Amplitude' , pos=(570,150))
	tsum = wx.StaticText(pnl , label='Amplitude' , pos=(300,150))
	tsum = wx.StaticText(pnl , label='Time Shift' , pos=(30,225))
	tsum = wx.StaticText(pnl , label='Time Shift' , pos=(300,225))
	tsum = wx.StaticText(pnl , label='Time Shift' , pos=(570,225))
	tsum = wx.StaticText(pnl , label='Time Scaling' , pos=(30,300))
	tsum = wx.StaticText(pnl , label='Time Scaling' , pos=(300,300))
	tsum = wx.StaticText(pnl , label='Time Scaling' , pos=(570,300))
	
	#Funcs for selecting files  , playing files , record too
	btn1.Bind(wx.EVT_BUTTON , self.load1)
	btn2.Bind(wx.EVT_BUTTON , self.load2)
	btn3.Bind(wx.EVT_BUTTON , self.load3)

	mpbtn1.Bind(wx.EVT_BUTTON , self.play1)
	mpbtn2.Bind(wx.EVT_BUTTON , self.play2)
	mpbtn3.Bind(wx.EVT_BUTTON , self.play3)
	mpbtn4.Bind(wx.EVT_BUTTON , self.play4)
	mpbtn5.Bind(wx.EVT_BUTTON , self.play5)

	recbtn.Bind(wx.EVT_BUTTON , self.record_to_file)

	#Funcs for checkboxes
	cb1.Bind(wx.EVT_CHECKBOX , self.check1)
	cb2.Bind(wx.EVT_CHECKBOX , self.check2)
	cb3.Bind(wx.EVT_CHECKBOX , self.check3)
	cb4.Bind(wx.EVT_CHECKBOX , self.check4)
	cb5.Bind(wx.EVT_CHECKBOX , self.check5)
	cb6.Bind(wx.EVT_CHECKBOX , self.check6)
	cb7.Bind(wx.EVT_CHECKBOX , self.check7)
	cb8.Bind(wx.EVT_CHECKBOX , self.check8)
	cb9.Bind(wx.EVT_CHECKBOX , self.check9)

	#Funcs for sliders
	sld1.Bind(wx.EVT_SCROLL , self.slide1)
	sld2.Bind(wx.EVT_SCROLL , self.slide2)
	sld3.Bind(wx.EVT_SCROLL , self.slide3)
	sld4.Bind(wx.EVT_SCROLL , self.slide4)
	sld5.Bind(wx.EVT_SCROLL , self.slide5)
	sld6.Bind(wx.EVT_SCROLL , self.slide6)
	sld7.Bind(wx.EVT_SCROLL , self.slide7)
	sld8.Bind(wx.EVT_SCROLL , self.slide8)
	sld9.Bind(wx.EVT_SCROLL , self.slide9)

        self.SetSize((800, 750))
        self.SetTitle('Wave Mixer')
        self.Centre()
        self.Show(True)          
	

    def play1(self , e):
	global stream1,cb1,sld1,sld4,sld7,array1
	#define stream chunk   
	chunk = 1024  

	#instantiate PyAudio  
	p = pyaudio.PyAudio() 

	tmp1 = cb1.IsChecked()
        tmp2 = float(sld1.GetValue())/10
        tmp3 = float(sld4.GetValue())/10
        tmp4 = float(sld7.GetValue())/10

	self.wavemorph(tmp2 , tmp3 , tmp4 , tmp1 , self.select1 , 1)
	stream1 = wave.open(self.select1,"rb")
	stream = p.open(format = p.get_format_from_width(stream1.getsampwidth()),  
		channels = stream1.getnchannels(),  
		rate = int(stream1.getframerate()*tmp4),  
		output = True) 


	#read data  
#	data = stream3.readframes(chunk) 

	j=0
	framecount = stream1.getnframes()
	#play stream  
	while(j<framecount):
		str1 = ''.join(array1[j:j+1024])
		stream.write(str1)
		j=j+1024
#	stream1 = wave.open(self.select1,"rb")

	#stop stream  
	stream.stop_stream()  
	stream.close()  
	#close PyAudio  
	p.terminate()
	stream1.close()

    def play2(self , e):
	global stream2,cb2,sld2,sld5,sld8,array2
	#define stream chunk   
	chunk = 1024  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  

	tmp1 = cb2.IsChecked()
        tmp2 = float(sld2.GetValue())/10
        tmp3 = float(sld5.GetValue())/10
        tmp4 = float(sld8.GetValue())/10

	self.wavemorph(tmp2 , tmp3 , tmp4 , tmp1 , self.select2 , 2)
	stream2 = wave.open(self.select2,"rb")
	stream = p.open(format = p.get_format_from_width(stream2.getsampwidth()),  
		channels = stream2.getnchannels(),  
		rate = int(stream2.getframerate()*tmp4),  
		output = True)  
	#read data  
#	data = stream3.readframes(chunk) 
	j=0
	framecount = stream2.getnframes()
	#play stream  
	while(j<framecount):
		str1 = ''.join(array2[j:j+1024])
		stream.write(str1)
		j=j+1024

	#stop stream  
	stream.stop_stream()  
	stream.close()  

	#close PyAudio  
	p.terminate()
	stream2.close()

    def play3(self , e):
	global stream3,cb3,sld3,sld6,sld9,array3
	#define stream chunk   
	chunk = 1024  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	tmp1 = cb3.IsChecked()
        tmp2 = float(sld3.GetValue())/10
        tmp3 = float(sld6.GetValue())/10
        tmp4 = float(sld9.GetValue())/10

	self.wavemorph(tmp2 , tmp3 , tmp4 , tmp1 , self.select3 , 3)
	stream3 = wave.open(self.select3,"rb")
	stream = p.open(format = p.get_format_from_width(stream3.getsampwidth()),  
		channels = stream3.getnchannels(),  
		rate = int(stream3.getframerate()*tmp4),  
		output = True)  
	#read data  
#	data = stream3.readframes(chunk) 
	j=0
	framecount = stream3.getnframes()
	#play stream  
	while(j<framecount):
		str1 = ''.join(array3[j:j+1024])
		stream.write(str1)
		j=j+1024
#	while data != '':  
#		stream.write(data)  
#		data = stream3.readframes(chunk)  

	#stop stream  
	stream.stop_stream()  
	stream.close()  

	#close PyAudio  
	p.terminate()
	stream3.close()

    def play4(self , e):
	global stream1,stream2,stream3,cb5,cb6,cb7,sld1,sld2,sld3,sld4,sld5,sld6,sld7,sld8,sld9,array1,array2,array3,array4
	#define stream chunk   
	chunk = 1024  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	streamx = ''

        tmp2 = float(sld7.GetValue())/10
        tmp3 = float(sld8.GetValue())/10
        tmp4 = float(sld9.GetValue())/10
	
	p1 = cb5.IsChecked()
	p2 = cb6.IsChecked()
	p3 = cb7.IsChecked()

	t1 = t2 = t3 = 0
	aa1 = aa2 = aa3 = []
	if(self.select1 != 'No File Chosen'):
		tmp1 = cb1.IsChecked()
        	tmp2 = float(sld1.GetValue())/10
      	        tmp3 = float(sld4.GetValue())/10
       	 	tmp4 = float(sld7.GetValue())/10
		self.wavemorph(tmp2 , tmp3 , tmp4 , tmp1 , self.select1 , 1)
		stream1 = wave.open(self.select1 , "rb")
		aa1 = []
		j = int(tmp4 * stream1.getnframes())
		for i in range(0 , j):
			aa1.append(array1[int(i/tmp4)])
		t1 = len(aa1)
		if(cb4.IsChecked() is False):
			t1 = 0
			aa1 = []
		if(cb5.IsChecked() is False):
			t2 = 0
			aa2 = []
		if(cb6.IsChecked() is False):
			t3 = 0
			aa3 = []
		stream1.close()

	if(self.select2 != 'No File Chosen'):
		tmp1 = cb2.IsChecked()
        	tmp2 = float(sld2.GetValue())/10
      	        tmp3 = float(sld5.GetValue())/10
       	 	tmp4 = float(sld8.GetValue())/10
		self.wavemorph(tmp2 , tmp3 , tmp4 , tmp1 , self.select2 , 2)
		stream2 = wave.open(self.select2 , "rb")
		aa2 = []
		j = int(tmp4 * stream2.getnframes())
		for i in range(0 , j):
			aa2.append(array2[int(i/tmp4)])
		t2 = len(aa2)
		if(cb4.IsChecked() is False):
			aa1 = []
			t1 = 0
		if(cb5.IsChecked() is False):
			aa2 = []
			t2 = 0
		if(cb6.IsChecked() is False):
			aa3 = []
			t3 = 0
		stream2.close()

	if(self.select3 != 'No File Chosen'):
		tmp1 = cb3.IsChecked()
        	tmp2 = float(sld3.GetValue())/10
      	        tmp3 = float(sld6.GetValue())/10
       	 	tmp4 = float(sld9.GetValue())/10
		self.wavemorph(tmp2 , tmp3 , tmp4 , tmp1 , self.select3 , 3)
		stream3 = wave.open(self.select3 , "rb")
		aa3 = []
		j = int(tmp4 * stream3.getnframes())
		for i in range(0 , j):
			aa3.append(array3[int(i/tmp4)])
		t3 = len(aa3)
		if(cb4.IsChecked() is False):
			aa1 = []
			t1 = 0
		if(cb5.IsChecked() is False):
			aa2 = []
			t2 = 0
		if(cb6.IsChecked() is False):
			aa3 = []
			t3 = 0
		stream3.close()

		
	if(t1 == max(t1 , t2 , t3)):
		if(t2 == max(t2 , t3)):
			self.modulate(aa3 , aa2 , aa1)
		else:
			self.modulate(aa2 , aa3 , aa1)
		streamx = stream1
	elif(t2 == max(t1 , t2 , t3)):
		if(t1 == max(t1 , t3)):
			self.modulate(aa3 , aa1 , aa2)
		else:
			self.modulate(aa1 , aa3 , aa2)
		streamx = stream2
	elif(t3 == max(t1 , t2 , t3)):
		if(t2 == max(t2 , t1)):
			self.modulate(aa1 , aa2 , aa3)
		else:
			self.modulate(aa2 , aa1 , aa3)
		streamx = stream3
	
	stream = p.open(format = p.get_format_from_width(streamx.getsampwidth()),  
		channels = streamx.getnchannels(),  
		rate = streamx.getframerate(),  
		output = True)

	#read data  
	j=0

	framecount = streamx.getnframes()
	while(j<framecount):
		str1 = ''.join(array4[j:j+1024])
		stream.write(str1)
		j+=1024

	#stop stream  
	stream.stop_stream()  
	stream.close()  

	#close PyAudio  
	p.terminate()
	streamx.close()


    def play5(self , e):
	global stream1,stream2,stream3,cb5,cb6,cb7,sld1,sld2,sld3,sld4,sld5,sld6,sld7,sld8,sld9,array1,array2,array3,array4
	#define stream chunk   
	chunk = 1024  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	streamx = ''

        tmp2 = float(sld7.GetValue())/10
        tmp3 = float(sld8.GetValue())/10
        tmp4 = float(sld9.GetValue())/10
	
	p1 = cb5.IsChecked()
	p2 = cb6.IsChecked()
	p3 = cb7.IsChecked()

	t1 = t2 = t3 = 0
	aa1 = aa2 = aa3 = []
	if(self.select1 != 'No File Chosen'):
		tmp1 = cb1.IsChecked()
        	tmp2 = float(sld1.GetValue())/10
      	        tmp3 = float(sld4.GetValue())/10
       	 	tmp4 = float(sld7.GetValue())/10
		self.wavemorph(tmp2 , tmp3 , tmp4 , tmp1 , self.select1 , 1)
		stream1 = wave.open(self.select1 , "rb")
		aa1 = []
		j = int(tmp4 * stream1.getnframes())
		for i in range(0 , j):
			aa1.append(array1[int(i/tmp4)])
		t1 = len(aa1)
		if(cb7.IsChecked() is False):
			t1 = 0
			aa1 = []
		if(cb8.IsChecked() is False):
			t2 = 0
			aa2 = []
		if(cb9.IsChecked() is False):
			t3 = 0
			aa3 = []
		stream1.close()

	if(self.select2 != 'No File Chosen'):
		tmp1 = cb2.IsChecked()
        	tmp2 = float(sld2.GetValue())/10
      	        tmp3 = float(sld5.GetValue())/10
       	 	tmp4 = float(sld8.GetValue())/10
		self.wavemorph(tmp2 , tmp3 , tmp4 , tmp1 , self.select2 , 2)
		stream2 = wave.open(self.select2 , "rb")
		aa2 = []
		j = int(tmp4 * stream2.getnframes())
		for i in range(0 , j):
			aa2.append(array2[int(i/tmp4)])
		t2 = len(aa2)
		if(cb7.IsChecked() is False):
			aa1 = []
			t1 = 0
		if(cb8.IsChecked() is False):
			aa2 = []
			t2 = 0
		if(cb9.IsChecked() is False):
			aa3 = []
			t3 = 0
		stream2.close()

	if(self.select3 != 'No File Chosen'):
		tmp1 = cb3.IsChecked()
        	tmp2 = float(sld3.GetValue())/10
      	        tmp3 = float(sld6.GetValue())/10
       	 	tmp4 = float(sld9.GetValue())/10
		self.wavemorph(tmp2 , tmp3 , tmp4 , tmp1 , self.select3 , 3)
		stream3 = wave.open(self.select3 , "rb")
		aa3 = []
		j = int(tmp4 * stream3.getnframes())
		for i in range(0 , j):
			aa3.append(array3[int(i/tmp4)])
		t3 = len(aa3)
		if(cb7.IsChecked() is False):
			aa1 = []
			t1 = 0
		if(cb8.IsChecked() is False):
			aa2 = []
			t2 = 0
		if(cb9.IsChecked() is False):
			aa3 = []
			t3 = 0
		stream3.close()

		
	if(t1 == max(t1 , t2 , t3)):
		if(t2 == max(t2 , t3)):
			self.mix(aa3 , aa2 , aa1)
		else:
			self.mix(aa2 , aa3 , aa1)
		streamx = stream1
	elif(t2 == max(t1 , t2 , t3)):
		if(t1 == max(t1 , t3)):
			self.mix(aa3 , aa1 , aa2)
		else:
			self.mix(aa1 , aa3 , aa2)
		streamx = stream2
	elif(t3 == max(t1 , t2 , t3)):
		if(t2 == max(t2 , t1)):
			self.mix(aa1 , aa2 , aa3)
		else:
			self.mix(aa2 , aa1 , aa3)
		streamx = stream3
	
	stream = p.open(format = p.get_format_from_width(streamx.getsampwidth()),  
		channels = streamx.getnchannels(),  
		rate = streamx.getframerate(),  
		output = True)

	#read data  
	j=0

	framecount = streamx.getnframes()
	while(j<framecount):
		str1 = ''.join(array4[j:j+1024])
		stream.write(str1)
		j+=1024

	#stop stream  
	stream.stop_stream()  
	stream.close()  

	#close PyAudio  
	p.terminate()
	streamx.close()

    def load1(self , e):
	global stream1

	openFileDialog = wx.FileDialog(self, "Open", "", "","Wav Files (*.wav)|*.wav",wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
	openFileDialog.ShowModal()
	self.select1=openFileDialog.GetPath()
	a=re.sub(r'.*\/','',self.select1)
	self.name1.SetLabel(str(a))

	stream1 = wave.open(self.select1,"rb")
	sample_rate = stream1.getframerate()
	num_frames = stream1.getnframes()
	t=num_frames/sample_rate
	sld4.SetMax(10.0)
	sld4.SetMin(-10.0)
	sld7.SetMin(1)
	stream1.close()

	openFileDialog.Destroy()

    def load2(self , e):
	global stream2

	openFileDialog = wx.FileDialog(self, "Open", "", "","Wav Files (*.wav)|*.wav",wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
	openFileDialog.ShowModal()
	self.select2=openFileDialog.GetPath()
	a=re.sub(r'.*\/','',self.select2)
	self.name2.SetLabel(str(a))

	stream2 = wave.open(self.select2,"rb")
	sample_rate = stream2.getframerate()
	num_frames = stream2.getnframes()
	t=num_frames/sample_rate
	sld5.SetMax(10.0)
	sld5.SetMin(-10.0)
	sld8.SetMin(1)
	stream2.close()

	openFileDialog.Destroy()

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

    def check2(self, e):
	sender = e.GetEventObject()
	isChecked = sender.GetValue()

    def check3(self, e):
	sender = e.GetEventObject()
	isChecked = sender.GetValue()

    def check4(self, e):
	sender = e.GetEventObject()
	isChecked = sender.GetValue()

    def check5(self, e):
	sender = e.GetEventObject()
	isChecked = sender.GetValue()

    def check6(self, e):
	sender = e.GetEventObject()
	isChecked = sender.GetValue()

    def check7(self, e):
	sender = e.GetEventObject()
	isChecked = sender.GetValue()

    def check8(self, e):
	sender = e.GetEventObject()
	isChecked = sender.GetValue()

    def check9(self, e):
	sender = e.GetEventObject()
	isChecked = sender.GetValue()

    def slide1(self, e):	        
	obj = e.GetEventObject()
	val = obj.GetValue()
	val = val*1.0/10
	self.txt1.SetLabel(str(val)) 

    def slide2(self, e):	        
	obj = e.GetEventObject()
	val = obj.GetValue()
	val = val*1.0/10
	self.txt2.SetLabel(str(val)) 

    def slide3(self, e):	        
	obj = e.GetEventObject()
	val = obj.GetValue()
	val = val*1.0/10
	self.txt3.SetLabel(str(val)) 

    def slide4(self, e):	        
	obj = e.GetEventObject()
	val = obj.GetValue()
	val = val*1.0/10
	self.txt4.SetLabel(str(val)) 
	
    def slide5(self, e):	        
	obj = e.GetEventObject()
	val = obj.GetValue()
	val = val*1.0/10
	self.txt5.SetLabel(str(val)) 

    def slide6(self, e):	        
	obj = e.GetEventObject()
	val = obj.GetValue()
	val = val*1.0/10
	self.txt6.SetLabel(str(val)) 

    def slide7(self, e):	        
	obj = e.GetEventObject()
	val = obj.GetValue()
	val = val*1.0/10
	self.txt7.SetLabel(str(val)) 

    def slide8(self, e):	        
	obj = e.GetEventObject()
	val = obj.GetValue()
	val = val*1.0/10
	self.txt8.SetLabel(str(val)) 
	
    def slide9(self, e):	        
	obj = e.GetEventObject()
	val = obj.GetValue()
	val = val*1.0/10
	self.txt9.SetLabel(str(val)) 

    def OnClose(self, e):
	self.Close(True)
        
def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    

if __name__ == "__main__":
	main()
