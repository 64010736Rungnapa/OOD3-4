'''รับ string มาเข้าคิวหา secret code โดยรับ input คือ

code เป็น string ยาว

hint คือตัวแรกของรหัสที่ถูกต้อง

**คำใบ้**

ascii ของ "f" มีค่า = 102

ascii ของ "g" มีค่า = 103

ascii ของ "h" มีค่า = 104

ascii ของ "i" มีค่า = 105

ascii ของ "j" มีค่า = 106'''
class Queue:
    def __init__(self):
        self.items = []
        
    def enQueue(self,i):
        self.items.append(i)
        
    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def front(self):
        return self.items[0] if self.size() > 0 else -1
    
queue = Queue()
a,b = input("Enter code,hint : ").split(",")
s = ord(b)-ord(a[0])
for i in a:
    queue.enQueue(chr(ord(i)+s))
    print(queue.items)