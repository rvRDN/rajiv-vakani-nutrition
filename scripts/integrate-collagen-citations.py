#!/usr/bin/env python3
"""Add citations to insights/collagen-compared-to-what.html (citation pass only)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "insights" / "collagen-compared-to-what.html"

REPLACEMENTS = [
    (
        "Not once. Repeatedly.</p>",
        "Not once. Repeatedly.<sup><a href=\"#src-1\">1</a></sup><sup><a href=\"#src-2\">2</a></sup></p>",
    ),
    (
        "Meta-analyses for skin. Reviews for osteoarthritis. Wound-healing trials where certain preparations seemed to speed recovery.",
        "Meta-analyses for skin.<sup><a href=\"#src-3\">3</a></sup> Reviews for osteoarthritis.<sup><a href=\"#src-6\">6</a></sup> Wound-healing trials where certain preparations seemed to speed recovery.<sup><a href=\"#src-15\">15</a></sup>",
    ),
    (
        "Major guidelines for osteoarthritis, wound care, and healthy aging don&rsquo;t routinely recommend oral collagen for ordinary connective-tissue maintenance the way this market suggests.",
        "Major guidelines for osteoarthritis, wound care, and healthy aging don&rsquo;t routinely recommend oral collagen for ordinary connective-tissue maintenance the way this market suggests.<sup><a href=\"#src-5\">5</a></sup>",
    ),
    (
        "tiny doses of type II collagen that work through an entirely different mechanism",
        "tiny doses of type II collagen that work through an entirely different mechanism<sup><a href=\"#src-7\">7</a></sup>",
    ),
    (
        "Does collagen beat placebo? Pooled across trials, often yes, for some outcomes, over eight to twelve weeks. What if you filter for study quality, or industry funding, or independent replication? A careful recent skin meta-analysis found the pooled effects often shrink toward zero.",
        "Does collagen beat placebo? Pooled across trials, often yes, for some outcomes, over eight to twelve weeks.<sup><a href=\"#src-3\">3</a></sup> What if you filter for study quality, or industry funding, or independent replication? A careful recent skin meta-analysis found the pooled effects often shrink toward zero.<sup><a href=\"#src-4\">4</a></sup>",
    ),
    (
        "For muscle, someone did run the comparison. Collagen looks worse than whey for muscle protein synthesis. In one training study with older men, collagen beat placebo on body composition, but lost head-to-head against whey.",
        "For muscle, someone did run the comparison. Collagen looks worse than whey for muscle protein synthesis.<sup><a href=\"#src-8\">8</a></sup> In one training study with older men, collagen beat placebo on body composition, but lost head-to-head against whey.<sup><a href=\"#src-9\">9</a></sup>",
    ),
    (
        "For joints, there&rsquo;s a trial where a mix of amino acids with no collagen at all still improved discomfort versus placebo.",
        "For joints, there&rsquo;s a trial where a mix of amino acids with no collagen at all still improved discomfort versus placebo.<sup><a href=\"#src-10\">10</a></sup>",
    ),
    (
        "In sun-protected aged skin, production drops sharply, and the enzymes that break collagen apart rise, without a matching rise in the inhibitors that normally keep them in check.",
        "In sun-protected aged skin, production drops sharply, and the enzymes that break collagen apart rise, without a matching rise in the inhibitors that normally keep them in check.<sup><a href=\"#src-11\">11</a></sup>",
    ),
    (
        "In sun-exposed skin, cells can show signs of trying to rebuild while collagen still falls, because destruction outpaces repair.",
        "In sun-exposed skin, cells can show signs of trying to rebuild while collagen still falls, because destruction outpaces repair.<sup><a href=\"#src-12\">12</a></sup>",
    ),
    (
        "There&rsquo;s a loop researchers have traced in aged and sun-damaged skin.",
        "There&rsquo;s a loop researchers have traced in aged and sun-damaged skin.<sup><a href=\"#src-11\">11</a></sup><sup><a href=\"#src-12\">12</a></sup>",
    ),
    (
        "In one striking human study, restoring structural support in the dermis (with filler, not oral collagen), re-stretched those cells and production came back.",
        "In one striking human study, restoring structural support in the dermis (with filler, not oral collagen), re-stretched those cells and production came back.<sup><a href=\"#src-13\">13</a></sup>",
    ),
    (
        "Oral collagen may not do nothing. Some imaging studies report less fragmentation in the dermis; wound trials suggest peptide content matters.",
        "Oral collagen may not do nothing. Some imaging studies report less fragmentation in the dermis;<sup><a href=\"#src-19\">19</a></sup> wound trials suggest peptide content matters.<sup><a href=\"#src-15\">15</a></sup>",
    ),
    (
        "Wound and ulcer trials, where tissue is actively rebuilding, had some of the most coherent results I found, especially when products differed in peptide content. Osteoarthritis pools show modest pain and function improvements; I didn&rsquo;t see proof of cartilage growing back. Low-dose type II collagen appears to work through immune modulation, not &ldquo;eat collagen, rebuild cartilage.&rdquo; Tendon trials with resistance training sometimes show bigger cross-sectional area versus placebo; exercise is doing the heavy lifting either way.",
        "Wound and ulcer trials, where tissue is actively rebuilding, had some of the most coherent results I found, especially when products differed in peptide content.<sup><a href=\"#src-15\">15</a></sup> Osteoarthritis pools show modest pain and function improvements;<sup><a href=\"#src-6\">6</a></sup> I didn&rsquo;t see proof of cartilage growing back. Low-dose type II collagen appears to work through immune modulation, not &ldquo;eat collagen, rebuild cartilage.&rdquo;<sup><a href=\"#src-7\">7</a></sup> Tendon trials with resistance training sometimes show bigger cross-sectional area versus placebo;<sup><a href=\"#src-17\">17</a></sup> exercise is doing the heavy lifting either way.<sup><a href=\"#src-18\">18</a></sup>",
    ),
    (
        "One rigorous academic trial in people with severe age-related skin thinning: six months of collagen, no detectable benefit.",
        "One rigorous academic trial in people with severe age-related skin thinning: six months of collagen, no detectable benefit.<sup><a href=\"#src-14\">14</a></sup>",
    ),
    (
        "Pooled analyses look positive. Stricter subgroups often don&rsquo;t.",
        "Pooled analyses look positive.<sup><a href=\"#src-3\">3</a></sup> Stricter subgroups often don&rsquo;t.<sup><a href=\"#src-4\">4</a></sup>",
    ),
    (
        "Specific peptides from collagen do things in cell studies that generic amino acids don&rsquo;t: nudging cell behavior, hyaluronic acid production, populations of cells involved in wound repair. Some human trials suggest high-peptide products outperform low-peptide ones.",
        "Specific peptides from collagen do things in cell studies that generic amino acids don&rsquo;t: nudging cell behavior, hyaluronic acid production, populations of cells involved in wound repair.<sup><a href=\"#src-20\">20</a></sup> Some human trials suggest high-peptide products outperform low-peptide ones.<sup><a href=\"#src-15\">15</a></sup><sup><a href=\"#src-19\">19</a></sup>",
    ),
    (
        "Vitamin C is required for assembly; without it you get scurvy, which is collagen failure in the literal sense. Extra vitamin C beyond an already adequate diet doesn&rsquo;t automatically improve synthesis in replete adults.",
        "Vitamin C is required for assembly; without it you get scurvy, which is collagen failure in the literal sense.<sup><a href=\"#src-21\">21</a></sup> Extra vitamin C beyond an already adequate diet doesn&rsquo;t automatically improve synthesis in replete adults.<sup><a href=\"#src-22\">22</a></sup>",
    ),
    (
        "Joint comfort showed up in at least one trial from amino acids alone, no collagen.",
        "Joint comfort showed up in at least one trial from amino acids alone, no collagen.<sup><a href=\"#src-10\">10</a></sup>",
    ),
    (
        "Resistance training and loading, if tendons and bone matter to you, are real connective-tissue interventions, not generic wellness habits.",
        "Resistance training and loading, if tendons and bone matter to you, are real connective-tissue interventions, not generic wellness habits.<sup><a href=\"#src-16\">16</a></sup><sup><a href=\"#src-17\">17</a></sup>",
    ),
]

SOURCES = """    <section class="post-sources" aria-label="Sources">
      <div class="post-wrap">
        <div class="post-sources__group">
          <p class="post-sources__label">Sources</p>
          <ol>
            <li id="src-1">
              Iwai K, Hasegawa T, Taguchi Y, et al. Identification of food-derived collagen peptides in human blood after oral ingestion of gelatin hydrolysates. <em>J Agric Food Chem</em>. 2005;53(16):6531&ndash;6536.
              <a href="https://doi.org/10.1021/jf050206p" target="_blank" rel="noopener noreferrer">https://doi.org/10.1021/jf050206p</a>
            </li>
            <li id="src-2">
              Oesser S, Adam M, Babel W, Seifert J. Oral administration of <sup>14</sup>C labeled gelatin hydrolysate leads to an accumulation of radioactivity in cartilage of mice (C57/BL). <em>J Nutr</em>. 1999;129(10):1891&ndash;1895.
              <a href="https://doi.org/10.1093/jn/129.10.1891" target="_blank" rel="noopener noreferrer">https://doi.org/10.1093/jn/129.10.1891</a>
            </li>
            <li id="src-3">
              de Miranda RB, Weimer P, Rossi RC. Effects of hydrolyzed collagen supplementation on skin aging: a systematic review and meta-analysis. <em>Int J Dermatol</em>. 2021;60(12):1449&ndash;1461.
              <a href="https://doi.org/10.1111/ijd.15518" target="_blank" rel="noopener noreferrer">https://doi.org/10.1111/ijd.15518</a>
            </li>
            <li id="src-4">
              Myung SK, Park Y. Effects of collagen supplements on skin aging: a systematic review and meta-analysis of randomized controlled trials. <em>Am J Med</em>. 2025;138(9):1264&ndash;1277.
              <a href="https://doi.org/10.1016/j.amjmed.2025.04.034" target="_blank" rel="noopener noreferrer">https://doi.org/10.1016/j.amjmed.2025.04.034</a>
            </li>
            <li id="src-5">
              Kolasinski SL, Neogi T, Hochberg MC, et al. 2019 American College of Rheumatology/Arthritis Foundation guideline for the management of osteoarthritis of the hand, hip, and knee. <em>Arthritis Care Res (Hoboken)</em>. 2020;72(2):149&ndash;162.
              <a href="https://doi.org/10.1002/acr.24131" target="_blank" rel="noopener noreferrer">https://doi.org/10.1002/acr.24131</a>
            </li>
            <li id="src-6">
              Liang CW, Cheng HY, Lee YH, et al. Efficacy and safety of collagen derivatives for osteoarthritis: a trial sequential meta-analysis. <em>Osteoarthritis Cartilage</em>. 2024;32(3):276&ndash;289.
              <a href="https://doi.org/10.1016/j.joca.2023.12.010" target="_blank" rel="noopener noreferrer">https://doi.org/10.1016/j.joca.2023.12.010</a>
            </li>
            <li id="src-7">
              Kouzuma Y, Nagata-Kouzuma Y, Nagata N. Type II collagen oral tolerance; mechanism and role in collagen-induced arthritis and rheumatoid arthritis. <em>Mod Rheumatol</em>. 2009;19(6):581&ndash;589.
              <a href="https://doi.org/10.3109/s10165-009-0210-0" target="_blank" rel="noopener noreferrer">https://doi.org/10.3109/s10165-009-0210-0</a>
            </li>
            <li id="src-8">
              Oikawa SY, McGlory C, D&rsquo;Souza AK, et al. Whey protein but not collagen peptides stimulate acute and longer-term muscle protein synthesis with and without resistance exercise in healthy older women: a randomized controlled trial. <em>Am J Clin Nutr</em>. 2020;111(3):708&ndash;718.
              <a href="https://doi.org/10.1093/ajcn/nqz332" target="_blank" rel="noopener noreferrer">https://doi.org/10.1093/ajcn/nqz332</a>
            </li>
            <li id="src-9">
              Jendricke P, Centner C, Zdzieblik D, et al. The influence of specific bioactive collagen peptides on body composition and muscle strength in middle-aged, untrained men: a randomized controlled trial. <em>Int J Environ Res Public Health</em>. 2021;18(9):4837.
              <a href="https://doi.org/10.3390/ijerph18094837" target="_blank" rel="noopener noreferrer">https://doi.org/10.3390/ijerph18094837</a>
            </li>
            <li id="src-10">
              Takeuchi F, Takada M, Kobuna Y, et al. Effects of non-essential amino acids on knee joint conditions in adults: a randomised, double-blind, placebo-controlled trial. <em>Nutrients</em>. 2022;14(17):3628.
              <a href="https://doi.org/10.3390/nu14173628" target="_blank" rel="noopener noreferrer">https://doi.org/10.3390/nu14173628</a>
            </li>
            <li id="src-11">
              Varani J, Dame MK, Rittie L, et al. Decreased collagen production in chronologically aged skin: roles of age-dependent alteration in fibroblast function and defective mechanical stimulation. <em>Am J Pathol</em>. 2006;168(6):1861&ndash;1868.
              <a href="https://doi.org/10.2353/ajpath.2006.051302" target="_blank" rel="noopener noreferrer">https://doi.org/10.2353/ajpath.2006.051302</a>
            </li>
            <li id="src-12">
              Fligiel SE, Varani J, Datta SC, et al. Collagen degradation in aged/photodamaged skin in vivo and after exposure to matrix metalloproteinase-1 in vitro. <em>J Invest Dermatol</em>. 2003;120(5):842&ndash;848.
              <a href="https://doi.org/10.1046/j.1523-1747.2003.12148.x" target="_blank" rel="noopener noreferrer">https://doi.org/10.1046/j.1523-1747.2003.12148.x</a>
            </li>
            <li id="src-13">
              Wang F, Garza LA, Kang S, et al. In vivo stimulation of de novo collagen production caused by cross-linked hyaluronic acid dermal filler injections in photodamaged human skin. <em>Arch Dermatol</em>. 2007;143(2):155&ndash;163.
              <a href="https://doi.org/10.1001/archderm.143.2.155" target="_blank" rel="noopener noreferrer">https://doi.org/10.1001/archderm.143.2.155</a>
            </li>
            <li id="src-14">
              Guadanhim LRS, Miot HA, Soares JLM, et al. Efficacy and safety of topical or oral hydrolyzed collagen in women with dermatoporosis: a randomized, double-blind, factorial design study. <em>Dermatol Ther (Heidelb)</em>. 2023;13(2):523&ndash;534.
              <a href="https://doi.org/10.1007/s13555-022-00859-y" target="_blank" rel="noopener noreferrer">https://doi.org/10.1007/s13555-022-00859-y</a>
            </li>
            <li id="src-15">
              Sugihara F, Inoue N, Venkateswarathirukumara S. Ingestion of bioactive collagen hydrolysates enhanced pressure ulcer healing in a randomized double-blind placebo-controlled clinical study. <em>Sci Rep</em>. 2018;8:11403.
              <a href="https://doi.org/10.1038/s41598-018-29831-7" target="_blank" rel="noopener noreferrer">https://doi.org/10.1038/s41598-018-29831-7</a>
            </li>
            <li id="src-16">
              Shaw G, Lee-Barthel A, Ross MLR, et al. Vitamin C&ndash;enriched gelatin supplementation before intermittent activity augments collagen synthesis. <em>Am J Clin Nutr</em>. 2017;105(1):136&ndash;143.
              <a href="https://doi.org/10.3945/ajcn.116.138594" target="_blank" rel="noopener noreferrer">https://doi.org/10.3945/ajcn.116.138594</a>
            </li>
            <li id="src-17">
              Nulty CD, Phelan KJ, Rankin P, et al. Hydrolysed collagen supplementation enhances patellar tendon adaptations to 12 weeks&rsquo; resistance training in middle-aged men. <em>Eur J Sport Sci</em>. 2025;25(4):e12281.
              <a href="https://doi.org/10.1002/ejsc.12281" target="_blank" rel="noopener noreferrer">https://doi.org/10.1002/ejsc.12281</a>
            </li>
            <li id="src-18">
              Khatri M, Naughton RJ, Clifford T, et al. The effects of collagen peptide supplementation on body composition, collagen synthesis, and recovery from joint injury and exercise: a systematic review. <em>Amino Acids</em>. 2021;53(10):1493&ndash;1506.
              <a href="https://doi.org/10.1007/s00726-021-03072-x" target="_blank" rel="noopener noreferrer">https://doi.org/10.1007/s00726-021-03072-x</a>
            </li>
            <li id="src-19">
              Asserin J, Lati E, Shioya T, Prawitt J. The effect of oral collagen peptide supplementation on skin moisture and the dermal collagen network: evidence from an ex vivo model and randomized, placebo-controlled clinical trials. <em>J Cosmet Dermatol</em>. 2015;14(4):291&ndash;301.
              <a href="https://doi.org/10.1111/jocd.12174" target="_blank" rel="noopener noreferrer">https://doi.org/10.1111/jocd.12174</a>
            </li>
            <li id="src-20">
              Ohara H, Ichikawa S, Matsumoto H, et al. Collagen-derived di-peptide, prolylhydroxyproline (Pro-Hyp): a new low molecular weight growth-initiating factor for specific fibroblasts associated with wound healing. <em>Front Cell Dev Biol</em>. 2020;8:548975.
              <a href="https://doi.org/10.3389/fcell.2020.548975" target="_blank" rel="noopener noreferrer">https://doi.org/10.3389/fcell.2020.548975</a>
            </li>
            <li id="src-21">
              Myllyharju J. Prolyl 4-hydroxylases, the key enzymes of collagen biosynthesis. <em>Matrix Biol</em>. 2003;22(1):15&ndash;24.
              <a href="https://doi.org/10.1016/S0945-053X(03)00006-4" target="_blank" rel="noopener noreferrer">https://doi.org/10.1016/S0945-053X(03)00006-4</a>
            </li>
            <li id="src-22">
              Choi SY, Ko EJ, Lee YH, et al. Effects of collagen tripeptide supplement on skin properties: a prospective, randomized, controlled study. <em>J Cosmet Laser Ther</em>. 2014;16(3):132&ndash;137.
              <a href="https://doi.org/10.3109/14764172.2013.854119" target="_blank" rel="noopener noreferrer">https://doi.org/10.3109/14764172.2013.854119</a>
            </li>
          </ol>
        </div>
      </div>
    </section>

"""


def main() -> None:
    text = HTML.read_text(encoding="utf-8")
    original = text

    for old, new in REPLACEMENTS:
        if old not in text:
            raise SystemExit(f"Missing expected text:\n{old[:120]}...")
        text = text.replace(old, new, 1)

    marker = '    <section class="post-next" aria-label="Next">'
    if marker not in text:
        raise SystemExit("post-next marker not found")
    if "post-sources" in text:
        raise SystemExit("post-sources already present")

    text = text.replace(marker, SOURCES + "\n" + marker, 1)

    if text == original:
        raise SystemExit("No changes made")

    HTML.write_text(text, encoding="utf-8", newline="\n")
    print(f"Updated {HTML}")
    print(f"Sources: 22")
    print(f"Inline citation markers added: {text.count('<sup><a href=\"#src-')}")


if __name__ == "__main__":
    main()
