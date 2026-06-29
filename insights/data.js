/* ============================================================
   Knowledge Library  --  Single Source of Truth
   ============================================================

   This file defines `window.RVData`, the only place where library
   structure and article metadata live. The render layer in
   library.js reads from it synchronously.

   Adding a new article:
     1. Add an entry to RVData.articles (see schema below).
     2. Create the article HTML page using _template.html.

   Adding a new topic or cluster:
     Edit RVData.library.topics in place.

   Renaming a topic, cluster, or article:
     Update the entry here; check that pinned recommendations in `next`
     and topic URLs still resolve.

   ------------------------------------------------------------
   ARTICLE SCHEMA
   ------------------------------------------------------------
   {
     slug:    string  -- unique identifier; must match the body
                         data-article-slug attribute on the page
     url:     string  -- site-relative path to the article HTML
     title:   string
     lede:    string  -- short voiced summary used in listings
     summary: string  -- longer voiced description
     type:    "Essay" | "Research Review" | "Observation" | "Guide"
     date:    "YYYY-MM-DD"
     topic:   string  -- must match a topics[].id
     cluster: string  -- must match a clusters[].id within that topic
     status:  "published" | "draft"
     next:    string[] -- pinned recommendation slugs (0..3).
                         Empty or short lists auto-fill from
                         same-cluster -> same-topic -> cross-topic.
   }
   ============================================================ */

