# JEP Mapping to Colorado Artificial Intelligence Act (SB 24-205)

**Detailed Section-by-Section Mapping with Code Examples and Verification Methods**

## 📋 Overview

This document provides a comprehensive mapping between the **Judgment Event Protocol (JEP)** and the **Colorado Artificial Intelligence Act (SB 24-205)** , the first comprehensive US state law regulating algorithmic discrimination in high-risk AI systems.

The law takes effect **June 30, 2026**. This mapping covers all key requirements for both developers and deployers of high-risk AI systems.

---

## 📊 Part 1: Definitions and Scope

### Section 6-1-1701: Definitions

| Term | Definition | JEP Implementation |
|------|------------|-------------------|
| **Algorithmic Discrimination** | Differential treatment that harms protected classes | Fairness metrics + bias testing |
| **Consequential Decision** | Decisions in employment, financial, housing, etc. | Decision type classification |
| **Developer** | Person who develops or intentionally modifies high-risk AI | Entity type tracking |
| **Deployer** | Person who uses high-risk AI for consequential decisions | Entity type tracking |
| **High-Risk AI System** | AI that is a substantial factor in consequential decisions | Risk level classification |
| **Protected Class** | Age, race, gender, disability, etc. | Demographic tracking |

### Section 6-1-1702: Applicability

| Requirement | JEP Implementation | Verification |
|-------------|-------------------|--------------|
| **Jurisdiction** - Applies to Colorado residents | Geolocation tracking | `verify-colorado.py --jurisdiction` |
| **Exemptions** - Small businesses, certain sectors | Exemption flags | `verify-colorado.py --exemptions` |

---

## 📊 Part 2: Requirements for Developers

### Section 6-1-1703: Duty of Reasonable Care

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 6-1-1703(1)** - Exercise reasonable care to avoid algorithmic discrimination | Complete fairness framework | `tracker.conduct_risk_assessment()` | `verify-colorado.py --care` |
| **§ 6-1-1703(2)** - Document intended uses and limitations | `intended_use` + `limitations` fields | `system["limitations"] = [...]` | `verify-colorado.py --documentation` |
| **§ 6-1-1703(3)** - Provide documentation to deployers | `provide_deployer_documentation()` | `tracker.provide_deployer_documentation()` | `verify-colorado.py --docs` |

**Code Example:**
```python
from jep.us.colorado import ColoradoAITracker

developer = ColoradoAITracker(
    entity_type="developer",
    organization="AI Solutions Inc."
)

# Register high-risk AI system with documentation
system = developer.register_high_risk_system(
    system_id="HR-001",
    system_name="Resume Screener Pro",
    system_type="employment",
    description="AI system for resume screening",
    intended_use="Assist HR in initial candidate screening",
    limitations=[
        "Not validated for executive positions",
        "May have lower accuracy for non-traditional careers",
        "Requires regular bias testing"
    ],
    training_data_summary={
        "size": 50000,
        "demographics": "broad",
        "industries": ["tech", "finance", "healthcare"]
    },
    performance_metrics={
        "accuracy": 0.94,
        "precision": 0.93,
        "recall": 0.95
    },
    mitigation_strategies=[
        "Quarterly bias testing",
        "Human review required",
        "Continuous monitoring"
    ]
)

# Provide documentation to deployer
docs = developer.provide_deployer_documentation(
    system_id="HR-001",
    deployer_id="DEPLOYER-123",
    documentation_package={
        "model_name": system["system_name"],
        "intended_use": system["intended_use"],
        "limitations": system["limitations"],
        "performance_metrics": system["performance_metrics"],
        "training_data_summary": system["training_data_summary"],
        "mitigation_strategies": system["mitigation_strategies"],
        "testing_results": {
            "bias_testing": "passed",
            "adversarial_testing": "passed"
        }
    }
)
```

---

## 📊 Part 3: Requirements for Deployers

