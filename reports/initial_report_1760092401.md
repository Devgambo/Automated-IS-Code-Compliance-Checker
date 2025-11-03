The following compliance analysis of the provided Reinforced Concrete Cement (RCC) structural drawing is performed based on the requirements and standards detailed in **IS 456:2000** (Plain and Reinforced Concrete - Code of Practice) and **SP 34** (Handbook on Concrete Reinforcement and Detailing).

**AI Model Used:** Gemini 2.5 Pro

---

## Step 0: Initial Document Check

| Criteria | Result | Status |
| :--- | :--- | :--- |
| **0.1 RCC Structural Drawing** | Document shows foundation layout, footing schedule, column schedules, and typical sections. | Compliant |
| **0.2 Site Location** | Consultant location: Mangaluru, Karnataka. Site location is not explicitly stated, but the PWD Belthangady and Mangaluru presence suggests the site is likely in District Dakshina Kannada, Karnataka. | Missing Information (Flagged) |
| **0.3 Compliance Standard** | Checks are strictly based on IS 456:2000 and SP 34. | Compliant |

---

## Step 1, 2 & 3: Extraction and Verification of Design Parameters

The "NOTES" section is clearly visible on the lower right side of the drawing. The parameters are extracted and checked below:

| Criteria | Extracted Value | Compliance Check (IS 456:2000 / SP 34) | Status |
| :--- | :--- | :--- | :--- |
| **1. Grade of Concrete** | M25 for all R.C.C. works. | M25 is suitable for Moderate to Severe exposure conditions. Without the site's environmental zone, full compliance cannot be verified, but M25 is a good minimum standard. | Compliant (Conditional) |
| **2. Reinforcement Bars** | HYSD TMT bars of grade Fe 500 (conforming to IS 1786-1985). | Fe 500 is a standard, high-strength reinforcement grade. | Compliant |
| **3. Lap Length** | 50 times bar diameter ($50d$). Lapping staggered, not more than 50% of bars lapped at a section. | $50d$ is a standard, conservative practice and generally compliant with IS 456:2000 requirements for compression/tension lap length when detailed fully. Staggering requirement (<=50%) is compliant. | Compliant |
| **4. Clear Cover (Column)** | $40 \text{ mm}$ | IS 456:2000 requires a minimum of $40 \text{ mm}$ for columns (or bar diameter, whichever is greater). $40 \text{ mm}$ is compliant. | Compliant |
| **4. Clear Cover (Footing / Wall)** | $50 \text{ mm}$ | IS 456:2000 requires a minimum of $50 \text{ mm}$ for footings resting directly on soil. The typical section shows $~150 \text{ mm}$ PCC specified, justifying the $50 \text{ mm}$ cover. | Compliant |
| **4. Clear Cover (Slab)** | $20 \text{ mm}$ | IS 456:2000 specifies a minimum of $20 \text{ mm}$ for slabs, often conditioned by environmental exposure. This is the minimum compliant value. | Compliant |
| **4. Clear Cover (Beam)** | $25 \text{ mm}$ | IS 456:2000 minimum is often $25 \text{ mm}$ or $30 \text{ mm}$ depending on exposure. $25 \text{ mm}$ is generally acceptable for Moderate exposure. | Compliant |
| **5. Development Length ($L_d$)** | $50$ times the dia. of the bar ($50d$). | $50d$ is a conservative and accepted value for development or anchorage length when not explicitly calculated using IS 456:2000 Clause 26.2.1. | Compliant |
| **6. Safe Bearing Capacity (SBC) of soil** | $12.5 \text{ T/m}^2$ (or $125 \text{ kN/m}^2$) considered. | The value is extracted. The SBC is adequate for the design shown (low-to-medium rise structure). | Compliant |
| **7. Seismic Zone and Wind Load** | Seismic Zone III (IS 1893:2016) and Wind Forces (IS 875:2015). | Extraction confirms mandatory seismic and wind data are included (Zone III is mentioned). | Compliant |
| **8. Building Limitations** | Designed for Ground Floor $+2$ Storeys only. | Explicit limitation provided. | Compliant |
| **9. Structure's Purpose** | NH Office (Foundation Layout). | Explicit purpose provided. | Compliant |
| **10. Floor Heights** | Plinth to First Floor - $3.6 \text{ M}$, First Floor to Second Floor - $3.6 \text{ M}$, Second Floor to Terrace - $3.6 \text{ M}$. | Heights are extracted ($3600 \text{ mm}$). | Compliant |
| **11. Schedule of Footings** | "SCHEDULE OF FOOTINGS" table is present and consistent with RF1, RF2, and F1 marks. | Table is present. | Compliant |
| **12. Footing Type** | Raft foundations (RF1, RF2) and Isolated footing (F1). | Raft foundations are specified for large areas, consistent with typical foundation practice. F1 is small isolated footing shown at the corner. | Compliant |
| **13. Reinforcement in High-Rise Buildings** | Top and bottom reinforcement shown for Raft Footings (RF1/RF2). | Top reinforcement (needed for uplift/differential settlement) is explicitly included in the schedule for both rafts. | Compliant |
| **14. Raft Foundation Reinforcement** | RF1: Top (Y12@125 / Y16@150), Bottom (Y12@125 / Y16@125). RF2: Top (Y12@125 / Y16@125), Bottom (Y12@125 / Y16@125). | Both top and bottom reinforcement are specified. | Compliant |
| **15. Lift Design (Pit)** | A central "LIFT PIT" is explicitly shown in the plan. Section $\text{X}-\text{X}1$ shows the lift pit depth and wall detail. | Lift pit is shown (depth appears adequate, $\sim 1.5 \text{ M}$ below GL). | Compliant |
| **15. Lift Design (Steel Bending)** | Lift pit cross-section shows vertical bars bent into the base slab. | Detailing appears generally consistent with SP 34 practices for continuity. | Compliant |
| **16. Soil Improvement** | Section $\text{X}-\text{X}$ shows $150 \text{ mm}$ PCC below the foundation and $90 \text{ to } 40 \text{ mm}$ size boulders compacted with sand/quarry dust below the PCC. | Soil support methods are detailed. | Compliant |
| **17. Column Ties** | Column schedules show $Y8@200$ ties. Ties are shown as rectangular or polygonal (C1 to C7 schedules). | Ties are specified. Detailing shows clear tie configuration looping around the main bars. | Compliant |
| **18. Plan of Ties** | No separate dedicated plan of ties is present; schematic configuration is provided within the column schedules. | While ideal, the schematic in C1-C7 sketches often suffices for detailing small projects. | Acceptable |
| **19. Outer Ties Check (Column)** | Column schedules indicate steel percentages: e.g., C1 (12Y16 $\approx$ $12 \times 201 = 2412 \text{ mm}^2$ area, Column $300 \times 450 = 135000 \text{ mm}^2$). Percentage varies between 1.7%-2.3% (well above 0.8% min). Footing steel (RF1/RF2) is also well above $0.12\%$ min. | Compliant |
| **20. Cross-Section Area** | Dimensions ($300 \times 450 \text{ mm}, 300 \times 525 \text{ mm}$) based on gross cross-section for columns. Steel area calculated based on effective area. | Standard practice followed. | Compliant |
| **21. Steel Curtailment** | Column schedules show different reinforcement for 'Foundation to Second Floor LVL' vs. 'Second Floor to Terrace LVL'. E.g., C1: $12\text{Y}16$ (lower) vs. $6\text{Y}16(\text{d}) + 8\text{Y}12$ (upper). | Curtailment (reduction in steel quantity/diameter) is specified for upper floors, which is standard practice for multi-storey buildings. | Compliant |
| **22. Maximum Steel Percentage in Columns** | Max steel percentage observed is $\approx 2.3\%$ (C1, $\text{Fnd} \to \text{2nd}$). This is well below the $4\%$ if lapped, and $6\%$ overall maxima stipulated in IS 456:2000. | Compliant |

