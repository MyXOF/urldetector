'''
    state list
    add your states here
'''
states = ['start-no-match','start-match','h','ht','htt',
          'http','https','https:','http:/','http://',
          'https:/','protocol_ready','domain_normal','domain-','port0',
          'port1','port2','port3','port4','port5',
          'param'];

__num__ = ['0','1','2','3','4','5','6','7','8','9'];
__lower_letter__ = ['q','w','e','r','t',
                    'y','u','i','o','p',
                    'a','s','d','f','g',
                    'h','j','k','l','z',
                    'x','c','v','b','n',
                    'm'];
__upper_letter__ = ['Q','W','E','R','T',
                    'Y','U','I','O','P',
                    'A','S','D','F','G',
                    'H','J','K','L','Z',
                    'X','C','V','B','N',
                    'M'];
                    
__domain_special_letter__ = '-';
__domain_separator__ = '.';
__port_letter__ = ':';
__param_begin__ = '/';
__param_special_type__ = ['=','-',' ','.','?',
                          '%','&','+','<','>',
                          '_','@','#','$','^',
                          '*','/'];

'''
    transition and match rules
    match: match rules
    err: state if no match for input
    matchStart: match the start of an url
    accept: matched an valid url
'''
transitions = {
    'start-no-match':{
                        #'match':{'h':'h'}, 
                        'h':'h',
                        'accept':False,
                        'err':'start-no-match'
                    },
    'start-match'   :{
                        #'match':{'h','h'},
                        'h':'h',
                        'accept':True,
                        'err':'start-no-match'
                    },        
    'h'             :{
                        #'match':{'t':'ht', 'h':'h'},
                        't':'ht',
                        'h':'h',
                        'matchStart':True, 
                        'err':'start-no-match'
                    },
    'ht'            :{
                        #'match':{'t':'htt', 'h':'h'}, 
                        't':'htt',
                        'h':'h',
                        'err':'start-no-match'
                    },
    'htt'           :{
                        #'match':{'p':'http', 'h':'h'}, 
                        'p':'http',
                        'h':'h',
                        'err':'start-no-match'
                    },
    'http'          :{
                        #'match':{'s':'https',':':'http:','h':'h'},
                        's':'https',
                        ':':'http:',
                        'h':'h',
                        'err':'start-no-match'
                    },
    'https'         :{
                        #'match':{':':'https:','h':'h'},
                        ':':'https:',
                        'h':'h',
                        'err':'start-no-match'
                      },
    'http:'         :{
                        #'match':{'/':'http:/','h':'h'},
                        '/':'http:/',
                        'h':'h',
                        'err':'start-no-match'
                      },
    'https:'        :{
                        #'match':{'/':'https:/','h':'h'},
                        '/':'https:/',
                        'h':'h',
                        'err':'start-no-match'
                      },
    'http:/'        :{
                        #'match':{'/':'protocol-ready','h':'h'},
                        '/':'protocol-ready',
                        'h':'h',
                        'err':'start-no-match'
                      },
    'https:/'       :{
                        #'match':{'/':'protocol-ready','h':'h'},
                        '/':'protocol-ready',
                        'h':'h',
                        'err':'start-no-match'
                      },
    'protocol-ready':{
                        'number':'domain-noraml',
                        'letter':'domain-normal',
                        'err':'start-no-match'
                      },
    'domain-normal' :{
                        'number':'domain-normal',
                        'letter':'domain-normal',
                        '-':'domain-',
                        ':':'port',
                        '/':'param',
                        '.':'protocol-ready',
                        'err':'start-match'
                      },
    'domain-'       :{
                        'number':'domain-normal',
                        'letter':'domain-normal',
                        '-':'domain-',
                        'err':'start-no-match'
                      },
    'port0'         :{
                      'number':'port1',
                      'err':'start-match'
                      },
    'port1'         :{
                      'number':'port2',
                      '/':'param',
                      'err':'start-match'
                      },               
    'port2'         :{
                      'number':'port3',
                      '/':'param',
                      'err':'start-match'
                      },
    'port3'         :{
                      'number':'port4',
                      '/':'param',
                      'err':'start-match'
                      },    
    'port4'         :{
                      'number':'port5',
                      '/':'param',
                      'err':'start-match'
                      },        
    'port5'          :{
                      '/':'param',
                      'err':'start-match'
                      },
    'param'         :{
                      'number':'param',
                      'letter':"param",
                      'special':'param',
                      'err':'start-match'
                      }         
#add the code of your transitions here
}


state = states[0]  # the current state
startpos = 0       # mark the start of an URL
result = []        # the detected URLs


with open('test.html', 'rb') as f:
    input_str = f.readline()
    


for index, content in enumerate(input_str):
    t = transitions[state]
    if 'matchStart' in t and t['matchStart']: 
        startpos = index - 1
    elif 'accept' in t and t['accept']: 
        result.append(input_str[startpos, index - startpos])
        
    if content in t:
        state = t[content]
    else:
        if 'number' in t:
            if content in __num__:
                state = t['number']
        elif 'letter' in t:
            if (content in __upper_letter__) or (content in __lower_letter__):
                state = t['letter']
        elif 'special' in t:
            if content in __param_special_type__:
                state = t['special']
        else:
            state = t['err']                
    #elif 'match' in t:
    #    raise Exception('add your code here')    
        #add your code here
    #else: state = t['err']
 
t = transitions[state]
if 'accept' in t and t['accept']: result.append(input_str[startpos:])

with open('test.txt', 'wb') as f:
    f.write('\n'.join(result))

class Stack():  
    def __init__(self,size):  
        self.size=size;  
        self.stack=[];  
        self.top=-1;  
    def push(self,ele):  #入栈之前检查栈是否已满  
        if self.isfull():  
            raise Exception("out of range");  
        else:  
            self.stack.append(ele);  
            self.top=self.top+1;  
    def pop(self):             # 出栈之前检查栈是否为空  
        if self.isempty():  
            raise Exception("stack is empty");  
        else:  
            self.top=self.top-1;  
            return self.stack.pop();  
      
    def isfull(self):  
        return self.top+1==self.size;  
    def isempty(self):  
        return self.top==-1;