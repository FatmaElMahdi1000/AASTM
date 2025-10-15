def extractor(FileName):
    idx = FileName.find('.')
    return FileName[idx + 1:]



FileName = input("Enter file name: ")
Result = extractor(FileName)
print(Result)