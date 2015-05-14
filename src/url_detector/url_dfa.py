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
                        'h':'h',
                        'accept':False,
                        'err':'start-no-match'
                    },
    'start-match'   :{
                        'h':'h',
                        'accept':True,
                        'err':'start-no-match'
                    },        
    'h'             :{
                        't':'ht',
                        'h':'h',
                        'matchStart':True, 
                        'err':'start-no-match'
                    },
    'ht'            :{
                        't':'htt',
                        'h':'h',
                        'err':'start-no-match'
                    },
    'htt'           :{
                        'p':'http',
                        'h':'h',
                        'err':'start-no-match'
                    },
    'http'          :{
                        's':'https',
                        ':':'http:',
                        'h':'h',
                        'err':'start-no-match'
                    },
    'https'         :{
                        ':':'https:',
                        'h':'h',
                        'err':'start-no-match'
                      },
    'http:'         :{
                        '/':'http:/',
                        'h':'h',
                        'err':'start-no-match'
                      },
    'https:'        :{
                        '/':'https:/',
                        'h':'h',
                        'err':'start-no-match'
                      },
    'http:/'        :{
                        '/':'protocol-ready',
                        'h':'h',
                        'err':'start-no-match'
                      },
    'https:/'       :{
                        '/':'protocol-ready',
                        'h':'h',
                        'err':'start-no-match'
                      },
    'protocol-ready':{
                        'number':'domain-normal',
                        'letter':'domain-normal',
                        'err':'start-no-match'
                      },
    'domain-normal' :{
                        'number':'domain-normal',
                        'letter':'domain-normal',
                        '-':'domain-',
                        ':':'port0',
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
