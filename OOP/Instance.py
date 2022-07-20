#Point 實體物件的設計: 平面座標上的點
class Point :
    def __init__(self,x,y): #初始化函數
        self.x = x #實體屬性
        self.y = y
    #定義實體方法
    def show(self):
        print(self.x,self.y) 
    def distance(self,targetX,targetY):
        return (((self.x-targetX)**2+(self.y-targetY)**2)**0.5)
p1 = Point(3,4)
print(p1.x,p1.y) # 實體物件.屬性名稱
p1.show() #呼叫實體方法
print(p1.distance(0,0)) #計算座標3,4 和座標0,0之間的距離
p2 = Point(5,6)
print(p2.x,p2.y)
#FullName 實體物件的設計: 分開紀錄性 明資料的全名


class FullName:
    def __init__(self,first,last):
        self.first = first
        self.last = last
name1 = FullName("K.Y","HUANG")
print(name1.first,name1.last)
name2 =FullName("T.Y.","Lin")
print(name2.first,name2.last)


#File 實體物件的設計:包裝檔案讀取的程式
class File :
    def __init__(self,name):
        self.name = name 
        self.file = None # 尚未開啟檔案,初期是None
    def open(self):
        self.file = open(self.name,mode="r",encoding="utf-8")
    def read(self):
        return self.file.read()
#讀取第一個物件        
f1 = File("data1.txt")
f1.open()
data = f1.read()
print(data)

#讀取第二個檔案
f2 = File("data2.txt")
f1.open()
data = f2.read()
print(data)
#複雜的code包裝在類別中，用使體物件操作，使程式碼簡單清楚