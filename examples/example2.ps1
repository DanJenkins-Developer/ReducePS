$paths = @('C:\Users\user1\Downloads\badfile1.exe', 'C:\Users\user1\Downloads\badfile*.exe', 'C:\Windows\System32\Tasks\badtask', 'C:\Users\user12345\AppData\Local\Temp\baddirectory\');

foreach ($path in $paths) {

    if (Test-Path($path))
    {
        Write-Output \"Deleting $path\";
        Remove-Item -Path $path -Recurse -Force -ErrorAction SilentlyContinue;
    }
    else {
        Write-Output \"$path does not exist\";
    }
}