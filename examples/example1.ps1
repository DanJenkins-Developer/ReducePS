$paths = @('C:\Users\', 'C:\Windows\System32\Tasks');

foreach ($path in $paths) {

    if (Test-Path($path))
    {
        Get-ChildItem -Path $path -Force | Sort-Object -Property LastWriteTime;
        # Get-ChildItem -Path $path -Force -Recurse | Sort-Object -Property LastWriteTime;
    }
    else {
        Write-Output \"$path does not exist\";
    }
}