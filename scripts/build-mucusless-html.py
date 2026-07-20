# -*- coding: utf-8 -*-
"""Build insights/mucusless-diet.html from the revised manuscript."""

import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "insights" / "mucusless-diet.html"
CACHE = "20260719180000"
META_DESC = (
    "An investigation into Arnold Ehret's Mucusless Diet Healing System, "
    "how the claims reach Instagram, and why a model that doesn't hold up "
    "physiologically can still survive for more than a century."
)
META_DESC_JSON = json.dumps(META_DESC)


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def cite(*nums: int) -> str:
    return "".join(f'<sup><a href="#src-{n}">{n}</a></sup>' for n in nums)


def p(text: str) -> str:
    return f"        <p>{text}</p>\n"


def h2(text: str) -> str:
    return f"\n        <h2>{esc(text)}</h2>\n\n"


def em(text: str) -> str:
    return f"<em>{esc(text)}</em>"


def a(href: str, text: str) -> str:
    return f'<a href="{href}">{esc(text)}</a>'


body_parts: list[str] = []

# Act I
body_parts.append(h2("Act I: The Claim"))
body_parts.append(
    p(
        "A family member sent me an Instagram reel claiming that cantaloupe juice "
        "dissolves accumulated waste along the walls of the digestive tract. The juice "
        "works as a chemical cleanser, the creator said. The fruit&rsquo;s indigestible "
        f"fiber then helps move the loosened waste toward the exit.{cite(1)}"
    )
)
body_parts.append(
    p(
        "The comments were just as interesting. Some people said they had experienced "
        "it themselves. Others wanted to know where to begin. A few were skeptical. "
        "Most seemed convinced they were looking at something mainstream medicine had overlooked."
    )
)
body_parts.append(p("I had never heard the claim before."))
body_parts.append(p("For the reel to be right, three things had to be true."))
body_parts.append(p("The digestive tract would have to accumulate the kind of old waste he described."))
body_parts.append(
    p(
        "Cantaloupe juice would have to contain something capable of chemically "
        "loosening and dissolving that material."
    )
)
body_parts.append(
    p("And cantaloupe fiber would have to move the loosened waste by rubbing against the digestive tract.")
)
body_parts.append(p("The first stop was the waste itself."))
body_parts.append(
    p(
        "The reel moved through constipation, arterial plaque, gout, and microplastics "
        "as evidence that the body accumulates unusable waste. But those examples involve "
        "different materials, in different parts of the body, through different processes. "
        "Together, they don&rsquo;t establish a general layer of old food waste coating "
        f"the digestive tract.{cite(1)}"
    )
)
body_parts.append(
    p(
        "Fecal stones are real. Doctors call them fecaliths or, when they become large "
        "masses, fecalomas. They are hardened stool associated with constipation and "
        "impaction, not proof that everyone carries old food waste along the intestinal "
        f"walls.{cite(4)}"
    )
)
body_parts.append(
    p(
        "The reel was right about one narrow point: the digestive tract isn&rsquo;t clean. "
        "It isn&rsquo;t supposed to be. A thin mucus layer lubricates stool, shields the "
        "intestinal lining, and helps manage the microbial community living there. "
        f"It&rsquo;s part of a healthy colon.{cite(2, 3)}"
    )
)
body_parts.append(
    p(
        "It isn&rsquo;t permanent either. The body keeps producing, renewing, and shedding it. "
        f"In a healthy colon, it doesn&rsquo;t build into decades-old sheets.{cite(2)}"
    )
)
body_parts.append(
    p("The colon contains stool, but stool isn&rsquo;t a permanent layer of old waste attached to its wall.")
)
body_parts.append(p("That brings us to the cantaloupe."))
body_parts.append(
    p(
        "If cantaloupe juice chemically dissolved accumulated waste, what did the dissolving? "
        "An enzyme? Another chemical? What study in people showed it happening?"
    )
)
body_parts.append(
    p(
        "Neither showed up. Cantaloupe provides water, fiber, vitamin C, and carotenoids. "
        "Its water and fiber can change stool consistency and how quickly it moves. "
        "That isn&rsquo;t the same as chemically dissolving hardened waste."
    )
)
body_parts.append(
    p(
        "But the person in the video clearly believed it, and dozens of people in the "
        "comments seemed to believe it too."
    )
)
body_parts.append(p("So where did this idea come from?"))

