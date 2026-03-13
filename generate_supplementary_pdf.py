"""
Generate the revised supplementary information PDF with changes highlighted in red.
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

FIGDIR = os.path.join(os.path.dirname(__file__), 'figures')
OUTPATH = os.path.join(os.path.dirname(__file__), 'revised_supplementary.pdf')

doc = SimpleDocTemplate(OUTPATH, pagesize=letter,
                        topMargin=0.8*inch, bottomMargin=0.8*inch,
                        leftMargin=1*inch, rightMargin=1*inch)

styles = getSampleStyleSheet()

title_style = ParagraphStyle('Title2', parent=styles['Title'], fontSize=14,
                              leading=18, spaceAfter=12, alignment=TA_CENTER)
heading_style = ParagraphStyle('Heading2', parent=styles['Heading1'], fontSize=13,
                                leading=17, spaceBefore=16, spaceAfter=8)
body_style = ParagraphStyle('Body2', parent=styles['Normal'], fontSize=10,
                             leading=14, spaceAfter=6, alignment=TA_JUSTIFY)
caption_style = ParagraphStyle('Caption', parent=styles['Normal'], fontSize=9,
                                leading=12, spaceAfter=6, alignment=TA_JUSTIFY)

def R(text):
    return f'<font color="red">{text}</font>'

def B(text):
    return f'<b>{text}</b>'

story = []

# Title
story.append(Paragraph("Supplementary Information:", title_style))
story.append(Paragraph(
    "Context Without Contact: Top-Down Information Flow from Shared "
    "Modulation in Uncoupled Prebiotic Systems",
    ParagraphStyle('SubTitle', parent=styles['Title'], fontSize=12, leading=16, spaceAfter=18)))

story.append(Paragraph(B("This PDF file includes:"), body_style))
story.append(Paragraph("Supporting Figures S1 to S3", body_style))
story.append(Spacer(1, 24))

# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE S1
# ═══════════════════════════════════════════════════════════════════════════════
figS1_path = os.path.join(FIGDIR, 'figS1.png')
if os.path.exists(figS1_path):
    story.append(Image(figS1_path, width=4*inch, height=3*inch))
story.append(Spacer(1, 6))
story.append(Paragraph(
    B("Figure S1. Mean transfer entropy (TE) as a function of embedding lag k for modulation "
      "amplitude A=25. ") +
    "Top-down TE (M\u2192x, circles) measures information from the macroscopic "
    + R("mean field") + " to an individual unit, while bottom-up TE (x\u2192M, squares) measures "
    "the reverse direction. Values are averaged over 10 random seeds. Parameters: N=1000, "
    "K\u2080=100, r<sub>i</sub>\u2208[3.9,4.0], T=10,000 steps (first 1,000 discarded), "
    "15-bin histograms.",
    caption_style))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE S2
# ═══════════════════════════════════════════════════════════════════════════════
figS2_path = os.path.join(FIGDIR, 'figS2.png')
if os.path.exists(figS2_path):
    story.append(Image(figS2_path, width=6*inch, height=4.5*inch))
story.append(Spacer(1, 6))
story.append(Paragraph(
    B("Figure S2. Directional information flow from macroscopic to microscopic dynamics under "
      "different modulation profiles. ") +
    "Transfer entropy (TE) between the " + R("mean field") + " M<sub>n</sub> and a representative "
    "unit x<sub>n</sub>, computed in both directions: M \u2192 x (blue) and x \u2192 M (gray), "
    "for a population of N = 1000 uncoupled logistic units evolving under carrying capacity "
    "modulated by (A,C) logistic increase, and (B,D) inverse logistic. In all cases "
    "K<sub>0</sub> = 100, A = 25, r<sub>i</sub> \u2208 [3.9, 4.0], and steepness is k = 0.05, "
    "simulated over 10 independent simulations, each run for T = 10,000 steps (first 1,000 "
    "discarded). Top row: The black curve shows the external modulation K<sub>n</sub>, the blue "
    "line corresponds to the " + R("mean field") + " M, sampled every 200 steps, and the shaded "
    "gray band indicates the range of individual states at each sampled point. Bottom row: TE "
    "estimated using a histogram-based method with lag k = 2 and 15 bins. Shaded regions "
    "indicate 95% confidence intervals.",
    caption_style))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE S3 (MINOR-8: corrected caption A = {0, 20, 40, 60})
# ═══════════════════════════════════════════════════════════════════════════════
figS3_path = os.path.join(FIGDIR, 'figS3.png')
if os.path.exists(figS3_path):
    story.append(Image(figS3_path, width=5*inch, height=4.2*inch))
story.append(Spacer(1, 6))
story.append(Paragraph(
    B("Figure S3. Structural modulation induces low-dimensional macroscopic dynamics. ") +
    "Return maps of (M<sub>n</sub>, M<sub>n+1</sub>) for "
    + R("A = {0, 20, 40, 60}") +
    ", N = 1,000, K<sub>0</sub> = 100, r<sub>i</sub> \u2208 [3.9, 4.0], and T = 10,000 steps "
    "(first 1,000 discarded). The dashed line shows the identity M<sub>n+1</sub> = M<sub>n</sub> "
    "and the gray curve shows the single-unit logistic map for comparison. At A=0, points cluster "
    "near (K<sub>0</sub>/2, K<sub>0</sub>/2). As A increases, shared modulation widens the "
    "distribution of M<sub>n</sub>, producing a diagonal spread.",
    caption_style))

# Build PDF
doc.build(story)
print(f"Revised supplementary saved to: {OUTPATH}")
