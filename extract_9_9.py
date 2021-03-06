from bs4 import BeautifulSoup #as Soup
import os

##import soupselect_bs4; soupselect_bs4.monkeypatch()
import urllib.request

###soup = BeautifulSoup(urllib.request.urlopen('http://slashdot.org/')) #Soup()
##select(soup, 'div#firehoselist > article > h2.story > span.story-title a')
##soup.findSelect('h2.story span a')

for i in range(5):
    file_name = 'sample'+str(18757665+i)+'.htm'
    try: 
        file_size_bytes = os.stat(file_name).st_size
    except FileNotFoundError as e: 
        #print(str(e))
        print("파일 없음")
    else:
        if file_size_bytes < 1030 :
            continue
        with open(file_name) as f:
            indent_init = 0
            indent_true = False

            soup = BeautifulSoup(f.read())  #Soup()

            yes_wrap = soup.select('div#yesWrap')[0]
            wrapper_content = yes_wrap.select('div#wrapperContent')[0]
            
            title_div = wrapper_content.select('div#title')[0] #1.제목든div##
            
            media_kind = title_div.select('span.rkeyL')[0]            
            book_or_not = media_kind.contents[0]

            author_anchor = title_div.select('p > a')[0]
            author_name = author_anchor.contents[0]
            translator_anchor = title_div.select('p > a')[1]
            translator_name = translator_anchor.contents[0]
            press_anchor = title_div.select('p > a')[2]
            press_name = press_anchor.contents[0]
            originalB_anchor = title_div.select('p > a')[3]
            originalB__name = originalB_anchor.contents[0]

            book_salsInfo_div = wrapper_content.select('div#salsInfo')[0]
            book_timespace_dd = book_salsInfo_div.select('dd.pdDate')
            #print(book_timespace_dd[0])
            #print(book_timespace_dd[0].contents)
            book_birthdate = book_timespace_dd[0].select('p')[0].contents[0]
            #    print(book_birthdate) 
            book_space_dim = book_timespace_dd[0].find_all('p')[1].contents[0].strip()
            #    print(book_space_dim)
            
            print(book_or_not)

            if book_or_not == '도서':
                interim_div = wrapper_content.select('div#contents')[0] #a1.책소개든div##

                goods_book_detail_div = wrapper_content.select('div.detailGoodsBasic')[0]
                goods_book_prices_info = goods_book_detail_div.select('td')
                print()
                print(goods_book_prices_info)
                print()
                #intro_p0 = interim_div.select('div.communityHide') 
                #print(intro_p0)
                intro_p0 = interim_div.select('td')[0].contents #old: .find_all

                ##new_chosen_div = wrapper_content.select('div#contents > div')[1]
                ##last_chosen_paragraphs = new_chosen_div('p')
                #print(last_chosen_paragraphs)
                ##for p_elt in last_chosen_paragraphs:
                ##    print(p_elt.contents[0].strip())

                print("----책 정보 요약 BEGIN----")
                #print("---Beginning of *.----")
                #print(next_interim_div)
                #print("---End of Book *.----")
                
                #intro_p0 = next_interim_div.select('td')[0]
                
                title_h1 = title_div.select('h1 > a')[0] #2.제목든div 속의 것##

                authors_transl_press_a_s = title_div.select('p > a')
                print(authors_transl_press_a_s)
                authors = authors_transl_press_a_s[0].contents[0]
                transl = authors_transl_press_a_s[1].contents[0]
                press = authors_transl_press_a_s[2].contents[0]
                #a2.책소개든div  속의 것##
                
                print("파일명 : " + file_name)
                print("책 제목 : " + str(title_h1.contents[0])) #3.제목 든 것 끄집어냄##
                print("출간일 : "+ book_birthdate)
                
                print("저자 : " + authors)
                print("역자 : "+transl)
                print("출판사 : "+press)
                print()
                #  print("---Beginning of Book Intro.----")
                print("[ 책 소개 ]")
                #print(intro_p0)
                #if (  len(intro_p) > 0 )
                #    for raw_p in intro_p
                #      p_elt = str(raw_p)
                #      print(p_elt)
                

                ###print(intro_p0)
                tmp_str = ""
                for raw_elt in intro_p0 :
                    elt = str(raw_elt)
                    if elt.startswith('<iframe '):
                        continue
                    else:
                        #print('    ' + elt.replace('<br/>', '\n'), end='')
                        elt = elt.replace('\n', ' ')
                        tmp_str = tmp_str + elt.replace('<br/>', '\n')
                print(tmp_str.strip())
                #   next_interim_div = interim_div.select("div + div + div h2 + p")[0]
                #   print("---End of Book Intro.----")

                #print("출간일 : "+book_birthdate)
                
                print()
                print("책외형 : "+book_space_dim) 
                if soup.select('p#contents_constitution_text0'):            
                    chapters = soup.select('p#contents_constitution_text0')[0]
                    only_contents = chapters.select('span.more_contents')[0]
                    #print  ("----1-----"+'\n')
                    #print(str(only_contents.contents))
                    #print("----2-----"+'\n')
                    #print(str(only_contents.contents).replace('<br/>', '\n'))
                    for raw_elt in only_contents.contents :
                        elt = str(raw_elt)
                        if elt.startswith('Part'):
                            indent_init += 1
                            indent_true = False
                        else:
                            indent_true = True 
                        #print ("Indentation: " + str(indent_true))
                        
                    #print("----3-----"+'\n')
                    #print("Title : " + str(title_h1.contents[0]))
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
                else:
                    print("...목차없음...")
                print("----책 정보 요약 END-----"+'\n')
            else:
                print("책이 아님...")
                print(book_or_not+"임")
            f.close()
