"""
Generate response.pdf — formal response letter addressing all reviewer comments.
Uses reportlab to produce a PDF with the same content as generate_response_docx.py.
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import black
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

OUTPATH = os.path.join(os.path.dirname(__file__), 'response.pdf')

doc = SimpleDocTemplate(OUTPATH, pagesize=letter,
                        topMargin=2.03*cm, bottomMargin=2.03*cm,
                        leftMargin=2.54*cm, rightMargin=2.54*cm)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle('Title2', parent=styles['Title'],
                              fontName='Times-Roman', fontSize=16,
                              leading=20, spaceAfter=4, alignment=TA_CENTER)
subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'],
                                 fontName='Times-Italic', fontSize=11,
                                 leading=14, spaceAfter=4, alignment=TA_CENTER)
journal_style = ParagraphStyle('Journal', parent=styles['Normal'],
                                fontName='Times-Roman', fontSize=10,
                                leading=14, spaceAfter=18, alignment=TA_CENTER)
body_style = ParagraphStyle('Body2', parent=styles['Normal'],
                             fontName='Times-Roman', fontSize=10,
                             leading=14, spaceAfter=6, alignment=TA_JUSTIFY)
heading1_style = ParagraphStyle('H1', parent=styles['Heading1'],
                                 fontName='Times-Bold', fontSize=14,
                                 leading=18, spaceBefore=18, spaceAfter=8,
                                 textColor=black)
heading2_style = ParagraphStyle('H2', parent=styles['Heading2'],
                                 fontName='Times-Bold', fontSize=12,
                                 leading=15, spaceBefore=12, spaceAfter=6,
                                 textColor=black)
comment_style = ParagraphStyle('Comment', parent=body_style,
                                fontName='Times-Italic', fontSize=10,
                                leading=14, spaceAfter=4,
                                leftIndent=1.0*cm, alignment=TA_JUSTIFY)
response_style = ParagraphStyle('Response', parent=body_style,
                                 fontName='Times-Roman', fontSize=10,
                                 leading=14, spaceAfter=12, alignment=TA_JUSTIFY)


def B(text):
    return f'<b>{text}</b>'

def I(text):
    return f'<i>{text}</i>'

def BI(text):
    return f'<b><i>{text}</i></b>'

def nl2br(text):
    """Convert newlines to <br/> for reportlab Paragraphs."""
    return text.replace('\n', '<br/>')


def add_comment_response(story, comment_text, response_text):
    """Add a reviewer comment (italic, indented) followed by a response."""
    comment_para = f'{BI("Comment: ")}{I(comment_text)}'
    story.append(Paragraph(comment_para, comment_style))

    response_para = f'{B("Response: ")}{nl2br(response_text)}'
    story.append(Paragraph(response_para, response_style))


story = []

# ═════════════════════════════════════════════════════════════════════════════
# HEADER
# ═════════════════════════════════════════════════════════════════════════════

story.append(Paragraph(B("Response to Reviewer Comments"), title_style))
story.append(Paragraph(
    I("Context Without Contact: Top-Down Information Flow from Shared "
      "Modulation in Uncoupled Prebiotic Systems"),
    subtitle_style
))
story.append(Paragraph(
    "Manuscript submitted to Royal Society Open Science",
    journal_style
))

# ── Preamble ─────────────────────────────────────────────────────────────────

story.append(Paragraph(
    "We thank the reviewers for their constructive and insightful comments. "
    "We have carefully addressed every point raised. Below, we respond to "
    "each comment individually and describe the specific changes made. "
    "All modifications to the manuscript are highlighted in red font in the "
    "revised manuscript and supplementary information.",
    body_style
))
story.append(Spacer(1, 6))

# ═════════════════════════════════════════════════════════════════════════════
# REVIEWER 1
# ═════════════════════════════════════════════════════════════════════════════

story.append(Paragraph("Reviewer 1", heading1_style))

# ── Major 1 ──────────────────────────────────────────────────────────────────

story.append(Paragraph("Major Comment 1: Strengthen the Introduction", heading2_style))

add_comment_response(story,
    "The article is structured into three sections: the Introduction provides "
    "background, the Results section outlines the methodology and numerical "
    "experiments, and the Discussion interprets the findings in the context of "
    "the origin of life. I recommend a more thorough treatment of the underlying "
    "themes. In particular, the Introduction would benefit from additional detail "
    "and references to prior work that has considered top-down causation in the "
    "context of the origin of life and evolutionary transitions. Greater attention "
    "should also be given to the role of logistic map models in computational "
    "biology and the application of information-theoretic measures. These additions "
    "would substantially strengthen the Introduction, which in its current form is "
    "insufficient.",

    "We have substantially expanded the Introduction with three new paragraphs:\n\n"
    "(a) Top-down causation in origin of life and evolutionary transitions: "
    "We added a paragraph reviewing prior work on top-down causation in the "
    "context of major evolutionary transitions and the origin of life. This "
    "paragraph now provides the conceptual context for our study, covering the "
    "taxonomy of top-down causation mechanisms (Ellis 2012), the identification "
    "of major evolutionary transitions as events where independent replicating "
    "entities become integrated into higher-level units (Szathm\u00e1ry &amp; Maynard "
    "Smith 1995; Szathm\u00e1ry 2015), top-down causation by information control "
    "(Auletta, Ellis &amp; Jaeger 2008), and the characterization of the origin of "
    "life as a transition from dynamics governed by physical law to dynamics "
    "governed by information (Walker 2014; Walker &amp; Davies 2013).\n\n"
    "(b) Logistic maps in computational biology: We added a paragraph covering "
    "the use of logistic map models in population dynamics and computational "
    "biology, including their role as minimal models exhibiting deterministic "
    "chaos (May 1976; Strogatz 2024). We also acknowledged that synchronization "
    "of chaotic systems under common external forcing is a well-characterized "
    "phenomenon in nonlinear dynamics (Boccaletti et al. 2002), and discussed "
    "the use of coupled logistic maps to study collective behavior and "
    "information flow (Cisneros et al. 2002; Kaneko 1990). The value of such "
    "minimal models for isolating dynamical consequences from biochemical "
    "complexity in prebiotic chemistry is noted (Ruiz-Mirazo et al. 2014).\n\n"
    "(c) Information-theoretic measures: We added a paragraph reviewing the "
    "application of transfer entropy (Schreiber 2000) across fields, including "
    "neuroscience (Vicente et al. 2011; Bossomaier et al. 2016), climate "
    "science (Runge et al. 2014; Runge 2018), and ecology (Sugihara et al. "
    "2012). We explicitly discuss a key limitation of standard TE \u2014 its "
    "sensitivity to common-driver confounds (Lizier &amp; Prokopenko 2010; Runge "
    "et al. 2014) \u2014 and introduce conditional transfer entropy (CTE) as a "
    "principled correction (Runge 2018; Smirnov &amp; Bezruchko 2012), which we "
    "then employ in our analysis."
)

# ── Major 2 ──────────────────────────────────────────────────────────────────

story.append(Paragraph("Major Comment 2: Add a dedicated Methodology section", heading2_style))

add_comment_response(story,
    "I strongly recommend adding a dedicated methodology section that clearly "
    "presents the model and parameter choices, some of which appear arbitrary "
    "(e.g., r_min, r_max, K\u2080, A, \u03c9). This would help demonstrate the "
    "robustness of the argument.",

    "We have reorganized the manuscript and added a dedicated Methods section "
    "(placed after the Discussion). This section now contains:\n\n"
    "(a) Information-theoretic measures: Full formal definitions of both "
    "transfer entropy (TE) and conditional transfer entropy (CTE) are written "
    "out explicitly, including the conditioning on the environmental signal "
    "K\u2099. The interpretation of CTE is stated: if the TE asymmetry were "
    "entirely due to the common environmental driver, CTE should be "
    "approximately zero in both directions.\n\n"
    "(b) Regression-based alignment metrics: We now provide the explicit "
    "formulas for the coefficient of determination R\u00b2 (from a linear "
    "regression of the unit trajectory on the mean field) and the "
    "signal-to-noise ratio SNR (defined as the variance of the mean field "
    "divided by the variance of the regression residuals).\n\n"
    "(c) Model parameters: Each parameter is justified in dedicated prose. "
    "The growth rate interval r \u2208 [3.9, 4.0] ensures all units operate "
    "deep within the chaotic regime. The baseline carrying capacity K\u2080 = "
    "100 is noted to be a scale parameter (dynamics depend on x/K, not "
    "absolute values). The modulation amplitude A was varied from 0 to 60 "
    "(A/K\u2080 up to 0.6). The modulation frequency \u03c9 = 2\u03c0/2000 provides "
    "approximately 4.5 full cycles within the analysis window, with "
    "robustness to \u03c9 demonstrated in Supplementary Figure S1. Population "
    "size N = 1000 and simulation length T = 10,000 steps (first 1,000 "
    "discarded as transients) are also justified.\n\n"
    "(d) Analysis parameters: The histogram-based TE estimation method is "
    "fully documented, including the choice of 15 equally spaced bins, "
    "embedding lag k = 2 (chosen to reduce near-synchronous correlations "
    "that inflate TE at k = 1, with sensitivity shown in Supplementary "
    "Figure S3), conversion to bits, averaging over 10 seeds, and 95% "
    "confidence intervals via the Student\u2019s t-distribution.\n\n"
    "(e) Surrogate significance test: The circular-shift surrogate method "
    "(Shorten et al. 2021) is described in full, including the number of "
    "surrogates (100), minimum shift (10 steps), and the empirical "
    "p-value formula with significance threshold p &lt; 0.01."
)

# ── Major 3 ──────────────────────────────────────────────────────────────────

story.append(Paragraph(
    "Major Comment 3: Disentangle top-down causation from common-driver forcing",
    heading2_style
))

add_comment_response(story,
    "From a methodological standpoint, I am not convinced that the Author "
    "demonstrates convincingly that the alignment of individual units with "
    "the mean field is due to top-down causation rather than to forcing caused "
    "by the environmental modulation A. [...] I encourage the Author to "
    "supplement their analysis by isolating constraint-driven order from "
    "mean-field-driven order. Conditional transfer entropy could be useful for "
    "this purpose. Moreover, I encourage the Author to pay particular attention "
    "to the value of A/K\u2080, which determines the extent to which the quadratic "
    "term influences the forcing from the environmental constraint. Combined "
    "with a deeper analysis of Figure 1 \u2014 for instance, why TE increases "
    "monotonically with A, and why the confidence interval rises sharply when "
    "A \u2248 50 \u2014 this would substantially strengthen the Author\u2019s argument.",

    "We thank the reviewer for this important suggestion, which has "
    "substantially strengthened the manuscript. We have addressed all three "
    "sub-points:\n\n"
    "(a) Conditional transfer entropy (CTE) analysis: We computed CTE in both "
    "directions (M \u2192 x and x \u2192 M), conditioning on the environmental signal "
    "K\u2099, across the same parameter sweep as Figure 1B (A = 0 to 60). Results "
    "are presented in a new Figure 3 and a new Results subsection "
    "(\u201cConditional transfer entropy: disentangling environmental forcing\u201d). "
    "The analysis reveals a two-component structure: the environmental signal "
    "accounts for a large share of the unconditional TE (as expected, since "
    "it is the shared driver), but a residual CTE(M\u2192x|K\u2099) persists across "
    "modulation amplitudes. At A = 60, conditioning reduces the TE by "
    "approximately 91%, yet the residual conditioned signal still shows "
    "CTE(M\u2192x|K\u2099) &gt; CTE(x\u2192M|K\u2099). A directional difference "
    "\u0394_CTE = CTE(M\u2192x|K\u2099) \u2212 CTE(x\u2192M|K\u2099) changes sign at intermediate "
    "amplitudes (A~15) and becomes positive at moderate to high modulation "
    "strengths. The two components \u2014 environmental scaffolding and emergent "
    "information flow from nonlinear aggregation \u2014 are discussed explicitly "
    "in both the Results and Discussion sections.\n\n"
    "(b) A/K\u2080 ratio analysis: We performed a parameter sweep over different "
    "baseline carrying capacities (K\u2080 = 50, 100, 200, and 400). The results "
    "(new Supplementary Figure S2) show that the TE curves collapse onto a "
    "single curve when plotted as a function of A/K\u2080, confirming this ratio "
    "as the relevant control parameter governing the transition from the "
    "nonlinear (quadratic-dominated) regime to the near-linear regime. This "
    "is now discussed in the Results section.\n\n"
    "(c) Explanation of Figure 1B features: We added explicit explanations "
    "for the two features the reviewer highlighted. First, TE(M\u2192x) increases "
    "monotonically with A because, at low amplitudes, idiosyncratic "
    "fluctuations from differences in the intrinsic growth rates dominate "
    "and the mean field has little predictive power; as the amplitude "
    "increases, the common modulation progressively shapes all trajectories, "
    "increasing the predictive information from the mean field about "
    "individual trajectories; once the environmental signal dominates the "
    "dynamics, additional increases in A introduce little additional "
    "predictive information, and the TE saturates. Second, the widening of "
    "the confidence interval at large amplitudes (A \u2273 40\u201350) reflects "
    "increased sensitivity to initial conditions across simulation seeds as "
    "the modulation amplitude approaches the scale of the baseline carrying "
    "capacity (A/K\u2080 ~ 0.5). In this regime, stronger forcing amplifies "
    "small differences in the chaotic trajectories, leading to greater "
    "variability in the estimated TE across runs."
)

# ── Minor 3 ──────────────────────────────────────────────────────────────────

story.append(Paragraph("Minor Comment 3: Unify terminology", heading2_style))

add_comment_response(story,
    'Please unify the terminology: "ensemble mean" (p. 4) vs. "mean field" '
    '(p. 5), "population mean" (p. 6), and so on.',

    'We have standardized the terminology to "mean field" throughout the '
    "entire manuscript (main text, figure captions, and supplementary "
    "materials). All instances of \u201censemble mean\u201d and \u201cpopulation mean\u201d "
    "have been replaced."
)

# ── Minor 4 ──────────────────────────────────────────────────────────────────

story.append(Paragraph("Minor Comment 4: Show how TE varies with \u03c9", heading2_style))

add_comment_response(story,
    "In Figure 1B, I suggest adding an inset illustrating how TE varies "
    "as a function of \u03c9.",

    "We have added a new Supplementary Figure S1 showing TE(M\u2192x) as a "
    "function of the modulation period (2\u03c0/\u03c9) at fixed amplitude "
    "A = 25. Transfer entropy remains high for slow modulation (long periods) "
    "but decreases as the modulation frequency increases, indicating that "
    "rapid environmental oscillations average out relative to the intrinsic "
    "chaotic dynamics and impose weaker coherent structure. A brief "
    "description has been added to the Results text, and the Methods section "
    "references this figure in the justification of \u03c9 = 2\u03c0/2000."
)

# ── Minor 5 ──────────────────────────────────────────────────────────────────

story.append(Paragraph(
    "Minor Comment 5: Clarify the saturation / soft-bound statement",
    heading2_style
))

add_comment_response(story,
    'The Author writes that "The saturation was not due to numerical clipping; '
    'although a soft bound..." Please explain.',

    "We have expanded this passage to clarify three points: (a) what the soft "
    "bound is \u2014 a bound of (0, 2K\u2080) = (0, 200) was imposed on all unit "
    "states at each time step to prevent unphysical negative concentrations "
    "and runaway growth while preserving the natural dynamics; (b) how often "
    "the bound was approached \u2014 at the highest modulation amplitude tested "
    "(A = 60), the lower bound (x \u2264 0) was approached in fewer than 10% of "
    "unit-timestep pairs across all seeds, and the upper bound (x \u2265 200) was "
    "never reached; and (c) why this rules out clipping as the driver of TE "
    "saturation \u2014 since the bound is rarely active, the saturation in TE "
    "reflects the genuine information-theoretic ceiling of environmental "
    "entrainment rather than an artifact."
)

# ── Minor 6 ──────────────────────────────────────────────────────────────────

story.append(Paragraph("Minor Comment 6: Write out SNR and R\u00b2 formulas", heading2_style))

add_comment_response(story,
    "Please explicitly write out the SNR and R\u00b2 formulas actually computed.",

    "We have added explicit formulas for both metrics in the new Methods "
    "section under \u201cRegression-based alignment metrics.\u201d R\u00b2 is defined "
    "as the standard coefficient of determination from a linear regression "
    "of the unit trajectory on the mean field. SNR is defined as "
    "Var(M\u2099) / Var(x \u2212 x\u0302), where x\u0302 denotes the regression prediction. "
    "Both formulas include full variable definitions."
)

# ── Minor 7 ──────────────────────────────────────────────────────────────────

story.append(Paragraph("Minor Comment 7: Fix the GitHub repo URL", heading2_style))

add_comment_response(story,
    "The address of the GitHub repo is incorrect.",

    "The GitHub repository URL has been corrected to "
    "https://github.com/celiablanco/macro_to_micro in both the main manuscript "
    "and the supplementary information."
)

# ── Minor 8 ──────────────────────────────────────────────────────────────────

story.append(Paragraph("Minor Comment 8: Fix Supplementary Figure S5 caption", heading2_style))

add_comment_response(story,
    'Supplementary Information, p. 4: The caption should indicate '
    '"Return maps of [...] A = {0, 20, 40, 60}".',

    "The caption for Supplementary Figure S5 has been corrected to indicate "
    "A = {0, 20, 40, 60}, matching the actual figure panels."
)

# ═════════════════════════════════════════════════════════════════════════════
# REVIEWER 2
# ═════════════════════════════════════════════════════════════════════════════

story.append(Paragraph("Reviewer 2", heading1_style))

add_comment_response(story,
    "The starting point of this work is the fact that a set of chaotic systems "
    "can synchronize even in the absence of mutual coupling when driven by a "
    "common external signal, for example, through the modulation of one of their "
    "control parameters. This is a well-known phenomenon, characterized in the "
    "classical literature on chaotic systems. [...] I think this work should be "
    "mentioned, in particular for its section 5: Boccaletti, S., Kurths, J., "
    "Osipov, G., Valladares, D. L., &amp; Zhou, C. S. (2002). The synchronization "
    "of chaotic systems. Physics Reports, 366(1\u20132), 1\u2013101. It goes without "
    "saying that it would be appreciated, at least in the continuation of this "
    "research line, to show the implications of the concept of synchronization "
    "in a simulation including some concrete aspect of biochemistry or biophysics.",

    "We thank the reviewer for this important reference. We have made two "
    "additions to the manuscript:\n\n"
    "(a) We now explicitly acknowledge in the Introduction that the "
    "synchronization of chaotic systems under common external forcing is a "
    "well-characterized phenomenon in nonlinear dynamics, citing Boccaletti "
    "et al. (2002). The relevant passage notes that \u201ceven without mutual "
    "coupling, a shared driving signal can entrain individually chaotic units "
    "into coherent collective behavior.\u201d\n\n"
    "(b) We have added a future-direction statement at the end of the Discussion "
    "noting that a natural extension of this work would be to test these "
    "principles in models incorporating more realistic prebiotic chemistry or "
    "biophysics \u2014 for example, protocell populations with explicit metabolic "
    "kinetics under cyclic environmental forcing \u2014 to determine whether the "
    "informational signatures identified here persist in more detailed "
    "chemical settings."
)

# ═════════════════════════════════════════════════════════════════════════════
# REVIEWER 3
# ═════════════════════════════════════════════════════════════════════════════

story.append(Paragraph("Reviewer 3", heading1_style))

add_comment_response(story,
    "One minor suggestion would be to sharpen, perhaps in the Discussion, the "
    "distinction between externally imposed boundary conditions and internally "
    'generated coordination, to further preempt potential misunderstandings '
    'regarding "top-down" causation.',

    "We have added a new paragraph in the Discussion that explicitly "
    "distinguishes two modes of coordination often conflated under the umbrella "
    'of "top-down causation": (i) externally imposed boundary conditions \u2014 '
    "such as the modulated carrying capacity K\u2099 in our model \u2014 which constrain "
    "all units from outside the system, and (ii) internally generated "
    "coordination arising from coupling among units themselves (e.g., "
    "autocatalytic feedback, cross-catalysis, or metabolic networks). The "
    "paragraph explains that our model demonstrates how external boundary "
    "conditions alone can produce the informational signatures of top-down "
    "influence, including a directional TE asymmetry and inter-unit "
    "predictability. The CTE analysis refines this interpretation by separating "
    "the component attributable to the external driver from the smaller "
    "residual component generated by nonlinear aggregation within the "
    "population. This clarifies that the \u2018top-down\u2019 signal in our model is "
    "not a claim of autonomous macroscopic agency, but rather a demonstration "
    "that externally structured environments can generate the informational "
    "preconditions from which internally coordinated systems may subsequently "
    "emerge."
)

# ═════════════════════════════════════════════════════════════════════════════

doc.build(story)
print(f"Response letter PDF saved to: {OUTPATH}")
