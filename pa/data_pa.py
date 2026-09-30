# -*- coding: utf-8 -*-
"""
============================================================
PA SITE CONTENT — Public Administration Theories & Topics
============================================================
Sister site of the Methodology Map. Same architecture:
  TREE     : the theory hierarchy. Node = {"name": ..., "children": [...]}
             - the three trunk nodes carry "color" (reuse site palette)
             - append " ★" to mark a core canon / priority reading
  PROFILES : theory cards. Keys must exactly match leaf names in TREE.
             Fields: use        = core proposition (one sentence)
                     explain    = what the theory says and why it matters
                     concepts   = 4-7 key terms, rendered as chips
                     founders   = foundational scholars & seminal works
                     classics   = 2-3 classic readings
                     frameworks = key analytical frameworks / theoretical
                                  variants with one-line descriptions
                     apply      = how to use it: typical research questions,
                                  operationalization, method pairings
                                  (cross-reference the Methodology Map)

[To add a theory — 3 steps]
  1. Add a leaf under the right category in TREE
  2. Add a profile with the same name in PROFILES (copy any entry and edit)
  3. Run  python build_pa.py  to regenerate index.html
============================================================
"""

TREE = {
  "name": "PUBLIC\nADMINISTRATION",
  "children": [
    {
      "name": "ORGANIZATIONS & MANAGEMENT",
      "color": "quant",
      "children": [
        {
          "name": "Bureaucratic Theory",
          "children": [
            {"name": "Weberian Bureaucracy"},
            {"name": "Street-Level Bureaucracy ★"},
            {"name": "Representative Bureaucracy"},
            {"name": "Organizational Culture & Decoupling"},
          ]
        },
        {
          "name": "Management & Reform",
          "children": [
            {"name": "New Public Management ★"},
            {"name": "Public Value Management ★"},
            {"name": "New Public Service"},
            {"name": "Post-NPM & Digital-Era Governance"},
          ]
        },
        {
          "name": "Networks & Collaboration",
          "children": [
            {"name": "Governance & Network Theory ★"},
            {"name": "Collaborative Governance"},
            {"name": "Coproduction & Co-creation ★"},
            {"name": "Collaborative Public Management"},
          ]
        },
      ]
    },
    {
      "name": "INSTITUTIONS & POLICY PROCESS",
      "color": "qual",
      "children": [
        {
          "name": "Rationality & Choice",
          "children": [
            {"name": "Rational Choice & Public Choice"},
            {"name": "Budget-Maximizing Bureaucracy"},
            {"name": "Bureau-Shaping"},
            {"name": "Principal–Agent Theory"},
          ]
        },
        {
          "name": "Policy Process Theories",
          "children": [
            {"name": "Multiple Streams Framework ★"},
            {"name": "Advocacy Coalition Framework ★"},
            {"name": "Punctuated Equilibrium Theory ★"},
            {"name": "Policy Feedback & Path Dependence ★"},
            {"name": "Institutional Analysis & Development ★"},
            {"name": "Policy Diffusion"},
          ]
        },
        {
          "name": "Institutionalisms",
          "children": [
            {"name": "Historical Institutionalism"},
            {"name": "Sociological Institutionalism"},
            {"name": "Discursive Institutionalism"},
          ]
        },
      ]
    },
    {
      "name": "DEMOCRACY, BEHAVIOR & VALUES",
      "color": "mixed",
      "children": [
        {
          "name": "Democratic Theory & Legitimacy",
          "children": [
            {"name": "Representative Democracy & Legitimacy"},
            {"name": "Deliberative Democracy & Mini-Publics"},
            {"name": "Accountability Theory"},
            {"name": "Transparency & Open Government"},
          ]
        },
        {
          "name": "Behavior & Psychology",
          "children": [
            {"name": "Public Service Motivation ★"},
            {"name": "Behavioral Public Administration ★"},
            {"name": "Procedural Fairness & Trust"},
            {"name": "Citizen Satisfaction & Expectations"},
          ]
        },
        {
          "name": "Equity & Ethics",
          "children": [
            {"name": "Social Equity ★"},
            {"name": "Public Sector Ethics"},
            {"name": "Public Trust in Government"},
          ]
        },
      ]
    },
  ]
}

