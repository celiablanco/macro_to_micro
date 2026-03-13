"""
Generate the revised main paper PDF with changes highlighted in red.
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import red, black
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Image,
                                 Table, TableStyle, PageBreak, KeepTogether)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors

FIGDIR = os.path.join(os.path.dirname(__file__), 'figures')
OUTPATH = os.path.join(os.path.dirname(__file__), 'revised_paper.pdf')

doc = SimpleDocTemplate(OUTPATH, pagesize=letter,
                        topMargin=0.8*inch, bottomMargin=0.8*inch,
                        leftMargin=1*inch, rightMargin=1*inch)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle('Title2', parent=styles['Title'], fontSize=16,
                              leading=20, spaceAfter=12, alignment=TA_CENTER)
heading_style = ParagraphStyle('Heading2', parent=styles['Heading1'], fontSize=14,
                                leading=18, spaceBefore=18, spaceAfter=8)
subheading_style = ParagraphStyle('SubHeading', parent=styles['Heading2'], fontSize=12,
                                   leading=15, spaceBefore=12, spaceAfter=6)
body_style = ParagraphStyle('Body2', parent=styles['Normal'], fontSize=10,
                             leading=14, spaceAfter=6, alignment=TA_JUSTIFY)
caption_style = ParagraphStyle('Caption', parent=styles['Normal'], fontSize=9,
                                leading=12, spaceAfter=6, alignment=TA_JUSTIFY)
ref_style = ParagraphStyle('Ref', parent=styles['Normal'], fontSize=9,
                            leading=12, spaceAfter=3, leftIndent=24, firstLineIndent=-24)
abstract_style = ParagraphStyle('Abstract', parent=body_style, fontSize=10,
                                 leading=14, leftIndent=18, rightIndent=18)
table_style_rlab = ParagraphStyle('TableCell', parent=styles['Normal'], fontSize=8,
                                   leading=10)

def R(text):
    """Wrap text in red font to indicate changes."""
    return f'<font color="red">{text}</font>'

def B(text):
    return f'<b>{text}</b>'

def I(text):
    return f'<i>{text}</i>'

def BI(text):
    return f'<b><i>{text}</i></b>'

story = []

# ═══════════════════════════════════════════════════════════════════════════════
# TITLE PAGE
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Context Without Contact: Top-Down Information Flow from Shared Modulation in Uncoupled Prebiotic Systems", title_style))
story.append(Spacer(1, 24))

story.append(Paragraph(B("Abstract"), body_style))
story.append(Spacer(1, 6))
# Abstract - unchanged parts + modified parts
abstract_text = (
    "Shifts from bottom-up to top-down influences are considered a hallmark of major evolutionary "
    "transitions, including the origin of life. We explore how such directional information flow can "
    "arise without direct interactions among the system components using a minimal model of uncoupled "
    "logistic maps subject to a shared, time-varying constraint. Transfer entropy (TE) reveals a "
    "consistent macro-to-micro bias across diverse modulation profiles, along with increased inter-unit "
    "predictability and confinement of macroscopic dynamics to low-dimensional manifolds. "
    + R("Conditional transfer entropy (CTE) analysis, in which the environmental signal is conditioned out, "
        "reveals a two-component structure: while the shared environment mediates a large fraction of "
        "the asymmetry, a genuine residual information flow from the mean field to individuals persists, "
        "peaking at intermediate modulation amplitudes. This residual demonstrates that nonlinear "
        "aggregation of uncoupled chaotic units generates emergent top-down predictive structure "
        "beyond common-driver effects. ")
    + "These results show that structured environmental variation alone is sufficient to generate an "
    "asymmetric "
    + R("directional ")
    + "information flow "
    + R("signature")
    + ", suggesting that dynamic external constraints may serve as an early scaffold for coordination "
    "before the evolution of internal coupling mechanisms."
)
story.append(Paragraph(abstract_text, abstract_style))
story.append(Spacer(1, 12))

story.append(Paragraph(f"{B('Word count:')} {R('~4,200')} words, excluding references.", body_style))
story.append(Paragraph(f"{B('Keywords:')} origins of life, emergence, astrobiology, top-down causation{R(', transfer entropy, conditional transfer entropy')}", body_style))
story.append(Paragraph(f"{B('Ethical Compliance:')} This article does not present research with ethical considerations", body_style))
story.append(Paragraph(f"{B('Conflict of Interest declaration:')} The authors declare that they have no affiliations with or involvement in any organization or entity with any financial interest in the subject matter or materials discussed in this Manuscript.", body_style))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# INTRODUCTION (expanded per MAJOR-1)
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Introduction", heading_style))

# Para 1 - original intro (slightly modified for terminology)
story.append(Paragraph(
    "Top-down causation, in which higher-level organization shapes the dynamics of lower-level "
    "components, occurs at all scales of biological organization and helps explain the hierarchy of "
    "structures in living systems (1\u20133). Indeed, it has been proposed that shifts from predominantly "
    "bottom-up to predominantly top-down influences are hallmarks of major evolutionary transitions "
    "(4,5), including the emergence of life (6\u20138). In this view, higher-level organizations emerge from "
    "previously independent units and informational control arises at the collective level. One way to "
    "study such transitions is by examining the directional information flow between scales, "
    "specifically, whether the macroscopic state of a system can predict the dynamics of its parts "
    "better than the reverse (9).",
    body_style))

# NEW para - MAJOR-1a: Prior work on top-down causation in origin of life
story.append(Paragraph(R(
    "The concept of top-down causation in the context of the origin of life and major evolutionary "
    "transitions has received considerable theoretical attention. Walker and Davies (8) argued that "
    "the transition from non-life to life is fundamentally an informational transition, in which "
    "top-down causal structure becomes a defining feature of living systems. Ellis (6) provided a "
    "taxonomy of top-down causation mechanisms, distinguishing algorithmic, non-adaptive, and "
    "adaptive forms, and argued that downward causation is essential for understanding biological "
    "organization. Szathm\u00e1ry and Smith (4) identified the major evolutionary transitions as events "
    "in which formerly independent replicating entities become integrated into higher-level units, "
    "a process that implies the emergence of top-down constraints. Szathm\u00e1ry (5) further argued "
    "that the transition framework should be extended to include the informational and regulatory "
    "dimensions of these transitions. Auletta, Ellis, and Jaeger (2) framed top-down causation by "
    "information control as a scientific research programme, providing a philosophical foundation "
    "for empirical investigation. Walker (7) specifically connected the rise of informational "
    "control to the emergence of life, proposing that the origin of life involves a transition from "
    "dynamics governed solely by physical law to dynamics governed by information. These works "
    "collectively establish that top-down causation is a central, though still debated, concept in "
    "understanding how higher-level organization arises during evolutionary transitions. The present "
    "study contributes to this programme by asking whether the informational signatures of "
    "top-down influence can arise even in the absence of internal coupling, driven solely by "
    "shared environmental constraints."
), body_style))

# Para 2 - original question paragraph
story.append(Paragraph(
    "This perspective motivates a key question particularly relevant for early chemical evolution: can "
    "asymmetric directional information flow between levels arise even in the absence of direct "
    "coupling among low-level components, driven solely by a shared environmental structure? "
    "Structured external cycles (such as tides, day\u2013night rhythms, or wet\u2013dry fluctuations) are "
    "known to promote essential prebiotic processes (10\u201312), but could such global patterns have "
    "also imposed system-wide constraints capable of coordinating dynamics across otherwise "
    "independent units?",
    body_style))

# NEW para - MAJOR-1b: Logistic maps in computational biology
story.append(Paragraph(R(
    "To investigate this question, we employ logistic maps as our model system. The logistic map, "
    "introduced by May (30) as a minimal model of population dynamics, has become a paradigmatic "
    "tool in nonlinear dynamics and computational biology. Despite its simplicity, it captures the "
    "essential features of density-dependent growth, including period-doubling cascades and "
    "deterministic chaos (31). More broadly, the synchronization of chaotic systems under common "
    "external forcing is a well-characterized phenomenon in nonlinear dynamics (36); even without "
    "mutual coupling, a shared driving signal can entrain individually chaotic units into coherent "
    "collective behavior. Coupled logistic maps have been widely used to study synchronization, "
    "collective behavior, and information flow in spatially extended systems (14,32). In the context "
    "of prebiotic chemistry, such minimal models are valuable because they isolate the dynamical "
    "consequences of environmental forcing from the biochemical complexity of real systems, "
    "allowing the identification of generic mechanisms that do not depend on molecular detail (33)."
), body_style))

# Para 3 - TE paragraph (expanded per MAJOR-1c)
story.append(Paragraph(
    "To probe this, we use a deliberately minimal model in which a population of uncoupled logistic "
    "maps is subject to a single time-varying global constraint, implemented as a sinusoidal "
    "modulation of the carrying capacity. We then investigated whether such purely environmental "
    "structuring could produce measurable macro-to-micro predictive bias. We computed Transfer "
    "Entropy (TE) (13) to quantify directional information flow. TE measures how much knowledge "
    "of the past of one variable improves predictions about the future of another, beyond what "
    "the variable's own past can explain.",
    body_style))

# NEW para - MAJOR-1c: Information-theoretic measures in this domain
story.append(Paragraph(R(
    "Transfer entropy, introduced by Schreiber (13), has become a standard tool for detecting "
    "directed information flow in complex systems. It has been applied extensively in neuroscience "
    "to map effective connectivity between brain regions (20,34), in climate science to identify "
    "causal interactions between climatic variables (22,24), and in ecology to characterize "
    "predator-prey and species interaction networks (35). In the context of multi-scale biological "
    "systems, TE has been used to quantify information flow between levels of organization, "
    "including the detection of top-down informational influence in coupled map lattices (9,14). "
    "A key limitation of standard TE is its sensitivity to common-driver confounds: when two "
    "variables share a common input, TE may detect apparent information transfer that is entirely "
    "attributable to the shared source (20\u201322). Conditional transfer entropy (CTE), which "
    "conditions out known confounding variables, provides a principled correction for this issue "
    "(23,24). We employ both unconditional and conditional TE in our analysis to distinguish "
    "genuine mean-field-driven information flow from environmentally scaffolded coordination."
), body_style))

# Original closing paragraph of intro (modified)
story.append(Paragraph(
    "While the interpretation of informational asymmetry as literal causation remains debated, "
    "here we treat it as an operational signal or a measurable statistical signature that may "
    "accompany early forms of coordinated behavior, regardless of whether an underlying causal "
    "mechanism is in place. This framework has been used to operationalize top-down informational "
    "influence in a system where units are explicitly coupled (9); however, here, the focus is on "
    "the limiting case with no internal coupling, isolating environmental structure as a potential "
    "driver of coordination in prebiotic contexts.",
    body_style))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# MODEL AND METHODS (new section per MAJOR-2)
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph(R("Model"), heading_style))

story.append(Paragraph(
    "We consider a minimal system of " + I("N") + " uncoupled logistic maps, each evolving under a "
    "shared time-dependent carrying capacity, " + I("K") + "<sub>n</sub>. Let " + I("x") +
    "<sub>i,n</sub> denote the state of unit " + I("i") + ", where " + I("i") +
    " = {1... " + I("N") + "}, at discrete time step " + I("n") + ". Each unit follows:",
    body_style))

story.append(Paragraph(
    "<i>x</i><sub>i,n+1</sub> = <i>r</i><sub>i</sub> <i>x</i><sub>i,n</sub> "
    "(1 \u2212 <i>x</i><sub>i,n</sub> / <i>K</i><sub>n</sub>),",
    ParagraphStyle('Eq', parent=body_style, alignment=TA_CENTER, spaceBefore=6, spaceAfter=6)))

story.append(Paragraph(
    "where <i>r</i><sub>i</sub> \u2208 [<i>r</i><sub>min</sub>, <i>r</i><sub>max</sub>] is sampled "
    "independently from a uniform distribution to ensure that, in the absence of modulation, each "
    "unit operates in a chaotic regime (9,14). There are no interactions among the units; the only "
    "shared influence is the global carrying capacity <i>K</i><sub>n</sub>, which is modulated "
    "sinusoidally as <i>K</i><sub>n</sub> = <i>K</i><sub>0</sub> + <i>A</i> sin(\u03c9 <i>n</i>). "
    "This modulation represents synchronized environmental rhythms (e.g., day\u2013night cycles, "
    "tides, or wet\u2013dry transitions) that affect the entire population. The macroscopic variable "
    "is defined as the " + R("mean field") + ": "
    "<i>M</i><sub>n</sub> = (1/<i>N</i>) \u2211<sub>i=1..N</sub> <i>x</i><sub>i,n</sub>.",
    body_style))

story.append(Paragraph(
    "While abstract, the model components can be loosely interpreted in prebiotic terms: the global "
    "constraint <i>K</i><sub>n</sub> represents an externally imposed limit on the system carrying "
    "capacity (e.g., availability of resources, space, or favorable conditions), the intrinsic "
    "parameters <i>r</i><sub>i</sub> reflect heterogeneity in how individual entities respond to that "
    "environment, and the " + R("mean field") + " <i>M</i><sub>n</sub> captures an aggregate property "
    "of the population, such as an overall reaction yield or bulk chemical state.",
    body_style))

# MAJOR-2b: Parameter justification table
story.append(Paragraph(R("Parameter choices"), subheading_style))

story.append(Paragraph(R(
    "Table 1 summarizes all model and analysis parameters together with their justifications. "
    "The growth rate interval [3.9, 4.0] ensures that all units operate deep within the chaotic "
    "regime of the logistic map (31), guaranteeing sensitive dependence on initial conditions and "
    "preventing periodic orbits that would trivially synchronize. The baseline carrying capacity "
    "K<sub>0</sub> = 100 is a conventional scaling choice; because the logistic map dynamics depend "
    "on the ratio x/K rather than absolute values, results are invariant to this scale. "
    "The modulation amplitude A is swept from 0 to 60 to explore the full range from no modulation "
    "to strong modulation (A/K<sub>0</sub> up to 0.6). The angular frequency \u03c9 = 2\u03c0/2000 "
    "was chosen to provide approximately 4.5 full modulation cycles within the analysis window, "
    "balancing statistical power with temporal resolution; robustness to \u03c9 is demonstrated in "
    "the inset of Figure 1B. The population size N = 1000 ensures that the mean field is a "
    "well-averaged macroscopic quantity (\u221aN averaging reduces idiosyncratic noise by a factor "
    "of ~31.6). The total simulation length T = 10,000 with the first 1,000 steps discarded as "
    "transients provides T<sub>eff</sub> = 9,000 time points for analysis, sufficient for reliable "
    "histogram-based TE estimation."
), body_style))

# Parameter table
table_data = [
    [Paragraph(R(B('Parameter')), table_style_rlab),
     Paragraph(R(B('Value')), table_style_rlab),
     Paragraph(R(B('Rationale')), table_style_rlab)],
    [Paragraph(R('<i>r</i><sub>min</sub>, <i>r</i><sub>max</sub>'), table_style_rlab),
     Paragraph(R('3.9, 4.0'), table_style_rlab),
     Paragraph(R('Deep chaotic regime; avoids periodic windows (9,14,31)'), table_style_rlab)],
    [Paragraph(R('<i>K</i><sub>0</sub>'), table_style_rlab),
     Paragraph(R('100'), table_style_rlab),
     Paragraph(R('Conventional scale; results invariant to rescaling'), table_style_rlab)],
    [Paragraph(R('<i>A</i>'), table_style_rlab),
     Paragraph(R('0\u201360'), table_style_rlab),
     Paragraph(R('Swept; covers A/K<sub>0</sub> = 0 to 0.6'), table_style_rlab)],
    [Paragraph(R('\u03c9'), table_style_rlab),
     Paragraph(R('2\u03c0/2000'), table_style_rlab),
     Paragraph(R('~4.5 cycles in analysis window; robustness shown in Fig. 1B inset'), table_style_rlab)],
    [Paragraph(R('<i>N</i>'), table_style_rlab),
     Paragraph(R('1000'), table_style_rlab),
     Paragraph(R('Large enough for well-averaged mean field (\u221aN \u2248 31.6)'), table_style_rlab)],
    [Paragraph(R('<i>T</i>'), table_style_rlab),
     Paragraph(R('10,000'), table_style_rlab),
     Paragraph(R('Sufficient length for TE estimation; first 1,000 discarded'), table_style_rlab)],
    [Paragraph(R('Bins'), table_style_rlab),
     Paragraph(R('15'), table_style_rlab),
     Paragraph(R('Standard for histogram-based TE; balances bias and variance (13)'), table_style_rlab)],
    [Paragraph(R('Lag <i>k</i>'), table_style_rlab),
     Paragraph(R('2'), table_style_rlab),
     Paragraph(R('Avoids near-synchronous inflation at k=1; see Fig. S1'), table_style_rlab)],
    [Paragraph(R('Surrogates'), table_style_rlab),
     Paragraph(R('100'), table_style_rlab),
     Paragraph(R('Circular-shift method; sufficient for p &lt; 0.01 threshold'), table_style_rlab)],
]

t = Table(table_data, colWidths=[1.1*inch, 0.8*inch, 3.6*inch])
t.setStyle(TableStyle([
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('BACKGROUND', (0,0), (-1,0), colors.Color(0.9, 0.9, 0.9)),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
]))
story.append(Spacer(1, 6))
story.append(t)
story.append(Paragraph(R(B("Table 1.") + " Summary of model and analysis parameters with justifications."), caption_style))
story.append(Spacer(1, 6))

# ── Information-theoretic measures (formulas stay with Model) ──
story.append(Paragraph(R("Information-theoretic measures"), subheading_style))

story.append(Paragraph(
    "To assess whether shared modulation produces directional relationships between macro- and "
    "micro-level dynamics, we computed the transfer entropy (TE) in both directions: top-down "
    "(from " + R("mean field") + " to representative unit, <i>M</i> \u2192 <i>x</i>) and bottom-up "
    "(from representative unit to " + R("mean field") + ", <i>x</i> \u2192 <i>M</i>). Formally:",
    body_style))

story.append(Paragraph(
    "<i>T</i><sub>Y\u2192X</sub> = \u2211 <i>p</i>(<i>x</i><sub>n+1</sub>, "
    "<i>x</i><sub>n</sub><sup>(k)</sup>, <i>y</i><sub>n</sub><sup>(k)</sup>) "
    "log<sub>2</sub> [ <i>p</i>(<i>x</i><sub>n+1</sub> | <i>x</i><sub>n</sub><sup>(k)</sup>, "
    "<i>y</i><sub>n</sub><sup>(k)</sup>) / <i>p</i>(<i>x</i><sub>n+1</sub> | "
    "<i>x</i><sub>n</sub><sup>(k)</sup>) ]",
    ParagraphStyle('Eq', parent=body_style, alignment=TA_CENTER, spaceBefore=6, spaceAfter=6)))

story.append(Paragraph(
    "where <i>x</i><sub>n</sub><sup>(k)</sup> and <i>y</i><sub>n</sub><sup>(k)</sup> are the "
    "histories of length <i>k</i> for the target and source variables, respectively.",
    body_style))

story.append(Paragraph(R(
    "To disentangle environmental forcing from genuine mean-field-driven information flow, "
    "we also computed the conditional transfer entropy (CTE), conditioning on "
    "the environmental signal K<sub>n</sub>:"
), body_style))

story.append(Paragraph(R(
    "CTE<sub>Y\u2192X|Z</sub> = \u2211 p(x<sub>n+1</sub>, x<sub>n</sub><sup>(k)</sup>, "
    "y<sub>n</sub><sup>(k)</sup>, z<sub>n</sub><sup>(k)</sup>) "
    "log<sub>2</sub> [ p(x<sub>n+1</sub> | x<sub>n</sub><sup>(k)</sup>, y<sub>n</sub><sup>(k)</sup>, "
    "z<sub>n</sub><sup>(k)</sup>) / p(x<sub>n+1</sub> | x<sub>n</sub><sup>(k)</sup>, "
    "z<sub>n</sub><sup>(k)</sup>) ]"
), ParagraphStyle('Eq', parent=body_style, alignment=TA_CENTER, spaceBefore=6, spaceAfter=6)))

story.append(Paragraph(R(
    "where z<sub>n</sub><sup>(k)</sup> is the history of the conditioning variable K<sub>n</sub>. "
    "CTE measures the information that the source provides about the target beyond what is already "
    "explained by both the target's own past and the conditioning variable's past. If the TE "
    "asymmetry is entirely due to the common environmental driver, CTE should be approximately "
    "zero in both directions."
), body_style))

story.append(Paragraph(R(
    "We also quantified the statistical alignment between the mean field M<sub>n</sub> and a "
    "representative unit x<sub>1,n</sub> using two regression-based metrics: the coefficient "
    "of determination R\u00b2 = 1 \u2212 SS<sub>res</sub>/SS<sub>tot</sub> and the "
    "signal-to-noise ratio SNR = Var(M<sub>n</sub>) / Var(\u03b5), "
    "where \u03b5 denotes the residuals from the linear regression of x<sub>1,n</sub> "
    "on M<sub>n</sub>."
), body_style))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# METHODS (standalone section — technical implementation details only)
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph(R("Methods"), heading_style))

story.append(Paragraph(R(
    "All information-theoretic quantities (TE and CTE) were estimated using a histogram-based "
    "(plug-in) method. Each time series was discretized into 15 equally spaced bins, with bin "
    "edges determined from the pooled range of the past and future target values. The embedding "
    "lag was set to k = 2 to reduce near-synchronous correlations that can inflate TE at k = 1; "
    "Supplementary Figure S1 shows the sensitivity to this choice. Results were averaged over 10 "
    "independent random seeds, each drawing growth rates r<sub>i</sub> ~ Uniform[3.9, 4.0]. "
    "Confidence intervals (95%) were computed via the Student\u2019s t-distribution."
), body_style))

story.append(Paragraph(R(
    "Statistical significance of inter-unit TE was assessed using a circular-shift surrogate "
    "method (16): the source series was shifted by a random offset (minimum 10 steps) to preserve "
    "autocorrelation while destroying temporal alignment. For each pair, 100 surrogates were "
    "generated, and significance was assessed at the p &lt; 0.01 level."
), body_style))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# RESULTS
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Results", heading_style))

story.append(Paragraph(R("Unconditional transfer entropy reveals macro-to-micro asymmetry"), subheading_style))

story.append(Paragraph(
    "The time-varying <i>K</i><sub>n</sub> imposes a common oscillatory envelope on all "
    "trajectories <i>x</i>, introducing a coherent pattern that shapes the "
    + R("mean field") + " <i>M</i> (Figure 1A).",
    body_style))

story.append(Paragraph(
    "TE analysis revealed clear directional asymmetry (Figure 1B). Without modulation "
    "(<i>A</i> \u2248 0), TE is negligible in both directions, which is consistent with "
    "unstructured dynamics. As <i>A</i> increases, the TE from the "
    + R("mean field") + " to the individuals (<i>M</i> \u2192 <i>x</i>) increases steadily, "
    "whereas the reverse (<i>x</i> \u2192 <i>M</i>) remains negligible. This indicates that "
    "shared modulation generates top-down informational influences without reciprocal predictability. "
    + R("Intuitively, the mean field is a low-dimensional projection that retains only the shared "
        "environmental signal, whereas each unit carries both that signal and idiosyncratic noise "
        "from its intrinsic growth rate. As the signal fraction grows with A, the predictive "
        "information flowing from M to x increases while the reverse direction remains negligible."),
    body_style))

# MAJOR-3c: Explain Figure 1B features
story.append(Paragraph(R(
    "The monotonic increase of TE(M \u2192 x) with A reflects the progressive dominance of the "
    "shared environmental signal over idiosyncratic chaotic fluctuations. At low A, each unit's "
    "trajectory is dominated by its intrinsic chaotic dynamics (governed by r<sub>i</sub>), and "
    "the mean field contains little predictive information about any single unit. As A increases, "
    "the common modulation of K<sub>n</sub> forces all units through a similar range of carrying "
    "capacities, aligning their trajectories and making the mean field increasingly informative "
    "about individual dynamics. The sharp rise in the confidence interval near A \u2248 50 "
    "corresponds to a regime transition related to the ratio A/K<sub>0</sub>: when A approaches "
    "K<sub>0</sub>/2 = 50, the minimum carrying capacity K<sub>min</sub> = K<sub>0</sub> \u2212 A "
    "approaches 50, at which point the effective nonlinearity of the logistic equation changes "
    "qualitatively. In this regime, some seeds produce populations near the edge of the clipping "
    "boundary (0, 2K<sub>0</sub>), introducing seed-dependent variability in the TE estimates "
    "and widening the confidence interval."
), body_style))

# MINOR-4: mention omega inset
story.append(Paragraph(R(
    "The inset of Figure 1B shows the dependence of TE(M \u2192 x) on the modulation frequency "
    "\u03c9 at fixed A = 25. TE remains high for slow modulation (long periods) and decreases "
    "for fast modulation (short periods), consistent with the expectation that very rapid "
    "oscillations average out and fail to impose coherent structure on the chaotic dynamics."
), body_style))

# Insert Figure 1
story.append(Spacer(1, 6))
fig1a_path = os.path.join(FIGDIR, 'fig1a.png')
fig1b_path = os.path.join(FIGDIR, 'fig1b.png')
if os.path.exists(fig1a_path):
    story.append(Image(fig1a_path, width=3.2*inch, height=2.1*inch))
if os.path.exists(fig1b_path):
    story.append(Image(fig1b_path, width=3.4*inch, height=2.3*inch))
story.append(Paragraph(
    B("Figure 1. Modulation-driven asymmetry and entrainment under sinusoidal forcing. ")
    + "(A) Time series of a population of N = 1000 uncoupled logistic units evolving under "
    "sinusoidal carrying capacity (K<sub>0</sub> = 100, A = 25, r<sub>i</sub> \u2208 [3.9, 4.0]). "
    "The black dashed curve shows the external modulation K<sub>n</sub>, the orange line the "
    + R("mean field") + " M sampled every 200 steps, and the shaded band the range of individual "
    "states at each sample. (B) Transfer entropy (TE) between the " + R("mean field") +
    " M<sub>n</sub> and a representative unit x<sub>i,n</sub>, computed in both directions: "
    "M \u2192 x (blue) and x \u2192 M (gray), across modulation amplitudes A. The dashed line "
    "shows the logistic fit to TE(M \u2192 x). "
    + R("Inset: TE(M \u2192 x) as a function of modulation period 2\u03c0/\u03c9 at A = 25. ")
    + "Results are averaged over 10 seeds. Shaded regions show 95% confidence intervals.",
    caption_style))

story.append(Spacer(1, 6))

# Plateau discussion
story.append(Paragraph(
    "At high modulation amplitudes, TE (M\u2192x) approaches a plateau (Figure 1B), well captured "
    "by a logistic fit as TE<sub>M\u2192x</sub>(A) = T<sub>max</sub>/(1 + exp(\u2212\u03b1(A \u2212 "
    "A<sub>0</sub>))), with R\u00b2=0.983. This plateau reflects the natural ceiling set by the "
    "extent to which a unit's dynamics can be explained by a shared environmental signal. At low "
    "amplitudes, idiosyncratic fluctuations from differences in the intrinsic growth rates "
    "(<i>r</i><sub>i</sub>) dominate; therefore, the " + R("mean field") + " has little "
    "predictive power. As the amplitude increases, the common modulation progressively shapes all "
    "trajectories, making the " + R("mean field") + " a stronger predictor of individual behavior. "
    "However, once the environmental signal overwhelms individual variability, no further "
    "information can be gained, and the predictive relationship has reached the limit imposed by "
    "the variance in the environmental drive itself.",
    body_style))

# Figures 2A and 2B
story.append(Paragraph(
    "This is consistent with the observation that, in the high-amplitude regime, the fraction of "
    "variance in individual trajectories explained by the " + R("mean field") + " approaches unity "
    "(R\u00b2 ~1; Figure 2A). In other words, stronger modulation eventually adds no new structure "
    "and rescales only the same signal. The same saturation trend is reflected in the "
    "regression-based measures of alignment (Figure 2B), where both the fraction of variance "
    "explained and the signal-to-noise ratio (SNR) increase with amplitude before leveling off.",
    body_style))

story.append(Paragraph(
    "We obtained the same qualitative asymmetry when replacing the sinusoidal forcing with a "
    "logistic one (representing gradual favorable environmental shift) and with an inverse logistic "
    "(representing gradual environmental decline) (Supplementary Figure S2), indicating that the "
    "effect is robust to the shape of the modulation.",
    body_style))

# MINOR-5: Clarify soft-bound statement
story.append(Paragraph(
    "The saturation was not due to numerical clipping. "
    + R("A soft bound of (0, 2K<sub>0</sub>) = (0, 200) was imposed on all unit states at each "
        "time step to prevent unphysical negative concentrations and runaway growth. At the highest "
        "modulation amplitude tested (A = 60), the lower bound (x \u2264 0) was approached in fewer "
        "than 10% of unit-timestep pairs across all seeds, and the upper bound (x \u2265 200) was "
        "never reached. Clipping therefore cannot account for the TE saturation, which instead "
        "reflects the information-theoretic ceiling described above."),
    body_style))

# Insert Figures 2A and 2B
story.append(Spacer(1, 6))
fig2a_path = os.path.join(FIGDIR, 'fig2a.png')
fig2b_path = os.path.join(FIGDIR, 'fig2b.png')
if os.path.exists(fig2a_path):
    story.append(Image(fig2a_path, width=3.2*inch, height=2.1*inch))
if os.path.exists(fig2b_path):
    story.append(Image(fig2b_path, width=3.6*inch, height=2*inch))
story.append(Paragraph(
    B("Figure 2. Alignment with " + R("mean field") + " and modulation signal under increasing amplitude. ")
    + "(A) Fraction of variance in the " + R("mean field") + " (blue) and in a representative "
    "unit's trajectory (orange) explained directly by the modulation signal K<sub>n</sub>, as a "
    "function of A. (B) Relationship between modulation amplitude A and statistical alignment "
    "between the " + R("mean field") + " M<sub>n</sub> and a representative unit x<sub>1,n</sub>. "
    + R("R\u00b2 = 1 \u2212 SS<sub>res</sub>/SS<sub>tot</sub> (teal); "
        "SNR = Var(M<sub>n</sub>)/Var(residuals) (magenta)."),
    caption_style))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# CTE RESULTS (new section per MAJOR-3a)
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph(R("Conditional transfer entropy: disentangling environmental forcing"), subheading_style))

story.append(Paragraph(R(
    "The unconditional TE asymmetry demonstrated above could, in principle, arise entirely from "
    "the shared environmental signal K<sub>n</sub> acting as a common driver. To test this, we "
    "computed the conditional transfer entropy (CTE) in both directions, conditioning on "
    "K<sub>n</sub> (Figure " + R("4") + "). The CTE measures the residual information flow between "
    "the mean field and an individual unit after the contribution of the environmental signal has "
    "been removed."
), body_style))

story.append(Paragraph(R(
    "The results reveal a two-component structure in the macro-to-micro information flow. "
    "First, CTE(M \u2192 x | K<sub>n</sub>) remains non-zero across all modulation amplitudes, "
    "peaking at intermediate A (\u2248 0.36 bits near A \u2248 15). This residual represents "
    "genuine predictive information that the mean field carries about individual dynamics "
    "beyond what is explained by the environmental signal alone. Because the mean field is a "
    "nonlinear aggregate of all unit states, it encodes statistical structure \u2014 arising from "
    "the interplay of heterogeneous growth rates and shared modulation \u2014 that cannot be "
    "reduced to the common driver. Second, comparing unconditional and conditional TE at "
    "high amplitude (A = 60) shows that the environmental component accounts for approximately "
    "91% of the total TE, confirming that shared forcing is the dominant contributor in the "
    "strong-modulation regime. Together, these results demonstrate that the TE asymmetry has "
    "two distinct sources: environmentally scaffolded coordination and genuine emergent "
    "information flow from nonlinear aggregation."
), body_style))

# Insert CTE figure
story.append(Spacer(1, 6))
fig_cte_path = os.path.join(FIGDIR, 'fig_cte.png')
if os.path.exists(fig_cte_path):
    story.append(Image(fig_cte_path, width=3.6*inch, height=2.4*inch))
story.append(Paragraph(R(
    B("Figure 4. Conditional transfer entropy analysis. ")
    + "Unconditional TE (solid lines) and conditional TE (dashed lines, conditioning on "
    "K<sub>n</sub>) in both directions: M \u2192 x (blue/red) and x \u2192 M (gray/orange). "
    "CTE(M \u2192 x | K<sub>n</sub>) drops to ~9% of the unconditional TE at high A, indicating "
    "that the asymmetry is predominantly driven by the shared environmental signal. "
    "Parameters: N = 1000, K<sub>0</sub> = 100, r<sub>i</sub> \u2208 [3.9, 4.0], 10 seeds."
), caption_style))

story.append(Spacer(1, 6))

# MAJOR-3b: A/K0 ratio sweep
story.append(Paragraph(R("Role of the A/K<sub>0</sub> ratio"), subheading_style))

story.append(Paragraph(R(
    "The ratio A/K<sub>0</sub> determines the relative strength of environmental modulation and "
    "governs the transition between dynamical regimes. When A/K<sub>0</sub> is small, the logistic "
    "equation retains its full quadratic nonlinearity: the term x<sub>i,n</sub>/K<sub>n</sub> varies "
    "only slightly, and individual chaotic trajectories dominate. As A/K<sub>0</sub> increases, "
    "the modulation increasingly constrains the effective range of K<sub>n</sub>, and when "
    "K<sub>n</sub> becomes large relative to x<sub>i,n</sub>, the quadratic term "
    "x<sub>i,n</sub>/K<sub>n</sub> \u2192 0, driving the dynamics toward a near-linear regime "
    "where units effectively evolve as x<sub>i,n+1</sub> \u2248 r<sub>i</sub> x<sub>i,n</sub>. "
    "In this linear limit, all units scale proportionally with K<sub>n</sub>, trivially increasing "
    "their alignment with the mean field."
), body_style))

story.append(Paragraph(R(
    "Figure 5 confirms that TE(M \u2192 x) collapses onto a single curve when plotted against "
    "A/K<sub>0</sub> for different values of K<sub>0</sub>, demonstrating that this ratio is the "
    "natural control parameter for the strength of environmentally induced coordination. "
    "The TE onset occurs near A/K<sub>0</sub> \u2248 0.05\u20130.1 and saturates around "
    "A/K<sub>0</sub> \u2248 0.3\u20130.4."
), body_style))

# Insert A/K0 figure
fig_ratio_path = os.path.join(FIGDIR, 'fig_ak0_ratio.png')
if os.path.exists(fig_ratio_path):
    story.append(Image(fig_ratio_path, width=3.6*inch, height=2.4*inch))
story.append(Paragraph(R(
    B("Figure 5. TE(M \u2192 x) as a function of the ratio A/K<sub>0</sub> ")
    + "for K<sub>0</sub> = 50, 100, 200, 400. The collapse onto approximately the same curve "
    "confirms that A/K<sub>0</sub> is the natural control parameter. N = 1000, 5 seeds."
), caption_style))

story.append(Spacer(1, 6))

# Inter-unit predictability (Figure 3)
story.append(Paragraph(R("Inter-unit predictability"), subheading_style))

story.append(Paragraph(
    "The presence of directional information flow between the " + R("mean field") +
    " and individuals raises a further question: can shared modulation generate consistent "
    "directional relationships between individuals? Even without interactions, a common drive "
    "may induce dependencies across the ensemble. We tested this by comparing the transfer "
    "entropy (TE) from a reference unit to 50 other units against a null distribution generated "
    "from a circularly shifted surrogate series that preserves autocorrelation while destroying "
    "temporal alignment (16) (Figure 3). Significance was defined as a real TE exceeding the "
    "95th percentile of the surrogate distribution, using 100 surrogates per target. With no "
    "modulation (A=0), no units exceeded the significance threshold, which is consistent with "
    "the absence of temporal coordination. Under moderate modulation (A=25), however, 39 out "
    "of 50 units were significant, demonstrating that shared modulation alone induces emergent "
    "inter-unit predictability.",
    body_style))

# Insert Figure 3
story.append(Spacer(1, 6))
fig3_path = os.path.join(FIGDIR, 'fig3.png')
if os.path.exists(fig3_path):
    story.append(Image(fig3_path, width=3.8*inch, height=2.2*inch))
story.append(Paragraph(
    B("Figure 3. ") + "Transfer entropy (TE) from reference unit x<sub>0</sub> to each target "
    "unit x<sub>j</sub> for two modulation amplitudes (A = 0, A = 25). Real TE values (symbols) "
    "are compared to the distribution from 100 circularly shifted surrogates (shaded bands). "
    "Solid symbols mark significant cases (p &lt; 0.05); open symbols are non-significant. "
    "Results shown for N = 1000, K<sub>0</sub> = 100, r<sub>i</sub> \u2208 [3.9, 4.0], "
    "T = 10,000 steps (first 1,000 discarded).",
    caption_style))

story.append(Paragraph(
    "Finally, we assessed how modulation shapes macroscopic dynamics by examining the return maps "
    "of the " + R("mean field") + ". Increasing the modulation amplitude broadens the range of "
    "accessible states but maintains trajectories in a coordinated, low-dimensional pattern, "
    "indicating that the shared environmental structure expands the dynamical range without "
    "disrupting collective organization (Figure S3).",
    body_style))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# DISCUSSION (updated with CTE reframing)
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Discussion", heading_style))

story.append(Paragraph(
    "Origins-of-life theories often assume that coordination arises from internal chemical "
    "coupling among components (e.g., autocatalytic sets (17), hypercycles (18), and early "
    "metabolism (19)). These frameworks share the premise that organizations depend on direct "
    "chemical interactions; however, they do not always provide satisfactory explanations for "
    "the non-trivial question of how such coupling originates in the first place. Here, we "
    "explore a simpler scenario in which structured organizations can emerge without direct "
    "interactions, driven solely by shared environmental structures.",
    body_style))

story.append(Paragraph(
    "Our model isolates this idea in its simplest possible form, as a population of uncoupled "
    "logistic maps exposed to the same time-varying constraint. Global modulation, implemented "
    "through sinusoidal changes in the carrying capacity, introduces a temporal structure without "
    "inducing direct interactions between components. We then used transfer entropy (TE) as an "
    "operational measure of top-down informational influence to quantify this asymmetry, a "
    "framework previously applied to systems with explicit coupling (9). In this context, TE "
    "is not intended to imply mechanistic causation, but to test whether shared environmental "
    "modulation alone can induce directional predictability between scales.",
    body_style))

# Reframed CTE discussion
story.append(Paragraph(R(
    "Our conditional transfer entropy (CTE) analysis reveals that the observed TE asymmetry "
    "has a two-component structure. At high modulation amplitude (A = 60), the environmental "
    "signal accounts for approximately 91% of the unconditional TE, confirming that shared "
    "forcing is the dominant contributor. Crucially, however, a genuine residual persists: "
    "CTE(M \u2192 x | K<sub>n</sub>) remains non-zero across all amplitudes and peaks at "
    "intermediate A (~0.36 bits), demonstrating that the mean field carries predictive "
    "information about individual dynamics that is not attributable to the shared environment. "
    "This residual arises because the mean field is a nonlinear aggregate of heterogeneous "
    "chaotic units; it encodes collective statistical structure that the linear environmental "
    "signal cannot capture. The CTE analysis thus addresses the distinction between "
    "common-driver forcing and genuine top-down information flow raised in the literature "
    "(20\u201324) by showing that both mechanisms contribute to the observed asymmetry."
), body_style))

story.append(Paragraph(R(
    "The genuine residual CTE demonstrates that even without direct coupling, the nonlinear "
    "aggregation of individually chaotic units into a mean field creates emergent predictive "
    "structure \u2014 information about individual dynamics that cannot be attributed to the "
    "shared environment. This is a non-trivial finding: in a purely linear system, conditioning "
    "on the common driver would eliminate the TE asymmetry entirely, yet the nonlinear dynamics "
    "of the logistic map generate additional statistical dependencies between the collective "
    "and the individual. The environmental scaffolding and the emergent component play "
    "complementary roles in prebiotic scenarios: the shared environment provides the dominant "
    "coordinating force, while the nonlinear collective dynamics produce genuine top-down "
    "predictive structure on top of it. Together, they create a macroscopic variable that "
    "carries information about microscopic dynamics \u2014 a precondition for functional "
    "top-down causation \u2014 even before internal coupling mechanisms have evolved. "
    "The A/K<sub>0</sub> analysis further clarifies that this coordination depends on the "
    "relative strength of the modulation: the ratio A/K<sub>0</sub> serves as a natural "
    "control parameter, with TE onset near A/K<sub>0</sub> \u2248 0.05 and saturation "
    "near A/K<sub>0</sub> \u2248 0.4."
), body_style))

story.append(Paragraph(
    "In the transfer entropy (TE) literature, correlations induced by a shared input are often "
    "classified as \u201ccommon driver effects\u201d (20\u201322) and treated as confounds to be "
    "removed (23,24). "
    + R("Our CTE analysis shows that the TE asymmetry reflects two complementary mechanisms: "
        "environmentally scaffolded coordination (the dominant contributor at high A) and "
        "genuine emergent information flow from nonlinear aggregation (peaking at intermediate A). "
        "In the prebiotic context, neither component should be viewed as a confound. The "
        "environmental component shows that a common driver ") + I("is") + R(" a mechanism "
        "of interest: shared forcing imposes system-wide coordination that could scaffold the "
        "later emergence of internal coupling. The emergent component shows that even without "
        "such coupling, the nonlinear collective dynamics of uncoupled units generate additional "
        "top-down predictive structure \u2014 a form of proto-organization that goes beyond "
        "what the environment alone can impose."),
    body_style))

story.append(Paragraph(R(
    "It is important to distinguish two modes of coordination that are often conflated under the "
    "umbrella of \u2018top-down causation.\u2019 Externally imposed boundary conditions \u2014 such as "
    "the modulated carrying capacity K<sub>n</sub> in our model \u2014 constrain the dynamics of all "
    "units from outside the system. By contrast, internally generated coordination arises from "
    "coupling among the units themselves (e.g., autocatalytic feedback, cross-catalysis, or metabolic "
    "networks). Our model demonstrates that external boundary conditions alone can produce the "
    "informational signatures of top-down influence, including a directional TE asymmetry and "
    "inter-unit predictability. The CTE analysis refines this picture: the environmental component "
    "of the TE reflects the boundary-condition mechanism, while the genuine residual CTE reflects "
    "emergent statistical structure arising from the nonlinear aggregation of heterogeneous units "
    "\u2014 a form of collective information processing that, while not internally coupled, goes "
    "beyond passive entrainment. This distinction clarifies that the \u2018top-down\u2019 signal in "
    "our model is not a claim of autonomous macroscopic agency, but rather a demonstration that "
    "externally structured environments can generate the informational preconditions from which "
    "internally coordinated systems may subsequently emerge."
), body_style))

story.append(Paragraph(
    "Although the model is minimal and abstract in nature, it directly relates to scenarios in "
    "origins-of-life research where prebiotic chemistry is unfolded under rhythmic environmental "
    "forcing. Regular cycles such as wet-dry, freeze-thaw, day-night, and tidal rhythms are "
    "known to concentrate reactants, drive condensation, promote molecular restructuring, "
    "stabilize intermediates, and facilitate protocell assembly (10\u201312,25\u201329). Beyond "
    "enabling specific reactions, such cycles may impose system-wide constraints, thus aligning "
    "otherwise independent chemical processes. We represent these well-studied periodic influences "
    "with sinusoidal forcing, however, the results are not limited to perfect periodicity. "
    "Logistic and inverse-logistic modulation, which represent gradual environmental improvements "
    "or declines, yield comparable qualitative asymmetries. The key factor is not the waveform "
    "itself, but its capacity to impose a coherent structure across the system. In our framework, "
    "modulated carrying capacity serves as a proxy for this type of global context, acting as a "
    "constraint capable of entraining independent components without direct, physical interaction.",
    body_style))

story.append(Paragraph(
    "This broader principle may apply across many of life's major evolutionary transitions, "
    "where collections of simpler units become integrated wholes (in part) due to a shared "
    "environment. Structured environmental conditions could have served as an early coordinating "
    "force prior to the evolution of internal control mechanisms. For example, vesicle populations "
    "may have synchronized division under thermal cycles, early microbial communities may have "
    "differentiated along spatial gradients, and hominins may have aligned behaviors through "
    "shared cues before developing language. While these examples are speculative, they illustrate "
    "how directional information flow can be externally imposed and later internalized by evolving "
    "systems. More generally, the findings highlight how shared external drivers can generate "
    "proto-organization in uncoupled systems, a mechanism that may recur across the physical, "
    "chemical, and biological domains. Our results suggest that such environmentally driven "
    "coordination, even if transient, may provide a scaffold for the emergence of persistent "
    "self-organized complexity. "
    + R("A natural extension of this work would be to test these principles in models that "
        "incorporate concrete aspects of prebiotic biochemistry or biophysics \u2014 for example, "
        "populations of protocells with explicit metabolic kinetics under cyclic environmental "
        "forcing \u2014 to determine whether the informational signatures identified here persist "
        "in more realistic chemical settings."),
    body_style))

# Data availability (MINOR-7: fix GitHub URL)
story.append(Paragraph(R("Data availability"), subheading_style))
story.append(Paragraph(R(
    "All code and data required to reproduce the results are available at: "
    "https://github.com/celia/macro-to-micro"
), body_style))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# REFERENCES (expanded)
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("References", heading_style))

refs = [
    '1. Campbell DT. "downward causation" in hierarchically organised biological systems. In: Studies in the Philosophy of Biology. London: Macmillan Education UK; 1974. p. 179\u201386.',
    '2. Auletta G, Ellis GFR, Jaeger L. Top-down causation by information control: from a philosophical problem to a scientific research programme. J R Soc Interface. 2008;5(27):1159\u201372.',
    '3. Davies PCW. The epigenome and top-down causation. Interface Focus. 2012;2(1):42\u20138.',
    '4. Szathm\u00e1ry E, Smith JM. The major evolutionary transitions. Nature. 1995;374(6519):227\u201332.',
    '5. Szathm\u00e1ry E. Toward major evolutionary transitions theory 2.0. Proc Natl Acad Sci USA. 2015;112(33):10104\u201311.',
    '6. Ellis GFR. Top-down causation and emergence: some comments on mechanisms. Interface Focus. 2012;2(1):126\u201340.',
    '7. Walker S. Top-down causation and the rise of information in the emergence of life. Information. 2014;5(3):424\u201339.',
    '8. Walker SI, Davies PCW. The algorithmic origins of life. J R Soc Interface. 2013;10(79):20120869.',
    '9. Walker SI. Evolutionary transitions and top-down causation. In: Artificial Life 13. MIT Press; 2012.',
    '10. Monnard PA, Szostak JW. Metal-ion catalyzed polymerization in the eutectic phase in water-ice. J Inorg Biochem. 2008;102(5\u20136):1104\u201311.',
    '11. Campbell TD, et al. Prebiotic condensation through wet-dry cycling regulated by deliquescence. Nat Commun. 2019;10(1):4508.',
    '12. Zhang SJ, et al. Freeze-thaw cycles enable a prebiotically plausible and continuous pathway from nucleotide activation to nonenzymatic RNA copying. Proc Natl Acad Sci USA. 2022;119(17):e2116429119.',
    '13. Schreiber T. Measuring information transfer. Phys Rev Lett. 2000;85(2):461\u20134.',
    '14. Cisneros L, et al. Information transfer and nontrivial collective behavior in chaotic coupled map networks. Phys Rev E. 2002;65(4 Pt 2A):045204.',
    '15. Walker SI. Evolutionary transitions and top-down causation. In: Artificial Life 13. MIT Press; 2012.',
    '16. Shorten DP, Spinney RE, Lizier JT. Estimating Transfer Entropy in Continuous Time Between Neural Spike Trains or Other Event-Based Data. PLoS Comput Biol. 2021;17(4):e1008054.',
    '17. Kauffman SA. The origins of order: Self-organization and selection in evolution. Oxford University Press; 1993.',
    '18. Eigen M, Schuster P. The Hypercycle: A Principle of Natural Self-Organization. Springer; 2012.',
    '19. W\u00e4chtersh\u00e4user G. Evolution of the first metabolic cycles. Proc Natl Acad Sci USA. 1990;87(1):200\u20134.',
    '20. Vicente R, et al. Transfer entropy\u2014a model-free measure of effective connectivity for the neurosciences. J Comput Neurosci. 2011;30(1):45\u201367.',
    '21. Lizier JT, Prokopenko M. Differentiating information transfer and causal effect. Eur Phys J B. 2010;73(4):605\u201315.',
    '22. Runge J, Petoukhov V, Kurths J. Quantifying the strength and delay of climatic interactions. J Clim. 2014;27(2):720\u201339.',
    '23. Smirnov DA, Bezruchko BP. Spurious causalities due to low temporal resolution. EPL. 2012;100(1):10005.',
    '24. Runge J. Causal network reconstruction from time series. Chaos. 2018;28(7):075310.',
    '25. Fares HM, et al. Impact of wet-dry cycling on the phase behavior and compartmentalization properties of complex coacervates. Nat Commun. 2020;11(1):5423.',
    '26. Song X, et al. Wet-dry cycles cause nucleic acid monomers to polymerize into long chains. Proc Natl Acad Sci USA. 2024;121(49):e2412784121.',
    '27. Menor-Salv\u00e1n C, Mar\u00edn-Yaseli MR. Prebiotic chemistry in eutectic solutions at the water-ice matrix. Chem Soc Rev. 2012;41(16):5404\u201315.',
    '28. Rimmer PB, et al. Timescales for Prebiotic Photochemistry Under Realistic Surface Ultraviolet Conditions. Astrobiology. 2021;21(9):1099\u2013120.',
    '29. Lathe R. Fast tidal cycling and the origin of life. Icarus. 2004;168(1):18\u201322.',
]

# New references
new_refs = [
    R('30. May RM. Simple mathematical models with very complicated dynamics. Nature. 1976;261(5560):459\u201367.'),
    R('31. Strogatz SH. Nonlinear Dynamics and Chaos. 2nd ed. Westview Press; 2015.'),
    R('32. Kaneko K. Clustering, coding, switching, hierarchical ordering, and control in a network of chaotic elements. Physica D. 1990;41(2):137\u201372.'),
    R('33. Ruiz-Mirazo K, Briones C, de la Escosura A. Prebiotic systems chemistry: new perspectives for the origins of life. Chem Rev. 2014;114(1):285\u2013366.'),
    R('34. Bossomaier T, et al. An Introduction to Transfer Entropy. Springer; 2016.'),
    R('35. Sugihara G, et al. Detecting causality in complex ecosystems. Science. 2012;338(6106):496\u2013500.'),
    R('36. Boccaletti S, Kurths J, Osipov G, Valladares DL, Zhou CS. The synchronization of chaotic systems. Phys Rep. 2002;366(1\u20132):1\u2013101.'),
]

for ref in refs:
    story.append(Paragraph(ref, ref_style))
for ref in new_refs:
    story.append(Paragraph(ref, ref_style))

# Build PDF
doc.build(story)
print(f"Revised paper saved to: {OUTPATH}")
