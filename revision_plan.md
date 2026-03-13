# Revision Plan: RSOS Manuscript Review Response

**Manuscript:** Context Without Contact: Top-Down Information Flow from Shared Modulation in Uncoupled Prebiotic Systems
**Review decision:** Major revisions
**Total tasks:** 9 (3 major, 6 minor)

---

## Execution Order

Execute tasks in this sequence. Each task lists its dependencies explicitly.

1. `MAJOR-3` (core analysis; determines framing for everything else)
2. `MAJOR-2` (methodology section; incorporates new CTE results)
3. `MAJOR-1` (introduction expansion; framing depends on CTE outcome)
4. `MINOR-3` through `MINOR-8` (editorial pass; no dependencies on each other)

---

## MAJOR-3: Disentangle top-down causation from common-driver forcing

**Priority:** Critical. This is the reviewer's core objection and determines whether the central claim survives as-is or needs reframing.

**Reviewer concern:** The observed macro-to-micro TE asymmetry may be entirely explained by shared environmental forcing (common driver) rather than genuine top-down causation. The current defense (that shared input is the mechanism of interest) conflates two distinct claims: (a) shared input produces population-level structure, and (b) that structure constitutes downward causation.

**Subtasks:**

### MAJOR-3a: Conditional transfer entropy (CTE) analysis

- **What:** Compute conditional TE in both directions (M -> x and x -> M), conditioning on the environmental signal K_n.
- **Why:** If the macro-to-micro asymmetry persists after conditioning out K_n, that is evidence for top-down causation beyond simple common driving. If it vanishes, the claim must be reframed (still publishable, but as environmentally scaffolded coordination rather than top-down causation per se).
- **Where in manuscript:** New results subsection; also update Discussion to reflect outcome.
- **Acceptance criteria:** CTE computed for the same parameter sweep as Figure 1B (A = 0 to 60). Results plotted alongside unconditional TE for direct comparison. Interpretation stated clearly.

### MAJOR-3b: A/K_0 ratio sweep

- **What:** Run a parameter sweep over A/K_0 values to characterize how the ratio of modulation amplitude to baseline carrying capacity governs the transition from nonlinear (quadratic-dominated) to near-linear regime.
- **Why:** The reviewer identifies A/K_0 as the key control parameter determining when the quadratic term in the logistic equation becomes negligible, which alone can increase unit alignment independent of any top-down mechanism.
- **Where in manuscript:** New figure or panel; referenced in both Methods and Results.
- **Acceptance criteria:** Plot showing TE (or CTE) as a function of A/K_0. Discussion of the regime boundary where quadratic dynamics become negligible.

### MAJOR-3c: Explain Figure 1B features

- **What:** Provide explicit explanations for two unexplained features of Figure 1B:
  1. Why TE(M -> x) increases monotonically with A.
  2. Why the confidence interval rises sharply around A ~ 50 (what does this transition represent physically?).
- **Why:** The reviewer flags both as requiring at minimum a brief explanation. Currently absent.
- **Where in manuscript:** Results section, in the paragraph discussing Figure 1B.
- **Acceptance criteria:** Each feature explained in 2-3 sentences with physical or information-theoretic reasoning. The A ~ 50 transition should be connected to the A/K_0 analysis from MAJOR-3b if applicable.

---

## MAJOR-2: Add a dedicated Methodology section

**Priority:** High. Depends on MAJOR-3 (new CTE methodology content to include).

**Reviewer concern:** Model description and parameter choices are embedded in Results. Several parameters (r_min, r_max, K_0, A, omega) appear arbitrary without justification.

**Subtasks:**

### MAJOR-2a: Extract model description from Results

- **What:** Move the model definition (equations, variable definitions, ensemble mean definition) from the current Results section into a new Methods section placed between Introduction and Results.
- **Where in manuscript:** Create new "Model and Methods" section after Introduction.
- **Acceptance criteria:** Results section no longer contains model setup; it opens directly with findings.

### MAJOR-2b: Justify parameter choices

- **What:** For each parameter (r_min, r_max, K_0, A, omega, N, T, number of bins, embedding lag k), provide either:
  - A physical or biological motivation, or
  - A sensitivity analysis reference (pointing to supplementary figures), or
  - An explicit statement that the choice is conventional in the literature (with citation).
- **Where in manuscript:** Methods section. Consider adding a parameter table.
- **Acceptance criteria:** No parameter appears without justification. A summary table listing parameter, value, and rationale is included.

### MAJOR-2c: Document TE estimation procedure

- **What:** Clearly present the histogram-based TE estimation method, including bin count selection, lag selection rationale (referencing Supplementary Figure S1), and the surrogate testing procedure (circular shift method, number of surrogates, significance threshold).
- **Where in manuscript:** Methods section.
- **Acceptance criteria:** A reader could reproduce the TE computation from the Methods section alone.

---

## MAJOR-1: Strengthen the Introduction

**Priority:** High. Depends on MAJOR-3 (framing of the central claim may shift based on CTE results).

**Reviewer concern:** The Introduction is insufficient. It needs more depth on three fronts.

**Subtasks:**

### MAJOR-1a: Prior work on top-down causation in origin of life and evolutionary transitions

- **What:** Add 1-2 paragraphs reviewing prior work on top-down causation specifically in the context of origin of life and major evolutionary transitions. Some of this material currently lives in the Discussion (references to Walker, Ellis, Szathmary); move the framing earlier and expand with additional citations.
- **Where in manuscript:** Introduction, after the current opening paragraph.
- **Acceptance criteria:** At least 5-6 references to prior work on top-down causation in evolutionary transitions context. Clear statement of what has been done and what gap this paper fills.

