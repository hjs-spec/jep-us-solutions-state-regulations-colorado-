#!/usr/bin/env python3
"""
Colorado AI Act - Financial Services Example
===============================================

This example demonstrates a complete consumer lending system
that complies with Colorado's Artificial Intelligence Act (SB 24-205),
covering:

- Loan application processing
- Credit scoring and risk assessment
- Lending decisions (approval/denial)
- Adverse action notifications
- Fair lending analysis
- ECOA compliance
- Annual risk assessments
- Consumer rights (correction, appeal)
"""

import json
import time
import sys
import random
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from state_regulations.colorado.sb_24_205.implementation.colorado_tracker import (
    ColoradoAITracker,
    EntityType,
    DecisionType
)


class ConsumerLendingSystem:
    """
    Complete consumer lending system with Colorado AI Act compliance.
    
    Features:
    - Loan application processing
    - AI-powered credit scoring
    - Fair lending analysis
    - Adverse action notifications
    - ECOA compliance
    - Disparate impact monitoring
    - Annual risk assessments
    - Consumer correction and appeal rights
    """
    
    def __init__(self, institution_name: str):
        self.institution_name = institution_name
        self.tracker = ColoradoAITracker(
            entity_type=EntityType.DEPLOYER,
            organization=institution_name,
            contact_email="compliance@lender.com"
        )
        
        self.loan_products = {}
        self.applications = []
        self.approvals = []
        self.denials = []
        
        print("="*80)
        print(f"💰 Consumer Lending System - {institution_name}")
        print("="*80)
        print(f"Colorado AI Act Effective: June 30, 2026")
    
    def setup_lending_system(self):
        """Register the lending AI system with Colorado."""
        
        system = self.tracker.register_high_risk_system(
            system_id="LENDING-001",
            system_name="AI-Powered Credit Scoring Engine",
            system_type=DecisionType.FINANCIAL,
            description="Automated system for credit scoring and loan underwriting decisions",
            intended_use=(
                "Assess creditworthiness of loan applicants, "
                "calculate risk scores, and make initial lending decisions "
                "based on established underwriting criteria"
            ),
            limitations=[
                "Not validated for jumbo loans (> $1M)",
                "May have lower accuracy for thin-file applicants",
                "Requires regular fair lending testing",
                "Should not be the sole factor for adverse decisions",
                "Not suitable for commercial lending"
            ],
            training_data_summary={
                "size": 100000,
                "demographics": "broad",
                "date_range": "2020-2025",
                "data_sources": ["credit_bureaus", "application_data", "public_records"]
            },
            performance_metrics={
                "accuracy": 0.96,
                "precision": 0.95,
                "recall": 0.94,
                "f1_score": 0.95,
                "auc_roc": 0.98
            },
            mitigation_strategies=[
                "Quarterly fair lending testing",
                "Human review for all adverse decisions",
                "Continuous monitoring for disparate impact",
                "Annual model validation",
                "Bias mitigation training"
            ],
            responsible_officer="chief-credit-officer@lender.com"
        )
        
        print(f"\n✅ Lending system registered: {system['system_id']}")
        print(f"   Limitations documented: {len(system['limitations'])}")
        print(f"   Mitigation strategies: {len(system['mitigation_strategies'])}")
        
        return system
    
    def create_loan_product(self, product_data: dict) -> str:
        """Create a new loan product."""
        product_id = f"LOAN-{int(time.time())}-{hash(product_data['name']) % 1000:03d}"
        
        self.loan_products[product_id] = {
            "product_id": product_id,
            "name": product_data['name'],
            "type": product_data['type'],
            "min_amount": product_data['min_amount'],
            "max_amount": product_data['max_amount'],
            "min_credit_score": product_data['min_credit_score'],
            "max_dti": product_data['max_dti'],
            "max_ltv": product_data.get('max_ltv', 80),
            "interest_rate_range": product_data['interest_rate_range'],
            "terms": product_data['terms'],
            "created_date": time.time(),
            "status": "ACTIVE"
        }
        
        print(f"\n📋 Loan Product Created: {product_data['name']}")
        print(f"   Product ID: {product_id}")
        print(f"   Amount Range: ${product_data['min_amount']:,.0f} - ${product_data['max_amount']:,.0f}")
        print(f"   Min Credit Score: {product_data['min_credit_score']}")
        print(f"   Max DTI: {product_data['max_dti']}%")
        
        return product_id
    
    def submit_loan_application(self, application_data: dict) -> str:
        """Submit a loan application."""
        application_id = f"APP-{int(time.time())}-{random.randint(1000, 9999)}"
        
        # Hash applicant ID for privacy
        applicant_hash = f"APP-{hash(application_data['email']) % 10000:04d}"
        
        # Calculate DTI
        monthly_income = application_data['annual_income'] / 12
        dti = (application_data['monthly_debt'] / monthly_income) * 100 if monthly_income > 0 else 999
        
        application = {
            "application_id": application_id,
            "product_id": application_data['product_id'],
            "applicant_id": applicant_hash,
            "applicant_name": application_data['name'],
            "email": application_data['email'],
            "phone": application_data.get('phone'),
            "address": application_data.get('address'),
            "loan_amount": application_data['loan_amount'],
            "loan_purpose": application_data['loan_purpose'],
            "credit_score": application_data['credit_score'],
            "annual_income": application_data['annual_income'],
            "monthly_debt": application_data['monthly_debt'],
            "dti": dti,
            "employment_years": application_data['employment_years'],
            "assets": application_data.get('assets', 0),
            "property_value": application_data.get('property_value'),
            "submitted_date": time.time(),
            "status": "PENDING",
            
            # Demographic data for fair lending analysis
            "race": application_data.get('race'),
            "ethnicity": application_data.get('ethnicity'),
            "gender": application_data.get('gender'),
            "age": application_data.get('age'),
            "zip_code": application_data.get('zip_code')
        }
        
        self.applications.append(application)
        
        print(f"\n📝 Loan Application Received:")
        print(f"   Application ID: {application_id}")
        print(f"   Applicant: {application_data['name']}")
        print(f"   Amount: ${application_data['loan_amount']:,.0f}")
        print(f"   Credit Score: {application_data['credit_score']}")
        print(f"   DTI: {dti:.1f}%")
        
        return application_id
    
    def process_loan_application(self, application_id: str) -> dict:
        """
        Process a loan application using AI and log the consequential decision.
        """
        # Find application
        application = next(
            (a for a in self.applications if a["application_id"] == application_id),
            None
        )
        if not application:
            return {"error": "Application not found"}
        
        product = self.loan_products.get(application["product_id"])
        
        print(f"\n🔍 Processing Loan Application: {application_id}")
        print(f"   Applicant: {application['applicant_name']}")
        print(f"   Product: {product['name']}")
        print(f"   Amount: ${application['loan_amount']:,.0f}")
        print(f"   Credit Score: {application['credit_score']}")
        print(f"   DTI: {application['dti']:.1f}%")
        
        # Perform AI underwriting
        underwriting_result = self._perform_underwriting(application, product)
        
        # Make lending decision
        approved = underwriting_result['approved']
        
        # Prepare principal reasons (required by § 6-1-1706)
        principal_reasons = self._generate_principal_reasons(
            application, product, underwriting_result, approved
        )
        
        # Calculate LTV if applicable
        ltv = None
        if application.get('property_value') and application['property_value'] > 0:
            ltv = (application['loan_amount'] / application['property_value']) * 100
        
        # Log the consequential decision
        decision = self.tracker.log_consequential_decision(
            system_id="LENDING-001",
            consumer_id=application['applicant_id'],
            decision_type=DecisionType.FINANCIAL,
            decision="APPROVED" if approved else "DENIED",
            principal_reasons=principal_reasons,
            ai_was_determining_factor=True,
            ai_role_description="AI system assessed creditworthiness based on credit score, DTI, and other factors",
            explanation=self._generate_explanation(underwriting_result, approved),
            decision_factors=underwriting_result['factors'],
            notice_provided=True,
            notice_url=f"https://{self.institution_name}/ai-notice",
            is_ai_generated=True,
            human_review_available=True,
            appeal_rights_provided=True,
            appeal_deadline=time.time() + 2592000,  # 30 days
            metadata={
                "application_id": application_id,
                "product_id": product['product_id'],
                "product_name": product['name'],
                "applicant_name": application['applicant_name'],
                "loan_amount": application['loan_amount'],
                "credit_score": application['credit_score'],
                "dti": application['dti'],
                "ltv": ltv,
                "underwriting_score": underwriting_result['score'],
                "demographics": {
                    "race": application.get('race'),
                    "ethnicity": application.get('ethnicity'),
                    "gender": application.get('gender'),
                    "age": application.get('age'),
                    "zip_code": application.get('zip_code')
                }
            }
        )
        
        # Update application status
        application['status'] = "APPROVED" if approved else "DENIED"
        application['decision_id'] = decision['decision_id']
        application['underwriting_score'] = underwriting_result['score']
        
        if approved:
            self.approvals.append(application)
        else:
            self.denials.append(application)
        
        print(f"\n📊 Underwriting Result:")
        print(f"   Decision: {decision['decision']}")
        print(f"   Score: {underwriting_result['score']:.1f}/100")
        print(f"   Reasons: {', '.join(principal_reasons)}")
        print(f"   Appeal Deadline: {datetime.fromtimestamp(decision['appeal_deadline'])}")
        
        return decision
    
    def _perform_underwriting(self, application: dict, product: dict) -> dict:
        """Simulate AI underwriting of loan application."""
        
        score = 0
        factors = {}
        
        # Credit score evaluation (0-40 points)
        credit_score = application['credit_score']
        min_score = product['min_credit_score']
        
        if credit_score >= 780:
            score += 40
            factors['credit_score'] = {
                "score": 40,
                "value": credit_score,
                "rating": "excellent",
                "details": f"Excellent credit score {credit_score}"
            }
        elif credit_score >= 740:
            score += 35
            factors['credit_score'] = {
                "score": 35,
                "value": credit_score,
                "rating": "very good",
                "details": f"Very good credit score {credit_score}"
            }
        elif credit_score >= 700:
            score += 30
            factors['credit_score'] = {
                "score": 30,
                "value": credit_score,
                "rating": "good",
                "details": f"Good credit score {credit_score}"
            }
        elif credit_score >= min_score:
            score += 25
            factors['credit_score'] = {
                "score": 25,
                "value": credit_score,
                "rating": "fair",
                "details": f"Credit score {credit_score} meets minimum {min_score}"
            }
        else:
            score += max(0, 15 * (credit_score / min_score))
            factors['credit_score'] = {
                "score": score,
                "value": credit_score,
                "rating": "below_minimum",
                "details": f"Credit score {credit_score} below minimum {min_score}"
            }
        
        # DTI evaluation (0-30 points)
        dti = application['dti']
        max_dti = product['max_dti']
        
        if dti <= 30:
            score += 30
            factors['dti'] = {
                "score": 30,
                "value": dti,
                "rating": "excellent",
                "details": f"Excellent DTI ratio {dti:.1f}%"
            }
        elif dti <= 36:
            score += 25
            factors['dti'] = {
                "score": 25,
                "value": dti,
                "rating": "good",
                "details": f"Good DTI ratio {dti:.1f}%"
            }
        elif dti <= max_dti:
            score += 20
            factors['dti'] = {
                "score": 20,
                "value": dti,
                "rating": "acceptable",
                "details": f"DTI ratio {dti:.1f}% within limit {max_dti}%"
            }
        else:
            score += max(0, 10 * (max_dti / dti))
            factors['dti'] = {
                "score": score,
                "value": dti,
                "rating": "exceeds_limit",
                "details": f"DTI ratio {dti:.1f}% exceeds limit {max_dti}%"
            }
        
        # Employment stability (0-15 points)
        employment_years = application['employment_years']
        if employment_years >= 5:
            score += 15
            factors['employment'] = {
                "score": 15,
                "value": employment_years,
                "rating": "stable",
                "details": f"Stable employment: {employment_years} years"
            }
        elif employment_years >= 2:
            score += 10
            factors['employment'] = {
                "score": 10,
                "value": employment_years,
                "rating": "moderate",
                "details": f"Employed for {employment_years} years"
            }
        elif employment_years >= 1:
            score += 5
            factors['employment'] = {
                "score": 5,
                "value": employment_years,
                "rating": "limited",
                "details": f"Limited employment: {employment_years} years"
            }
        else:
            factors['employment'] = {
                "score": 0,
                "value": employment_years,
                "rating": "unstable",
                "details": "Unstable employment history"
            }
        
        # Assets/LTV (0-15 points)
        if application.get('property_value'):
            ltv = (application['loan_amount'] / application['property_value']) * 100
            if ltv <= 70:
                score += 15
                factors['ltv'] = {
                    "score": 15,
                    "value": ltv,
                    "rating": "excellent",
                    "details": f"Excellent LTV ratio {ltv:.1f}%"
                }
            elif ltv <= 80:
                score += 10
                factors['ltv'] = {
                    "score": 10,
                    "value": ltv,
                    "rating": "good",
                    "details": f"Good LTV ratio {ltv:.1f}%"
                }
            elif ltv <= 90:
                score += 5
                factors['ltv'] = {
                    "score": 5,
                    "value": ltv,
                    "rating": "acceptable",
                    "details": f"Acceptable LTV ratio {ltv:.1f}%"
                }
            else:
                factors['ltv'] = {
                    "score": 0,
                    "value": ltv,
                    "rating": "high",
                    "details": f"High LTV ratio {ltv:.1f}%"
                }
        else:
            # Asset-based scoring for unsecured loans
            assets = application.get('assets', 0)
            loan_amount = application['loan_amount']
            if assets >= loan_amount * 2:
                score += 15
                factors['assets'] = {
                    "score": 15,
                    "value": assets,
                    "rating": "strong",
                    "details": f"Strong asset position"
                }
            elif assets >= loan_amount:
                score += 10
                factors['assets'] = {
                    "score": 10,
                    "value": assets,
                    "rating": "good",
                    "details": f"Adequate asset coverage"
                }
            elif assets >= loan_amount * 0.5:
                score += 5
                factors['assets'] = {
                    "score": 5,
                    "value": assets,
                    "rating": "fair",
                    "details": f"Partial asset coverage"
                }
        
        # Decision threshold (70)
        approved = score >= 70
        
        return {
            "score": score,
            "approved": approved,
            "factors": factors,
            "dti": application['dti'],
            "credit_score": application['credit_score']
        }
    
    def _generate_principal_reasons(self, application: dict, product: dict,
                                    underwriting: dict, approved: bool) -> List[str]:
        """Generate principal reasons for the decision (required by § 6-1-1706)."""
        reasons = []
        
        if approved:
            if application['credit_score'] >= product['min_credit_score']:
                reasons.append(f"Credit score ({application['credit_score']}) meets minimum requirements")
            if application['dti'] <= product['max_dti']:
                reasons.append(f"Debt-to-income ratio ({application['dti']:.1f}%) within acceptable range")
            if application['employment_years'] >= 2:
                reasons.append(f"Stable employment history ({application['employment_years']} years)")
            if application.get('property_value'):
                ltv = (application['loan_amount'] / application['property_value']) * 100
                if ltv <= 80:
                    reasons.append(f"Loan-to-value ratio ({ltv:.1f}%) favorable")
        else:
            if application['credit_score'] < product['min_credit_score']:
                reasons.append(f"Credit score ({application['credit_score']}) below minimum requirement ({product['min_credit_score']})")
            if application['dti'] > product['max_dti']:
                reasons.append(f"Debt-to-income ratio ({application['dti']:.1f}%) exceeds maximum allowed ({product['max_dti']}%)")
            if application['employment_years'] < 1:
                reasons.append("Insufficient employment history")
            if application.get('property_value'):
                ltv = (application['loan_amount'] / application['property_value']) * 100
                if ltv > 90:
                    reasons.append(f"Loan-to-value ratio ({ltv:.1f}%) too high")
        
        return reasons[:3]
    
    def _generate_explanation(self, underwriting: dict, approved: bool) -> str:
        """Generate human-readable explanation."""
        if approved:
            return (
                f"Your loan application has been approved with a score of "
                f"{underwriting['score']:.1f}/100. You meet our credit criteria. "
                f"If you disagree with this decision, you have the right to appeal "
                f"or request human review within 30 days."
            )
        else:
            return (
                f"Your loan application was not approved at this time. "
                f"Score: {underwriting['score']:.1f}/100. Please see the principal "
                f"reasons above for more information. You have the right to request "
                f"human review or appeal this decision within 30 days."
            )
    
    def handle_appeal(self, appeal_data: dict) -> dict:
        """Handle an appeal from a rejected applicant (§ 6-1-1708)."""
        
        appeal = self.tracker.handle_appeal(
            appeal_id=f"APPEAL-{int(time.time())}",
            consumer_id=appeal_data['applicant_id'],
            decision_id=appeal_data['decision_id'],
            appeal_date=time.time(),
            appeal_reason=appeal_data['reason'],
            review_status="IN_PROGRESS",
            reviewer="loan-appeals-officer",
            appeal_deadline=time.time() + 604800,  # 7 days
            evidence_submitted=appeal_data.get('evidence', []),
            metadata={
                "application_id": appeal_data['application_id'],
                "applicant_name": appeal_data['applicant_name']
            }
        )
        
        print(f"\n⚖️ Appeal Filed (§ 6-1-1708):")
        print(f"   Appeal ID: {appeal['appeal_id']}")
        print(f"   Reason: {appeal_data['reason'][:100]}...")
        print(f"   Status: {appeal['review_status']}")
        print(f"   Deadline: {datetime.fromtimestamp(appeal['appeal_deadline'])}")
        
        return appeal
    
    def resolve_appeal(self, appeal_id: str, resolution: str, notes: str) -> dict:
        """Resolve an appeal with final decision."""
        
        resolution = self.tracker.resolve_appeal(
            appeal_id=appeal_id,
            resolution=resolution,  # "UPHELD" or "DENIED"
            resolution_date=time.time(),
            resolution_notes=notes,
            notified_consumer=True,
            notification_method="email"
        )
        
        print(f"\n⚖️ Appeal Resolved:")
        print(f"   Appeal ID: {appeal_id}")
        print(f"   Resolution: {resolution['review_status']}")
        print(f"   Notes: {notes}")
        
        return resolution
    
    def handle_correction(self, correction_data: dict) -> dict:
        """Handle a data correction request (§ 6-1-1707)."""
        
        correction = self.tracker.handle_correction(
            request_id=f"REQ-{int(time.time())}",
            consumer_id=correction_data['applicant_id'],
            decision_id=correction_data['decision_id'],
            field_corrected=correction_data['field'],
            old_value=correction_data['old_value'],
            new_value=correction_data['new_value'],
            verification_method=correction_data['verification_method'],
            verification_document=correction_data.get('verification_document'),
            resolution="ACCEPTED",
            notification_to_consumer=True,
            notification_method="email",
            metadata={
                "application_id": correction_data['application_id'],
                "applicant_name": correction_data['applicant_name']
            }
        )
        
        print(f"\n✏️ Correction Processed (§ 6-1-1707):")
        print(f"   Correction ID: {correction['correction_id']}")
        print(f"   Field: {correction_data['field']}")
        print(f"   Old Value: {correction_data['old_value']}")
        print(f"   New Value: {correction_data['new_value']}")
        print(f"   Resolution: {correction['resolution']}")
        
        return correction
    
    def conduct_annual_risk_assessment(self) -> dict:
        """Conduct annual risk assessment as required by § 6-1-1704."""
        
        # Collect all decisions for analysis
        all_decisions = self.tracker.decisions
        
        # Calculate fairness metrics by demographic group
        demographic_data = {}
        for decision in all_decisions:
            demo = decision.get('metadata', {}).get('demographics', {})
            for key, value in demo.items():
                if value:
                    if key not in demographic_data:
                        demographic_data[key] = {}
                    if value not in demographic_data[key]:
                        demographic_data[key][value] = {"total": 0, "approved": 0}
                    
                    demographic_data[key][value]["total"] += 1
                    if decision['decision'] == 'APPROVED':
                        demographic_data[key][value]["approved"] += 1
        
        # Calculate disparate impact
        disparate_impact = {}
        for dim, groups in demographic_data.items():
            if len(groups) > 1:
                rates = []
                group_names = []
                for group, stats in groups.items():
                    if stats["total"] > 0:
                        rate = stats["approved"] / stats["total"]
                        rates.append(rate)
                        group_names.append(group)
                if len(rates) > 1:
                    disparate_impact[dim] = {
                        "min_rate": min(rates),
                        "max_rate": max(rates),
                        "ratio": min(rates) / max(rates) if max(rates) > 0 else 1.0,
                        "groups": group_names
                    }
        
        assessment = self.tracker.conduct_risk_assessment(
            system_id="LENDING-001",
            assessment_date=time.time(),
            fairness_metrics={
                "total_decisions": len(all_decisions),
                "approval_rate": len([d for d in all_decisions if d['decision'] == 'APPROVED']) / len(all_decisions) if all_decisions else 0,
                "disparate_impact": disparate_impact,
                "demographic_breakdown": demographic_data
            },
            bias_test_results={
                "race": "PASS" if disparate_impact.get('race', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "ethnicity": "PASS" if disparate_impact.get('ethnicity', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "gender": "PASS" if disparate_impact.get('gender', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "age": "PASS_WITH_MONITORING" if disparate_impact.get('age', {}).get('ratio', 1.0) >= 0.75 else "FAIL"
            },
            risk_factors=[
                {"factor": k, "disparity": v['ratio'], "status": "monitor" if v['ratio'] < 0.85 else "acceptable"}
                for k, v in disparate_impact.items()
            ],
            mitigation_strategies=[
                "Quarterly fair lending testing",
                "Human review for all adverse decisions",
                "Continuous disparate impact monitoring",
                "Annual model validation",
                "Bias mitigation training"
            ],
            residual_risk="LOW" if all(v.get('ratio', 1.0) >= 0.8 for v in disparate_impact.values()) else "MEDIUM",
            next_assessment_date=time.time() + 31536000,  # 1 year
            conducted_by="fair-lending-officer@lender.com"
        )
        
        print(f"\n📊 Annual Risk Assessment (§ 6-1-1704):")
        print(f"   Assessment ID: {assessment['assessment_id']}")
        print(f"   Total Decisions: {len(all_decisions)}")
        print(f"   Disparate Impact Ratios: { {k:v['ratio'] for k,v in disparate_impact.items()} }")
        print(f"   Residual Risk: {assessment['residual_risk']}")
        print(f"   Next Assessment: {datetime.fromtimestamp(assessment['next_assessment_date'])}")
        
        return assessment
    
    def qualify_safe_harbor(self) -> dict:
        """Qualify for safe harbor under § 6-1-1709 (NIST AI RMF)."""
        
        certificate = self.tracker.qualify_safe_harbor(
            framework="NIST AI RMF",
            version="1.0",
            assessment_date=time.time(),
            certified_by="third-party-auditor",
            certificate_url=f"https://{self.institution_name}/compliance/nist-certificate"
        )
        
        print(f"\n🛡️ Safe Harbor Certificate (§ 6-1-1709):")
        print(f"   Certificate ID: {certificate['certificate_id']}")
        print(f"   Framework: {certificate['framework']}")
        print(f"   Certified By: {certificate['certified_by']}")
        print(f"   Expires: {datetime.fromtimestamp(certificate['expiry_date'])}")
        
        return certificate
    
    def run_lending_demo(self):
        """Run complete lending demonstration with Colorado AI Act compliance."""
        
        # Register system
        self.setup_lending_system()
        
        # Create loan products
        products = [
            {
                "name": "Conventional Mortgage",
                "type": "mortgage",
                "min_amount": 50000,
                "max_amount": 750000,
                "min_credit_score": 680,
                "max_dti": 43,
                "max_ltv": 80,
                "interest_rate_range": "4.5-6.5%",
                "terms": [15, 20, 30]
            },
            {
                "name": "FHA Loan",
                "type": "mortgage",
                "min_amount": 30000,
                "max_amount": 500000,
                "min_credit_score": 580,
                "max_dti": 50,
                "max_ltv": 96.5,
                "interest_rate_range": "5.0-7.0%",
                "terms": [15, 20, 30]
            },
            {
                "name": "Auto Loan",
                "type": "auto",
                "min_amount": 5000,
                "max_amount": 75000,
                "min_credit_score": 640,
                "max_dti": 45,
                "interest_rate_range": "4.0-8.0%",
                "terms": [24, 36, 48, 60, 72]
            },
            {
                "name": "Personal Loan",
                "type": "personal",
                "min_amount": 1000,
                "max_amount": 50000,
                "min_credit_score": 620,
                "max_dti": 40,
                "interest_rate_range": "7.0-15.0%",
                "terms": [12, 24, 36, 48, 60]
            }
        ]
        
        product_ids = []
        for product in products:
            pid = self.create_loan_product(product)
            product_ids.append(pid)
        
        # Submit applications with diverse demographics
        applications = [
            # Strong applicant (white male)
            {
                "product_id": product_ids[0],
                "name": "John Smith",
                "email": "john.smith@email.com",
                "phone": "303-555-1234",
                "address": "123 Main St, Denver, CO",
                "loan_amount": 350000,
                "loan_purpose": "purchase",
                "credit_score": 780,
                "annual_income": 95000,
                "monthly_debt": 1500,
                "employment_years": 10,
                "assets": 80000,
                "property_value": 450000,
                "race": "white",
                "ethnicity": "not_hispanic",
                "gender": "male",
                "age": 45,
                "zip_code": "80202"
            },
            # Strong applicant (black female)
            {
                "product_id": product_ids[0],
                "name": "Michelle Johnson",
                "email": "michelle.johnson@email.com",
                "phone": "720-555-5678",
                "address": "456 Oak St, Boulder, CO",
                "loan_amount": 320000,
                "loan_purpose": "purchase",
                "credit_score": 770,
                "annual_income": 88000,
                "monthly_debt": 1400,
                "employment_years": 8,
                "assets": 75000,
                "property_value": 400000,
                "race": "black",
                "ethnicity": "not_hispanic",
                "gender": "female",
                "age": 38,
                "zip_code": "80301"
            },
            # Good applicant (hispanic male)
            {
                "product_id": product_ids[1],
                "name": "Carlos Rodriguez",
                "email": "carlos.rodriguez@email.com",
                "phone": "719-555-9012",
                "address": "789 Pine St, Colorado Springs, CO",
                "loan_amount": 250000,
                "loan_purpose": "purchase",
                "credit_score": 680,
                "annual_income": 65000,
                "monthly_debt": 1400,
                "employment_years": 5,
                "assets": 35000,
                "property_value": 300000,
                "race": "hispanic",
                "ethnicity": "hispanic",
                "gender": "male",
                "age": 35,
                "zip_code": "80903"
            },
            # Fair applicant (asian female) - may be borderline
            {
                "product_id": product_ids[1],
                "name": "Yuki Tanaka",
                "email": "yuki.tanaka@email.com",
                "phone": "970-555-3456",
                "address": "321 Elm St, Fort Collins, CO",
                "loan_amount": 280000,
                "loan_purpose": "purchase",
                "credit_score": 640,
                "annual_income": 58000,
                "monthly_debt": 1800,
                "employment_years": 3,
                "assets": 25000,
                "property_value": 320000,
                "race": "asian",
                "ethnicity": "asian",
                "gender": "female",
                "age": 32,
                "zip_code": "80521"
            },
            # Auto loan applicant
            {
                "product_id": product_ids[2],
                "name": "Robert Brown",
                "email": "robert.brown@email.com",
                "phone": "303-555-7890",
                "address": "555 Cedar Ln, Denver, CO",
                "loan_amount": 35000,
                "loan_purpose": "auto_purchase",
                "credit_score": 710,
                "annual_income": 65000,
                "monthly_debt": 800,
                "employment_years": 4,
                "assets": 15000,
                "race": "white",
                "ethnicity": "not_hispanic",
                "gender": "male",
                "age": 42,
                "zip_code": "80210"
            },
            # Personal loan applicant
            {
                "product_id": product_ids[3],
                "name": "Sarah Chen",
                "email": "sarah.chen@email.com",
                "phone": "720-555-2345",
                "address": "888 Maple Dr, Boulder, CO",
                "loan_amount": 15000,
                "loan_purpose": "debt_consolidation",
                "credit_score": 690,
                "annual_income": 55000,
                "monthly_debt": 900,
                "employment_years": 3,
                "assets": 8000,
                "race": "asian",
                "ethnicity": "asian",
                "gender": "female",
                "age": 29,
                "zip_code": "80302"
            }
        ]
        
        app_ids = []
        for app in applications:
            app_id = self.submit_loan_application(app)
            app_ids.append(app_id)
        
        # Process applications
        decisions = []
        for app_id in app_ids:
            decision = self.process_loan_application(app_id)
            decisions.append(decision)
        
        # Handle appeal for denied applicant
        denied_app = next(
            (a for a in self.applications if a["status"] == "DENIED"),
            None
        )
        if denied_app:
            appeal = self.handle_appeal({
                "applicant_id": denied_app["applicant_id"],
                "decision_id": denied_app["decision_id"],
                "application_id": denied_app["application_id"],
                "applicant_name": denied_app["applicant_name"],
                "reason": "My credit score was incorrectly reported. I have documentation showing it should be higher.",
                "evidence": ["credit_report.pdf", "dispute_letter.pdf"]
            })
            
            # Resolve appeal
            self.resolve_appeal(
                appeal_id=appeal['appeal_id'],
                resolution="UPHELD",
                notes="After reviewing credit report, applicant's score was corrected from 640 to 680. Application approved."
            )
        
        # Handle correction for data error
        if denied_app:
            self.handle_correction({
                "applicant_id": denied_app["applicant_id"],
                "decision_id": denied_app["decision_id"],
                "application_id": denied_app["application_id"],
                "applicant_name": denied_app["applicant_name"],
                "field": "credit_score",
                "old_value": 640,
                "new_value": 680,
                "verification_method": "credit_report_review",
                "verification_document": "updated_credit_report.pdf"
            })
        
        # Conduct annual risk assessment
        self.conduct_annual_risk_assessment()
        
        # Qualify for safe harbor
        self.qualify_safe_harbor()
        
        # Generate Attorney General report
        report = self.tracker.generate_compliance_report()
        
        print("\n" + "="*80)
        print("📊 Colorado AI Act Compliance Summary")
        print("="*80)
        print(f"   Loan Products: {len(product_ids)}")
        print(f"   Applications: {len(app_ids)}")
        print(f"   Approvals: {len(self.approvals)}")
        print(f"   Denials: {len(self.denials)}")
        print(f"   Approval Rate: {len(self.approvals)/len(app_ids)*100:.1f}%")
        print(f"   Appeals Filed: 1")
        print(f"   Corrections Processed: 1")
        print(f"   Annual Risk Assessment: ✓")
        print(f"   Safe Harbor Qualified: ✓")
        
        return report


if __name__ == "__main__":
    system = ConsumerLendingSystem("Colorado Credit Union")
    report = system.run_lending_demo()
    
    # Save report
    with open("colorado_lending_report.json", "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\n✅ Report saved: colorado_lending_report.json")
    print(f"\n⚠️ Note: Colorado AI Act effective June 30, 2026")
    print(f"   Ensure compliance before this date.")
