class Stack():  
    def __init__(self,size):  
        self.size=size;  
        self.stack=[];  
        self.top=-1;  
    def push(self,ele):
        if self.isfull():  
            raise Exception("out of range");  
        else:  
            self.stack.append(ele);  
            self.top=self.top+1;  
    def pop(self):
        if self.isempty():  
            raise Exception("stack is empty");  
        else:  
            self.top=self.top-1;  
            return self.stack.pop();  
    def isfull(self):  
        return self.top+1==self.size;  
    def isempty(self):  
        return self.top==-1;
    def geturl(self):
        if self.top==-1:
            return ''
        else:
            url=''
            while(self.top != -1):
                url = self.stack.pop() + url
                self.top = self.top-1
            return url
    def clear(self):
        while(self.top != -1):
            self.stack.pop();
            self.top=self.top-1; 