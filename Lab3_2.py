'''
จงเขียนโปรแกรมเพื่อตรวจสอบว่า นิพจน์มีวงเล็บครบถ้วนหรือไม่ โดยใช้ Stack ช่วยในการแก้ปัญหา

โดยสามารถแจ้งได้ว่าข้อผิดพลาดที่เกิดขึ้นเกิดจากสาเหตุใด

1. มี วงเปิดไม่ตรงชนิดกับวงเล็บปิด

2. วงเล็บปิดเกิน

3. วงเล็บเปิดเกิน

แล้วให้แสดงผลตามตัวอย่าง'''
class Stack :
 
 def __init__ (self , list = None) :
 
  if list == None :
   self.items = []
  else :
   self.items = list
   
 
 def push (self,i) :
  self.items.append(i)
  
 def pop(self):
  return self.items.pop()
  
 def isEmpty(self):
   return self.items == []
   
 def size(self) :
  return len(self.items)
 
 def __str__(self):
    s = ""
    for element in self.items :
        s += str(element)
    return s

s = Stack()
errorType = 0 

exp = input("Enter expresion : ")

for i in exp :
    if i in "([{" :
        s.push(i)
    elif i in ")]}" :
        if s.size() > 0 :
            temp = s.pop()
            if (i == ")" and temp == "(") or (i == "]" and temp == "[") or( i == "}" and temp == "{" ) :
                continue
            else :
                errorType = 1  # Unmatch open-close
        else :
            if errorType != 1 :
                errorType = 2 # close paren excess

if s.size() > 0 :
    if errorType != 1 :
        errorType = 3  # open paren excess

print(exp,end=" ")

if errorType == 0 :
    print("MATCH")
elif errorType == 1 :
    print("Unmatch open-close")
elif errorType == 2 :
    print("close paren excess")
elif errorType == 3 :
    print("open paren excess  ",s.size(),":",s)


