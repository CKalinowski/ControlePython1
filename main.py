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
def verifTLD(tldOK, tld):
  if tld in tldOK :
    return True
  else : 
    return False

###### exercice 05
def ipVerifFormat (adresseIp) :

  if(adresseIp.count('.') != 3):
    print('nombre de champs incorrect')
    return False
  else :
    nb = adresseIp.split('.')

    if((int(nb[0]) >= 0 and int(nb[0]) <= 255) and (int(nb[1]) >= 0 and int(nb[1]) <= 255) and (int(nb[2]) >= 0 and int(nb[2]) <= 255) and (int(nb[2]) >= 0 and int(nb[2]) <= 255) and (int(nb[3]) >= 0 and int(nb[3]) <= 255)) :
      return True
    else : 
      print('champ d’adresse incorrect')
      return False

###### exercice 06
def makeTLD(dico):
  listeTld = []
  nbLigne = 0

  for url in dico:
    tld = url.split(",")[0]
    tld = tld.split(".")[1]

    if tld not in listeTld:
      listeTld.append(tld)
      nbLigne += 1

  print("Creation d'une liste de TLD comprenant "+ str(nbLigne) +" entrees")
  return listeTld

# Zone 2 ## zone pour les classes
###### exercice 07
class serveurDNS:
  def __init__(self, resolDns):
    self.resolDns = resolDns

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
  result = ipVerifFormat ('192.168.1.290') # result de type booléen True/False,adresseIp de type String

  ###### exercice 06
  print("exercice 06 #######################")
  tldOk = makeTLD (resolDns)# tldOk de type liste, dico de type dictionnaire
  print(tldOk)


  # Zone 4 ## zone pour les tests de la classe

  ###### exercice 07
  print("exercice 07 #######################")
  s = serveurDNS (resolDns)# s de type serveurDns, resolDns de type dictionnaire
  print(type(s))

  ###### exercice 08
  print("exercice 08 #######################")
  #adresseIp = s.resolDNS(url)#adresseIp de type String, url de type String

  ###### exercice 09
  print("exercice 09 #######################")

  ###### exercice 10
  print("exercice 10 #######################")

if __name__=="__main__":
    print("main()")
    main()