#Activex_export_data.py

#This code sets up Excel as a COM server and writes data onto the file specified
#(at this moment, the file has to already exist!)

#Shogo Minakata, sm34g11@soton.ac.uk, Created 12 Nov 2014

import win32com.client
import pythoncom
import os

cwd = os.getcwd() #Find out current working directory
#filename = 'TestResults.xlsx'     #NOPE, excel file name is defined in Test_find_L_over_D.py

Excel = win32com.client.Dispatch("Excel.Application")
Excel.Visible = 1     #1 to make Excel visible, 0 to make it invisible. Default is 0.
Excel.DisplayAlerts = False     #False to suppress warning dialogue. True to unsuppress. Default is True.

#Workbook = Excel.Workbooks.Open(r"E:\Dropbox\Academic\Pt.4 GDP\Temp\Mytest.xlsx")    #Opening existing workbook
Workbook = Excel.Workbooks.Add()     #Open a new workbook


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

#Workbook.Save()   #Equivalent to a simple 'Save'. Only use if opening existing file
Workbook.SaveAs(cwd+'\\'+resultfilename)    #Saves workbook in cwd with filename specified
Workbook.Close()
Excel.Quit()

#EXTRA-------------------------
#Reference websites used...
#http://stackoverflow.com/questions/1065844/what-can-you-do-with-com-activex-in-python
#http://stackoverflow.com/questions/3373955/python-and-excel-overwriting-an-existing-file-always-prompts-despite-xlsavecon
#http://d.hatena.ne.jp/Wacky/20060412/1144850587
