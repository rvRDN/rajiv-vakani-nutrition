#!/usr/bin/env python3
"""Add citations to insights/invisible-maintenance.html (citation pass only)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "insights" / "invisible-maintenance.html"

REPLACEMENTS = [
    (
        "Collagen is not an ingredient in the way salt is an ingredient. It is a family of structural proteins: dozens of types, each with its own tissue habits. The ones people mean most often are the fibrillar collagens: rope-like molecules that assemble into cables and scaffolds. Type I dominates skin, tendon, ligament, and the organic framework of bone. Type II is the main collagen of cartilage. Type III shows up in softer, more compliant networks and in early repair before tissue matures.",
        "Collagen is not an ingredient in the way salt is an ingredient. It is a family of structural proteins: dozens of types, each with its own tissue habits.<sup><a href=\"#src-1\">1</a></sup> The ones people mean most often are the fibrillar collagens: rope-like molecules that assemble into cables and scaffolds. Type I dominates skin, tendon, ligament, and the organic framework of bone. Type II is the main collagen of cartilage. Type III shows up in softer, more compliant networks and in early repair before tissue matures.<sup><a href=\"#src-1\">1</a></sup>",
    ),
    (
        "<strong>Repair</strong> is what happens after disruption: hemostasis, inflammation, a provisional matrix, granulation tissue, remodeling over months to years.",
        "<strong>Repair</strong> is what happens after disruption: hemostasis, inflammation, a provisional matrix, granulation tissue, remodeling over months to years.<sup><a href=\"#src-5\">5</a></sup>",
    ),
    (
        "Estimates vary by tissue and method, but the broad truth is uncomfortable for quick-fix stories: much of what you are living inside was laid down slowly and may be replaced slowly, if at all, in specific compartments. Skin collagen can have residence times on the order of years to decades depending on what you measure. Cartilage is slower still.",
        "Estimates vary by tissue and method, but the broad truth is uncomfortable for quick-fix stories: much of what you are living inside was laid down slowly and may be replaced slowly, if at all, in specific compartments. Skin collagen can have residence times on the order of years to decades depending on what you measure.<sup><a href=\"#src-2\">2</a></sup> Cartilage is slower still.<sup><a href=\"#src-2\">2</a></sup>",
    ),
    (
        "Scar tissue is rich in collagen. Nobody considers it an upgrade. The fibers are there. They are organized wrong: more parallel, less elastic, mechanically inferior to unwounded skin. Cartilage repair after injury often produces fibrocartilage, not the hyaline matrix you started with.",
        "Scar tissue is rich in collagen. Nobody considers it an upgrade. The fibers are there. They are organized wrong: more parallel, less elastic, mechanically inferior to unwounded skin.<sup><a href=\"#src-5\">5</a></sup> Cartilage repair after injury often produces fibrocartilage, not the hyaline matrix you started with.<sup><a href=\"#src-6\">6</a></sup>",
    ),
    (
        "Without enough vitamin C, collagen assembly breaks down. Gums bleed. Wounds won&rsquo;t close properly. The body has amino acids. It cannot complete the chemistry that stabilizes the triple helix.",
        "Without enough vitamin C, collagen assembly breaks down. Gums bleed. Wounds won&rsquo;t close properly. The body has amino acids. It cannot complete the chemistry that stabilizes the triple helix.<sup><a href=\"#src-7\">7</a></sup>",
    ),
    (
        "Ultraviolet light cleaves dermal collagen; fragments accumulate; and the cells responsible for upkeep can lose their grip on intact fibrils, make less new matrix, and amplify the enzymes that cut collagen apart.",
        "Ultraviolet light cleaves dermal collagen; fragments accumulate; and the cells responsible for upkeep can lose their grip on intact fibrils, make less new matrix, and amplify the enzymes that cut collagen apart.<sup><a href=\"#src-8\">8</a></sup><sup><a href=\"#src-9\">9</a></sup>",
    ),
    (
        "Mechanical loading is a primary signal for tendon and bone adaptation. Tenocytes respond to stretch. Bone remodeling responds to strain sensed through osteocytes, tiny cells embedded in mineralized matrix, translating physical force into biological instruction. Disuse does the opposite. Immobilization after injury can halve tendon collagen synthesis within weeks.",
        "Mechanical loading is a primary signal for tendon and bone adaptation.<sup><a href=\"#src-11\">11</a></sup> Tenocytes respond to stretch.<sup><a href=\"#src-11\">11</a></sup> Bone remodeling responds to strain sensed through osteocytes, tiny cells embedded in mineralized matrix, translating physical force into biological instruction.<sup><a href=\"#src-12\">12</a></sup> Disuse does the opposite. Immobilization after injury can halve tendon collagen synthesis within weeks.<sup><a href=\"#src-10\">10</a></sup>",
    ),
    (
        "Training studies show that tendons can increase stiffness and modulus over months, often more clearly than they increase cross-sectional area. Acute rises in collagen synthesis markers after exercise peak around a day and do not, by themselves, prove that the entire mature tendon has been replaced.",
        "Training studies show that tendons can increase stiffness and modulus over months, often more clearly than they increase cross-sectional area.<sup><a href=\"#src-13\">13</a></sup> Acute rises in collagen synthesis markers after exercise peak around a day<sup><a href=\"#src-11\">11</a></sup> and do not, by themselves, prove that the entire mature tendon has been replaced.<sup><a href=\"#src-3\">3</a></sup>",
    ),
    (
        "Bomb-pulse carbon dating suggests much of the core collagen in a healthy adult Achilles may have been laid down long ago, with minimal renewal in midlife.",
        "Bomb-pulse carbon dating suggests much of the core collagen in a healthy adult Achilles may have been laid down long ago, with minimal renewal in midlife.<sup><a href=\"#src-3\">3</a></sup>",
    ),
    (
        "Tendinopathy (tendon disease) is associated with abnormally high turnover years before symptoms.",
        "Tendinopathy (tendon disease) is associated with abnormally high turnover years before symptoms.<sup><a href=\"#src-4\">4</a></sup>",
    ),
    (
        "Even in skin, mechanical context shapes fibroblast behavior; the dermis is not a soup you season with protein.",
        "Even in skin, mechanical context shapes fibroblast behavior;<sup><a href=\"#src-14\">14</a></sup> the dermis is not a soup you season with protein.",
    ),
    (
        "Has that been shown against a meaningful comparator? Pooled trials often report improved hydration and elasticity over eight to twelve weeks. A careful 2025 meta-analysis found effects shrinking or disappearing in higher-quality and non-industry-funded subgroups. A six-month trial in women with severe skin atrophy found no structural benefit from oral or topical hydrolyzed collagen.",
        "Has that been shown against a meaningful comparator? Pooled trials often report improved hydration and elasticity over eight to twelve weeks. A careful 2025 meta-analysis found effects shrinking or disappearing in higher-quality and non-industry-funded subgroups.<sup><a href=\"#src-15\">15</a></sup> A six-month trial in women with severe skin atrophy found no structural benefit from oral or topical hydrolyzed collagen.<sup><a href=\"#src-16\">16</a></sup>",
    ),
    (
        "Some trials suggest collagen timed around workouts may add something on top of training; exercise still appears to be the primary driver; comparisons to matched whey are sparse.",
        "Some trials suggest collagen timed around workouts may add something on top of training;<sup><a href=\"#src-17\">17</a></sup> exercise still appears to be the primary driver;<sup><a href=\"#src-11\">11</a></sup><sup><a href=\"#src-13\">13</a></sup> comparisons to matched whey are sparse.",
    ),
    (
        "undenatured type II collagen at milligram doses for joint symptoms.</strong> Immune tolerance, not grams of substrate.",
        "undenatured type II collagen at milligram doses for joint symptoms.</strong> Immune tolerance, not grams of substrate.<sup><a href=\"#src-18\">18</a></sup>",
    ),
    (
        "hydrolyzed collagen can yield peptides in blood. That keeps certain objections alive.",
        "hydrolyzed collagen can yield peptides in blood.<sup><a href=\"#src-19\">19</a></sup> That keeps certain objections alive.",
    ),
]

SOURCES = """    <section class="post-sources" aria-label="Sources">
      <div class="post-wrap">
        <div class="post-sources__group">
          <p class="post-sources__label">Sources</p>
          <ol>
            <li id="src-1">
              Ricard-Blum S. The collagen family. <em>Cold Spring Harb Perspect Biol</em>. 2011;3(1):a004978.
              <a href="https://doi.org/10.1101/cshperspect.a004978" target="_blank" rel="noopener noreferrer">https://doi.org/10.1101/cshperspect.a004978</a>
            </li>
            <li id="src-2">
              Verzijl N, DeGroot J, Thorpe SR, et al. Effect of collagen turnover on the accumulation of advanced glycation end products. <em>J Biol Chem</em>. 2000;275(15):39027&ndash;39031.
              <a href="https://doi.org/10.1074/jbc.M006700200" target="_blank" rel="noopener noreferrer">https://doi.org/10.1074/jbc.M006700200</a>
            </li>
            <li id="src-3">
              Heinemeier KM, Schjerling P, Heinemeier J, et al. Lack of tissue renewal in human adult Achilles tendon is revealed by nuclear bomb <sup>14</sup>C. <em>FASEB J</em>. 2013;27(5):2074&ndash;2079.
              <a href="https://doi.org/10.1096/fj.12-225599" target="_blank" rel="noopener noreferrer">https://doi.org/10.1096/fj.12-225599</a>
            </li>
            <li id="src-4">
              Heinemeier KM, Schjerling P, &Oslash;hlenschl&aelig;ger TF, et al. Carbon-14 bomb pulse dating shows that tendinopathy is preceded by years of abnormally high collagen turnover. <em>FASEB J</em>. 2018;32(9):4763&ndash;4775.
              <a href="https://doi.org/10.1096/fj.201701569r" target="_blank" rel="noopener noreferrer">https://doi.org/10.1096/fj.201701569r</a>
            </li>
            <li id="src-5">
              Gurtner GC, Werner S, Barrandon Y, Longaker MT. Wound repair and regeneration. <em>Nature</em>. 2008;453(7193):314&ndash;321.
              <a href="https://doi.org/10.1038/nature07039" target="_blank" rel="noopener noreferrer">https://doi.org/10.1038/nature07039</a>
            </li>
            <li id="src-6">
              Hunziker EB, Lippuner K, Keel MJ, Shintani N. An educational review of cartilage repair: precepts &amp; practice. <em>Swiss Med Wkly</em>. 2015;145:w22218.
              <a href="https://doi.org/10.4414/smw.2015.22218" target="_blank" rel="noopener noreferrer">https://doi.org/10.4414/smw.2015.22218</a>
            </li>
            <li id="src-7">
              Myllyharju J. Prolyl 4-hydroxylases, the key enzymes of collagen biosynthesis. <em>Matrix Biol</em>. 2003;22(1):15&ndash;24.
              <a href="https://doi.org/10.1016/S0945-053X(03)00006-4" target="_blank" rel="noopener noreferrer">https://doi.org/10.1016/S0945-053X(03)00006-4</a>
            </li>
            <li id="src-8">
              Fisher GJ, Quan T, Purohit T, et al. Collagen fragmentation promotes oxidative stress and elevates matrix metalloproteinase-1 in fibroblasts in aged human skin. <em>Am J Pathol</em>. 2009;174(1):101&ndash;114.
              <a href="https://doi.org/10.2353/ajpath.2009.080599" target="_blank" rel="noopener noreferrer">https://doi.org/10.2353/ajpath.2009.080599</a>
            </li>
            <li id="src-9">
              Fligiel SE, Varani J, Datta SC, et al. Collagen degradation in aged/photodamaged skin in vivo and after exposure to matrix metalloproteinase-1 in vitro. <em>J Invest Dermatol</em>. 2003;120(5):842&ndash;848.
              <a href="https://doi.org/10.1046/j.1523-1747.2003.12148.x" target="_blank" rel="noopener noreferrer">https://doi.org/10.1046/j.1523-1747.2003.12148.x</a>
            </li>
            <li id="src-10">
              de Boer MD, Maganaris CN, Seynnes OR, et al. The temporal responses of protein synthesis, gene expression and cell signalling in human quadriceps muscle and patellar tendon to disuse. <em>J Physiol</em>. 2007;585(Pt 1):241&ndash;251.
              <a href="https://doi.org/10.1113/jphysiol.2007.142828" target="_blank" rel="noopener noreferrer">https://doi.org/10.1113/jphysiol.2007.142828</a>
            </li>
            <li id="src-11">
              Miller BF, Olesen JL, Hansen M, et al. Coordinated collagen and muscle protein synthesis in human patella tendon and quadriceps muscle after exercise. <em>J Physiol</em>. 2005;567(Pt 3):1021&ndash;1033.
              <a href="https://doi.org/10.1113/jphysiol.2005.093690" target="_blank" rel="noopener noreferrer">https://doi.org/10.1113/jphysiol.2005.093690</a>
            </li>
            <li id="src-12">
              Robling AG, Bonewald LF. The osteocyte: new insights. <em>Annu Rev Physiol</em>. 2020;82:485&ndash;506.
              <a href="https://doi.org/10.1146/annurev-physiol-021119-034332" target="_blank" rel="noopener noreferrer">https://doi.org/10.1146/annurev-physiol-021119-034332</a>
            </li>
            <li id="src-13">
              Bohm S, Mersmann F, Arampatzis A. Human tendon adaptation in response to mechanical loading: a systematic review and meta-analysis of exercise intervention studies on healthy adults. <em>Sports Med Open</em>. 2015;1:7.
              <a href="https://doi.org/10.1186/s40798-015-0009-9" target="_blank" rel="noopener noreferrer">https://doi.org/10.1186/s40798-015-0009-9</a>
            </li>
            <li id="src-14">
              Varani J, Dame MK, Rittie L, et al. Decreased collagen production in chronologically aged skin: roles of age-dependent alteration in fibroblast function and defective mechanical stimulation. <em>Am J Pathol</em>. 2006;168(6):1861&ndash;1868.
              <a href="https://doi.org/10.2353/ajpath.2006.051302" target="_blank" rel="noopener noreferrer">https://doi.org/10.2353/ajpath.2006.051302</a>
            </li>
            <li id="src-15">
              Myung SK, Park Y. Effects of collagen supplements on skin aging: a systematic review and meta-analysis of randomized controlled trials. <em>Am J Med</em>. 2025;138(9):1264&ndash;1277.
              <a href="https://doi.org/10.1016/j.amjmed.2025.04.034" target="_blank" rel="noopener noreferrer">https://doi.org/10.1016/j.amjmed.2025.04.034</a>
            </li>
            <li id="src-16">
              Guadanhim LRS, Miot HA, Soares JLM, et al. Efficacy and safety of topical or oral hydrolyzed collagen in women with dermatoporosis: a randomized, double-blind, factorial design study. <em>Dermatol Ther (Heidelb)</em>. 2023;13(2):523&ndash;534.
              <a href="https://doi.org/10.1007/s13555-022-00859-y" target="_blank" rel="noopener noreferrer">https://doi.org/10.1007/s13555-022-00859-y</a>
            </li>
            <li id="src-17">
              Nulty CD, Phelan KJ, Rankin P, et al. Hydrolysed collagen supplementation enhances patellar tendon adaptations to 12 weeks&rsquo; resistance training in middle-aged men. <em>Eur J Sport Sci</em>. 2025;25(4):e12281.
              <a href="https://doi.org/10.1002/ejsc.12281" target="_blank" rel="noopener noreferrer">https://doi.org/10.1002/ejsc.12281</a>
            </li>
            <li id="src-18">
              Kouzuma Y, Nagata-Kouzuma Y, Nagata N. Type II collagen oral tolerance; mechanism and role in collagen-induced arthritis and rheumatoid arthritis. <em>Mod Rheumatol</em>. 2009;19(6):581&ndash;589.
              <a href="https://doi.org/10.3109/s10165-009-0210-0" target="_blank" rel="noopener noreferrer">https://doi.org/10.3109/s10165-009-0210-0</a>
            </li>
            <li id="src-19">
              Iwai K, Hasegawa T, Taguchi Y, et al. Identification of food-derived collagen peptides in human blood after oral ingestion of gelatin hydrolysates. <em>J Agric Food Chem</em>. 2005;53(16):6531&ndash;6536.
              <a href="https://doi.org/10.1021/jf050206p" target="_blank" rel="noopener noreferrer">https://doi.org/10.1021/jf050206p</a>
            </li>
          </ol>
        </div>
      </div>
    </section>

"""


def main() -> None:
    text = HTML.read_text(encoding="utf-8")

    text = text.replace("<span>June 28, 2026</span>", "<span>June 29, 2026</span>")
    text = text.replace("library.css?v=20260628100000", "library.css?v=20260629100000")
    text = text.replace("data.js?v=20260628100000", "data.js?v=20260629100000")

    text = text.replace(
        "      </div>\n\n      </div>\n    </article>",
        "      </div>\n    </article>",
        1,
    )

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

    HTML.write_text(text, encoding="utf-8", newline="\n")
    print(f"Updated {HTML}")
    print("Sources: 19")
    print(f"Inline citation markers: {text.count('<sup><a href=\"#src-')}")


if __name__ == "__main__":
    main()
