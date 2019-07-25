def dict_maker(n):
    dic={}
    for i in range(n):
        man=(input()).split(':')
        dic[man[0]]=list(map(lambda x: x.lstrip(),man[1:][0].split(',')))
    return dic

def pair_maker(pref_m,pref_w, m_d,w_d):
    while '' in m_d.values():
        for man in m_d:
            if m_d[man]=='':
                for woman in pref_m[man]:
                    if w_d[woman]=='':
                        m_d[man]=woman
                        w_d[woman]=man
                        break
                    else:
                        present,potential=0,0
                        for candidate,n in enumerate(pref_w[woman]):
                            if candidate==w_d[woman]:
                                present=n
                            if candidate==man:
                                potential=n
                        if present>potential:
                            m_d[present]=''
                            w_d[woman]=man
                            m_d[man]=woman
    return m_d,w_d


m_d,w_d={},{}
list_men=input().split(", ")
list_women=input().split(", ")
pref_m=dict_maker(10)
pref_w=dict_maker(10)
for i in list_men:
    m_d[i]=''
for i in list_women:
    w_d[i]=''

#code is modified


    
                                
                
        
        
    
