Rem Attribute VBA_ModuleType=VBAModule
Option VBASupport 1
Sub FinishHim()
    Dim x As Integer
    Dim columns
    columns = Array("C", "D", "E", "F", "G", "H", "I")
    For x = 1 To Sheets.Count Step 1
        Sheets(x).Activate
        Dim length As Integer
        Dim Report As Worksheet
        Set Report = Excel.ActiveSheet
        length = ActiveSheet.UsedRange.Rows.Count - 5
        Dim y As Integer
        For y = 0 To 6 Step 1
            Sheets(x).Range(columns(y) & length + 6).Value = Excel.WorksheetFunction.Sum(Sheets(x).Range(columns(y) & "6" & ":" & columns(y) & (5 + length)))
        Next
    Next
End Sub
