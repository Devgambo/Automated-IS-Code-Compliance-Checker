## RCC Structural Drawing Compliance Report - Foundations

**Project:** [Not Specified in Drawing]
**Drawing Title:** FOUNDATIONS
**Date of Analysis:** [Current Date]
**Based on:** IS 456:2000 and SP 34

---

### Step 0: Initial Document Check
- **0.1:** The document is an RCC structural drawing of "FOUNDATIONS" only.
- **0.2:** Site location: Mangalore (User Provided).
- **0.3:** All compliance checks will be based only on IS 456:2000 and SP 34.

### Step 1: Locate the "NOTES" Section
- **Status:** Compliant

### Step 2 & 3: Extract and Verify Design Parameters from "NOTES"

| Criteria | Extracted Value / User Input | Compliance Check | Status | IS Clause Reference |
|---|---|---|---|---|
| **1. Grade of Concrete** | M20 for all R.C.C works | M20 is a common grade. For Mangalore (coastal region), exposure conditions are typically 'severe' as per IS 456:2000, Table 3. M20 concrete is generally suitable for 'moderate' exposure. For 'severe' exposure, minimum grade of M25 is recommended for RCC. However, without explicit exposure class in the drawing, and given the user input of M20, we proceed with M20. | Cannot Verify / Potential Non-Compliance | IS 456:2000, Table 3 & 5 |
| **2. Reinforcement Bars** | HYSD TMT bars of Grade Fe 500 conforming to IS 1786-2008. Shear reinforcement and stirrups are mentioned in the "SCHEDULE OF COLUMNS" as "TIES Y8@8" and "TIES Y8@4". | Fe 500 is standard and compliant with IS 1786. The mention of stirrups/ties is good. | Compliant | SP 34, Clause 12 (referencing IS 1786) |
| **3. Lap Length** | 50 times dia of the bar, to be staggered such that not more than 50% of the bars are lapped at a section. | Complies with the general rule of 50d. Staggering is good practice as per good detailing practices. | Compliant | IS 456:2000, Clause 26.2.5 |
| **4. Clear Cover** | Footing/Wall: 50 mm, Columns: 40 mm, Beam: 25 mm, Slab: 20 mm. | Footing cover (50mm) is minimum for 'moderate' exposure (IS 456:2000, Table 16A). Given Mangalore's coastal environment, 'severe' exposure might apply, requiring 50mm minimum cover for footings. PCC is mentioned in Section X, which is good for a 50mm cover. Column cover (40mm) is within the 40-70mm range for columns (IS 456:2000, Clause 26.4.2.1). Beam and Slab covers are typical. | Compliant | IS 456:2000, Clause 26.4.2.1, Table 16A |
| **5. Development Length (Ld)** | 50 times the dia of the bar. | A common value (50d). This value should be calculated based on concrete grade and steel grade as per IS 456:2000, Clause 26.2.1. | Compliant (as a general rule, but specific calculation is needed) | IS 456:2000, Clause 26.2.1 |
| **6. Safe Bearing Capacity (SBC) of soil** | 18 T/m2 | SBC is mentioned. PCC is specified in Section X. | Compliant | - |
| **7. Seismic Zone and Wind Load** | Seismic Zone: Zone 3 (User Provided). Wind Load: Not mentioned. | Seismic Zone 3 is now specified. Wind load is still missing, which is mandatory for structural design. | Partially Compliant / Missing Information | IS 1893 (Part 1):2016 (for seismic), IS 875 (Part 3):1987 (for wind) |
| **8. Building Limitations** | Structure is designed for G+1 storey. | Building limitation (G+1 storey) is mentioned. | Compliant | - |
| **9. Structure's Purpose** | Not explicitly mentioned, but implied as a G+1 storey building. | The specific purpose (e.g., residential, commercial) is not stated. This can influence live loads and other design parameters. | Missing Information | IS 875 (Part 2):1987 |
| **10. Floor Heights** | 3.6m (floor to floor) with 0.3m slab + finish and 0.6m ceiling (User Provided). | Floor heights are now specified. | Compliant | - |
| **11. Schedule of Footings** | A "SCHEDULE OF FOOTINGS" table is present and appears consistent with the "FOUNDATION PLAN". | The table is present and seems consistent. | Compliant | SP 34, Clause 3.3.15 |
| **12. Footing Type** | Isolated footings (F1 to F5). | Isolated footings are used for a G+1 storey building, which is appropriate for low-rise structures. | Compliant | SP 34, Section 6 |
| **13. Reinforcement in High-Rise Buildings** | Not applicable as the structure is G+1 storey (low-rise). | Not Applicable | Not Applicable | - |
| **14. Raft Foundation Reinforcement** | Not applicable as isolated footings are used. | Not Applicable | Not Applicable | - |
| **15. Lift Design** | Not mentioned, and no lift pit is shown. | Not Applicable | Not Applicable | - |
| **16. Soil Improvement** | Soil improvement already done (User Provided). | Details about soil improvement are now provided. | Compliant | - |
| **17. Column Ties** | "COLUMN TIES" are indicated in Section X and "TIES" are specified in the "SCHEDULE OF COLUMNS". They appear continuous in the typical column details. | Column ties are shown and specified. | Compliant | SP 34, Clause 3.4.2 |
| **18. Plan of Ties** | A separate plan for ties is not explicitly present, but tie details are given in the "SCHEDULE OF COLUMNS". | While not a separate plan, the details are provided. | Compliant | SP 34, Clause 3.3.15 |
| **19. Outer Ties Check** | Column C1: Main bars 8Y12, Ties Y8@8. Column C2: Main bars 4Y16 + 4Y12, Ties Y8@8. Column C3: Main bars 4Y16 + 4Y12, Ties Y8@4. Percentage of steel cannot be calculated without column dimensions. | The number and diameter of bars and ties are specified. Column dimensions are still needed to verify actual percentage of steel against limiting values. | Cannot Verify | IS 456:2000, Clause 26.5.3.1 |
| **20. Cross-Section Area** | Assume limiting value of steel in column, cross section also to be taken as limiting value (User Provided). | User assumes limiting values. However, the actual column dimensions are still not provided in the drawing, which are essential for verification. | Cannot Verify | IS 456:2000, Clause 26.5.3.1 |
| **21. Steel Curtailment** | Not applicable for a G+1 storey building. | Not Applicable | Not Applicable | - |
| **22. Maximum Steel Percentage in Columns** | Assume limiting value of steel in column, max steel percentage also to be taken as limiting value (User Provided). | User assumes limiting values. The maximum percentage of steel in columns is 6% (IS 456:2000, Clause 26.5.3.1). This assumption cannot replace explicit design values or actual column dimensions for verification. | Cannot Verify | IS 456:2000, Clause 26.5.3.1 |

