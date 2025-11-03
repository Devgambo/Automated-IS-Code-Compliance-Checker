from typing import List, Dict
from groq import Groq
import os

client = Groq(api_key=os.getenv('GROQ_API_KEY'))
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

def generate_compliance_report(
    Initial_report: str,
    vectordb,
    embedding_model,
    previous_analysis,
    user_input,
    k: int = 5
) -> str:
    """
    Generate a compliance report by comparing validated drawing data 
    with IS codes (via RAG) using Groq + LLaMA-3.
    """
    # Resolve content if a file path is provided, otherwise treat as raw markdown
    if os.path.isfile(Initial_report):
        with open(Initial_report, encoding="utf-8") as f:
            Initial_report = f.read()
    else:
        Initial_report = Initial_report

    # --- 1. Embed image data and query vector DB ---
    query_embedding = embedding_model.embed_query(Initial_report)
    retrieved = vectordb.query([query_embedding], n_results=k)

    context_texts = "\n\n".join(
        [f"[Source: {r['metadata'].get('source_file', 'N/A')}, "
         f"Clause: {r['metadata'].get('chunk_id', 'N/A')}]\n{r['document']}"
         for r in retrieved]
    )
    
    # --- 2. Prompt ---
    system_prompt = """
You are a Indian Senior Civil engineer. Your task is to refine a previous analysis of an RCC structural drawing based on new information provided by the user. Output a combined report of both the initial report and user input and also the context extracted from the IS codes and generate a final report of structural drawing data.Always cite the specific IS clause from the provided context.
Output a structured compliance report. You will be given the PREVIOUS ANALYSIS and the USER'S NEW INPUT.
"""

    user_prompt = f"""
**PREVIOUS ANALYSIS:**
---
{previous_analysis}
---

**USER'S NEW INPUT:**
---
{user_input}
---

**IS Code Context (Retrieved)**
{context_texts}


**Your Tasks:**
1.  **Integrate New Information:** Carefully review the USER'S NEW INPUT and use it to fill in the gaps and correct the information in the PREVIOUS ANALYSIS.
2.  **Re-run Compliance Checks:** With the new information, re-evaluate the compliance of each checklist item against The extracted IS Code contexts.
2.  **Re-run Compliance Checks:** With the new information, re-evaluate the compliance of each checklist item against IS 456:2000 and SP 34.
3.  **Produce an Updated Report:** Generate a single, complete, and updated report in the same Markdown checklist format as the original.
4.  **Update Missing Information List:** The final "**Missing or Wrong Information**" section should only contain items that are *still* missing or non-compliant after incorporating the user's input. If all issues are resolved, state this clearly.

Do not ask for more information. Provide the updated report based only on the context provided.

### Initial Preliminary Report with additioal user input
{Initial_report}



"""

    # --- 3. Call Groq ---
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.0  # deterministic
    )

    print("response generated.")

    return response.choices[0].message.content









    #         user_prompt = f"""
    # ### Initial Preliminary Report with additioal user input
    # {Initial_report}

    # ### IS Code Context (Retrieved)
    # {context_texts}

    # ### Task
    # Compare and validate the extracted RCC design data against the provisions of *SP 34*, identifying whether the design parameters meet the code requirements and highlighting any deviations, warnings, or violations.

    # ---

    # ### 📄 *Input Data (Provide or Attach):*

    # Include all or any available RCC design data extracted from the drawing or report, for example:

    # * *Member Type:* (e.g., Beam / Slab / Column / Footing)
    # * *Dimensions:* (b, D, L, cover, etc.)
    # * *Material Grades:* (fck = … MPa, fy = … MPa)
    # * *Load Details:* (DL, LL, factored load, etc.)
    # * *Reinforcement Details:*

    # * Main bars (number, diameter, spacing)
    # * Distribution or secondary steel
    # * Stirrups / Ties (diameter, spacing)
    # * *Support Conditions*
    # * *Design Moments & Shear Values* (if available)
    # * *Location or exposure condition* (for durability checks)
    # * *Concrete cover and effective depth*
    # * *Any special design notes* (development length, anchorage, detailing, etc.)

    # ---

    # ### ⚙ *Task Instructions:*

    # 1. *Step 1 — Validate Design Inputs*

    # * Check if all the necessary parameters for RCC design are available.
    # * Identify missing or inconsistent data (e.g., unspecified cover, bar diameters without spacing, etc.).

    # 2. *Step 2 — IS 456:2000 Compliance*
    # Perform a *clause-by-clause verification* based on IS 456:2000, including but not limited to:

    # * *Clause 5–9:* Material properties (cement, aggregates, reinforcement grades)
    # * *Clause 22:* Design philosophy (limit state method)
    # * *Clause 26:* Requirements for durability, cover, exposure, and quality control
    # * *Clause 36:* Reinforcement detailing and bar curtailment
    # * *Clause 40:* Development length and anchorage
    # * *Clause 41–46:* Serviceability checks (deflection, cracking)
    # * *Annex A/B:* Stress-strain relations, permissible limits
    # * *Member-specific clauses:*

    #     * Beams — flexure, shear, torsion (Clauses 38, 40.1)
    #     * Slabs — one-way/two-way (Clauses 24, 26.5.2)
    #     * Columns — axial load + bending (Clause 39)
    #     * Footings — bearing, punching shear (Clause 34)

    # For each check, include:

    # * Reference clause number
    # * Formula or criterion from IS 456
    # * Computed or given value from design data
    # * Pass/Fail or Compliant/Non-Compliant verdict

    # 3. *Step 3 — SP 34 Comparison*

    # * Use *SP 34* for reinforcement detailing checks (preferred bar spacing, curtailment, anchorage, lap length, etc.)
    # * Verify:

    #     * Bar placement and spacing limits
    #     * Minimum and maximum reinforcement ratios
    #     * Detailing around supports and corners
    #     * Shear reinforcement distribution
    #     * Recommended detailing practices for ductility and crack control
    # * Cite the *SP 34 table/figure reference* and provide a short note comparing the design’s detailing to those guidelines.

    # 4. *Step 4 — Tabular Comparison*
    # Prepare a structured comparison table like:

    # | Check Type    | Parameter            | Design Value | IS 456:2000 Limit/Requirement | SP 34 Guideline | Clause/Ref        | Status (OK/Not OK) | Remarks            |
    # | ------------- | -------------------- | ------------ | ----------------------------- | --------------- | ----------------- | ------------------ | ------------------ |
    # | Flexure       | Mu (kNm)             | 68.5         | < Mu_lim (72.4)               | –               | IS 456 Cl. 38.1   | ✅ OK               | Within capacity    |
    # | Reinforcement | Main bars (mm²)      | 804          | ≥ 804                         | Fig. 7, SP34    | ✅                 | OK                 |                    |
    # | Cover         | Effective cover (mm) | 20           | ≥ 25 (moderate exposure)      | –               | IS 456 Cl. 26.4.2 | ❌                  | Less than required |

    # 5. *Step 5 — Final Output*

    # * Provide a *summary of compliance* (e.g., 85% compliant with IS 456, 90% compliant with SP 34)
    # * Highlight *critical deviations* that could affect safety, serviceability, or code compliance.
    # * Suggest *rectifications or redesign notes* where applicable.

    # ---

    # ### 🧾 *Output Format (Structured Response)*

    # * *Section 1:* Summary of data checked
    # * *Section 2:* IS 456:2000 verification (with clause references)
    # * *Section 3:* SP 34 detailing check (with figure/table references)
    # * *Section 4:* Comparison Table (as shown above)
    # * *Section 5:* Observations and Recommendations

    # ---

    # ### ⚠ *Optional Enhancements*

    # If you want the comparison to be automated or AI-assisted:

    # * Ask the model to highlight non-compliance in red and suggest correction per code.
    # * Ask for *separate summaries per RCC member type* (beam/slab/column/footing).
    # * Request the *percentage deviation from IS code permissible limits* for each parameter.

    # ---

    # ### ✅ *Example Prompt (ready-to-use)*

    # > You are an RCC design auditor.
    # > I will provide RCC design data extracted from construction drawings.
    # > Compare every design parameter against the rules and clauses of *IS 456:2000* and *SP 34*, and create a detailed compliance report.
    # >
    # > For each check:
    # >
    # > * Mention the *IS clause number or SP 34 reference*.
    # > * Show formula or limit used for verification.
    # > * Provide computed value from the extracted data.
    # > * Mark as *Compliant / Non-Compliant / Insufficient Data*.
    # > * Give recommendations for correction if not compliant.
    # >
    # > Output in this structure:
    # >
    # > 1. Data Summary
    # > 2. IS 456:2000 Clause-wise Verification
    # > 3. SP 34 Detailing Check
    # > 4. Comparative Table (as shown above)
    # > 5. Summary and Recommendations

    # """