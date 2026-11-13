param (
    [string]$Path = "."
)

# Resolve target directory to a full path
$targetPath = Resolve-Path $Path

# Recursively retrieve all .py files
$pythonFiles = Get-ChildItem -Path $targetPath -Filter "*.py" -Recurse -File

if ($pythonFiles.Count -eq 0) {
    Write-Host "No Python (.py) files found in $targetPath" -ForegroundColor Yellow
    exit
}

foreach ($file in $pythonFiles) {
    Write-Host "`n========================================================" -ForegroundColor Cyan
    Write-Host "File: $($file.Name)" -ForegroundColor Green
    Write-Host "Path: $($file.FullName)" -ForegroundColor DarkCyan
    Write-Host "========================================================" -ForegroundColor Cyan

    # Read and output file content safely (UTF-8)
    try {
        Get-Content -Path $file.FullName -Raw -Encoding utf8
    }
    catch {
        Write-Warning "Could not read file: $($file.FullName). Error: $_"
    }
}