### MAJOR-1b: Logistic maps in computational biology

- **What:** Add a paragraph covering the use of logistic map models in computational biology and population dynamics, including their role as minimal models for chaotic systems and their relevance to the type of dynamics being studied here.
- **Where in manuscript:** Introduction, in the paragraph that motivates the model choice.
- **Acceptance criteria:** At least 2-3 references to logistic maps in biological/prebiotic modeling contexts. Brief statement of why this model class is appropriate.

### MAJOR-1c: Information-theoretic measures in this domain

- **What:** Add a paragraph reviewing the application of transfer entropy and related information-theoretic measures to biological systems, multi-scale dynamics, and causality detection. The current mention of TE is too brief.
- **Where in manuscript:** Introduction, before the paragraph describing the present study's approach.
- **Acceptance criteria:** At least 3-4 references covering TE applications in biological or complex systems contexts. Brief discussion of strengths and limitations of TE as a causality proxy.

---

## MINOR-3: Unify terminology

**Priority:** Low. No dependencies.

- **What:** Audit the entire manuscript for inconsistent terminology referring to the macroscopic variable. Current variants: "ensemble mean" (p. 4), "mean field" (p. 5), "population mean" (p. 6).
- **Action:** Choose one term (recommend "mean field" as it is most precise for this model) and replace all variants consistently in main text, figure captions, and supplementary materials.
- **Acceptance criteria:** A text search for "ensemble mean" and "population mean" returns zero hits (except where explicitly comparing terminology). "Mean field" used throughout.

---

## MINOR-4: Add omega inset to Figure 1B

**Priority:** Low. No dependencies.

- **What:** Add a small inset to Figure 1B showing how TE varies as a function of omega (modulation frequency).
- **Action:** If the omega sweep has already been run, extract the data and add the inset. If not, run a sweep over omega values (suggest 5-10 values spanning at least one order of magnitude) with other parameters held at defaults.
- **Acceptance criteria:** Inset panel in Figure 1B showing TE(M -> x) vs. omega. Brief mention in Results text (1-2 sentences).

---

## MINOR-5: Clarify the saturation / soft-bound statement

**Priority:** Low. No dependencies.

- **What:** The sentence on p. 7 ("The saturation was not due to numerical clipping; although a soft bound...") is unclear.
- **Action:** Expand to explain: (a) what the soft bound of (0, 2K_0) is and why it was imposed, (b) how often it was approached at different A values, and (c) why hitting it in <10% of cases at A=60 rules out clipping as the driver of TE saturation.
- **Acceptance criteria:** A reader unfamiliar with the implementation can understand what the bound does and why it does not confound the result. 2-3 sentences.

---

## MINOR-6: Write out SNR and R-squared formulas

**Priority:** Low. No dependencies.

- **What:** The SNR and R-squared metrics (referenced in Figure 2B and surrounding text) are not formally defined.
- **Action:** Add explicit formulas for both. For R-squared: the standard coefficient of determination between M_n and x_{1,n}. For SNR: Var(M_n) / Var(residuals from regressing x_{1,n} on M_n).
- **Where in manuscript:** Methods section (after MAJOR-2 restructuring) or inline in Results near Figure 2 discussion.
- **Acceptance criteria:** Both formulas written out with variable definitions.

---

## MINOR-7: Fix the GitHub repo URL

**Priority:** Low. No dependencies.

- **What:** The GitHub repository address on p. 11 is incorrect.
- **Action:** Verify the correct URL and replace.
- **Acceptance criteria:** URL resolves to the correct repository.

---

## MINOR-8: Fix Supplementary Figure S3 caption

**Priority:** Low. No dependencies.

- **What:** The caption for Figure S3 currently lists A = {0, 25, 50}. The reviewer states it should read A = {0, 20, 40, 60}.
- **Action:** Check the actual panels in Figure S3. If panels show A = {0, 20, 40, 60}, update the caption. If panels show A = {0, 25, 50}, update the caption to match and note the discrepancy with the reviewer's suggestion (the reviewer may have been looking at a different version or making a suggestion for new values).
- **Acceptance criteria:** Caption matches the actual figure panels exactly.

---

## Checklist (for final pass before resubmission)

- [ ] MAJOR-3a: CTE analysis complete; results plotted and interpreted
- [ ] MAJOR-3b: A/K_0 sweep complete; figure added
- [ ] MAJOR-3c: Figure 1B features explained in text
- [ ] MAJOR-2a: Methods section created; model setup moved from Results
- [ ] MAJOR-2b: Parameter table with justifications included
- [ ] MAJOR-2c: TE estimation procedure fully documented
- [ ] MAJOR-1a: Top-down causation literature expanded in Introduction
- [ ] MAJOR-1b: Logistic maps in computational biology reviewed
- [ ] MAJOR-1c: Information-theoretic measures reviewed
- [ ] MINOR-3: Terminology unified to "mean field" throughout
- [ ] MINOR-4: Omega inset added to Figure 1B
- [ ] MINOR-5: Soft-bound statement clarified
- [ ] MINOR-6: SNR and R-squared formulas written out
- [ ] MINOR-7: GitHub URL corrected
- [ ] MINOR-8: Supplementary Figure S3 caption corrected
- [ ] Response letter drafted addressing each reviewer comment with specific changes made
