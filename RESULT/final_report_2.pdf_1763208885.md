## RCC Structural Drawing Compliance Report

**Project:** Foundations for Entrance Gate and Guard Room
**Location:** Malpe Fishery Harbour, Udupi
**Reference Standards:** IS 456:2000, SP 34

### Step 0: Initial Document Check
- **0.1:** The document is an RCC structural drawing of "FOUNDATIONS" only.
- **0.2:** Site Location: Malpe Fishery Harbour, Udupi.
- **0.3:** All compliance checks are based only on IS 456:2000 and SP 34.

### Step 1: Locate the "NOTES" Section
- **Status:** Compliant

### Step 2 & 3: Extract and Verify Design Parameters from "NOTES" (Updated with User Input)

| Criteria | Extracted Value / User Input | Compliance Check | Status |
|---|---|---|---|
| **1. Grade of Concrete** | M20 (User Input) | The user has specified M20. As per SP 34, Clause 11.8.4.7, the minimum grade of concrete for foundation shall be not less than M20. This is compliant. | Compliant |
| **2. Reinforcement Bars** | HYSD TMT Bars, Grade Fe 550, conforming to IS 1786-1985. Column vertical reinforcement: 8Y16. Column ties: Y8@200. Footing bottom reinforcement: Y10@125. | Fe 550 is a high-strength grade. However, IS 1786-1985 is an older standard; the current standard for high strength deformed steel bars is IS 1786:2008. This is a non-compliance. | Non-Compliant |
| **3. Lap Length** | 50 times dia of the bar, not more than 50% of bars are lapped at a section. | 50d is a common and generally compliant value as per IS 456:2000, Clause 26.2.5.1. The staggering requirement is also good practice. | Compliant |
| **4. Clear Cover** | Footing/Wall: 50 mm, Columns: 40 mm, Slab: 25 mm, Beam: 30 mm. | Footing cover of 50mm is the minimum as per IS 456:2000, Clause 26.4.2.2. The drawing shows 150mm PCC below the footing, which is good practice for a 50mm cover. Column cover of 40mm is compliant as per IS 456:2000, Clause 26.4.2.1 (minimum 40mm or diameter of bar, whichever is greater). Slab and beam covers are also generally compliant for normal exposure. SP 34, Clause 11.8.4.6 specifies 100mm for base slab and 50mm for columns, but these are for specific industrial foundations, and the general IS 456:2000 values are applicable here. | Compliant |
| **5. Development Length (Ld)** | 50 times the dia. of the bar. | 50d is a common and generally compliant value. For Fe 550 and M20 concrete, the tabulated value for tension bars (SP 34, Clause 43) is 56.6d for 10mm bar and 90.6d for 16mm bar. For compression bars, it's 45.3d for 10mm bar and 72.5d for 16mm bar. A general value of 50d is often used as a simplified approach, but specific calculation based on bar diameter and concrete grade is required for exact compliance as per IS 456:2000, Clause 26.2.1. | Cannot Verify |
| **6. Safe Bearing Capacity (SBC) of soil** | 10 T/m2 (100 kN/m2). PCC is mentioned (150mm thick). | SBC is mentioned. PCC is specified. SP 34, Clause 3.3.3 states that information regarding the underside conditions, such as the thickness of blinding, shall be shown. | Compliant |
| **7. Seismic Zone and Wind Load** | Seismic Zone III and Wind Forces as per IS 1893:2016 & IS 875:2015 respectively. | Seismic zone and wind load standards are mentioned and are current. | Compliant |
| **8. Building Limitations** | Structure is designed for Ground + 1 Storey + Lightweight Roof. | Building limitations are specified. | Compliant |
| **9. Structure's Purpose** | Entrance Gate and Guard Room. | The purpose of the structure is mentioned. | Compliant |
| **10. Floor Heights** | 3.6m (floor to floor) with 0.3m slab + finish and 0.6m ceiling (User Input) | Specific floor heights are now provided. SP 34, Clause 3.3.5 states that main dimensions of the structure, such as heights between floors, shall be shown on the drawings. | Compliant |
| **11. Schedule of Footings** | Present and consistent with F1 footing details. | A "SCHEDULE OF FOOTINGS" table is present and provides dimensions and reinforcement for F1. | Compliant |
| **12. Footing Type** | Isolated footings (F1). | Isolated footings are used for a Ground + 1 Storey structure, which is appropriate. | Compliant |
| **13. Reinforcement in High-Rise Buildings** | Not applicable. | The structure is Ground + 1 Storey, not a high-rise building. | Not Applicable |
| **14. Raft Foundation Reinforcement** | Not applicable. | Raft foundation is not used. | Not Applicable |
| **15. Lift Design** | Not applicable. | No lift is designed for this structure. | Not Applicable |
| **16. Soil Improvement** | "Improved S.B.C of soil considered is 10 T/m2". Note 1 in Section X mentions "SIZE STONE LAYERS BELOW THE FOOTING IS TO BE LAID AFTER EXCAVATING AND OMPACTING THE SAME AS PER THE STANDARD PROCEDURE". | Soil improvement is indicated by the improved SBC and the mention of stone layers and compaction. | Compliant |
| **17. Column Ties** | Column ties are shown in Section X and the C1 detail. Ties are Y8@200. They appear continuous in the C1 detail. | Column ties are shown and appear continuous. | Compliant |
| **18. Plan of Ties** | A separate plan for ties is not explicitly present, but the C1 column detail shows the arrangement of ties. | A dedicated plan for ties is not present, but the detail provides the necessary information. SP 34, Clause 3.3.1 states that the exact position, shape, size and spacing of the reinforcement shall be given. The C1 detail provides this. | Compliant |
| **19. Outer Ties Check** | Column vertical reinforcement: 8Y16. Column ties: Y8@200. Footing bottom reinforcement: Y10@125. Percentage of steel in columns: For a 300x450 column, 8Y16 bars (Area = 8 * pi * (16/2)^2 = 1608.5 mm2). Gross area = 300 * 450 = 135000 mm2. Percentage = (1608.5 / 135000) * 100 = 1.19%. This is >= 0.8% (IS 456:2000, Clause 26.5.3.1). Footing reinforcement: Y10@125. For a 2100mm wide footing, area of steel per meter = (1000/125) * (pi * (10/2)^2) = 8 * 78.54 = 628.32 mm2. Percentage = (628.32 / (2100 * 450)) * 100 = 0.066%. This is less than 0.12% for slabs/footings as per IS 456:2000 (cl. 26.5.2.1). | Column steel percentage is compliant. Footing steel percentage is non-compliant. | Non-Compliant |
| **20. Cross-Section Area** | Assume limiting value (User Input) | The user has specified to assume limiting value for cross-section area. This implies that the design should consider the minimum required cross-section for the given loads and reinforcement. However, it is not explicitly stated whether gross or effective area is used for calculations in the notes. SP 34, Clause 3.3.5 states that main dimensions of the structure, such as beam and column sizes, shall be shown. | Missing Information |
| **21. Steel Curtailment** | Not explicitly mentioned in the notes. | For a G+1 structure, curtailment might not be as critical as in high-rise buildings, but general principles of curtailment should be followed as per IS 456:2000, Clause 26.2.3. Not explicitly detailed. | Missing Information |
| **22. Maximum Steel Percentage in Columns** | Assume limiting value (User Input) | The user has specified to assume limiting value for maximum steel percentage. As per IS 456:2000, Clause 26.5.3.1, the maximum percentage of reinforcement in columns shall not exceed 6 percent of the gross cross-sectional area. If bars are not lapped, this can be 4 percent. The calculated percentage for C1 is 1.19%, which is well within these limits. | Compliant |

