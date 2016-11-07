Rem Attribute VBA_ModuleType=VBAModule
Option VBASupport 1
Sub MoveEm()

    Dim arr()
    
    Dim coolarr(1)
    Dim selection As Range
    Dim strName As String
    Dim Myrange As Range
    Dim flip As String
    Dim rangeA As Range, rangeB As Range, comRange As Range
    Set rangeA = Sheets("Payroll Summary").Range("A1:J5")
    Dim i As Integer, j As Integer, sheetC As Integer, startPart As Integer
    i = 0
    ReDim arr(i)
    Set Myrange = Worksheets("Payroll Summary").Range("B6:B1381")
    For Each cell In Myrange
        
        coolarr(0) = cell.Value
        coolarr(1) = cell.Row
        arr(i) = coolarr()
        i = i + 1
        ReDim Preserve arr(i)
    Next
    flip = arr(0)(0)
    startPart = arr(0)(1)
    sheetC = 1
    i = i - 1
    For j = 0 To i Step 1
        If flip <> arr(j)(0) Then
            flip = arr(j)(0)
            Dim sheetName As String
            Worksheets("Payroll Summary").Activate
            Set rangeB = Sheets("Payroll Summary").Range(Cells(startPart, 1), Cells(arr(j - 1)(1), 10))
            Set comRange = Union(rangeA, rangeB)
            comRange.Copy
            sheetName = "Worker #" & sheetC
            'MsgBox sheetName
            Sheets.Add.Name = sheetName
            MsgBox comRange.Rows.Count
            Sheets(sheetName).Range("A1").Resize(comRange.Rows.Count, comRange.columns.Count).Select
            Sheets(sheetName).Paste
            sheetC = sheetC + 1
            startPart = arr(j)(1)
        End If
    Next
End Sub
