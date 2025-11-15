## RCC Structural Drawing Compliance Report - Foundations

**Project:** Malpe Fishery Harbour, Udupi (Original Site) / Kutch, Gujarat (New Input)
**Drawing Type:** Foundations
**Compliance Standards:** IS 456:2000, SP 34

---

### User's New Input:
*   **Site:** Kutch, Gujarat
*   **Reinforcement Bars:** Fe 550D
*   **Floor Height:** 11m

---

### Step 0: Initial Document Check
-   **0.1:** The document is an RCC structural drawing of "FOUNDATIONS" only.
-   **0.2:** Site Location: Kutch, Gujarat (Updated from Malpe Fishery Harbour, Udupi).
-   **0.3:** All compliance checks are based only on IS 456:2000 and SP 34.

### Step 1: Locate the "NOTES" Section
-   **Status:** Compliant

### Step 2 & 3: Extract and Verify Design Parameters from "NOTES"

| Criteria | Extracted Value | Compliance Check | Status |
|---|---|---|---|
| **1. Grade of Concrete** | M25 | For Kutch, Gujarat (seismic zone V as per IS 1893:2016), and considering potential for aggressive environments (e.g., coastal proximity if applicable, though not specified for Kutch), M25 might be acceptable for moderate exposure. However, for structures in seismic zones IV and V, IS 456:2000, Table 5, often recommends higher grades for durability and seismic performance. Without specific environmental exposure classification for Kutch, it's difficult to definitively confirm compliance. | Cannot Verify |
| **2. Reinforcement Bars** | HYSD TMT Bars, Grade Fe 550, conforming to IS 1786-1985. Column vertical reinforcement: 8Y16. Column ties: Y8@200. Footing bottom reinforcement: Y10@125. **User Input:** Fe 550D. | The user input of Fe 550D is a specific grade of high-strength deformed bars. The original drawing specified Fe 550. Both Fe 550 and Fe 550D are high-strength grades. However, the standard IS 1786-1985 is outdated; the current standard is IS 1786:2008. SP 34, Clause 1.1.1, refers to mild steel and medium tensile steel bars, but modern practice uses HYSD bars. The use of Fe 550D is generally good practice for ductility. | Non-Compliant |
| **3. Lap Length** | 50 times dia of the bar, not more than 50% of bars are lapped at a section. | 50d is a common and generally compliant value for lap length in tension for Fe 500/550 grades with M25 concrete (referencing SP 34, Clause 43 for Fe 500, M25, 16mm bar, tension Ld = 77.7 cm or 777mm, which is approx 48.5d. 50d is conservative). The staggering requirement is also good practice. | Compliant |
| **4. Clear Cover** | Footing/Wall: 50 mm, Columns: 40 mm, Slab: 25 mm, Beam: 30 mm. | Footing cover of 50mm is the minimum as per IS 456:2000, Clause 26.4.2.2. The drawing shows 150mm PCC below the footing, which is good practice for a 50mm cover. Column cover of 40mm is compliant as per IS 456:2000, Clause 26.4.2.1 (minimum 40mm or bar diameter, whichever is greater). Slab and beam covers are also generally compliant for normal exposure conditions (IS 456:2000, Clause 26.4.2.1). SP 34, Clause 11.8.4.6, specifies 50mm for columns and 40mm for beams. | Compliant |
| **5. Development Length (Ld)** | 50 times the dia. of the bar. | 50d is a common and generally compliant value for development length. For Fe 500/550 and M25 concrete, the required development length for tension bars is approximately 48.5d (from SP 34, Clause 43, for Fe 500, M25, 16mm bar, Ld = 77.7 cm). 50d is a conservative and acceptable value. | Compliant |
| **6. Safe Bearing Capacity (SBC) of soil** | 10 T/m2 (100 kN/m2). PCC is mentioned (150mm thick). | SBC is mentioned. PCC is specified. SP 34, Clause 3.3.3, states that information regarding the underside conditions, such as the thickness of blinding (PCC), should be shown. | Compliant |
| **7. Seismic Zone and Wind Load** | Seismic Zone III and Wind Forces as per IS 1893:2016 & IS 875:2015 respectively. | **User Input:** Site is Kutch, Gujarat. Kutch falls under Seismic Zone V as per IS 1893:2016. The drawing specifies Seismic Zone III, which is incorrect for Kutch. This is a critical non-compliance. | Non-Compliant |
| **8. Building Limitations** | Structure is designed for Ground + 1 Storey + Lightweight Roof. | Building limitations are specified. | Compliant |
| **9. Structure's Purpose** | Entrance Gate and Guard Room. | The purpose of the structure is mentioned. | Compliant |
| **10. Floor Heights** | Not explicitly mentioned in the "NOTES" section. "First Floor to Terrace Lvl" is indicated in the column detail, but specific floor heights are not listed. **User Input:** 11m. | The user input provides a total floor height of 11m. This clarifies the overall height of the structure. SP 34, Clause 3.3.5, states that main dimensions of the structure, such as heights between floors, should be shown. | Compliant |
| **11. Schedule of Footings** | Present and consistent with F1 footing details. | A "SCHEDULE OF FOOTINGS" table is present and provides dimensions and reinforcement for F1. | Compliant |
| **12. Footing Type** | Isolated footings (F1). | Isolated footings are used for a Ground + 1 Storey structure, which is appropriate. | Compliant |
| **13. Reinforcement in High-Rise Buildings** | Not applicable. | The structure is Ground + 1 Storey, not a high-rise building. | Not Applicable |
| **14. Raft Foundation Reinforcement** | Not applicable. | Raft foundation is not used. | Not Applicable |
| **15. Lift Design** | Not applicable. | No lift is designed for this structure. | Not Applicable |
| **16. Soil Improvement** | "Improved S.B.C of soil considered is 10 T/m2". Note 1 in Section X mentions "SIZE STONE LAYERS BELOW THE FOOTING IS TO BE LAID AFTER EXCAVATING AND OMPACTING THE SAME AS PER THE STANDARD PROCEDURE". | Soil improvement is indicated by the improved SBC and the mention of stone layers and compaction. | Compliant |
| **17. Column Ties** | Column ties are shown in Section X and the C1 detail. Ties are Y8@200. They appear continuous in the C1 detail. | Column ties are shown and appear continuous. SP 34, Clause 11.8.4.5, states that the maximum spacing of longitudinal bars should not be more than 150mm, which implies appropriate tie spacing to hold them. | Compliant |
| **18. Plan of Ties** | A separate plan for ties is not explicitly present, but the C1 column detail shows the arrangement of ties. | A dedicated plan for ties is not present, but the detail provides the necessary information. SP 34, Clause 3.3.1, requires the exact position, shape, size, and spacing of reinforcement to be given. The detail fulfills this. | Compliant |
| **19. Outer Ties Check** | Column vertical reinforcement: 8Y16. Column ties: Y8@200. Footing bottom reinforcement: Y10@125. Percentage of steel in columns: For a 300x450 column, 8Y16 bars (Area = 8 * pi * (16/2)^2 = 1608.5 mm2). Gross area = 300 * 450 = 135000 mm2. Percentage = (1608.5 / 135000) * 100 = 1.19%. This is >= 0.8% (IS 456:2000, Clause 26.5.3.1). Footing reinforcement: Y10@125. For a 2100mm wide footing, area of steel per meter = (1000/125) * (pi * (10/2)^2) = 8 * 78.54 = 628.32 mm2. Percentage = (628.32 / (2100 * 450)) * 100 = 0.066%. This is less than 0.12% for slabs/footings as per IS 456:2000 (cl. 26.5.2.1). | Column steel percentage is compliant. Footing steel percentage is non-compliant. | Non-Compliant |
| **20. Cross-Section Area** | Not explicitly stated whether gross or effective area is used for calculations in the notes. | This information is not explicitly mentioned in the notes. | Missing Information |
| **21. Steel Curtailment** | Not explicitly mentioned in the notes. | For a G+1 structure, curtailment might not be as critical as in high-rise buildings, but general principles of curtailment should be followed. Not explicitly detailed. | Missing Information |
| **22. Maximum Steel Percentage in Columns** | Not explicitly mentioned in the notes. Calculated percentage for C1 is 1.19%, which is well within the 6% (or 4% with lapping) limit (IS 456:2000, Clause 26.5.3.1). | The maximum percentage is not stated in the notes, but the calculated value is compliant. | Missing Information |

