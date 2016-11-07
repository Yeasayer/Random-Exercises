Rem Attribute VBA_ModuleType=VBAModule
Option VBASupport 1
Sub White()

    Dim namearr()
    Dim strPattern As String: strPattern = "\*"
    Dim strReplace As String: strReplace = ""
    Dim regEx As New RegExp
    Dim strInput As String
    Dim Myrange As Range
    Dim Count As Integer
    Count = 0

    Set Myrange = ActiveSheet.Range("B6:B1380")
    
    For Each cell In Myrange
        If strPattern <> "" Then
            strInput = cell.Value
            
            With regEx
                .Global = True
                .Pattern = strPattern
            End With
            
            If regEx.Test(strInput) Then
                cell.Value = regEx.Replace(strInput, strReplace)
                Count = Count + 1
            End If
        End If
    Next
    MsgBox "We've Found " & Count & " Instances of an Asterik!"
End Sub
