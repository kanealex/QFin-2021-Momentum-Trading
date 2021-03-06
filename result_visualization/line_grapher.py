import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("results_overnight_kane.csv")

df2 = df.groupby("Strategy_Name")

tograph = "standard_no_volume"

optimization  = pd.DataFrame()
for a, b in df.groupby(["Strategy_Name","Coin"]):
    if(a[0] =='standard_no_volume' and tograph == 'standard_no_volume'):
        value = pd.DataFrame()
        value["y-axis"] = b["Strategy"]- b["Buy and Hold"]
        value["x-axis"] = b["Price_Window"]
        optimization[str(a[1])] = value["y-axis"]
        optimization[str(a[1])+ "variable"] = value["x-axis"]
        optimization.to_csv("results.csv")
        plt.plot(value["x-axis"].values.tolist(), value["y-axis"].values.tolist(), label = str(a[1]))
        plt.xlabel('Price Window')
        plt.ylabel('Percentage Improvement on Buy and Hold')
        plt.title('% Profit on Buy and Hold for SMA No Volume Algorithm')
        # plt.legend()
    if(a[0] =='standard' and tograph == 'standard_price'):
        yaxis = []
        xaxis = []
        for e,c in b.groupby(["Volume_Window"]):
            value = pd.DataFrame()
            value["y-axis"] = c["Strategy"] - c["Buy and Hold"]
            xaxis = c["Price_Window"].values.tolist()
            yaxis.append(value["y-axis"].values.tolist())
        arrays = [np.array(x) for x in yaxis]
        result = [np.mean(k) for k in zip(*arrays)]
        plt.plot(xaxis, result, label = "Volume window: "+str(a[1]))
        plt.xlabel('Price Window')
        plt.ylabel('Percentage Improvement on Buy and Hold')
        plt.title('% Profit on Buy and Hold for SMA Algorithm')
        # plt.legend()
    if(a[0] =='standard' and tograph == 'standard_volume'):
        yaxis = []
        xaxis = []
        for e,c in b.groupby(["Price_Window"]):
            value = pd.DataFrame()
            value["y-axis"] = c["Strategy"] - c["Buy and Hold"]
            xaxis = c["Volume_Window"].values.tolist()
            yaxis.append(value["y-axis"].values.tolist())
        arrays = [np.array(x) for x in yaxis]
        result = [np.mean(k) for k in zip(*arrays)]
        plt.plot(xaxis, result, label = "Price window: "+str(a[1]))
        plt.xlabel('Volume Window')
        plt.ylabel('Percentage Improvement on Buy and Hold')
        plt.title('% Profit on Buy and Hold for SMA Algorithm')
        # plt.legend()
    if(a[0] =='exp_no_volume' and tograph == 'exp_no_volume'):
        value = pd.DataFrame()
        value["y-axis"] = b["Strategy"] - b["Buy and Hold"]
        value["x-axis"] = b["Price_Window"]
        print(value)
        value.to_csv("results.csv")
        plt.plot(value["x-axis"].values.tolist(), value["y-axis"].values.tolist(), label = str(a[1]))
        plt.xlabel('Price Window')
        plt.ylabel('Percentage improvement on Buy and Hold')
        plt.title('% Profit on Buy and Hold for EMA No Volume Algorithm')
        # plt.legend()
    if(a[0] =='Crossover moving average' and tograph == 'Crossover moving average long'):
        yaxis = []
        xaxis = []
        for e,c in b.groupby(["Long_Price_Window"]):
            value = pd.DataFrame()
            value["y-axis"] = c["Strategy"] - c["Buy and Hold"]
            xaxis = c["Price_Window"].values.tolist()
            yaxis.append(value["y-axis"].values.tolist())
        arrays = [np.array(x) for x in yaxis]
        result = [np.mean(k) for k in zip(*arrays)]
        plt.plot(xaxis, result, label = "Volume window: "+str(a[1]))
        plt.xlabel('Short Price Window')
        plt.ylabel('Percentage Improvement on Buy and Hold')
        plt.title('% Profit on Buy and Hold for Crossover Algorithm')
        # plt.legend()
    if(a[0] =='Crossover moving average' and tograph == 'Crossover moving average short'):
        yaxis = []
        xaxis = []
        for e,c in b.groupby(["Price_Window"]):
            value = pd.DataFrame()
            value["y-axis"] = c["Strategy"] - c["Buy and Hold"]
            xaxis = c["Long_Price_Window"].values.tolist()
            yaxis.append(value["y-axis"].values.tolist())
        arrays = [np.array(x) for x in yaxis]
        result = [np.mean(k) for k in zip(*arrays)]
        plt.plot(xaxis, result, label = "Price window: "+str(a[1]))
        plt.xlabel('Long Price Window')
        plt.ylabel('Percentage Improvement on Buy and Hold')
        plt.title('% Profit on Buy and Hold for Crossover Algorithm')
        # plt.legend()
plt.show()
