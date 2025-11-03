The following analysis is based on the provided RCC structural drawing (Foundation Plan and Details) and the compliance requirements stipulated by IS 456 on the Design of Structures (Plain and Reinforced Concrete) and SP 34 (Handbook on Concrete Reinforcement and Detailing).

**AI Model Used:** Gemini 2.5 Pro

***

## Step 0: Initial Document Check

| Criteria | Extracted Value | Compliance Check | Status |
| :--- | :--- | :--- | :--- |
| **0.1 Document Type** | "FOUNDATION PLAN AND DETAILS" (RCC Drawing) | Confirmed. | **PASS** |
| **0.2 Site Location** | Project: MORARJI DESAI SCHOOL QUARTERS (Location not specified; Consultant located in Mangalore) | Site location (e.g., city/district) is required to verify specific environmental exposure mandates (IS 456:2000, Table 3) and seismic zone criteria. | **MISSING** |
| **0.3 Compliance Standard** | IS 456:2000 and SP 34 | All checks are based solely on these codes. | **PASS** |

***

## Step 1, 2, & 3: Locate, Extract, and Verify Design Parameters

The analysis extracts and verifies parameters found within the "NOTES" section of the drawing.

| Criteria | Extracted Value | Compliance Check & IS/SP Mandate | Status |
| :--- | :--- | :--- | :--- |
| **1. Grade of Concrete** | M25 for all R.C.C. works. | M25 is a suitable minimum grade for general RCC structures (IS 456:2000 Cl 9.1). **Cannot fully verify suitability** without the site's environmental exposure classification (e.g., Severe, Very Severe). | **CONDITIONAL PASS** (Exposure check pending site data) |
| **2. Reinforcement Bars** | HYSD TMT Bars of Grade Fe 500, conforming to IS 1786-1985. | Fe 500 is standard and complies with recommended grades. | **PASS** |
| **3. Lap Length** | 50 times dia of the bar (50d). Must be staggered, with not more than 50% of bars lapped at a section. | **Compliance:** IS 456:2000 Cl 26.2.5 (Development Length) and SP 34. 50d is acceptable for tension/compression lap. The staggering rule (max 50% lapped at one section) is excellent practice for strength continuity. | **PASS** |
| **4. Clear Cover - Footing/Wall** | 50 mm | **Compliance:** IS 456:2000 Table 16 specifies a minimum of 50 mm for foundations. This complies with the minimum. If exposure is 'Severe' or 'Very Severe', a larger cover (e.g., 75 mm) would be needed, or adequate environmental protection specified. | **CONDITIONAL PASS** (Meets minimum, but needs exposure check) |
| **4. Clear Cover - Column** | 40 mm | **Compliance:** IS 456:2000 Table 16 specifies a minimum of 40 mm, or bar diameter, whichever is greater. Range 40mm-70mm is suitable. | **PASS** |
| **4. Clear Cover - Slab**| 20 mm | **Compliance:** IS 456:2000 Table 16 minimum 20 mm, or bar diameter, whichever is greater. Standard practice for slabs. | **PASS** |
| **4. Clear Cover - Beam**| 25 mm | **Compliance:** IS 456:2000 Table 16 minimum 25 mm, or bar diameter, whichever is greater. Standard practice for beams. | **PASS** |
| **5. Development Length (Ld)** | 50 times the dia of the bar (50d). | **Compliance:** Development length (Ld) is calculated as $\phi \cdot \sigma_s / (4 \cdot \tau_{bd})$ (IS 456:2000 Cl 26.2.1). The value of $50d$ is often used as a conservative design approximation for tension bars in Fe 500 and is acceptable if calculation details are not specified. | **PASS** |
| **6. Safe Bearing Capacity (SBC) of soil** | 20 T/m$^2$ | SBC is noted. PCC is specified in the details (Section X and Typical Plan of Footing with Pedestal) as 50mm P.C.C. The SBC value is noted for stability checks. | **PASS** |
| **7. Seismic Zone and Wind Load** | Not specified in NOTES or GENERAL NOTES. | This information is mandatory for structural integrity verification under IS 1893 (Seismic) and IS 875 (Wind). | **MISSING** |
| **8. Building Limitations** | Structure is designed for Ground + 3 Stories only. | Defines the project scope (low to medium-rise). | **PASS** |
| **9. Structure's Purpose** | MORARJI DESAI SCHOOL QUARTERS | Confirmed. | **PASS** |
| **10. Floor Heights** | Basement, Ground, First, Second, Terrace. Heights are shown: Ground to First (3.0M), First to Second (3.0M), Second to Terrace (3.0M). | Floor heights are dimensioned. | **PASS** |
| **11. Schedule of Footings** | Present (F1 to F6, CF1, F4A, F5A, F5B). | A detailed "SCHEDULE OF FOOTINGS" table is present and referenced. | **PASS**|
| **12. Footing Type** | Isolated spread footings (F1-F6) with some combined or strap footings (CF1, F5A/F5B, indicated by layout). | Suitable for the specified Ground + 3 story structure. | **PASS** |
| **13. Reinforcement in Upper Floors (Curtailment)** | The column schedule shows a reduction in steel reinforcement quantity/diameter from the Foundation level up to the Terrace. | Example: C1 moves from 12Y12 (Foundation to F1) to 6Y16+6Y12(e) (F1 to F3). This indicates appropriate curtailment/optimization. | **PASS** |
| **14. Raft Foundation Reinforcement** | Raft foundation is not used. (Isolated footings are used.) | Not Applicable (N/A) | **N/A** |
| **15. Lift Design** | A LIFT PIT is shown (Section X1, Grid CF1). Dimensions: 1500 mm MIN. or as per Arch. drawing. | Minimum 1500mm depth specified. This is standard requirement for hydraulic or traction lifts. | **PASS** |
| **16. Soil Improvement** | Not specified. (The drawing relies on 20 T/m$^2$ SBC.) | Not specified. | **MISSING** |
| **17. Column Ties** | Column ties are specified in the column schedule (e.g., Y8@200). Ties are shown as rectangular links in the typical column cross-sections. | Ties are continuous links, complying with the requirement for shear/confinement reinforcement. | **PASS** |
| **18. Plan of Ties** | Not a separate plan, but details integrated into the Column Schedule graphics. | Sufficient for detailing. | **PASS** |
| **19. Outer Ties and Steel Percentage** | Outer ties are specified by spacing (e.g., Y8@200). Percentage check requires calculation. Max % steel in columns for C1 (Foundation): 12x $\pi/4 \cdot 12^2 = 1357.17$ mm$^2$. Column size is 450x450 mm $\implies Area_{gross} = 202500$ mm$^2$. $1357.17/202500 \approx 0.67\%$. | The minimum steel required for columns is 0.8% (IS 456:2000 Cl 26.5.3.1). The calculated percentage (0.67%) for C1 in the foundation level, based on the *schedule*, is **less** than the mandated 0.8%. | **FAIL** (Minimum steel requirement) |
| **20. Cross-Section Area** | Gross cross-section area used for column calculations. | Standard IS 456 practice. | **PASS** |
| **21. Steel Curtailment** | Yes, steel size/number decreases with height (See Criterion 13). | **PASS** |
| **22. Maximum Steel Percentage in Columns** | Max % used is 0.67% (C1 at foundation). | The maximum allowed is 6% (or 4% when lapping is present, IS 456:2000 Cl 26.5.3.1). The design is well within the limit. | **PASS** |

***

## Missing or Wrong Information

The following items are flagged as either missing from the drawing notes, cannot be verified, or violate the mandates of IS 456:2000:

1.  **Site Location for Exposure Classification:** The specific location *of the site* is missing. Necessary to classify the environmental exposure (Table 3, IS 456:2000) to ensure the M25 grade and clear covers (50mm for footing) are adequate (Step 0.2, Step 2.1).
2.  **Seismic Zone and Wind Load:** Critical design data (IS 1893:2002 and IS 875) for lateral load resistance is entirely missing from the notes. This information is mandatory for a compliant structural design (Step 2.7).
3.  **Minimum Steel in Columns (C1):** The calculated reinforcement percentage for Column C1 (Foundation to First Floor) in the schedule (0.67%) is **below the minimum standard** requirement of 0.8% of the gross cross-sectional area as per IS 456:2000, Clause 26.5.3.1. This must be corrected by increasing the bar diameter or count.