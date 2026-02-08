# PowerShell script to create .env file from .env.example
# Run this script after installing PostgreSQL and creating the database

Write-Host "Creating .env file from .env.example..." -ForegroundColor Green

# Check if .env.example exists
if (-not (Test-Path ".env.example")) {
    Write-Host "Error: .env.example not found!" -ForegroundColor Red
    exit 1
}

# Check if .env already exists
if (Test-Path ".env") {
    Write-Host "Warning: .env file already exists!" -ForegroundColor Yellow
    $overwrite = Read-Host "Do you want to overwrite it? (y/N)"
    if ($overwrite -ne "y" -and $overwrite -ne "Y") {
        Write-Host "Cancelled." -ForegroundColor Yellow
        exit 0
    }
}

# Copy .env.example to .env
Copy-Item ".env.example" ".env" -Force

Write-Host "✅ .env file created successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "⚠️  IMPORTANT: Edit .env file and update:" -ForegroundColor Yellow
Write-Host "   - DATABASE_PASSWORD (set to your PostgreSQL lkc_user password)" -ForegroundColor Yellow
Write-Host ""
Write-Host "You can edit it with:" -ForegroundColor Cyan
Write-Host "   notepad .env" -ForegroundColor Cyan
Write-Host "   or" -ForegroundColor Cyan
Write-Host "   code .env" -ForegroundColor Cyan



