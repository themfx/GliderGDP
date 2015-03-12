#testing active x capability in python

import win32com.client
import pythoncom
import os

Excel = win32com.client.Dispatch("Excel.Application")
Excel.Visible = 1

#cwd = os.getcwd() #For when the code can specify locations

Workbook = Excel.Workbooks.Open(r"E:\Dropbox\Academic\Pt.4 GDP\Temp\Mytest.xlsx")

for n in range(len(velocity_inputs)):
    Workbook.ActiveSheet.Cells(1,1+10*n).Value = "Velocity = " + str(velocity_inputs[n])
    Workbook.ActiveSheet.Cells(2,1+10*n).Value = "Time"
    Workbook.ActiveSheet.Cells(2,2+10*n).Value = "Latitude"
    Workbook.ActiveSheet.Cells(2,3+10*n).Value = "Longitude"
    Workbook.ActiveSheet.Cells(2,4+10*n).Value = "Altitude"
    Workbook.ActiveSheet.Cells(2,5+10*n).Value = "Distance"
    Workbook.ActiveSheet.Cells(2,6+10*n).Value = "Airspeed"
    Workbook.ActiveSheet.Cells(2,7+10*n).Value = "gz"
    Workbook.ActiveSheet.Cells(2,8+10*n).Value = "Wind Direction"
    Workbook.ActiveSheet.Cells(2,9+10*n).Value = "Wind Velocity"
    for m in range(datalength):
        m = m+3 #+3 to compensate for velocity label text and the fact python indexing (start with 0)
        Workbook.ActiveSheet.Cells(m+1,1+10*n).Value = times[n][m-3]
        Workbook.ActiveSheet.Cells(m+1,2+10*n).Value = latitude[n][m-3]
        Workbook.ActiveSheet.Cells(m+1,3+10*n).Value = longitude[n][m-3]
        Workbook.ActiveSheet.Cells(m+1,4+10*n).Value = altitude[n][m-3]
        Workbook.ActiveSheet.Cells(m+1,5+10*n).Value = distance[n][m-3]
        Workbook.ActiveSheet.Cells(m+1,6+10*n).Value = airspeed[n][m-3]
        Workbook.ActiveSheet.Cells(m+1,7+10*n).Value = gz[n][m-3]
        Workbook.ActiveSheet.Cells(m+1,8+10*n).Value = winddir[n][m-3]
        Workbook.ActiveSheet.Cells(m+1,9+10*n).Value = windvel[n][m-3]

Workbook.Save()
Workbook.Close()
Excel.Quit()

