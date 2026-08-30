$url = 'https://backend-practice-ejvi.onrender.com/'
$log = Join-Path $env:USERPROFILE 'backend-practice-keepalive.log'
$ts = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
try {
    $code = (curl.exe -s -o NUL -w '%{http_code}' --max-time 30 $url)
    Add-Content -Path $log -Value "$ts HTTP=$code" -Encoding UTF8
} catch {
    Add-Content -Path $log -Value "$ts ERR=$($_.Exception.Message)" -Encoding UTF8
}
