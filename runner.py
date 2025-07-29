from src.be.getDataFrame import getDataFrame
from src.be.runScan import runScan

df = getDataFrame()

runScan(df)

print(df)