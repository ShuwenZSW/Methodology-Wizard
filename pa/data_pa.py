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
             Fields: use     = core proposition (one sentence)
                     explain = what the theory says and why it matters
                     founders= foundational scholars & seminal works
                     classics= 2-3 classic readings
                     frontier= 2-3 cutting-edge empirical studies / agendas
                               in top journals (PAR, JPART, Governance,
                               Public Administration, PMR, JPAM, ARPA ...)

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
    "founders": "Max Weber — Wirtschaft und Gesellschaft (1922; Economy and Society, 1978); 'Politics as a Vocation' (1919). Systematized for American PA by Robert K. Merton and Alvin Gouldner (bureaucratic dysfunctions).",
    "classics": [
      "Weber, M. (1947). From Max Weber: Essays in Sociology (Gerth & Mills, Eds.)",
      "Crozier, M. (1964). The Bureaucratic Phenomenon",
      "Wilson, W. (1887). 'The Study of Administration,' Political Science Quarterly",
    ],
    "frontier": [
      "Moynihan, D., & Herd, P. (2010). 'Red Tape and Democracy: How Rules Affect Citizenship Rights,' American Review of Public Administration 40(6) — administrative burden as a threat to citizenship; foundational for the equity turn in red-tape research.",
      "Contemporary empirical stream in Public Administration Review on measuring and reducing red tape burdens in frontline service delivery.",
    ],
  },

  "Street-Level Bureaucracy ★": {
    "use": "Frontline workers — teachers, police officers, social workers — effectively make public policy through discretion exercised under scarcity.",
    "explain": "Lipsky showed that the people who interact with citizens in person are the real policymakers: resource scarcity, ambiguous goals, and high caseloads force them to ration services, simplify routines, and develop coping mechanisms. Implementation is therefore not faithful execution but continuous reconstruction of policy at the point of contact — which makes frontline discretion a permanent feature of governance, to be designed rather than suppressed.",
    "founders": "Michael Lipsky — Street-Level Bureaucracy: Dilemmas of the Individual in Public Services (1980; 30th-anniversary ed. 2010).",
    "classics": [
      "Lipsky, M. (1980). Street-Level Bureaucracy",
      "Maynard-Moody, S., & Musheno, M. (2003). Cops, Teachers, Counselors: Stories from the Front Lines of Public Service",
      "Zacka, B. (2017). When the State Meets the Street: Public Service and Moral Agency",
    ],
    "frontier": [
      "Tummers, L., Bekkers, V., & Voorberg, W. (2015). 'Policy Alienation of Public Professionals: The Interactive Effects of General Doubts and Day-to-Day Work,' Public Administration Review.",
      "Emerging empirical agenda on algorithmic management of frontline discretion — how algorithms reshape (and constrain) street-level decision-making, in Journal of Public Administration Research and Theory and Public Administration Review.",
    ],
  },

  "Representative Bureaucracy": {
    "use": "A public workforce that mirrors the population (passive representation) tends to serve underrepresented groups better (active representation).",
    "explain": "Rooted in King'sley's wartime study of the British civil service, the theory holds that demographic similarity builds empathy, trust, and advocacy: bureaucrats draw on their own group experiences when making discretionary decisions, so passive representation converts into active representation when discretion, group salience, and organizational conditions align. It is PA's main bridge between public workforce diversity and social equity outcomes.",
    "founders": "J. Donald Kingsley — Representative Bureaucracy (1944); Herbert Kaufman (patronage vs. merit context); Samuel Krislov (1974); David Rosenbloom (1973, 'equal protection' bureaucracies).",
    "classics": [
      "Kingsley, J. D. (1944). Representative Bureaucracy",
      "Krislov, S. (1974). Representative Bureaucracy",
      "Selden, S. C. (1997). The Promise of Representative Bureaucracy: Diversity and Responsiveness in a Government Agency",
    ],
    "frontier": [
      "Riccucci, N. M., & Van Ryzin, G. G. (2017). 'Representative Bureaucracy: A Lever to Enhance Social Equity, Coproduction, and Democracy,' Public Administration Review — field experiments showing representative teachers reduce school-discipline disparities.",
      "Nicholson-Crotty, S., Nicholson-Crotty, J., & Fernandez, S. (2016). 'Will More Black Cops Matter? Officer Race and Police-Involved Homicides of Black Citizens,' Public Administration Review.",
    ],
  },

  "Organizational Culture & Decoupling": {
    "use": "Formal structures are often ceremonial myths, decoupled from what organizations actually do to maintain legitimacy.",
    "explain": "Combining Selznick's insight that organizations are infused with value (goals get displaced by survival) with new-institutionalism: to gain legitimacy, agencies adopt rational-looking structures and reforms that are merely 'talk' or ritual compliance, while actual practices continue unchanged (decoupling). Explains why reforms so often fail to change frontline practice and why measurement becomes symbolic.",
    "founders": "Philip Selznick — TVA and the Grass Roots (1949); John W. Meyer & Brian Rowan — 'Institutionalized Organizations: Formal Structure as Myth and Ceremony' (1977); DiMaggio & Powell (1983).",
    "classics": [
      "Selznick, P. (1949). TVA and the Grass Roots",
      "Meyer, J. W., & Rowan, B. (1977). 'Institutionalized Organizations,' American Journal of Sociology",
      "DiMaggio, P. J., & Powell, W. W. (1983). 'The Iron Cage Revisited,' American Sociological Review",
    ],
    "frontier": [
      "Bromley, P., & Powell, W. W. (2012). 'From Smoke and Mirrors to Walking the Talk: Decoupling in the Contemporary World,' Academy of Management Annals — theoretical stock-taking now feeding PA studies of reform implementation.",
      "Empirical studies of institutional logics and hybridity in public and hybrid organizations in Public Management Review and Governance.",
    ],
  },

  "New Public Management ★": {
    "use": "Import private-sector management — competition, markets, targets, and performance measurement — into government to cut costs and raise responsiveness.",
    "explain": "Hood's manifesto named the reform wave of the 1980s–90s (Thatcher/Reagan, 'Reinventing Government'): disaggregate hierarchies into agencies, expose them to markets and quasi-markets, measure outputs, and manage by results. NPM remains the reference point against which every later reform (public value, collaboration, digital governance) defines itself; its empirical legacy is mixed efficiency gains plus documented gaming and fragmentation costs.",
    "founders": "Christopher Hood — 'A Public Management for All Seasons?' (1991, PAR); David Osborne & Ted Gaebler — Reinventing Government (1992); Donald Kettl (implementation critique).",
    "classics": [
      "Hood, C. (1991). 'A Public Management for All Seasons?,' Public Administration Review",
      "Osborne, D., & Gaebler, T. (1992). Reinventing Government",
      "Pollitt, C. (1993). Managerialism and the Public Services",
    ],
    "frontier": [
      "Bevan, G., & Hood, C. (2006). 'What's Measured Is What Matters: Targets and Gaming in the English Public Health Care System,' Public Administration — canonical evidence of performance-regime gaming.",
      "Hood, C., & Dixon, R. (2015). A Government That Worked Better and Cost Less? Evaluating Three Decades of Reform and Change in UK Central Government — full empirical audit of the NPM experiment.",
    ],
  },

  "Public Value Management ★": {
    "use": "Public managers are explorers of public value: they create it through deliberation and collective choice, not by merely hitting efficiency targets.",
    "explain": "Moore reframed the public manager's job as creating public value — a 'public value account' weighing outcomes against costs and fairness — and building a legitimacy coalition among authorizing environment, operational capability, and public support. PVM answers NPM's market metaphor with a democratic one: value is defined politically, managers mediate between citizens and outcomes, and legitimacy is built through engagement.",
    "founders": "Mark H. Moore — Creating Public Value: Strategic Management in Government (1995); John Benington & Mark Moore (Eds.), Public Value: Theory and Practice (2011).",
    "classics": [
      "Moore, M. H. (1995). Creating Public Value",
      "Benington, J., & Moore, M. H. (Eds.) (2011). Public Value: Theory and Practice",
      "Bozeman, B. (2007). Public Values and Public Interest: Counterbalancing Economic Individualism",
    ],
    "frontier": [
      "Meynhardt, T. (2009). 'Public Value Inside: What Is Public Value Creation?,' International Journal of Public Administration — psychological operationalization used in empirical studies.",
      "Empirical applications of the public value failure framework (Bozeman) to science policy and infrastructure governance in Public Administration Review and Administration & Society.",
    ],
  },

  "New Public Service": {
    "use": "Serve citizens, not customers: democratic citizenship, community, and the public interest should drive administration, not entrepreneurial steering.",
    "explain": "The Denhardts' normative counter-model to NPM (and to 'steering, not rowing'): government should facilitate democratic dialogue, build shared interests and community, and treat citizens as owners whose trust must be earned — value arises from the deliberative process, not just results. Anchors much of today's citizen-engagement and trust scholarship.",
    "founders": "Robert B. Denhardt & Janet V. Denhardt — The New Public Service: Serving, Not Steering (2000; 4th ed. 2015); 'The New Public Service: Serving Rather Than Steering' (2000, PAR).",
    "classics": [
      "Denhardt, R. B., & Denhardt, J. V. (2000). 'The New Public Service: Serving Rather Than Steering,' Public Administration Review",
      "Fox, C. J., & Miller, H. T. (1995). Postmodern Public Administration",
      "Denhardt, R. B., & Denhardt, J. V. (2015). The New Public Service (4th ed.)",
    ],
    "frontier": [
      "Contemporary empirical tests linking citizen-engagement practice to trust and legitimacy, e.g., studies of participatory budgeting and deliberative forums in Public Administration Review and Governance.",
    ],
  },

  "Post-NPM & Digital-Era Governance": {
    "use": "The reform wave after NPM: reintegrate fragmented agencies, re-aggregate around needs, and exploit digitization end-to-end.",
    "explain": "Dunleavy et al. declared NPM dead: contracting out and agencification multiplied coordination costs and produced silos. Digital-era governance (DEG) predicts reintegration (shared services, joined-up government), needs-based holism (life-event services), and digitization as process redesign, not mere channel addition. Frames today's whole-of-government and AI-in-government research.",
    "founders": "Patrick Dunleavy, Helen Margetts, Simon Bastow & Jane Tinkler — 'New Public Management Is Dead — Long Live Digital-Era Governance' (2006, JPART); Christensen & Lægreid (whole-of-government).",
    "classics": [
      "Dunleavy, P., Margetts, H., Bastow, S., & Tinkler, J. (2006). 'New Public Management Is Dead — Long Live Digital-Era Governance,' Journal of Public Administration Research and Theory",
      "Christensen, T., & Lægreid, P. (2007). 'The Whole-of-Government Approach to Public Sector Reform,' Public Administration Review",
    ],
    "frontier": [
      "Empirical studies of digitalization outcomes and algorithmic/AI governance in public organizations — a fast-growing agenda across JPART, Public Administration Review, and Governance (2020s).",
      "Meijer, A. (Ed.) stream on the algorithmic state and automated decision-making in public administration.",
    ],
  },

  "Governance & Network Theory ★": {
    "use": "Public outcomes are produced by networks of interdependent public, private, and civic actors — hierarchy and market are only two of many governing modes.",
    "explain": "Rhodes' 'governance' thesis: the state has become a collection of inter-organizational networks marked by mutual dependence and resource exchange; governing now means 'governing without government' — steering through negotiation, meta-governance, and shared purpose rather than command. Kooiman adds governing as the interplay of self-organization, co-managing, and hierarchical control, making governance theory the umbrella for collaboration and network management research.",
    "founders": "R. A. W. Rhodes — 'The New Governance: Governing without Government' (1996, Political Studies); Jan Kooiman — Governing as Governance (2003); Renate Mayntz (network failure); Fritz Scharpf.",
    "classics": [
      "Rhodes, R. A. W. (1996). 'The New Governance: Governing without Government,' Political Studies",
      "Kooiman, J. (Ed.) (1993). Modern Governance; Kooiman, J. (2003). Governing as Governance",
      "Pierre, J., & Peters, B. G. (2000). Governance, Politics and the State",
    ],
    "frontier": [
      "Sørensen, E., & Torfing, J. (2017). 'Meta-governance of Collaborative Innovation,' British Journal of Politics and International Relations — empirical framing of how public authorities govern networks.",
      "Network-level empirical studies of collaborative capacity and meta-governance instruments in Public Management Review and Governance.",
    ],
  },

  "Collaborative Governance": {
    "use": "One or more public agencies directly engage non-state stakeholders in a consensus-oriented, collective decision process that is formal, deliberative, and self-enforcing.",
    "explain": "Ansell & Gash's canonical definition and their 161-case meta-analysis showed collaboration emerges from starting conditions (power/resources, incentives, interdependence), facilitative leadership, and institutional design, via face-to-face dialogue, trust, and commitment. Emerson et al. extend it into a dynamic integrative framework (collaborative governance regime ↔ collaborative dynamics ↔ actions/outcomes). The default theory for PPPs, watershed councils, and crisis governance.",
    "founders": "Chris Ansell & Alison Gash — 'Collaborative Governance in Theory and Practice' (2008, JPART); Kirk Emerson, Tina Nabatchi & Stephen Balogh — 'An Integrative Framework for Collaborative Governance' (2012, PAR).",
    "classics": [
      "Ansell, C., & Gash, A. (2008). 'Collaborative Governance in Theory and Practice,' Journal of Public Administration Research and Theory",
      "Emerson, K., Nabatchi, T., & Balogh, S. (2012). 'An Integrative Framework for Collaborative Governance,' Public Administration Review",
      "Milward, H. B., & Provan, K. G. (2000). 'Governing the Hollow State,' Journal of Public Administration Research and Theory",
    ],
    "frontier": [
      "Newig, J., & Fritsch, O. (2009). 'Environmental Governance and Participatory Effectiveness: Can Civic Participation Foster Environmental Policy Outputs?,' Policy Studies Journal — cross-case empirical test of collaboration outcomes.",
      "Ansell & Gash (2018) 'Collaborative Platforms as a Governance Strategy,' JPART — platform model now tested empirically in policy domains from climate to health.",
    ],
  },

  "Coproduction & Co-creation ★": {
    "use": "Public services are jointly produced by professionals and citizens; involving users as active partners raises quantity and quality of outcomes.",
    "explain": "From Ostrom's production functions (citizen inputs are often necessary complements to professional labor) to today's co-creation: engagement can range from individual-level coproduction (parenting education alongside schooling) to collective community-level production. Explains why services fail when users are passive, and grounds participatory design, peer support, and community resilience programs.",
    "founders": "Elinor Ostrom et al., 'The Public Service Production Process' (1978, Policy Studies Journal); Gordon P. Whitaker — 'Coproduction: Citizen Participation in Service Delivery' (1980, PAR); the Indiana Ostrom Workshop.",
    "classics": [
      "Whitaker, G. P. (1980). 'Coproduction: Citizen Participation in Service Delivery,' Public Administration Review",
      "Parks, R. B., et al. (1981). 'Consumers as Coproducers of Public Services,' Journal of Public Administration Research and Theory",
      "Ostrom, E. (1996). 'Crossing the Great Divide: Coproduction, Synergy, and Development,' World Development",
    ],
    "frontier": [
      "Siciliano, M. D. (2016). 'Coproduction and Street-Level Bureaucracy: Does Participation in Coproduction Help to Build Citizen Trust?,' Journal of Public Administration Research and Theory — field-experimental evidence.",
      "Bovaird & Loeffler (co-creation in public services) stream and recent Public Management Review empirical studies on when coproduction improves service outcomes versus excluding harder-to-reach users.",
    ],
  },

  "Collaborative Public Management": {
    "use": "Managing across organizational boundaries — through structures, processes, and boundary-spanning leadership — to produce public value no single agency can.",
    "explain": "Agranoff & McGuire distinguish managing IN networks (hierarchies), managing THROUGH networks (networks as tools), and managing WITHIN networks (being a member); effective collaborative public management requires activating, framing, mobilizing, and synthesizing. Thomson & Perry decompose collaboration into governance, administration, organizational autonomy, mutuality, and trust/reciprocity — the process measures used in empirical work.",
    "founders": "Robert Agranoff & Michael McGuire — Collaborative Public Management: New Strategies for Local Governments (2003); Ann Marie Thomson & James L. Perry (2006, JPART); Rosemary O'Leary & Lisa Blomgren Bingham (2009).",
    "classics": [
      "Agranoff, R., & McGuire, M. (2003). Collaborative Public Management",
      "Thomson, A. M., & Perry, J. L. (2006). 'Collaboration Processes: Inside the Black Box,' Public Administration Review",
      "O'Leary, R., & Bingham, L. B. (Eds.) (2009). The Collaborative Public Manager",
    ],
    "frontier": [
      "Empirical process-outcome studies of collaborative governance components (trust, joint decision-making) in local service delivery and emergency management, in Public Management Review and Journal of Public Administration Research and Theory.",
    ],
  },
}

