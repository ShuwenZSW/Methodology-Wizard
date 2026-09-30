# -*- coding: utf-8 -*-
"""
============================================================
SITE CONTENT — this is the only file you need to edit
============================================================
Structure:
  TREE     : the method hierarchy. Each node = {"name": ..., "children": [...]}
             - the three trunk nodes carry "color": qual (green) / quant (blue)
               / mixed (terracotta)
             - append " ★" to a name to mark it as a recommended priority
  PROFILES : method detail cards. Keys must exactly match leaf names in TREE
             (including any ★ suffix).
             Fields: use   = where to use it      / data  = data required
                     n     = typical scale         / assume = key assumptions
                     skill = skill level           / time   = time to implement
                     adopt = adoption priority 1-5 / watch  = when it fails

[To add a method — 3 steps]
  1. Add a node under the right category in TREE:  {"name": "New Method"},
  2. Add a profile with the same name in PROFILES (copy any entry and edit)
  3. Run  python build_site.py  to regenerate index.html, then git push
============================================================
"""

TREE = {
  "name": "SOCIAL SCIENCE\nMETHODOLOGY",
  "children": [
    {
      "name": "QUALITATIVE",
      "color": "qual",
      "children": [
        {
          "name": "Interpretive & Ethnographic",
          "children": [
            {
              "name": "Ethnography & Participant Observation"
            },
            {
              "name": "Phenomenology / IPA"
            },
            {
              "name": "Grounded Theory"
            },
            {
              "name": "Narrative & Life-History Analysis"
            },
            {
              "name": "Discourse Analysis"
            }
          ]
        },
        {
          "name": "Interview-Based",
          "children": [
            {
              "name": "Semi-Structured Interviews"
            },
            {
              "name": "Cognitive Interviews"
            },
            {
              "name": "Expert & Elite Interviews"
            },
            {
              "name": "Focus Groups"
            },
            {
              "name": "Oral History"
            }
          ]
        },
        {
          "name": "Text & Document Analysis",
          "children": [
            {
              "name": "Qualitative Content Analysis"
            },
            {
              "name": "Thematic Analysis"
            },
            {
              "name": "Frame Analysis"
            },
            {
              "name": "Critical Discourse Analysis"
            },
            {
              "name": "Archival & Historical Methods"
            }
          ]
        },
        {
          "name": "Case-Oriented Comparison",
          "children": [
            {
              "name": "Process Tracing"
            },
            {
              "name": "Comparative Historical Analysis"
            },
            {
              "name": "QCA (csQCA / fsQCA)"
            },
            {
              "name": "Most Similar / Different Systems"
            }
          ]
        },
        {
          "name": "Emerging Qualitative",
          "children": [
            {
              "name": "Digital & Virtual Ethnography"
            },
            {
              "name": "Visual & Photo-Elicitation"
            },
            {
              "name": "LLM-Assisted Qualitative Coding ★"
            }
          ]
        }
      ]
    },
    {
      "name": "QUANTITATIVE",
      "color": "quant",
      "children": [
        {
          "name": "Experimental",
          "children": [
            {
              "name": "Lab Experiments"
            },
            {
              "name": "Field Experiments & RCTs"
            },
            {
              "name": "Survey Experiments & Conjoint ★"
            },
            {
              "name": "Natural Experiments"
            }
          ]
        },
        {
          "name": "Causal Inference Core",
          "children": [
            {
              "name": "Randomized Controlled Trials"
            },
            {
              "name": "Difference-in-Differences ★"
            },
            {
              "name": "Instrumental Variables"
            },
            {
              "name": "Regression Discontinuity"
            },
            {
              "name": "Propensity Score Matching"
            },
            {
              "name": "DAGs & Causal Identification ★"
            },
            {
              "name": "Synthetic Control Method"
            }
          ]
        },
        {
          "name": "Statistical Modelling",
          "children": [
            {
              "name": "OLS & Generalised Linear Models"
            },
            {
              "name": "Multilevel / Hierarchical Models"
            },
            {
              "name": "Structural Equation Modelling"
            },
            {
              "name": "Panel & Fixed-Effects Models"
            },
            {
              "name": "Survival & Event History Analysis"
            },
            {
              "name": "Bayesian Inference"
            }
          ]
        },
        {
          "name": "Survey & Measurement",
          "children": [
            {
              "name": "Survey Design & Sampling"
            },
            {
              "name": "Psychometrics & Scale Validation"
            },
            {
              "name": "IRT & Factor Analysis"
            },
            {
              "name": "Weighting & Non-Response Adjustment"
            }
          ]
        },
        {
          "name": "Social Network Analysis",
          "children": [
            {
              "name": "Centrality Measures ★"
            },
            {
              "name": "Community Detection & Clustering"
            },
            {
              "name": "ERGM"
            },
            {
              "name": "Longitudinal SNA / SAOM"
            },
            {
              "name": "Two-Mode & Multiplex Networks"
            }
          ]
        },
        {
          "name": "Computational & Data-Driven",
          "children": [
            {
              "name": "NLP & Topic Modeling ★"
            },
            {
              "name": "LLM-Based Text Annotation ★"
            },
            {
              "name": "Agent-Based Modeling"
            },
            {
              "name": "Geospatial Analysis & GIS ★"
            },
            {
              "name": "Machine Learning Prediction"
            },
            {
              "name": "Causal Machine Learning"
            }
          ]
        }
      ]
    },
    {
      "name": "MIXED METHODS",
      "color": "mixed",
      "children": [
        {
          "name": "Core Designs",
          "children": [
            {
              "name": "Convergent Parallel Design"
            },
            {
              "name": "Explanatory Sequential ★"
            },
            {
              "name": "Exploratory Sequential"
            },
            {
              "name": "Embedded Design"
            }
          ]
        },
        {
          "name": "Advanced Integration",
          "children": [
            {
              "name": "Case- & Variable-Based Integration"
            },
            {
              "name": "QCA + Regression Triangulation"
            },
            {
              "name": "Mixed-Methods SNA"
            },
            {
              "name": "Text Mining + Close Reading"
            }
          ]
        },
        {
          "name": "Evaluation & Applied",
          "children": [
            {
              "name": "Theory-Based Evaluation"
            },
            {
              "name": "Realist Evaluation"
            },
            {
              "name": "Contribution Analysis"
            },
            {
              "name": "Participatory Action Research"
            }
          ]
        },
        {
          "name": "Meta-Analytic",
          "children": [
            {
              "name": "Systematic Review & Meta-Analysis"
            },
            {
              "name": "Meta-Ethnography"
            },
            {
              "name": "Evidence Gap Mapping"
            }
          ]
        },
        {
          "name": "Deliberative & Participatory",
          "children": [
            {
              "name": "Delphi Method"
            },
            {
              "name": "Citizen Juries & Deliberative Polling"
            },
            {
              "name": "Community-Based Participatory Research"
            }
          ]
        }
      ]
    }
  ]
}