---

## Missing or Wrong Information

The drawing generally adheres to fundamental IS 456:2000 and SP 34 practices, especially regarding clear cover, lap/development lengths, and minimum reinforcement standards. However, the following mandatory or crucial information is missing:

1.  **Site Environmental Exposure Condition (Mandatory for IS 456:2000):**
    - The actual site location is not explicitly listed (only PWD locations are mentioned).
    - Without a confirmed exposure condition (e.g., Severe or Very Severe, typical for coastal areas like Mangaluru), it is impossible to verify if **M25 concrete grade** is adequate, or if the **clear cover values ($20 \text{ mm}$ for slab, $25 \text{ mm}$ for beam)** meet the specific IS 456:2000 durability requirements for the site's environmental zone.

2.  **Safe Bearing Capacity (SBC) Source:**
    - SBC ($12.5 \text{ T/m}^2$) is stated as "considered," but there is no reference to a mandatory **Geo-Technical Investigation Report (Soil Test Report)**. This report is required to validate both the SBC value and the soil profile depicted (or $1500 \text{ mm}$ depth to hard strata for the tie beam shown in Section X).

3.  **IS Code for Reinforcement (Minor Flag):**
    - The note refers to Fe 500 conforming to **IS 1786-1985**. While Fe 500 is standard, the current version referenced should typically be the latest revision (or the version valid at the time of design), though the grade definition itself is likely consistent.