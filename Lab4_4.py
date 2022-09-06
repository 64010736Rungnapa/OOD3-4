'''โรงอาหารของบริษัทแห่งหนึ่ง จะมีเจ้าหน้าที่คอยจัดแถวสำหรับการซื้ออาหาร โดยจะมีหลักการคือจะดูจากแผนกของพนักงานแต่ละคนว่าอยู่แผนกไหน ถ้าหากในแถวที่ต่ออยู่มีแผนกนั้น จะนำพนักงานคนนั้นแทรกไปด้านหลังของแผนกเดียวกัน ตัวอย่างเช่น
Front | 1 2 2 2 2 3 3 3 | Rear  จาก Queue ถ้าหากมีพนักงานแผนก1เข้ามา Queue จะกลายเป็น Front | 1 1 2 2 2 2 3 3 3 | Rear

Input :
จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นแผนกของพนักงานและIDของพนักงานแต่ละคน  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
E < id >  ->   เป็นการนำพนักงานเข้า Queue
D  ->  เป็นการนำพนักงานคนหน้าสุดออกจากแถว โดยจะแสดงผลเป็น id ของพนักงานคนนั้น ถ้าหากไม่มีพนักงานในแถวจะทำการแสดงผลเป็น Empty

อธิบาย TestCase_1 :  จะมีพนักงาน 4 คน คือแผนก 1 id=101,102 และแผนก 2 id=201,202  ต่อมาจะแสดงผล Empty เพราะยังไม่มีพนักงานในแถว  และนำพนักงาน id=101และ201 เข้าแถวตามลำดับ ต่อมาจะแสดงผลเป็น 101 เพราะพนักงาน 101 อยู่คนแรกและแสดงผล 201 เพราะอยู่คนแรก

'''
class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        if len(self.items)>0:
            return self.items.pop(0)
    def copy(self,i):
        self.items = i
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def returnQueue(self):
        return self.items
    def insertQueue(self,data,point):
        self.temp = []
        for i in range(point):
            self.temp.append(self.items[i])
        self.temp.append(data)
        for i in range (point,len(self.items)):
            self.temp.append(self.items[i])
        self.items = self.temp

q = Queue()
order = Queue()

Num_ID,request = input("Enter Input : ").split('/')
Num_ID = list(Num_ID.split(','))
request = list(request.split(','))
for i in request:
    l = i.split()
    if l[0] == 'D':
        if q.size() == 0:
            print("Empty")
        else:
            k = q.deQueue()
            order.deQueue()
            print(k)
    elif l[0] == 'E':
        for j in Num_ID:
            t = j.split()
            if t[1]==l[1]:
                point = q.size()
                for ID in range(order.size()-1,-1,-1):
                    if order.returnQueue()[ID] == t[0]:
                        point = ID+1
                        break
                if point == q.size():
                    q.enQueue(t[1])
                    order.enQueue(t[0])
                else:
                    q.insertQueue(t[1],point)
                    order.insertQueue(t[0],point)