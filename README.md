# Blood-Donating-App
Blood Donating App has been created using the Python language and using the external framework Kivy.
# Over View
We have created a blood donating app in order to provide the fast donation of blood.
This app would contain the data of all types of blood the people are having. 
The blood of donor would be there and according to the receiver if their blood type matches than the blood would be donated as fast as it can according to the desired location. 
This app would automatically allocate rest time to the donors who had donated the blood. 
# Scope
If this app would spread than many lives can be saved as the finding of the perfect blood for donor and the receiver would be there.
A healthy lifestyle would be adopted and for future emergencies there will be no hustle and bustle. 
# Language Used
The language used in this is python with the help of the Kivy library.
# 	CODE:

import kivy
	from kivy.app import App
	from kivy.uix.button import Button
	from kivy.uix.gridlayout import GridLayout
	from kivy.uix.textinput import TextInput
	from kivy.uix.label import Label
	

	#Layout
	class grid_layout_used(GridLayout):
	    #counstructor
	    def __init__(self, **kwargs):
	        #base class constructor
	        super().__init__(**kwargs)
	        self.start_tab()
	        return
	    #starting or program
	    def start_tab(self):
	        #clearing screen
	        self.clear_widgets()
	        self.cols = 1
	        self.donor_button = Button(text="DONOR INFO", background_color =(0,1,1,1),color =(1, 1, 1, 1))
	        self.donor_button.bind(on_press=self.on_click_donor)
	        self.reciver_button = Button(text="RECIEVER INFO" , background_color =(0,1,1,1),color =(1, 1, 1, 1))
	        self.reciver_button.bind(on_press=self.on_click_reciever)
	        self.add_widget(self.reciver_button)
	        self.add_widget(self.donor_button)
	        return
	

	    def bind_start_tab(self,instance):
	        self.start_tab()
	        return
	    #reciever function start
	    def on_click_reciever(self, instance):
	        self.clear_widgets()
	        self.cols=2
	        self.spacing = 4
	        #Creating label dynamically
	        for i in range(0,active_list.counter):
	            arr=active_list.Reciever_func()
	            self.bu1 = Label(text=str(i+1),font_size="18sp")
	            self.add_widget(self.bu1)
	            self.add_widget(Label(text=F'{arr[0]}{arr[1]}{arr[2]}{arr[3]}'))
	        self.bu2=Button(text="Enter Serial Number")
	        self.bu2.bind(on_press=self.on_click)
	        self.add_widget(self.bu2)
	        self.index=TextInput(multiline=False)
	        self.add_widget(self.index)
	        self.exit=Button(text="Exit")
	        self.exit.bind(on_press=self.bind_start_tab)
	        self.add_widget(self.exit)
	        return
	

	    def on_click(self, instance):
	        self.clear_widgets()
	        self.cols=1
	        self.add_widget(Label(text="Have you Recieved the Blood?",font_size="15sp"))
	        self.butt2 = Button(text="Yes")
	        self.butt3 = Button(text="No")
	        self.add_widget(self.butt2)
	        self.add_widget(self.butt3)
	        self.butt2.bind(on_press=self.on_click_yes)
	        self.butt3.bind(on_press=self.on_click_reciever)
	        return
	

	    def on_click_yes(self, instance):
	        self.clear_widgets()
	        self.cols=1
	        #moving information from active to inactive linked list
	        arr=active_list.delete_send_informtion(int(self.index.text))
	        inactive_list.create_node(arr[0],arr[1],arr[2],arr[3])
	        self.write_file_for_inactive(arr)
	        #deleting the selected node
	        active_list.Delete_at(int(self.index.text))
	        self.del_from_active_file(arr)
	

	        self.butoon=Button(text="Thank You",font_size="16sp")
	        self.butoon.bind(on_press=self.bind_start_tab)
	        self.add_widget(self.butoon)
	        return
	    #function to del data from active file
	    def del_from_active_file(self,arr):
	        FILE=open("Active.txt","w")
	        for i in range(active_list.counter):
	            li=active_list.backward_traversing()
	            for i in li:
	                FILE.write(i)
	        return
	    #function to write data in inactive file
	    def write_file_for_inactive(self,arr):
	        FILE=open("Inactive.txt","a")
	        FILE.write(arr[0])
	        FILE.write(arr[1])
	        FILE.write(arr[2])
	        FILE.write(arr[3])
	        FILE.close()
	        return
	

	    #donor tab function starts
	    def on_click_donor(self, instance):
	        # CLERING THE SCREEN
	        self.clear_widgets()
	        self.spacing = 4
	        # COLUMN = 2
	        self.cols = 2
	

	        # button to submit data
	        self.button1 = Button(text="Submit", background_color=(0, 1, 1, 1),color=(1, 1, 1, 1))
	        self.button1.bind(on_press=self.on_submit)
	        self.button2 = Button(text="Exit", background_color=(0, 1, 1, 1), color=(1, 1, 1, 1))
	        self.button2.bind(on_press=self.bind_start_tab)
	

	        self.text0 = Label(text="Donor Name")
	        self.name = TextInput(multiline=False)
	

	        self.text1 = Label(text="Donor Contact Number")
	        self.phone = TextInput(multiline=False)
	

	        self.text2 = Label(text="Donor Blood_Type")
	        self.blood = TextInput(multiline=False)
	

	        self.text3 = Label(text="City (where is he currently available)")
	        self.city = TextInput(multiline=False)
	

	        # adding widgets
	        self.add_widget(self.text0)
	        self.add_widget(self.name)
	        # phone number
	        self.add_widget(self.text1)
	        self.add_widget(self.phone)
	        # blood type
	        self.add_widget(self.text2)
	        self.add_widget(self.blood)
	        # city
	        self.add_widget(self.text3)
	        self.add_widget(self.city)
	

	        self.add_widget(self.button1)
	        self.add_widget(self.button2)
	        return
	

	    def on_submit(self, instance):
	        #opeing active file and appending data in it
	        FILE = open("Active.txt", "a")
	        FILE.write("\n")
	        FILE.write(self.name.text)
	        FILE.write("\n")
	        FILE.write(self.phone.text)
	        FILE.write("\n")
	        FILE.write(self.blood.text)
	        FILE.write("\n")
	        FILE.write(self.city.text)
	        FILE.close()
	        #creating data to be stored in active list Adding a new line after eachh variable
	        self.name.text=self.name.text+"\n"
	        self.phone.text=self.phone.text+"\n"
	        self.blood.text=self.blood.text+"\n"
	        self.city.text=self.city.text+"\n"
	        active_list.create_node(self.name.text, self.phone.text,self.blood.text,self.city.text)
	        self.start_tab()
	        return
	    #donor tab function ends
	

	#class for creating the app
	class Blood_DonationApp(App):
	    def build(self):
	        return grid_layout_used()
	

	

	

	# data struture
	class Node:
	    #defing data to be stored
	    def __init__(self, name=None, phone_num=None, blood_type=None, city=None, next=None, pre=None):
	        self.name = name
	        self.phone_number = phone_num
	        self.blood_type = blood_type
	        self.city = city
	        self.next = next
	        self.pre = pre
	        return
	#data collection class
	class data_collection_Dlinkedlist:
	    def __init__(self):
	        self.head = None
	        self.last = self.head
	        self.reciever_data = None
	        self.file_data=None
	        self.counter=0
	        return
	

	    # creating a node for storing data of the donor (we are creating node at the start)
	    def create_node(self, name, phone_num, blood_type, city):
	        node = Node(name, phone_num, blood_type, city)
	        if self.head == None:
	            self.head = node
	            self.last=self.head
	            self.file_data=self.last
	        else:
	            node.next = self.head
	            self.head.pre = node
	            self.head = node
	        self.counter += 1
	        self.reciever_data = self.head
	        return
	

	    # traversing
	    def forward_traversing(self,turns):
	        temp = self.head
	        for i in range(0, turns):
	            temp = temp.next
	        print("Phone Number of donor: ", temp.name)
	        print("City Type of donor: ", temp.city)
	        print("Phone Number of donor: ", temp.phone_number)
	        print("Blood Type of donor: ", temp.blood_type)
	        return
	

	    #USING THIS FUNCTION TO STORE VALUES in  Inactive FILE
	    def backward_traversing(self):
	        if self.file_data==None:
	            self.file_data=self.last
	        li=[]
	        li.append(self.file_data.name)
	        li.append(self.file_data.phone_number)
	        li.append(self.file_data.blood_type)
	        li.append(self.file_data.city)
	        self.file_data=self.file_data.pre
	        return li
	

	    # DISPLAYING ALL NODES THATS HAVE BEEN CREATED
	    def Display_all(self):
	        temp = self.head
	        while temp != None:
	            print("Name of donor: ", temp.name)
	            print("Phone Number of donor: ", temp.phone_number)
	            print("Blood Type of donor: ", temp.blood_type)
	            print("City of donor: ", temp.city)
	            temp = temp.next
	        return
	

	    #this function is use to take information from the node and return it in list form
	    def Reciever_func(self):
	        if(self.reciever_data==None):
	            self.reciever_data=self.head
	        li = []
	        li.append(self.reciever_data.name)
	        li.append(self.reciever_data.phone_number)
	        li.append(self.reciever_data.blood_type)
	        li.append(self.reciever_data.city)
	        self.reciever_data = self.reciever_data.next
	        return li
	

	    #delete any node from any location
	    def Delete_at(self, pos):
	        if self.head == None:
	            print("Node is empty")
	        elif pos == 1: #deleting from start
	            self.head = self.head.next
	            if self.counter==1:
	                pass
	            else:
	                self.head.pre = None
	        elif pos==self.counter:         #deleting from end
	            temp = self.head
	            while temp.next != None:
	                temp = temp.next
	            temp = temp.pre
	            temp.next = None
	            self.last=temp
	            self.file_data=self.last
	        else:        #deleting from any point
	            temp = self.head
	            i = 1
	            while i < pos:
	                print(i)
	                temp = temp.next
	                i += 1
	            temp.pre.next = temp.next
	            temp.next.pre = temp.pre
	            temp.next = None
	            temp.prev = None
	        self.counter =self.counter-1
	        return
	    #returing the information store in the node that is to be deleted so that we can store
	    #it in inactive file
	    def delete_send_informtion(self,pos):
	        temp=self.head
	        i=1
	        while i<pos:
	            temp=temp.next
	            i+=1
	        li=[]
	        li.append(temp.name)
	        li.append(temp.phone_number)
	        li.append(temp.blood_type)
	        if pos==1:
	            temp.city=temp.city+"\n"
	        li.append(temp.city)
	        return li
	

	# CREATING GLOBAL OBJECT OF DATA COLLLECTION CLASS SO THAT WE CAN USE IT IN ANYOTHER CLASS
	global active_list
	global inactive_list
	active_list = data_collection_Dlinkedlist()
	inactive_list= data_collection_Dlinkedlist()
	

	if __name__ == "__main__":
	    #opening file
	    FILE = open("Active.txt", "r")
	    y = 0
	    for i in FILE:
	        y += 1
	        if y == 1:
	            name = i
	        elif y == 2:
	            contact_num = i
	        elif y == 3:
	            blood_type = i
	        elif y == 4:
	            city = i
	            active_list.create_node(name, contact_num, blood_type, city)
	            y = 0
	    FILE.close()
	    #closing file
	    Blood_DonationApp().run()
  # Blood Donation App Start look: 
  ![image](https://user-images.githubusercontent.com/92653096/193654316-3f37f523-f3b0-4d2b-83da-b94a3a234c06.png)
# RECIVER TAB:
![image](https://user-images.githubusercontent.com/92653096/193654398-894ddc35-365e-4ee3-ba4a-df18439da81a.png)
# Confirmation that the user has received blood:
![image](https://user-images.githubusercontent.com/92653096/193654455-d1535d8f-a3e1-4691-8fbe-ff058fa97ca6.png)
# Taking Blood Donation information:
![image](https://user-images.githubusercontent.com/92653096/193654539-559daba8-18c4-4db5-b746-20831e588ad2.png)
![image](https://user-images.githubusercontent.com/92653096/193654553-935080d4-08fe-438f-a2ec-7b8ecd2f41f7.png)
# THANK YOU, TAB:
![image](https://user-images.githubusercontent.com/92653096/193654606-1f584b61-8985-4993-a849-f944a04bed66.png)

  #  	CONCLUSION:
We learned how to design an app. We used the concept of linked list Which, is the important part of data structures and algorithm.