# Act II
body_parts.append(h2("Act II: Following the Thread"))
body_parts.append(p("The reel gave me a name."))
body_parts.append(p("Arnold Ehret."))
body_parts.append(
    p(
        "The creator said he&rsquo;d practiced Ehret&rsquo;s Mucusless Diet Healing System "
        "for almost five years. To understand cantaloupe, he said, "
        f'{em("you have to reject nutritional concepts altogether.")} '
        "His profile led to a website dedicated to the lifestyle, with articles, videos, "
        f"and educational materials.{cite(1)}"
    )
)
body_parts.append(
    p(
        "JC&rsquo;s Journals says its owner is affiliated with Mucus-Free Life and appears "
        "in its Transition Diet 101 course. The site says it&rsquo;s independently operated "
        "but directs readers to the organization&rsquo;s books, courses, and memberships."
        f"{cite(5)}"
    )
)
body_parts.append(
    p(
        "Arnold Ehret was born in Germany in 1866. He developed what he believed was a "
        "complete explanation for human health and disease, published books, operated a "
        "sanitarium, and attracted followers who treated his ideas as a more natural "
        f"understanding of the body.{cite(6)}"
    )
)
body_parts.append(
    p(
        "What first looked like an unconventional dietary philosophy turned out to be an "
        "entirely different model of human physiology."
    )
)
body_parts.append(
    p(
        "According to Ehret, disease wasn&rsquo;t mainly about infection, genetics, or the "
        "mechanisms recognized by modern medicine. It came down to mucus building up inside "
        "the body. Food made the body cleaner or more obstructed. Protein meant something "
        "else. So did white blood cells. Even major organs had different jobs."
        f"{cite(6)}"
    )
)
body_parts.append(
    p(
        "People debate nutrition all the time, usually within the same understanding of "
        "physiology. Ehret was proposing another physiology. Recipes couldn&rsquo;t test it. "
        "The model itself had to hold up."
    )
)
body_parts.append(p("Could it survive what we now know about the body?"))

# Act III
body_parts.append(h2("Act III: Testing the Model"))
body_parts.append(p("The first surprise wasn&rsquo;t about food. It was about the circulatory system."))
body_parts.append(
    p(
        "Buried among Ehret&rsquo;s explanations was the claim that the lungs, not the heart, "
        "move blood through the body, while the heart functions primarily as a valve."
        f"{cite(6)}"
    )
)
body_parts.append(p("I stopped reading. I thought I had misunderstood. I hadn&rsquo;t."))
body_parts.append(
    p("This was no longer a disagreement about nutrition. It was a disagreement about circulation.")
)
body_parts.append(
    p(
        "The heart&rsquo;s ventricles generate the pressure that moves blood through the lungs "
        "and the body. The lungs exchange gases. A total artificial heart can replace the "
        "ventricles and circulate blood while the lungs remain in place."
        f"{cite(7, 8)}"
    )
)
body_parts.append(
    p(
        "White blood cells weren&rsquo;t described as part of the body&rsquo;s defense against "
        "infection. They were presented as accumulated waste, another form of mucus the body "
        f"was trying to eliminate.{cite(6)}"
    )
)
body_parts.append(
    p(
        "White blood cells develop from bone marrow and do specific immune jobs. When some "
        "types are missing, the risk of particular infections rises. They&rsquo;re not "
        f"dietary mucus.{cite(9)}"
    )
)
body_parts.append(
    p(
        "The explanation always came back to mucus. Disease became mucus. Inflammation became "
        "mucus. Even the body&rsquo;s attempts to heal became mucus. It wasn&rsquo;t one idea "
        "inside the system. It supported nearly everything else."
    )
)
body_parts.append(
    p(
        "Ehret wasn&rsquo;t simply saying that people eat too much protein. He treated the "
        "whole idea of protein as a basic error and elevated fruit sugar as the body&rsquo;s "
        f"main building material.{cite(6)}"
    )
)
body_parts.append(
    p(
        "Nine amino acids are essential for adults because the body can&rsquo;t make enough "
        "of them. They must come from food and help build tissues, enzymes, and antibodies. "
        "A well-planned plant-based diet can provide them. A fruit-dominant diet that rejects "
        f"concentrated plant protein sources makes that harder.{cite(10, 11)}"
    )
)
body_parts.append(
    p(
        "Vitamin B12 helps make blood cells and keeps nerves working. Plants don&rsquo;t "
        "naturally contain it, so people who eat no animal products need fortified foods or "
        "supplements. A deficiency can cause anemia and nerve injury, yet the body&rsquo;s "
        f"stores can delay symptoms for years.{cite(12)}"
    )
)
body_parts.append(
    p(
        "The modern movement doesn&rsquo;t treat this as a gap to fill. In "
        f"{em('Spira Speaks')}, Professor Spira frames B12 as a myth, questions what blood "
        "tests are measuring, and presents supplementation as part of a faulty way of thinking."
        f"{cite(13)}"
    )
)
body_parts.append(p("Naming a nutrient did not invent the body&rsquo;s dependence on it."))
body_parts.append(
    p(
        "Ehret described the body as an air-gas engine powered by oxygen, minimizing food "
        f"as the source of usable energy.{cite(6, 13)}"
    )
)
body_parts.append(
    p(
        "Oxygen is necessary for cells to release energy, but it isn&rsquo;t the fuel. "
        "During fasting, the body uses energy stored as glycogen and fat, then increasingly "
        "draws on lean tissue. Oxygen permits combustion. It is not the wood."
        f"{cite(14)}"
    )
)
body_parts.append(p("The physiology did not hold up. The movement survived."))
body_parts.append(
    p(
        "Many followers described feeling healthier, and some practices could plausibly help: "
        "eating more fruit, reducing highly processed foods, losing excess weight, or fasting "
        "in some circumstances. Those changes can be real without validating the mucus theory."
    )
)
body_parts.append(
    p(
        "How does a model of the body that doesn&rsquo;t hold up keep persuading intelligent "
        "people, generation after generation?"
    )
)

