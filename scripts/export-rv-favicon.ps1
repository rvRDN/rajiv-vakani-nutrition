Add-Type -AssemblyName System.Drawing

$root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
if (-not (Test-Path (Join-Path $root 'RV Favicon Monogram.png'))) {
  $root = 'c:\Users\rajiv\OneDrive\Desktop\rajiv-vakani-nutrition'
}

$srcPath = Join-Path $root 'RV Favicon Monogram.png'
$out512  = Join-Path $root 'favicon-512.png'
$outMark = Join-Path $root 'logo-mark.png'
$out32   = Join-Path $root 'favicon.png'
$out16   = Join-Path $root 'favicon-16.png'
$ink     = [System.Drawing.Color]::FromArgb(255, 26, 26, 26)
$clear   = [System.Drawing.Color]::FromArgb(0, 0, 0, 0)
$cream   = [System.Drawing.Color]::FromArgb(255, 250, 245, 234)

$src = [System.Drawing.Bitmap]::FromFile($srcPath)
$maxYScan = [int]($src.Height * 0.62)
$minX = $src.Width; $minY = $maxYScan; $maxX = 0; $maxY2 = 0

for ($y = 0; $y -lt $maxYScan; $y++) {
  for ($x = 0; $x -lt $src.Width; $x++) {
    if ($src.GetPixel($x, $y).A -gt 128) {
      if ($x -lt $minX) { $minX = $x }
      if ($x -gt $maxX) { $maxX = $x }
      if ($y -lt $minY) { $minY = $y }
      if ($y -gt $maxY2) { $maxY2 = $y }
    }
  }
}

$pad = 24
$minX = [Math]::Max(0, $minX - $pad)
$minY = [Math]::Max(0, $minY - $pad)
$maxX = [Math]::Min($src.Width - 1, $maxX + $pad)
$maxY2 = [Math]::Min($maxYScan - 1, $maxY2 + $pad)
$w = $maxX - $minX + 1
$h = $maxY2 - $minY + 1
Write-Host "Crop: $minX,$minY ${w}x$h"

$cropped = New-Object System.Drawing.Bitmap($w, $h, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
for ($y = 0; $y -lt $h; $y++) {
  for ($x = 0; $x -lt $w; $x++) {
    if ($src.GetPixel($minX + $x, $minY + $y).A -gt 128) {
      $cropped.SetPixel($x, $y, $ink)
    } else {
      $cropped.SetPixel($x, $y, $clear)
    }
  }
}
$src.Dispose()

$size = [Math]::Max($w, $h)
$square = New-Object System.Drawing.Bitmap($size, $size, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
$g = [System.Drawing.Graphics]::FromImage($square)
$g.Clear($clear)
$g.DrawImage($cropped, [int](($size - $w) / 2), [int](($size - $h) / 2))
$g.Dispose()
$cropped.Dispose()

function Save-OnBackground($source, $outPath, $dim, $bg) {
  $bmp = New-Object System.Drawing.Bitmap($dim, $dim)
  $gfx = [System.Drawing.Graphics]::FromImage($bmp)
  $gfx.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
  $gfx.Clear($bg)
  $gfx.DrawImage($source, 0, 0, $dim, $dim)
  $gfx.Dispose()
  $bmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)
  $bmp.Dispose()
}

Save-OnBackground $square $out512 $size $cream
$square.Save($outMark, [System.Drawing.Imaging.ImageFormat]::Png)
foreach ($dim in @(32, 16)) {
  $out = if ($dim -eq 32) { $out32 } else { $out16 }
  Save-OnBackground $square $out $dim $cream
}
$square.Dispose()
Write-Host "Exported: logo-mark.png (nav), favicon-512.png, favicon.png, favicon-16.png"
