# -*- coding: utf-8 -*-



def cigar_party(cigars, is_weekend):
  if cigars >= 40 and is_weekend == True:
      print("True") 
      return True
  elif cigars >= 40 and cigars <= 60:
      print("True")
      return True
  else: 
      print("False")
      return False

cigar_party(90, False)


#submission 1 - correct
#def cigar_party(cigars, is_weekend):
#  if cigars >= 40 and is_weekend == True:
#    return True
#  elif cigars >= 40 and cigars <= 60:
#    return True
#  else: 
#      return False