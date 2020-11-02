import subprocess, sys
nameSpace = "miniudm"
cmdTypes = [ "serviceaccounts" ,"service" , "rolebinding" ,"roles","jobs", "pvc" ,"configmap","secret",  "statefulset"]

def deleteDataValidation(cmdType,tempItem, nameSpace ):
  try:
    deleteCmd = "kubectl delete "+ cmdType +" "+str(tempItem)+" -n "+ nameSpace
    generateStatement = str(cmdType) +" has found the resource ===> "+ str(tempItem) +" <=== and its deleted..."
    return generateStatement
  except Exception as ex:
        print(str(ex) + '\tLine No:' + str(sys.exc_info()[2].tb_lineno))
        
def dataValidations(tempList,keyWord):
  try:
    tempList = []
    if keyWord == "EmptyList":
      generateSatement = str(cmdType) +" has No resources found ... So Nothing to delete..."
      return generateSatement
    elif keyWord == "notEmptyList":
      for eachIndex, eachItem in enumerate(tempList):
        if not eachItem.startswith("default"):
          # Here we are skipping the default value and the remaining values need to be delete..
          tempData = deleteDataValidation(cmdType,eachItem, nameSpace)
          tempList.append(tempData)
      return tempList
  except Exception as ex:
        print(str(ex) + '\tLine No:' + str(sys.exc_info()[2].tb_lineno))

if __name__ == "__main__": 
  try:
    for index, cmdType in enumerate(cmdTypes):
      getCmd = "kubectl get "+ cmdType +" -n "+ nameSpace + "|awk '{if (NR!=1) print $1}'"
      direct_output = subprocess.check_output(getCmd, shell=True)
      direct_output = direct_output.split("\n")
      if direct_output == ['']:
        statement = dataValidations(direct_output, "EmptyList")
        print statement
      else:
        direct_output = direct_output[:-1]
        print "Total Resources Captured for  cmdType =>",(direct_output)
        statements = dataValidations(direct_output, "notEmptyList")
        for statement  in statements:
          print statement
      raw_input("****************************************************************")
  except Exception as ex:
        print(str(ex) + '\tLine No:' + str(sys.exc_info()[2].tb_lineno))