# ================= INSTITUTIONS & POLICY PROCESS =================

PROFILES.update({

  "Rational Choice & Public Choice": {
    "use": "Public outcomes — voting, lobbying, budgeting, bureaucracy — can be explained as the aggregate of self-interested, utility-maximizing individual choices.",
    "explain": "Downs' economic theory of democracy (voters rationally ignorant, parties converge to the median) and Olson's logic of collective action (free-riding defeats latent groups without selective incentives) founded a research program applying microeconomics to politics. In PA it grounds public choice theories of bureaucracy (Niskanen, Tullock), rent-seeking, and the design of constitutions — and provides the foil that behavioral PA later corrects.",
    "founders": "Anthony Downs — An Economic Theory of Democracy (1957); James Buchanan & Gordon Tullock — The Calculus of Consent (1962); Mancur Olson — The Logic of Collective Action (1965); William Niskanen (1971).",
    "classics": [
      "Downs, A. (1957). An Economic Theory of Democracy",
      "Olson, M. (1965). The Logic of Collective Action",
      "Buchanan, J. M., & Tullock, G. (1962). The Calculus of Consent",
    ],
    "frontier": [
      "Experimental and field evidence from behavioral public administration (PSM, pro-social motivation, framing) systematically qualifies the pure self-interest assumption — e.g., Bellè, N. (2013) on PSM and performance in Journal of Public Administration Research and Theory.",
      "Public choice explanations of bureaucratic and regulatory behavior remain a live empirical agenda in Journal of Public Administration Research and Theory and Public Choice.",
    ],
  },

  "Budget-Maximizing Bureaucracy": {
    "use": "Bureaucrats maximize their bureau's budget, not its output — monopoly supply plus discretionary information produces oversized government.",
    "explain": "Niskanen's model: since bureaus face no competitors and sponsors (legislatures) cannot meter output, bureau chiefs extract the maximum budget by offering all-or-nothing output bundles, pushing output beyond its optimal level. It generated the dominant empirical predictions about budget growth — and a literature of critiques (bureau-shaping, slack maximization, output rather than budget goals) that sharpened tests of bureaucratic objective functions.",
    "founders": "William A. Niskanen Jr. — Bureaucracy and Representative Government (1971); tested and qualified in Blais & Dion (Eds.), The Budget-Maximizing Bureaucrat (1991).",
    "classics": [
      "Niskanen, W. A. (1971). Bureaucracy and Representative Government",
      "Blais, A., & Dion, S. (Eds.) (1991). The Budget-Maximizing Bureaucrat: Appraisals and Evidence",
    ],
    "frontier": [
      "Empirical re-examination using disaggregated agency data and quasi-experimental designs — recent work in Public Administration and Journal of Public Administration Research and Theory on what bureau chiefs actually maximize (budget, output, or prestige).",
      "Performance-budgeting experiments in JPAM/Public Administration Review testing whether output-based funding changes bureau behavior as predicted.",
    ],
  },

  "Bureau-Shaping": {
    "use": "Senior officials maximize personal utility — prestige, interesting work, career rewards — by shaping bureaus toward functions they prefer, not necessarily bigger budgets.",
    "explain": "Dunleavy's critique of Niskanen: officials dislike managing large production-line bureaucracies; they prefer small, elite policy cores near political power. Hence reforms like agencification, contracting-out, and 'Next Steps': senior managers shed routine delivery functions to agencies and contractors while keeping core policy work. Explains privatization and agencification from officials' own incentives.",
    "founders": "Patrick Dunleavy — Democracy, Bureaucracy and Public Choice: Economic Explanations in Political Science (1991).",
    "classics": [
      "Dunleavy, P. (1991). Democracy, Bureaucracy and Public Choice",
      "Dunleavy, P. (1985). 'Bureaucrats, Budgets and the Growth of the State: Reconstructing an Instrumental Model,' British Journal of Political Science 15(3) — the precursor article reconstructing bureaucratic objective functions.",
    ],
    "frontier": [
      "Empirical studies of agency design, agencification, and termination — e.g., work on why governments create and abolish executive agencies, in Governance and Journal of Public Administration Research and Theory.",
      "Recent applications of bureau-shaping to explain digital-era reorganizations and the creation of central 'digital' units in Public Administration and Public Management Review.",
    ],
  },

  "Principal–Agent Theory": {
    "use": "Delegation creates information asymmetry; principals control agents through monitoring, incentives, reporting rules, and careful selection — each costly.",
    "explain": "Applied to public administration (politicians→bureaucracy, ministries→agencies, government→contractors), P-A theory identifies adverse selection and moral hazard, and prescribes institutional remedies: oversight, performance contracts, civil-service rules, transparency. Waterman & Meier's famous corrective — multiple, competing principals and agents who are themselves principals — made 'backward mapping' and bureaucratic influence standard parts of the toolkit.",
    "founders": "Kenneth Arrow / Stephen Ross (formal agency theory); Gary Miller (managerial dilemmas); Richard Waterman & Kenneth Meier (1998, JPART); B. Guy Peters & Jon Pierre.",
    "classics": [
      "Waterman, R. W., & Meier, K. J. (1998). 'Principal–Agent Models: An Expansion?,' Public Administration Review",
      "Miller, G. J. (2005). 'The Political Evolution of Principal–Agent Models,' Annual Review of Political Science",
      "Moe, T. M. (1984). 'The New Economics of Organization,' American Journal of Political Science",
    ],
    "frontier": [
      "Empirical studies of political control, civil-service protection, and agency politicization using personnel and performance data, in Journal of Public Administration Research and Theory and Public Administration Review.",
      "P–A analyses of contracting and co-production relationships (citizens as agents), a growing empirical line in Public Administration and Governance.",
    ],
  },

  "Multiple Streams Framework ★": {
    "use": "Policy change happens when problems, policies, and politics streams couple — pushed by policy entrepreneurs through open policy windows.",
    "explain": "Kingdon's Agendas, Alternatives and Public Policies: problems are recognized (indicators, focusing events, feedback), policies float in a 'primeval soup' of ideas, and politics follows predictable national moods and turnover; windows open unpredictably and close fast, so change needs prepared entrepreneurs who couple the streams. Rooted in the Cohen-March-Olsen garbage-can model of organized anarchies; today's most-used framework for agenda-setting studies worldwide.",
    "founders": "John W. Kingdon — Agendas, Alternatives, and Public Policies (1984; 2nd ed. 2003/2011); Michael Cohen, James March & Johan Olsen — 'A Garbage Can Model of Organizational Choice' (1972).",
    "classics": [
      "Kingdon, J. W. (1984). Agendas, Alternatives, and Public Policies",
      "Cohen, M. D., March, J. G., & Olsen, J. P. (1972). 'A Garbage Can Model of Organizational Choice,' Administrative Science Quarterly",
      "Zahariadis, N. (1999). Markets, States, and Public Policy (comparative MSF extension)",
    ],
    "frontier": [
      "Herweg, N., Huß, C., & Zohlnhöfer, R. (2017). 'Straightening the Three Streams: Theorising Extensions of the Multiple Streams Framework,' European Journal of Political Research — clarifying coupling and windows for empirical testing.",
      "Zohlnhöfer, R., Herweg, N., & Huß, C. (2016). Bringing Together Multiple Streams: A Revised Framework and Empirical Application to German Higher Education Policy — and a wave of non-US empirical MSF applications in Governance, Policy Studies Journal, and Comparative Political Studies.",
    ],
  },

  "Advocacy Coalition Framework ★": {
    "use": "Policy subsystems are decade-long contests between advocacy coalitions unified by deep-core and policy beliefs; change comes through policy-oriented learning and external shocks.",
    "explain": "Sabatier & Jenkins-Smith rejected the stages model: actors in a subsystem — agencies, legislators, researchers, journalists — sort into coalitions by shared belief systems (deep core → policy core → secondary aspects), use resources to influence institutions, and change only gradually via learning within the coalition structure or abruptly via perturbations (crises, regime change, public opinion swings). Methodologically, it demands 10+ year analyses and is the leading framework for belief-driven policy conflict.",
    "founders": "Paul A. Sabatier & Hank C. Jenkins-Smith — Policy Change and Learning: An Advocacy Coalition Approach (1993); Sabatier & Weible (Eds.), Theories of the Policy Process (successive editions).",
    "classics": [
      "Sabatier, P. A., & Jenkins-Smith, H. C. (1988). 'An Advocacy Coalition Framework of Policy Change and the Role of Policy-Oriented Learning Therein,' Policy Sciences",
      "Sabatier, P. A., & Weible, C. M. (2007). 'The Advocacy Coalition Framework: Innovations and Clarifications,' in Theories of the Policy Process (2nd ed.)",
      "Jenkins-Smith, H. C., Nohrstedt, D., Weible, C. M., & Sabatier, P. A. (2018). Theories of the Policy Process (4th ed., ACF chapter)",
    ],
    "frontier": [
      "Weible, C. M., Sabatier, P. A., & Jenkins-Smith, H. C. (2011). 'The Narrative Policy Framework: Clear Enough to Be Wrong?,' Journal of Public Administration Research and Theory — launching the empirical narrative-analysis line inside ACF.",
      "Recent comparative empirical tests of coalition learning, belief change, and coalition resources in Policy Sciences, Review of Policy Research, and Governance (2015–2025).",
    ],
  },

  "Punctuated Equilibrium Theory ★": {
    "use": "Policy makes long periods of stability with rare bursts of radical change, produced by institutional friction, bounded rationality, and disproportionate information processing.",
    "explain": "Baumgartner & Jones: institutional structures (venues, committees, jurisdictions) filter signals so most issues stay off the agenda; when attention shifts — after focusing events or reframing — the same friction amplifies change, producing leptokurtic (heavy-tailed) policy distributions. Founded the Policy Agendas Project and gave policy studies measurable signatures of friction: kurtosis and skew in budgeting and attention data.",
    "founders": "Frank R. Baumgartner & Bryan D. Jones — Agendas and Instability in American Politics (1993; 2nd ed. 2009); foundational article 'Agenda Dynamics and Policy Subsystems' (1991, Journal of Politics).",
    "classics": [
      "Baumgartner, F. R., & Jones, B. D. (1993). Agendas and Instability in American Politics",
      "True, J. L., Jones, B. D., & Baumgartner, F. R. (1999). 'Punctuated Equilibrium Theory: Explaining Stability and Change in American Policymaking,' in Sabatier (Ed.), Theories of the Policy Process",
      "Jones, B. D., & Baumgartner, F. R. (2005). The Politics of Attention",
    ],
    "frontier": [
      "Baumgartner, F. R., Foucault, M., & Nuytemans, A. (2008). 'Punctuated Equilibrium in Comparative Perspective,' American Review of Public Administration — testing the signature outside the US.",
      "Breunig, C., Schnatterer, T., & others — cross-country applications of distributional tests of punctuations in Policy Studies Journal and West European Politics; attention-based empirical studies remain a growing comparative agenda.",
    ],
  },

  "Policy Feedback & Path Dependence ★": {
    "use": "Policies are politically consequential: they build constituencies, distribute resources, and shape interpretation — locking in (or unlocking) future policy choices.",
    "explain": "Pierson's 'when effect becomes cause': large-scale policies change the landscape of power — beneficiaries defend them, administrative capacities channel later demands, and experiences reshape mass understandings of government. Positive feedback (increasing returns, switching costs, learning, coordination effects) generates path dependence; critical junctures set trajectories. Makes welfare states, administrative institutions, and reform failure intelligible over decades.",
    "founders": "Paul Pierson — 'When Effect Becomes Cause: Policy Feedback and Political Change' (1993, World Politics); 'Increasing Returns, Path Dependence, and the Study of Politics' (2000, APSR); Theda Skocpol — Protecting Soldiers and Mothers (1992).",
    "classics": [
      "Pierson, P. (1993). 'When Effect Becomes Cause,' World Politics",
      "Pierson, P. (2000). 'Increasing Returns, Path Dependence, and the Study of Politics,' American Political Science Review",
      "Skocpol, T. (1992). Protecting Soldiers and Mothers: The Political Origins of Social Policy in the United States",
    ],
    "frontier": [
      "Mettler, S., & Soss, J. (2004). 'The Consequences of Public Policy for Democratic Citizenship: Bridging Policy Studies and Mass Politics,' Perspectives on Politics — feedback on participation and citizenship.",
      "Moynihan, D. P., & Soss, J. (2014). 'Policy Feedback and the Politics of Administrative Reform,' Journal of Public Administration Research and Theory — how administrative experience feeds back into legitimacy; empirical burden-and-participation studies continue in JPART and PAR.",
    ],
  },

  "Institutional Analysis & Development ★": {
    "use": "Collective action over common-pool resources succeeds when user communities devise and self-enforce rules-in-use — monitored, graduated-sanction, locally-legitimate rules.",
    "explain": "Ostrom's IAD framework dissects the 'action situation' (positions, actions, information, outcomes, control) nested in operational, collective-choice, and constitutional rule tiers; from hundreds of cases she distilled design principles (clear boundaries, congruence, collective-choice arrangements, monitoring, graduated sanctions, conflict-resolution, minimal recognition of rights, nested enterprises). It shifts governance research from market-vs-state to a polycentric understanding of many autonomous centers of rule-making.",
    "founders": "Elinor Ostrom — Governing the Commons (1990, Nobel Prize 2009); Ostrom, Gardner & Walker — Rules, Games, and Common-Pool Resources (1994); Vincent Ostrom (polycentricity).",
    "classics": [
      "Ostrom, E. (1990). Governing the Commons: The Evolution of Institutions for Collective Action",
      "Ostrom, E., Gardner, R., & Walker, J. (1994). Rules, Games, and Common-Pool Resources",
      "Ostrom, E. (2005). Understanding Institutional Diversity",
    ],
    "frontier": [
      "Cox, M., Arnold, G., & Tomás, S. V. (2010). 'A Review of Design Principles for Community-Based Natural Resource Management,' Ecology and Society — systematic re-validation of the design principles.",
      "Lab-in-the-field and framed-field experiments on rule compliance and monitoring in public goods and CPR settings, feeding policy design work in PNAS, Governance, and Journal of Institutional Economics.",
    ],
  },

  "Policy Diffusion": {
    "use": "Governments adopt policies partly because other governments adopted them — via learning, imitation, competition, and coercion.",
    "explain": "Event-history analyses of state lotteries, taxes, and innovations showed adoption timing is interdependent: Berry & Berry modeled internal determinants plus regional and national diffusion. Berry & Berry (1990) remains the template; later work disentangles mechanisms (Boehmke & Witmer; Makse & Volden on policy attributes like complexity and cost) and criticizes identification. The backbone of federalism, policy transfer, and global governance-spread research.",
    "founders": "Frances Stokes Berry & William D. Berry — 'State Lottery Adoptions as Policy Innovations' (1990, AJPS); Jack Walker — 'The Diffusion of Innovations among the American States' (1969, APSR); Virginia Gray (1973).",
    "classics": [
      "Berry, F. S., & Berry, W. D. (1990). 'State Lottery Adoptions as Policy Innovations,' American Journal of Political Science",
      "Walker, J. L. (1969). 'The Diffusion of Innovations among the American States,' American Political Science Review",
      "Shipan, C. R., & Volden, C. (2008). 'The Mechanisms of Policy Diffusion,' American Journal of Political Science",
    ],
    "frontier": [
      "Boehmke, F. J., & Witmer, R. (2004). 'Disentangling Diffusion: The Effects of Social Learning and Economic Competition on State Policy Innovation and Expansion,' Political Research Quarterly.",
      "Makse, T., & Volden, C. (2011). 'The Role of Policy Attributes in the Diffusion of Innovations,' Journal of Politics — how policy characteristics drive learning versus imitation; international diffusion studies now extend this in Governance and Journal of Public Policy.",
    ],
  },

  "Historical Institutionalism": {
    "use": "Institutions structure conflict over time; the timing and sequence of events — critical junctures and path dependence — explain why similar countries end up with different states.",
    "explain": "Steinmo, Thelen & Longstreth's Structuring Politics institutionalized the approach: institutions distribute power, shape strategies and identities, and produce self-reinforcing sequences. Mahoney & Thelen distinguish gradual institutional change types (layering, displacement, drift, conversion) — directly applicable to administrative reform. In PA, HI explains welfare-state administration, civil-service development, and why reforms land differently on different institutional legacies.",
    "founders": "Sven Steinmo, Kathleen Thelen & Frank Longstreth (Eds.), Structuring Politics: Historical Institutionalism in Comparative Analysis (1992); Paul Pierson — Politics in Time (2004).",
    "classics": [
      "Steinmo, S., Thelen, K., & Longstreth, F. (Eds.) (1992). Structuring Politics",
      "Pierson, P. (2004). Politics in Time: History, Institutions, and Social Analysis",
      "Mahoney, J., & Thelen, K. (2010). Explaining Institutional Change: Ambiguity, Agency, and Power",
    ],
    "frontier": [
      "Empirical applications of layering/drift/conversion to administrative reform, agencification, and welfare-state implementation in Governance, Comparative Political Studies, and Public Administration.",
      "Historical-institutionalist studies of state capacity development — increasingly informing PA debates on administrative state-building.",
    ],
  },

  "Sociological Institutionalism": {
    "use": "Institutions are not just rules but culturally embedded scripts and categories: they constitute actors' identities and define what counts as legitimate, rational action.",
    "explain": "March & Olsen's rediscovery of institutions emphasized rules, routines, symbols, and myths; DiMaggio & Powell showed organizations become more similar (isomorphic) through coercive (rules), mimetic (uncertainty), and normative (professions) pressures — explaining the global spread of similar administrative forms (performance measurement, agencies, ISO-style routines) regardless of efficiency.",
    "founders": "James G. March & Johan P. Olsen — 'The New Institutionalism: Organizational Factors in Political Life' (1984, APSR) and Rediscovering Institutions (1989); DiMaggio & Powell (1983, ASR).",
    "classics": [
      "March, J. G., & Olsen, J. P. (1984). 'The New Institutionalism,' American Political Science Review",
      "March, J. G., & Olsen, J. P. (1989). Rediscovering Institutions: The Organizational Basis of Politics",
      "DiMaggio, P. J., & Powell, W. W. (1983). 'The Iron Cage Revisited,' American Sociological Review",
    ],
    "frontier": [
      "Empirical studies of isomorphic adoption in public administration — e.g., worldwide diffusion of performance measurement, transparency laws, and agency models — in Public Administration Review, Governance, and Public Management Review.",
      "Institutional logics research on hybrid public organizations (welfare offices, hospitals, universities) in Public Administration and Administration & Society.",
    ],
  },

  "Discursive Institutionalism": {
    "use": "Ideas and discourse are institutions' content and constructs: change occurs when actors' background ideational abilities and foreground discursive abilities shift.",
    "explain": "Schmidt's fourth new institutionalism: institutions are both structures (contexts of action) and constructs (internalized scripts); 'coordinate' discourse among policy actors and 'communicative' discourse between elites and the public transmit ideas — programs, philosophies, paradigms — enabling change even within seemingly rigid institutions. Bridges PA with policy narratives, framing, and deliberation research.",
    "founders": "Vivien A. Schmidt — 'Discursive Institutionalism: The Explanatory Power of Ideas and Discourse' (2008, Annual Review of Political Science); 'Taking Ideas and Discourse Seriously' (2010); Maarten Hajer — The Politics of Environmental Discourse (1995).",
    "classics": [
      "Schmidt, V. A. (2008). 'Discursive Institutionalism,' Annual Review of Political Science",
      "Schmidt, V. A., & Radaelli, C. M. (2004). 'Policy Change and Discourse in Europe,' West European Politics",
      "Hajer, M. A. (1995). The Politics of Environmental Discourse",
    ],
    "frontier": [
      "Shanahan, E. A., Jones, M. D., & McBeth, M. K. (2011). 'How to Conduct a Narrative Policy Framework Study,' The Social Science Journal — the operational guide for the framework's empirical wave.",
      "Narrative-policy-framework experiments and discourse-network analyses (Leifeld) applied to PA reform debates, in Policy Studies Journal and Journal of Public Administration Research and Theory.",
    ],
  },
})

