# Shell

Always use PowerShell for all shell commands and hook `runCommand` entries. Never use bash, CMD, or any other shell.

## JSON File Encoding

tes3conv requires JSON files without a UTF-8 BOM. The `fsWrite` tool writes files with BOM by default. After creating any JSON file that will be passed to tes3conv, strip the BOM using:

```powershell
$content = [System.IO.File]::ReadAllText("file.json", [System.Text.Encoding]::UTF8)
[System.IO.File]::WriteAllText("file.json", $content, (New-Object System.Text.UTF8Encoding $false))
```
