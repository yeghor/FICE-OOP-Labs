param (
    [string]$Path = ".",
    [string]$OutputFile = "python_files.txt"
)

# Resolve target directory to a full path
$targetPath = Resolve-Path $Path

# Resolve output file path
$outputPath = Join-Path (Get-Location) $OutputFile

# Initialize output file
"" | Out-File -FilePath $outputPath -Encoding utf8

# Recursively retrieve all .py files
$pythonFiles = Get-ChildItem -Path $targetPath -Filter "*.py" -Recurse -File

if ($pythonFiles.Count -eq 0) {
    Write-Host "No Python (.py) files found in $targetPath" -ForegroundColor Yellow
    exit
}

foreach ($file in $pythonFiles) {

    $header = @"

========================================================
File: $($file.Name)
Path: $($file.FullName)
========================================================

"@

    # Write file header
    $header | Out-File -FilePath $outputPath -Encoding utf8 -Append

    # Read and append file content safely (UTF-8)
    try {
        Get-Content -Path $file.FullName -Raw -Encoding utf8 |
            Out-File -FilePath $outputPath -Encoding utf8 -Append
    }
    catch {
        $errorMessage = "Could not read file: $($file.FullName). Error: $_"
        $errorMessage | Out-File -FilePath $outputPath -Encoding utf8 -Append
        Write-Warning $errorMessage
    }

    # Add separator between files
    "`n" | Out-File -FilePath $outputPath -Encoding utf8 -Append
}

Write-Host "Successfully exported $($pythonFiles.Count) Python files." -ForegroundColor Green
Write-Host "Output saved to: $outputPath" -ForegroundColor Cyan