PROFILES = {
  "Ethnography & Participant Observation": {
    "use": "Understand a group's culture from the inside — street-level bureaucracy, organisations, online tribes.",
    "data": "Fieldnotes, observations, artefacts",
    "n": "1–3 sites, months–years",
    "assume": "Genuine access and rapport; disciplined reflexivity about your own role.",
    "skill": "Expert",
    "time": "Long",
    "adopt": 3,
    "watch": "Shallow access yields front-stage performances, not actual practice."
  },
  "Phenomenology / IPA": {
    "use": "Lived experience of a phenomenon — illness, migration, identity transition.",
    "data": "In-depth interviews",
    "n": "3–15 participants",
    "assume": "A fairly homogeneous sample; bracketing of prior assumptions.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 3,
    "watch": "A heterogeneous sample dilutes the 'essence' you claim to find."
  },
  "Grounded Theory": {
    "use": "Build theory bottom-up where existing theory is thin or missing.",
    "data": "Iterative interviews + fieldwork",
    "n": "20–60 interviews to saturation",
    "assume": "Theoretical sampling and constant comparison are followed strictly.",
    "skill": "Expert",
    "time": "Long",
    "adopt": 3,
    "watch": "Declaring 'saturation' too early is the most common reviewer criticism."
  },
  "Narrative & Life-History Analysis": {
    "use": "Identity construction and biographical turning points.",
    "data": "Long-form interviews, diaries, letters",
    "n": "5–30 narratives",
    "assume": "Stories are treated as meaning-making, not factual records.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 3,
    "watch": "Don't fact-check narratives against reality — analyse why the story is told this way."
  },
  "Discourse Analysis": {
    "use": "How language constructs objects, subjects and power relations.",
    "data": "Texts, talk, policy documents",
    "n": "10–500 texts",
    "assume": "Language is constitutive of social reality, not merely descriptive.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 3,
    "watch": "Cherry-picked quotes — show a systematic text selection strategy."
  },
  "Semi-Structured Interviews": {
    "use": "Explore experiences and perceptions, e.g. of marginalized groups.",
    "data": "Primary interviews",
    "n": "15–40, to saturation",
    "assume": "Rapport and interviewer reflexivity.",
    "skill": "Beginner",
    "time": "Medium",
    "adopt": 5,
    "watch": "Leading questions, and stopping before real saturation is reached."
  },
  "Cognitive Interviews": {
    "use": "Pre-test whether survey items are understood as intended.",
    "data": "Think-aloud / probing sessions",
    "n": "5–15 per round",
    "assume": "Verbal reports reflect actual comprehension.",
    "skill": "Beginner",
    "time": "Short",
    "adopt": 5,
    "watch": "Small convenience samples miss subgroup misunderstandings."
  },
  "Expert & Elite Interviews": {
    "use": "Process knowledge and the institutional backstage — how decisions were really made.",
    "data": "Primary access to elites",
    "n": "10–30",
    "assume": "Access can be secured; positionality is managed.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 4,
    "watch": "Elites perform for the record — triangulate with documents."
  },
  "Focus Groups": {
    "use": "Group norms and contested views; how people justify positions socially.",
    "data": "Moderated group discussions",
    "n": "4–10 groups × 6–10 people",
    "assume": "Interaction reveals shared norms rather than suppressing them.",
    "skill": "Beginner–Intermediate",
    "time": "Medium",
    "adopt": 3,
    "watch": "Dominant voices suppress dissent; unsuitable for sensitive disclosures."
  },
  "Oral History": {
    "use": "Memory of events by those who lived them — movements, institutions, communities.",
    "data": "Recorded life narratives, archives",
    "n": "10–50 narrators",
    "assume": "Memory is constructive but still evidentiary.",
    "skill": "Intermediate",
    "time": "Long",
    "adopt": 2,
    "watch": "Retrospective bias — corroborate dates and facts independently."
  },
  "Qualitative Content Analysis": {
    "use": "Systematic description of themes in documents or open-ended answers.",
    "data": "Archived text, transcripts",
    "n": "20–1,000 texts",
    "assume": "Codebook reliability (inter-coder agreement) is reported.",
    "skill": "Beginner",
    "time": "Short–Medium",
    "adopt": 5,
    "watch": "Counting themes without reporting coder agreement."
  },
  "Thematic Analysis": {
    "use": "Flexible identification of patterns in interview data.",
    "data": "Transcripts",
    "n": "15–40 interviews",
    "assume": "A disciplined phase process (familiarise → code → theme → review).",
    "skill": "Beginner",
    "time": "Short–Medium",
    "adopt": 5,
    "watch": "Topic summaries masquerading as themes — a theme needs a central organising concept."
  },
  "Frame Analysis": {
    "use": "How media or politicians package issues (conflict, human interest, responsibility frames).",
    "data": "News, speeches, documents",
    "n": "100–5,000 texts",
    "assume": "Frames are operationalised from prior literature, not invented ad hoc.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 3,
    "watch": "Ad-hoc frame definitions that cannot be replicated."
  },
  "Critical Discourse Analysis": {
    "use": "Expose ideology and power in language — policy, media, institutions.",
    "data": "Texts plus social context",
    "n": "10–200 key texts",
    "assume": "The analyst's interpretive chain is made transparent.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 3,
    "watch": "High subjectivity — without transparency it reads as opinion."
  },
  "Archival & Historical Methods": {
    "use": "Reconstruct past processes from primary sources.",
    "data": "Archives, official records, newspapers",
    "n": "One collection to many",
    "assume": "Source criticism: authenticity, provenance, bias.",
    "skill": "Intermediate",
    "time": "Long",
    "adopt": 3,
    "watch": "Survival bias — what was archived is not what happened."
  },
  "Process Tracing": {
    "use": "Test causal mechanisms within a single case.",
    "data": "Documents, interviews, primary sources",
    "n": "1–5 cases",
    "assume": "Explicit evidence tests (hoop, smoking-gun) for each clue.",
    "skill": "Expert",
    "time": "Long",
    "adopt": 4,
    "watch": "Storytelling without naming the test each piece of evidence performs."
  },
  "Comparative Historical Analysis": {
    "use": "Macro outcomes: revolutions, welfare states, democratisation.",
    "data": "Historical archives, secondary literature",
    "n": "2–20 cases",
    "assume": "Cases are comparable across time and context.",
    "skill": "Expert",
    "time": "Long",
    "adopt": 2,
    "watch": "Selecting cases on the dependent variable."
  },
  "QCA (csQCA / fsQCA)": {
    "use": "Necessary/sufficient conditions and equifinal paths to an outcome.",
    "data": "Calibrated case knowledge",
    "n": "10–50 cases",
    "assume": "Calibration anchors are justified; consistency thresholds are principled.",
    "skill": "Intermediate–Expert",
    "time": "Medium",
    "adopt": 3,
    "watch": "Arbitrary calibration — every threshold needs a substantive defence."
  },
  "Most Similar / Different Systems": {
    "use": "Classic small-N comparison isolating key similarities or differences.",
    "data": "Comparative case data",
    "n": "2–6 cases",
    "assume": "Ceteris paribus roughly holds across systems.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 2,
    "watch": "Cases are rarely truly 'most similar' — treat as heuristic, not proof."
  },
  "Digital & Virtual Ethnography": {
    "use": "Online communities and platform cultures.",
    "data": "Platform observation, posts, interactions",
    "n": "Weeks–months of immersion",
    "assume": "Ethics of observing public / semi-public data is resolved.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 4,
    "watch": "ToS and consent grey zones — seek ethics approval early."
  },
  "Visual & Photo-Elicitation": {
    "use": "Access tacit or hard-to-verbalise experience through images.",
    "data": "Participant- or researcher-made photos",
    "n": "10–30 participants",
    "assume": "Images prompt richer talk than questions alone.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 2,
    "watch": "Analysing the photo itself instead of the talk it elicited."
  },
  "LLM-Assisted Qualitative Coding ★": {
    "use": "Accelerate coding of large qualitative corpora with human validation.",
    "data": "Transcripts + LLM access",
    "n": "100s–10,000s of segments",
    "assume": "Human-in-the-loop validation; agreement metrics vs human coders.",
    "skill": "Intermediate",
    "time": "Short",
    "adopt": 5,
    "watch": "Never skip the human gold standard — report inter-rater agreement."
  },
  "Lab Experiments": {
    "use": "Isolate causal mechanisms under maximal control (bias, decision-making).",
    "data": "Primary behavioural data",
    "n": "50–300 participants",
    "assume": "Random assignment; no demand characteristics.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 4,
    "watch": "Student samples and artificial tasks limit external validity."
  },
  "Field Experiments & RCTs": {
    "use": "Average treatment effects of real interventions — policy, education, development.",
    "data": "Primary trial data",
    "n": "200–10,000+ units",
    "assume": "SUTVA; no spillovers; compliance; randomisation integrity.",
    "skill": "Expert",
    "time": "Long",
    "adopt": 4,
    "watch": "Attrition and spillovers quietly destroy identification."
  },
  "Survey Experiments & Conjoint ★": {
    "use": "Causal effects of information or framing; decompose multi-attribute preferences.",
    "data": "Primary survey with embedded randomisation",
    "n": "500–5,000 respondents",
    "assume": "Random assignment; no profile-order contamination.",
    "skill": "Beginner–Intermediate",
    "time": "Short",
    "adopt": 5,
    "watch": "Underpowered interaction tests; artificial profiles ≠ real decisions."
  },
  "Natural Experiments": {
    "use": "Exploit lotteries or arbitrary thresholds as as-if random variation.",
    "data": "Administrative / observational data",
    "n": "1k–1M units",
    "assume": "Genuine as-if randomness; excludability.",
    "skill": "Expert",
    "time": "Medium–Long",
    "adopt": 3,
    "watch": "The 'natural' randomisation is often less random than claimed — interrogate it."
  },
  "Randomized Controlled Trials": {
    "use": "The gold standard for estimating average treatment effects.",
    "data": "Primary trial data",
    "n": "200–10,000+ units",
    "assume": "SUTVA; compliance; randomisation integrity.",
    "skill": "Expert",
    "time": "Long",
    "adopt": 4,
    "watch": "Cost, ethics and attrition constraints — pre-register and monitor."
  },
  "Difference-in-Differences ★": {
    "use": "Evaluate policy rollouts with panel data when randomisation is impossible.",
    "data": "Panel / repeated cross-sections",
    "n": "2+ periods, 100s–millions of units",
    "assume": "Parallel trends; no anticipation; modern staggered estimators.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 5,
    "watch": "Two-way FE under staggered timing can flip signs — use Callaway–Sant'Anna or Sun–Abraham."
  },
  "Instrumental Variables": {
    "use": "Causal effects despite unobserved confounding (returns to education, institutions).",
    "data": "Observational data + valid instrument",
    "n": "1,000+ typically",
    "assume": "Relevance; exclusion restriction; monotonicity (LATE).",
    "skill": "Expert",
    "time": "Medium",
    "adopt": 3,
    "watch": "Weak instruments and indefensible exclusion restrictions sink the paper."
  },
  "Regression Discontinuity": {
    "use": "Local treatment effects at cutoffs — grant thresholds, election margins.",
    "data": "Administrative data near the cutoff",
    "n": "1,000+ within bandwidth",
    "assume": "Continuity of potential outcomes; no manipulation of the running variable.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 4,
    "watch": "Bunching near the cutoff signals manipulation — always run a density test."
  },
  "Propensity Score Matching": {
    "use": "Balance treated and control groups on observed covariates.",
    "data": "Cross-section or panel with rich covariates",
    "n": "500–100,000",
    "assume": "Conditional independence (selection on observables); common support.",
    "skill": "Intermediate",
    "time": "Short",
    "adopt": 4,
    "watch": "Balances only what you measured — unobserved confounding remains."
  },
  "DAGs & Causal Identification ★": {
    "use": "Map causal structure, choose valid adjustment sets, spot colliders — before running anything.",
    "data": "None — theory-driven",
    "n": "n/a",
    "assume": "The drawn structure is defensible.",
    "skill": "Intermediate",
    "time": "Short",
    "adopt": 5,
    "watch": "A DAG you cannot defend is decoration — commit to every arrow and non-arrow."
  },
  "Synthetic Control Method": {
    "use": "Evaluate a single treated unit (country, state, city) against a weighted donor pool.",
    "data": "Long pre-treatment panel of aggregate units",
    "n": "1 treated + 5–30 donors, 10+ pre-periods",
    "assume": "Good pre-treatment fit; no interference.",
    "skill": "Expert",
    "time": "Medium",
    "adopt": 4,
    "watch": "Cherry-picked donors — report in-space placebo tests."
  },
  "OLS & Generalised Linear Models": {
    "use": "Baseline description, associative modelling, control strategies.",
    "data": "Any structured data",
    "n": "100+",
    "assume": "Linearity; exogeneity; appropriate (robust) standard errors.",
    "skill": "Beginner",
    "time": "Short",
    "adopt": 4,
    "watch": "Reading associations as causal effects."
  },
  "Multilevel / Hierarchical Models": {
    "use": "Nested data — students in schools, citizens in regions; contextual effects.",
    "data": "Hierarchically structured data",
    "n": "30+ groups, 500+ individuals",
    "assume": "Random-effects distribution; correct level-2 specification.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 4,
    "watch": "Fewer than ~30 level-2 units gives unreliable variance estimates."
  },
  "Structural Equation Modelling": {
    "use": "Test latent-variable measurement and path theories jointly.",
    "data": "Survey with multi-item scales",
    "n": "200–500+",
    "assume": "Correct measurement model; normality or a robust estimator.",
    "skill": "Intermediate–Expert",
    "time": "Medium",
    "adopt": 3,
    "watch": "Chasing fit via modification indices until the model is overfit."
  },
  "Panel & Fixed-Effects Models": {
    "use": "Control all time-invariant unobserved confounding.",
    "data": "Panel data, 2+ waves",
    "n": "100+ units × 3+ waves",
    "assume": "Strict exogeneity; sufficient within-unit variation.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 4,
    "watch": "No within-unit variation means no identification."
  },
  "Survival & Event History Analysis": {
    "use": "Duration outcomes — job exit, policy adoption, conflict onset.",
    "data": "Time-to-event data with censoring",
    "n": "300+ events",
    "assume": "Proportional hazards (Cox); independent censoring.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 3,
    "watch": "Violated proportional hazards — test it, don't assume it."
  },
  "Bayesian Inference": {
    "use": "Small samples, partial pooling, full uncertainty quantification.",
    "data": "Any; shines with sparse data",
    "n": "Even 50–500",
    "assume": "Priors are appropriate and justifiable.",
    "skill": "Expert",
    "time": "Long",
    "adopt": 3,
    "watch": "Computational cost; reviewers will probe every prior."
  },
  "Survey Design & Sampling": {
    "use": "Population-representative description of attitudes and behaviours.",
    "data": "Primary fieldwork",
    "n": "1,000–5,000",
    "assume": "Known inclusion probabilities; frame coverage.",
    "skill": "Intermediate",
    "time": "Long",
    "adopt": 4,
    "watch": "Coverage gaps in the sampling frame bias everything downstream."
  },
  "Psychometrics & Scale Validation": {
    "use": "Build and validate multi-item measures.",
    "data": "Multi-item survey data",
    "n": "300–1,000",
    "assume": "Dimensionality; local independence.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 3,
    "watch": "Reporting Cronbach's alpha as if it were validation."
  },
  "IRT & Factor Analysis": {
    "use": "Item calibration; measurement invariance across groups.",
    "data": "Multi-item response data",
    "n": "300–1,000+",
    "assume": "Model fit; unidimensionality or a correctly specified structure.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 3,
    "watch": "Comparing groups without first establishing measurement invariance."
  },
  "Weighting & Non-Response Adjustment": {
    "use": "Correct non-probability samples; small-area opinion via MRP.",
    "data": "Survey + census/auxiliary margins",
    "n": "1,000+ survey cases",
    "assume": "The adjustment model captures the selection mechanism.",
    "skill": "Expert",
    "time": "Medium",
    "adopt": 4,
    "watch": "Weighting cannot fix variables you never measured."
  },
  "Centrality Measures ★": {
    "use": "Identify influential actors, brokers and diffusion paths.",
    "data": "Relational edge-lists / adjacency matrices",
    "n": "30–10,000 nodes",
    "assume": "Accurate tie measurement; defensible network boundary.",
    "skill": "Beginner–Intermediate",
    "time": "Short",
    "adopt": 5,
    "watch": "Centrality ≠ importance without a theory of what flows through the network."
  },
  "Community Detection & Clustering": {
    "use": "Find factions, echo chambers and field structure.",
    "data": "Edge-lists",
    "n": "100–1M nodes",
    "assume": "The network actually has block structure.",
    "skill": "Intermediate",
    "time": "Short",
    "adopt": 4,
    "watch": "The resolution limit silently merges small communities."
  },
  "ERGM": {
    "use": "Model tie formation: homophily vs influence, triadic closure.",
    "data": "Complete network, one wave",
    "n": "50–500 nodes",
    "assume": "Dependence assumptions; model convergence.",
    "skill": "Expert",
    "time": "Medium",
    "adopt": 3,
    "watch": "Model degeneracy — always run goodness-of-fit checks."
  },
  "Longitudinal SNA / SAOM": {
    "use": "Disentangle selection from influence over time.",
    "data": "Panel networks, 2+ waves",
    "n": "50–300 actors × 3+ waves",
    "assume": "Markov evolution; actor-oriented decision rules.",
    "skill": "Expert",
    "time": "Long",
    "adopt": 2,
    "watch": "Heavy computation and fragile convergence — budget time."
  },
  "Two-Mode & Multiplex Networks": {
    "use": "Board interlocks, event participation, co-authorship structures.",
    "data": "Bipartite edge-lists",
    "n": "100–10,000 nodes",
    "assume": "Projection choices are made deliberately.",
    "skill": "Intermediate",
    "time": "Short",
    "adopt": 3,
    "watch": "Projecting two-mode data inflates clustering coefficients."
  },
  "NLP & Topic Modeling ★": {
    "use": "Discover latent themes in large text corpora — policy documents, social media.",
    "data": "Archived / digital text",
    "n": "1,000–10M documents",
    "assume": "Justified k; validation against close reading.",
    "skill": "Intermediate",
    "time": "Short–Medium",
    "adopt": 5,
    "watch": "Topics are not themes — validate with human reading of exemplars."
  },
  "LLM-Based Text Annotation ★": {
    "use": "Scale hand-coding of stance, frames or sentiment at near-zero marginal cost.",
    "data": "Text corpora + LLM access",
    "n": "10k–1M documents",
    "assume": "Prompt validity established against a human gold standard.",
    "skill": "Intermediate",
    "time": "Short",
    "adopt": 5,
    "watch": "Model version drift — lock versions, report agreement metrics."
  },
  "Agent-Based Modeling": {
    "use": "Show how macro patterns emerge from micro rules — segregation, diffusion.",
    "data": "Theory + calibration data",
    "n": "100–100k agents × many runs",
    "assume": "Rule validity; thorough sensitivity analysis.",
    "skill": "Expert",
    "time": "Long",
    "adopt": 2,
    "watch": "Anything can emerge from a simulation — validation standards are contested."
  },
  "Geospatial Analysis & GIS ★": {
    "use": "Spatial inequality, exposure to hazards, service access, place-based policy evaluation.",
    "data": "Geocoded administrative / survey / satellite data",
    "n": "100s of areas to millions of points",
    "assume": "Spatial autocorrelation handled; MAUP acknowledged.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 4,
    "watch": "Naive maps invite MAUP and autocorrelation critiques from reviewers."
  },
  "Machine Learning Prediction": {
    "use": "Prediction tasks — risk scores, forecasting, variable discovery.",
    "data": "Large structured data",
    "n": "5,000+",
    "assume": "No leakage; honest train/test separation; calibration.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 4,
    "watch": "Data leakage and uncalibrated probabilities."
  },
  "Causal Machine Learning": {
    "use": "Heterogeneous treatment effects with high-dimensional controls (causal forests, double ML).",
    "data": "Large observational datasets",
    "n": "5,000+",
    "assume": "Unconfoundedness; overlap; honest sample splitting.",
    "skill": "Expert",
    "time": "Long",
    "adopt": 3,
    "watch": "ML cannot fix selection on unobservables — the DAG still comes first."
  },
  "Convergent Parallel Design": {
    "use": "Triangulate qualitative and quantitative evidence on the same question at once.",
    "data": "Both strands collected in parallel",
    "n": "Full Ql + Qn samples",
    "assume": "Both strands genuinely address the same construct.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 4,
    "watch": "Two studies stapled together — plan the integration joint display upfront."
  },
  "Explanatory Sequential ★": {
    "use": "Follow up surprising or significant quantitative results with targeted interviews.",
    "data": "Survey / experiment → interviews",
    "n": "500+ survey → 15–30 interviews",
    "assume": "Purposeful follow-up sampling from the quantitative results.",
    "skill": "Intermediate",
    "time": "Medium–Long",
    "adopt": 5,
    "watch": "Interviewing a convenience sample instead of outliers and informative cases."
  },
  "Exploratory Sequential": {
    "use": "Build instruments from qualitative insight, then test them at scale.",
    "data": "Interviews → pilot → survey",
    "n": "20 interviews → 300+ survey",
    "assume": "Construct coverage from the Ql phase; psychometric validation.",
    "skill": "Intermediate",
    "time": "Long",
    "adopt": 4,
    "watch": "Skipping the validation phase between strands."
  },
  "Embedded Design": {
    "use": "One strand supports the other — e.g. interviews nested inside a trial.",
    "data": "Primary strand + supplemental strand",
    "n": "Varies",
    "assume": "A clear priority of one strand over the other.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 3,
    "watch": "The supplemental strand ends up too thin to support any claim."
  },
  "Case- & Variable-Based Integration": {
    "use": "Combine within-case mechanism insight with cross-case estimation.",
    "data": "Cases + full dataset",
    "n": "2–5 cases + full N",
    "assume": "Cases are selected deliberately from the regression geometry.",
    "skill": "Expert",
    "time": "Long",
    "adopt": 3,
    "watch": "Case selection on the dependent variable without justification."
  },
  "QCA + Regression Triangulation": {
    "use": "Cross-validate correlational and configurational causal claims.",
    "data": "Calibrated cases + dataset",
    "n": "20–100 cases",
    "assume": "Both models are correctly specified.",
    "skill": "Expert",
    "time": "Medium",
    "adopt": 2,
    "watch": "Presenting contradictory results without resolving why they differ."
  },
  "Mixed-Methods SNA": {
    "use": "Combine network structure with the meaning of ties — why ties exist.",
    "data": "Edge-lists + interviews",
    "n": "50–500 nodes + 15–30 interviews",
    "assume": "Tie meanings actually match the relational data.",
    "skill": "Expert",
    "time": "Long",
    "adopt": 3,
    "watch": "Treating structural ties as self-explanatory."
  },
  "Text Mining + Close Reading": {
    "use": "Distant reading to find patterns, close reading to verify them.",
    "data": "Large corpus + sampled passages",
    "n": "10k documents + 50–200 passages",
    "assume": "Algorithmic patterns survive qualitative scrutiny.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 4,
    "watch": "Reporting algorithm output without the close-reading check."
  },
  "Theory-Based Evaluation": {
    "use": "Evaluate programmes by testing their theory of change, step by step.",
    "data": "Programme records, interviews, admin data",
    "n": "1 programme, multi-source",
    "assume": "An explicit, testable theory of change exists.",
    "skill": "Intermediate",
    "time": "Long",
    "adopt": 3,
    "watch": "A theory of change written after the fact to fit the data."
  },
  "Realist Evaluation": {
    "use": "What works, for whom, in what circumstances (context–mechanism–outcome).",
    "data": "Multi-source programme data",
    "n": "1 programme, multiple sites",
    "assume": "Generative mechanisms exist and are empirically accessible.",
    "skill": "Expert",
    "time": "Long",
    "adopt": 3,
    "watch": "CMO jargon without empirical bite."
  },
  "Contribution Analysis": {
    "use": "Make credible contribution claims where RCTs are infeasible.",
    "data": "Theory of change + multiple evidence streams",
    "n": "1 intervention",
    "assume": "The assembled contribution story is verifiable.",
    "skill": "Intermediate–Expert",
    "time": "Long",
    "adopt": 3,
    "watch": "Confusing contribution with attribution."
  },
  "Participatory Action Research": {
    "use": "Research with communities, aimed at change, not just knowledge.",
    "data": "Co-generated data",
    "n": "Community-defined",
    "assume": "Authentic power-sharing with participants.",
    "skill": "Expert",
    "time": "Long",
    "adopt": 3,
    "watch": "Token participation — communities treated as data sources only."
  },
  "Systematic Review & Meta-Analysis": {
    "use": "Synthesise effect sizes across a literature; funder-friendly evidence.",
    "data": "Published studies and effect sizes",
    "n": "20–200+ studies",
    "assume": "Publication bias handled; preregistered protocol.",
    "skill": "Intermediate",
    "time": "Medium–Long",
    "adopt": 4,
    "watch": "Garbage in, garbage out — screen study quality rigorously."
  },
  "Meta-Ethnography": {
    "use": "Synthesise qualitative studies into higher-order interpretations.",
    "data": "Published qualitative studies",
    "n": "5–40 studies",
    "assume": "Studies are conceptually translatable into one another.",
    "skill": "Expert",
    "time": "Long",
    "adopt": 2,
    "watch": "Forcing synthesis of incommensurable studies."
  },
  "Evidence Gap Mapping": {
    "use": "Show funders where evidence exists — and where the holes are.",
    "data": "Systematic literature search",
    "n": "100s–1,000s of studies",
    "assume": "A consistent, piloted coding framework.",
    "skill": "Intermediate",
    "time": "Medium",
    "adopt": 3,
    "watch": "A gap map without a quality dimension misleads decision-makers."
  },
  "Delphi Method": {
    "use": "Expert consensus forecasting — policy priorities, scenario building.",
    "data": "Iterative expert questionnaires",
    "n": "10–50 experts, 2–4 rounds",
    "assume": "Panel representativeness; controlled feedback between rounds.",
    "skill": "Beginner–Intermediate",
    "time": "Medium",
    "adopt": 3,
    "watch": "Attrition between rounds quietly skews the consensus."
  },
  "Citizen Juries & Deliberative Polling": {
    "use": "Informed public judgement on contested policy questions.",
    "data": "Deliberation transcripts + pre/post surveys",
    "n": "12–24 (juries) / 100–300 (polls)",
    "assume": "Balanced briefing materials; near-random recruitment.",
    "skill": "Intermediate",
    "time": "Long",
    "adopt": 2,
    "watch": "Unbalanced briefings manufacture consent rather than measure it."
  },
  "Community-Based Participatory Research": {
    "use": "Co-production of knowledge with marginalized populations.",
    "data": "Co-generated data",
    "n": "Community-defined",
    "assume": "Ethical partnership and shared ownership of outputs.",
    "skill": "Expert",
    "time": "Long",
    "adopt": 3,
    "watch": "Extraction dressed up as participation."
  }
}
