Const FILE_NAME="Commandbar.xlam"

Call Exec

Sub Exec()
    Dim objExcel
    Dim strAdPath
    Dim strMyPath
    Dim strAdCp
    Dim strMyCp
    Dim objFileSys
    Dim oAdd

    Set objExcel   = CreateObject("Excel.Application")
    Set objFileSys = CreateObject("Scripting.FileSystemObject")

    'AddInsのフォルダパス取得
    strAdPath = objExcel.Application.UserLibraryPath

    'このスクリプトのフルパスからスクリプト名を削除して，スクリプトのあるフォルダパスを取得する
    strMyPath = Replace(WScript.ScriptFullName, WScript.ScriptName, "")

    '文字列 \AddIns\FILE_NAME を作成
    strAdCp   = objFileSys.BuildPath(strAdPath, FILE_NAME)

    '文字列 \スクリプトのパス\FILE_NAME を作成
    strMyCp   = objFileSys.BuildPath(strMyPath, FILE_NAME)

    'FILE_NAMEをAddInsフォルダにコピー
    objFileSys.CopyFile strMyCp, strAdCp

    'Workbookの作成
    objExcel.Workbooks.Add

    'アドインの一覧に追加
    Set oAdd = objExcel.AddIns.Add(strAdCp,True)

    'アドインをインストール
    oAdd.Installed = True

    'Excelアプリケーションの終了
    objExcel.Quit

    Set objExcel   = Nothing
    Set objFileSys = Nothing

    MsgBox "Complete!"
End Sub