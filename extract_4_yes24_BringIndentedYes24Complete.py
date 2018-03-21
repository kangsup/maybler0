from bs4 import BeautifulSoup

with open('279739.htm') as f:
    indent_init = 0
    indent_true = False
    
    soup = BeautifulSoup(f.read())

    yes_wrap = soup.select('div#yesWrap')[0]
    wrapper_content = yes_wrap.select('div#wrapperContent')[0]
    
    title_div = wrapper_content.select('div#title')[0]
    title_h1 = title_div.select('h1 > a')[0]
    print("Title : " + str(title_h1.contents))
                            
    chapters = soup.select('p#contents_constitution_text0')[0]
    only_contents = chapters.select('span.more_contents')[0]
    print  ("----1-----"+'\n')
    print(str(only_contents.contents))
    print("----2-----"+'\n')
    print(str(only_contents.contents).replace('<br/>', '\n'))
    for raw_elt in only_contents.contents :
        elt = str(raw_elt)
        if elt.startswith('Part'):
            indent_init += 1
            indent_true = False
        else:
            indent_true = True 
        #print ("Indentation: " + str(indent_true))
        
    print("----3-----"+'\n')
    print("Title : " + str(title_h1.contents[0]))
    for span_elt in only_contents.contents:
        elt = str(span_elt)
        if elt.startswith('Part'):
            elt = '  ' + elt
            indent_true = False
        else:
            elt = '    ' + elt
            indent_true = True 
        # print ("Indentation: " + str(indent_true))
        print(elt.replace('<br/>', '\n'), end='')
    print("\n----4-----"+'\n') 
    
    print("----END-----"+'\n')
