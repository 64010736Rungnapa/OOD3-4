'''ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
+: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
-: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
*: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
/: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
DUP: Duplicate (not double) ค่าบนสุดของ stack
POP: Pop ค่าบนสุดออกจาก stack และ discard.
PSH: ทำการ push ตัวเลขลง stack
หมายเหตุ คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
*************************************************
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())'''
class StackCalc:
    
    def __init__(self) -> None:
        self.stack=[]
        Value = ""

    def run(self,arg_in):
        arg_list = arg_in.split(" ")

        for arg in arg_list:
            self.Value = ""

            if arg >= "0" and arg <= "9":
                self.stack.append(int(arg))
            elif arg == "+":
                temp=self.stack[-1]
                self.stack.pop()
                temp2=self.stack[-1]
                self.stack.pop()
                self.stack.append(temp+temp2)
            elif arg == "-":
                temp=self.stack[-1]
                self.stack.pop()
                temp2=self.stack[-1]
                self.stack.pop()
                self.stack.append(temp-temp2)
            elif arg == "*":
                temp=self.stack[-1]
                self.stack.pop()
                temp2=self.stack[-1]
                self.stack.pop()
                self.stack.append(temp*temp2)
            elif arg == "/":
                temp=self.stack[-1]
                self.stack.pop()
                temp2=self.stack[-1]
                self.stack.pop()
                self.stack.append(temp/temp2)
            elif arg == "DUP":
                self.stack.append(self.stack[-1])
            elif arg == "POP":
                self.stack.pop()
            else:
                print("Invalid instruction: "+arg)
                self.Value = arg
                return
        
    def getValue(self):
        if len(self.stack) != 0:
            return int(self.stack[-1])
        elif self.Value != "":
            return ""
        elif len(self.stack) == 0 and self.Value=="":
            return 0


print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())