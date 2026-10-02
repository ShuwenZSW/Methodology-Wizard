# -*- coding: utf-8 -*-
"""
============================================================
MEASUREMENT MAP CONTENT — Concepts, Instruments & Data
============================================================
Third map of Tiny Atlas, sister to the Methodology Map and the PA
Theory Map. Same architecture:
  TREE     : the concept hierarchy. Node = {"name": ..., "children": [...]}
             - the seven branch nodes carry "color" (see template_me.html
               COLORS for the palette keys)
  PROFILES : concept cards. Keys must exactly match leaf names in TREE.
             Fields: use        = core proposition (one sentence)
                     explain    = what the concept means and why it matters
                     concepts   = 4-6 key terms, rendered as chips
                     founders   = foundational scholars & seminal works
                     classics   = 2-3 classic readings
                     frameworks = key models / traditions with one-line
                                  descriptions
                     apply      = how to use it in a PA research design;
                                  method names are auto-linked to the
                                  Methodology Map (see build_measure.py)

[To add a concept — 3 steps]
  1. Add a leaf under the right category in TREE
  2. Add a profile with the same name in PROFILES (copy any entry and edit)
  3. Run  python build_measure.py  to regenerate index.html
============================================================
"""

TREE = {
  "name": "MEASUREMENT &\nDATA COLLECTION",
  "children": [
    {
      "name": "SCALES OF MEASUREMENT",
      "color": "scales",
      "children": [
        {
          "name": "Levels & Scaling",
          "children": [
            {"name": "Nominal & Ordinal"},
            {"name": "Interval & Ratio"},
          ]
        },
        {
          "name": "Rating & Cumulative Scales",
          "children": [
            {"name": "Likert & Summated Scales"},
            {"name": "Guttman & Cumulative Scales"},
          ]
        },
        {
          "name": "Index Construction",
          "children": [
            {"name": "Reflective vs Formative"},
          ]
        },
      ]
    },
    {
      "name": "VALIDITY",
      "color": "validity",
      "children": [
        {
          "name": "Validity Evidence",
          "children": [
            {"name": "Content Validity"},
            {"name": "Construct Validity"},
            {"name": "Criterion Validity"},
          ]
        },
        {
          "name": "Validation Strategy",
          "children": [
            {"name": "MTMM — Convergent & Discriminant"},
            {"name": "Validity Argument (Messick / Kane)"},
          ]
        },
      ]
    },
    {
      "name": "RELIABILITY",
      "color": "reliability",
      "children": [
        {
          "name": "Stability & Consistency",
          "children": [
            {"name": "Test–Retest & Parallel Forms"},
            {"name": "Internal Consistency — α & ω"},
          ]
        },
        {
          "name": "Raters & Facets",
          "children": [
            {"name": "Inter-Rater Reliability — κ & ICC"},
            {"name": "Standard Error of Measurement"},
            {"name": "Generalizability Theory"},
          ]
        },
      ]
    },
    {
      "name": "ERROR & BIAS",
      "color": "error",
      "children": [
        {
          "name": "Random Error",
          "children": [
            {"name": "Random Error & Attenuation"},
          ]
        },
        {
          "name": "Systematic Bias",
          "children": [
            {"name": "Systematic Bias & Response Styles"},
            {"name": "Common Method Variance"},
            {"name": "Mode & Interviewer Effects"},
            {"name": "Missing Data & Nonresponse Bias"},
          ]
        },
      ]
    },
    {
      "name": "DATA SOURCES",
      "color": "sources",
      "children": [
        {
          "name": "Asking & Observing",
          "children": [
            {"name": "Survey Data"},
            {"name": "Ethnographic & Field Observation"},
          ]
        },
        {
          "name": "Records & Traces",
          "children": [
            {"name": "Administrative & Register Data"},
            {"name": "Digital Trace Data"},
            {"name": "Unobtrusive & Archival Data"},
          ]
        },
      ]
    },
    {
      "name": "SAMPLING & COVERAGE",
      "color": "sampling",
      "children": [
        {
          "name": "Selection Designs",
          "children": [
            {"name": "Probability Sampling"},
            {"name": "Non-Probability Sampling"},
            {"name": "Sampling Error & Sample Size"},
          ]
        },
        {
          "name": "Frames & Nonresponse",
          "children": [
            {"name": "Coverage Error & Sampling Frames"},
            {"name": "Nonresponse & Weighting"},
          ]
        },
      ]
    },
    {
      "name": "COMPARABILITY",
      "color": "comparability",
      "children": [
        {
          "name": "Equivalence Testing",
          "children": [
            {"name": "Measurement Invariance"},
            {"name": "Scale Linking & Alignment (IRT)"},
          ]
        },
        {
          "name": "Adaptation & Harmonization",
          "children": [
            {"name": "Translation & Cross-Cultural Adaptation"},
            {"name": "Ex-Post Harmonization"},
            {"name": "Documentation & Codebooks (DDI)"},
          ]
        },
      ]
    },
  ]
}