PROFILES = {

  # ================= ORGANIZATIONS & MANAGEMENT =================

  "Weberian Bureaucracy": {
    "use": "Formal hierarchy, merit appointment, written rules, and impersonality form the technically most efficient — and legitimate — basis of modern state administration.",
    "explain": "Weber's ideal type defines bureaucracy as rational-legal domination: offices are organized in a strict hierarchy, appointed by merit and technical qualification, governed by impersonal written rules, with a clear separation of office and person. Public administration research uses it both as the benchmark for competence and predictability and as the foil for dysfunctions — red tape, rigidity, goal displacement — that later theories explain.",
    "concepts": ["rational-legal authority", "ideal type", "hierarchy", "meritocracy", "impersonality", "rule governance", "red tape"],
    "founders": "Max Weber — Wirtschaft und Gesellschaft (1922; Economy and Society, 1978); 'Politics as a Vocation' (1919). Systematized for American PA by Robert K. Merton and Alvin Gouldner (bureaucratic dysfunctions).",
    "classics": [
      "Weber, M. (1947). From Max Weber: Essays in Sociology (Gerth & Mills, Eds.)",
      "Crozier, M. (1964). The Bureaucratic Phenomenon",
      "Wilson, W. (1887). 'The Study of Administration,' Political Science Quarterly",
    ],
    "frameworks": [
      "Ideal-type methodology — use bureaucracy as a benchmark to measure deviation, not a literal description of any real office",
      "Merton's bureaucratic dysfunctions — trained incapacity, goal displacement, ritualism as unintended byproducts of rules",
      "Gouldner's patterns of bureaucracy — representative vs punishment-centered (mock/representative) bureaucracies",
      "Bozeman's red-tape typology — distinguishing objective rule burden from perceived red tape",
    ],
    "apply": "Use for comparing administrative traditions across countries (Rechtsstaat vs Anglo-American models), measuring rule formalization and red tape in organizations (validated scales by Pandey & Scott), and explaining why rule density produces street-level rigidity. Pairs well with surveys of perceived red tape, cross-country comparison, and organizational ethnography (see Methodology Map).",
  },

  "Street-Level Bureaucracy ★": {
    "use": "Frontline workers — teachers, police officers, social workers — effectively make public policy through discretion exercised under scarcity.",
    "explain": "Lipsky showed that the people who interact with citizens in person are the real policymakers: resource scarcity, ambiguous goals, and high caseloads force them to ration services, simplify routines, and develop coping mechanisms. Implementation is therefore not faithful execution but continuous reconstruction of policy at the point of contact — which makes frontline discretion a permanent feature of governance, to be designed rather than suppressed.",
    "concepts": ["discretion", "coping mechanisms", "rationing", "client typologies", "implementation gap", "moral agency"],
    "founders": "Michael Lipsky — Street-Level Bureaucracy: Dilemmas of the Individual in Public Services (1980; 30th-anniversary ed. 2010).",
    "classics": [
      "Lipsky, M. (1980). Street-Level Bureaucracy",
      "Maynard-Moody, S., & Musheno, M. (2003). Cops, Teachers, Counselors: Stories from the Front Lines of Public Service",
      "Zacka, B. (2017). When the State Meets the Street: Public Service and Moral Agency",
    ],
    "frameworks": [
      "Coping typology (Lipsky) — rationing, creaming, deterrence: the three basic strategies for managing scarcity",
      "Citizen-agent vs state-agent scripts (Maynard-Moody & Musheno) — how workers narrate themselves as advocates or enforcers",
      "Policy alienation framework (Tummers) — strategic, tactical, and operational dimensions of distance from policy",
      "Accountability drift (Zacka) — how mundane workplace demands erode moral agency",
      "Discretion-in-practice grids — mapping when workers use rule-following, case-by-case judgment, or routine processing",
    ],
    "apply": "Core theory for studying implementation, welfare encounters, policing, and frontline digitalization. Typical designs: ethnography of frontline units, vignette or survey experiments on discretionary choices, analysis of case records and decision data, interviews on coping strategies. Combines naturally with process tracing of single cases (see Methodology Map).",
  },

  "Representative Bureaucracy": {
    "use": "A public workforce that mirrors the population (passive representation) tends to serve underrepresented groups better (active representation).",
    "explain": "Rooted in Kingsley's wartime study of the British civil service, the theory holds that demographic similarity builds empathy, trust, and advocacy: bureaucrats draw on their own group experiences when making discretionary decisions, so passive representation converts into active representation when discretion, group salience, and organizational conditions align. It is PA's main bridge between public workforce diversity and social equity outcomes.",
    "concepts": ["passive representation", "active representation", "symbolic representation", "critical mass", "discretion", "social equity"],
    "founders": "J. Donald Kingsley — Representative Bureaucracy (1944); Samuel Krislov (1974); David Rosenbloom (1973); extended empirically by Kenneth Meier.",
    "classics": [
      "Kingsley, J. D. (1944). Representative Bureaucracy",
      "Krislov, S. (1974). Representative Bureaucracy",
      "Selden, S. C. (1997). The Promise of Representative Bureaucracy: Diversity and Responsiveness in a Government Agency",
    ],
    "frameworks": [
      "Passive vs active representation (Mosher) — the classic two-stage distinction linking composition to behavior",
      "Meier's theory of representative bureaucracy — minority representation → attitudes → service outcomes, with school-system tests",
      "Micro-level representation (Riccucci & Van Ryzin) — identification-based empathy in service encounters, tested with vignette experiments",
      "Critical mass & critical actors hypotheses — when does token representation flip to systematic advocacy?",
      "Conditions for active representation — discretion, task salience, group consciousness, organizational mission",
    ],
    "apply": "Link workforce composition data (HR records, FOIA-based rosters) to service outcomes: school discipline by teacher race, police stops by officer demographics, benefit take-up by caseworker assignment. Field and survey experiments test citizen responses to representative bureaucrats. Methods: multilevel models, administrative data, randomized vignettes (see Methodology Map).",
  },

  "Organizational Culture & Decoupling": {
    "use": "Formal structures are often ceremonial myths, decoupled from what organizations actually do to maintain legitimacy.",
    "explain": "Combining Selznick's insight that organizations are infused with value (goals get displaced by survival) with new-institutionalism: to gain legitimacy, agencies adopt rational-looking structures and reforms that are merely 'talk' or ritual compliance, while actual practices continue unchanged (decoupling). Explains why reforms so often fail to change frontline practice and why measurement becomes symbolic.",
    "concepts": ["institutional myth", "ceremonial conformity", "decoupling", "organizational culture", "institutional logics"],
    "founders": "Philip Selznick — TVA and the Grass Roots (1949); John W. Meyer & Brian Rowan — 'Institutionalized Organizations' (1977); DiMaggio & Powell (1983).",
    "classics": [
      "Selznick, P. (1949). TVA and the Grass Roots",
      "Meyer, J. W., & Rowan, B. (1977). 'Institutionalized Organizations,' American Journal of Sociology",
      "DiMaggio, P. J., & Powell, W. W. (1983). 'The Iron Cage Revisited,' American Sociological Review",
    ],
    "frameworks": [
      "Decoupling model (Meyer & Rowan) — formal structure vs actual practice; policy-practice gaps as legitimacy management",
      "Three mechanisms of isomorphism (DiMaggio & Powell) — coercive, mimetic, normative pressures toward sameness",
      "Institutional logics (Thornton, Ocasio & Lounsbury) — competing value systems (state, market, profession, family) inside organizations",
      "Hybrid organization responses (Pache & Santos) — compartmentalization, blending, selective coupling",
      "Ceremonial adoption checklist — talk, decisions, actions, outcomes as separable layers (Brunsson)",
    ],
    "apply": "Diagnose why reforms stall: compare formal rules, espoused practice, and observed frontline behavior in the same organization. Study the global spread of similar administrative forms (performance regimes, transparency portals) through institutional pressure rather than efficiency. Methods: multi-sited fieldwork, document analysis, longitudinal case comparison (see Methodology Map).",
  },

  "New Public Management ★": {
    "use": "Import private-sector management — competition, markets, targets, and performance measurement — into government to cut costs and raise responsiveness.",
    "explain": "Hood's manifesto named the reform wave of the 1980s–90s (Thatcher/Reagan, 'Reinventing Government'): disaggregate hierarchies into agencies, expose them to markets and quasi-markets, measure outputs, and manage by results. NPM remains the reference point against which every later reform (public value, collaboration, digital governance) defines itself; its empirical legacy is mixed efficiency gains plus documented gaming and fragmentation costs.",
    "concepts": ["managerialism", "marketization", "agencification", "performance targets", "steering not rowing", "quasi-markets"],
    "founders": "Christopher Hood — 'A Public Management for All Seasons?' (1991, PAR); David Osborne & Ted Gaebler — Reinventing Government (1992); Donald Kettl (implementation critique).",
    "classics": [
      "Hood, C. (1991). 'A Public Management for All Seasons?,' Public Administration Review",
      "Osborne, D., & Gaebler, T. (1992). Reinventing Government",
      "Pollitt, C. (1993). Managerialism and the Public Services",
    ],
    "frameworks": [
      "Hood's NPM doctrine inventory — seven doctrinal components (hands-on management, explicit standards, output control, disaggregation, competition, private-sector styles, discipline and parsimony)",
      "Osborne & Gaebler's ten principles — catalytic government, competition, mission-driven, results-oriented, customer-driven...",
      "Performance regime & gaming typology (Bevan & Hood) — ratcheting, threshold effects, output distortions under targets",
      "Principal-agent analyses of contracting — market provision as delegation problem",
      "NPM evaluation matrix — cost/efficiency, quality, equity, democratic accountability side-by-side",
    ],
    "apply": "Evaluate reform programs with quasi-experimental designs (difference-in-differences, synthetic control on agency outputs); measure gaming through distorted indicators; compare NPM trajectories across countries. Essential framing for any performance management study. Methods: quasi-experiments, interrupted time series, cross-national comparison (see Methodology Map).",
  },

  "Public Value Management ★": {
    "use": "Public managers are explorers of public value: they create it through deliberation and collective choice, not by merely hitting efficiency targets.",
    "explain": "Moore reframed the public manager's job as creating public value — a 'public value account' weighing outcomes against costs and fairness — and building a legitimacy coalition among authorizing environment, operational capability, and public support. PVM answers NPM's market metaphor with a democratic one: value is defined politically, managers mediate between citizens and outcomes, and legitimacy is built through engagement.",
    "concepts": ["public value", "authorizing environment", "operational capability", "legitimacy coalition", "public value account"],
    "founders": "Mark H. Moore — Creating Public Value: Strategic Management in Government (1995); John Benington & Mark Moore (Eds.), Public Value: Theory and Practice (2011).",
    "classics": [
      "Moore, M. H. (1995). Creating Public Value",
      "Benington, J., & Moore, M. H. (Eds.) (2011). Public Value: Theory and Practice",
      "Bozeman, B. (2007). Public Values and Public Interest: Counterbalancing Economic Individualism",
    ],
    "frameworks": [
      "Strategic triangle (Moore) — public value ↔ legitimacy & support ↔ operational capability; strategy must close the triangle",
      "Public value account — intended outcomes vs costs and fairness, mirroring a balance sheet",
      "Public value failure framework (Bozeman) — market failure analogs: mechanisms for valuing, aggregation, monopoly, etc.",
      "Public value inside (Meynhardt) — psychological operationalization: value creation as felt by public employees and users",
    ],
    "apply": "Use for strategy formulation and evaluation in public organizations, assessing programs where market logic fails (science, culture, security), and legitimacy-building analysis of controversial agencies. Methods: case-based strategy analysis, deliberative evaluation, stakeholder mapping (see Methodology Map).",
  },
}

# ================= ORGANIZATIONS & MANAGEMENT (continued) =================

