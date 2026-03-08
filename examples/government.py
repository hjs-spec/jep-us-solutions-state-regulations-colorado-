#!/usr/bin/env python3
"""
Colorado AI Act - Government Benefits Example
================================================

This example demonstrates a complete government benefits eligibility system
that complies with Colorado's Artificial Intelligence Act (SB 24-205),
covering:

- Benefits eligibility determination
- Fraud detection and risk scoring
- Benefit amount calculation
- Appeals and fair hearings
- Data correction for beneficiaries
- Demographic fairness monitoring
- Transparency in automated decision-making
- Annual risk assessments
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


class GovernmentBenefitsSystem:
    """
    Complete government benefits system with Colorado AI Act compliance.
    
    Under SB 24-205, government benefits are explicitly designated as "consequential decisions"
    requiring consumer protections .
    
    Features:
    - Benefits eligibility determination
    - Fraud detection and risk scoring
    - Benefit amount calculation
    - Appeals and fair hearings
    - Data correction for beneficiaries
    - Demographic fairness monitoring
    - Transparency in automated decision-making
    - Annual risk assessments
    """
    
    def __init__(self, agency_name: str):
        self.agency_name = agency_name
        self.tracker = ColoradoAITracker(
            entity_type=EntityType.DEPLOYER,
            organization=agency_name,
            contact_email="ai-compliance@state.co.us"
        )
        
        self.beneficiaries = {}
        self.applications = []
        self.determinations = []
        self.fraud_alerts = []
        self.appeals = []
        self.benefit_programs = {}
        
        print("="*80)
        print(f"🏛️ Government Benefits System - {agency_name}")
        print("="*80)
        print(f"Colorado AI Act Effective: June 30, 2026")
        print(f"Consequential Decisions: Essential government services (benefits, eligibility, fraud) ")
    
    def setup_benefits_system(self):
        """Register the government benefits AI system with Colorado."""
        
        system = self.tracker.register_high_risk_system(
            system_id="GOV-BENEFITS-001",
            system_name="Benefits Eligibility & Fraud Detection System",
            system_type=DecisionType.GOVERNMENT,
            description="AI system for determining benefits eligibility, calculating benefit amounts, and detecting potential fraud",
            intended_use=(
                "Assist government agencies by determining eligibility for "
                "benefits programs, calculating benefit amounts, and flagging "
                "applications for fraud review"
            ),
            limitations=[
                "Not the sole factor in benefits determinations",
                "Requires regular fairness testing across demographic groups",
                "May have lower accuracy for applicants with complex circumstances",
                "Final determinations require human review",
                "Accommodation requests handled manually"
            ],
            training_data_summary={
                "size": 100000,
                "data_sources": ["applications", "tax_records", "prior_benefits_history"],
                "demographic_coverage": "broad",
                "program_types": ["SNAP", "Medicaid", "TANF", "LIHEAP"],
                "date_range": "2018-2025"
            },
            performance_metrics={
                "eligibility_accuracy": 0.94,
                "fraud_detection_precision": 0.87,
                "fraud_detection_recall": 0.82,
                "benefit_calculation_accuracy": 0.96,
                "f1_score": 0.91
            },
            mitigation_strategies=[
                "Quarterly fairness testing across protected classes",
                "Human review for all adverse determinations",
                "Continuous monitoring for disparate impact",
                "Annual model validation",
                "Bias mitigation training for caseworkers",
                "Regular calibration with audit results"
            ],
            responsible_officer="benefits-program-director@state.co.us"
        )
        
        print(f"\n✅ Government benefits system registered: {system['system_id']}")
        print(f"   Limitations documented: {len(system['limitations'])}")
        print(f"   Mitigation strategies: {len(system['mitigation_strategies'])}")
        print(f"   Note: Government benefits are \"essential government services\" under SB 24-205 ")
        
        return system
    
    def add_benefit_program(self, program_data: dict) -> str:
        """Add a benefit program to the system."""
        program_id = f"PROG-{int(time.time())}-{random.randint(100, 999)}"
        
        self.benefit_programs[program_id] = {
            "program_id": program_id,
            "name": program_data['name'],
            "type": program_data['type'],
            "description": program_data['description'],
            "eligibility_criteria": program_data['eligibility_criteria'],
            "income_thresholds": program_data.get('income_thresholds', {}),
            "asset_thresholds": program_data.get('asset_thresholds', {}),
            "benefit_formula": program_data.get('benefit_formula', {}),
            "max_benefit": program_data.get('max_benefit'),
            "funding_source": program_data.get('funding_source', 'federal'),
            "date_added": time.time(),
            "status": "ACTIVE"
        }
        
        print(f"\n📋 Benefit Program Added:")
        print(f"   Program ID: {program_id}")
        print(f"   Name: {program_data['name']}")
        print(f"   Type: {program_data['type']}")
        print(f"   Max Benefit: ${program_data.get('max_benefit', 0):,.0f}")
        
        return program_id
    
    def add_beneficiary(self, beneficiary_data: dict) -> str:
        """Add a beneficiary to the system."""
        beneficiary_id = f"BEN-{int(time.time())}-{random.randint(1000, 9999)}"
        
        # Hash for privacy
        beneficiary_hash = f"BEN-{hash(beneficiary_data['name'] + beneficiary_data.get('ssn_last4', '')) % 10000:04d}"
        
        self.beneficiaries[beneficiary_id] = {
            "beneficiary_id": beneficiary_id,
            "hash": beneficiary_hash,
            "name": beneficiary_data['name'],
            "age": beneficiary_data.get('age'),
            "gender": beneficiary_data.get('gender'),
            "race": beneficiary_data.get('race'),
            "ethnicity": beneficiary_data.get('ethnicity'),
            "household_size": beneficiary_data.get('household_size', 1),
            "household_composition": beneficiary_data.get('household_composition', {}),
            "income": beneficiary_data.get('income', {}),
            "assets": beneficiary_data.get('assets', {}),
            "employment_status": beneficiary_data.get('employment_status'),
            "disability_status": beneficiary_data.get('disability_status'),
            "veteran_status": beneficiary_data.get('veteran_status'),
            "prior_benefits": beneficiary_data.get('prior_benefits', []),
            "language_preference": beneficiary_data.get('language_preference', 'en'),
            "accommodation_needed": beneficiary_data.get('accommodation_needed'),
            "created_date": time.time()
        }
        
        print(f"\n👤 Beneficiary Added:")
        print(f"   Beneficiary ID: {beneficiary_id}")
        print(f"   Name: {beneficiary_data['name']}")
        print(f"   Household Size: {beneficiary_data.get('household_size', 1)}")
        print(f"   Income: ${beneficiary_data.get('income', {}).get('annual', 0):,.0f}")
        
        return beneficiary_id
    
    def submit_benefits_application(self, application_data: dict) -> str:
        """Submit a benefits application."""
        application_id = f"APP-{int(time.time())}-{random.randint(1000, 9999)}"
        
        application = {
            "application_id": application_id,
            "beneficiary_id": application_data['beneficiary_id'],
            "program_id": application_data['program_id'],
            "application_date": time.time(),
            "status": "PENDING",
            "documents_submitted": application_data.get('documents', []),
            "self_reported_data": {
                "income": application_data.get('income'),
                "assets": application_data.get('assets'),
                "household_size": application_data.get('household_size'),
                "special_circumstances": application_data.get('special_circumstances', [])
            },
            "priority_flag": application_data.get('priority_flag', False),
            "accommodation_request": application_data.get('accommodation_request'),
            "submitted_by": application_data.get('submitted_by', 'self')
        }
        
        self.applications.append(application)
        
        program = self.benefit_programs.get(application_data['program_id'])
        beneficiary = self.beneficiaries.get(application_data['beneficiary_id'])
        
        print(f"\n📝 Benefits Application Received:")
        print(f"   Application ID: {application_id}")
        print(f"   Beneficiary: {beneficiary['name'] if beneficiary else 'Unknown'}")
        print(f"   Program: {program['name'] if program else 'Unknown'}")
        print(f"   Household Size: {application_data.get('household_size', 1)}")
        
        return application_id
    
    def determine_eligibility(self, application_id: str, caseworker_id: str) -> dict:
        """
        Determine benefits eligibility using AI and log the consequential decision.
        
        Under SB 24-205, government benefits determinations are "consequential decisions"
        requiring consumer notice, explanation, and appeal rights .
        """
        # Find application
        application = next(
            (a for a in self.applications if a["application_id"] == application_id),
            None
        )
        if not application:
            return {"error": "Application not found"}
        
        beneficiary = self.beneficiaries.get(application["beneficiary_id"])
        program = self.benefit_programs.get(application["program_id"])
        
        print(f"\n🔍 Determining Eligibility: {application_id}")
        print(f"   Beneficiary: {beneficiary['name']}")
        print(f"   Program: {program['name']}")
        print(f"   Household Size: {application['self_reported_data']['household_size']}")
        
        # Check for accommodation request
        if application.get('accommodation_request'):
            return self._handle_accommodation_request(application, beneficiary)
        
        # Perform AI eligibility determination
        eligibility_result = self._determine_eligibility_ai(application, beneficiary, program)
        
        # Prepare principal reasons (required by § 6-1-1706)
        principal_reasons = self._generate_eligibility_reasons(eligibility_result, program)
        
        # Log the consequential decision
        decision = self.tracker.log_consequential_decision(
            system_id="GOV-BENEFITS-001",
            consumer_id=beneficiary['beneficiary_id'],
            decision_type=DecisionType.GOVERNMENT,
            decision=f"Eligibility: {eligibility_result['status']}",
            principal_reasons=principal_reasons,
            ai_was_determining_factor=True,
            ai_role_description="AI system determined benefits eligibility based on income, household size, and program criteria",
            explanation=eligibility_result['explanation'],
            decision_factors=eligibility_result['factors'],
            notice_provided=True,
            notice_url=f"https://{self.agency_name}/benefits/ai-notice",
            is_ai_generated=True,
            human_review_available=True,
            appeal_rights_provided=True,
            appeal_deadline=time.time() + 2592000,  # 30 days
            metadata={
                "application_id": application_id,
                "beneficiary_id": beneficiary['beneficiary_id'],
                "program_id": program['program_id'],
                "program_name": program['name'],
                "beneficiary_demographics": {
                    "race": beneficiary.get('race'),
                    "ethnicity": beneficiary.get('ethnicity'),
                    "gender": beneficiary.get('gender'),
                    "age": beneficiary.get('age'),
                    "disability_status": beneficiary.get('disability_status'),
                    "veteran_status": beneficiary.get('veteran_status')
                },
                "eligibility_status": eligibility_result['status'],
                "benefit_amount": eligibility_result.get('benefit_amount'),
                "determination_factors": eligibility_result['factors'],
                "caseworker_id": caseworker_id
            }
        )
        
        # Store determination
        determination = {
            "determination_id": f"DET-{int(time.time())}",
            "application_id": application_id,
            "beneficiary_id": beneficiary['beneficiary_id'],
            "program_id": program['program_id'],
            "status": eligibility_result['status'],
            "benefit_amount": eligibility_result.get('benefit_amount'),
            "decision_id": decision['decision_id'],
            "timestamp": time.time()
        }
        
        self.determinations.append(determination)
        
        # Update application status
        application['status'] = eligibility_result['status']
        application['determination_id'] = determination['determination_id']
        
        print(f"\n📊 Eligibility Determination:")
        print(f"   Status: {eligibility_result['status']}")
        if eligibility_result.get('benefit_amount'):
            print(f"   Benefit Amount: ${eligibility_result['benefit_amount']:,.2f}/month")
        if eligibility_result.get('eligibility_period'):
            print(f"   Eligibility Period: {eligibility_result['eligibility_period']} months")
        print(f"   Reasons: {', '.join(principal_reasons)}")
        print(f"   Appeal Deadline: {datetime.fromtimestamp(decision['appeal_deadline'])}")
        
        return determination
    
    def _handle_accommodation_request(self, application: dict, beneficiary: dict) -> dict:
        """Handle accommodation request (manual review)."""
        
        accommodation_id = f"ACC-{int(time.time())}"
        
        accommodation = {
            "accommodation_id": accommodation_id,
            "application_id": application['application_id'],
            "beneficiary_name": beneficiary['name'],
            "request": application['accommodation_request'],
            "status": "PENDING_REVIEW",
            "assigned_to": "accommodation-specialist",
            "review_deadline": time.time() + 172800,  # 48 hours
            "notes": "Manual review required for accommodation request"
        }
        
        print(f"\n🦮 Accommodation Request Received:")
        print(f"   Accommodation ID: {accommodation_id}")
        print(f"   Request: {application['accommodation_request']}")
        print(f"   Status: {accommodation['status']}")
        print(f"   Review Deadline: {datetime.fromtimestamp(accommodation['review_deadline'])}")
        
        # Log that AI was not the determining factor
        decision = self.tracker.log_consequential_decision(
            system_id="GOV-BENEFITS-001",
            consumer_id=beneficiary['beneficiary_id'],
            decision_type=DecisionType.GOVERNMENT,
            decision="PENDING_MANUAL_REVIEW",
            principal_reasons=["Accommodation request requires manual review"],
            ai_was_determining_factor=False,
            explanation="Your application requires manual review due to accommodation request.",
            human_review_available=True,
            appeal_rights_provided=True,
            metadata=accommodation
        )
        
        return {"accommodation_id": accommodation_id, "status": "PENDING_REVIEW"}
    
    def _determine_eligibility_ai(self, application: dict, beneficiary: dict, program: dict) -> dict:
        """Simulate AI eligibility determination."""
        
        factors = {}
        income = application['self_reported_data'].get('income', {}).get('annual', 0)
        household_size = application['self_reported_data'].get('household_size', 1)
        
        # Income threshold check
        income_thresholds = program.get('income_thresholds', {})
        threshold = income_thresholds.get(str(household_size), income_thresholds.get('default', 30000))
        
        income_ratio = income / threshold if threshold > 0 else 1.0
        
        if income <= threshold:
            factors['income'] = {
                "score": 80,
                "value": income,
                "threshold": threshold,
                "details": f"Income ${income:,.0f} within limit ${threshold:,.0f}"
            }
        else:
            factors['income'] = {
                "score": 30,
                "value": income,
                "threshold": threshold,
                "details": f"Income ${income:,.0f} exceeds limit ${threshold:,.0f}"
            }
        
        # Asset threshold check
        assets = application['self_reported_data'].get('assets', {}).get('total', 0)
        asset_thresholds = program.get('asset_thresholds', {})
        asset_limit = asset_thresholds.get(str(household_size), asset_thresholds.get('default', 5000))
        
        if assets <= asset_limit:
            factors['assets'] = {
                "score": 80,
                "value": assets,
                "threshold": asset_limit,
                "details": f"Assets ${assets:,.0f} within limit ${asset_limit:,.0f}"
            }
        else:
            factors['assets'] = {
                "score": 30,
                "value": assets,
                "threshold": asset_limit,
                "details": f"Assets ${assets:,.0f} exceed limit ${asset_limit:,.0f}"
            }
        
        # Categorical eligibility (e.g., disability, veteran status)
        categorical_factors = 0
        if beneficiary.get('disability_status') == 'disabled':
            categorical_factors += 1
            factors['disability'] = {
                "score": 90,
                "details": "Disability status - categorical eligibility"
            }
        
        if beneficiary.get('veteran_status') == 'veteran':
            categorical_factors += 1
            factors['veteran'] = {
                "score": 85,
                "details": "Veteran status - categorical eligibility"
            }
        
        # Special circumstances
        special_circumstances = application['self_reported_data'].get('special_circumstances', [])
        if 'homeless' in special_circumstances:
            factors['homeless'] = {
                "score": 95,
                "details": "Homeless - expedited processing"
            }
        
        # Calculate benefit amount
        benefit_amount = 0
        benefit_formula = program.get('benefit_formula', {})
        
        if 'percentage_of_need' in benefit_formula:
            need_standard = benefit_formula.get('need_standard', {}).get(str(household_size), 1000)
            benefit_amount = need_standard * benefit_formula['percentage_of_need']
        elif 'income_based' in benefit_formula:
            benefit_amount = max(0, threshold - income) * benefit_formula.get('multiplier', 0.3)
        elif 'fixed' in benefit_formula:
            benefit_amount = benefit_formula['fixed']
        
        benefit_amount = min(benefit_amount, program.get('max_benefit', benefit_amount))
        
        # Determine eligibility
        income_eligible = income <= threshold
        asset_eligible = assets <= asset_limit
        
        if categorical_factors > 0:
            status = "ELIGIBLE - CATEGORICAL"
            explanation = "Eligible based on categorical factors (disability/veteran status)"
        elif income_eligible and asset_eligible:
            status = "ELIGIBLE"
            explanation = f"Eligible based on income and asset criteria"
        else:
            status = "INELIGIBLE"
            explanation = f"Not eligible based on income and/or asset criteria"
        
        return {
            "status": status,
            "benefit_amount": round(benefit_amount, 2),
            "eligibility_period": 12,  # months
            "factors": factors,
            "explanation": explanation
        }
    
    def _generate_eligibility_reasons(self, eligibility: dict, program: dict) -> List[str]:
        """Generate principal reasons for eligibility determination."""
        reasons = []
        
        if "ELIGIBLE" in eligibility['status']:
            reasons.append(f"Meets income and asset criteria for {program['name']}")
            if eligibility.get('benefit_amount'):
                reasons.append(f"Monthly benefit amount: ${eligibility['benefit_amount']:,.2f}")
        else:
            reasons.append(f"Does not meet eligibility criteria for {program['name']}")
        
        return reasons[:3]
    
    def detect_fraud_risk(self, application_id: str) -> dict:
        """
        Detect potential fraud using AI.
        
        Fraud detection results may lead to "consequential decisions" affecting
        benefits access .
        """
        application = next(
            (a for a in self.applications if a["application_id"] == application_id),
            None
        )
        if not application:
            return {"error": "Application not found"}
        
        beneficiary = self.beneficiaries.get(application["beneficiary_id"])
        
        print(f"\n🚨 Fraud Risk Detection: {application_id}")
        print(f"   Beneficiary: {beneficiary['name']}")
        
        # Perform fraud risk analysis
        fraud_result = self._analyze_fraud_risk(application, beneficiary)
        
        # Log the decision
        decision = self.tracker.log_consequential_decision(
            system_id="GOV-BENEFITS-001",
            consumer_id=beneficiary['beneficiary_id'],
            decision_type=DecisionType.GOVERNMENT,
            decision=f"Fraud Risk: {fraud_result['risk_level']}",
            principal_reasons=fraud_result['reasons'],
            ai_was_determining_factor=False,
            ai_role_description="AI system flagged application for potential fraud review",
            explanation=fraud_result['explanation'],
            decision_factors=fraud_result['factors'],
            notice_provided=False,  # Fraud detection notices may be delayed
            is_ai_generated=True,
            human_review_available=True,
            appeal_rights_provided=True,
            metadata={
                "application_id": application_id,
                "beneficiary_id": beneficiary['beneficiary_id'],
                "risk_score": fraud_result['risk_score'],
                "risk_level": fraud_result['risk_level'],
                "flags": fraud_result['flags']
            }
        )
        
        # Store fraud alert
        alert = {
            "alert_id": f"FRAUD-{int(time.time())}",
            "application_id": application_id,
            "beneficiary_id": beneficiary['beneficiary_id'],
            "risk_score": fraud_result['risk_score'],
            "risk_level": fraud_result['risk_level'],
            "flags": fraud_result['flags'],
            "decision_id": decision['decision_id'],
            "timestamp": time.time()
        }
        
        self.fraud_alerts.append(alert)
        
        print(f"\n📊 Fraud Risk Assessment:")
        print(f"   Risk Level: {fraud_result['risk_level']}")
        print(f"   Risk Score: {fraud_result['risk_score']:.1f}%")
        print(f"   Flags: {', '.join(fraud_result['flags'])}")
        
        return alert
    
    def _analyze_fraud_risk(self, application: dict, beneficiary: dict) -> dict:
        """Simulate AI fraud risk analysis."""
        
        risk_score = random.randint(10, 90)
        flags = []
        
        # Income inconsistencies
        if random.random() > 0.7:
            flags.append("Income inconsistent with reported employment")
            risk_score += 15
        
        # Multiple applications
        prior_apps = len([a for a in self.applications if a['beneficiary_id'] == beneficiary['beneficiary_id']])
        if prior_apps > 3:
            flags.append("Multiple applications in short period")
            risk_score += 10
        
        # Address inconsistencies
        if random.random() > 0.8:
            flags.append("Address inconsistent with prior records")
            risk_score += 10
        
        # Identity verification flags
        if random.random() > 0.9:
            flags.append("Identity verification incomplete")
            risk_score += 20
        
        # Determine risk level
        if risk_score >= 70:
            risk_level = "HIGH"
        elif risk_score >= 40:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"
        
        reasons = [
            f"Risk Score: {risk_score:.0f}%",
            f"Flags: {len(flags)} issues identified"
        ]
        
        return {
            "risk_score": min(risk_score, 100),
            "risk_level": risk_level,
            "flags": flags[:3],
            "reasons": reasons,
            "factors": {
                "prior_applications": prior_apps,
                "flag_count": len(flags)
            },
            "explanation": f"Fraud risk assessment complete. {len(flags)} potential issues identified."
        }
    
    def handle_appeal(self, appeal_data: dict) -> dict:
        """Handle an appeal of a benefits determination (§ 6-1-1708)."""
        
        appeal = self.tracker.handle_appeal(
            appeal_id=f"APPEAL-{int(time.time())}",
            consumer_id=appeal_data['beneficiary_id'],
            decision_id=appeal_data['decision_id'],
            appeal_date=time.time(),
            appeal_reason=appeal_data['reason'],
            review_status="IN_PROGRESS",
            reviewer="fair-hearings-officer",
            appeal_deadline=time.time() + 604800,  # 7 days
            evidence_submitted=appeal_data.get('evidence', []),
            metadata={
                "application_id": appeal_data.get('application_id'),
                "beneficiary_name": appeal_data.get('beneficiary_name'),
                "program_id": appeal_data.get('program_id')
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
            notification_method="mail"
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
            consumer_id=correction_data['beneficiary_id'],
            decision_id=correction_data['decision_id'],
            field_corrected=correction_data['field'],
            old_value=correction_data['old_value'],
            new_value=correction_data['new_value'],
            verification_method=correction_data['verification_method'],
            verification_document=correction_data.get('verification_document'),
            resolution="ACCEPTED",
            notification_to_consumer=True,
            notification_method="mail",
            metadata={
                "application_id": correction_data.get('application_id'),
                "beneficiary_name": correction_data.get('beneficiary_name')
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
        """
        Conduct annual risk assessment as required by § 6-1-1704.
        
        The assessment must evaluate potential algorithmic discrimination
        across protected classes in government benefits determinations .
        """
        
        # Collect all determinations for analysis
        all_decisions = self.tracker.decisions
        gov_decisions = [d for d in all_decisions if d['decision_type'] == DecisionType.GOVERNMENT.value]
        
        # Analyze outcomes by demographic group
        demographic_data = {
            "race": {},
            "ethnicity": {},
            "gender": {},
            "age_group": {},
            "disability_status": {},
            "veteran_status": {}
        }
        
        for decision in gov_decisions:
            demo = decision.get('metadata', {}).get('beneficiary_demographics', {})
            for protected, value in demo.items():
                if protected in demographic_data and value:
                    if value not in demographic_data[protected]:
                        demographic_data[protected][value] = {
                            "total": 0,
                            "eligible": 0,
                            "avg_benefit": 0,
                            "benefit_sum": 0
                        }
                    
                    demographic_data[protected][value]["total"] += 1
                    
                    if 'ELIGIBLE' in decision.get('decision', ''):
                        demographic_data[protected][value]["eligible"] += 1
                    
                    # Track benefit amounts
                    metadata = decision.get('metadata', {})
                    if metadata.get('benefit_amount'):
                        demographic_data[protected][value]["benefit_sum"] += metadata['benefit_amount']
        
        # Calculate average benefits
        for protected, groups in demographic_data.items():
            for group, stats in groups.items():
                if stats["total"] > 0:
                    stats["avg_benefit"] = stats["benefit_sum"] / stats["total"] if stats["benefit_sum"] > 0 else 0
                    stats["eligibility_rate"] = stats["eligible"] / stats["total"] if stats["total"] > 0 else 0
        
        # Calculate disparate impact ratios
        disparate_impact = {}
        for protected, groups in demographic_data.items():
            if len(groups) > 1:
                eligibility_rates = []
                group_names = []
                for group, stats in groups.items():
                    if stats["total"] > 0:
                        eligibility_rates.append(stats["eligibility_rate"])
                        group_names.append(group)
                
                if len(eligibility_rates) > 1:
                    disparate_impact[protected] = {
                        "min_rate": min(eligibility_rates),
                        "max_rate": max(eligibility_rates),
                        "ratio": min(eligibility_rates) / max(eligibility_rates) if max(eligibility_rates) > 0 else 1.0,
                        "groups": group_names
                    }
        
        # Benefit amount disparity analysis
        benefit_disparity = {}
        for protected, groups in demographic_data.items():
            if len(groups) > 1:
                avg_benefits = [stats["avg_benefit"] for stats in groups.values() if stats["total"] > 0]
                if len(avg_benefits) > 1 and max(avg_benefits) > 0:
                    benefit_disparity[protected] = {
                        "min_avg": min(avg_benefits),
                        "max_avg": max(avg_benefits),
                        "ratio": min(avg_benefits) / max(avg_benefits) if max(avg_benefits) > 0 else 1.0
                    }
        
        assessment = self.tracker.conduct_risk_assessment(
            system_id="GOV-BENEFITS-001",
            assessment_date=time.time(),
            fairness_metrics={
                "total_decisions": len(gov_decisions),
                "eligibility_rate": len([d for d in gov_decisions if 'ELIGIBLE' in d.get('decision', '')]) / len(gov_decisions) if gov_decisions else 0,
                "disparate_impact": disparate_impact,
                "benefit_disparity": benefit_disparity,
                "demographic_breakdown": demographic_data
            },
            bias_test_results={
                "race": "PASS" if disparate_impact.get('race', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "ethnicity": "PASS" if disparate_impact.get('ethnicity', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "gender": "PASS" if disparate_impact.get('gender', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "disability": "PASS" if disparate_impact.get('disability_status', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "veteran": "PASS" if disparate_impact.get('veteran_status', {}).get('ratio', 1.0) >= 0.8 else "FAIL"
            },
            risk_factors=[
                {"factor": k, "disparity": v['ratio'], "status": "monitor" if v['ratio'] < 0.85 else "acceptable"}
                for k, v in disparate_impact.items()
            ],
            mitigation_strategies=[
                "Quarterly fairness testing across protected classes",
                "Human review for all adverse determinations",
                "Continuous monitoring for disparate impact",
                "Annual model validation",
                "Bias mitigation training for eligibility workers",
                "Community outreach to underrepresented groups"
            ],
            residual_risk="LOW" if all(v.get('ratio', 1.0) >= 0.8 for v in disparate_impact.values()) else "MEDIUM",
            next_assessment_date=time.time() + 31536000,  # 1 year
            conducted_by="benefits-program-director@state.co.us"
        )
        
        print(f"\n📊 Annual Risk Assessment (§ 6-1-1704):")
        print(f"   Assessment ID: {assessment['assessment_id']}")
        print(f"   Total Determinations: {len(gov_decisions)}")
        print(f"   Disparate Impact Ratios: { {k:v['ratio'] for k,v in disparate_impact.items()} }")
        print(f"   Benefit Disparity Ratios: { {k:v['ratio'] for k,v in benefit_disparity.items()} }")
        print(f"   Residual Risk: {assessment['residual_risk']}")
        print(f"   Next Assessment: {datetime.fromtimestamp(assessment['next_assessment_date'])}")
        print(f"\n⚖️ Note: Under SB 24-205, government benefits are \"essential government services\" requiring annual risk assessments ")
        
        return assessment
    
    def qualify_safe_harbor(self) -> dict:
        """
        Qualify for safe harbor under § 6-1-1709 (NIST AI RMF).
        
        Organizations that comply with NIST AI RMF receive a rebuttable presumption
        of reasonable care .
        """
        
        certificate = self.tracker.qualify_safe_harbor(
            framework="NIST AI RMF",
            version="1.0",
            assessment_date=time.time(),
            certified_by="third-party-auditor",
            certificate_url=f"https://{self.agency_name}/compliance/nist-certificate"
        )
        
        print(f"\n🛡️ Safe Harbor Certificate (§ 6-1-1709):")
        print(f"   Certificate ID: {certificate['certificate_id']}")
        print(f"   Framework: {certificate['framework']}")
        print(f"   Certified By: {certificate['certified_by']}")
        print(f"   Expires: {datetime.fromtimestamp(certificate['expiry_date'])}")
        print(f"   Note: Compliance with NIST AI RMF provides a rebuttable presumption of reasonable care ")
        
        return certificate
    
    def run_government_demo(self):
        """Run complete government benefits demonstration with Colorado AI Act compliance."""
        
        # Register system
        self.setup_benefits_system()
        
        # Add benefit programs
        programs = [
            {
                "name": "Supplemental Nutrition Assistance Program (SNAP)",
                "type": "nutrition",
                "description": "Food assistance for low-income households",
                "eligibility_criteria": ["income-based", "asset-based"],
                "income_thresholds": {
                    "1": 15000,
                    "2": 20000,
                    "3": 25000,
                    "4": 30000,
                    "default": 35000
                },
                "asset_thresholds": {
                    "default": 5000
                },
                "benefit_formula": {
                    "percentage_of_need": 0.8,
                    "need_standard": {
                        "1": 800,
                        "2": 1200,
                        "3": 1600,
                        "4": 2000
                    }
                },
                "max_benefit": 1500
            },
            {
                "name": "Low Income Home Energy Assistance Program (LIHEAP)",
                "type": "energy",
                "description": "Energy bill assistance",
                "eligibility_criteria": ["income-based"],
                "income_thresholds": {
                    "1": 18000,
                    "2": 24000,
                    "3": 30000,
                    "4": 36000,
                    "default": 40000
                },
                "asset_thresholds": {
                    "default": 10000
                },
                "benefit_formula": {
                    "fixed": 500
                },
                "max_benefit": 1000
            },
            {
                "name": "Temporary Assistance for Needy Families (TANF)",
                "type": "cash",
                "description": "Cash assistance for families",
                "eligibility_criteria": ["income-based", "asset-based", "work-requirements"],
                "income_thresholds": {
                    "1": 12000,
                    "2": 16000,
                    "3": 20000,
                    "4": 24000,
                    "default": 28000
                },
                "asset_thresholds": {
                    "default": 2000
                },
                "benefit_formula": {
                    "income_based": True,
                    "multiplier": 0.5
                },
                "max_benefit": 800
            }
        ]
        
        program_ids = []
        for prog in programs:
            pid = self.add_benefit_program(prog)
            program_ids.append(pid)
        
        # Add beneficiaries with diverse demographics
        beneficiaries = [
            # White family, eligible
            {
                "name": "John Smith",
                "age": 45,
                "gender": "male",
                "race": "white",
                "ethnicity": "non-hispanic",
                "household_size": 4,
                "income": {"annual": 28000},
                "assets": {"total": 3000},
                "employment_status": "employed",
                "disability_status": "none",
                "veteran_status": "veteran"
            },
            # Hispanic family, eligible
            {
                "name": "Maria Garcia",
                "age": 38,
                "gender": "female",
                "race": "hispanic",
                "ethnicity": "hispanic",
                "household_size": 3,
                "income": {"annual": 22000},
                "assets": {"total": 1000},
                "employment_status": "employed_part_time",
                "disability_status": "none",
                "veteran_status": "non-veteran"
            },
            # Black family with disability, eligible
            {
                "name": "James Johnson",
                "age": 52,
                "gender": "male",
                "race": "black",
                "ethnicity": "non-hispanic",
                "household_size": 2,
                "income": {"annual": 15000},
                "assets": {"total": 500},
                "employment_status": "unemployed",
                "disability_status": "disabled",
                "veteran_status": "non-veteran"
            },
            # Asian senior, eligible
            {
                "name": "Wei Chen",
                "age": 68,
                "gender": "male",
                "race": "asian",
                "ethnicity": "asian",
                "household_size": 1,
                "income": {"annual": 12000},
                "assets": {"total": 8000},
                "employment_status": "retired",
                "disability_status": "none",
                "veteran_status": "veteran"
            },
            # White family with accommodation request
            {
                "name": "Sarah Williams",
                "age": 35,
                "gender": "female",
                "race": "white",
                "ethnicity": "non-hispanic",
                "household_size": 3,
                "income": {"annual": 24000},
                "assets": {"total": 2000},
                "employment_status": "employed",
                "disability_status": "none",
                "veteran_status": "non-veteran",
                "accommodation_needed": "language assistance - Spanish interpreter needed"
            }
        ]
        
        beneficiary_ids = []
        for ben in beneficiaries:
            bid = self.add_beneficiary(ben)
            beneficiary_ids.append(bid)
        
        # Submit applications
        applications_to_submit = [
            {"beneficiary_idx": 0, "program_idx": 0, "income": {"annual": 28000}, "assets": {"total": 3000}, "household_size": 4},
            {"beneficiary_idx": 0, "program_idx": 1, "income": {"annual": 28000}, "assets": {"total": 3000}, "household_size": 4},
            {"beneficiary_idx": 1, "program_idx": 0, "income": {"annual": 22000}, "assets": {"total": 1000}, "household_size": 3},
            {"beneficiary_idx": 2, "program_idx": 0, "income": {"annual": 15000}, "assets": {"total": 500}, "household_size": 2, "special_circumstances": ["disability"]},
            {"beneficiary_idx": 2, "program_idx": 2, "income": {"annual": 15000}, "assets": {"total": 500}, "household_size": 2, "special_circumstances": ["disability"]},
            {"beneficiary_idx": 3, "program_idx": 1, "income": {"annual": 12000}, "assets": {"total": 8000}, "household_size": 1},
            {"beneficiary_idx": 4, "program_idx": 0, "income": {"annual": 24000}, "assets": {"total": 2000}, "household_size": 3, "accommodation_request": "Language assistance - Spanish interpreter needed"}
        ]
        
        app_ids = []
        for app_data in applications_to_submit:
            app_id = self.submit_benefits_application({
                "beneficiary_id": beneficiary_ids[app_data['beneficiary_idx']],
                "program_id": program_ids[app_data['program_idx']],
                "income": app_data.get('income', {}),
                "assets": app_data.get('assets', {}),
                "household_size": app_data.get('household_size', 1),
                "special_circumstances": app_data.get('special_circumstances', []),
                "accommodation_request": app_data.get('accommodation_request'),
                "documents": ["ID.pdf", "income_proof.pdf"]
            })
            app_ids.append(app_id)
        
        # Process determinations
        determinations = []
        for app_id in app_ids[:5]:  # First 5 applications
            det = self.determine_eligibility(app_id, "caseworker-123")
            determinations.append(det)
        
        # Run fraud detection on some applications
        for app_id in app_ids[2:4]:
            self.detect_fraud_risk(app_id)
        
        # Handle appeal for a denied application
        # Find a denied determination
        denied_det = None
        for det in self.determinations:
            if det.get('status') == 'INELIGIBLE':
                denied_det = det
                break
        
        if denied_det:
            app = next((a for a in self.applications if a['application_id'] == denied_det['application_id']), None)
            ben = self.beneficiaries.get(denied_det['beneficiary_id']) if denied_det else None
            if app and ben:
                self.handle_appeal({
                    "beneficiary_id": denied_det['beneficiary_id'],
                    "decision_id": denied_det['decision_id'],
                    "application_id": denied_det['application_id'],
                    "beneficiary_name": ben['name'],
                    "program_id": denied_det['program_id'],
                    "reason": "My income was calculated incorrectly - I have dependents that were not counted.",
                    "evidence": ["dependent_verification.pdf", "tax_return.pdf"]
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
        print(f"   Benefit Programs: {len(program_ids)}")
        print(f"   Beneficiaries: {len(beneficiary_ids)}")
        print(f"   Applications: {len(app_ids)}")
        print(f"   Determinations: {len(self.determinations)}")
        print(f"   Fraud Alerts: {len(self.fraud_alerts)}")
        print(f"   Appeals: {len(self.appeals)}")
        print(f"   Annual Risk Assessment: ✓")
        print(f"   Safe Harbor Qualified: ✓")
        print(f"\n⚖️ Note: Government benefits are \"essential government services\" under SB 24-205 ")
        print(f"   Protected classes monitored: race, ethnicity, gender, age, disability, veteran status ")
        
        return report


if __name__ == "__main__":
    system = GovernmentBenefitsSystem("Colorado Department of Human Services")
    report = system.run_government_demo()
    
    # Save report
    with open("colorado_government_report.json", "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\n✅ Report saved: colorado_government_report.json")
    print(f"\n⚠️ Note: Colorado AI Act effective June 30, 2026 ")
    print(f"   Government benefits are explicitly designated as \"essential government services\" under SB 24-205 ")
    print(f"\n📋 SB 24-205 Requirements Demonstrated:")
    print(f"   • Developer documentation (§ 6-1-1703)")
    print(f"   • Annual risk assessments (§ 6-1-1704)")
    print(f"   • Consumer notice (§ 6-1-1705)")
    print(f"   • Adverse explanation (§ 6-1-1706)")
    print(f"   • Correction rights (§ 6-1-1707)")
    print(f"   • Appeal rights (§ 6-1-1708)")
    print(f"   • Safe harbor (NIST AI RMF) (§ 6-1-1709)")
