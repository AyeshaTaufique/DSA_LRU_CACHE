def updated(dict1,dict2):
        dict1={**dict1,**dict2}
        return dict1
def addList(list1,item):
    list1=list1+[item]
    return list1
def lenght(dict):
    i=0
    for j in dict:
        i=i+1
    return i   
def dicGet(item,dic):
    for i in  dic:
        if i==item:
            return dic[i]



class LRU():
    def __init__(self,size):
        assert size <=50 , "you are not allowed to have that much allocation"
        assert size >0, "Invalid size given"
        self.dict={}
        self.size=size
        self.cache_miss=0
        self.track=[]
    def put(self,key,item):
        l=lenght(self.dict)
        
        if l==self.size:
            if key in self.dict:
                self.track.remove(key)
                self.track=addList(self.track,key)
                self.dict.pop(key)
            else: 
              self.cache_miss+=1
              x=self.track.pop(0)
              self.dict.pop(x)
            self.dict=updated(self.dict,{key:item})
            
        else:
            self.cache_miss+=1
            self.dict=updated(self.dict,{key:item})
        self.track=addList(self.track,key)

    def get(self,key):
        if key in self.dict:
            y=dicGet(key,self.dict)
            self.dict.pop(key)
            self.dict=updated(self.dict,{key:y})
            self.track.remove(key)
            self.track=addList(self.track,key)
            return  dicGet(key,self.dict)
        else:
            self.cache_miss+=1 
            return -1 
    def __str__(self):
    
        strg="{"
        for i in self.dict:
            v=[i,dicGet(i,self.dict)]
            strg=strg+str(v[0])+"="+str(v[1])+","
        strg=strg[ :-1]+""
        return strg+"}"


        

l1=LRU(50)
print("Inserting 50 numbers from 0 to 49:")
for i in range(50):
    l1.put(i,i)
print(l1)  
print("reteriving odd numbers:")
for i in range(1,25,2):
        (l1.get(i)) 
print(l1) 

print("Inserting prime numbers:")
k=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for i in k:
        l1.put(i,i)
print(l1)        
 
print("Miss rate = ",l1.cache_miss)   
             

    