PROFILES.update({

  "New Public Service": {
    "use": "Serve citizens, not customers: democratic citizenship, community, and the public interest should drive administration, not entrepreneurial steering.",
    "explain": "The Denhardts' normative counter-model to NPM (and to 'steering, not rowing'): government should facilitate democratic dialogue, build shared interests and community, and treat citizens as owners whose trust must be earned — value arises from the deliberative process, not just results. Anchors much of today's citizen-engagement and trust scholarship.",
    "concepts": ["citizenship", "public interest", "community", "democratic governance", "service not steering"],
    "founders": "Robert B. Denhardt & Janet V. Denhardt — The New Public Service: Serving, Not Steering (2000; 4th ed. 2015); 'The New Public Service: Serving Rather Than Steering' (2000, PAR).",
    "classics": [
      "Denhardt, R. B., & Denhardt, J. V. (2000). 'The New Public Service: Serving Rather Than Steering,' Public Administration Review",
      "Fox, C. J., & Miller, H. T. (1995). Postmodern Public Administration",
      "Denhardt, R. B., & Denhardt, J. V. (2015). The New Public Service (4th ed.)",
    ],
    "frameworks": [
      "Seven principles of the New Public Service — serve citizens not customers; seek public interest; value citizenship over entrepreneurship; think strategically act democratically; accountability is hard; serve rather than steer; value people over productivity",
      "Citizen governance (Box) — administrative state, citizenship, and governance as community ownership",
      "Energy-discourse model (Fox & Miller) — authentic deliberation requires energy, relevancy, and invitation",
      "NPS practice matrix — engagement, dialogue, and community-building as testable organizational practices",
    ],
    "apply": "Normative-evaluative lens for engagement programs: test whether participation practices build community and trust rather than merely inform. Design citizen-centered services and dialogue formats. Methods: trust surveys before/after engagement, deliberative evaluation, action research (see Methodology Map).",
  },

  "Post-NPM & Digital-Era Governance": {
    "use": "The reform wave after NPM: reintegrate fragmented agencies, re-aggregate around needs, and exploit digitization end-to-end.",
    "explain": "Dunleavy et al. declared NPM dead: contracting out and agencification multiplied coordination costs and produced silos. Digital-era governance (DEG) predicts reintegration (shared services, joined-up government), needs-based holism (life-event services), and digitization as process redesign, not mere channel addition. Frames today's whole-of-government and AI-in-government research.",
    "concepts": ["reintegration", "needs-based holism", "digitization", "joined-up government", "whole-of-government", "algorithmic governance"],
    "founders": "Patrick Dunleavy, Helen Margetts, Simon Bastow & Jane Tinkler — 'New Public Management Is Dead — Long Live Digital-Era Governance' (2006, JPART); Christensen & Lægreid (whole-of-government).",
    "classics": [
      "Dunleavy, P., Margetts, H., Bastow, S., & Tinkler, J. (2006). 'New Public Management Is Dead — Long Live Digital-Era Governance,' Journal of Public Administration Research and Theory",
      "Christensen, T., & Lægreid, P. (2007). 'The Whole-of-Government Approach to Public Sector Reform,' Public Administration Review",
    ],
    "frameworks": [
      "DEG triad (Dunleavy et al.) — reintegration + needs-based holism + digitization as process change",
      "Whole-of-government coordination instruments (Christensen & Lægreid) — formal, budgetary, informal coordination",
      "Mergel's DEG stages — digitization (e-government) → engagement → context-aware governance",
      "Algorithmic governance framework (Meijer) — public values vs efficiency in automated decision systems",
    ],
    "apply": "Assess digital service platforms and one-stop government; study AI adoption and automation in administrative decision-making; analyze coordination across silos in crisis or major projects. Methods: process tracing of platform reforms, case comparison, platform usage data (see Methodology Map).",
  },

  "Governance & Network Theory ★": {
    "use": "Public outcomes are produced by networks of interdependent public, private, and civic actors — hierarchy and market are only two of many governing modes.",
    "explain": "Rhodes' 'governance' thesis: the state has become a collection of inter-organizational networks marked by mutual dependence and resource exchange; governing now means 'governing without government' — steering through negotiation, meta-governance, and shared purpose rather than command. Kooiman adds governing as the interplay of self-organization, co-managing, and hierarchical control, making governance theory the umbrella for collaboration and network management research.",
    "concepts": ["interdependence", "resource exchange", "meta-governance", "self-organization", "hollow state", "polycentricity"],
    "founders": "R. A. W. Rhodes — 'The New Governance: Governing without Government' (1996, Political Studies); Jan Kooiman — Governing as Governance (2003); Renate Mayntz (network failure).",
    "classics": [
      "Rhodes, R. A. W. (1996). 'The New Governance: Governing without Government,' Political Studies",
      "Kooiman, J. (Ed.) (1993). Modern Governance; Kooiman, J. (2003). Governing as Governance",
      "Pierre, J., & Peters, B. G. (2000). Governance, Politics and the State",
    ],
    "frameworks": [
      "Power-dependence model (Rhodes) — network formation explained by resource dependencies among organizations",
      "Governability framework (Kooiman) — interactions between system-to-be-governed and governing system",
      "Meta-governance repertoire (Sørensen & Torfing) — framing, goal-setting, institutional design, participation, hands-on management",
      "Network effectiveness contingencies (Provan & Milward) — density, centralization, and external environment conditions",
      "Network failure diagnosis (Mayntz) — when networks deadlock, exclude, or drift",
    ],
    "apply": "Map and analyze inter-organizational networks with social network analysis; diagnose governance failure in PPPs and crisis networks; evaluate meta-governance strategies. Methods: SNA, QCA across network cases, elite interviews (see Methodology Map).",
  },

  "Collaborative Governance": {
    "use": "One or more public agencies directly engage non-state stakeholders in a consensus-oriented, collective decision process that is formal, deliberative, and self-enforcing.",
    "explain": "Ansell & Gash's canonical definition and their 161-case meta-analysis showed collaboration emerges from starting conditions (power/resources, incentives, interdependence), facilitative leadership, and institutional design, via face-to-face dialogue, trust, and commitment. Emerson et al. extend it into a dynamic integrative framework (collaborative governance regime ↔ collaborative dynamics ↔ actions/outcomes). The default theory for PPPs, watershed councils, and crisis governance.",
    "concepts": ["consensus orientation", "stakeholder engagement", "trust", "facilitative leadership", "collaborative advantage", "boundary organization"],
    "founders": "Chris Ansell & Alison Gash — 'Collaborative Governance in Theory and Practice' (2008, JPART); Kirk Emerson, Tina Nabatchi & Stephen Balogh — 'An Integrative Framework for Collaborative Governance' (2012, PAR).",
    "classics": [
      "Ansell, C., & Gash, A. (2008). 'Collaborative Governance in Theory and Practice,' Journal of Public Administration Research and Theory",
      "Emerson, K., Nabatchi, T., & Balogh, S. (2012). 'An Integrative Framework for Collaborative Governance,' Public Administration Review",
      "Milward, H. B., & Provan, K. G. (2000). 'Governing the Hollow State,' Journal of Public Administration Research and Theory",
    ],
    "frameworks": [
      "Collaborative dynamics model (Ansell & Gash) — starting conditions + facilitative leadership + institutional design → collaborative process → outcomes, with feedback loops",
      "Integrative framework (Emerson, Nabatchi & Balogh) — collaborative governance regime ↔ drivers → collaborative dynamics → actions & outcomes",
      "Collaborative advantage vs collaborative inertia (Huxham) — why collaboration succeeds or exhausts itself",
      "Six dimensions of collaborative process — face-to-face dialogue, trust-building, commitment, shared understanding, intermediate outcomes",
      "Collaborative platforms model (Ansell & Gash 2018) — orchestrated collaboration across a policy domain",
    ],
    "apply": "Code collaborative cases for meta-analysis; measure trust, commitment, and intermediate outcomes longitudinally; design collaborative institutions and evaluate their performance. Methods: meta-analysis, structured case comparison, network surveys, process tracing (see Methodology Map).",
  },

  "Coproduction & Co-creation ★": {
    "use": "Public services are jointly produced by professionals and citizens; involving users as active partners raises quantity and quality of outcomes.",
    "explain": "From Ostrom's production functions (citizen inputs are often necessary complements to professional labor) to today's co-creation: engagement can range from individual-level coproduction (parenting education alongside schooling) to collective community-level production. Explains why services fail when users are passive, and grounds participatory design, peer support, and community resilience programs.",
    "concepts": ["coproduction", "co-creation", "active citizenship", "service ecosystems", "community production"],
    "founders": "Elinor Ostrom et al., 'The Public Service Production Process' (1978, Policy Studies Journal); Gordon P. Whitaker — 'Coproduction' (1980, PAR); the Indiana Ostrom Workshop.",
    "classics": [
      "Whitaker, G. P. (1980). 'Coproduction: Citizen Participation in Service Delivery,' Public Administration Review",
      "Parks, R. B., et al. (1981). 'Consumers as Coproducers of Public Services,' Journal of Public Administration Research and Theory",
      "Ostrom, E. (1996). 'Crossing the Great Divide: Coproduction, Synergy, and Development,' World Development",
    ],
    "frameworks": [
      "Co-production in the production chain (Ostrom) — regular, individual, collective co-production; coproduction as complement to professional inputs",
      "Co-commissioning ladder (Bovaird & Loeffler) — co-commissioning → co-design → co-delivery → co-assessment as escalating forms",
      "Individual vs collective co-production (Pestoff) — service-level mutual help vs community-level self-organization",
      "Service-dominant logic (Vargo & Lusch) — value co-created in use, adopted by public service research",
      "Co-production risks — self-selection bias, exclusion of hard-to-reach users, hidden costs to volunteers",
    ],
    "apply": "Field experiments testing participation prompts and default designs; measure citizen inputs (volunteer hours, peer support) as production factors; design and evaluate co-created services. Watch for self-selection into coproduction. Methods: RCTs, contribution measurement, qualitative process evaluation (see Methodology Map).",
  },

  "Collaborative Public Management": {
    "use": "Managing across organizational boundaries — through structures, processes, and boundary-spanning leadership — to produce public value no single agency can.",
    "explain": "Agranoff & McGuire distinguish managing IN networks (hierarchies), managing THROUGH networks (networks as tools), and managing WITHIN networks (being a member); effective collaborative public management requires activating, framing, mobilizing, and synthesizing. Thomson & Perry decompose collaboration into governance, administration, organizational autonomy, mutuality, and trust/reciprocity — the process measures used in empirical work.",
    "concepts": ["boundary spanning", "network management", "activating", "framing", "mobilizing", "synthesizing"],
    "founders": "Robert Agranoff & Michael McGuire — Collaborative Public Management: New Strategies for Local Governments (2003); Ann Marie Thomson & James L. Perry (2006, PAR); Rosemary O'Leary & Lisa Blomgren Bingham (2009).",
    "classics": [
      "Agranoff, R., & McGuire, M. (2003). Collaborative Public Management",
      "Thomson, A. M., & Perry, J. L. (2006). 'Collaboration Processes: Inside the Black Box,' Public Administration Review",
      "O'Leary, R., & Bingham, L. B. (Eds.) (2009). The Collaborative Public Manager",
    ],
    "frameworks": [
      "Managerial behavior repertoire (Agranoff & McGuire) — activating, framing, mobilizing, synthesizing as core network-management activities",
      "Five collaboration components (Thomson & Perry) — governance, shared norms/structure, internal administration, organizational autonomy, trust & reciprocity",
      "Agranoff's collaboration stages — conditions → process → structure → contingencies → performance",
      "Network leadership framework — administrative, enabling, and executive roles for network orchestrators",
    ],
    "apply": "Study interlocal service agreements and regional service delivery; survey network managers about their behavioral repertoire; examine collaborative management in emergency response and homeland security. Methods: network surveys, structured case comparison, QCA across collaboration cases (see Methodology Map).",
  },
})

# ================= INSTITUTIONS & POLICY PROCESS =================

