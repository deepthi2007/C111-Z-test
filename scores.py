import pandas as pd
import plotly.figure_factory as pf
import plotly.graph_objects as pg
import statistics as st
import random as rn

df = pd.read_csv("School1.csv")
mainData = df["Math_score"].tolist()
mainMean = st.mean(mainData)
mainStdev = st.stdev(mainData)
print("Mean ->",mainMean)
print("StDev -> ", mainStdev)


def randSamples(size):
    sampleData = []
    for i in range(0,100):
        randNo = rn.randint(0,len(mainData)-1)
        sampleData.append(mainData[randNo])
    samplemean = st.mean(sampleData)
    return samplemean

def setup():
    sampleMeans = []
    for i in range(0,1000):
        randommeans = randSamples(100)
        sampleMeans.append(randommeans)
    return sampleMeans

means = setup()
samplingMean = st.mean(means)
samplingStDev = st.stdev(means)
print("Sampling-mean -> ",samplingMean)
print("Sampling-stdev -> ",samplingStDev)

firstStDevStart , firstStDevEnd = samplingMean-samplingStDev,samplingMean+samplingStDev
secondStDevStart , secondStDevEnd = samplingMean-(samplingStDev*2),samplingMean+(samplingStDev*2)
thridStDevStart , thridStDevEnd = samplingMean-(samplingStDev*3),samplingMean+(samplingStDev*3)

""" Calculate sample mean for the students who got extra material (D:\deepthi projects\C111\School_1_Sample.csv) """
""" df1 = pd.read_csv("D:\deepthi projects\C111\School_1_Sample.csv")
mainData1 = df1["Math_score"].tolist()
meanOfSample1 = st.mean(mainData1)
print("mean of sample 1 : ",meanOfSample1) """

""" Calculate sample mean for the students who got workshops (D:\deepthi projects\C111\School_2_Sample.csv) """
df2 = pd.read_csv("D:\deepthi projects\C111\School_2_Sample.csv")
mainData2 = df2["Math_score"].tolist()
meanOfSample2 = st.mean(mainData2)
print("mean of sample 2 : ",meanOfSample2)
zScore = (samplingMean-meanOfSample2)/samplingStDev
print("Zscore -> ",zScore)


""" Calculate the mean for student who got technoly for teaching in classroom (D:\deepthi projects\C111\School_3_Sample.csv)"""
""" df3 = pd.read_csv("D:\deepthi projects\C111\School_1_Sample.csv")
mainData3 = df3["Math_score"].tolist()
meanOfSample3 = st.mean(mainData3)
print("mean of sample 3 : ",meanOfSample3)
 """
fig = pf.create_distplot([means],["sampling mean scores"],show_hist=False)
fig.add_trace(pg.Scatter(x=[samplingMean,samplingMean],y=[0,1],mode="lines",name="Mean"))
""" fig.add_trace(pg.Scatter(x=[meanOfSample1,meanOfSample1],y=[0,1],mode="lines",name="Mean of sample 1")) """
fig.add_trace(pg.Scatter(x=[meanOfSample2,meanOfSample2],y=[0,1],mode="lines",name="Mean of sample 2"))
""" fig.add_trace(pg.Scatter(x=[meanOfSample3,meanOfSample3],y=[0,1],mode="lines",name="Mean of sample 3")) """
fig.add_trace(pg.Scatter(x=[firstStDevStart,firstStDevStart],y=[0,1],mode="lines",name="St dev 1"))
fig.add_trace(pg.Scatter(x=[firstStDevEnd,firstStDevEnd],y=[0,1],mode="lines",name="St dev 1"))
fig.add_trace(pg.Scatter(x=[secondStDevStart,secondStDevStart],y=[0,1],mode="lines",name="St dev 2"))
fig.add_trace(pg.Scatter(x=[secondStDevEnd,secondStDevEnd],y=[0,1],mode="lines",name="St dev 2"))
fig.add_trace(pg.Scatter(x=[thridStDevStart,thridStDevStart],y=[0,1],mode="lines",name="St dev 3"))
fig.add_trace(pg.Scatter(x=[thridStDevEnd,thridStDevEnd],y=[0,1],mode="lines",name="St dev 3"))
fig.show()
