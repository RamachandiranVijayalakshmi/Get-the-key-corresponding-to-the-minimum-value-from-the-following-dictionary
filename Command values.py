sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(min(sampleDict, key=sampleDict.get))