PROFILES.update({

  "Rational Choice & Public Choice": {
    "use": "Public outcomes — voting, lobbying, budgeting, bureaucracy — can be explained as the aggregate of self-interested, utility-maximizing individual choices.",
    "explain": "Downs' economic theory of democracy (voters rationally ignorant, parties converge to the median) and Olson's logic of collective action (free-riding defeats latent groups without selective incentives) founded a research program applying microeconomics to politics. In PA it grounds public choice theories of bureaucracy (Niskanen, Tullock), rent-seeking, and the design of constitutions — and provides the foil that behavioral PA later corrects.",
    "concepts": ["rational ignorance", "median voter", "free-riding", "collective action", "rent-seeking", "constitutional choice"],
    "founders": "Anthony Downs — An Economic Theory of Democracy (1957); James Buchanan & Gordon Tullock — The Calculus of Consent (1962); Mancur Olson — The Logic of Collective Action (1965).",
    "classics": [
      "Downs, A. (1957). An Economic Theory of Democracy",
      "Olson, M. (1965). The Logic of Collective Action",
      "Buchanan, J. M., & Tullock, G. (1962). The Calculus of Consent",
    ],
    "frameworks": [
      "Downsian spatial model — party competition around the median voter; turnout calculus (p·B − C + D)",
      "Olson's byproduct/selective incentive theory — why latent groups fail and how they can be organized",
      "Rent-seeking model (Tullock, Krueger) — the social cost of contesting government favors",
      "Constitutional economics (Buchanan & Tullock) — rules for rule-making under uncertainty about one's future position",
      "Bureaucratic supply models — Niskanen, bureau-shaping, and their rivals as competing objective functions",
    ],
    "apply": "Explain institutional design choices (voting rules, bicameralism, contracting-out decisions), model turnout and lobbying, and derive testable predictions about bureaucratic behavior. Experimental economics now tests the self-interest assumption directly. Methods: formal modeling, lab experiments, structural estimation (see Methodology Map).",
  },

  "Budget-Maximizing Bureaucracy": {
    "use": "Bureaucrats maximize their bureau's budget, not its output — monopoly supply plus discretionary information produces oversized government.",
    "explain": "Niskanen's model: since bureaus face no competitors and sponsors (legislatures) cannot meter output, bureau chiefs extract the maximum budget by offering all-or-nothing output bundles, pushing output beyond its optimal level. It generated the dominant empirical predictions about budget growth — and a literature of critiques (bureau-shaping, slack maximization, output rather than budget goals) that sharpened tests of bureaucratic objective functions.",
    "concepts": ["budget maximization", "sponsor", "output metering", "information asymmetry", "oversupply", "all-or-nothing"],
    "founders": "William A. Niskanen Jr. — Bureaucracy and Representative Government (1971); tested and qualified in Blais & Dion (Eds.), The Budget-Maximizing Bureaucrat (1991).",
    "classics": [
      "Niskanen, W. A. (1971). Bureaucracy and Representative Government",
      "Blais, A., & Dion, S. (Eds.) (1991). The Budget-Maximizing Bureaucrat: Appraisals and Evidence",
    ],
    "frameworks": [
      "Niskanen's all-or-nothing demand revelation — the sponsor accepts or rejects the whole output-budget bundle",
      "Blais & Dion's qualitative test battery — what evidence would confirm or refute budget maximization",
      "Bureau-shaping alternative (Dunleavy) — officials maximize task mix and status, not size",
      "Borcherding's government growth accounting — decomposing public sector growth into demand and supply factors",
      "Slack maximization (Migue & Bélanger) — officials trade budget for easier work",
    ],
    "apply": "Test with time-series and panel data on bureau budgets and outputs; examine whether output-based funding changes bureau behavior as predicted; explain waves of privatization and agencification. Methods: panel econometrics, quasi-experimental funding reforms (see Methodology Map).",
  },

  "Bureau-Shaping": {
    "use": "Senior officials maximize personal utility — prestige, interesting work, career rewards — by shaping bureaus toward functions they prefer, not necessarily bigger budgets.",
    "explain": "Dunleavy's critique of Niskanen: officials dislike managing large production-line bureaucracies; they prefer small, elite policy cores near political power. Hence reforms like agencification, contracting-out, and 'Next Steps': senior managers shed routine delivery functions to agencies and contractors while keeping core policy work. Explains privatization and agencification from officials' own incentives.",
    "concepts": ["utility maximization", "policy core", "delivery periphery", "agencification", "hollowing out", "status"],
    "founders": "Patrick Dunleavy — Democracy, Bureaucracy and Public Choice (1991); precursor article 'Bureaucrats, Budgets and the Growth of the State' (1985, BJPS).",
    "classics": [
      "Dunleavy, P. (1991). Democracy, Bureaucracy and Public Choice",
      "Dunleavy, P. (1985). 'Bureaucrats, Budgets and the Growth of the State: Reconstructing an Instrumental Model,' British Journal of Political Science 15(3)",
    ],
    "frameworks": [
      "Bureau-shaping model (Dunleavy) — utility from task mix: policy cores over delivery peripheries; agency types (delivery, regulatory, transfer, contracts)",
      "James' agency-creation tests — applying bureau-shaping to explain the UK's Next Steps agencies",
      "Marsh-Smith-Richards critique — bureaucrats respond to politicians' preferences, not only their own utility",
      "Reputation-building alternative (Carpenter) — agencies innovate to win autonomy through demonstrated competence",
    ],
    "apply": "Explain executive agency formation, agencification waves, and the hollowing-out of central departments; analyze senior officials' preferences through career data and interviews. Methods: historical analysis, elite interviews, process tracing of reorganizations (see Methodology Map).",
  },

  "Principal–Agent Theory": {
    "use": "Delegation creates information asymmetry; principals control agents through monitoring, incentives, reporting rules, and careful selection — each costly.",
    "explain": "Applied to public administration (politicians→bureaucracy, ministries→agencies, government→contractors), P-A theory identifies adverse selection and moral hazard, and prescribes institutional remedies: oversight, performance contracts, civil-service rules, transparency. Waterman & Meier's famous corrective — multiple, competing principals and agents who are themselves principals — made 'backward mapping' and bureaucratic influence standard parts of the toolkit.",
    "concepts": ["delegation", "adverse selection", "moral hazard", "monitoring", "incomplete contracts", "multiple principals"],
    "founders": "Kenneth Arrow / Stephen Ross (formal agency theory); Gary Miller (managerial dilemmas); Richard Waterman & Kenneth Meier (1998, PAR); B. Guy Peters & Jon Pierre.",
    "classics": [
      "Waterman, R. W., & Meier, K. J. (1998). 'Principal–Agent Models: An Expansion?,' Public Administration Review",
      "Miller, G. J. (2005). 'The Political Evolution of Principal–Agent Models,' Annual Review of Political Science",
      "Moe, T. M. (1984). 'The New Economics of Organization,' American Journal of Political Science",
    ],
    "frameworks": [
      "Standard P-A remedies matrix — monitoring, reporting rules, rotation, incentive pay, selection & screening, institutional checks",
      "Expansion model (Waterman & Meier) — multiple principals, agent discretion, and agents-as-principals; forward vs backward mapping",
      "Managerial dilemmas (Miller) — why incentive schemes fail under team production and repeated games",
      "Delegation as commitment device — insulating agents (courts, central banks, regulators) to solve time-inconsistency",
      "Incomplete contracting — what cannot be specified drives the choice between hierarchy, contract, and hybrid",
    ],
    "apply": "Study political control of bureaucracy, agency politicization, performance contracting, and contracting-out governance; analyze when governments insulate vs control administrative bodies. Methods: delegation event analysis, contract analysis, quasi-experimental personnel reforms (see Methodology Map).",
  },

  "Multiple Streams Framework ★": {
    "use": "Policy change happens when problems, policies, and politics streams couple — pushed by policy entrepreneurs through open policy windows.",
    "explain": "Kingdon's Agendas, Alternatives and Public Policies: problems are recognized (indicators, focusing events, feedback), policies float in a 'primeval soup' of ideas, and politics follows predictable national moods and turnover; windows open unpredictably and close fast, so change needs prepared entrepreneurs who couple the streams. Rooted in the Cohen-March-Olsen garbage-can model of organized anarchies; today's most-used framework for agenda-setting studies worldwide.",
    "concepts": ["problem stream", "policy stream", "politics stream", "policy window", "policy entrepreneur", "coupling"],
    "founders": "John W. Kingdon — Agendas, Alternatives, and Public Policies (1984; 2nd ed. 2003/2011); Michael Cohen, James March & Johan Olsen — 'A Garbage Can Model of Organizational Choice' (1972).",
    "classics": [
      "Kingdon, J. W. (1984). Agendas, Alternatives, and Public Policies",
      "Cohen, M. D., March, J. G., & Olsen, J. P. (1972). 'A Garbage Can Model of Organizational Choice,' Administrative Science Quarterly",
      "Zahariadis, N. (1999). Markets, States, and Public Policy (comparative MSF extension)",
    ],
    "frameworks": [
      "Three streams (Kingdon) — problems: indicators, focusing events, feedback; policies: 'primeval soup', criteria (value acceptability, technical feasibility, resource adequacy); politics: national mood, interest groups, turnover",
      "Policy windows & coupling — open by political events or new problems; entrepreneurs invest resources to couple streams",
      "Garbage can model (C-M-O) — organized anarchies: problems, solutions, participants, choice opportunities flow in four semi-independent streams",
      "Refined coupling sequence (Herweg, Huß & Zohlnhöfer) — problematization → agenda setting → decision making as distinct coupling points",
      "Comparative extensions (Zahariadis) — multiple venues, ambiguity, and bargaining beyond the US separation-of-powers context",
    ],
    "apply": "Trace agenda-setting and reform adoption: reconstruct streams and coupling points through elite interviews and documents; compare cases across countries where windows open differently; identify entrepreneurs' resources and strategies. Methods: process tracing, structured-focused comparison, fsQCA across multiple cases (see Methodology Map).",
  },

  "Advocacy Coalition Framework ★": {
    "use": "Policy subsystems are decade-long contests between advocacy coalitions unified by deep-core and policy beliefs; change comes through policy-oriented learning and external shocks.",
    "explain": "Sabatier & Jenkins-Smith rejected the stages model: actors in a subsystem — agencies, legislators, researchers, journalists — sort into coalitions by shared belief systems (deep core → policy core → secondary aspects), use resources to influence institutions, and change only gradually via learning within the coalition structure or abruptly via perturbations (crises, regime change, public opinion swings). Methodologically, it demands 10+ year analyses and is the leading framework for belief-driven policy conflict.",
    "concepts": ["belief system", "advocacy coalition", "policy subsystem", "policy-oriented learning", "perturbations", "policy broker"],
    "founders": "Paul A. Sabatier & Hank C. Jenkins-Smith — Policy Change and Learning: An Advocacy Coalition Approach (1993); Sabatier & Weible (Eds.), Theories of the Policy Process (successive editions).",
    "classics": [
      "Sabatier, P. A., & Jenkins-Smith, H. C. (1988). 'An Advocacy Coalition Framework of Policy Change,' Policy Sciences",
      "Sabatier, P. A., & Weible, C. M. (2007). 'The Advocacy Coalition Framework: Innovations and Clarifications,' in Theories of the Policy Process (2nd ed.)",
      "Jenkins-Smith, H. C., Nohrstedt, D., Weible, C. M., & Sabatier, P. A. (2018). Theories of the Policy Process (4th ed., ACF chapter)",
    ],
    "frameworks": [
      "Belief hierarchy — deep core (normative ontology) → policy core (basic positions within subsystem) → secondary aspects (instrument settings); coalitions cohere around policy core",
      "Policy-oriented learning — across coalitions through professional forums, under conditions of uncertainty; brokers mediate",
      "Perturbations — internal (failures, learning) vs external (socioeconomic change, regime shifts, public opinion swings)",
      "Narrative Policy Framework — stories with setting, characters (hero/villain/victim), moral, and solution as measurable belief carriers",
      "ACF flow model — subsystem attributes → coalitions & strategies → institutional rules → policy outputs → impacts → feedback",
    ],
    "apply": "Run longitudinal subsystem studies (10+ years): track coalitions' belief systems through surveys of subsystem actors, map advocacy networks, content-code arguments for belief positions and narratives. Methods: longitudinal case design, elite surveys, network analysis, discourse analysis (see Methodology Map).",
  },

  "Punctuated Equilibrium Theory ★": {
    "use": "Policy makes long periods of stability with rare bursts of radical change, produced by institutional friction, bounded rationality, and disproportionate information processing.",
    "explain": "Baumgartner & Jones: institutional structures (venues, committees, jurisdictions) filter signals so most issues stay off the agenda; when attention shifts — after focusing events or reframing — the same friction amplifies change, producing leptokurtic (heavy-tailed) policy distributions. Founded the Policy Agendas Project and gave policy studies measurable signatures of friction: kurtosis and skew in budgeting and attention data.",
    "concepts": ["friction", "bounded rationality", "disproportionate information processing", "venue shopping", "policy image", "leptokurtosis"],
    "founders": "Frank R. Baumgartner & Bryan D. Jones — Agendas and Instability in American Politics (1993; 2nd ed. 2009); 'Agenda Dynamics and Policy Subsystems' (1991, Journal of Politics).",
    "classics": [
      "Baumgartner, F. R., & Jones, B. D. (1993). Agendas and Instability in American Politics",
      "True, J. L., Jones, B. D., & Baumgartner, F. R. (1999). 'Punctuated Equilibrium Theory,' in Sabatier (Ed.), Theories of the Policy Process",
      "Jones, B. D., & Baumgartner, F. R. (2005). The Politics of Attention",
    ],
    "frameworks": [
      "Punctuated equilibrium model — stability (venue control, policy monopolies) + punctuation (disproportionate attention response), with feedback",
      "Policy Agendas coding & distributional tests — leptokurtosis, skew, and positive kurtosis as signatures of friction",
      "Disproportionate information processing (Jones & Baumgartner) — cognitive limits + institutional friction → step functions",
      "Venue shopping & policy images — losers in one venue reframe the issue and move to friendlier arenas",
      "Dual-process attention — parallel processing under low attention, serial processing under high attention",
    ],
    "apply": "Analyze budget or attention distributions for kurtosis signatures across countries and levels of government; trace venue shifts and reframing in case studies; build comparative agendas datasets (Comparative Agendas Project). Methods: time-series analysis, distributional statistics, text-as-data attention measures (see Methodology Map).",
  },

  "Policy Feedback & Path Dependence ★": {
    "use": "Policies are politically consequential: they build constituencies, distribute resources, and shape interpretation — locking in (or unlocking) future policy choices.",
    "explain": "Pierson's 'when effect becomes cause': large-scale policies change the landscape of power — beneficiaries defend them, administrative capacities channel later demands, and experiences reshape mass understandings of government. Positive feedback (increasing returns, switching costs, learning, coordination effects) generates path dependence; critical junctures set trajectories. Makes welfare states, administrative institutions, and reform failure intelligible over decades.",
    "concepts": ["policy feedback", "increasing returns", "path dependence", "critical juncture", "lock-in", "resource & interpretive effects"],
    "founders": "Paul Pierson — 'When Effect Becomes Cause' (1993, World Politics); 'Increasing Returns, Path Dependence, and the Study of Politics' (2000, APSR); Theda Skocpol — Protecting Soldiers and Mothers (1992).",
    "classics": [
      "Pierson, P. (1993). 'When Effect Becomes Cause,' World Politics",
      "Pierson, P. (2000). 'Increasing Returns, Path Dependence, and the Study of Politics,' American Political Science Review",
      "Skocpol, T. (1992). Protecting Soldiers and Mothers: The Political Origins of Social Policy in the United States",
    ],
    "frameworks": [
      "Resource effects — policies allocate material resources and mobilize constituencies (benefit visibility, group formation)",
      "Interpretive effects — policies shape mass understandings of deservingness, government, and citizenship",
      "Increasing returns mechanisms — coordination, complementarities, learning, adaptive expectations, setup costs",
      "Gradual change typology (Mahoney & Thelen) — layering, displacement, drift, conversion as transformation modes",
      "Mettler's submerged state — hidden policies weaken feedback visibility and distort citizenship",
    ],
    "apply": "Trace how a policy reshapes participation and coalitions over decades (welfare programs, healthcare, veterans' benefits); analyze why similar reforms land differently on distinct institutional legacies; study sequencing effects in administrative development. Methods: comparative historical analysis, longitudinal process tracing, sequence analysis (see Methodology Map).",
  },

  "Institutional Analysis & Development ★": {
    "use": "Collective action over common-pool resources succeeds when user communities devise and self-enforce rules-in-use — monitored, graduated-sanction, locally-legitimate rules.",
    "explain": "Ostrom's IAD framework dissects the 'action situation' (positions, actions, information, outcomes, control) nested in operational, collective-choice, and constitutional rule tiers; from hundreds of cases she distilled design principles (clear boundaries, congruence, collective-choice arrangements, monitoring, graduated sanctions, conflict-resolution, minimal recognition of rights, nested enterprises). It shifts governance research from market-vs-state to a polycentric understanding of many autonomous centers of rule-making.",
    "concepts": ["action situation", "rules-in-use", "common-pool resource", "collective action", "polycentricity", "social-ecological systems"],
    "founders": "Elinor Ostrom — Governing the Commons (1990, Nobel Prize 2009); Ostrom, Gardner & Walker — Rules, Games, and Common-Pool Resources (1994); Vincent Ostrom (polycentricity).",
    "classics": [
      "Ostrom, E. (1990). Governing the Commons: The Evolution of Institutions for Collective Action",
      "Ostrom, E., Gardner, R., & Walker, J. (1994). Rules, Games, and Common-Pool Resources",
      "Ostrom, E. (2005). Understanding Institutional Diversity",
    ],
    "frameworks": [
      "Action situation grammar — participants, positions, actions, information, control, outcomes, costs/benefits",
      "Rules typology — position, boundary, choice, aggregation, information, payoff, scope rules; operational/collective-choice/constitutional tiers",
      "Eight design principles — boundaries, congruence, collective-choice, monitoring, graduated sanctions, conflict resolution, minimal recognition, nested enterprises",
      "SES framework — resource system, resource units, governance system, users as interacting 2nd-tier variables (McGinnis)",
      "Institutional rational choice — rules shape the structure of the game individuals play",
    ],
    "apply": "Diagnose institutional failure in irrigation, forests, fisheries, urban commons, and digital commons; run lab-in-field experiments testing rules (monitoring, sanctions); design community-based governance programs. Methods: comparative case analysis, framed field experiments, agent-based simulation (see Methodology Map).",
  },

  "Policy Diffusion": {
    "use": "Governments adopt policies partly because other governments adopted them — via learning, imitation, competition, and coercion.",
    "explain": "Event-history analyses of state lotteries, taxes, and innovations showed adoption timing is interdependent: Berry & Berry modeled internal determinants plus regional and national diffusion. Later work disentangles mechanisms (Boehmke & Witmer; Makse & Volden on policy attributes like complexity and cost) and criticizes identification. The backbone of federalism, policy transfer, and global governance-spread research.",
    "concepts": ["policy innovation", "learning", "imitation", "competition", "coercion", "event history analysis"],
    "founders": "Frances Stokes Berry & William D. Berry — 'State Lottery Adoptions as Policy Innovations' (1990, AJPS); Jack Walker — 'The Diffusion of Innovations among the American States' (1969, APSR).",
    "classics": [
      "Berry, F. S., & Berry, W. D. (1990). 'State Lottery Adoptions as Policy Innovations,' American Journal of Political Science",
      "Walker, J. L. (1969). 'The Diffusion of Innovations among the American States,' American Political Science Review",
      "Shipan, C. R., & Volden, C. (2008). 'The Mechanisms of Policy Diffusion,' American Journal of Political Science",
    ],
    "frameworks": [
      "EHA diffusion model (Berry & Berry) — internal determinants + regional & national adoption effects in hazard-rate models",
      "Four mechanisms (Shipan & Volden) — learning, imitation, competition, coercion as distinct spatial/temporal signatures",
      "Policy attributes model (Makse & Volden) — complexity and salience determine learning vs imitation",
      "Disentangling design (Boehmke & Witmer) — separating learning from competition empirically",
      "Constructivist diffusion (Strang & Macy) — imitation, theorization, and network position beyond rational choice",
    ],
    "apply": "Model adoption timing across US states or countries; test which mechanism drives a diffusion wave (e.g., anti-smoking laws, carbon pricing); study international policy transfer and global scripts. Methods: event history analysis, spatial econometrics, network diffusion models (see Methodology Map).",
  },

  "Historical Institutionalism": {
    "use": "Institutions structure conflict over time; the timing and sequence of events — critical junctures and path dependence — explain why similar countries end up with different states.",
    "explain": "Steinmo, Thelen & Longstreth's Structuring Politics institutionalized the approach: institutions distribute power, shape strategies and identities, and produce self-reinforcing sequences. Mahoney & Thelen distinguish gradual institutional change types (layering, displacement, drift, conversion) — directly applicable to administrative reform. In PA, HI explains welfare-state administration, civil-service development, and why reforms land differently on different institutional legacies.",
    "concepts": ["path dependence", "critical junctures", "sequencing", "increasing returns", "layering", "drift"],
    "founders": "Sven Steinmo, Kathleen Thelen & Frank Longstreth (Eds.), Structuring Politics (1992); Paul Pierson — Politics in Time (2004).",
    "classics": [
      "Steinmo, S., Thelen, K., & Longstreth, F. (Eds.) (1992). Structuring Politics",
      "Pierson, P. (2004). Politics in Time: History, Institutions, and Social Analysis",
      "Mahoney, J., & Thelen, K. (2010). Explaining Institutional Change: Ambiguity, Agency, and Power",
    ],
    "frameworks": [
      "Structuring politics — institutions as distributions of power and constraints on strategy, shaping both interests and identities",
      "Increasing returns & path dependence (Pierson) — four mechanisms: coordination, complementarity, learning, adaptive expectations",
      "Gradual change typology — layering (new rules on old), displacement, drift (rules unchanged, context shifts), conversion (rules reinterpreted)",
      "Critical juncture analytics — antecedent conditions, contingency, choice, legacy consolidation",
      "Sequence analysis — order matters: institutional configurations traced over time (Aminzade)",
    ],
    "apply": "Explain divergent administrative reform outcomes across countries with similar pressures; trace civil-service and welfare-state development over the longue durée; analyze how layering creates contradictory administrative hybrids. Methods: comparative historical analysis, process tracing, within-case sequence reconstruction (see Methodology Map).",
  },

  "Sociological Institutionalism": {
    "use": "Institutions are not just rules but culturally embedded scripts and categories: they constitute actors' identities and define what counts as legitimate, rational action.",
    "explain": "March & Olsen's rediscovery of institutions emphasized rules, routines, symbols, and myths; DiMaggio & Powell showed organizations become more similar (isomorphic) through coercive (rules), mimetic (uncertainty), and normative (professions) pressures — explaining the global spread of similar administrative forms (performance measurement, agencies, ISO-style routines) regardless of efficiency.",
    "concepts": ["scripts", "taken-for-grantedness", "isomorphism", "legitimacy", "cognitive frames"],
    "founders": "James G. March & Johan P. Olsen — 'The New Institutionalism' (1984, APSR) and Rediscovering Institutions (1989); DiMaggio & Powell (1983, ASR).",
    "classics": [
      "March, J. G., & Olsen, J. P. (1984). 'The New Institutionalism,' American Political Science Review",
      "March, J. G., & Olsen, J. P. (1989). Rediscovering Institutions: The Organizational Basis of Politics",
      "DiMaggio, P. J., & Powell, W. W. (1983). 'The Iron Cage Revisited,' American Sociological Review",
    ],
    "frameworks": [
      "Isomorphism trichotomy (DiMaggio & Powell) — coercive, mimetic, normative pressures predicting organizational sameness",
      "Myth & ceremony (Meyer & Rowan) — rationalized formal structure as legitimacy resource, decoupled from practice",
      "Institutional logics — intersectoral value systems (state, market, profession, corporation, family) structuring cognition",
      "Institutional entrepreneurship & translation — how actors adapt global scripts locally",
      "Garbage can institutionalism (March & Olsen) — ambiguity, temporal sorting, and rule-following",
    ],
    "apply": "Study worldwide diffusion of administrative practices (performance budgets, transparency laws, agency models); analyze identity and legitimacy in public organizations; explain ceremonial adoption of reforms. Methods: cross-national surveys, discourse and document analysis, network models of diffusion (see Methodology Map).",
  },

  "Discursive Institutionalism": {
    "use": "Ideas and discourse are institutions' content and constructs: change occurs when actors' background ideational abilities and foreground discursive abilities shift.",
    "explain": "Schmidt's fourth new institutionalism: institutions are both structures (contexts of action) and constructs (internalized scripts); 'coordinate' discourse among policy actors and 'communicative' discourse between elites and the public transmit ideas — programs, philosophies, paradigms — enabling change even within seemingly rigid institutions. Bridges PA with policy narratives, framing, and deliberation research.",
    "concepts": ["ideas", "discourse", "frames", "narratives", "coordinative discourse", "communicative discourse"],
    "founders": "Vivien A. Schmidt — 'Discursive Institutionalism' (2008, Annual Review of Political Science); Maarten Hajer — The Politics of Environmental Discourse (1995).",
    "classics": [
      "Schmidt, V. A. (2008). 'Discursive Institutionalism,' Annual Review of Political Science",
      "Schmidt, V. A., & Radaelli, C. M. (2004). 'Policy Change and Discourse in Europe,' West European Politics",
      "Hajer, M. A. (1995). The Politics of Environmental Discourse",
    ],
    "frameworks": [
      "Two levels of discourse — coordinative (among policy actors: policy construction) vs communicative (elite-public: political legitimation)",
      "Three kinds of ideas — philosophies (deep), programs (policy), paradigms (policy core across programs)",
      "Discourse coalitions & story-lines (Hajer) — actors unified by shared narratives, not interests alone",
      "Narrative Policy Framework — setting, characters (hero/villain/victim), moral of the story, solution as analyzable story elements",
      "Discourse network analysis (Leifeld) — mapping actors and concepts in policy debates as affiliation networks",
    ],
    "apply": "Analyze how governments legitimate controversial reforms; trace story-lines across a policy debate; connect framing experiments to institutional change. Methods: discourse analysis, narrative coding, DNA (discourse network analysis), survey experiments (see Methodology Map).",
  },
})

