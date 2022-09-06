'''ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา

E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผลค่าที่ทำการ enqueue และ index ของตัวที่ทำการเพิ่มเข้าไป

D                 ให้ทำการ dequeue ตัวที่อยู่หน้าสุดของ Queue ออกและแสดงตัวเลขที่เอาออกและแสดงขนาดของ Queue

                    หลังจากทำการ dequeue แล้ว

*** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty ***'''
class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self,i):
        self.items.append(i)
        print(f"Add {i} index is {len(self.items)-1}")

    def deQueue(self):
        #return self.items.pop(0)
        if len(self.items) == 0:
            print("-1")
        else:
            return print(f"Pop {(self.items.pop(0))} size in queue is {len(self.items)}")

    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def returnQueue(self):
        return self.items

num = input("Enter Input : ").split(",")
q = Queue()

for x in range(len(num)):
    if len(num[x]) == 4:
        if 'E' in num[x]:
            q.enQueue(str(num[x][-2]+num[x][-1]))
    else:
        if 'D' in num[x]:
            q.deQueue()

if len(q.items) != 0:
    print(f"Number in Queue is :  {q.items}", end = "")
    
else:
    print("Empty")