### Section 6-1-1704: Risk Assessments

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 6-1-1704(1)** - Conduct annual risk assessments | `conduct_risk_assessment()` | `tracker.conduct_risk_assessment()` | `verify-colorado.py --risk` |
| **§ 6-1-1704(2)** - Identify known risks of algorithmic discrimination | `risk_factors` + bias testing | `assessment["risk_factors"]` | `verify-colorado.py --identify` |
| **§ 6-1-1704(3)** - Implement risk mitigation strategies | `mitigation_strategies` | `assessment["mitigation_strategies"]` | `verify-colorado.py --mitigation` |
| **§ 6-1-1704(4)** - Maintain documentation for 3 years | Audit trail + retention | `tracker.generate_audit_report()` | `verify-colorado.py --retention` |

**Code Example:**
```python
deployer = ColoradoAITracker(
    entity_type="deployer",
    organization="Colorado Company"
)

# Register the system from developer
deployer.register_high_risk_system(
    system_id="HR-001",
    system_name="Resume Screener Pro",
    system_type="employment",
    description="AI system for resume screening",
    intended_use="Assist HR in initial candidate screening",
    limitations=["Not for executive positions"]
)

# Conduct annual risk assessment
assessment = deployer.conduct_risk_assessment(
    system_id="HR-001",
    assessment_date=time.time(),
    fairness_metrics={
        "disparate_impact": 0.98,
        "demographic_parity": 0.97,
        "equal_opportunity": 0.96,
        "test_population": 5000,
        "test_period": "2025-2026"
    },
    bias_test_results={
        "race": {
            "white": {"approved": 0.84, "sample": 2000},
            "black": {"approved": 0.82, "sample": 1000},
            "asian": {"approved": 0.85, "sample": 1000},
            "hispanic": {"approved": 0.81, "sample": 1000},
            "disparate_impact": 0.95
        },
        "gender": {
            "male": {"approved": 0.83, "sample": 2500},
            "female": {"approved": 0.84, "sample": 2500},
            "disparate_impact": 0.99
        }
    },
    risk_factors=[
        {"factor": "age", "disparity": 0.93, "status": "monitor"},
        {"factor": "disability", "disparity": 0.96, "status": "acceptable"}
    ],
    mitigation_strategies=[
        "Quarterly bias testing",
        "Human review for all final decisions",
        "Continuous monitoring for drift",
        "Annual fairness audit"
    ],
    residual_risk="LOW",
    next_assessment_date=time.time() + 31536000,  # 1 year
    conducted_by="compliance-officer@company.com"
)

# Assessment record includes signature for non-repudiation
assert assessment["signature"] is not None
```

### Section 6-1-1705: Consumer Notice

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 6-1-1705(1)** - Provide notice before decision | `log_consequential_decision()` | `tracker.log_consequential_decision()` | `verify-colorado.py --notice` |
| **§ 6-1-1705(2)** - Statement that AI was used | `is_ai_generated` flag | `decision["is_ai_generated"] = True` | `verify-colorado.py --ai-disclosure` |
| **§ 6-1-1705(3)** - Description of AI role | `ai_role` field | `decision["ai_role"] = "substantial_factor"` | `verify-colorado.py --ai-role` |

**Code Example:**
```python
# Log consequential decision with full notice
decision = deployer.log_consequential_decision(
    system_id="HR-001",
    consumer_id="CANDIDATE-123",
    decision_type="employment",
    decision="REJECT",
    
    # § 6-1-1705(1) - Pre-decision notice
    notice_provided=True,
    notice_url="https://company.com/ai-notice",
    
    # § 6-1-1705(2) - AI disclosure
    is_ai_generated=True,
    
    # § 6-1-1705(3) - Description of AI role
    ai_was_determining_factor=True,
    ai_role_description="AI system screened resumes and identified candidates not meeting minimum qualifications",
    
    # Principal reasons
    principal_reasons=[
        "Work experience below minimum threshold (2 years required, 1.5 years provided)",
        "Skills assessment score below threshold"
    ],
    
    explanation="Your application was screened by an AI system based on the criteria above.",
    
    human_review_available=True,
    appeal_rights_provided=True,
    appeal_deadline=time.time() + 2592000  # 30 days
)
```

