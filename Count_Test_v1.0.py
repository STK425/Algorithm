import WordsCount as WC
import time

path = "F:\\VS_Projects\\PythonApplication1\\data.csv"

def get_data():
    data = []
    f = open(path, "r")
    for line in f:
        data.append(line.split(","))
    f.close()
    return data

start = time.perf_counter()
WC.InfoSet_Comput(get_data())
end = time.perf_counter()
print(end - start)

print(WC.get_TopTenInfo())

print(WC.get_30DaysInfo("山东大学"))

print(WC.get_12MonthsInfo("山东大学"))

print(WC.get_10YearsInfo("山东大学"))
