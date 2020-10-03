Attribute VB_Name = "Module1"
Sub Stock():

' Global Variable Declaration
Dim Ticker As String
Dim Volume As Double
Dim YChange As Double ' Change during the Year
Dim LRow As Long 'Last Row
Dim RValue As Integer
Dim SOpen As Double 'Stock Opening Price
Dim PChange As Double ' Percentage Change


For Each ws In Worksheets

' Creating the new Column in the Sheet
ws.Range("I1") = "Ticker"
ws.Range("J1") = "Yearly Change"
ws.Range("K1") = "Percent Change"
ws.Range("L1") = "Total Stock Volume"
ws.Range("O2") = "Greatest % Increase"
ws.Range("O3") = "Greatest % Decrease"
ws.Range("O4") = "Greatest Total Volume"
ws.Range("P1") = "Ticker"
ws.Range("Q1") = "Value"

'Last Row of the sheet
LRow = ws.Cells(Rows.Count, 1).End(xlUp).Row

Volume = 0
RValue = 2

For i = 2 To LRow
If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
    Ticker = ws.Cells(i, 1).Value
    Volume = Volume + ws.Cells(i, 7).Value
    YChange = ws.Cells(i, 6).Value - SOpen
    
    If SOpen = 0 Then
        PChange = 0
    Else:
        PChange = YChange / SOpen
    End If

' Yearly & Percentage Change for each Ticker
ws.Range("I" & RValue).Value = Ticker
ws.Range("L" & RValue).Value = Volume

Volume = 0

ws.Range("J" & RValue).Value = YChange
ws.Range("K" & RValue).Value = PChange
ws.Range("K" & RValue).Style = "Percent"
ws.Range("K" & RValue).NumberFormat = "0.00%"


RValue = RValue + 1
'Volume Calculation
ElseIf ws.Cells(i - 1, 1).Value <> ws.Cells(i, 1).Value Then
    SOpen = ws.Cells(i, 3).Value
    Volume = Volume + ws.Cells(i, 7).Value

Else: Volume = Volume + ws.Cells(i, 7).Value
End If

Next i

' Highlighting the Positive Change and Negative Change Green and Red
For i = 2 To LRow
    If ws.Range("J" & i).Value > 0 Then
        ws.Range("J" & i).Interior.ColorIndex = 4
    ElseIf ws.Range("J" & i).Value < 0 Then
        ws.Range("J" & i).Interior.ColorIndex = 3
    End If
Next i

'Calculation of Greatest Increase, Decrease and Volume
Dim GIncrease As Double
Dim GDecrease As Double
Dim GVolume As Double

GIncrease = 0
GDecrease = 0
GVolume = 0

'Calculation of Greatest Increase
For a = 2 To LRow
    If ws.Cells(a, 11).Value > GIncrease Then
        GIncrease = ws.Cells(a, 11).Value
        ws.Range("Q2").Value = GIncrease
        ws.Range("Q2").Style = "Percent"
        ws.Range("Q2").NumberFormat = "0.00%"
        ws.Range("P2").Value = ws.Cells(a, 9).Value
    End If
Next a

'Calculation of Greatest Decrease
For b = 2 To LRow
    If ws.Cells(b, 11).Value < GDecrease Then
        GDecrease = ws.Cells(b, 11).Value
        ws.Range("P3").Value = ws.Cells(b, 9).Value
    End If
Next b

    ws.Range("Q3").Value = GDecrease
    ws.Range("Q3").Style = "Percent"
    ws.Range("Q3").NumberFormat = "0.00%"
    
'Calculation of Greatest Volume
For c = 2 To LRow
    If ws.Cells(c, 12).Value > GVolume Then
        GVolume = ws.Cells(c, 12).Value
        ws.Range("Q4").Value = GVolume
        ws.Range("P4").Value = ws.Cells(c, 9).Value
        
    End If
Next c

ws.Columns("A:Q").AutoFit
Next ws
End Sub