PROFILES = {

  # ================= SCALES OF MEASUREMENT =================

  "Nominal & Ordinal": {
    "use": "Nominal scales name and classify; ordinal scales rank — but the distances between ranks are unknown, so treating them as interval silently corrupts the statistics.",
    "explain": "Stevens' 1946 partition sorts variables by the transformations that leave them unchanged: nominal data (party affiliation, policy sector, country) support counting and the mode; ordinal data (satisfaction rankings, education bands) preserve order but not spacing. Taking means of pure ranks or computing raw correlations on ordered categories is a category error — it is defensible only when the scale plausibly approximates interval properties, a claim that must be argued, not assumed.",
    "concepts": ["permissible statistics", "permutation invariance", "mode vs median", "ordered categories", "monotonic transformation"],
    "founders": "S. S. Stevens — 'On the Theory of Scales of Measurement,' Science (1946); the typology behind nearly every methods textbook, and the target of its most famous critique.",
    "classics": [
      "Stevens, S. S. (1946). 'On the Theory of Scales of Measurement,' Science 103, 677–680",
      "Stevens, S. S. (1951). Mathematics, Measurement, and Psychophysics, in Handbook of Experimental Psychology",
      "Velleman, P. F., & Wilkinson, L. (1993). 'Nominal, Ordinal, Interval, and Ratio Typologies Are Misleading,' The American Statistician",
    ],
    "frameworks": [
      "Stevens' hierarchy (1946) — nominal → ordinal → interval → ratio, each level adding one admissible transformation",
      "Permissible statistics rule — means and SD only at interval+, medians for ordinal, modes for nominal",
      "Velleman & Wilkinson critique (1993) — the type of a variable is a property of its analysis, not of the numbers themselves",
      "Ordered-category models — cumulative logit/probit as the honest default when spacing is unknown",
    ],
    "apply": "Audit every variable before modeling: which statistics does each support? For ordinal survey items, show robustness with cumulative-link models alongside OLS & Generalised Linear Models; for nominal outcomes use multinomial specifications. Pre-register the scale-type assumptions of composite indexes and test whether results survive rank-based transformations (see Methodology Map: Survey Design & Sampling).",
  },

  "Interval & Ratio": {
    "use": "Interval scales have equal spacing but no true zero; ratio scales add a zero and support proportions, growth rates, and meaningful ratios.",
    "explain": "Calendar years and temperature are interval: differences of one unit mean the same everywhere, but 'twice as much' is meaningless. Income, population, and response times are ratio: zero is real, so ratios and percent changes are valid. Most administrative outcomes are ratio variables, while most attitudinal batteries are only defensibly interval. Confusing the two — computing growth rates on interval-bounded indices — produces numbers that look precise and mean nothing.",
    "concepts": ["equal units", "absolute zero", "permissible transformations", "ratio statements", "origin dependence"],
    "founders": "Stevens (1946) for the distinction; the practical tradition of measurement-unit theory in physics-based scaling and economics (index numbers).",
    "classics": [
      "Stevens, S. S. (1946). 'On the Theory of Scales of Measurement,' Science 103, 677–680",
      "Krantz, D. H., Luce, R. D., Suppes, P., & Tversky, A. (1971). Foundations of Measurement, Vol. I",
      "Velleman, P. F., & Wilkinson, L. (1993). 'Nominal, Ordinal, Interval, and Ratio Typologies Are Misleading,' The American Statistician",
    ],
    "frameworks": [
      "Stevens' interval/ratio distinction — affine vs similarity transformations as the dividing line",
      "Origin sensitivity — why ratios of interval scales (e.g., index points) are meaningless",
      "Index-number theory — what it takes for a difference of '1 point' to mean the same across a scale",
      "Distributional consequences — skew and boundedness in ratio outcomes shape the whole modeling pipeline",
    ],
    "apply": "Classify outcomes before modeling: budgets, caseloads, and processing times are ratio; thermometers and most indices are interval at best. Avoid percent changes on interval-bounded measures, and test origin shifts across waves or countries before interpreting trends in Panel & Fixed-Effects Models or Multilevel / Hierarchical Models (see Methodology Map).",
  },

  "Likert & Summated Scales": {
    "use": "A set of ordinal items with a common construct is summed or averaged into one score — the workhorse of attitude measurement in public administration research.",
    "explain": "Rensis Likert (1932) showed that a simple sum of equally weighted agree–disagree items outperformed then-current scaling techniques in reliability. The summated scale assumes items are parallel manifestations of one latent dimension; its justification rests on internal consistency and factor structure, not on the items being interval. Treat the sum as an estimate of a latent score, validate it, and report the item pool alongside the composite.",
    "concepts": ["summated rating", "item polarity", "balanced keys", "ceiling/floor effects", "ordinal-vs-interval debate"],
    "founders": "Rensis Likert — A Technique for the Measurement of Attitudes (1932); the psychometric consolidation by Cronbach and Guttman in the same era.",
    "classics": [
      "Likert, R. (1932). A Technique for the Measurement of Attitudes, Archives of Psychology",
      "Cronbach, L. J. (1951). 'Coefficient Alpha and the Internal Structure of Tests,' Psychometrika",
      "Krosnick, J. A., & Presser, S. (2010). 'Question and Questionnaire Design,' in Handbook of Survey Research",
    ],
    "frameworks": [
      "Likert's equal-weights summation — simple sum of item scores as the attitude estimate",
      "Balanced key design — mix positively and negatively worded items to neutralize acquiescence",
      "Latent-composite justification — interval treatment of summed scores validated via factor analysis, not convenience",
      "Points-per-item trade-off — 5 vs 7 vs 11 response categories: reliability gains against respondent burden",
    ],
    "apply": "Build public-service-motivation, trust, or red-tape scales from validated item batteries; pretest wording with Cognitive Interviews before fielding; check dimensionality with IRT & Factor Analysis and report α/ω alongside. Sensitivity-test ordinal alternatives (cumulative models) against the summed score (see Methodology Map: Survey Design & Sampling, Psychometrics & Scale Validation).",
  },

  "Guttman & Cumulative Scales": {
    "use": "A Guttman scale orders items so that endorsing a harder item implies endorsing all easier ones — revealing a single underlying continuum.",
    "explain": "Louis Guttman's scalogram model (1944, 1950) sought deterministic cumulative structure: items form a hierarchy (from tolerance of mild incivility to acceptance of corruption), and a respondent's total score locates them on that continuum. Perfect Guttman scales are rare; the model survives as a diagnostic ideal — reproducibility and scalability coefficients measure how close a set of items comes to cumulative ordering, informing scale purification before any averaging is justified.",
    "concepts": ["scalogram", "cumulative structure", "reproducibility coefficient", "scalability", "item hierarchy"],
    "founders": "Louis Guttman — 'A Basis for Scaling Qualitative Data' (1944) and 'The Basis for Scalogram Analysis' (1950); evaluation coefficients from Menzel (1953).",
    "classics": [
      "Guttman, L. (1944). 'A Basis for Scaling Qualitative Data,' American Sociological Review 9(2)",
      "Guttman, L. (1950). 'The Basis for Scalogram Analysis,' in Stouffer et al., Measurement and Prediction",
      "Menzel, H. (1953). 'A New Coefficient for Scalogram Analysis,' Public Opinion Quarterly",
    ],
    "frameworks": [
      "Scalogram model — deterministic cumulative ordering as the scaling ideal",
      "Reproducibility (REP ≥ .90) rule — the classic acceptability threshold for a cumulative scale",
      "Scalability coefficient — how well each item's difficulty ordering matches the total ordering",
      "Mokken scale analysis — probabilistic, nonparametric descendant testing monotone homogeneity",
    ],
    "apply": "Use when theory predicts a strict hierarchy: stages of e-government adoption, escalating citizen participation, tolerance gradients. Screen items with Mokken analysis before assuming additivity; report reproducibility alongside α. IRT & Factor Analysis models generalize the idea to probabilistic measurement (see Methodology Map: Psychometrics & Scale Validation).",
  },

  "Reflective vs Formative": {
    "use": "Decide whether the construct causes its indicators (reflective — satisfaction) or the indicators cause the construct (formative — socio-economic status); the wrong model makes weights meaningless and inference invalid.",
    "explain": "In reflective measurement, a latent construct (trust in government) manifests in interchangeable, correlated indicators; dropping one changes reliability, not meaning. In formative measurement, the construct (social vulnerability) is built from causally distinct components — income, housing, health — that need not correlate; omitting one changes the construct itself. Bollen & Lennox (1991) supplied the canonical diagnostic: indicator intercorrelations reveal the causal direction, and α is meaningless for formative composites.",
    "concepts": ["reflective indicator", "formative indicator", "indicator interchangeability", "composite reliability", "causal direction"],
    "founders": "Kenneth Bollen & Richard Lennox — 'Conventional Wisdom on Measurement: A Structural Equation Perspective,' Psychological Bulletin (1991); causal-indicator tradition extended by Edwards & Bagozzi.",
    "classics": [
      "Bollen, K., & Lennox, R. (1991). 'Conventional Wisdom on Measurement: A Structural Equation Perspective,' Psychological Bulletin 110(2)",
      "Edwards, J. R., & Bagozzi, R. P. (2000). 'On the Nature and Direction of Relationships Between Constructs and Measures,' Psychological Methods",
      "Diamantopoulos, A., & Winklhofer, H. M. (2001). 'Index Construction with Formative Indicators,' Journal of Marketing Research",
    ],
    "frameworks": [
      "Bollen–Lennox diagnostic — correlated indicators signal reflective; causal, non-redundant indicators signal formative",
      "External validation requirement — formative indexes must be validated against criteria outside the indicator set",
      "PLS/components debate — component scores as proxies when formative models resist identification",
      "Weighting schemes — equal weights vs expert weights vs data-driven weights (PCA, Machine Learning Prediction), with comparability consequences",
    ],
    "apply": "Classify every composite before analysis: is the transparency index formative (distinct components) and the corruption-perceptions index reflective (exchangeable manifestations)? Validate formative indexes against external criteria and justify weights; specify Structural Equation Modelling measurement blocks accordingly (see Methodology Map: Psychometrics & Scale Validation).",
  },

  # ================= VALIDITY =================

  "Content Validity": {
    "use": "Does the instrument cover the full domain it claims to measure — and nothing outside it? Content validity is established by expert judgment, not by statistics.",
    "explain": "Content validity asks whether the item sample represents the construct's domain. Lawshe (1975) converted expert judgments into a quantified content-validity ratio (CVR), and Lynn (1986) formalized minimum panel sizes and agreement thresholds. In survey work, content failure is the most common source of invalidity: a citizen-satisfaction battery that omits fairness, or adds service speed, measures the wrong construct no matter how reliable its scores are.",
    "concepts": ["domain sampling", "content validity ratio", "expert panel", "face validity", "domain representativeness"],
    "founders": "C. H. Lawshe — 'A Quantitative Approach to Content Validity,' Personnel Psychology (1975); Mary Lynn — 'Determination and Quantification of Content Validity,' Nursing Research (1986).",
    "classics": [
      "Lawshe, C. H. (1975). 'A Quantitative Approach to Content Validity,' Personnel Psychology 28(4)",
      "Lynn, M. R. (1986). 'Determination and Quantification of Content Validity,' Nursing Research 35(6)",
      "Nunnally, J. C., & Bernstein, I. H. (1994). Psychometric Theory (3rd ed.), chapters on validity",
    ],
    "frameworks": [
      "Lawshe CVR — (ne − N/2) / (N/2) threshold for rating items 'essential'",
      "Lynn's minimum-panel rule — at least 3 experts, 5 when chance agreement must be discounted",
      "Domain specification table — map each construct facet to items before drafting a single question",
      "Face vs content validity — surface plausibility to respondents vs representativeness of the domain",
    ],
    "apply": "Start any new PA scale (digital-government readiness, collaborative capacity) with a domain map and expert CVR ratings before piloting; document the item-to-domain mapping in the codebook. Content review precedes Cognitive Interviews in the validation pipeline (see Methodology Map: Psychometrics & Scale Validation, Survey Design & Sampling).",
  },

  "Construct Validity": {
    "use": "Does the instrument capture the abstract construct rather than a neighboring one? Establish it through convergent, discriminant, and nomological evidence.",
    "explain": "Cronbach & Meehl (1955) reconceived validity: a construct is a theoretical entity, and validating a test means validating inferences from its scores via a nomological network linking the construct to indicators and to other constructs. Campbell & Fiske's multitrait–multimethod matrix (1959) supplied the empirical engine — convergence across methods and discrimination across traits. Construct validity subsumes content, convergent, discriminant, and criterion evidence as parts of one argument.",
    "concepts": ["nomological network", "convergent evidence", "discriminant evidence", "construct underrepresentation", "validity inference"],
    "founders": "Lee Cronbach & Paul Meehl — 'Construct Validity in Psychological Tests,' Psychological Bulletin (1955); Donald Campbell & Donald Fiske — the MTMM matrix (1959).",
    "classics": [
      "Cronbach, L. J., & Meehl, P. E. (1955). 'Construct Validity in Psychological Tests,' Psychological Bulletin 52(4)",
      "Campbell, D. T., & Fiske, D. W. (1959). 'Convergent and Discriminant Validation by the Multitrait-Multimethod Matrix,' Psychological Bulletin 56(2)",
      "Messick, S. (1989). 'Validity,' in R. L. Linn (ed.), Educational Measurement (3rd ed.)",
    ],
    "frameworks": [
      "Cronbach–Meehl nomological network — the construct embedded in a web of lawful relations",
      "MTMM logic — trait variance should exceed method variance in the correlation matrix",
      "Convergent/discriminant triangulation — high same-trait cross-method, low same-method cross-trait",
      "Messick's unified view — validity as integrated evaluative judgment of score meaning and use",
    ],
    "apply": "When adapting trust, legitimacy, or PSM scales to a new language or country, treat re-validation as mandatory: correlate the adapted scale with the source-language original and with theoretically adjacent and distinct constructs. Nomological tests — does the construct predict policy support as theory requires? — anchor the argument (see Methodology Map: Psychometrics & Scale Validation, Structural Equation Modelling).",
  },

  "Criterion Validity": {
    "use": "Does the score predict an external criterion it should predict — now (concurrent) or later (predictive)? Evidence is a correlation against a gold standard.",
    "explain": "Criterion validity concerns correspondence with an external standard: a short burnout screen validated against a clinical interview (concurrent), civil-service exam scores validated against later job performance (predictive). The challenge is rarely statistical — it is the criterion itself. In public administration, true performance, true corruption, and true public value are imperfectly observable, so criterion validation becomes a judgment about which imperfect standard to trust, and how much incremental validity the new measure adds.",
    "concepts": ["concurrent validity", "predictive validity", "gold standard", "criterion contamination", "incremental validity"],
    "founders": "Rooted in the APA's Technical Recommendations for Psychological Tests (1954); consolidated in successive editions of the Standards for Educational and Psychological Testing (AERA/APA/NCME).",
    "classics": [
      "American Psychological Association (1954). 'Technical Recommendations for Psychological Tests and Diagnostic Techniques,' Psychological Bulletin 51(2)",
      "AERA, APA & NCME (2014). Standards for Educational and Psychological Testing",
      "Guion, R. M. (1980). 'On Trinitarian Doctrines of Validity,' Professional Psychology",
    ],
    "frameworks": [
      "Concurrent vs predictive — criterion timing determines the validation design",
      "Criterion deficiency vs contamination — the standard itself may be narrow or biased",
      "Incremental validity — does the new measure add prediction beyond existing cheap proxies?",
      "Multiple imperfect criteria — when no gold standard exists, triangulate several flawed ones",
    ],
    "apply": "Validate screening instruments against hard outcomes: does a citizen-experience score predict complaint escalation, or an audit score predict sanction? Document the criterion's own measurement error and report incremental R² over administrative baselines. Where criteria are latent (performance), build the case from multiple imperfect criteria (see Methodology Map: Machine Learning Prediction, OLS & Generalised Linear Models).",
  },

  "MTMM — Convergent & Discriminant": {
    "use": "Correlate multiple traits measured by multiple methods: true constructs converge across methods; method artifacts do not.",
    "explain": "Campbell & Fiske's (1959) multitrait–multimethod matrix is the classic empirical test of construct validity. The same trait measured by survey, behavioral trace, and expert rating should correlate strongly (convergent validity); different traits measured by the same method should correlate weakly (discriminant validity). Method effects — a halo in self-report, a bias in one agency's records — inflate same-method correlations and are exposed when trait correlations exceed method correlations.",
    "concepts": ["multitrait-multimethod matrix", "convergent coefficient", "discriminant coefficient", "method variance", "halo effect"],
    "founders": "Donald T. Campbell & Donald W. Fiske — 'Convergent and Discriminant Validation by the Multitrait-Multimethod Matrix,' Psychological Bulletin (1959).",
    "classics": [
      "Campbell, D. T., & Fiske, D. W. (1959). 'Convergent and Discriminant Validation by the Multitrait-Multimethod Matrix,' Psychological Bulletin 56(2)",
      "Widaman, K. F. (1985). 'Hierarchically Nested Covariance Structure Models for Multitrait-Multimethod Data,' Applied Psychological Measurement",
      "Eid, M. (2000). 'A Multitrait-Multimethod Model with Minimal Assumptions,' Psychometrika",
    ],
    "frameworks": [
      "MTMM matrix anatomy — validity diagonals vs heterotrait-heteromethod triangles",
      "Campbell–Fiske criteria — convergent correlations should be the highest in their row/column and exceed method correlations",
      "CT-C(M-1) latent models — modern MTMM separating trait from method factors",
      "Same-source warning — mono-method survey correlations as a method-artifact alarm",
    ],
    "apply": "Before trusting self-reported trust, performance, or network-tie data, triangulate at least one trait across methods: survey + digital trace, survey + administrative record. Estimate trait and method factors with Structural Equation Modelling to quantify method bias, and report whether trait effects survive it — vital for network surveys where name generators interact with method (see Methodology Map: Mixed-Methods SNA, Survey Design & Sampling).",
  },

  "Validity Argument (Messick / Kane)": {
    "use": "Validity is not a property of a test but a coherent argument from evidence and consequences — assemble it explicitly, inference by inference.",
    "explain": "Samuel Messick (1989) unified validity into a single construct: the degree to which evidence and theory support score interpretation for a proposed use — including the consequences of that use. Michael Kane reframed validation as argument-building: an interpretation/use argument (IUA) whose inferences and assumptions must each be backed by evidence, from scoring through generalization and extrapolation to implication. The argumentative turn replaced validation checklists with pre-structured validity arguments carrying explicit warrants.",
    "concepts": ["unified validity", "interpretation/use argument", "extrapolation", "consequential evidence", "warrant"],
    "founders": "Samuel Messick — 'Validity' (1989); Michael T. Kane — 'Validating the Interpretations and Uses of Test Scores' (2013) and the argument-based approach since 1992.",
    "classics": [
      "Messick, S. (1989). 'Validity,' in R. L. Linn (ed.), Educational Measurement (3rd ed.)",
      "Kane, M. T. (2013). 'Validating the Interpretations and Uses of Test Scores,' Journal of Educational Measurement 50(1)",
      "Cronbach, L. J. (1988). 'Five Perspectives on Validity Argument,' in H. Wainer (ed.), Test Validity",
    ],
    "frameworks": [
      "Messick's unified construct — content, substantive, structural, generalizability, external, and consequential facets",
      "Kane's IUA chain — scoring → generalization → extrapolation → implication, each with explicit assumptions",
      "Validity-argument templates — mapping which evidence answers which inference",
      "Consequential validity — uses of scores that systematically harm groups count against the interpretation",
    ],
    "apply": "For high-stakes PA measurement — performance regimes, audit scores, algorithmic risk indices — write the validity argument before publishing: what inference, what evidence per inference, what could invalidate it. Consequences count: a fairness index that punishes minority-serving agencies fails validity even at high reliability (see Methodology Map: Realist Evaluation, Theory-Based Evaluation for consequence-evidence designs).",
  },

  # ================= RELIABILITY =================

  "Test–Retest & Parallel Forms": {
    "use": "Repeat the measurement after a suitable interval (or use alternate forms) and correlate: stability over time and equivalence across forms are the oldest reliability evidences.",
    "explain": "Classical test theory separates a true score from random error by repeating measurement: the test–retest correlation estimates stability, provided the interval is short enough that the trait has not changed and long enough that respondents cannot recall answers. Parallel forms — different item samples drawn from the same domain — estimate equivalence without memory effects. Both assume a static construct; for malleable attitudes, low stability reflects real change, not error, which is why every reliability claim must state its interval.",
    "concepts": ["stability coefficient", "parallel forms", "practice & memory effects", "trait change vs measurement error", "time sampling"],
    "founders": "Classical test theory formulated by Charles Spearman (1904, 1910) and consolidated in Gulliksen's Theory of Mental Tests (1950).",
    "classics": [
      "Spearman, C. (1904). 'The Proof and Measurement of Association Between Two Things,' American Journal of Psychology",
      "Gulliksen, H. (1950). Theory of Mental Tests",
      "Lord, F. M., & Novick, M. R. (1968). Statistical Theories of Mental Test Scores",
    ],
    "frameworks": [
      "Classical test theory — X = T + E; reliability = true-score variance / total variance",
      "Stability–interval trade-off — too short invites memory inflation, too long invites trait drift",
      "Parallel-forms assumption — equal true scores and equal error variances across forms",
      "Reliability of change — repeated-measure designs need reliability at each wave, not just of the difference",
    ],
    "apply": "Report test–retest correlations with the interval stated for any new PA scale; use alternate forms across panel waves to control item memory. Interpret low stability jointly with known trait volatility (trust after crises), and propagate wave-level reliability into change-score estimates in Panel & Fixed-Effects Models (see Methodology Map: Survey Design & Sampling).",
  },

  "Internal Consistency — α & ω": {
    "use": "A scale is internally consistent when its items correlate strongly enough to be exchangeable manifestations of one latent score; coefficient α estimates this, and ω improves on it.",
    "explain": "Cronbach's α (1951) is the expected correlation of the total score with all possible same-length splits of the items — a lower bound to reliability under essentially tau-equivalent assumptions. Those assumptions are often violated: unequal loadings make α underestimate reliability, while multidimensionality can leave it looking respectable while the score mixes constructs. McDonald's ω models unequal loadings through a factor model and is generally the better estimator; both presuppose a unidimensionality check.",
    "concepts": ["coefficient alpha", "essential tau-equivalence", "McDonald's omega", "unidimensionality", "split-half logic"],
    "founders": "Lee Cronbach — 'Coefficient Alpha and the Internal Structure of Tests' (1951); Roderick McDonald — Test Theory: A Unified Treatment (1999).",
    "classics": [
      "Cronbach, L. J. (1951). 'Coefficient Alpha and the Internal Structure of Tests,' Psychometrika 16(3)",
      "McDonald, R. P. (1999). Test Theory: A Unified Treatment",
      "Sijtsma, K. (2009). 'On the Use, the Misuse, and the Very Limited Usefulness of Cronbach's Alpha,' Psychometrika",
    ],
    "frameworks": [
      "Cronbach's α — lower-bound estimator under essential tau-equivalence",
      "McDonald's ω — factor-model reliability allowing unequal loadings",
      "α-if-item-deleted diagnostics — scale purification vs shotgun item dropping",
      "Unidimensionality precondition — composite reliability presumes one factor",
    ],
    "apply": "Report ω (and α) with factor loadings for every multi-item scale — PSM subscales, relational batteries, red-tape indexes; never report α for formative composites. Run IRT & Factor Analysis before trusting either number, and use α-if-deleted only to spot redundancy (see Methodology Map: Psychometrics & Scale Validation).",
  },

  "Inter-Rater Reliability — κ & ICC": {
    "use": "When judgment is the instrument — coding documents, auditing agencies, annotating text — agreement between raters must be quantified and chance-corrected.",
    "explain": "Raw percent agreement overstates reliability because raters agree by chance, especially with skewed category distributions. Cohen's κ (1960) corrects for chance agreement between two raters; Fleiss' κ generalizes to many; Krippendorff's α handles missing data and any measurement level. For continuous or ordinal judgments, the intraclass correlation partitions variance into target and rater components. Conventions (κ ≥ .60 acceptable, ≥ .80 strong) are heuristics — the right benchmark depends on decision stakes.",
    "concepts": ["chance correction", "Cohen's kappa", "Krippendorff's alpha", "intraclass correlation", "adjudication"],
    "founders": "Jacob Cohen — 'A Coefficient of Agreement for Nominal Scales' (1960); Klaus Krippendorff — Content Analysis (1980); ICC formalized by Bartko and Shrout & Fleiss.",
    "classics": [
      "Cohen, J. (1960). 'A Coefficient of Agreement for Nominal Scales,' Educational and Psychological Measurement 20(1)",
      "Fleiss, J. L. (1971). 'Measuring Nominal Scale Agreement Among Many Raters,' Psychological Bulletin",
      "Shrout, P. E., & Fleiss, J. L. (1979). 'Intraclass Correlations: Uses in Assessing Rater Reliability,' Psychological Bulletin",
    ],
    "frameworks": [
      "Cohen's κ — observed minus chance agreement, normalized; weighted κ for ordinal data",
      "Fleiss' κ & Krippendorff's α — many raters, missing values, multiple measurement levels",
      "ICC(2,k) — average-rating reliability for continuous coding",
      "Annotation pipeline — pilot → codebook iteration → double-coding ≥ 20% → adjudication",
    ],
    "apply": "Mandatory for qualitative coding of policy documents, interview transcripts, and administrative records: double-code a random 20%, report κ/α/ICC, and feed disagreements into a revised codebook. For LLM-assisted coding, report human–model agreement on the same chance-corrected footing (see Methodology Map: Qualitative Content Analysis, LLM-Assisted Qualitative Coding, Thematic Analysis).",
  },

  "Standard Error of Measurement": {
    "use": "Every observed score carries a standard error; the SEM converts reliability into the confidence interval around a unit's true score.",
    "explain": "The SEM is the standard deviation of the error component in classical test theory: SEM = SD·√(1−r). Expressed in score units, it supports individual-level inference — a band around an observed score estimates where the true score likely lies. It underlies decisions about thresholds and cutoffs, and it powers the correction for attenuation that connects reliability to causal inference: knowing the SEM turns reliability from a summary statistic into a working quantity.",
    "concepts": ["error component", "true-score band", "conditional SEM", "attenuation", "decision consistency"],
    "founders": "Derivable from Spearman's true-score model (1904); standard presentation in Gulliksen (1950) and Lord & Novick (1968).",
    "classics": [
      "Gulliksen, H. (1950). Theory of Mental Tests",
      "Lord, F. M., & Novick, M. R. (1968). Statistical Theories of Mental Test Scores",
      "Harvill, L. M. (1991). 'Standard Error of Measurement,' Educational Measurement: Issues and Practice",
    ],
    "frameworks": [
      "SEM = SD·√(1−r) — error expressed in score units",
      "Conditional SEM — precision varies across the score range under IRT",
      "Decision consistency — SEM-based bands around cutoffs in high-stakes uses",
      "Correction for attenuation — disattenuating correlations and slopes by measured reliability",
    ],
    "apply": "Before declaring agencies above or below a performance threshold, compute SEM-based bands — many published rankings sit within measurement noise. Disattenuate key correlations (e.g., trust → compliance) before interpreting effect sizes, and report conditional SEM across the trait range where IRT & Factor Analysis is used (see Methodology Map: Psychometrics & Scale Validation).",
  },

  "Generalizability Theory": {
    "use": "Reliability is never one number: decompose score variance across persons, items, occasions, and raters simultaneously, then design the measurement to minimize error for its actual purpose.",
    "explain": "Cronbach, Gleser, Nanda & Rajaratnam's generalizability theory treats every measurement facet as a potential random effect. A G-study estimates all variance components; a D-study asks what happens under changed designs — more items, fewer raters, different occasions — yielding a generalizability coefficient for the intended decision. It subsumes test–retest, parallel-forms, and inter-rater reliability as special cases of one ANOVA-like framework, and it converts reliability from a reported statistic into a design tool.",
    "concepts": ["variance components", "G-study", "D-study", "facets", "generalizability coefficient"],
    "founders": "Lee Cronbach, Goldine Gleser, Harinder Nanda & Nageswari Rajaratnam — The Dependability of Behavioral Measurements (1972; originating papers 1963–65).",
    "classics": [
      "Cronbach, L. J., Rajaratnam, N., & Gleser, G. C. (1963). 'Theory of Generalizability: A Liberalization of Reliability Theory,' British Journal of Statistical Psychology",
      "Rajaratnam, N., Cronbach, L. J., & Gleser, G. C. (1965). 'Generalizability of Stratified-Parallel Tests,' Psychometrika",
      "Cronbach, L. J., Gleser, G. C., Nanda, H., & Rajaratnam, N. (1972). The Dependability of Behavioral Measurements",
    ],
    "frameworks": [
      "G-study — estimate variance components for person × item × rater × occasion designs",
      "D-study — optimize the design: which facet deserves more items, at what cost",
      "Relative vs absolute decisions — G coefficient vs Phi for norm- vs criterion-referenced uses",
      "Nested and crossed facets — the design grammar of multi-facet measurement",
    ],
    "apply": "Use when several error sources coexist: citizen panels rating multiple services on multiple occasions, or agencies audited by rotating teams on changing criteria. Estimate variance components to show whether error lives in items, raters, or occasions, and reallocate the measurement budget accordingly; Multilevel / Hierarchical Models provide the estimation engine (see Methodology Map: Psychometrics & Scale Validation).",
  },

  # ================= ERROR & BIAS =================

  "Random Error & Attenuation": {
    "use": "Unsystematic noise inflates variance and — worse — attenuates every correlation with the mismeasured variable toward zero, shrinking the effects you care about.",
    "explain": "Random error is uncorrelated noise around the true score: slips, guesses, momentary mood. Its best-known consequence is attenuation — observed correlations equal true correlations multiplied by the square root of the product of the two reliabilities (Spearman 1904). A trust scale with reliability .70 caps any true correlation with trust near .84 even when the other measure is perfect. Random error also inflates standard errors and distorts interactions, making noisy measurement an enemy of causal identification as much as of effect size.",
    "concepts": ["attenuation", "error variance inflation", "disattenuation", "reliability ceiling", "errors-in-variables"],
    "founders": "Charles Spearman — 'The Proof and Measurement of Association Between Two Things' (1904); the disattenuation formula is classical test theory's first practical product.",
    "classics": [
      "Spearman, C. (1904). 'The Proof and Measurement of Association Between Two Things,' American Journal of Psychology 15(1)",
      "Spearman, C. (1910). 'Correlation Calculated from Faulty Data,' British Journal of Psychology",
      "Schmidt, F. L., & Hunter, J. E. (1996). 'Measurement Error in Psychological Research,' Psychological Methods",
    ],
    "frameworks": [
      "Spearman attenuation formula — r_observed = r_true · √(r_xx · r_yy)",
      "Correction for attenuation — divide by reliabilities; propagate the uncertainty",
      "Measurement-error sensitivity — bound conclusions across plausible reliability ranges",
      "Errors-in-variables regression — structural approaches when reliabilities are unknown",
    ],
    "apply": "Quantify attenuation before interpreting null or small effects: a non-finding may be a ceiling imposed by measurement error, not evidence of no effect. Apply disattenuation via Structural Equation Modelling latent variables or reliability bounds, and report sensitivity across plausible reliabilities — critical for self-reported mediators in causal chains (see Methodology Map: OLS & Generalised Linear Models).",
  },

  "Systematic Bias & Response Styles": {
    "use": "Respondents differ in how they use scales — acquiescence, extremity, midpoint responding — fabricating group differences that masquerade as substance.",
    "explain": "Response styles are stable individual tendencies unrelated to content: acquiescent respondents agree regardless of item direction; extreme responders favor scale ends; midpoint selectors avoid commitment. Because styles correlate with culture, age, and education, naive comparisons across groups confound substance with style — a measured 'gap' in trust between countries may partly be a gap in willingness to agree. Remedies include balanced item keys, anchoring vignettes, and modeling style as a latent variable.",
    "concepts": ["acquiescence bias", "extremity responding", "midpoint responding", "balanced keys", "anchoring vignettes"],
    "founders": "Survey methodology tradition — Likert's balanced scales (1932), modern measurement models from Krosnick & Presser; anchoring vignettes from King, Murray, Salomon & Tandon (2004).",
    "classics": [
      "Krosnick, J. A. (1991). 'Response Strategies for Coping with the Cognitive Demands of Attitude Measures in Surveys,' Applied Cognitive Psychology",
      "King, G., Murray, C. J. L., Salomon, J. A., & Tandon, A. (2004). 'Enhancing the Validity and Cross-Cultural Comparability of Measurement in Survey Research,' American Political Science Review",
      "Baumgartner, H., & Steenkamp, J.-B. E. M. (2001). 'Response Styles in Marketing Research,' Journal of Marketing Research",
    ],
    "frameworks": [
      "Balanced key design — positively and negatively worded items cancel acquiescence",
      "Anchoring vignettes — self-assessment anchors recover interpersonal comparability",
      "Multidimensional item response models — content and style as separate latent traits",
      "Extremity diagnostics — within-person variance and category-usage profiles as style indicators",
    ],
    "apply": "For cross-national PA surveys, test differential item functioning by country before comparing means; add anchoring vignettes when resources allow. Within one country, check whether subgroup gaps survive style-adjusted scoring, using IRT & Factor Analysis to separate content from style (see Methodology Map: Survey Design & Sampling, Psychometrics & Scale Validation).",
  },

  "Common Method Variance": {
    "use": "When predictor and outcome come from the same respondent, instrument, and time point, shared method variance can manufacture correlations — design it away before you analyze it away.",
    "explain": "Podsakoff et al. (2003) systematized a worry older than their label: mono-source designs inflate correlations through consistency motives, implicit theories, social desirability, and item-context effects. The remedy hierarchy starts with design — separate sources, separate times, marker variables — and only then with statistics (Harman's test, latent method factors, measured markers). The statistical cures are contested; the procedural cures are not.",
    "concepts": ["mono-method bias", "consistency motive", "marker variable", "latent method factor", "temporal separation"],
    "founders": "Philip Podsakoff, Scott MacKenzie, Jeong-Yeon Lee & Nathan Podsakoff — 'Common Method Biases in Behavioral Research,' Journal of Applied Psychology (2003); substantive lineage in Campbell & Fiske (1959).",
    "classics": [
      "Podsakoff, P. M., MacKenzie, S. B., Lee, J.-Y., & Podsakoff, N. P. (2003). 'Common Method Biases in Behavioral Research,' Journal of Applied Psychology 88(5)",
      "Podsakoff, P. M., MacKenzie, S. B., & Podsakoff, N. P. (2012). 'Sources of Method Bias in Social Science Research,' Annual Review of Psychology",
      "Campbell, D. T., & Fiske, D. W. (1959). 'Convergent and Discriminant Validation by the MTMM Matrix,' Psychological Bulletin",
    ],
    "frameworks": [
      "Procedural remedies first — psychological, source, and temporal separation",
      "Marker variable technique — partial out a theoretically unrelated construct",
      "Latent method factor models — method factors orthogonal to traits (contested but common)",
      "Dyad triangulation — employee–supervisor or citizen–official paired informants",
    ],
    "apply": "In PA surveys of leadership, trust, or red tape, avoid asking one respondent both X and Y when feasible: use supervisor performance ratings, administrative outcomes, or lagged waves. Where single-source is unavoidable, separate scale blocks, reverse-key some items, and estimate method effects explicitly under Structural Equation Modelling (see Methodology Map: Survey Design & Sampling).",
  },

  "Mode & Interviewer Effects": {
    "use": "The channel of data collection — face-to-face, phone, web, paper — itself changes responses; so does the presence and behavior of an interviewer.",
    "explain": "Mode effects arise because channels differ in social presence, privacy, cognitive burden, and channel capacity: acquiescence and satisficing fall in self-administered modes, while socially desirable answers drift toward norms in interviewer modes. Interviewer effects add variance between interviews conducted by different people, measurable as an interviewer-level ICC. Both are design variables, not noise: mixed-mode strategies trade coverage gains against measurement comparability, and equivalence must be tested before pooling.",
    "concepts": ["social desirability", "acquiescence by mode", "interviewer variance", "mode comparability", "mixed-mode design"],
    "founders": "Survey methodology tradition — Dillman's mode comparisons; Groves, Fowler, Couper, Lepkowski, Singer & Tourangeau, Survey Methodology (2009); interviewer effects systematized by Groves & Magilavy.",
    "classics": [
      "Dillman, D. A. (2000). Mail and Internet Surveys: The Tailored Design Method",
      "Groves, R. M., Fowler, F. J., Couper, M. P., Lepkowski, J. M., Singer, E., & Tourangeau, R. (2009). Survey Methodology (2nd ed.)",
      "de Leeuw, E. D. (2005). 'To Mix or Not to Mix Data Collection Modes in Surveys,' Journal of Official Statistics",
    ],
    "frameworks": [
      "Mode taxonomy — interviewer-administered vs self-administered; presence of visual aids",
      "Social presence theory — more presence, more desirability and acquiescence",
      "Interviewer variance decomposition — intra-interviewer correlation as a design parameter",
      "Mixed-mode equivalence testing — measurement invariance across modes before pooling",
    ],
    "apply": "Before pooling web and phone waves of a citizen panel, run measurement-invariance tests across modes; if scalar invariance fails, model mode as a grouping variable. In establishment surveys of public organizations, document mode and interviewer assignment, and estimate interviewer ICCs with Multilevel / Hierarchical Models (see Methodology Map: Survey Design & Sampling).",
  },

  "Missing Data & Nonresponse Bias": {
    "use": "Missingness is rarely random: item gaps, wave attrition, and unit nonresponse follow propensities that can bias every estimate — diagnose the mechanism, then model it.",
    "explain": "Rubin's (1976) taxonomy separates missing completely at random (MCAR), at random (MAR — explainable by observed variables), and not at random (MNAR — dependent on unobserved values). Listwise deletion assumes MCAR and burns power; multiple imputation handles MAR; MNAR demands sensitivity analysis or selection models. And nonresponse bias equals nonresponse rate times the respondent–nonrespondent difference — a low response rate with balanced respondents is safer than a moderate rate with skewed participation.",
    "concepts": ["MCAR / MAR / MNAR", "item vs unit nonresponse", "attrition", "multiple imputation", "nonresponse bias formula"],
    "founders": "Donald Rubin — 'Inference and Missing Data,' Biometrika (1976); comprehensive treatment in Little & Rubin (2002).",
    "classics": [
      "Rubin, D. B. (1976). 'Inference and Missing Data,' Biometrika 63(3)",
      "Little, R. J. A., & Rubin, D. B. (2002). Statistical Analysis with Missing Data (2nd ed.)",
      "Groves, R. M. (2006). 'Nonresponse Rates and Nonresponse Bias in Household Surveys,' Public Opinion Quarterly",
    ],
    "frameworks": [
      "Rubin's taxonomy — MCAR / MAR / MNAR as design diagnostics",
      "Groves' bias formula — bias risk rises with rate × respondent–nonrespondent difference",
      "Multiple imputation by chained equations — principled MAR-based inference",
      "Attrition analysis — compare stayers vs leavers on wave-1 observables; weight or model the gap",
    ],
    "apply": "For panels of public servants or citizen panels, model attrition propensity and apply Weighting & Non-Response Adjustment or imputation; report response rates by subgroup and sensitivity to MNAR assumptions. In administrative-data linkage, treat linkage failure as its own missing-data mechanism with a dedicated bias analysis (see Methodology Map: Propensity Score Matching, Multilevel / Hierarchical Models).",
  },

  # ================= DATA SOURCES =================

  "Survey Data": {
    "use": "Probability-sample surveys remain the only source for attitudes, perceptions, and reported behavior — what citizens and officials think, know, and claim to do.",
    "explain": "Surveys measure what registers and records cannot: trust, perceived fairness, internal states, and counterfactual claims. Their weaknesses are structural: self-report bias, social desirability, recall error, and rising nonresponse. Modern practice treats survey methodology as its own discipline — frame design, questionnaire construction, mode selection, nonresponse management, and weighting are measurement decisions that determine validity as much as the items do.",
    "concepts": ["probability sampling", "question wording", "recall error", "social desirability", "post-stratification weights"],
    "founders": "George Gallup's polling program and the Michigan Survey Research Center's probability revolution; standards consolidated by AAPOR and in Groves et al., Survey Methodology (2009).",
    "classics": [
      "Groves, R. M., Fowler, F. J., Couper, M. P., Lepkowski, J. M., Singer, E., & Tourangeau, R. (2009). Survey Methodology (2nd ed.)",
      "Krosnick, J. A., & Presser, S. (2010). 'Question and Questionnaire Design,' in Handbook of Survey Research",
      "Dillman, D. A., Smyth, J. D., & Christian, L. M. (2014). Internet, Phone, Mail, and Mixed-Mode Surveys: The Tailored Design Method (4th ed.)",
    ],
    "frameworks": [
      "Total survey error — sampling + nonresponse + measurement + coverage as one error budget",
      "Cognitive response process — comprehension → retrieval → judgment → response",
      "Mode-by-population fit — match channel to access and topic sensitivity",
      "Weighting pipeline — design weights → nonresponse adjustment → post-stratification",
    ],
    "apply": "Design PA surveys as measurement instruments: pretest with Cognitive Interviews, randomize question-order experiments, report AAPOR response rates, and archive items with weights. Calibrate self-report against administrative benchmarks, and remember frame quality dominates sampling error in establishment surveys (see Methodology Map: Survey Design & Sampling, Weighting & Non-Response Adjustment).",
  },

  "Administrative & Register Data": {
    "use": "Government records — births, taxes, benefits, casework, procurement — offer full-population coverage and longitudinal depth without recall error: they measure what institutions did, not what people say.",
    "explain": "Register data arise as byproducts of administration: near-universal coverage, timestamps, and linkage keys make them the strongest source for longitudinal and causal designs. But registers measure institutional categories — what a system records is shaped by its rules, incentives, and recording practices, producing classification drift, selection into the register itself, and access regimes governed by privacy law. Cross-country comparison often compares recording systems, not behaviors.",
    "concepts": ["register population", "classification drift", "linkage keys", "measurement by administration", "data governance"],
    "founders": "Nordic register tradition (Statistics Denmark, Statistics Sweden); methodological consolidation in Wallgren & Wallgren, Register-Based Statistics (2007), and in economics' administrative-data turn.",
    "classics": [
      "Wallgren, A., & Wallgren, B. (2007). Register-Based Statistics: Administrative Data for Statistical Purposes",
      "Card, D., Chetty, R., Feldstein, M., & Saez, E. (2010). 'Expanding Access to Administrative Data for Research in the United States,' white paper",
      "Connelly, R., Playford, C. J., Gayle, V., & Dibben, C. (2016). 'The Role of Administrative Data in the Big Data Revolution,' Social Science Research",
    ],
    "frameworks": [
      "Byproduct measurement — administrative categories are constructed, not natural",
      "Linkage architecture — deterministic vs probabilistic record linkage",
      "Population vs process coverage — who enters the register, and when",
      "Governance pipeline — legal basis → anonymization → safe rooms → reproducibility",
    ],
    "apply": "Exploit registers for full-population studies of welfare trajectories, procurement networks, and public employment careers with Survival & Event History Analysis and Panel & Fixed-Effects Models; document category definitions and their change over time as metadata. Treat register entry itself as a treatment or selection mechanism where relevant (see Methodology Map: Natural Experiments, Propensity Score Matching).",
  },

  "Digital Trace Data": {
    "use": "Search queries, social media, platform logs, and mobility traces capture behavior at scale in real time — nonreactive, high-frequency, and full of selection and construct traps.",
    "explain": "Digital traces promise measurement of revealed behavior: what people do when no one asks. They are nonreactive, fine-grained, and massive. But they are profoundly selected — platform users differ from populations; algorithms shape what is visible; the meaning of a trace is platform-specific (a post is not an opinion, a search is not a need). Construct validity, not sample size, is the binding constraint on inference from digital traces.",
    "concepts": ["digital footprint", "nonreactivity", "platform bias", "construct drift", "API access"],
    "founders": "Computational social science — Lazer et al. (2009); the critical tradition of boyd & Crawford (2012) and Tufekci (2014); methodological synthesis in Salganik, Bit by Bit (2018).",
    "classics": [
      "Lazer, D., et al. (2009). 'Computational Social Science,' Science 323(5915)",
      "boyd, d., & Crawford, K. (2012). 'Critical Questions for Big Data,' Information, Communication & Society 15(5)",
      "Salganik, M. J. (2018). Bit by Bit: Social Research in the Digital Age",
    ],
    "frameworks": [
      "Total error for big data — representation + construct + algorithmic + drift errors",
      "Nonreactive advantage vs platform-mediated selection",
      "Found vs designed data — observational traces lack the survey's design layer",
      "Algorithmic confounding — recommender systems structure the traces we analyze",
    ],
    "apply": "Use traces to complement, not replace, surveys: mobility for protest turnout, search for issue salience, platform data for network structure. Validate constructs against survey benchmarks (does sentiment track approval?), report platform demographics as coverage statements, and plan for API deprecation — NLP & Topic Modeling is the standard toolkit (see Methodology Map: Machine Learning Prediction, Text Mining + Close Reading).",
  },

  "Unobtrusive & Archival Data": {
    "use": "Documents, minutes, budgets, and institutional records created for non-research purposes let you observe organizations without disturbing them — with provenance and context as the core measurement questions.",
    "explain": "Unobtrusive measures (Webb et al., 1966) sidestep reactivity: official records, physical traces, and content archives. Their validity hinges on two questions — why was this record created, and what survived? Public administration runs on paper and portals: council minutes, procurement notices, FOIA releases, agency reports. Archival sources require treating the archive as a constructed collection with selection rules, silences, and custodial history — not a neutral mirror of the past.",
    "concepts": ["reactivity avoidance", "provenance", "record silences", "document sampling frames", "triangulation"],
    "founders": "Eugene Webb, Donald Campbell, Richard Schwartz & Lee Sechrest — Unobtrusive Measures (1966); the archival-science tradition from Jenkinson to Schellenberg.",
    "classics": [
      "Webb, E. J., Campbell, D. T., Schwartz, R. D., & Sechrest, L. (1966). Unobtrusive Measures: Nonreactive Research in the Social Sciences",
      "Scott, J. (1990/2014). A Matter of Record: Documentary Sources in Social Research",
      "Prior, L. (2003). Using Documents in Social Research",
    ],
    "frameworks": [
      "Record creation theory — documents as products of organizational routines and incentives",
      "Archive as collection — custodial history, selection, and silences bias any sample",
      "Document sampling frames — universe definition: which bodies, which years, which series",
      "Corroboration hierarchy — triangulate records against testimony and physical traces",
    ],
    "apply": "Study policy development from minutes and drafts; map procurement networks from tender notices; measure transparency from what agencies publish versus what they must. Build document sampling frames explicitly (series, years, custodians), code with validated schemes and reported inter-rater reliability, and read records against their production context (see Methodology Map: Archival & Historical Methods, Qualitative Content Analysis, Comparative Historical Analysis).",
  },

  "Ethnographic & Field Observation": {
    "use": "Sustained presence inside organizations reveals what records and surveys cannot — practice as it happens, meaning as actors make it.",
    "explain": "Ethnographic measurement trades standardization for depth: participant observation, field notes, and informal conversation capture tacit knowledge, informal norms, and the gap between formal rules and actual work. The 'measurement' is the fieldworker's disciplined attention under a documented protocol. Validity claims rest on prolonged engagement, triangulation across sites and informants, and a transparent audit trail from raw notes to interpretation.",
    "concepts": ["participant observation", "field notes", "thick description", "informal norms", "reflexivity"],
    "founders": "Bronisław Malinowski's fieldwork charter; organizational ethnography from the Chicago school through Whyte's Street Corner Society (1943) to Van Maanen's Tales of the Field (1988).",
    "classics": [
      "Malinowski, B. (1922). Argonauts of the Western Pacific",
      "Whyte, W. F. (1943). Street Corner Society",
      "Van Maanen, J. (1988/2011). Tales of the Field: On Writing Ethnography",
    ],
    "frameworks": [
      "From observation to note — jottings → expanded notes → analytic memos as the measurement chain",
      "Thick description (Geertz) — behavior plus its context and meaning",
      "Fieldwork validity strategies — prolonged engagement, persistent observation, triangulation, member checks",
      "Access as a data-quality variable — critical vs typical sites shape what can be seen",
    ],
    "apply": "Deploy when the construct is practice itself: street-level discretion, coproduction encounters, crisis management in control rooms. Combine observation logs with Semi-Structured Interviews and document analysis, and systematize notes into codeable corpora. Digital extensions widen the field to online policy communities (see Methodology Map: Ethnography & Participant Observation, Digital & Virtual Ethnography, Grounded Theory).",
  },

  # ================= SAMPLING & COVERAGE =================

  "Probability Sampling": {
    "use": "Random selection from a defined frame is the only design that guarantees representativeness in expectation — every alternative borrows credibility it has not earned.",
    "explain": "Probability sampling gives every population element a known, non-zero inclusion probability, making design-based inference possible: unbiased estimates with measurable standard errors. Simple random sampling is the ideal; stratification reduces variance by subgroup; cluster and multistage designs cut cost at the price of design effects; PPS sampling handles unequal-size units — the standard in surveys of organizations and officials.",
    "concepts": ["inclusion probability", "stratification", "clustering & design effect", "PPS sampling", "Horvitz–Thompson estimator"],
    "founders": "Laplace's 1802 birth-rate estimation; Neyman's stratification theory (1934); Hansen & Hurwitz (1943) for unequal-probability sampling.",
    "classics": [
      "Neyman, J. (1934). 'On the Two Different Aspects of the Representative Method,' Journal of the Royal Statistical Society 97(4)",
      "Kish, L. (1965). Survey Sampling",
      "Lohr, S. L. (2021). Sampling: Design and Analysis (3rd ed.)",
    ],
    "frameworks": [
      "Design-based inference — randomization lives in the selection, not in a model",
      "Stratified sampling — proportional or optimal allocation on known covariates",
      "Multistage cluster designs — PSUs → SSUs, with design effects (deff) as the cost metric",
      "PPS for organizations — probability proportional to size solves unequal agency rosters",
    ],
    "apply": "Sample public officials via stratified multistage designs (region × level × function), agencies via PPS from registers, and citizens via address-based frames. Always carry design weights and report design effects; stratify on organizational variables (size, sector) that drive the outcomes of interest (see Methodology Map: Survey Design & Sampling, Weighting & Non-Response Adjustment).",
  },

  "Non-Probability Sampling": {
    "use": "Convenience, quota, and opt-in online samples trade random selection for speed and reach — usable with modeling caveats, dangerous under naive inference.",
    "explain": "Non-probability samples lack known inclusion probabilities: student pools, volunteer panels, river samples. Their bias can be modeled — post-stratification on many covariates, sample matching, MRP-style multilevel regression — but the modeling assumptions are untestable without a probability benchmark. Transparent reporting and bias audits against gold-standard surveys are the community's answer, and even then selection on unobservables remains an open risk.",
    "concepts": ["opt-in panels", "quota sampling", "post-stratification", "MRP", "selection on unobservables"],
    "founders": "AAPOR Online Panel Task Force reports (2010–2013); Rivers on opt-in panels; multilevel regression and post-stratification from Gelman & Little (1997).",
    "classics": [
      "Baker, R., et al. (2010). 'Research Synthesis: AAPOR Report on Online Panels,' Public Opinion Quarterly",
      "Rivers, D. (2007). 'Sampling for Web Surveys,' proceedings of the Joint Statistical Meetings",
      "Gelman, A., & Little, T. C. (1997). 'Poststratification into Many Categories Using Hierarchical Logistic Regression,' Survey Methodology",
    ],
    "frameworks": [
      "Opt-in bias anatomy — coverage + self-selection + panel conditioning",
      "Calibration weighting — raking to margins; its limits when unobservables drive selection",
      "MRP — multilevel models + post-stratification for small-area and group estimates",
      "Benchmark audit — compare against probability gold standards and document divergence",
    ],
    "apply": "For hard-to-reach PA populations (mayors, procurement officers), prefer register frames or targeted designs over open links; if opt-in panels are unavoidable, post-stratify on political and demographic covariates with Multilevel / Hierarchical Models and audit against official statistics. Report the design as non-probability so readers can weigh it (see Methodology Map: Survey Design & Sampling, Weighting & Non-Response Adjustment).",
  },

  "Sampling Error & Sample Size": {
    "use": "Random samples differ from populations by chance alone; sample size governs that error, and power analysis turns it into a design decision made before fieldwork.",
    "explain": "Sampling error shrinks with the square root of n — quadrupling the sample halves the standard error. Statistical power is the probability of detecting an effect of a given size; underpowered studies miss real effects and inflate the ones they find (the winner's curse). Power inputs — effect size, alpha, power, design effect — should fix n before data collection; cluster designs multiply required n by the design effect, and subgroup analyses multiply it again.",
    "concepts": ["standard error", "power (1−β)", "minimum detectable effect", "design effect", "winner's curse"],
    "founders": "The Neyman–Pearson framework (1933); Jacob Cohen's power analyses (1962, 1988) that made underpowered research impossible to ignore.",
    "classics": [
      "Neyman, J., & Pearson, E. S. (1933). 'On the Problem of the Most Efficient Tests of Statistical Hypotheses,' Philosophical Transactions of the Royal Society A 231",
      "Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences (2nd ed.)",
      "Gelman, A., & Carlin, J. (2014). 'Beyond Power Calculations: Assessing Type S (Sign) and Type M (Magnitude) Errors,' Perspectives on Psychological Science",
    ],
    "frameworks": [
      "SE ∝ 1/√n — the square-root law of precision",
      "MDE = (z_{1−α/2} + z_{1−β})·SE — the smallest detectable effect as a design output",
      "Design effect — clustering and weighting inflate variance: n_eff = n / deff",
      "Type S/M errors — sign and magnitude errors dominate in small samples",
    ],
    "apply": "Power PA field experiments and survey experiments on plausible effect sizes from prior literature, not conventions like d = 0.2; inflate for cluster randomization at the school or agency level. Pre-register subgroup analyses and their required n, and report achieved power and MDE alongside results — for fixed budgets, optimal allocation formulas beat uniform sampling (see Methodology Map: Field Experiments & RCTs, Survey Experiments & Conjoint, OLS & Generalised Linear Models).",
  },

  "Coverage Error & Sampling Frames": {
    "use": "A frame is the operational list of who can be sampled; its mismatches with the target population — missing, duplicated, ineligible entries — create coverage error that sampling cannot repair.",
    "explain": "Coverage error is the gap between the target population and the frame population: registers miss informal organizations, web panels miss the offline, and lists of mayors go stale. Undercoverage of mobile or marginalized groups biases even perfectly executed random samples. Frame evaluation — match rates, vacancy rates, duplication — is a measurable design step, and multiple-frame designs (register + area + web) are the standard repair when no single list suffices.",
    "concepts": ["frame population vs target population", "undercoverage", "frame duplication", "multiple-frame sampling", "frame evaluation"],
    "founders": "The frame concept in Kish (1965); total survey error treatment in Groves et al. (2009); multiple-frame methodology from Hartley (1962, 1974).",
    "classics": [
      "Kish, L. (1965). Survey Sampling",
      "Groves, R. M., et al. (2009). Survey Methodology (2nd ed.), chapter on coverage and frames",
      "Hartley, H. O. (1974). 'Multiple Frame Methodology and Selected Applications,' Sankhyā 36",
    ],
    "frameworks": [
      "Coverage error anatomy — separate undercoverage from overcoverage and ineligibility",
      "Frame quality metrics — match rate, vacancy rate, duplication rate, freshness",
      "Dual/multiple-frame estimators — Hartley weights combine overlapping frames",
      "Frame maintenance — update cycles and churn registers for elite populations",
    ],
    "apply": "Audit frames before PA establishment surveys: how current is the roster of municipalities, NGOs, or procurement officers? Combine registers with area frames when informal providers matter, and quantify undercoverage against benchmarks. For elite surveys, refresh frames continuously — office turnover is coverage decay (see Methodology Map: Survey Design & Sampling, Expert & Elite Interviews).",
  },

  "Nonresponse & Weighting": {
    "use": "Nonresponse converts the designed sample into an achieved sample; weighting restores known population totals but cannot fix what it cannot see — measure and report both.",
    "explain": "Unit nonresponse follows measurable propensities: busy professionals, distrustful citizens, and marginalized groups respond less. Post-stratification and calibration weighting (raking, GREG estimators) align the achieved sample to known margins; response-propensity models and nonresponse adjustment cells target the same end. Diagnostics — R-indicators, weight distributions — quantify remaining imbalance, and sensitivity analysis bounds what weighting cannot know.",
    "concepts": ["response propensity", "calibration weighting", "raking", "R-indicator", "weight trimming"],
    "founders": "Response-propensity framework from Groves & Couper (1998); calibration estimation from Deville & Särndal (1992).",
    "classics": [
      "Groves, R. M., & Couper, M. P. (1998). Nonresponse in Household Interview Surveys",
      "Deville, J.-C., & Särndal, C.-E. (1992). 'Calibration Estimators in Survey Sampling,' Journal of the American Statistical Association 87(418)",
      "Schouten, B., Cobben, F., & Bethlehem, J. (2009). 'Indicators for the Representativeness of Survey Response,' Survey Methodology",
    ],
    "frameworks": [
      "Weighting pipeline — base weights → nonresponse adjustment → calibration to margins",
      "Propensity-cell adjustment — model response, weight within strata",
      "Design-based vs model-assisted weighting — raking and GREG as compromise estimators",
      "Weight diagnostics — distribution, trimming, and effective sample size loss from dispersion",
    ],
    "apply": "For official and elite PA surveys with 30–60% response, report response rates by subgroup, build weighting classes on registry covariates, and publish weighted/unweighted estimates side by side. Trim extreme weights and report effective n; assess remaining imbalance with R-indicators. In longitudinal panels, refresh weights each wave for attrition (see Methodology Map: Weighting & Non-Response Adjustment, Panel & Fixed-Effects Models).",
  },

  # ================= COMPARABILITY =================

  "Measurement Invariance": {
    "use": "A scale measures the same thing across groups, countries, or time only if factor structure, loadings, and intercepts hold — test configural, metric, and scalar invariance before comparing means.",
    "explain": "Multi-group confirmatory factor analysis formalizes comparability as a hierarchy: configural invariance (same items on the same factors), metric/weak invariance (equal loadings → comparable covariances and slopes), and scalar/strong invariance (equal intercepts → comparable means). Without scalar invariance, a cross-national gap in trust may reflect differential item functioning, not attitude. The ΔCFI ≈ .01 criterion (Cheung & Rensvold 2002) is the standard practical test for each step.",
    "concepts": ["configural invariance", "metric (weak) invariance", "scalar (strong) invariance", "partial invariance", "differential item functioning"],
    "founders": "Willett Meredith (1993) formalized the hierarchy; Steenkamp & Baumgartner (1998) set the cross-national testing protocol; Cheung & Rensvold (2002) gave practical fit criteria.",
    "classics": [
      "Meredith, W. (1993). 'Measurement Invariance, Factor Analysis and Factorial Invariance,' Psychometrika 58(4)",
      "Steenkamp, J.-B. E. M., & Baumgartner, H. (1998). 'Assessing Measurement Invariance in Cross-National Consumer Research,' Journal of Consumer Research 25(1)",
      "Cheung, G. W., & Rensvold, R. B. (2002). 'Evaluating Goodness-of-Fit Indexes for Testing Measurement Invariance,' Structural Equation Modeling 9(2)",
    ],
    "frameworks": [
      "Invariance hierarchy — configural → metric → scalar → strict as nested constraints",
      "Alignment optimization — approximate invariance for many groups",
      "Partial invariance fallback — proceed when most loadings and intercepts are equal",
      "DIF detection — likelihood-ratio tests and score-based methods for offending items",
    ],
    "apply": "Mandatory before any cross-country PA comparison (trust in government, perceived corruption, public service motivation): establish at least partial scalar invariance or restrict comparison to factor scores with caveats. For longitudinal policy panels, test invariance across waves before interpreting trends; alignment and Bayesian approximate methods handle 20+ groups (see Methodology Map: Structural Equation Modelling, IRT & Factor Analysis).",
  },

  "Scale Linking & Alignment (IRT)": {
    "use": "When different instruments claim to measure the same trait — across surveys, countries, or years — IRT linking puts them on a common scale via anchor items or score equating.",
    "explain": "Linking answers the comparability question when instruments differ: common-item nonequivalent-groups designs (anchor items shared across forms), concurrent calibration, and score equating. Alignment (Asparouhov & Muthén 2014) maximizes approximate invariance across many groups, enabling comparisons even when strict invariance fails. Linking quality is judged by anchor-item stability — drift in anchor parameters signals that 'the same' item measures differently across contexts.",
    "concepts": ["anchor items", "concurrent calibration", "score equating", "alignment", "item parameter drift"],
    "founders": "Item response theory from Rasch (1960) and Lord (1980); the test-equating tradition (Kolen & Brennan); alignment from Asparouhov & Muthén (2014).",
    "classics": [
      "Rasch, G. (1960). Probabilistic Models for Some Intelligence and Attainment Tests",
      "Kolen, M. J., & Brennan, R. L. (2014). Test Equating, Scaling, and Linking (3rd ed.)",
      "Asparouhov, T., & Muthén, B. (2014). 'Multiple-Group Factor Analysis Alignment,' Structural Equation Modeling 21(4)",
    ],
    "frameworks": [
      "Nonequivalent-groups anchor design — shared items calibrate different forms",
      "Concurrent vs separate calibration — one model for all groups vs chained links",
      "Equating methods — observed-score (linear, equipercentile) vs IRT true-score linking",
      "Alignment optimization — approximate invariance maximization for many-group comparisons",
    ],
    "apply": "Link repeated cross-sections of citizen surveys when item batteries change over time; equate trust or PSM measures across survey programs to build comparable longitudinal series. Evaluate anchor-item drift before interpreting linked trends, and report linking error in the final estimates (see Methodology Map: IRT & Factor Analysis, Structural Equation Modelling).",
  },

  "Translation & Cross-Cultural Adaptation": {
    "use": "A translated instrument is a new measurement act: semantic, idiomatic, experiential, and conceptual equivalence must be built, then verified by invariance testing.",
    "explain": "Brislin's back-translation (1970) started the field; the ITC Guidelines and Beaton et al.'s (2000) cross-cultural adaptation protocol turned it into a staged process — forward translation, reconciliation, back-translation, expert committee, pretesting. Linguistic equivalence (same words) is the floor; conceptual equivalence (the same idea evoked) is the target — concepts like 'public service motivation' or 'accountability' carry different cultural loads, so adaptation may require item replacement plus full psychometric revalidation.",
    "concepts": ["forward/back-translation", "conceptual equivalence", "decentering", "committee approach", "linguistic validation"],
    "founders": "Richard Brislin's back-translation (1970); International Test Commission Guidelines (2017); Beaton et al.'s (2000) cross-cultural adaptation protocol, widely adopted across disciplines.",
    "classics": [
      "Brislin, R. W. (1970). 'Back-Translation for Cross-Cultural Research,' Journal of Cross-Cultural Psychology 1(3)",
      "Beaton, D. E., et al. (2000). 'Guidelines for the Process of Cross-Cultural Adaptation of Self-Report Measures,' Spine 25(24)",
      "International Test Commission (2017). The ITC Guidelines for Translating and Adapting Tests (2nd ed.)",
    ],
    "frameworks": [
      "Brislin back-translation — literal check of translation fidelity",
      "Beaton stages — translation → synthesis → back-translation → expert committee → pretesting",
      "Decentering — treat source and target symmetrically rather than the source as gold",
      "Cross-language cognitive interviewing — comprehension probes catch conceptual nonequivalence",
    ],
    "apply": "Adapt PA instruments for multilingual administration with the full Beaton pipeline plus bilingual Cognitive Interviews; never assume a published translation is validated — re-establish reliability and Measurement Invariance on your own sample. Document adaptation decisions in the codebook for comparability audits (see Methodology Map: Psychometrics & Scale Validation, Structural Equation Modelling).",
  },

  "Ex-Post Harmonization": {
    "use": "Different studies collected different variables; harmonization re-expresses them into common metrics after the fact — powerful for synthesis and replication, bounded by what the sources contain.",
    "explain": "Ex-post harmonization creates integrated datasets from independently collected surveys or registers: recode variables to common classifications (ISCO, education bands), equate scales, align time references. Its core risk is harmonization error — losing construct validity in the name of comparability. Documented variable-level metadata, concordance tables, and sensitivity analysis of coding decisions are what distinguish rigorous harmonization from convenient recoding.",
    "concepts": ["harmonization error", "concordance tables", "common classifications", "metadata", "retrospective design"],
    "founders": "Cross-national survey harmonization infrastructure — ISSP, ESS, CSES; methodological framework from the Survey Data Recycling project and the ex-post harmonization quality literature.",
    "classics": [
      "Granda, P., Blasczyk, E., & Kulpinska, J. (2010). 'Guidelines for Best Practices in Cross-Cultural Surveys: Harmonization,' Survey Research Center, University of Michigan",
      "Kolczynska, M. (2020). 'Survey Quality and Measurement Equivalence in Cross-National Research,' Social Science Research",
      "Survey Data Recycling project (2016– ). 'New Analytic Strategies for Studying Survey Data Quality' reports",
    ],
    "frameworks": [
      "Harmonization pipeline — source inventory → target schema → concordance mapping → validation",
      "Harmonization error taxonomy — coverage, method, construct, and item non-equivalence",
      "Back-code validation — re-derive source variables from harmonized ones to audit information loss",
      "Metadata standards — DDI-based documentation of every transformation",
    ],
    "apply": "Build integrated PA datasets from multiple national surveys (trust, satisfaction, compliance) for comparative or replication work: publish concordance tables with the dataset, validate harmonized scales with invariance tests, and flag variables with partial equivalence. For meta-analytic harmonization across experimental studies, standardize outcome metrics and document every conversion (see Methodology Map: Systematic Review & Meta-Analysis, Most Similar / Different Systems).",
  },

  "Documentation & Codebooks (DDI)": {
    "use": "Measurement lives in its documentation: codebooks, variable labels, and provenance metadata determine whether data can be understood, reused, and cited — or quietly misunderstood.",
    "explain": "The Data Documentation Initiative (DDI) standard structures the social-science data lifecycle: question items, response categories, weights, derivation logic, and provenance in machine-readable form. Good codebooks make measurement visible — what each variable means, how it was constructed, what it omits — enabling secondary analysis, replication, and error correction. In an era of data reuse, documentation quality is measurement quality: undocumented data cannot be validly re-analyzed.",
    "concepts": ["codebook", "DDI metadata", "provenance", "variable derivation", "data citation"],
    "founders": "The DDI Alliance (2003– ); ICPSR's documentation tradition; the FAIR data principles (Wilkinson et al., 2016).",
    "classics": [
      "Vardigan, M., Heus, P., & Thomas, W. (2008). 'Data Documentation Initiative: Toward a Standard for the Social Sciences,' International Journal of Digital Curation",
      "Wilkinson, M. D., et al. (2016). 'The FAIR Guiding Principles for Scientific Data Management and Stewardship,' Scientific Data 3",
      "Borgman, C. L. (2015). Big Data, Little Data, No Data: Scholarship in the Networked World",
    ],
    "frameworks": [
      "DDI lifecycle model — study → data collection → variable → file as structured metadata",
      "Codebook completeness checklist — labels, categories, missing codes, weights, derivations",
      "FAIR principles — findable, accessible, interoperable, reusable as documentation goals",
      "Provenance chains — from instrument question to analysis variable, fully traceable",
    ],
    "apply": "Publish DDI-compliant codebooks with every PA dataset: the instrument as fielded (not as designed), translation versions, weight construction, and variable derivations. For administrative releases, document category changes and linkage decisions. Good documentation turns a measurement exercise from a one-off into infrastructure (see Methodology Map: Archival & Historical Methods, Systematic Review & Meta-Analysis).",
  },
}