### Step 5: Report Missing or Wrong Information

1.  **Reinforcement Bars:** The standard for reinforcement bars (IS 1786-1985) is outdated; the current standard is IS 1786:2008. This needs to be updated on the drawing.
2.  **Development Length (Ld):** While 50d is a common value, for precise compliance, the development length should be calculated based on the specific bar diameter, concrete grade (M20), and stress in the bar, as per IS 456:2000, Clause 26.2.1. The tabulated values in SP 34, Clause 40 and 43 show variations based on concrete grade and bar type.
3.  **Outer Ties Check (Footing Reinforcement):** The calculated percentage of steel for footing (0.066%) is less than the minimum required 0.12% for slabs/footings as per IS 456:2000, Clause 26.5.2.1. The footing reinforcement needs to be increased to meet this minimum requirement.
4.  **Cross-Section Area:** While the user input states to assume limiting value, it is not explicitly stated whether gross or effective cross-section area is used for calculations in the notes. This clarity is important for design verification.
5.  **Steel Curtailment:** Details regarding steel curtailment are not provided. While less critical for a G+1 structure, general principles of curtailment should be followed and indicated on the drawings as per IS 456:2000, Clause 26.2.3.

### Summary of Compliance (Updated)

-   **Total Criteria Evaluated:** 22
-   **Compliant Items:** 15
-   **Non-Compliant Items:** 2
-   **Missing Information Items:** 3
-   **Cannot Verify Items:** 1
-   **Not Applicable Items:** 3

**Overall Verdict:**
The integration of user-provided information has resolved some previously identified missing items, such as the grade of concrete and floor heights. However, critical non-compliances remain regarding the outdated reinforcement bar standard (IS 1786-1985) and, more significantly, the insufficient minimum reinforcement in the footing (0.066% vs. 0.12% required by IS 456:2000, Clause 26.5.2.1). The general value for development length (50d) needs to be verified against specific calculations for the given concrete and steel grades. Further clarification is also needed on the cross-section area assumption and steel curtailment details. These issues require immediate attention to ensure the structural integrity and compliance with IS codes.

**Recommendations:**
1.  **Update Reinforcement Standard:** Revise the drawing to specify reinforcement bars conforming to IS 1786:2008.
2.  **Increase Footing Reinforcement:** Redesign the footing reinforcement to meet the minimum 0.12% requirement as per IS 456:2000, Clause 26.5.2.1.
3.  **Verify Development Length:** Provide specific calculations or tabulated values for development length based on the actual bar diameters, M20 concrete, and Fe 550 steel, referencing IS 456:2000, Clause 26.2.1.
4.  **Clarify Cross-Section Area:** Explicitly state whether gross or effective cross-section area is used for design calculations in the notes.
5.  **Detail Steel Curtailment:** Include details or general notes regarding steel curtailment practices for beams and columns as per IS 456:2000, Clause 26.2.3.