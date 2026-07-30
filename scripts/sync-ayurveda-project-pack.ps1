# Sync Ayurveda project context pack from canonical repo sources.
# Run from repo root: .\scripts\sync-ayurveda-project-pack.ps1

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
if (-not (Test-Path (Join-Path $Root "docs\clinical-judgment-ledger.md"))) {
    throw "Could not locate repo root (expected docs\clinical-judgment-ledger.md)."
}

$Pack = Join-Path $Root "docs\ayurveda-project"
$InvPack = Join-Path $Pack "investigations"
$PublishedPack = Join-Path $Pack "published"

New-Item -ItemType Directory -Force -Path $Pack, $InvPack, $PublishedPack | Out-Null

$DocFiles = @(
    "ai-context-primer.md",
    "ayurveda-project-constitution-for-ai-context.md",
    "clinical-judgment-ledger.md",
    "communication-risks.md",
    "questions-that-changed.md",
    "candidate-article-notes.md",
    "rajiv-voice-and-thinking-book.md",
    "research-ayurveda-landscape-metabolic-v1.md",
    "research-ayurveda-prescribed-products-evidence-v1.md",
    "future-investigations.md"
)

$InvestigationFiles = @(
    "README.md",
    "metabolic-landscape.md",
    "ibs-lane-index.md",
    "oa-evidence-architecture.md",
    "oa-caraka-care-pathways.md",
    "cross-lane-synthesis.md"
)

$PublishedFiles = @(
    @{ Source = "insights\i-followed-a-real-ayurvedic-prescription.html"; Dest = "i-followed-a-real-ayurvedic-prescription.html" }
)

function Copy-SourceFile {
    param(
        [string]$Source,
        [string]$Destination
    )
    if (-not (Test-Path -LiteralPath $Source)) {
        Write-Warning "Missing source (skipped): $Source"
        return
    }
    Copy-Item -LiteralPath $Source -Destination $Destination -Force
    Write-Host "  -> $(Split-Path -Leaf $Destination)"
}

Write-Host "Syncing Ayurveda project pack to: $Pack"
Write-Host ""

Write-Host "Docs:"
foreach ($name in $DocFiles) {
    Copy-SourceFile (Join-Path $Root "docs\$name") (Join-Path $Pack $name)
}

Write-Host ""
Write-Host "Investigations:"
foreach ($name in $InvestigationFiles) {
    Copy-SourceFile (Join-Path $Root "docs\investigations\$name") (Join-Path $InvPack $name)
}

Write-Host ""
Write-Host "Published:"
foreach ($item in $PublishedFiles) {
    Copy-SourceFile (Join-Path $Root $item.Source) (Join-Path $PublishedPack $item.Dest)
}

Write-Host ""
Write-Host "Done. Pack ready at docs\ayurveda-project"