# ================= DEMOCRACY, BEHAVIOR & VALUES =================

PROFILES.update({

  "Representative Democracy & Legitimacy": {
    "use": "Administrative power is legitimate only when anchored in law, expertise, and democratic authorization — the enduring constitutional problem of the administrative state.",
    "explain": "From Wilson's politics-administration dichotomy to Waldo's challenge: bureaucracy inevitably involves discretion and therefore politics. The Friedrich–Finer debate (administrative responsibility through internal professional standards vs external political control) frames today's empirical work on how citizens actually grant legitimacy to agencies — legal-rational authority, expertise, fairness, and participation all matter conditionally.",
    "concepts": ["input/throughput/output legitimacy", "politics-administration dichotomy", "discretion", "responsibility", "administrative state"],
    "founders": "Woodrow Wilson (1887); Dwight Waldo — The Administrative State (1948); Carl Friedrich (1940) vs. Herman Finer (1941); Max Weber (authority types).",
    "classics": [
      "Waldo, D. (1948). The Administrative State: A Study of the Political Theory of American Public Administration",
      "Friedrich, C. J. (1940). 'Public Policy and the Nature of Administrative Responsibility,' in Friedrich & Mason (Eds.), Public Policy",
      "Finer, H. (1941). 'Administrative Responsibility in Democratic Government,' Public Administration Review",
    ],
    "frameworks": [
      "Friedrich–Finer debate — internal professional responsibility vs external political control; the field's founding normative fault line",
      "Three sources of legitimacy — legal mandate, expertise, procedural fairness (Weberian, technocratic, participative)",
      "Scharpf's legitimacy triad — input (democratic authorization), throughput (fair process), output (effective performance)",
      "Suchman's legitimacy typology — pragmatic (self-interest), moral (normative approval), cognitive (taken-for-grantedness)",
      "Discretion-responsibility matrix — when does discretion demand which control mechanism?",
    ],
    "apply": "Test citizens' legitimacy judgments with survey experiments manipulating legal basis, expertise cues, and fairness of procedures; constitutional analysis of discretion in welfare and regulatory agencies; legitimacy tracking of unpopular agencies. Methods: vignette experiments, legitimacy scales, legal analysis (see Methodology Map).",
  },

  "Deliberative Democracy & Mini-Publics": {
    "use": "Decisions are legitimate insofar as they result from reasoned deliberation among free and equal citizens; institutions like citizens' assemblies can institutionalize this.",
    "explain": "Habermas' communicative rationality and Rawlsian public reason ground a tradition distinguishing deliberative from aggregative democracy: preferences should be formed through exchange of reasons under conditions of inclusion and equality. Empirically, mini-publics (citizens' assemblies, deliberative polls) show ordinary citizens can master complex policy trade-offs; PA research tests when deliberation improves legitimacy, knowledge, and policy quality in real governance.",
    "concepts": ["deliberation", "public reason", "communicative rationality", "mini-public", "deliberative system", "co-creation"],
    "founders": "Jürgen Habermas — Theory of Communicative Action (1981), Between Facts and Norms (1996); John Rawls (1971); James Fishkin — Democracy and Deliberation (1991); John Dryzek (2000).",
    "classics": [
      "Habermas, J. (1996). Between Facts and Norms: Contributions to a Discourse Theory of Law and Democracy",
      "Fishkin, J. S. (1991). Democracy and Deliberation: New Directions for Democratic Reform",
      "Dryzek, J. S. (2000). Deliberative Democracy and Beyond: Liberals, Critics, Contestations",
    ],
    "frameworks": [
      "Ideal speech situation & discourse principle (Habermas) — validity claims redeemed through reasoned discourse",
      "Deliberative polling (Fishkin) — random sampling + balanced briefing + moderated small groups + measurement",
      "Mini-public design criteria (OECD) — random selection (representativeness), learning & consultation, deliberation, impact on policy",
      "Deliberative systems approach (Mansbridge et al.) — division of deliberative labor across venues; no single forum need do everything",
      "Discourse Quality Index (DQI) — coding deliberation for justification, respect, constructive politics (Steiner et al.)",
    ],
    "apply": "Evaluate citizens' assemblies and participatory budgeting with pre-post measurement of opinion change, knowledge, and legitimacy; code deliberation quality; design institutional interfaces between mini-publics and elected bodies. Methods: field experiments, deliberation analytics, survey panels (see Methodology Map).",
  },

  "Accountability Theory": {
    "use": "Accountability is a social relationship in which an actor must explain and justify conduct to a forum that can question, judge, and sanction; multiple, conflicting accountability regimes are the norm in public life.",
    "explain": "Romzek & Dubnick's Challenger analysis: public administrators simultaneously answer to legal, bureaucratic, political, and professional accountability regimes, and tragedies often follow wrong expectations about which regime applies. Bovens adds the forum-agent structure and five conceptual questions (who, for what, to whom, why, how). Empirical work maps accountability forums (auditors, courts, parliaments, media, citizens) and studies their real effects on behavior.",
    "concepts": ["forum-agent", "answerability", "enforcement", "accountability regimes", "blame", "reputation"],
    "founders": "Barbara Romzek & Melvin Dubnick — 'Accountability in the Public Sector' (1987, PAR); Mark Bovens (2007); Patricia Day & Rudolf Klein (1987).",
    "classics": [
      "Romzek, B. S., & Dubnick, M. J. (1987). 'Accountability in the Public Sector: Lessons from the Challenger Tragedy,' Public Administration Review",
      "Bovens, M. (2007). 'Analysing and Assessing Accountability: A Conceptual Framework,' European Journal of Political Research",
      "Romzek, B. S. (1998). 'Where the Buck Stops: Accountability as a Form of Control,' in Ferlie et al. (Eds.), The Oxford Handbook of Public Management",
    ],
    "frameworks": [
      "Four accountability regimes (Romzek & Dubnick) — hierarchical (bureaucratic), legal, political, professional; effective management means managing their competing expectations",
      "Forum-agent five questions (Bovens) — who is accountable, for what, to whom, why, and how (informing vs debating forums)",
      "Fire-alarm vs police-patrol oversight (McCubbins & Schwartz) — reactive triggers vs direct monitoring",
      "Social accountability & reputation triangle (Schillemans) — transparency, reputation, and accountability in the digital age",
      "Blame-management strategies (Hood, Brändström & Kuipers) — denial, blame-shifting, scapegoating, self-flagellation",
    ],
    "apply": "Map accountability forums around an agency and test their behavioral effects; evaluate performance audits and supreme audit institutions; analyze blame games in crisis response. Methods: survey experiments, process tracing of accountability events, comparative audit evaluation (see Methodology Map).",
  },

  "Transparency & Open Government": {
    "use": "Making government visible improves accountability, trust, and self-regulation — but full transparency can also fuel blame avoidance, gaming, and decision paralysis.",
    "explain": "From Hood & Heald's normative volume to Meijer's interactional model: transparency is not a product government delivers but a dynamic relationship between information provision and its use by citizens, media, and watchdogs. Empirics complicate the gospel: transparency raises perceived trustworthiness only when information is useful and intelligible; it can also induce risk-averse administration and strategic communication ('transparency illusions').",
    "concepts": ["transparency", "openness", "visibility", "intelligibility", "accountability", "gaming"],
    "founders": "Christopher Hood & David Heald (Eds.), Transparency: The Key to Better Governance? (2006); Albert Meijer — 'Understanding the Complex Dynamics of Transparency' (2013, PAR).",
    "classics": [
      "Hood, C., & Heald, D. (Eds.) (2006). Transparency: The Key to Better Governance?",
      "Meijer, A. J. (2013). 'Understanding the Complex Dynamics of Transparency,' Public Administration Review",
      "Birkinshaw, P. (2006). 'Freedom of Information and Openness: Fundamental Human Rights?,' Administrative Law Review",
    ],
    "frameworks": [
      "Dynamic transparency model (Meijer) — transparency as interaction between information supply and societal use, with feedback",
      "Varieties of transparency (Hood & Heald) — nominal vs effective; proactive vs reactive; forced vs voluntary",
      "Active vs passive transparency (Cucciniello; de Fine Licht) — actively pushed info vs info citizens must seek",
      "Transparency action cycle (Grimmelikhuijsen & Meijer) — perception, evaluation, and behavioral effects of information",
      "Transparency-gaming hypothesis — visibility without slack induces risk aversion and blame avoidance (Hood)",
    ],
    "apply": "Run online experiments varying transparency of government information; study FOIA request patterns and open-data use; evaluate whether transparency reforms change official behavior (gaming vs learning). Methods: survey/online experiments, usage data analysis, interrupted time series (see Methodology Map).",
  },

  "Public Service Motivation ★": {
    "use": "People are attracted to and energized by public service because of an intrinsic motivation to serve the public interest — and this matters for performance, selection, and job design.",
    "explain": "Rainey's finding that public managers value work that helps others differently from private managers, formalized by Perry & Wise: PSM comprises attraction to policy-making, commitment to the public interest, compassion, and self-sacrifice. Theory: person-environment fit raises performance and lowers turnover; crowding theory warns that extrinsic incentives can displace it. The single most productive construct in behavioral PA, now with validated scales and cross-national measurement.",
    "concepts": ["public service motivation", "prosocial motivation", "person-environment fit", "crowding out", "intrinsic motivation", "selection"],
    "founders": "Hal G. Rainey (1982, PAR); James L. Perry & Lois Recascino Wise (1990, Review of Public Personnel Administration); Perry (1996, JPART measurement).",
    "classics": [
      "Perry, J. L., & Wise, L. R. (1990). 'The Motivational Bases of Public Service,' Public Administration Review",
      "Perry, J. L. (1996). 'Measuring Public Service Motivation: An Assessment of Construct Reliability and Validity,' Journal of Public Administration Research and Theory",
      "Perry, J. L., & Hondeghem, A. (Eds.) (2008). Motivation in Public Management",
    ],
    "frameworks": [
      "Four-dimension PSM scale (Perry) — attraction to policy-making, commitment to public interest, compassion, self-sacrifice",
      "Three motivational bases (Perry & Wise) — rational (participation), normative (duty/citizenship), affective (identification)",
      "Self-Determination Theory micro-foundation (Deci & Ryan) — autonomy, competence, relatedness as PSM's psychological engine",
      "Crowding theory (Frey & Jegen) — extrinsic rewards can undermine intrinsic motivation; testable in pay-for-performance designs",
      "Person-environment fit (Kristof-Brown applied to PSM) — fit between PSM and organizational publicness predicts outcomes",
    ],
    "apply": "Measure PSM in employee surveys; run field experiments on incentive design (does pay-for-performance crowd out PSM?); use PSM in selection and HR analytics. Methods: psychometric validation, field experiments, multilevel analysis of nested employee data (see Methodology Map).",
  },

  "Behavioral Public Administration ★": {
    "use": "Combine psychological theory and experimental methods with PA questions — how citizens perceive, judge, and respond to government, and how officials actually decide.",
    "explain": "Grimmelikhuijsen & Tummers named the field: a two-way street in which PA supplies realistic contexts and psychology supplies theory and rigorous identification (lab, survey, and field experiments). Core topics: trust in government, transparency processing, fairness perceptions, nudges in services, PSM and pro-social behavior, stereotypes of bureaucrats. It has made experimentation a mainstream PA method and connected the field to behavioral economics.",
    "concepts": ["nudge", "bias", "framing", "trust cues", "procedural justice", "experimentation"],
    "founders": "Stephan Grimmelikhuijsen & Lars Tummers — 'Behavioral Public Administration' (2017, PAR); foundations in Thaler & Sunstein (2008), Tyler, and Perry & Wise.",
    "classics": [
      "Grimmelikhuijsen, S., & Tummers, L. (2017). 'Behavioral Public Administration: Combining Insights from Public Administration and Psychology,' Public Administration Review",
      "Thaler, R. H., & Sunstein, C. R. (2008). Nudge: Improving Decisions about Health, Wealth, and Happiness",
      "Battaglio, R. P., Jr., et al. (2019). 'Behavioral Public Administration: A Map of the Field,' Public Administration",
    ],
    "frameworks": [
      "Dual-process theory (Kahneman) — System 1 intuitive vs System 2 deliberative processing of government information",
      "Nudge taxonomy (Thaler & Sunstein) — defaults, simplification, salience, reminders, social norms as choice architecture",
      "Sludge framework (Sunstein; Herd & Moynihan) — excessive frictions in citizen-state interactions; sludge audits",
      "Three-stage transparency processing — attention, comprehension, evaluation (Grimmelikhuijsen & Meijer)",
      "Behavioral experiment hierarchy — lab (control), survey vignette (realism), field (external validity) trade-offs",
    ],
    "apply": "Design RCTs of service letters, benefit application forms, and compliance communications; test framing and trust cues in official messages; run lab studies of how citizens process transparency. Prime directive: pre-register, replicate, and mind external validity. Methods: lab/survey/field experiments, sludge audits (see Methodology Map).",
  },

  "Procedural Fairness & Trust": {
    "use": "People comply and cooperate when they experience procedures as fair and authorities as trustworthy — regardless of whether outcomes favor them.",
    "explain": "Tyler's procedural justice research overturned outcome-based accounts of compliance: legitimacy — the internalized obligation to obey — follows from fair treatment, neutral, consistent procedures and trustworthy motives. Lind & Tyler's group-value model adds that fair procedures signal respect and standing. Applied across policing, taxation, courts, and regulation, it is the behavioral engine of voluntary compliance and police-legitimacy reform.",
    "concepts": ["procedural justice", "distributive justice", "interactional justice", "legitimacy", "voluntary compliance", "fair treatment"],
    "founders": "Tom R. Tyler — Why People Obey the Law (1990; 2006 Princeton ed.); Allan Lind & Tom Tyler — The Social Psychology of Procedural Justice (1988).",
    "classics": [
      "Tyler, T. R. (1990). Why People Obey the Law",
      "Lind, E. A., & Tyler, T. R. (1988). The Social Psychology of Procedural Justice",
      "Tyler, T. R. (2006). Why People Obey the Law (2nd ed., Princeton)",
    ],
    "frameworks": [
      "Process-based regulation (Tyler) — legitimacy → voluntary compliance, independent of deterrence",
      "Group-value model (Lind & Tyler) — fair procedures signal respect and group standing, beyond instrumental stakes",
      "Leventhal's six criteria — consistency, bias suppression, accuracy, correctability, representativeness, ethicality",
      "Four-component model (procedural justice policing) — neutrality, trustworthiness (benevolence), voice, respect",
      "Legitimacy-cooperation pathway — legitimacy → obligation → compliance → cooperation with police",
    ],
    "apply": "Field trials of procedurally just policing and respectful tax administration; survey experiments manipulating voice and neutrality; compliance outcome tracking (filing, payment, re-offense). Methods: randomized field experiments, legitimacy scales, linked behavioral outcomes (see Methodology Map).",
  },

  "Citizen Satisfaction & Expectations": {
    "use": "Citizen satisfaction with services is shaped not only by performance but by expectations and their confirmation — the psychological metric of public management.",
    "explain": "Van Ryzin transplanted the expectancy-disconfirmation model to public services: satisfaction = f(perceived performance, expectations, disconfirmation), explaining why objectively similar services yield different satisfaction and why satisfaction with government exceeds performance levels. Distinguishing satisfaction as consumer experience from trust as political attitude clarified measurement in ACSI-style indices and anchored empirical public management.",
    "concepts": ["satisfaction", "expectations", "disconfirmation", "service quality", "trust", "indices"],
    "founders": "Gregg G. Van Ryzin — 'The Measurement of Overall Citizen Satisfaction' (2004, PAR) and expectancy-disconfirmation tests (2006, JPART); Richard L. Oliver (1980) for the consumer model.",
    "classics": [
      "Van Ryzin, G. G. (2004). 'The Measurement of Overall Citizen Satisfaction,' Public Administration Review",
      "Van Ryzin, G. G. (2006). 'Testing the Expectancy Disconfirmation Model of Citizen Satisfaction with Local Government,' Journal of Public Administration Research and Theory",
      "Van Ryzin, G. G., & Immerwahr, S. (2007). 'Importance–Performance Analysis of Citizen Satisfaction Surveys,' Public Administration Review",
    ],
    "frameworks": [
      "Expectancy-disconfirmation model (Oliver; Van Ryzin) — satisfaction = perceived performance − expectations, with disconfirmation as mediator",
      "ACSI adaptation — the American Customer Satisfaction Index adapted to public services (Fornell model)",
      "SERVQUAL dimensions — tangibles, reliability, responsiveness, assurance, empathy as service-quality drivers",
      "Importance-performance analysis (IPA; Van Ryzin & Immerwahr) — prioritize improvements by importance × performance quadrants",
      "Satisfaction vs trust distinction — consumer experience vs political support as separate constructs",
    ],
    "apply": "Build citizen satisfaction indices for local services; run importance-performance analysis for improvement prioritization; study how digital services and co-production shift expectations. Methods: survey measurement, IPA, structural equation modeling (see Methodology Map).",
  },

  "Social Equity ★": {
    "use": "Public administration has an affirmative obligation to promote fairness and justice for protected and marginalized groups — alongside efficiency and economy.",
    "explain": "Frederickson's Minnowbrook challenge made equity PA's 'third pillar' (with economy and efficiency): administrators hold a direct responsibility for social equity, not merely neutral competence. Today's operational agenda includes representative bureaucracy, equitable service allocation, and the equity turn in administrative burden research — who pays the learning, psychological, and compliance costs of interacting with the state.",
    "concepts": ["social equity", "fairness", "distributive justice", "administrative burden", "deservingness"],
    "founders": "H. George Frederickson — 'Toward a New Public Administration' (1968, Minnowbrook); Frederickson (2010) Social Equity and Public Administration (2nd ed.); Norma M. Riccucci & Susan T. Gooden.",
    "classics": [
      "Frederickson, H. G. (1971). 'Toward a New Public Administration,' in F. Marini (Ed.), Toward a New Public Administration: The Minnowbrook Perspective",
      "Frederickson, H. G. (2010). Social Equity and Public Administration: Origins, Developments, and Applications (2nd ed.)",
      "Gooden, S. T. (2015). Race and Social Equity: A Nervous Area of Government",
    ],
    "frameworks": [
      "Three pillars of PA — economy, efficiency, equity (Frederickson): equity as co-equal evaluative criterion",
      "Gooden's three pillars of social equity — substantive (outcomes), procedural (process fairness), structural (representation and access)",
      "Administrative burden typology (Herd & Moynihan) — learning, psychological, compliance costs as measurable inequity",
      "Equity audit — systematic disparity assessment across service allocation, process, and outcomes",
      "Deservingness criteria (van Oorschot) — perceived control, attitude, reciprocity, identity, age shaping who bears burdens",
    ],
    "apply": "Conduct equity audits of benefit take-up and sanction rates across groups; measure administrative burdens with time-and-motion audits of applications; study racialized and classed burden distribution. Methods: disparity statistics, audit studies, burden measurement, QCA (see Methodology Map).",
  },

  "Public Sector Ethics": {
    "use": "Public office entails role-based moral obligations — responsible discretion, integrity, and stewardship — beyond legal minimums and personal morality.",
    "explain": "From Waldo's question 'who should rule the rulers?' through Rohr's regime-value ethics and Cooper's responsible administrator model: ethical PA balances objective responsibility (accountability structures) with subjective responsibility (internalized moral agency). Thompson's paradox — administrative decisions are morally divisible yet bureaucracies demand personal integrity — frames today's empirical work on ethical climate, corruption, and integrity systems.",
    "concepts": ["integrity", "responsibility", "discretion", "whistleblowing", "ethical climate", "corruption"],
    "founders": "Dwight Waldo (1948); John A. Rohr — Ethics for Bureaucrats (1978); Terry L. Cooper — The Responsible Administrator (1990; 6th ed. 2012); Dennis F. Thompson (1985, PAR).",
    "classics": [
      "Rohr, J. A. (1978). Ethics for Bureaucrats: An Essay on Law and Values",
      "Cooper, T. L. (2012). The Responsible Administrator: An Approach to Ethics for the Administrative Role (6th ed.)",
      "Thompson, D. F. (1985). 'The Possibility of Administrative Ethics,' Public Administration Review",
    ],
    "frameworks": [
      "Responsible administrator model (Cooper) — problem definition → multiple alternatives → analysis of competing obligations → creative middle-ground possibilities → anticipation of self-deception",
      "Regime values approach (Rohr) — ethical obligations derived from constitutional principles of the regime",
      "Paradox of responsibility (Thompson) — many hands divide responsibility; many eyes demand personal accountability",
      "Ethical climate & culture instruments — individual, organizational, and systemic levels of integrity",
      "National integrity system (Transparency International) — pillars (legislature, executive, courts, audit, ombudsman, media, civil society) and their interdependence",
    ],
    "apply": "Survey ethical climate in agencies and link to misconduct; evaluate whistleblowing channels and anti-corruption commissions; run vignette experiments on ethical decision-making under pressure. Methods: vignette experiments, compliance data, institutional assessment frameworks (see Methodology Map).",
  },

  "Public Trust in Government": {
    "use": "Citizens' diffuse trust in government rests on evaluations of competence, benevolence, and integrity of both political institutions and administrative encounters.",
    "explain": "Easton's distinction between diffuse support and specific support structures the field: trust is a reservoir built by fair, competent performance across everyday administrative encounters — policing, benefits, schools — not just macro-politics. Administration scholars therefore test how service quality, procedural fairness, transparency, and burden shape trust, treating the administrative state as a daily producer (or destroyer) of political trust.",
    "concepts": ["political trust", "diffuse support", "competence", "benevolence", "integrity", "service encounters"],
    "founders": "David Easton — A Systems Analysis of Political Life (1965); William Gamson — Power and Disillusionment (1968); Bouckaert & Van de Walle (2003, PAR).",
    "classics": [
      "Easton, D. (1965). A Systems Analysis of Political Life",
      "Gamson, W. A. (1968). Power and Disillusionment",
      "Bouckaert, G., & Van de Walle, S. (2003). 'Comparing Measures of Citizen Trust and User Satisfaction as Indicators of Good Governance,' Public Administration Review",
    ],
    "frameworks": [
      "Diffuse vs specific support (Easton) — reservoir of legitimacy vs satisfaction with incumbents and outputs",
      "Trustworthiness triad (Mayer, Davis & Schoorman) — ability, benevolence, integrity as antecedents of trust",
      "Service-then-trust model (Van Ryzin) — administrative encounters precede and shape political trust",
      "Satisfaction–trust distinction (Bouckaert & Van de Walle) — consumer satisfaction and political trust are separate measures of 'good governance'",
      "Trust-performance loop — performance builds trust, trust buys discretion for reform, slack enables performance",
    ],
    "apply": "Link administrative performance and fairness to trust with panel surveys; test trust repair after scandals or service failures; study how digitalization and burden reshape trust across demographic groups. Methods: panel surveys, linked administrative-survey data, randomized communication experiments (see Methodology Map).",
  },
})