### Section 6-1-1706: Adverse Decision Explanations

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 6-1-1706(1)** - Provide principal reasons for adverse decisions | `principal_reasons` field | `decision["principal_reasons"]` | `verify-colorado.py --reasons` |
| **§ 6-1-1706(2)** - Explain how AI was a factor | `ai_was_determining_factor` | `decision["ai_was_determining_factor"]` | `verify-colorado.py --ai-factor` |

**Code Example:**
```python
# Principal reasons must be specific and meaningful
decision = deployer.log_consequential_decision(
    system_id="HR-001",
    consumer_id="CANDIDATE-123",
    decision_type="employment",
    decision="REJECT",
    
    # GOOD: Specific, meaningful reasons
    principal_reasons=[
        "Work experience: 1.5 years (minimum required: 2 years)",
        "Skills assessment score: 65 (minimum required: 70)",
        "Education: Bachelor's degree (preferred: Master's degree)"
    ],
    
    # GOOD: Clear explanation of AI role
    ai_was_determining_factor=True,
    ai_role_description="AI system applied objective criteria to screen candidates. Human review was available but not requested.",
    
    # Decision factors for audit
    decision_factors={
        "work_experience": {"value": 1.5, "threshold": 2, "weight": 0.4},
        "skills_score": {"value": 65, "threshold": 70, "weight": 0.3},
        "education": {"value": "bachelor", "threshold": "master", "weight": 0.2}
    }
)

# BAD: Vague reasons would not comply
# principal_reasons = ["Did not meet requirements"]  ❌
```

### Section 6-1-1707: Correction Rights

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 6-1-1707(1)** - Opportunity to correct incorrect data | `handle_correction()` | `tracker.handle_correction()` | `verify-colorado.py --correction` |
| **§ 6-1-1707(2)** - Process correction requests in timely manner | SLA tracking | `correction["resolution_date"]` | `verify-colorado.py --correction-sla` |

**Code Example:**
```python
# Handle correction request
correction = deployer.handle_correction(
    request_id="REQ-001",
    consumer_id="CANDIDATE-123",
    decision_id=decision["decision_id"],
    field_corrected="work_experience",
    old_value="1.5 years",
    new_value="2.5 years",
    verification_method="resume_review",
    verification_document="updated_resume.pdf",
    resolution="ACCEPTED",
    correction_date=time.time(),
    notification_to_consumer=True,
    notification_method="email"
)

# After correction, system should re-evaluate
if correction["resolution"] == "ACCEPTED":
    # Trigger re-evaluation
    new_decision = deployer.log_consequential_decision(
        system_id="HR-001",
        consumer_id="CANDIDATE-123",
        decision_type="employment",
        decision="APPROVED",
        principal_reasons=["Now meets minimum requirements after correction"],
        ai_was_determining_factor=True
    )
```

### Section 6-1-1708: Appeal Rights

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 6-1-1708(1)** - Opportunity for human review | `handle_appeal()` | `tracker.handle_appeal()` | `verify-colorado.py --appeal` |
| **§ 6-1-1708(2)** - Timely resolution of appeals | SLA tracking | `appeal["resolution_deadline"]` | `verify-colorado.py --appeal-sla` |
| **§ 6-1-1708(3)** - Notice of appeal decision | `resolution_notes` | `appeal["resolution_notes"]` | `verify-colorado.py --appeal-notice` |