### Summary of Compliance

-   **Total Criteria Evaluated:** 22
-   **Compliant Items:** 12
-   **Non-Compliant Items:** 3
-   **Missing Information Items:** 3
-   **Cannot Verify Items:** 1
-   **Not Applicable Items:** 3

### Missing or Wrong Information

1.  **Grade of Concrete:** Cannot verify compliance without specific environmental exposure classification for Kutch, Gujarat. M25 might be insufficient for severe/very severe coastal conditions or highly seismic regions (Zone V).
2.  **Reinforcement Bars Standard:** The standard for reinforcement bars (IS 1786-1985) is outdated; the current standard is IS 1786:2008. This needs to be updated in the drawing notes.
3.  **Seismic Zone:** The drawing specifies Seismic Zone III, which is incorrect for Kutch, Gujarat. Kutch falls under Seismic Zone V as per IS 1893:2016. The design must be revised to comply with Zone V requirements.
4.  **Outer Ties Check (Footing Reinforcement):** The calculated percentage of steel for footing (0.066%) is less than the minimum required 0.12% for slabs/footings as per IS 456:2000 (Clause 26.5.2.1). This is a critical non-compliance and requires an increase in footing reinforcement.
5.  **Cross-Section Area:** It is not explicitly stated whether gross or effective cross-section area is used for calculations. This should be clarified in the notes.
6.  **Steel Curtailment:** Details regarding steel curtailment are not provided. While the structure is small, general principles of curtailment should be followed and indicated.
7.  **Maximum Steel Percentage in Columns:** The maximum steel percentage allowed in columns is not explicitly stated in the notes. While the calculated value is compliant, it's good practice to state design limits.

### Overall Verdict:

The integration of user input has clarified some previously missing information, such as the floor height. However, it has also highlighted a critical non-compliance regarding the **Seismic Zone** for Kutch, Gujarat, which is Zone V, not Zone III as stated in the drawing. This necessitates a complete re-evaluation of the structural design for seismic forces. Additionally, the **footing reinforcement percentage** remains non-compliant with IS 456:2000, and the **reinforcement bar standard** is outdated. These issues, particularly the seismic zone discrepancy and insufficient footing reinforcement, are significant and require immediate attention and revision of the structural design and drawings to ensure safety and compliance with Indian Standards.