# Act IV
body_parts.append(h2("Act IV: The System That Survived"))
body_parts.append(
    p(
        "Ehret&rsquo;s ideas hadn&rsquo;t simply been preserved. They&rsquo;d been translated "
        "into modern books, websites, videos, and communities. The language had changed. "
        "The presentation had changed. The confidence hadn&rsquo;t. The Mucusless Diet had "
        "become an ecosystem."
    )
)
body_parts.append(p("One of the people who carried the system forward was Professor Spira."))
body_parts.append(
    p(
        "Public records identify Spira as Norman Michael Goecke, a jazz trombonist and "
        "ethnomusicologist who earned a PhD in musicology from Ohio State University in 2016. "
        "Ohio State describes him as the founder of Mucus-Free Life LLC."
        f"{cite(15, 16)}"
    )
)
body_parts.append(
    p(
        "The doctorate is real. Its field is musicology, not nutrition, medicine, or physiology. "
        f'The title {em("Professor")} can travel farther than the field that earned it.'
    )
)
body_parts.append(
    p(
        "An archive preserves a document. An annotated edition tells readers how to understand "
        "it. What it explains, and what it leaves unexplained, become editorial choices. "
        "In a book giving health advice, those choices carry responsibility."
    )
)
body_parts.append(
    p(
        "Spira has spent years republishing, annotating, teaching, and expanding the Mucusless "
        "Diet Healing System. Mucus-Free Life sells annotated editions, courses, memberships, "
        "coaching, and menu guidance. Its lifestyle coaching program is listed at $2,997 and "
        "includes a health questionnaire, menu templates, food-preparation instruction, "
        "accountability groups, and modules that cover lemon-juice enemas, herbal bowel "
        f'formulas, and {em("addiction")} to mucus-forming foods.{cite(17, 18)}'
    )
)
body_parts.append(
    p(
        "Selling health education doesn&rsquo;t make it wrong. But books, courses, coaching, "
        "and community give a doctrine somewhere to live and spread."
    )
)
body_parts.append(
    p(
        "The reel creator did not invent the physiology. He compressed it. A century of "
        "doctrine became a confident social media explanation about cantaloupe. That is a "
        "different kind of compression from the one I followed in "
        f'{a("where-the-egg-alzheimers-story-drifted.html", "Where the Egg–Alzheimer’s Story Drifted")}, '
        "but it belongs to the same family of problems: how a complicated story becomes "
        "something a stranger can believe in a minute."
    )
)
body_parts.append(p("Innerclean."))
body_parts.append(
    p(
        "Ehret did not only write. He sold. Innerclean was an intestinal laxative marketed "
        "under his own name, packaged with a leaflet promoting the Mucusless Diet. It promised "
        f'to remove {em("hardened feces, mucus, and other age-old")} waste from the intestines.'
        f"{cite(19)}"
    )
)
body_parts.append(
    p("The promise the reel now makes for cantaloupe was being sold in a box a century ago.")
)
body_parts.append(p("It helped explain why so many testimonials sounded sincere."))
body_parts.append(
    p(
        "Historical analyses and later formulations of Innerclean have repeatedly involved "
        "stimulant and bulk-forming ingredients such as senna, buckthorn or related bark, agar, "
        "and psyllium. Those ingredients would be expected to change stool output. Senna "
        "stimulates colonic motility. Psyllium and agar hold water and add bulk. The resulting "
        "stool can look larger, more gelatinous, or more dramatic than usual."
        f"{cite(19, 20, 21)}"
    )
)
body_parts.append(
    p(
        "Followers were seeing something real. The laxative changed what left their bodies. "
        "The doctrine told them what it meant."
    )
)
body_parts.append(
    p(
        "Feeling better proves cleansing. Feeling worse proves cleansing. A normal test fits. "
        "So does an abnormal one. Opposite outcomes confirm the theory."
    )
)
body_parts.append(p("The stakes changed when the same logic reached menstruation."))
body_parts.append(
    p(
        "Ehret taught that when a woman&rsquo;s body becomes perfectly clean through the diet, "
        "menstruation disappears, and he treated the monthly flow as impure waste. He described "
        "periods becoming less frequent and eventually stopping as the outcome of successful "
        f"cleansing.{cite(6)}"
    )
)
body_parts.append(
    p(
        "In reality, periods can stop when the body isn&rsquo;t getting enough energy, after "
        "weight loss, with excessive exercise, or under stress. After other causes are ruled "
        "out, doctors call this functional hypothalamic amenorrhea. Over time, it can "
        f"contribute to bone loss.{cite(22)}"
    )
)
body_parts.append(
    p(
        "A restrictive diet can stop menstruation, then turn that sign of physical strain "
        "into proof that the diet is working."
    )
)
body_parts.append(
    p(
        "Up to this point, I&rsquo;d been thinking about adults choosing a restrictive system. "
        "The infant passages changed the responsibility question."
    )
)
body_parts.append(
    p(
        "In the same section of Ehret&rsquo;s book, he advises diluting cow&rsquo;s milk with "
        "water and sweetening it with milk sugar or honey, starting fruit juices and honey "
        "diluted in water as soon as possible, interpreting a healthy-looking infant&rsquo;s "
        "weight as possible waste of decayed milk, putting babies through the same cleansing "
        "process as adults, avoiding special protein foods, and suggesting that after weaning "
        f'a child {em("could be raised on apples alone.")}{cite(6)}'
    )
)
body_parts.append(
    p(
        "Today, parents are told not to give infants honey, cow&rsquo;s milk as a drink, or "
        "fruit juice before 12 months. Honey can cause infant botulism. Cow&rsquo;s milk "
        f"doesn&rsquo;t have the right nutrient balance for an infant.{cite(23, 24)}"
    )
)
body_parts.append(
    p(
        "Ehret wrote before many modern pediatric safeguards existed. Mucus-Free Life continues "
        "to market annotated editions, courses, and coaching that present the system as usable "
        f"today.{cite(17, 18)}"
    )
)
body_parts.append(
    p(
        "Ehret developed the theory. Modern editors decide how it reaches new readers. "
        "Today&rsquo;s creators decide how confidently it&rsquo;s compressed online. Those "
        "aren&rsquo;t the same responsibilities."
    )
)
body_parts.append(
    p(
        "Somewhere along the way, I realized I had stopped investigating a diet. I was "
        "investigating how ideas survive."
    )
)
body_parts.append(
    p(
        "This one survived through a chain: an intuitive explanation, experiences that felt "
        "like proof, teachers who modernized the doctrine, institutions that reinforced it, "
        "and social media that compressed it into certainty."
    )
)
body_parts.append(
    p(
        "When my family member sent me the reel, I thought I was investigating cantaloupe. "
        "I ended up investigating how a health system whose physiology doesn&rsquo;t hold up "
        "can survive for more than a century and continue persuading intelligent people. "
        "That is the kind of question "
        f'{a("how-i-evaluate-nutrition-claims.html", "How I Evaluate Nutrition Claims")} '
        "was written to keep open, and the same family of compressed certainty I followed in "
        f'{a("the-mango-question.html", "The Mango Question")}.'
    )
)
body_parts.append(p("Understanding that process may be more useful than answering the original question."))
body_parts.append(
    p(
        "The next viral health claim probably won&rsquo;t involve mucus. When it arrives, "
        f'the first question is not {em("Do I believe this?")} It&rsquo;s '
        f'{em("How would I know if this were true?")}'
    )
)

