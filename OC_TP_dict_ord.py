class DictionnaireOrdonne(dict):

    
    def __init__(self, base={}, **donnees):
       
        
        self._cles = [] 
        self._valeurs = [] 
        
        
    
      
        for cle in base:
            self[cle] = base[cle]
        
       
        for cle in donnees:
            self[cle] = donnees[cle]

dico1 = {'pomme':12,' ''poire':45}
print(dico1)

dico2 = DictionnaireOrdonne(dico1)
print(dico2)

dico3 = DictionnaireOrdonne()
dico3['guillaume']='POO'
print(dico3)

dico4 = DictionnaireOrdonne(fruits=3, legumes=8)
print(dico4)