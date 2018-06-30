
import sys 
def mimi( ms , indx = 0 ):
    """ str -> str
"""
    #caracteres especiales
    #que -> qui (la u no te la puede transformar )
    #c[aou] -> qui
    #g[aeou] -> gui
    # estos casos han sido generados con un for de antemano
    esp = [ ["que" , "qui"] , ['ca', 'qui'], ['co', 'qui'], ['cu', 'qui'],['ga', 'gui'], ['ge', 'gui'], ['go', 'gui'], ['gu', 'gui'], 
                ['QUE', 'QUI'], ['CA', 'QUI'], ['CO', 'QUI'], ['CU', 'QUI'], ['GA', 'GUI'], ['GE', 'GUI'], ['GO', 'GUI'], ['GU', 'GUI']] 
    i = 0
    while i < len(esp):
        ind = ms.find( esp[i][0])
        if ind != -1:
            return mimi( ms[0:ind] , indx+1) + esp[i][1] + mimi(ms[ind+len(esp[i][0]):] , indx)
        else:
            i += 1
    return mimi_normal( ms[0:])
    
            

def mimi_normal (ms):
    """ str -> stryt
"""
    #Letras a reemplazar y su remplazamiento
    cadena = [ ["aeou" , "i"] , ["aeou".upper() , "I"] , [ "áéóú" , "í"]  , ["áéóú".upper() , "I" ] ]

    for cad in cadena:
        for vocal in cad[0]:
            ms = ms.replace(vocal , cad[1])
    return ms

if __name__ == '__main__':
    print(sys.argv[1])
    print(mimi(sys.argv[1]))