sources = [
    (
        "JC&rsquo;s Journals [@jcs_journals]. &ldquo;Cantaloupe is one of the best foods on the planet&hellip;&rdquo; "
        "Instagram reel. July 17, 2026. "
        '<a href="https://www.instagram.com/p/Da5mC8iSAf9/" target="_blank" rel="noopener noreferrer">'
        "https://www.instagram.com/p/Da5mC8iSAf9/</a>"
    ),
    (
        "Johansson ME, Larsson JM, Hansson GC. The two mucus layers of colon are organized by the MUC2 mucin, "
        "whereas the outer layer is a legislator of host-microbial interactions. "
        "<em>Proc Natl Acad Sci USA</em>. 2011;108(11):4659-4665. "
        '<a href="https://doi.org/10.1073/pnas.1006451107" target="_blank" rel="noopener">doi:10.1073/pnas.1006451107</a>'
    ),
    (
        "Song C, Chai Z, Chen S, Zhang H, Zhang X, Zhou Y. Intestinal mucus components and secretion mechanisms: "
        "what we do and do not know. <em>Exp Mol Med</em>. 2023;55:681-691. "
        '<a href="https://doi.org/10.1038/s12276-023-00960-y" target="_blank" rel="noopener">doi:10.1038/s12276-023-00960-y</a>'
    ),
    (
        "Cleveland Clinic. Fecalith &amp; Fecaloma: What They Are, Symptoms and Treatment. "
        '<a href="https://my.clevelandclinic.org/health/diseases/fecalith" target="_blank" rel="noopener">'
        "my.clevelandclinic.org</a>"
    ),
    (
        "JC&rsquo;s Journals. Terms of Use. Affiliation disclosure regarding Mucus-Free Life and Transition Diet 101. "
        '<a href="https://jcsjournals.com/" target="_blank" rel="noopener">jcsjournals.com</a>'
    ),
    (
        "Ehret A. <em>Mucusless Diet Healing System</em>. Historical text (archive.org). "
        '<a href="https://archive.org/details/profarnoldehrets00ehre" target="_blank" rel="noopener">archive.org</a>'
    ),
    (
        "Cleveland Clinic. How an Artificial Heart Works. "
        '<a href="https://my.clevelandclinic.org/health/procedures/22173-total-artificial-heart" target="_blank" rel="noopener">'
        "my.clevelandclinic.org</a>"
    ),
    (
        "Copeland JG, et al. Cardiac replacement with a total artificial heart as a bridge to transplantation. "
        "<em>N Engl J Med</em>. 2004;351(9):859-867. "
        '<a href="https://doi.org/10.1056/NEJMoa040186" target="_blank" rel="noopener">doi:10.1056/NEJMoa040186</a>'
    ),
    (
        "Murphy K, Weaver C. <em>Janeway&rsquo;s Immunobiology</em>. 9th ed. Garland Science; 2016. "
        "Chapters on innate and adaptive leukocyte lineages and functions."
    ),
    (
        "National Research Council. Protein and Amino Acids. In: <em>Recommended Dietary Allowances</em>. "
        "10th ed. National Academies Press; 1989. "
        '<a href="https://www.ncbi.nlm.nih.gov/books/NBK234922/" target="_blank" rel="noopener">NCBI Bookshelf</a>'
    ),
    (
        "EFSA Panel on Dietetic Products, Nutrition and Allergies. Scientific Opinion on Dietary Reference Values "
        "for protein. <em>EFSA Journal</em>. 2012. "
        '<a href="https://www.efsa.europa.eu/" target="_blank" rel="noopener">efsa.europa.eu</a>'
    ),
    (
        "National Institutes of Health, Office of Dietary Supplements. Vitamin B12: Health Professional Fact Sheet. "
        '<a href="https://ods.od.nih.gov/factsheets/VitaminB12-HealthProfessional/" target="_blank" rel="noopener">'
        "ods.od.nih.gov</a>"
    ),
    (
        "Goecke NM (Prof. Spira). <em>Spira Speaks: Dialogs and Essays on the Mucusless Diet Healing System</em>. "
        "Section: Further Exploring the B-12 Myth. Mucus-Free Life LLC. "
        '<a href="https://www.mucusfreelife.com/wp-content/uploads/2016/06/Spira-Speaks-Breathair-3rd-ed.-Professor-Spira.pdf" '
        'target="_blank" rel="noopener">PDF</a>'
    ),
    (
        "Cahill GF Jr. Fuel metabolism in starvation. <em>Annu Rev Nutr</em>. 2006;26:1-22. "
        '<a href="https://doi.org/10.1146/annurev.nutr.26.061505.111258" target="_blank" rel="noopener">'
        "doi:10.1146/annurev.nutr.26.061505.111258</a>"
    ),
    (
        "Ohio State University School of Music. Musicology Careers: Norman (Michael) Goecke, PhD 2016. "
        '<a href="https://music.osu.edu/future/areas/musicology/careers" target="_blank" rel="noopener">music.osu.edu</a>'
    ),
    (
        "Goecke NM. What Is at Stake in Jazz Education? Creative Black Music and the Twenty-First-Century Learning "
        "Environment. Doctoral dissertation, Ohio State University; 2016. "
        '<a href="https://etd.ohiolink.edu/" target="_blank" rel="noopener">etd.ohiolink.edu</a>'
    ),
    (
        "Mucus-Free Life LLC. About / books, courses, coaching, and membership offerings. "
        '<a href="https://www.mucusfreelife.com/" target="_blank" rel="noopener">mucusfreelife.com</a>'
    ),
    (
        "Mucus-Free Life. Mucus-free Diet &amp; Lifestyle Coaching (Thinkific course page; listed price $2,997). "
        '<a href="https://mucusfreelife.thinkific.com/courses/mucus-free-diet-lifestyle-coaching" target="_blank" rel="noopener">'
        "Thinkific</a>"
    ),
    (
        "Notices of Judgment under the Food and Drugs Act. 19066. Misbranding of Innerclean. "
        "<em>U.S. v. 125 Cartons of Innerclean</em>. 1931. See also Cramp AJ. Laxatives: Inner-Clean. "
        "In: <em>Nostrums and Quackery and Pseudo-Medicine</em>. Vol. 3. AMA; 1936."
    ),
    (
        "Drugs.com. Senna Monograph for Professionals. "
        '<a href="https://www.drugs.com/monograph/senna.html" target="_blank" rel="noopener">drugs.com</a>'
    ),
    (
        "McRorie JW Jr, McKeown NM. Understanding the physics of functional fibers in the gastrointestinal tract. "
        "<em>J Acad Nutr Diet</em>. 2017;117(2):251-264. "
        '<a href="https://doi.org/10.1016/j.jand.2016.09.021" target="_blank" rel="noopener">'
        "doi:10.1016/j.jand.2016.09.021</a>"
    ),
    (
        "Gordon CM, et al. Functional hypothalamic amenorrhea: an Endocrine Society clinical practice guideline. "
        "<em>J Clin Endocrinol Metab</em>. 2017;102(5):1413-1439. "
        '<a href="https://doi.org/10.1210/jc.2017-00131" target="_blank" rel="noopener">doi:10.1210/jc.2017-00131</a>'
    ),
    (
        "Centers for Disease Control and Prevention. Botulism Prevention: Do not feed honey to a child younger "
        "than 1 year old. "
        '<a href="https://www.cdc.gov/botulism/prevention/index.html" target="_blank" rel="noopener">cdc.gov</a>'
    ),
    (
        "Centers for Disease Control and Prevention. Foods and Drinks to Avoid or Limit: honey, cow&rsquo;s milk, "
        "and juice before 12 months. "
        '<a href="https://www.cdc.gov/infant-toddler-nutrition/foods-and-drinks/foods-and-drinks-to-avoid-or-limit.html" '
        'target="_blank" rel="noopener">cdc.gov</a>'
    ),
]

