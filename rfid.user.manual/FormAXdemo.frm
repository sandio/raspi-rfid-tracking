VERSION 5.00
Object = "{9416F6A8-EC78-4674-B870-E16474FD10DE}#1.0#0"; "rfidx.ocx"
Begin VB.Form Form1 
   Caption         =   "RFID Demo V1.0.0"
   ClientHeight    =   3090
   ClientLeft      =   60
   ClientTop       =   450
   ClientWidth     =   5355
   LinkTopic       =   "Form1"
   ScaleHeight     =   3090
   ScaleWidth      =   5355
   StartUpPosition =   3  'Windows Default
   Begin VB.CommandButton Command2 
      Caption         =   "Stop"
      Height          =   495
      Left            =   3600
      TabIndex        =   5
      Top             =   840
      Width           =   1575
   End
   Begin VB.CommandButton Command1 
      Caption         =   "Start"
      Height          =   495
      Left            =   3600
      TabIndex        =   4
      Top             =   240
      Width           =   1575
   End
   Begin VB.TextBox nCommPort 
      Height          =   375
      Left            =   1200
      TabIndex        =   2
      Text            =   "1"
      Top             =   2400
      Width           =   975
   End
   Begin VB.ListBox List1 
      Height          =   2010
      Left            =   240
      TabIndex        =   1
      Top             =   120
      Width           =   3255
   End
   Begin RFIDX.rfidAX rfidAX1 
      Height          =   615
      Left            =   1080
      TabIndex        =   0
      Top             =   1200
      Width           =   2055
      _ExtentX        =   3625
      _ExtentY        =   1085
   End
   Begin VB.Label Label1 
      Caption         =   "Comm Port"
      Height          =   375
      Left            =   240
      TabIndex        =   3
      Top             =   2400
      Width           =   855
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()
    If rfidAX1.OpenPort(nCommPort) Then
        MsgBox "OK"
    Else
        MsgBox "Comm port open error"
    End If
End Sub

Private Sub Command2_Click()
    rfidAX1.ClosePort
End Sub

Private Sub rfidAX1_rfidData(sID As String, dDataTime As Date)
    If List1.ListCount > 100 Then List1.RemoveItem (0)
    List1.AddItem sID + "    " + CStr(dDataTime)
    List1.ListIndex = (List1.ListCount - 1)
End Sub
