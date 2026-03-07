# 🇺🇸 JEP Colorado Solutions

**AI Accountability for the State of Colorado**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/downloads/)
[![Colorado AI Act](https://img.shields.io/badge/SB%2024--205-Compliance-blue)](https://leg.colorado.gov/bills/sb24-205)

## 📋 Overview

This directory provides a complete **Judgment Event Protocol (JEP)** implementation aligned with Colorado's **Artificial Intelligence Act (SB 24-205)** , the first comprehensive state law in the United States regulating algorithmic discrimination in high-risk AI systems.

### Why Colorado Matters

| Reason | Significance |
|--------|--------------|
| **First Comprehensive State AI Law** | Colorado is the pioneer in US AI regulation |
| **Effective Date** | **June 30, 2026** - only 3 months away |
| **Safe Harbor Provision** | NIST AI RMF compliance provides legal protection |
| **Consequential Decisions Coverage** | 7 critical areas: employment, financial, housing, healthcare, education, legal, government |
| **National Trendsetter** | Other states are following Colorado's model |

## 🎯 Colorado AI Act (SB 24-205) Requirements

| Requirement | Description | JEP Implementation | Verification |
|-------------|-------------|-------------------|--------------|
| **Risk Assessments** | Annual impact assessments for high-risk AI systems | `conduct_risk_assessment()` with fairness metrics | `verify-colorado.py --risk` |
| **Reasonable Care** | Prevent algorithmic discrimination | Bias testing + continuous monitoring | `verify-colorado.py --care` |
| **Consumer Disclosures** | Notice when AI influences decisions | `is_ai_generated` + `human_review_available` | `verify-colorado.py --disclosure` |
| **Adverse Explanations** | Principal reasons for adverse outcomes | `principal_reasons` + `explanation` | `verify-colorado.py --explanation` |
| **Correction Rights** | Opportunity to correct incorrect data | Correction logs + versioning | `verify-colorado.py --correction` |
| **Appeal Rights** | Human review of adverse decisions | Appeal workflow + escalation | `verify-colorado.py --appeal` |
| **Developer Documentation** | Documentation for deployers | Model cards + dataset cards | `verify-colorado.py --docs` |
| **Public Statements** | Summary of AI systems and risk management | JSON-LD machine-readable | `verify-colorado.py --public` |
| **NIST AI RMF Alignment** | Safe harbor for deployers | Complete NIST mapping | `verify-colorado.py --nist` |

## 📊 Consequential Decisions Covered

| Category | Examples | JEP Solution |
|----------|----------|--------------|
| **Employment** | Hiring, promotion, termination | [employment.py](examples/employment.py) |
| **Financial Services** | Credit, lending, insurance | [financial.py](examples/financial.py) |
| **Housing** | Rentals, mortgages, evictions | [housing.py](examples/housing.py) |
| **Healthcare** | Diagnosis, treatment, insurance | [healthcare.py](examples/healthcare.py) |
| **Education** | Admissions, scholarships | [education.py](examples/education.py) |
| **Legal Services** | Access to legal representation | [legal.py](examples/legal.py) |
| **Government Benefits** | Eligibility determinations | [government.py](examples/government.py) |

## 🏛️ Safe Harbor Provision

Under the Colorado AI Act, deployers who implement a risk management policy aligned with the **NIST AI Risk Management Framework** or **ISO/IEC 42001** receive a **rebuttable presumption of reasonable care**. JEP provides complete NIST mapping to help Colorado businesses qualify for this safe harbor.

## 🚀 Quick Start

```python
from jep.us.colorado import ColoradoAITracker

# Initialize tracker for a deployer
tracker = ColoradoAITracker(
    entity_type="deployer",  # or "developer"
    organization="Colorado Company"
)

# Log a consequential decision
decision = tracker.log_consequential_decision(
    system_id="HR-001",
    consumer_id="CONS-123",
    decision_type="employment",
    decision="REJECT",
    principal_reasons=[
        "Work experience below minimum threshold",
        "Skills assessment score below threshold"
    ],
    ai_was_determining_factor=True,
    human_review_available=True,
    appeal_rights_provided=True
)

# Conduct annual risk assessment
assessment = tracker.conduct_risk_assessment(
    system_id="HR-001",
    fairness_metrics={
        "disparate_impact": 0.98,
        "demographic_parity": 0.97
    },
    bias_test_results={
        "race": "PASS",
        "gender": "PASS"
    },
    residual_risk="LOW"
)
```

## 📁 Repository Structure

```
colorado/
├── README.md                          # This file
├── sb-24-205/                          # Colorado AI Act
│   ├── README.md                        # Act overview
│   ├── mapping.md                        # Detailed mapping
│   ├── implementation/
│   │   └── colorado_tracker.py            # Core implementation
│   └── examples/                          # Industry examples
│       ├── employment.py
│       ├── financial.py
│       ├── housing.py
│       ├── healthcare.py
│       ├── education.py
│       ├── legal.py
│       └── government.py
└── tests/
    └── verify-colorado.py                 # Verification script
```

## 🔍 Verification

```bash
# Run complete Colorado AI Act verification
python tests/verify-colorado.py

# Output:
# ========================================
# COLORADO AI ACT COMPLIANCE VERIFICATION
# ========================================
# ✅ Risk Assessments: Annual impact assessments ready
# ✅ Reasonable Care: Bias testing + monitoring active
# ✅ Consumer Disclosures: Pre-decision notice implemented
# ✅ Adverse Explanations: Principal reasons provided
# ✅ Correction Rights: DSAR workflow ready
# ✅ Appeal Rights: Human review available
# ✅ Developer Documentation: Model cards complete
# ✅ Public Statements: JSON-LD disclosures published
# ✅ NIST Alignment: Safe harbor qualification ready
# ========================================
# FULL COMPLIANCE VERIFIED
# ========================================
```

## 📚 References

- [Colorado SB 24-205 - Artificial Intelligence Act](https://leg.colorado.gov/bills/sb24-205)
- [Colorado Attorney General AI Guidance](https://coag.gov/ai)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

## 📬 Contact

For Colorado-specific inquiries:
- **Email**: colorado@humanjudgment.org
- **GitHub**: [hjs-spec/jep-us-solutions](https://github.com/hjs-spec/jep-us-solutions)

---

*Last Updated: March 2026*
*Supporting Colorado's leadership in AI governance*
```