source_lis = "\n".join(
    f'            <li id="src-{i}">{src}</li>' for i, src in enumerate(sources, 1)
)

html = f"""<!DOCTYPE html>
<html lang="en" class="post-page">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>

  <title>How the Mucusless Diet Survived a Century | Rajiv Vakani</title>
  <meta name="description" content="{esc(META_DESC)}">

  <meta property="og:type" content="article" />
  <meta property="og:url" content="https://rajivvakani.com/insights/mucusless-diet.html" />
  <meta property="og:title" content="How the Mucusless Diet Survived a Century | Rajiv Vakani" />
  <meta property="og:description" content="{esc(META_DESC)}" />
  <meta property="og:image" content="https://rajivvakani.com/headshot_36.jpg" />
  <meta property="og:site_name" content="Rajiv Vakani" />

  <link rel="canonical" href="https://rajivvakani.com/insights/mucusless-diet.html" />

  <meta property="twitter:card" content="summary_large_image" />
  <meta property="twitter:url" content="https://rajivvakani.com/insights/mucusless-diet.html" />
  <meta property="twitter:title" content="How the Mucusless Diet Survived a Century | Rajiv Vakani" />
  <meta property="twitter:description" content="{esc(META_DESC)}" />
  <meta property="twitter:image" content="https://rajivvakani.com/headshot_36.jpg" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preconnect" href="https://www.googletagmanager.com" />
  <link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700&family=Lora:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../rajiv-styles.min.css?v=20260715063000">
  <link rel="stylesheet" href="library.min.css?v={CACHE}">
  <link rel="icon" type="image/png" href="../favicon.png?v=rv7" />
  <link rel="apple-touch-icon" href="../favicon-512.png?v=rv7" />

  <script>
    window.addEventListener('load', function () {{
      if (location.hostname !== 'rajivvakani.com') return;
      var s = document.createElement('script');
      s.src = 'https://www.googletagmanager.com/gtag/js?id=G-0L41N5K2WV';
      s.async = true;
      document.head.appendChild(s);
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      window.gtag = gtag;
      gtag('js', new Date());
      gtag('config', 'G-0L41N5K2WV');
    }});
  </script>

  <script defer src="data.js?v={CACHE}"></script>
  <script defer src="library.js?v=2026060902"></script>
  <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "Article",
      "@id": "https://rajivvakani.com/insights/mucusless-diet.html#article",
      "headline": "How the Mucusless Diet Survived a Century",
      "description": {META_DESC_JSON},
      "url": "https://rajivvakani.com/insights/mucusless-diet.html",
      "mainEntityOfPage": {{
        "@type": "WebPage",
        "@id": "https://rajivvakani.com/insights/mucusless-diet.html#webpage"
      }},
      "author": {{
        "@id": "https://rajivvakani.com/#person"
      }},
      "publisher": {{
        "@type": "Person",
        "@id": "https://rajivvakani.com/#person",
        "name": "Rajiv Vakani",
        "url": "https://rajivvakani.com/about.html"
      }},
      "inLanguage": "en",
      "datePublished": "2026-07-19",
      "keywords": [
        "mucusless diet",
        "Arnold Ehret",
        "Mucusless Diet Healing System",
        "Professor Spira"
      ]
    }},
    {{
      "@type": "Person",
      "@id": "https://rajivvakani.com/#person",
      "name": "Rajiv Vakani",
      "url": "https://rajivvakani.com/about.html",
      "image": "https://rajivvakani.com/headshot_36.jpg"
    }}
  ]
}}
  </script>
</head>
<body class="post-page" data-article-slug="mucusless-diet" data-topic-id="reading-the-evidence">

  <nav class="main-nav">
    <div class="container nav-container">
      <a href="../index.html" class="site-logo"><img src="../logo-mark.png?v=rv9" alt="" class="site-logo__mark" decoding="async" width="543" height="543">Rajiv Vakani</a>
      <ul class="nav-links">
        <li><a href="../index.html">Home</a></li>
        <li><a href="../about.html">About</a></li>
        <li><a href="../journey.html">Journey</a></li>
        <li><a href="../insights.html" class="active">Insights</a></li>
        <li><a href="../library.html">Library</a></li>
        <li><a href="../contact.html">Contact</a></li>
      </ul>

      <button class="menu-toggle" aria-label="Toggle navigation">
        <span class="hamburger"></span><span class="hamburger"></span><span class="hamburger"></span>
      </button>
    </div>
  </nav>

  <div class="mobile-menu-overlay"></div>

  <main>

    <header class="post-header">
      <div class="post-wrap">
        <p class="post-anchor">
          in <a href="topics/reading-the-evidence.html">Reading the evidence</a>
        </p>
        <h1 class="post-title">How the Mucusless Diet Survived a Century</h1>
        <p class="post-dek">An investigation into how scientifically unsupported health systems persist.</p>
        <p class="post-meta">
          <span>Essay</span>
          <span>July 19, 2026</span>
        </p>
      </div>
    </header>

    <section class="post-glance" aria-label="At a glance">
      <div class="post-wrap">
        <p class="post-glance__label">At a glance</p>

        <p class="post-glance__beat">
          <span class="post-glance__beat-label">The claim</span>
          An Instagram reel said cantaloupe juice chemically dissolves accumulated waste in the digestive tract, then fiber moves it out.
        </p>

        <p class="post-glance__beat">
          <span class="post-glance__beat-label">What I found</span>
          The claim comes from Arnold Ehret&rsquo;s Mucusless Diet Healing System, a century-old model of the body that does not hold up against modern physiology.
        </p>

        <p class="post-glance__beat">
          <span class="post-glance__beat-label">Why it matters</span>
          The interesting question is not whether cantaloupe dissolves mucus. It is how an unsupported health system can keep persuading intelligent people.
        </p>

        <p class="post-glance__beat">
          <span class="post-glance__beat-label">Where I am now</span>
          Nutrition was the case study. The larger subject is how models survive: compression, institutions, experiences that feel like proof, and editorial responsibility.
        </p>
      </div>
    </section>

    <section class="post-claim-card" id="what-started-this" aria-labelledby="claim-card-title">
      <div class="post-wrap">

        <p class="post-claim-card__kicker">Claim source</p>

        <h2 class="post-claim-card__title" id="claim-card-title">What started this</h2>

        <p class="post-claim-card__intro">
          This article traces a public Instagram Reel from JC&rsquo;s Journals. The post claimed that cantaloupe juice chemically dissolves accumulated digestive waste and that the fruit&rsquo;s fiber helps move that waste toward elimination.
        </p>

        <div class="post-sources__claim">
          <p class="post-sources__claim-title">Instagram Reel by JC&rsquo;s Journals [@jcs_journals]</p>
          <p class="post-sources__claim-url">
            <a href="https://www.instagram.com/p/Da5mC8iSAf9/" target="_blank" rel="noopener noreferrer">https://www.instagram.com/p/Da5mC8iSAf9/</a>
          </p>
          <p class="post-sources__claim-accessed">Posted July 17, 2026. This article analyzes the claim, not the creator.</p>
        </div>

      </div>
    </section>

    <article class="post-body" id="journey">
      <div class="post-wrap">

{"".join(body_parts)}
      </div>
    </article>

    <section class="post-sources" aria-label="Sources">
      <div class="post-wrap">

        <details class="post-sources__disclosure">
          <summary>Sources <span class="post-sources__cue" aria-hidden="true">Open sources</span></summary>
          <div class="post-sources__disclosure-body">
            <div class="post-sources__group">
              <p class="post-sources__label">Claim source</p>
              <div class="post-sources__claim">
                <p class="post-sources__claim-title">Instagram Reel by JC&rsquo;s Journals [@jcs_journals]</p>
                <p class="post-sources__claim-url">
                  <a href="https://www.instagram.com/p/Da5mC8iSAf9/" target="_blank" rel="noopener noreferrer">https://www.instagram.com/p/Da5mC8iSAf9/</a>
                </p>
                <p class="post-sources__claim-accessed">Posted July 17, 2026.</p>
              </div>
            </div>

            <div class="post-sources__group">
              <p class="post-sources__label">Research and documentary sources</p>
            <ol>
{source_lis}
            </ol>
            </div>
          </div>
        </details>

      </div>
    </section>

    <section class="post-next" aria-label="Next">
      <div class="post-wrap" data-post-next></div>
    </section>

    <section class="post-colophon" aria-label="Signature">
      <div class="post-wrap">
        <p>
          <a href="../about.html">Rajiv Vakani</a>. Writing on nutrition from New York.<br class="colophon-break" aria-hidden="true">
          Since 2023. <a href="../contact.html">Email</a>.
        </p>
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2025&ndash;2026 Rajiv Vakani</p>
      <div class="footer-social" aria-label="Social links">
        <a href="https://instagram.com/rajivvakani" target="_blank" rel="noopener" aria-label="Instagram"><svg class="social-icon" aria-hidden="true" viewBox="0 0 448 512" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"/></svg></a>
        <a href="https://facebook.com/rajivvakani" target="_blank" rel="noopener" aria-label="Facebook"><svg class="social-icon" aria-hidden="true" viewBox="0 0 512 512" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M504 256C504 119 393 8 256 8S8 119 8 256c0 123.78 90.69 226.38 209.25 245V327.69h-63V256h63v-54.64c0-62.2 37-96.5 93.7-96.5 27.14 0 55.52 4.84 55.52 4.84v61h-31.28c-30.8 0-40.41 19.12-40.41 38.73V256h68.78l-11 71.69h-57.78V501C413.31 482.38 504 379.78 504 256z"/></svg></a>
        <a href="https://www.linkedin.com/in/rajivvakani/" target="_blank" rel="noopener" aria-label="LinkedIn"><svg class="social-icon" aria-hidden="true" viewBox="0 0 448 512" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"/></svg></a>
      </div>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', function () {{
      var menuToggle = document.querySelector('.menu-toggle');
      var navLinks = document.querySelector('.nav-links');
      var overlay = document.querySelector('.mobile-menu-overlay');
      if (menuToggle && navLinks) {{
        menuToggle.addEventListener('click', function () {{
          navLinks.classList.toggle('active');
          menuToggle.classList.toggle('active');
          if (overlay) overlay.classList.toggle('active');
          document.body.classList.toggle('menu-open');
        }});
      }}
      if (overlay) {{
        overlay.addEventListener('click', function () {{
          navLinks.classList.remove('active');
          menuToggle.classList.remove('active');
          overlay.classList.remove('active');
          document.body.classList.remove('menu-open');
        }});
      }}
    }});
  </script>
</body>
</html>
"""

OUT.write_text(html, encoding="utf-8")
print(OUT)