# ================= DEMOCRACY, BEHAVIOR & VALUES =================

PROFILES.update({

  "Representative Democracy & Legitimacy": {
    "use": "Administrative power is legitimate only when anchored in law, expertise, and democratic authorization — the enduring constitutional problem of the administrative state.",
    "explain": "From Wilson's politics-administration dichotomy to Waldo's challenge: bureaucracy inevitably involves discretion and therefore politics. The Friedrich–Finer debate (administrative responsibility through internal professional standards vs. external political control) frames today's empirical work on how citizens actually grant legitimacy to agencies — legal-rational authority, expertise, fairness, and participation all matter conditionally.",
    "founders": "Woodrow Wilson (1887); Dwight Waldo — The Administrative State (1948); Carl Friedrich (1940) vs. Herman Finer (1941) debate; Max Weber (authority types).",
    "classics": [
      "Waldo, D. (1948). The Administrative State: A Study of the Political Theory of American Public Administration",
      "Friedrich, C. J. (1940). 'Public Policy and the Nature of Administrative Responsibility,' in Friedrich & Mason (Eds.), Public Policy",
      "Finer, H. (1941). 'Administrative Responsibility in Democratic Government,' Public Administration Review",
    ],
    "frontier": [
      "Experimental studies of administrative legitimacy — how legal mandate, expertise, and procedural fairness drive citizens' acceptance of bureaucratic decisions — in Public Administration Review, Regulation & Governance, and Journal of Public Administration Research and Theory.",
      "Empirical research on legitimacy beliefs toward regulatory and welfare agencies amid populist distrust (2020s agenda in PAR and Governance).",
    ],
  },

  "Deliberative Democracy & Mini-Publics": {
    "use": "Decisions are legitimate insofar as they result from reasoned deliberation among free and equal citizens; institutions like citizens' assemblies can institutionalize this.",
    "explain": "Habermas' communicative rationality and Rawlsian public reason ground a tradition distinguishing deliberative from aggregative democracy: preferences should be formed through exchange of reasons under conditions of inclusion and equality. Empirically, mini-publics (citizens' assemblies, deliberative polls) show ordinary citizens can master complex policy trade-offs; PA research tests when deliberation improves legitimacy, knowledge, and policy quality in real governance.",
    "founders": "Jürgen Habermas — Theory of Communicative Action (1981), Between Facts and Norms (1996); John Rawls (1971); James Fishkin — Democracy and Deliberation (1991); John Dryzek — Deliberative Democracy and Beyond (2000).",
    "classics": [
      "Habermas, J. (1996). Between Facts and Norms: Contributions to a Discourse Theory of Law and Democracy",
      "Fishkin, J. S. (1991). Democracy and Deliberation: New Directions for Democratic Reform",
      "Dryzek, J. S. (2000). Deliberative Democracy and Beyond: Liberals, Critics, Contestations",
    ],
    "frontier": [
      "Caluwaerts, D., & Reuchamps, M. (2016). 'Strengthening Democracy through Bottom-Up Deliberation: Belgian G1000,' Acta Politica — systematic evaluation of a national mini-public.",
      "OECD (2020) 'Innovative Citizen Participation and New Democratic Institutions' inventory and post-2020 empirical evaluations of climate assemblies and permanent deliberative bodies in Governance and Public Administration Review.",
    ],
  },

  "Accountability Theory": {
    "use": "Accountability is a social relationship in which an actor must explain and justify conduct to a forum that can question, judge, and sanction; multiple, conflicting accountability regimes are the norm in public life.",
    "explain": "Romzek & Dubnick's Challenger analysis: public administrators simultaneously answer to legal, bureaucratic, political, and professional accountability regimes, and tragedies often follow wrong expectations about which regime applies. Bovens adds the forum-agent structure and five conceptual questions (who, for what, to whom, why, how). Empirical work maps accountability forums (auditors, courts, parliaments, media, citizens) and studies their real effects on behavior.",
    "founders": "Barbara Romzek & Melvin Dubnick — 'Accountability in the Public Sector: Lessons from the Challenger Tragedy' (1987, Public Administration Review); Mark Bovens (2007); Patricia Day & Rudolf Klein (1987).",
    "classics": [
      "Romzek, B. S., & Dubnick, M. J. (1987). 'Accountability in the Public Sector: Lessons from the Challenger Tragedy,' Public Administration Review",
      "Bovens, M. (2007). 'Analysing and Assessing Accountability: A Conceptual Framework,' European Journal of Political Research",
      "Romzek, B. S. (1998). 'Where the Buck Stops: Accountability as a Form of Control,' in Ferlie et al. (Eds.), The Oxford Handbook of Public Management (later ed.)",
    ],
    "frontier": [
      "Schillemans, T. (2013) and successors on 'social accountability' — reputational and public accountability in the digital age — in Public Administration and Public Management Review.",
      "Empirical studies of accountability effects: performance audits, blame games, and accountability-forcing events in Public Administration Review, Governance, and Administration & Society.",
    ],
  },

  "Transparency & Open Government": {
    "use": "Making government visible improves accountability, trust, and self-regulation — but full transparency can also fuel blame avoidance, gaming, and decision paralysis.",
    "explain": "From Hood & Heald's normative volume to Meijer's interactional model: transparency is not a product government delivers but a dynamic relationship between information provision and its use by citizens, media, and watchdogs. Empirics complicate the gospel: transparency raises perceived trustworthiness only when information is useful and intelligible; it can also induce risk-averse administration and strategic communication ('transparency illusions').",
    "founders": "Christopher Hood & David Heald (Eds.), Transparency: The Key to Better Governance? (2006); Albert Meijer — 'Understanding the Complex Dynamics of Transparency' (2013, PAR).",
    "classics": [
      "Hood, C., & Heald, D. (Eds.) (2006). Transparency: The Key to Better Governance?",
      "Meijer, A. J. (2013). 'Understanding the Complex Dynamics of Transparency,' Public Administration Review",
      "Birkinshaw, P. (2006). 'Freedom of Information and Openness: Fundamental Human Rights?,' Administrative Law Review",
    ],
    "frontier": [
      "Grimmelikhuijsen, S., & Meijer, A. (2014). 'Effects of Transparency on the Perceived Trustworthiness of a Government Organization: Evidence from Two Online Experiments,' Public Administration — the causal evidence base on transparency-trust.",
      "de Fine Licht, K. (2014). 'Transparency Actually: Why Does Increased Transparency Tend to Decrease Legitimacy?,' Public Administration — and the ensuing experimental literature on active and passive transparency in JPART and PAR.",
    ],
  },

  "Public Service Motivation ★": {
    "use": "People are attracted to and energized by public service because of an intrinsic motivation to serve the public interest — and this matters for performance, selection, and job design.",
    "explain": "Rainey's finding that public managers value work that helps others differently from private managers, formalized by Perry & Wise: PSM comprises attraction to policy-making, commitment to the public interest, compassion, and self-sacrifice. Theory: person-environment fit raises performance and lowers turnover; crowding theory warns that extrinsic incentives can displace it. The single most productive construct in behavioral PA, now with validated scales and cross-national measurement.",
    "founders": "Hal G. Rainey (1982, PAR); James L. Perry & Lois Recascino Wise (1990, Review of Public Personnel Administration); Perry (1996, JPART measurement).",
    "classics": [
      "Perry, J. L., & Wise, L. R. (1990). 'The Motivational Bases of Public Service,' Public Administration Review",
      "Perry, J. L. (1996). 'Measuring Public Service Motivation: An Assessment of Construct Reliability and Validity,' Journal of Public Administration Research and Theory",
      "Perry, J. L., & Hondeghem, A. (Eds.) (2008). Motivation in Public Management",
    ],
    "frontier": [
      "Kim, S., Vandenabeele, W., Wright, B. E., Andersen, L. B., Cerase, F. P., Christensen, R. K., et al. (2013). 'Investigating the Structure and Meaning of Public Service Motivation across Populations,' Journal of Public Administration Research and Theory — cross-national validation.",
      "Bellè, N. (2013). 'Experimental Evidence on the Relationship between Public Service Motivation and Job Performance,' Public Administration Review — causal field evidence on PSM and performance; recent meta-analyses and crowding-out experiments continue in Public Administration Review and Human Resource Management Review.",
    ],
  },

  "Behavioral Public Administration ★": {
    "use": "Combine psychological theory and experimental methods with PA questions — how citizens perceive, judge, and respond to government, and how officials actually decide.",
    "explain": "Grimmelikhuijsen & Tummers named the field: a two-way street in which PA supplies realistic contexts and psychology supplies theory and rigorous identification (lab, survey, and field experiments). Core topics: trust in government, transparency processing, fairness perceptions, nudges in services, PSM and pro-social behavior, stereotypes of bureaucrats. It has made experimentation a mainstream PA method and connected the field to behavioral economics.",
    "founders": "Stephan Grimmelikhuijsen & Lars Tummers — 'Behavioral Public Administration: Combining Insights from Public Administration and Psychology' (2017, PAR); earlier foundations in Perry & Wise, Tyler, and nudge work by Thaler & Sunstein (2008).",
    "classics": [
      "Grimmelikhuijsen, S., & Tummers, L. (2017). 'Behavioral Public Administration: Combining Insights from Public Administration and Psychology,' Public Administration Review",
      "Thaler, R. H., & Sunstein, C. R. (2008). Nudge: Improving Decisions about Health, Wealth, and Happiness",
      "Battaglio, R. P., Jr., et al. (2019). 'Behavioral Public Administration: A Map of the Field,' Public Administration (special issue framing)",
    ],
    "frontier": [
      "Bellè, N., Cantarelli, P., & Belardinelli, N. (2018). 'Prosocial Behavior and Public Service Motivation: A Field Experiment,' Public Administration Review — priming prosocial identity in a hospital setting.",
      "Jilke, S., Van Dooren, W., & Rys, S. (Eds.) (2018). Behavioral Public Administration: Connecting Psychology with Governance — and the ongoing experimental wave on administrative burden reduction ('sludge audits') in JPAM, PAR, and Behavioural Public Policy.",
    ],
  },

  "Procedural Fairness & Trust": {
    "use": "People comply and cooperate when they experience procedures as fair and authorities as trustworthy — regardless of whether outcomes favor them.",
    "explain": "Tyler's procedural justice research overturned outcome-based accounts of compliance: legitimacy — the internalized obligation to obey — follows from fair treatment, neutral, consistent procedures and trustworthy motives. Lind & Tyler's group-value model adds that fair procedures signal respect and standing. Applied across policing, taxation, courts, and regulation, it is the behavioral engine of voluntary compliance and police-legitimacy reform.",
    "founders": "Tom R. Tyler — Why People Obey the Law (1990; 2006 Princeton ed.); Allan Lind & Tom Tyler — The Social Psychology of Procedural Justice (1988); E. Allan Lind.",
    "classics": [
      "Tyler, T. R. (1990). Why People Obey the Law",
      "Lind, E. A., & Tyler, T. R. (1988). The Social Psychology of Procedural Justice",
      "Tyler, T. R. (2006). Why People Obey the Law (2nd ed., Princeton)",
    ],
    "frontier": [
      "Mazerolle, L., Antrobus, E., Bennett, S., & Tyler, T. R. (2013). 'Shaping Citizen Perceptions of Police Legitimacy: A Randomized Field Trial of Procedural Justice,' Criminology — among the largest procedural-justice policing experiments.",
      "Procedural-justice applications to tax compliance, administrative courts, and frontline encounters — an active empirical line in Regulation & Governance, Journal of Public Administration Research and Theory, and Public Administration Review.",
    ],
  },

  "Citizen Satisfaction & Expectations": {
    "use": "Citizen satisfaction with services is shaped not only by performance but by expectations and their confirmation — the psychological metric of public management.",
    "explain": "Van Ryzin transplanted the expectancy-disconfirmation model to public services: satisfaction = f(perceived performance, expectations, disconfirmation), explaining why objectively similar services yield different satisfaction and why satisfaction with government exceeds performance levels. Distinguishing satisfaction as consumer experience from trust as political attitude clarified measurement in ACSI-style indices and anchored empirical public management.",
    "founders": "Gregg G. Van Ryzin — 'The Measurement of Overall Citizen Satisfaction' (2004, PAR) and 'Testing the Expectancy Disconfirmation Model of Citizen Satisfaction' (2006, JPAM); Richard L. Oliver (1980) for the consumer model; Oliver James (2009).",
    "classics": [
      "Van Ryzin, G. G. (2004). 'The Measurement of Overall Citizen Satisfaction,' Public Administration Review",
      "Van Ryzin, G. G. (2006). 'Testing the Expectancy Disconfirmation Model of Citizen Satisfaction with Local Government,' Journal of Public Administration Research and Theory",
      "Van Ryzin, G. G., & Immerwahr, S. (2007). 'Importance–Performance Analysis of Citizen Satisfaction Surveys,' Public Administration Review",
    ],
    "frontier": [
      "Empirical extensions to digital services and co-production: how online service quality and participation shape satisfaction and trust — recent studies in Government Information Quarterly, Public Management Review, and Public Administration Review.",
      "Work linking citizen satisfaction to trust in government as distinct constructs (Van Ryzin stream) continues with panel and experimental designs.",
    ],
  },

  "Social Equity ★": {
    "use": "Public administration has an affirmative obligation to promote fairness and justice for protected and marginalized groups — alongside efficiency and economy.",
    "explain": "Frederickson's Minnowbrook challenge made equity PA's 'third pillar' (with economy and efficiency): administrators hold a direct responsibility for social equity, not merely neutral competence. Today's operational agenda includes representative bureaucracy, equitable service allocation, and the equity turn in administrative burden research — who pays the learning, psychological, and compliance costs of interacting with the state.",
    "founders": "H. George Frederickson — 'Toward a New Public Administration' (1968, in Marini (Ed.), Toward a New Public Administration); Frederickson (2010) Social Equity and Public Administration (2nd ed.); Norma M. Riccucci & Susan T. Gooden.",
    "classics": [
      "Frederickson, H. G. (1971). 'Toward a New Public Administration,' in F. Marini (Ed.), Toward a New Public Administration: The Minnowbrook Perspective",
      "Frederickson, H. G. (2010). Social Equity and Public Administration: Origins, Developments, and Applications (2nd ed.)",
      "Gooden, S. T. (2015). Race and Social Equity: A Nervous Area of Government",
    ],
    "frontier": [
      "Nisar, M. A. (2018). 'Children of a Lesser God: Administrative Burden and Social Equity in Citizen-State Interactions,' Journal of Public Administration Research and Theory 28(1) — who bears the burden, and why equity requires its measurement.",
      "Moynihan, D., Herd, P., & Harvey, H. (2015). 'Administrative Burden: Learning, Psychological, and Compliance Costs in Citizen-State Interactions,' Journal of Public Administration Research and Theory 25(1) — the cost typology behind the current equity-driven empirical agenda.",
      "Herd, P., & Moynihan, D. P. (2018). Administrative Burden: Policymaking by Other Means — with a growing empirical equity literature in Public Administration Review, JPART, and Perspectives on Public Management and Policy on racialized burdens in benefits take-up.",
    ],
  },

  "Public Sector Ethics": {
    "use": "Public office entails role-based moral obligations — responsible discretion, integrity, and stewardship — beyond legal minimums and personal morality.",
    "explain": "From Waldo's question 'who should rule the rulers?' through Rohr's regime-value ethics and Cooper's responsible administrator model: ethical PA balances objective responsibility (accountability structures) with subjective responsibility (internalized moral agency). Thompson's paradox — administrative decisions are morally divisible yet bureaucracies demand personal integrity — frames today's empirical work on ethical climate, corruption, whistleblowing, and integrity systems.",
    "founders": "Dwight Waldo (1948); John A. Rohr — Ethics for Bureaucrats: An Essay on Law and Values (1978); Terry L. Cooper — The Responsible Administrator (1990; 6th ed. 2012); Dennis F. Thompson (1985, PAR).",
    "classics": [
      "Rohr, J. A. (1978). Ethics for Bureaucrats: An Essay on Law and Values",
      "Cooper, T. L. (2012). The Responsible Administrator: An Approach to Ethics for the Administrative Role (6th ed.)",
      "Thompson, D. F. (1985). 'The Possibility of Administrative Ethics,' Public Administration Review",
    ],
    "frontier": [
      "Empirical studies of public integrity systems and ethical climate — Huberts' integrity-of-governance assessments and national integrity-system comparisons in Public Integrity and Public Administration Review.",
      "Whistleblowing, unethical pro-organizational behavior, and AI ethics in government: recent field and survey studies in Public Administration Review, Public Administration, and the Journal of Public Administration Research and Theory.",
    ],
  },

  "Public Trust in Government": {
    "use": "Citizens' diffuse trust in government rests on evaluations of competence, benevolence, and integrity of both political institutions and administrative encounters.",
    "explain": "Easton's distinction between diffuse support and specific support structures the field: trust is a reservoir built by fair, competent performance across everyday administrative encounters — policing, benefits, schools — not just macro-politics. Administration scholars therefore test how service quality, procedural fairness, transparency, and burden shape trust, treating the administrative state as a daily producer (or destroyer) of political trust.",
    "founders": "David Easton — A Systems Analysis of Political Life (1965); William Gamson — Power and Disillusionment (1968); B. Guy Peters & Jon Pierre on administrative trust; Bouckaert & Van de Walle (2003, PAR).",
    "classics": [
      "Easton, D. (1965). A Systems Analysis of Political Life",
      "Gamson, W. A. (1968). Power and Disillusionment",
      "Bouckaert, G., & Van de Walle, S. (2003). 'Comparing Measures of Citizen Trust and User Satisfaction as Indicators of Good Governance,' Public Administration Review",
    ],
    "frontier": [
      "Van Ryzin, G. G. (2011). 'Outcomes, Process, and Trust of Civil Servants,' Journal of Public Administration Research and Theory — trust follows fair process more than favorable outcomes.",
      "Christensen, T., & Lægreid, P. (2005). 'Trust in Government: The Relative Importance of Service Satisfaction, Political Factors, and Demography,' Public Performance & Management Review — and current experimental work on trust repair, transparency, and digitalization in Public Administration Review, Governance, and West European Politics.",
    ],
  },
})
