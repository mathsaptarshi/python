def binarySearch(l,val):
  BEG=0
  END=len(l)
  MID=int((BEG + END)/2)
  while BEG <= END and l[MID] != val:
    if val < l[MID]:
      END = MID - 1
    else:
      BEG = MID +1
    MID=int((BEG + END)/2)
    #if l[MID] == val:
      #print("value found at ",MID)
  if l[MID] == val:
    LOC = MID
  else:
    LOC = None
  print("LOC = ",LOC)
  print(li)

  
li = [1,2,3,44,12,13,14,15,16,17,18]
binarySearch(li,12)