# Author: vizius.com
# Date: July 02, 2024
# Purpose: Macro to generate remediation plan in the Risk Analysis spreadsheet
# License: https://github.com/TheViziusGroup/BCF/blob/main/LICENSE

Sub UpdateRemPlanSheets()
    Dim wsRemPlanT1 As Worksheet
    Dim wsRemPlanT2 As Worksheet
    Dim wsRemPlanT3 As Worksheet
    Dim wsRemPlanUnranked As Worksheet
    Dim wsSystemData As Worksheet
    Dim wsTierValues As Worksheet
    Dim lastRow As Long
    Dim i As Long, j As Long
    Dim tierCol As Long
    Dim tierValuesRow As Long
    
    ' Set the worksheets
    Set wsRemPlanT1 = ThisWorkbook.Sheets("RemPlan-T1")
    Set wsRemPlanT2 = ThisWorkbook.Sheets("RemPlan-T2")
    Set wsRemPlanT3 = ThisWorkbook.Sheets("RemPlan-T3")
    Set wsRemPlanUnranked = ThisWorkbook.Sheets("RemPlan-Unranked")
    Set wsSystemData = ThisWorkbook.Sheets("System Data")
    Set wsTierValues = ThisWorkbook.Sheets("TIER Values")
    
    ' Find the last row in System Data sheet
    lastRow = wsSystemData.Cells(wsSystemData.Rows.Count, "A").End(xlUp).Row
    
    ' Loop through each row in System Data for RemPlan-T1
    For i = 3 To lastRow
        ' Loop through each column in RemPlan-T1
        For j = 1 To 17
            ' Determine the corresponding column in System Data and TIER Values
            Select Case j
                Case 1
                    tierCol = 5 ' Column E in System Data for Hardware Age
                    tierValuesRow = 3 ' Corresponding row in TIER Values for Hardware Age
                Case 2
                    tierCol = 7 ' Column G in System Data for Physical Security
                    tierValuesRow = 4 ' Corresponding row in TIER Values for Physical Security
                Case 3
                    tierCol = 9 ' Column I in System Data for Failover System
                    tierValuesRow = 5 ' Corresponding row in TIER Values for Failover System
                Case 4
                    tierCol = 11 ' Column K in System Data for Vulnerabilities
                    tierValuesRow = 6 ' Corresponding row in TIER Values for Vulnerabilities
                Case 5
                    tierCol = 13 ' Column M in System Data for Centralized Logging
                    tierValuesRow = 7 ' Corresponding row in TIER Values for Centralized Logging
                Case 6
                    tierCol = 15 ' Column O in System Data for Centralized Alerting
                    tierValuesRow = 8 ' Corresponding row in TIER Values for Centralized Alerting
                Case 7
                    tierCol = 17 ' Column Q in System Data for Priv Accounts
                    tierValuesRow = 9 ' Corresponding row in TIER Values for Priv Accounts
                Case 8
                    tierCol = 19 ' Column S in System Data for PW Audits
                    tierValuesRow = 10 ' Corresponding row in TIER Values for PW Audits
                Case 9
                    tierCol = 21 ' Column U in System Data for XDR
                    tierValuesRow = 11 ' Corresponding row in TIER Values for XDR
                Case 10
                    tierCol = 23 ' Column W in System Data for Network ACLs
                    tierValuesRow = 12 ' Corresponding row in TIER Values for Network ACLs
                Case 11
                    tierCol = 25 ' Column Y in System Data for Backup Frequency
                    tierValuesRow = 13 ' Corresponding row in TIER Values for Backup Frequency
                Case 12
                    tierCol = 27 ' Column AA in System Data for Network Isolation for Backups
                    tierValuesRow = 14 ' Corresponding row in TIER Values for Network Isolation for Backups
                Case 13
                    tierCol = 29 ' Column AC in System Data for Auth Isolation for Backups
                    tierValuesRow = 15 ' Corresponding row in TIER Values for Auth Isolation for Backups
                Case 14
                    tierCol = 31 ' Column AE in System Data for Backup Validation
                    tierValuesRow = 16 ' Corresponding row in TIER Values for Backup Validation
                Case 15
                    tierCol = 33 ' Column AG in System Data for Backup RTO Match
                    tierValuesRow = 17 ' Corresponding row in TIER Values for Backup RTO Match
                Case 16
                    tierCol = 35 ' Column AI in System Data for Change Management
                    tierValuesRow = 18 ' Corresponding row in TIER Values for Change Management
                Case 17
                    tierCol = 37 ' Column AK in System Data for Configuration Management
                    tierValuesRow = 19 ' Corresponding row in TIER Values for Configuration Management
            End Select
            
            ' Construct the formula for RemPlan-T1 sheet
            wsRemPlanT1.Cells(i, j).Formula = "=IF(AND('System Data'!$C$" & i & "=""Tier 1"", 'System Data'!" & Cells(i, tierCol).Address & ">'TIER Values'!C" & tierValuesRow & "), 'System Data'!$A$" & i & ", """")"
            
            ' Construct the formula for RemPlan-T2 sheet
            wsRemPlanT2.Cells(i, j).Formula = "=IF(AND('System Data'!$C$" & i & "=""Tier 2"", 'System Data'!" & Cells(i, tierCol).Address & ">'TIER Values'!E" & tierValuesRow & "), 'System Data'!$A$" & i & ", """")"
            
            ' Construct the formula for RemPlan-T3 sheet
            wsRemPlanT3.Cells(i, j).Formula = "=IF(AND('System Data'!$C$" & i & "=""Tier 3"", 'System Data'!" & Cells(i, tierCol).Address & ">'TIER Values'!G" & tierValuesRow & "), 'System Data'!$A$" & i & ", """")"
            
            ' Construct the formula for RemPlan-Unranked sheet
            wsRemPlanUnranked.Cells(i, j).Formula = "=IF(AND('System Data'!$C$" & i & "=""Unranked"", 'System Data'!" & Cells(i, tierCol).Address & ">'TIER Values'!I" & tierValuesRow & "), 'System Data'!$A$" & i & ", """")"
        Next j
    Next i
End Sub

