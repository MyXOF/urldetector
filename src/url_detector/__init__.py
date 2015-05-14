from stack import Stack
import url_dfa

state = url_dfa.states[0]  # the current state
result = []        # the detected URLs
quality_url_stack = Stack(4096)

with open('../data/test1.html', 'rb') as f:
    #input_str = f.readline()
    for input_str in f:
        for content in input_str:
            t = url_dfa.transitions[state]
            if 'accept' in t and (not t['accept']):
                if (not quality_url_stack.isempty()):
                    quality_url_stack.clear()
            elif 'accept' in t and t['accept']:
                __url = quality_url_stack.geturl()
                result.append(__url)
                  
            if content in t:
                state = t[content]
                quality_url_stack.push(content)
            else:
                if 'number' in t:
                    if content in url_dfa.__num__:
                        state = t['number']
                        quality_url_stack.push(content)
                        continue
                if 'letter' in t:
                    if (content in url_dfa.__upper_letter__) or (content in url_dfa.__lower_letter__):
                        state = t['letter']
                        quality_url_stack.push(content)
                        continue
                if 'special' in t:
                    if content in url_dfa.__param_special_type__:
                        state = t['special']
                        quality_url_stack.push(content)
                        continue
                state = t['err']                
f.close()
for url in result:
    print url

# with open('test.txt', 'wb') as f:
#     f.write('\n'.join(result))

