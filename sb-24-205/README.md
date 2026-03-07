# 🇺🇸 Colorado Artificial Intelligence Act (SB 24-205)

**Complete Technical Implementation for the First Comprehensive US State AI Law**

## 📋 Overview

The **Colorado Artificial Intelligence Act (SB 24-205)** , signed into law in 2024, makes Colorado the first state in the nation to enact comprehensive legislation regulating algorithmic discrimination in high-risk AI systems. The law takes effect **June 30, 2026** .

### Bill Status
- **Introduced**: 2024
- **Signed into Law**: 2024
- **Effective Date**: June 30, 2026
- **Enforcement**: Colorado Attorney General has exclusive authority to enforce
- **Remedial Period**: One year after effective date before penalties apply

## 🎯 Key Requirements

| Requirement | Description | Compliance Deadline |
|-------------|-------------|---------------------|
| **Risk Assessments** | Annual impact assessments for high-risk AI systems | June 30, 2026 |
| **Reasonable Care** | Prevent algorithmic discrimination | June 30, 2026 |
| **Consumer Disclosures** | Notice when AI influences decisions | June 30, 2026 |
| **Adverse Explanations** | Principal reasons for adverse outcomes | June 30, 2026 |
| **Correction Rights** | Opportunity to correct incorrect data | June 30, 2026 |
| **Appeal Rights** | Human review of adverse decisions | June 30, 2026 |
| **Developer Documentation** | Documentation for deployers | June 30, 2026 |
| **Public Statements** | Summary of AI systems and risk management | June 30, 2026 |
| **Safe Harbor** | NIST AI RMF compliance provides legal protection | June 30, 2026 |

## 📊 Safe Harbor Provision

> "A deployer is rebuttably presumed to be in compliance with the duty of reasonable care... if the deployer has established, implemented, and maintains a risk management policy and system that is reasonably designed to identify and mitigate known or reasonably foreseeable risks of algorithmic discrimination."

**This safe harbor applies if the deployer's risk management framework is consistent with:**
- **NIST AI Risk Management Framework**, or
- **ISO/IEC 42001** (AI Management System)

## 🏢 Consequential Decisions Covered

The Act applies to high-risk AI systems that make, or are a substantial factor in, consequential decisions in these critical areas:

### Employment
- Hiring, promotion, termination
- Compensation, benefits
- Work assignments

### Financial Services
- Credit decisions
- Lending
- Insurance underwriting

### Housing
- Rental applications
- Mortgage approvals
- Eviction decisions

### Healthcare
- Diagnosis assistance
- Treatment recommendations
- Insurance coverage

### Education
- Admissions
- Scholarships
- Academic placement

### Legal Services
- Access to legal representation
- Case evaluation
- Settlement recommendations

### Government Benefits
- Eligibility determinations
- Benefit calculations
- Fraud detection

## 🔧 Implementation Approach

### For Developers

```python
# Developers must provide documentation to deployers
developer_tracker = ColoradoAITracker(
    entity_type="developer",
    organization="AI Developer Inc."
)

# Provide model documentation
docs = developer_tracker.provide_deployer_documentation(
    system_id="HR-SCREEN-001",
    deployer_id="DEPLOYER-123",
    documentation_package={
        "model_name": "Resume Screener v2",
        "intended_use": "Initial screening of job applicants",
        "limitations": ["Not for executive positions", "Requires bias testing"],
        "performance_metrics": {
            "accuracy": 0.94,
            "false_positive_rate": 0.03
        },
        "training_data_summary": {
            "size": 50000,
            "demographic_coverage": "broad"
        },
        "mitigation_strategies": [
            "Quarterly bias testing",
            "Human review required"
        ]
    }
)
```

### For Deployers

```python
# Deployers must conduct risk assessments and provide consumer rights
deployer_tracker = ColoradoAITracker(
    entity_type="deployer",
    organization="Colorado Company"
)

# Conduct annual risk assessment
assessment = deployer_tracker.conduct_risk_assessment(
    system_id="HR-SCREEN-001",
    assessment_date=time.time(),
    fairness_metrics={
        "disparate_impact": 0.98,
        "demographic_parity": 0.97
    },
    bias_test_results={
        "race": "PASS",
        "gender": "PASS",
        "age": "PASS_WITH_MONITORING"
    },
    residual_risk="LOW"
)

# Handle consumer appeal
appeal = deployer_tracker.handle_appeal(
    appeal_id="APPEAL-001",
    consumer_id="CONS-123",
    decision_id="DEC-001",
    appeal_reason="Experience miscalculated",
    reviewer="human-reviewer"
)
```

## 📁 Directory Contents

| File | Description |
|------|-------------|
| [README.md](README.md) | This file |
| [mapping.md](mapping.md) | Detailed mapping to bill sections |
| [implementation/colorado_tracker.py](implementation/colorado_tracker.py) | Core implementation |
| [examples/employment.py](examples/employment.py) | Employment decisions |
| [examples/financial.py](examples/financial.py) | Financial decisions |
| [examples/housing.py](examples/housing.py) | Housing decisions |
| [examples/healthcare.py](examples/healthcare.py) | Healthcare decisions |
| [examples/education.py](examples/education.py) | Education decisions |
| [examples/legal.py](examples/legal.py) | Legal services |
| [examples/government.py](examples/government.py) | Government benefits |

## 🔍 Verification

```bash
# Run Colorado AI Act verification
python ../../tests/verify-colorado.py --act sb-24-205
```

## 📚 References

- [Full Text of SB 24-205](https://leg.colorado.gov/sites/default/files/2024a_205_signed.pdf)
- [Colorado Attorney General AI Resources](https://coag.gov/ai)
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)

## 📬 Contact

- **Email**: colorado@humanjudgment.org
- **GitHub**: [hjs-spec/jep-us-solutions](https://github.com/hjs-spec/jep-us-solutions)
```
