$env:NODE_FUNCTION_ALLOW_BUILTIN = "fs,path"

$portInUse = Get-NetTCPConnection `
    -LocalPort 5678 `
    -State Listen `
    -ErrorAction SilentlyContinue

if ($portInUse) {
    exit 0
}

$logFolder = Join-Path $env:LOCALAPPDATA "GermanNewsFA\logs"
New-Item -ItemType Directory -Path $logFolder -Force | Out-Null

$n8nScript = Join-Path $env:APPDATA "npm\n8n.ps1"

& $n8nScript start *>> (Join-Path $logFolder "n8n-startup.log")
