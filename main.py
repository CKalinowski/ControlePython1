# Zone 1 ## zone pour les fonctions
# exercice 00 (la fonction est definie dans cette zone)
def exempleHello (msg):
  return "bonjour {}, comment allez-vous ?".format(msg)

###### exercice 01
def makeDico (fichier, chaine):
  dico = {}
  nbLigne = 0
  with open(fichier) as f:
    for line in f:
      (key, val) = line.split(chaine)
      dico[key] = val
      nbLigne += 1

  print("Creation d'un dictionnaire a partir du fichier "+ fichier +" avec '"+ str(nbLigne) +"' entrees")
  return(dico)


###### exercice 02
def verifUrl(url):
  url = url.split('.')

  if(len(url) == 2 and len(url[1]) == 3):
    return True
  else :
    return False

###### exercice 03
def getTLD(url):

  testUrl = verifUrl(url)

  if (testUrl == True) :
    tld = url.split('.')
    return (tld[1])
  else :
    return ('TLD mal formee') 

###### exercice 04
def verifTLD(liste, chaine):
  if chaine in liste :
    return True
  else : 
    return False

###### exercice 05


###### exercice 06


# Zone 2 ## zone pour les classes
###### exercice 07


###### exercice 08


###### exercice 09


# Zone 3 ## zone pour les tests des fonctions

def main() :
  from re import split
  ###### exercice 00 (la fonction est appelee dans cette zone afin de confirmer son fonctionnement)
  print("exercice 00 #######################")
  salutations = exempleHello("Michel")
  print(salutations)
  print(salutations.split(sep=" "))

  ###### exercice 01
  print("exercice 01 #######################")
  resolDns = makeDico ('dns.txt', ',')
  print(resolDns)

  ###### exercice 02
  print("exercice 02 #######################")
  result = verifUrl ('Wikipedia.org') # result de type booléen True/False, url de type String
  print(result)
  ###### exercice 03
  print("exercice 03 #######################")
  result = getTLD ('Wikipedia.org')# result de type String, url de type string
  print(result)

  ###### exercice 04
  print("exercice 04 #######################")
  tldOK = ['fr', 'com', 'net']
  result = verifTLD (tldOK ,'tld') # result de type booléen True/False, tldOk de type liste, tld de type String
  print(result)

  ###### exercice 05
  print("exercice 05 #######################")


  ###### exercice 06
  print("exercice 06 #######################")

  # Zone 4 ## zone pour les tests de la classe

  ###### exercice 07
  print("exercice 07 #######################")


  ###### exercice 08
  print("exercice 08 #######################")


  ###### exercice 09
  print("exercice 09 #######################")

  ###### exercice 10
  print("exercice 10 #######################")

if __name__=="__main__":
    print("main()")
    main()