import csv
import plotly
import plotly.graph_objs as go

with open('dataTestCW.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    xtest= []
    yt = []
    yh =[]
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            for col in row:
                print("column name %s"%(col))
            line_count += 1
        else:
            print("Date %s, temp %s, humidity %s"%(row[0], row[1], row[2]))
            line_count += 1
            xtest.append(line_count+1)
            yt.append(row[1])
            yh.append(row[2])

trace = go.Scatter(x=xtest,y=yt,name='Temperature (degrees C)',line=dict(color=('rgb(255,0,0)')))
trace1 = go.Scatter(x=xtest,y=yh,name='Humidity (%)',line=dict(color=('rgb(0,255,0)')))
data=[trace,trace1]

layout = dict(title='Weekly Building Analytics',
  xaxis=dict(title='Time'),
  yaxis = dict(title='Temperature (degrees C)'),)
fig = dict(data=data,layout=layout)
filename = input("Save filename as: ")
plotly.offline.plot(fig,filename=filename+".html")
            
