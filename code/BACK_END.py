global ctr
class Node:
    def __init__(self,name=None,phone_num=None,blood_type=None,city=None,next=None,pre=None):
        self.name=name
        self.phone_number=phone_num
        self.blood_type=blood_type
        self.city=city
        self.next=next
        self.pre=pre
        return

class data_collection_Dlinkedlist:
    def __init__(self):
        self.head=None
        self.last=self.head
        ctr=0
        return

    #creating a node for storing data of the donor
    def create_node(self,name,phone_num,blood_type,city):
        node=Node(name,phone_num,blood_type,city)
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head.pre=node
            self.head=node
        ctr+=1
        return
    #traversing when turns are smaller than or equal to half of the size of node
    def forward_traversing(self,turns):
        temp=self.head
        for i in range(0,turns):
            temp=temp.next
        print("Name of donor: ",temp.name)
        print("Phone Number of donor: ", temp.phone_number)
        print("Blood Type of donor: ", temp.blood_type)
        print("City of donor: ",temp.city)
        return

    #traversing when the turns are larger than the half of the size of node
    def backward_traversing(self,turns):
        temp=self.last
        turns=ctr-turns
        for i in range(0,turns):
            temp=temp.pre
        print("Name of donor: ", temp.name)
        print("Phone Number of donor: ", temp.phone_number)
        print("Blood Type of donor: ", temp.blood_type)
        print("City of donor: ", temp.city)
        return



if __name__=="__main__":


    pass