window.RVData = {

  _meta: {
    version: 2,
    description: 'Single source of truth for the Knowledge Library. Replaces the previous library.json + articles.json + inline duplicates in library.js. Loaded by every Library-system page via <script defer src="insights/data.js">.',
    schemaVersion: '2.0.0',
    lastUpdated: '2026-06-29'
  },

  /* ----------------------------------------------------------
     Library  --  topics, clusters, Current Attention
     ---------------------------------------------------------- */
  library: {

    currentAttention: [
      {
        kind: 'Reading',
        what: 'A long paper on legumes, fiber, and what fermentable carbohydrates actually do in the gut.'
      },
      {
        kind: 'Drafting',
        what: 'A piece on dal, read as nutrition rather than tradition.'
      },
      {
        kind: 'Reconsidering',
        what: 'Whether \u201Cinflammatory foods\u201D lists hold up once you read past the headlines.'
      },
    ],

    topics: [

      {
        id: 'reading-the-evidence',
        name: 'Reading the evidence',
        url: 'insights/topics/reading-the-evidence.html',
        shortDescription: 'How nutrition studies, labels, and claims actually work; what they really say versus what they appear to say.',
        framing: 'Most of what passes for nutrition advice begins with a study, a label, a headline, or a claim. The interesting work is figuring out what any of those actually say. Not what they appear to say. Not what someone summarizing them says. What they say once you read them carefully, in the context of everything else that has been said on the same question. The pieces here are about that work.',
        startHere: 'the-mango-question',
        clusters: [
          {
            id: 'how-nutrition-science-actually-works',
            name: 'How nutrition science actually works',
            framing: 'Study design, statistics, levels of evidence. What kinds of claims can be made from what kinds of studies, and where the seams are.'
          },
          {
            id: 'case-by-case',
            name: 'Case by case: specific substances, foods, and studies',
            framing: 'Carrageenan, ultraprocessed claims, saturated fat, individual papers worth examining. Each piece is a worked example of reading the evidence on one thing.'
          },
          {
            id: 'claims-headlines-and-translation',
            name: 'Claims, headlines, and translation',
            framing: 'How nutrition science becomes media, regulation, marketing, and dinner-table advice. The gap between the study and the headline. Includes drift traces that follow a single claim from first impression to source and name where the story changed shape.'
          },
          {
            id: 'living-with-uncertainty',
            name: 'Living with uncertainty',
            framing: 'How to act when the evidence is partial, contested, or absent. What posture the questions deserve.'
          }
        ]
      },

      {
        id: 'south-asian-food-and-nutrition',
        name: 'South Asian food and nutrition',
        url: 'insights/topics/south-asian-food-and-nutrition.html',
        shortDescription: 'Dal, ghee, masalas, the meals my parents and grandparents made, and how their nutrition has been read or misread.',
        framing: 'This cluster is the cultural and dietary lens this site comes out of. Dal, ghee, rice, roti, spices, sweets, fermentation, the way meals are actually built. Studies on South Asian populations. The ways South Asian diets get misread, both from the outside and inside the family. The pieces here treat the cuisine as something worth reading closely rather than translating into a checklist of nutrients.',
        startHere: 'dal-read-as-nutrition',
        clusters: [
          {
            id: 'the-staple-foods-read-as-nutrition',
            name: 'The staple foods, read as nutrition',
            framing: 'Dal, rice, roti, ghee, masalas, sweets. Each piece is one staple, considered closely.'
          },
          {
            id: 'studies-on-south-asian-populations',
            name: 'Studies on South Asian populations',
            framing: 'MASALA and similar cohort studies. What the evidence about us actually says.'
          },
          {
            id: 'misreadings-and-family-level-myths',
            name: 'Misreadings and family-level myths',
            framing: 'How South Asian diets get misread by Western discourse, and by family conversations and WhatsApp networks.'
          },
          {
            id: 'vegetarian-and-jain-traditions',
            name: 'Vegetarian and Jain traditions',
            framing: 'The practices and restrictions of vegetarian and Jain eating, and how they look nutritionally.'
          },
          {
            id: 'ayurvedic-metabolic-claims',
            name: 'Ayurvedic therapies and metabolic claims',
            framing: 'What traditional prescribing patterns suggest, what ingredient trials show, and what proprietary products can actually claim, traced through real prescriptions, not system verdicts.'
          }
        ]
      },

      {
        id: 'practical-nutrition',
        name: 'Practical nutrition',
        url: 'insights/topics/practical-nutrition.html',
        shortDescription: 'What to actually eat. Questions that come up every day at the grocery store, in the kitchen, at the table.',
        framing: 'Eventually the question becomes what to actually eat. Practical nutrition is where the reading meets the kitchen. The pieces here are about composing meals, reading what you are buying, getting specific about protein and fiber and the rest, and eating well across the contexts of an actual life. Useful, voiced, not generic.',
        startHere: 'should-you-buy-lentil-pasta',
        clusters: [
          {
            id: 'building-meals-and-plates',
            name: 'Building meals and plates',
            framing: 'How to compose nutrition practically. Plates, weeks, breakfasts.'
          },
          {
            id: 'reading-what-youre-buying',
            name: 'Reading what you\u2019re buying',
            framing: 'Labels, ingredient lists, claims, the actual decisions at the grocery store.'
          },
          {
            id: 'specific-nutrients-in-practice',
            name: 'Specific nutrients in practice',
            framing: 'Protein, fiber, fats, micronutrients. What to actually do, not how they work in the cell.'
          },
          {
            id: 'eating-in-context',
            name: 'Eating in context',
            framing: 'Travel, school, busy periods, social settings, family meals. The places where intentions meet the rest of life.'
          }
        ]
      },

      {
        id: 'food-culture-and-behavior',
        name: 'Food culture and behavior',
        url: 'insights/topics/food-culture-and-behavior.html',
        shortDescription: 'How people actually eat. Patterns, rituals, family, community, the gap between what we say and what we do.',
        framing: 'Most nutrition writing imagines the eater as a single person reading evidence and making choices. Real eating happens inside families, communities, conversations, rituals, and identities. This cluster takes the human side of food seriously. Why food choices feel moral. How nutrition beliefs travel through WhatsApp and grandmothers. The meanings we attach to what we eat. How to talk about any of this without turning into a sermon.',
        startHere: null,
        clusters: [
          {
            id: 'family-community-and-how-beliefs-travel',
            name: 'Family, community, and how beliefs travel',
            framing: 'How nutrition beliefs move through families, neighborhoods, social spaces, and the apps in between.'
          },
          {
            id: 'how-people-actually-eat',
            name: 'How people actually eat',
            framing: 'Stated versus actual eating. The gap between what we say and what we do.'
          },
          {
            id: 'identity-ethics-and-meaning',
            name: 'Identity, ethics, and meaning',
            framing: 'Why food choices feel moral. Identity, ritual, memory, ethics, and the meanings we attach to eating.'
          },
          {
            id: 'talking-and-teaching',
            name: 'Talking and teaching',
            framing: 'How to communicate and teach about nutrition without preaching.'
          }
        ]
      },

      {
        id: 'food-growing-and-systems',
        name: 'Food, growing, and systems',
        url: 'insights/topics/food-growing-and-systems.html',
        shortDescription: 'Where food comes from before it is food. Gardens, agriculture, supply, access.',
        framing: 'Before food is food it is a plant, a soil, a season, a system, a supply chain, a question of who can buy what and where. This cluster sits at that earlier layer. It is the part of the site about working with the material world food comes out of, and the systems that move food from there to here.',
        startHere: 'what-gardening-changed-about-how-i-think-about-food',
        clusters: [
          {
            id: 'gardening-and-growing',
            name: 'Gardening and growing',
            framing: 'The personal practice. What working with plants and seasons teaches about food.'
          },
          {
            id: 'where-food-comes-from-before-its-food',
            name: 'Where food comes from before it\u2019s food',
            framing: 'Agriculture, processing, supply chains, the chain behind a meal.'
          },
          {
            id: 'access-geography-and-systems',
            name: 'Access, geography, and systems',
            framing: 'Food deserts, local economies, who can eat what, and where.'
          }
        ]
      },

      {
        id: 'health-and-the-body',
        name: 'Health and the body',
        url: 'insights/topics/health-and-the-body.html',
        shortDescription: 'What food does in the body. Mechanism, outcomes, the specific health questions nutrition gets asked to answer.',
        framing: 'Some pieces are about how the body actually works with food. Mechanism, physiology, the systems that turn what we eat into how we feel and what shows up on labs. This cluster is for those pieces. Distinct from reading the evidence (which is about the science as science) and from practical nutrition (which is about eating).',
        startHere: null,
        clusters: [
          {
            id: 'heart-blood-and-metabolism',
            name: 'Heart, blood, and metabolism',
            framing: 'Cardiometabolic systems. Cholesterol, blood pressure, blood sugar, lipids.'
          },
          {
            id: 'gut-immunity-and-inflammation',
            name: 'Gut, immunity, and inflammation',
            framing: 'The gut microbiome, digestion, gut-immune crosstalk, inflammation as it shows up in food and the body.'
          },
          {
            id: 'weight-energy-and-body-composition',
            name: 'Weight, energy, and body composition',
            framing: 'How the body uses food at the energy and composition level.'
          }
        ]
      }

    ]
  },

  /* ----------------------------------------------------------
     Articles  --  the catalog
     ----------------------------------------------------------
     The `next` array holds pinned recommendations. The render
     layer auto-fills additional slots (up to 3 total) from same
     cluster, then same topic, then cross-topic. So:
       next: []                    -> 3 fully automatic
       next: ["a"]                 -> 1 pinned + 2 automatic
       next: ["a", "b", "c"]       -> all manual (legacy form)
     ---------------------------------------------------------- */
  articles: [

    {
      slug: 'how-i-evaluate-nutrition-claims',
      url: 'insights/how-i-evaluate-nutrition-claims.html',
      title: 'How I Evaluate Nutrition Claims',
      lede: 'The questions I return to when a confident nutrition claim catches my attention.',
      type: 'Guide',
      date: '2026-06-01',
      topic: 'reading-the-evidence',
      cluster: 'how-nutrition-science-actually-works',
      summary: 'A working method for reading nutrition claims. The questions to ask before agreeing or disagreeing, and the postures that make those questions useful.',
      status: 'published',
      next: ['why-nutrition-advice-keeps-changing', 'why-i-stopped-trusting-simple-answers', 'carrageenan']
    },

    {
      slug: 'why-i-stopped-trusting-simple-answers',
      url: 'insights/why-i-stopped-trusting-simple-answers.html',
      title: 'Why I Stopped Trusting Simple Answers',
      lede: 'Why simple nutrition rules often fall apart in real life, and what I started doing instead of looking for clearer ones.',
      type: 'Essay',
      date: '2026-06-01',
      topic: 'reading-the-evidence',
      cluster: 'living-with-uncertainty',
      summary: 'What I came to after years of looking for cleaner nutrition rules. Why the rules tend to collapse, and what posture replaces them.',
      status: 'published',
      next: ['how-i-evaluate-nutrition-claims', 'why-nutrition-advice-keeps-changing', 'what-dr-gundry-taught-me']
    },

    {
      slug: 'what-dr-gundry-taught-me',
      url: 'insights/what-dr-gundry-taught-me.html',
      title: 'What Dr. Gundry Taught Me Even Though I Don\u2019t Follow His Advice',
      lede: 'Five months on a lectin-restricted diet, what improved, what didn\u2019t, and what stayed with me after I stopped.',
      type: 'Essay',
      date: '2026-06-01',
      topic: 'reading-the-evidence',
      cluster: 'case-by-case',
      summary: 'A worked example of taking a confident authority seriously, trying the protocol, and reading both the experience and the evidence carefully on the way back out.',
      status: 'published',
      next: ['carrageenan', 'how-i-evaluate-nutrition-claims', 'why-i-stopped-trusting-simple-answers']
    },

    {
      slug: 'carrageenan',
      url: 'insights/carrageenan.html',
      title: 'Carrageenan: What the Human Evidence Actually Shows',
      lede: 'A careful read of the carrageenan literature \u2014 regulatory positions, human studies, mechanism work, and what any of it justifies concluding.',
      type: 'Research Review',
      date: '2026-06-08',
      topic: 'reading-the-evidence',
      cluster: 'case-by-case',
      summary: 'Carrageenan as a worked example of reading an additive controversy through the actual evidence rather than through the headlines.',
      status: 'draft',
      next: ['how-i-evaluate-nutrition-claims', 'what-dr-gundry-taught-me', 'why-nutrition-advice-keeps-changing']
    },

    {
      slug: 'why-nutrition-advice-keeps-changing',
      url: 'insights/why-nutrition-advice-keeps-changing.html',
      title: 'Why Nutrition Advice Keeps Changing',
      lede: 'Why nutrition advice updates more than other kinds of health advice, and what that means for how to read any single recommendation.',
      type: 'Essay',
      date: '2026-06-08',
      topic: 'reading-the-evidence',
      cluster: 'how-nutrition-science-actually-works',
      summary: 'A meta-piece on the nature of nutrition science. Why the field churns, where the churn is real progress, and where it is noise dressed as news.',
      status: 'draft',
      next: ['how-i-evaluate-nutrition-claims', 'why-i-stopped-trusting-simple-answers', 'carrageenan']
    },

    {
      slug: 'dal-read-as-nutrition',
      url: 'insights/dal-read-as-nutrition.html',
      title: 'Dal, Read as Nutrition',
      lede: 'What dal does as nutrition, considered carefully rather than as a default of \u201Cgood South Asian protein.\u201D',
      type: 'Essay',
      date: '2026-06-08',
      topic: 'south-asian-food-and-nutrition',
      cluster: 'the-staple-foods-read-as-nutrition',
      summary: 'Reading the most common South Asian staple closely. Protein quality, fiber and fermentation, the gut, glycemic response, and the difference between dal as tradition and dal as nutrition.',
      status: 'draft',
      next: ['a-practical-guide-to-vegetarian-protein', 'carrageenan', 'how-i-evaluate-nutrition-claims']
    },

    {
      slug: 'a-practical-guide-to-vegetarian-protein',
      url: 'insights/a-practical-guide-to-vegetarian-protein.html',
      title: 'A Practical Guide to Vegetarian Protein',
      lede: 'How to actually get enough protein on a vegetarian diet without overthinking it. Targets, sources, and how I think about combining them.',
      type: 'Guide',
      date: '2026-06-08',
      topic: 'practical-nutrition',
      cluster: 'specific-nutrients-in-practice',
      summary: 'A working guide to vegetarian protein. Daily targets, the sources that actually carry the load, and how to compose meals without turning every plate into a calculation.',
      status: 'draft',
      next: ['dal-read-as-nutrition', 'how-i-evaluate-nutrition-claims', 'why-i-stopped-trusting-simple-answers']
    },

    {
      slug: 'what-gardening-changed-about-how-i-think-about-food',
      url: 'insights/what-gardening-changed-about-how-i-think-about-food.html',
      title: 'What Gardening Changed About How I Think About Food',
      lede: 'Small things that became visible only after a few seasons of actually growing some of what I eat.',
      type: 'Observation',
      date: '2026-06-08',
      topic: 'food-growing-and-systems',
      cluster: 'gardening-and-growing',
      summary: 'Voiced noticing from a few seasons of vegetable gardening. What working with plants and weather changed about how I read nutrition advice, supply chains, and seasonality.',
      status: 'draft',
      next: ['dal-read-as-nutrition', 'a-practical-guide-to-vegetarian-protein', 'how-i-evaluate-nutrition-claims']
    },

    {
      slug: 'protein-marketing-and-trust',
      url: 'insights/protein-marketing-and-trust.html',
      title: 'Protein, Marketing, and Trust',
      lede: 'Reading the NYT piece on the David protein bar with one eye on the science and one on the marketing, and what that mix is doing to trust.',
      type: 'Essay',
      date: '2026-06-08',
      topic: 'reading-the-evidence',
      cluster: 'claims-headlines-and-translation',
      summary: 'How nutrition science gets translated into lifestyle messaging, what the David bar story says about influencer credibility, and what the protein boom reveals about the culture buying it.',
      status: 'draft',
      next: ['how-i-evaluate-nutrition-claims', 'why-nutrition-advice-keeps-changing', 'a-practical-guide-to-vegetarian-protein']
    },

    {
      slug: 'the-mango-question',
      url: 'insights/the-mango-question.html',
      title: 'The Mango Question',
      lede: 'A family question kept getting incompatible answers from people who all seemed to have evidence. Often they were answering different questions.',
      type: 'Essay',
      date: '2026-06-09',
      topic: 'reading-the-evidence',
      cluster: 'claims-headlines-and-translation',
      summary: 'When prediabetes and diabetes entered my family, one question kept surfacing: can I still eat mangoes? The answers collided until I noticed the fight was often about different questions compressed into one argument.',
      status: 'published',
      next: ['how-i-evaluate-nutrition-claims', 'the-glycemic-index-question']
    },

    {
      slug: 'the-glycemic-index-question',
      url: 'insights/the-glycemic-index-question.html',
      title: 'The Glycemic Index Isn\u2019t Wrong. We\u2019re Just Asking It the Wrong Question.',
      lede: 'Why so many \u201Chealthy\u201D foods score high on the glycemic index, and what the metric is, and isn\u2019t, actually measuring.',
      type: 'Essay',
      date: '2026-06-09',
      topic: 'reading-the-evidence',
      cluster: 'claims-headlines-and-translation',
      summary: 'A worked example of how a useful nutrition metric becomes misleading once it gets asked to answer questions it was never designed to answer, told through the puzzle of why watermelon and other healthy foods score so high on the glycemic index.',
      status: 'draft',
      next: ['the-mango-question', 'how-i-evaluate-nutrition-claims']
    },

    {
      slug: 'should-you-buy-lentil-pasta',
      url: 'insights/should-you-buy-lentil-pasta.html',
      title: 'What You\'re Really Paying For in Lentil Pasta',
      lede: 'Why does lentil pasta feel healthier before you read the label? And when is it actually worth the extra money?',
      type: 'Guide',
      date: '2026-06-20',
      topic: 'practical-nutrition',
      cluster: 'reading-what-youre-buying',
      summary: 'An aisle investigation into what healthier means on a premium pasta box. One train of thought from blood sugar to fiber to legumes to protein, then a cart decision: lentil, whole-grain, or regular durum.',
      status: 'published',
      next: ['a-practical-guide-to-vegetarian-protein', 'how-i-evaluate-nutrition-claims', 'the-glycemic-index-question']
    },

    {
      slug: 'where-the-egg-alzheimers-story-drifted',
      url: 'insights/where-the-egg-alzheimers-story-drifted.html',
      title: 'Where the Egg\u2013Alzheimer\u2019s Story Drifted',
      lede: 'A reel cited the Adventist Health Study and landed on a breakthrough. Two studies, one narrative, and a conclusion neither source fully supports.',
      type: 'Essay',
      date: '2026-06-22',
      topic: 'reading-the-evidence',
      cluster: 'claims-headlines-and-translation',
      summary: 'A drift trace of how egg and Alzheimer\u2019s findings traveled from two observational studies into one confident reel, and where merge, context drop, and confidence upgrade changed the story.',
      status: 'published',
      next: ['how-i-evaluate-nutrition-claims', 'the-mango-question', 'the-glycemic-index-question']
    },

    {
      slug: 'when-nutrition-advice-looks-like-precision-medicine',
      url: 'insights/when-nutrition-advice-looks-like-precision-medicine.html',
      title: 'When Nutrition Advice Starts Looking Like Precision Medicine',
      lede: 'Eight \u201Chealthy\u201D foods, eight conditions, eight avoid rules, all presented with the same clinical confidence. I opened a few rows. The evidence behind them looked nothing alike.',
      type: 'Essay',
      date: '2026-06-22',
      topic: 'reading-the-evidence',
      cluster: 'claims-headlines-and-translation',
      summary: 'A case study in why food-and-condition lists feel trustworthy: what real personalization requires, and what happens when the format outruns the evidence.',
      status: 'published',
      next: ['where-the-egg-alzheimers-story-drifted', 'how-i-evaluate-nutrition-claims', 'the-mango-question']
    },

    {
      slug: 'i-followed-a-real-ayurvedic-prescription',
      url: 'insights/i-followed-a-real-ayurvedic-prescription.html',
      title: 'I Followed a Real Ayurvedic Prescription Into the Research',
      lede: 'A relative\u2019s Ayurvedic prescription for blood sugar and triglycerides looked institutionally coherent. Tracing four products into the literature revealed a gap between familiar herbs and tested bottles.',
      type: 'Research Review',
      date: '2026-06-24',
      topic: 'south-asian-food-and-nutrition',
      cluster: 'ayurvedic-metabolic-claims',
      summary: 'A real Ayurvedic metabolic prescription traced through government guidelines, herb trials, and product gaps, without a verdict on whether Ayurveda works.',
      status: 'published',
      next: ['how-i-evaluate-nutrition-claims', 'the-mango-question', 'dal-read-as-nutrition']
    },

    {
      slug: 'creatine-used-to-live-in-the-gym',
      url: 'insights/creatine-used-to-live-in-the-gym.html',
      title: 'Creatine Used to Live in the Gym',
      lede: 'I already trusted creatine for training. Then the conversation expanded to brain health, aging, and focus. I followed the newer claims into the research.',
      type: 'Research Review',
      date: '2026-06-27',
      topic: 'reading-the-evidence',
      cluster: 'case-by-case',
      summary: 'A personal investigation into creatine beyond the gym: where the muscle evidence is strong, where the newer brain and aging claims hold up, and where they do not.',
      status: 'published',
      next: ['collagen-compared-to-what', 'how-i-evaluate-nutrition-claims', 'the-mango-question']
    },

    {
      slug: 'collagen-compared-to-what',
      url: 'insights/collagen-compared-to-what.html',
      title: 'Collagen, Compared to What?',
      lede: 'A mostly vegetarian friend takes bovine collagen every morning. I followed the trials and the biology to ask what decision she is actually making.',
      type: 'Research Review',
      date: '2026-06-27',
      topic: 'reading-the-evidence',
      cluster: 'case-by-case',
      summary: 'An investigation into oral collagen: absorption, contested skin trials, placebo comparators, and whether daily prevention matches where the evidence actually clusters.',
      status: 'published',
      next: ['invisible-maintenance', 'creatine-used-to-live-in-the-gym', 'how-i-evaluate-nutrition-claims']
    },

    {
      slug: 'invisible-maintenance',
      url: 'insights/invisible-maintenance.html',
      title: 'Invisible Maintenance',
      lede: 'Collagen was only the beginning.',
      type: 'Essay',
      date: '2026-06-29',
      topic: 'reading-the-evidence',
      cluster: 'case-by-case',
      summary: 'Most of what holds you together runs invisibly. Collagen was the entry point; this investigation asks what the body is sustaining, and what has to go wrong for structure to fail.',
      status: 'published',
      next: ['collagen-compared-to-what', 'how-i-evaluate-nutrition-claims', 'creatine-used-to-live-in-the-gym']
    }

  ]
};