**Code Example:**
```python
# Handle appeal
appeal = deployer.handle_appeal(
    appeal_id="APPEAL-001",
    consumer_id="CANDIDATE-123",
    decision_id=decision["decision_id"],
    appeal_date=time.time(),
    appeal_reason="My experience was miscalculated. I have 2.5 years, not 1.5.",
    review_status="IN_PROGRESS",
    reviewer="human-resources-manager",
    appeal_deadline=time.time() + 604800,  # 7 days
    evidence_submitted=["updated_resume.pdf", "employment_verification.pdf"]
)

# Resolve appeal
resolution = deployer.resolve_appeal(
    appeal_id="APPEAL-001",
    resolution="UPHELD",  # or "DENIED"
    resolution_date=time.time(),
    resolution_notes="After reviewing submitted evidence, the applicant's experience was verified as 2.5 years. Original decision overturned.",
    new_decision_id="DEC-002"  # Link to new decision
)
```

---

## 📊 Part 4: Safe Harbor

### Section 6-1-1709: Affirmative Defense

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 6-1-1709(1)** - NIST AI RMF compliance | Complete NIST mapping | `tracker.nist_compliance()` | `verify-colorado.py --nist` |
| **§ 6-1-1709(2)** - ISO/IEC 42001 compliance | ISO mapping | `tracker.iso_compliance()` | `verify-colorado.py --iso` |

**Code Example:**
```python
# Demonstrate NIST AI RMF compliance for safe harbor
nist_report = deployer.generate_nist_report()

# Verify all NIST functions are covered
assert nist_report["govern_complete"]
assert nist_report["map_complete"]
assert nist_report["measure_complete"]
assert nist_report["manage_complete"]

# Generate safe harbor qualification certificate
safe_harbor = deployer.qualify_safe_harbor(
    framework="NIST AI RMF",
    version="1.0",
    assessment_date=time.time(),
    certified_by="third-party-auditor"
)
```

---

## 📊 Part 5: Enforcement

### Section 6-1-1710: Attorney General Enforcement

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 6-1-1710(1)** - AG has exclusive enforcement authority | Compliance reports | `tracker.generate_compliance_report()` | `verify-colorado.py --enforcement` |
| **§ 6-1-1710(2)** - Civil penalties up to $20,000 per violation | Audit trail | Complete history | `verify-colorado.py --audit` |

**Code Example:**
```python
# Generate report for AG
report = deployer.generate_compliance_report(
    start_date="2026-01-01",
    end_date="2026-12-31",
    include_risk_assessments=True,
    include_consequential_decisions=True,
    include_appeals=True,
    include_corrections=True
)

# Save for potential AG inquiry
with open("colorado_compliance_report.json", "w") as f:
    json.dump(report, f, indent=2, default=str)
```

---

## ✅ Complete Verification

```bash
# Run complete Colorado AI Act verification
python tests/verify-colorado.py --all

# Output:
# ========================================
# COLORADO AI ACT COMPLIANCE VERIFICATION
# ========================================
#
# 📋 Developer Requirements
#   ✅ § 6-1-1703: Duty of Reasonable Care
#   ✅ Documentation provided to deployers
#
# 📋 Deployer Requirements
#   ✅ § 6-1-1704: Annual Risk Assessments
#   ✅ § 6-1-1705: Consumer Notice
#   ✅ § 6-1-1706: Adverse Explanations
#   ✅ § 6-1-1707: Correction Rights
#   ✅ § 6-1-1708: Appeal Rights
#
# 📋 Safe Harbor
#   ✅ § 6-1-1709: NIST AI RMF Compliance
#
# ========================================
# FULL COMPLIANCE VERIFIED
# ========================================
```

## 📚 References

- [Full Text of SB 24-205](https://leg.colorado.gov/sites/default/files/2024a_205_signed.pdf)
- [Colorado Attorney General AI Resources](https://coag.gov/ai)
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)

## 📬 Contact

For Colorado-specific inquiries:
- **Email**: colorado@humanjudgment.org
- **GitHub**: [hjs-spec/jep-us-solutions](https://github.com/hjs-spec/jep-us-solutions)

---

*Last Updated: March 2026*
```