### Step 5: Report Missing or Wrong Information

1.  **Grade of Concrete Suitability:** While M20 is specified, for Mangalore's coastal environment, 'severe' exposure conditions are likely, which would recommend M25 as per IS 456:2000, Table 5. The drawing should explicitly state the exposure class and justify the concrete grade.
2.  **Wind Load:** Wind load parameters (e.g., basic wind speed, terrain category, importance factor) are still missing. This is crucial for a complete structural design as per IS 875 (Part 3):1987.
3.  **Structure's Purpose:** The specific purpose of the building (e.g., residential, commercial, institutional) is not stated. This affects live load assumptions (IS 875 Part 2) and other design considerations.
4.  **Column Dimensions:** Actual column dimensions are still missing from the drawing. Without these, the percentage of steel, cross-section area, and maximum steel percentage cannot be verified against IS 456:2000, Clause 26.5.3.1, even with the user's assumption of limiting values. The drawing should provide these dimensions.
5.  **Development Length Calculation:** While 50d is a common value, the actual development length should be calculated based on the specific concrete grade (M20) and steel grade (Fe 500) as per IS 456:2000, Clause 26.2.1, and explicitly stated or verified.

### Summary of Compliance

-   **Total Criteria Evaluated:** 22
-   **Compliant Items:** 10
-   **Partially Compliant Items:** 1 (Seismic Zone provided, Wind Load missing)
-   **Cannot Verify Items:** 4 (Due to missing drawing information, even with user assumptions)
-   **Missing Information Items:** 4 (Still missing after user input)
-   **Potential Non-Compliance:** 1 (Concrete grade for exposure condition)

**Overall Verdict:** The user's input has significantly improved the completeness of the information, particularly regarding site location, seismic zone, floor heights, and soil improvement. However, critical information such as **wind load parameters** and **actual column dimensions** are still missing from the drawing. Additionally, the suitability of M20 concrete for the specified coastal site's exposure conditions needs explicit verification or justification in the drawing. The assumptions made by the user regarding limiting values for steel percentage and cross-section area cannot substitute for explicit dimensions and design calculations in the drawing itself for verification.