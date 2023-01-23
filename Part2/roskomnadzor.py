'''Роскомнадзор запретил букву
'''

def cenzor(txt, sim):
    if sim in txt:
        return txt.replace(sim, '')
    else:
        return txt

txt = input() + ' запретил букву'
for i in range(1072, 1104):
    if chr(i) in txt:
        print(txt.strip().replace('  ', ' ') + ' ' + chr(i))
    txt_new = cenzor(txt, chr(i))
    if txt_new != txt:
        txt = txt_new