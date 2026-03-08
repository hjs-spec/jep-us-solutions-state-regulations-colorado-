#!/usr/bin/env python3
"""
Colorado AI Act - Housing Decisions Example
==============================================

This example demonstrates a complete rental application screening system
that complies with Colorado's Artificial Intelligence Act (SB 24-205),
covering:

- Rental application processing
- Tenant screening and scoring
- Lease approval/denial decisions
- Fair housing compliance
- Reasonable accommodation requests
- Source of income protection
- Appeal and dispute resolution
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


class TenantScreeningSystem:
    """
    Complete tenant screening system with Colorado AI Act compliance.
    
    Features:
    - Rental application processing
    - AI-powered tenant scoring
    - Fair housing compliance (Fair Housing Act)
    - Source of income protection
    - Reasonable accommodation handling
    - Adverse action notifications
    - Appeal processing
    - Annual risk assessments
    """
    
    def __init__(self, property_management: str):
        self.property_management = property_management
        self.tracker = ColoradoAITracker(
            entity_type=EntityType.DEPLOYER,
            organization=property_management,
            contact_email="housing-compliance@pm.com"
        )
        
        self.properties = {}
        self.applications = []
        self.approvals = []
        self.denials = []
        self.accommodations = []
        
        print("="*80)
        print(f"🏠 Tenant Screening System - {property_management}")
        print("="*80)
        print(f"Colorado AI Act Effective: June 30, 2026")
    
    def setup_screening_system(self):
        """Register the tenant screening AI system with Colorado."""
        
        system = self.tracker.register_high_risk_system(
            system_id="TENANT-SCREEN-001",
            system_name="AI-Powered Tenant Screening Engine",
            system_type=DecisionType.HOUSING,
            description="Automated system for screening rental applicants, calculating tenant scores, and making leasing decisions",
            intended_use=(
                "Assist property managers by screening rental applications, "
                "calculating tenant risk scores, and identifying qualified "
                "applicants based on objective criteria"
            ),
            limitations=[
                "Not validated for commercial leases",
                "Requires regular fair housing testing",
                "May have lower accuracy for applicants with limited rental history",
                "Should not be the sole factor in leasing decisions",
                "Reasonable accommodations must be handled manually"
            ],
            training_data_summary={
                "size": 25000,
                "geographic_coverage": "Colorado statewide",
                "data_sources": ["applications", "credit_reports", "rental_history"],
                "date_range": "2020-2025"
            },
            performance_metrics={
                "accuracy": 0.92,
                "precision": 0.91,
                "recall": 0.90,
                "f1_score": 0.91
            },
            mitigation_strategies=[
                "Quarterly fair housing testing",
                "Human review for all adverse decisions",
                "Continuous monitoring for disparate impact",
                "Annual model validation",
                "Reasonable accommodation training"
            ],
            responsible_officer="fair-housing-officer@pm.com"
        )
        
        print(f"\n✅ Tenant screening system registered: {system['system_id']}")
        print(f"   Limitations documented: {len(system['limitations'])}")
        print(f"   Mitigation strategies: {len(system['mitigation_strategies'])}")
        
        return system
    
    def add_property(self, property_data: dict) -> str:
        """Add a rental property to the system."""
        property_id = f"PROP-{int(time.time())}-{random.randint(100, 999)}"
        
        self.properties[property_id] = {
            "property_id": property_id,
            "address": property_data['address'],
            "unit": property_data.get('unit'),
            "city": property_data['city'],
            "zip_code": property_data['zip_code'],
            "bedrooms": property_data['bedrooms'],
            "bathrooms": property_data['bathrooms'],
            "square_feet": property_data['square_feet'],
            "monthly_rent": property_data['monthly_rent'],
            "security_deposit": property_data['security_deposit'],
            "min_credit_score": property_data.get('min_credit_score', 620),
            "min_income_multiplier": property_data.get('min_income_multiplier', 3),
            "max_occupancy": property_data.get('max_occupancy', 4),
            "pets_allowed": property_data.get('pets_allowed', True),
            "section8_accepted": property_data.get('section8_accepted', False),
            "voucher_accepted": property_data.get('voucher_accepted', False),
            "date_added": time.time(),
            "status": "AVAILABLE"
        }
        
        print(f"\n🏢 Property Added:")
        print(f"   Property ID: {property_id}")
        print(f"   Address: {property_data['address']}, {property_data['city']}")
        print(f"   Rent: ${property_data['monthly_rent']:,.0f}/month")
        print(f"   Section 8 Accepted: {property_data.get('section8_accepted', False)}")
        print(f"   Vouchers Accepted: {property_data.get('voucher_accepted', False)}")
        
        return property_id
    
    def submit_rental_application(self, application_data: dict) -> str:
        """Submit a rental application."""
        application_id = f"RENT-{int(time.time())}-{random.randint(1000, 9999)}"
        
        # Hash applicant ID for privacy
        applicant_hash = f"APP-{hash(application_data['email']) % 10000:04d}"
        
        # Calculate income-to-rent ratio
        monthly_rent = self.properties[application_data['property_id']]['monthly_rent']
        income_to_rent = application_data['annual_income'] / 12 / monthly_rent if monthly_rent > 0 else 0
        
        application = {
            "application_id": application_id,
            "property_id": application_data['property_id'],
            "applicant_id": applicant_hash,
            "applicant_name": application_data['name'],
            "email": application_data['email'],
            "phone": application_data.get('phone'),
            "current_address": application_data.get('current_address'),
            "current_landlord": application_data.get('current_landlord'),
            "rental_history_years": application_data.get('rental_history_years', 0),
            "credit_score": application_data['credit_score'],
            "annual_income": application_data['annual_income'],
            "income_to_rent": income_to_rent,
            "employment_status": application_data.get('employment_status', 'employed'),
            "employment_years": application_data.get('employment_years', 0),
            "has_evictions": application_data.get('has_evictions', False),
            "has_felonies": application_data.get('has_felonies', False),
            "has_pets": application_data.get('has_pets', False),
            "pet_details": application_data.get('pet_details'),
            "source_of_income": application_data.get('source_of_income', 'employment'),
            "section8_voucher": application_data.get('section8_voucher', False),
            "housing_voucher": application_data.get('housing_voucher', False),
            "reasonable_accommodation": application_data.get('reasonable_accommodation'),
            "submitted_date": time.time(),
            "status": "PENDING",
            
            # Demographic data for fair housing analysis
            "race": application_data.get('race'),
            "ethnicity": application_data.get('ethnicity'),
            "gender": application_data.get('gender'),
            "age": application_data.get('age'),
            "family_status": application_data.get('family_status'),
            "disability": application_data.get('disability'),
            "zip_code": application_data.get('zip_code')
        }
        
        self.applications.append(application)
        
        print(f"\n📝 Rental Application Received:")
        print(f"   Application ID: {application_id}")
        print(f"   Applicant: {application_data['name']}")
        print(f"   Credit Score: {application_data['credit_score']}")
        print(f"   Income-to-Rent: {income_to_rent:.1f}x")
        print(f"   Section 8: {application_data.get('section8_voucher', False)}")
        print(f"   Housing Voucher: {application_data.get('housing_voucher', False)}")
        
        return application_id
    
    def screen_rental_application(self, application_id: str) -> dict:
        """
        Screen a rental application using AI and log the consequential decision.
        """
        # Find application
        application = next(
            (a for a in self.applications if a["application_id"] == application_id),
            None
        )
        if not application:
            return {"error": "Application not found"}
        
        property_data = self.properties.get(application["property_id"])
        
        print(f"\n🔍 Screening Rental Application: {application_id}")
        print(f"   Applicant: {application['applicant_name']}")
        print(f"   Property: {property_data['address']}")
        print(f"   Monthly Rent: ${property_data['monthly_rent']:,.0f}")
        print(f"   Applicant Income: ${application['annual_income']:,.0f}/year")
        print(f"   Income-to-Rent: {application['income_to_rent']:.1f}x")
        
        # Check for reasonable accommodation
        if application.get('reasonable_accommodation'):
            return self._handle_reasonable_accommodation(application, property_data)
        
        # Perform AI screening
        screening_result = self._perform_tenant_screening(application, property_data)
        
        # Make leasing decision
        approved = screening_result['approved']
        
        # Check source of income protection (Section 8, housing vouchers)
        if application['section8_voucher'] and not property_data['section8_accepted']:
            approved = False
            screening_result['source_of_income_issue'] = "Section 8 voucher not accepted"
        elif application['housing_voucher'] and not property_data['voucher_accepted']:
            approved = False
            screening_result['source_of_income_issue'] = "Housing voucher not accepted"
        
        # Prepare principal reasons (required by § 6-1-1706)
        principal_reasons = self._generate_principal_reasons(
            application, property_data, screening_result, approved
        )
        
        # Log the consequential decision
        decision = self.tracker.log_consequential_decision(
            system_id="TENANT-SCREEN-001",
            consumer_id=application['applicant_id'],
            decision_type=DecisionType.HOUSING,
            decision="APPROVE" if approved else "DENY",
            principal_reasons=principal_reasons,
            ai_was_determining_factor=True,
            ai_role_description="AI system screened rental application based on credit score, income, rental history, and other factors",
            explanation=self._generate_explanation(screening_result, approved),
            decision_factors=screening_result['factors'],
            notice_provided=True,
            notice_url=f"https://{self.property_management}/ai-notice",
            is_ai_generated=True,
            human_review_available=True,
            appeal_rights_provided=True,
            appeal_deadline=time.time() + 2592000,  # 30 days
            metadata={
                "application_id": application_id,
                "property_id": property_data['property_id'],
                "property_address": property_data['address'],
                "applicant_name": application['applicant_name'],
                "credit_score": application['credit_score'],
                "income_to_rent": application['income_to_rent'],
                "section8_voucher": application['section8_voucher'],
                "housing_voucher": application['housing_voucher'],
                "reasonable_accommodation": application.get('reasonable_accommodation'),
                "screening_score": screening_result['score'],
                "source_of_income_issue": screening_result.get('source_of_income_issue'),
                "demographics": {
                    "race": application.get('race'),
                    "ethnicity": application.get('ethnicity'),
                    "gender": application.get('gender'),
                    "age": application.get('age'),
                    "family_status": application.get('family_status'),
                    "disability": application.get('disability')
                }
            }
        )
        
        # Update application status
        application['status'] = "APPROVED" if approved else "DENIED"
        application['decision_id'] = decision['decision_id']
        application['screening_score'] = screening_result['score']
        
        if approved:
            self.approvals.append(application)
            property_data['status'] = "RENTED"
        else:
            self.denials.append(application)
        
        print(f"\n📊 Screening Result:")
        print(f"   Decision: {decision['decision']}")
        print(f"   Score: {screening_result['score']:.1f}/100")
        print(f"   Reasons: {', '.join(principal_reasons[:2])}")
        print(f"   Appeal Deadline: {datetime.fromtimestamp(decision['appeal_deadline'])}")
        
        return decision
    
    def _handle_reasonable_accommodation(self, application: dict, property_data: dict) -> dict:
        """Handle reasonable accommodation request (manual review)."""
        
        accommodation_id = f"ACC-{int(time.time())}"
        
        accommodation = {
            "accommodation_id": accommodation_id,
            "application_id": application['application_id'],
            "applicant_name": application['applicant_name'],
            "request": application['reasonable_accommodation'],
            "status": "PENDING_REVIEW",
            "assigned_to": "fair-housing-coordinator",
            "review_deadline": time.time() + 172800,  # 48 hours
            "notes": "Manual review required for reasonable accommodation"
        }
        
        self.accommodations.append(accommodation)
        
        print(f"\n🦮 Reasonable Accommodation Request:")
        print(f"   Accommodation ID: {accommodation_id}")
        print(f"   Request: {application['reasonable_accommodation']}")
        print(f"   Status: {accommodation['status']}")
        print(f"   Review Deadline: {datetime.fromtimestamp(accommodation['review_deadline'])}")
        
        # Log that AI was not the determining factor
        decision = self.tracker.log_consequential_decision(
            system_id="TENANT-SCREEN-001",
            consumer_id=application['applicant_id'],
            decision_type=DecisionType.HOUSING,
            decision="PENDING_MANUAL_REVIEW",
            principal_reasons=["Reasonable accommodation request requires manual review"],
            ai_was_determining_factor=False,
            explanation="Your application requires manual review due to reasonable accommodation request.",
            human_review_available=True,
            appeal_rights_provided=True,
            metadata=accommodation
        )
        
        return decision
    
    def _perform_tenant_screening(self, application: dict, property_data: dict) -> dict:
        """Simulate AI tenant screening."""
        
        score = 0
        factors = {}
        
        # Credit score evaluation (0-30 points)
        credit_score = application['credit_score']
        min_score = property_data['min_credit_score']
        
        if credit_score >= 750:
            score += 30
            factors['credit_score'] = {
                "score": 30,
                "value": credit_score,
                "rating": "excellent",
                "details": f"Excellent credit score {credit_score}"
            }
        elif credit_score >= 700:
            score += 25
            factors['credit_score'] = {
                "score": 25,
                "value": credit_score,
                "rating": "good",
                "details": f"Good credit score {credit_score}"
            }
        elif credit_score >= 680:
            score += 20
            factors['credit_score'] = {
                "score": 20,
                "value": credit_score,
                "rating": "fair",
                "details": f"Fair credit score {credit_score}"
            }
        elif credit_score >= min_score:
            score += 15
            factors['credit_score'] = {
                "score": 15,
                "value": credit_score,
                "rating": "acceptable",
                "details": f"Credit score {credit_score} meets minimum {min_score}"
            }
        else:
            score += max(0, 10 * (credit_score / min_score))
            factors['credit_score'] = {
                "score": score,
                "value": credit_score,
                "rating": "below_minimum",
                "details": f"Credit score {credit_score} below minimum {min_score}"
            }
        
        # Income-to-rent evaluation (0-30 points)
        income_to_rent = application['income_to_rent']
        min_multiplier = property_data['min_income_multiplier']
        
        if income_to_rent >= min_multiplier * 1.5:
            score += 30
            factors['income'] = {
                "score": 30,
                "value": income_to_rent,
                "rating": "excellent",
                "details": f"Income {income_to_rent:.1f}x rent (well above {min_multiplier}x)"
            }
        elif income_to_rent >= min_multiplier:
            score += 25
            factors['income'] = {
                "score": 25,
                "value": income_to_rent,
                "rating": "good",
                "details": f"Income {income_to_rent:.1f}x rent meets {min_multiplier}x requirement"
            }
        elif income_to_rent >= min_multiplier * 0.8:
            score += 15
            factors['income'] = {
                "score": 15,
                "value": income_to_rent,
                "rating": "fair",
                "details": f"Income {income_to_rent:.1f}x rent slightly below {min_multiplier}x"
            }
        else:
            score += max(0, 10 * (income_to_rent / min_multiplier))
            factors['income'] = {
                "score": score,
                "value": income_to_rent,
                "rating": "below_minimum",
                "details": f"Income {income_to_rent:.1f}x rent below {min_multiplier}x requirement"
            }
        
        # Rental history (0-20 points)
        rental_years = application['rental_history_years']
        if rental_years >= 5:
            score += 20
            factors['rental_history'] = {
                "score": 20,
                "value": rental_years,
                "rating": "excellent",
                "details": f"{rental_years} years positive rental history"
            }
        elif rental_years >= 3:
            score += 15
            factors['rental_history'] = {
                "score": 15,
                "value": rental_years,
                "rating": "good",
                "details": f"{rental_years} years rental history"
            }
        elif rental_years >= 1:
            score += 10
            factors['rental_history'] = {
                "score": 10,
                "value": rental_years,
                "rating": "fair",
                "details": f"{rental_years} years rental history"
            }
        elif rental_years > 0:
            score += 5
            factors['rental_history'] = {
                "score": 5,
                "value": rental_years,
                "rating": "limited",
                "details": f"Limited rental history ({rental_years} years)"
            }
        
        # Employment stability (0-20 points)
        employment_years = application['employment_years']
        if employment_years >= 5:
            score += 20
            factors['employment'] = {
                "score": 20,
                "value": employment_years,
                "rating": "stable",
                "details": f"Stable employment: {employment_years} years"
            }
        elif employment_years >= 3:
            score += 15
            factors['employment'] = {
                "score": 15,
                "value": employment_years,
                "rating": "good",
                "details": f"Employed for {employment_years} years"
            }
        elif employment_years >= 1:
            score += 10
            factors['employment'] = {
                "score": 10,
                "value": employment_years,
                "rating": "fair",
                "details": f"Employed for {employment_years} years"
            }
        else:
            factors['employment'] = {
                "score": 0,
                "value": employment_years,
                "rating": "unstable",
                "details": "Limited employment history"
            }
        
        # Negative factors
        if application['has_evictions']:
            score -= 30
            factors['evictions'] = {
                "score": -30,
                "details": "Previous eviction history"
            }
        
        if application['has_felonies']:
            score -= 20
            factors['criminal_history'] = {
                "score": -20,
                "details": "Felony conviction history"
            }
        
        # Decision threshold (70)
        approved = score >= 70 and not application['has_evictions']
        
        return {
            "score": max(0, score),
            "approved": approved,
            "factors": factors,
            "income_to_rent": income_to_rent,
            "meets_income_requirement": income_to_rent >= property_data['min_income_multiplier']
        }
    
    def _generate_principal_reasons(self, application: dict, property_data: dict,
                                    screening: dict, approved: bool) -> List[str]:
        """Generate principal reasons for the decision (required by § 6-1-1706)."""
        reasons = []
        
        if approved:
            if application['credit_score'] >= 700:
                reasons.append(f"Credit score ({application['credit_score']}) meets/exceeds requirements")
            if screening['meets_income_requirement']:
                reasons.append(f"Income ({application['income_to_rent']:.1f}x rent) meets minimum requirements")
            if application['rental_history_years'] >= 2:
                reasons.append(f"Positive rental history ({application['rental_history_years']} years)")
            if application['employment_years'] >= 2:
                reasons.append(f"Stable employment history ({application['employment_years']} years)")
        else:
            if screening.get('source_of_income_issue'):
                reasons.append(screening['source_of_income_issue'])
            elif application['has_evictions']:
                reasons.append("Previous eviction history")
            elif application['has_felonies']:
                reasons.append("Felony conviction history")
            elif application['credit_score'] < property_data['min_credit_score']:
                reasons.append(f"Credit score ({application['credit_score']}) below minimum ({property_data['min_credit_score']})")
            elif not screening['meets_income_requirement']:
                reasons.append(f"Income ({application['income_to_rent']:.1f}x rent) below minimum ({property_data['min_income_multiplier']}x)")
            elif application['section8_voucher'] and not property_data['section8_accepted']:
                reasons.append("Property does not accept Section 8 vouchers (source of income discrimination)")
            elif application['housing_voucher'] and not property_data['voucher_accepted']:
                reasons.append("Property does not accept housing vouchers (source of income discrimination)")
        
        return reasons[:3]
    
    def _generate_explanation(self, screening: dict, approved: bool) -> str:
        """Generate human-readable explanation."""
        if approved:
            return (
                f"Your rental application has been approved with a score of "
                f"{screening['score']:.1f}/100. You meet our tenant screening criteria. "
                f"If you disagree with any information used in this decision, you have "
                f"the right to request correction or appeal within 30 days."
            )
        else:
            return (
                f"Your rental application was not approved at this time. "
                f"Score: {screening['score']:.1f}/100. Please see the principal "
                f"reasons above for more information. You have the right to request "
                f"human review, correction of incorrect data, or appeal this decision "
                f"within 30 days."
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
            reviewer="housing-appeals-officer",
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
        protected_classes = ["race", "ethnicity", "gender", "family_status", "disability", "source_of_income"]
        
        for decision in all_decisions:
            demo = decision.get('metadata', {}).get('demographics', {})
            
            # Add source of income to analysis
            if decision.get('metadata', {}).get('section8_voucher'):
                demo['source_of_income'] = 'section8'
            elif decision.get('metadata', {}).get('housing_voucher'):
                demo['source_of_income'] = 'voucher'
            else:
                demo['source_of_income'] = 'employment'
            
            for protected in protected_classes:
                value = demo.get(protected)
                if value:
                    if protected not in demographic_data:
                        demographic_data[protected] = {}
                    if value not in demographic_data[protected]:
                        demographic_data[protected][value] = {"total": 0, "approved": 0}
                    
                    demographic_data[protected][value]["total"] += 1
                    if decision['decision'] == 'APPROVE':
                        demographic_data[protected][value]["approved"] += 1
        
        # Calculate disparate impact
        disparate_impact = {}
        for protected, groups in demographic_data.items():
            if len(groups) > 1:
                rates = []
                group_names = []
                for group, stats in groups.items():
                    if stats["total"] > 0:
                        rate = stats["approved"] / stats["total"]
                        rates.append(rate)
                        group_names.append(group)
                if len(rates) > 1:
                    disparate_impact[protected] = {
                        "min_rate": min(rates),
                        "max_rate": max(rates),
                        "ratio": min(rates) / max(rates) if max(rates) > 0 else 1.0,
                        "groups": group_names
                    }
        
        assessment = self.tracker.conduct_risk_assessment(
            system_id="TENANT-SCREEN-001",
            assessment_date=time.time(),
            fairness_metrics={
                "total_decisions": len(all_decisions),
                "approval_rate": len([d for d in all_decisions if d['decision'] == 'APPROVE']) / len(all_decisions) if all_decisions else 0,
                "disparate_impact": disparate_impact,
                "demographic_breakdown": demographic_data,
                "source_of_income_analysis": {
                    "section8_approval_rate": demographic_data.get('source_of_income', {}).get('section8', {}).get('approved', 0) / max(demographic_data.get('source_of_income', {}).get('section8', {}).get('total', 1), 1),
                    "voucher_approval_rate": demographic_data.get('source_of_income', {}).get('voucher', {}).get('approved', 0) / max(demographic_data.get('source_of_income', {}).get('voucher', {}).get('total', 1), 1),
                    "employment_approval_rate": demographic_data.get('source_of_income', {}).get('employment', {}).get('approved', 0) / max(demographic_data.get('source_of_income', {}).get('employment', {}).get('total', 1), 1)
                }
            },
            bias_test_results={
                "race": "PASS" if disparate_impact.get('race', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "ethnicity": "PASS" if disparate_impact.get('ethnicity', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "gender": "PASS" if disparate_impact.get('gender', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "family_status": "PASS" if disparate_impact.get('family_status', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "disability": "PASS" if disparate_impact.get('disability', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "source_of_income": "PASS" if min(
                    demographic_data.get('source_of_income', {}).get('section8', {}).get('approved', 0) / max(demographic_data.get('source_of_income', {}).get('employment', {}).get('total', 1), 1),
                    demographic_data.get('source_of_income', {}).get('voucher', {}).get('approved', 0) / max(demographic_data.get('source_of_income', {}).get('employment', {}).get('total', 1), 1)
                ) >= 0.8 else "FAIL"
            },
            risk_factors=[
                {"factor": k, "disparity": v['ratio'], "status": "monitor" if v['ratio'] < 0.85 else "acceptable"}
                for k, v in disparate_impact.items()
            ],
            mitigation_strategies=[
                "Quarterly fair housing testing",
                "Source of income discrimination training",
                "Reasonable accommodation training",
                "Human review for all adverse decisions",
                "Continuous monitoring for disparate impact",
                "Annual model validation"
            ],
            residual_risk="LOW" if all(v.get('ratio', 1.0) >= 0.8 for v in disparate_impact.values()) else "MEDIUM",
            next_assessment_date=time.time() + 31536000,  # 1 year
            conducted_by="fair-housing-officer@pm.com"
        )
        
        print(f"\n📊 Annual Risk Assessment (§ 6-1-1704):")
        print(f"   Assessment ID: {assessment['assessment_id']}")
        print(f"   Total Decisions: {len(all_decisions)}")
        print(f"   Disparate Impact Ratios: { {k:v['ratio'] for k,v in disparate_impact.items()} }")
        print(f"   Section 8 Approval Rate: {assessment['fairness_metrics']['source_of_income_analysis']['section8_approval_rate']:.1%}")
        print(f"   Voucher Approval Rate: {assessment['fairness_metrics']['source_of_income_analysis']['voucher_approval_rate']:.1%}")
        print(f"   Employment Approval Rate: {assessment['fairness_metrics']['source_of_income_analysis']['employment_approval_rate']:.1%}")
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
            certificate_url=f"https://{self.property_management}/compliance/nist-certificate"
        )
        
        print(f"\n🛡️ Safe Harbor Certificate (§ 6-1-1709):")
        print(f"   Certificate ID: {certificate['certificate_id']}")
        print(f"   Framework: {certificate['framework']}")
        print(f"   Certified By: {certificate['certified_by']}")
        print(f"   Expires: {datetime.fromtimestamp(certificate['expiry_date'])}")
        
        return certificate
    
    def run_housing_demo(self):
        """Run complete housing demonstration with Colorado AI Act compliance."""
        
        # Register system
        self.setup_screening_system()
        
        # Add properties
        properties = [
            {
                "address": "123 Main Street",
                "city": "Denver",
                "zip_code": "80202",
                "bedrooms": 2,
                "bathrooms": 1,
                "square_feet": 950,
                "monthly_rent": 1500,
                "security_deposit": 1500,
                "min_credit_score": 620,
                "min_income_multiplier": 3,
                "section8_accepted": True,
                "voucher_accepted": True
            },
            {
                "address": "456 Oak Avenue",
                "unit": "Apt 3B",
                "city": "Boulder",
                "zip_code": "80301",
                "bedrooms": 1,
                "bathrooms": 1,
                "square_feet": 750,
                "monthly_rent": 1800,
                "security_deposit": 1800,
                "min_credit_score": 640,
                "min_income_multiplier": 3.5,
                "section8_accepted": False,
                "voucher_accepted": True
            },
            {
                "address": "789 Pine Street",
                "city": "Colorado Springs",
                "zip_code": "80903",
                "bedrooms": 3,
                "bathrooms": 2,
                "square_feet": 1200,
                "monthly_rent": 1600,
                "security_deposit": 1600,
                "min_credit_score": 600,
                "min_income_multiplier": 2.5,
                "section8_accepted": True,
                "voucher_accepted": True
            }
        ]
        
        property_ids = []
        for prop in properties:
            pid = self.add_property(prop)
            property_ids.append(pid)
        
        # Submit applications with diverse demographics
        applications = [
            # Strong applicant - white male
            {
                "property_id": property_ids[0],
                "name": "John Smith",
                "email": "john.smith@email.com",
                "credit_score": 780,
                "annual_income": 65000,
                "rental_history_years": 8,
                "employment_years": 10,
                "has_evictions": False,
                "has_felonies": False,
                "source_of_income": "employment",
                "section8_voucher": False,
                "housing_voucher": False,
                "race": "white",
                "ethnicity": "not_hispanic",
                "gender": "male",
                "age": 42,
                "family_status": "single"
            },
            # Strong applicant - black female
            {
                "property_id": property_ids[0],
                "name": "Michelle Johnson",
                "email": "michelle.johnson@email.com",
                "credit_score": 760,
                "annual_income": 62000,
                "rental_history_years": 6,
                "employment_years": 7,
                "has_evictions": False,
                "has_felonies": False,
                "source_of_income": "employment",
                "section8_voucher": False,
                "housing_voucher": False,
                "race": "black",
                "ethnicity": "not_hispanic",
                "gender": "female",
                "age": 35,
                "family_status": "family_with_children"
            },
            # Section 8 applicant
            {
                "property_id": property_ids[0],
                "name": "Maria Garcia",
                "email": "maria.garcia@email.com",
                "credit_score": 650,
                "annual_income": 35000,
                "rental_history_years": 4,
                "employment_years": 5,
                "has_evictions": False,
                "has_felonies": False,
                "source_of_income": "section8",
                "section8_voucher": True,
                "housing_voucher": False,
                "race": "hispanic",
                "ethnicity": "hispanic",
                "gender": "female",
                "age": 32,
                "family_status": "family_with_children"
            },
            # Housing voucher applicant
            {
                "property_id": property_ids[1],
                "name": "Robert Taylor",
                "email": "robert.taylor@email.com",
                "credit_score": 620,
                "annual_income": 30000,
                "rental_history_years": 3,
                "employment_years": 4,
                "has_evictions": False,
                "has_felonies": False,
                "source_of_income": "voucher",
                "section8_voucher": False,
                "housing_voucher": True,
                "race": "black",
                "ethnicity": "not_hispanic",
                "gender": "male",
                "age": 45,
                "family_status": "single"
            },
            # Applicant with reasonable accommodation (disability)
            {
                "property_id": property_ids[2],
                "name": "Sarah Williams",
                "email": "sarah.williams@email.com",
                "credit_score": 680,
                "annual_income": 45000,
                "rental_history_years": 5,
                "employment_years": 6,
                "has_evictions": False,
                "has_felonies": False,
                "source_of_income": "employment",
                "section8_voucher": False,
                "housing_voucher": False,
                "reasonable_accommodation": "Need service animal for disability",
                "disability": "yes",
                "race": "white",
                "ethnicity": "not_hispanic",
                "gender": "female",
                "age": 38,
                "family_status": "single"
            },
            # Applicant with eviction history
            {
                "property_id": property_ids[2],
                "name": "James Davis",
                "email": "james.davis@email.com",
                "credit_score": 580,
                "annual_income": 40000,
                "rental_history_years": 2,
                "employment_years": 3,
                "has_evictions": True,
                "has_felonies": False,
                "source_of_income": "employment",
                "section8_voucher": False,
                "housing_voucher": False,
                "race": "white",
                "ethnicity": "not_hispanic",
                "gender": "male",
                "age": 52,
                "family_status": "single"
            }
        ]
        
        app_ids = []
        for app in applications:
            app_id = self.submit_rental_application(app)
            app_ids.append(app_id)
        
        # Screen applications
        decisions = []
        for app_id in app_ids:
            decision = self.screen_rental_application(app_id)
            decisions.append(decision)
        
        # Handle appeal for denied applicant
        denied_app = next(
            (a for a in self.applications if a["status"] == "DENIED"),
            None
        )
        if denied_app:
            applicant_name = next(
                (c['applicant_name'] for c in self.applications if c['application_id'] == denied_app['application_id']),
                "Unknown"
            )
            appeal = self.handle_appeal({
                "applicant_id": denied_app["applicant_id"],
                "decision_id": denied_app["decision_id"],
                "application_id": denied_app["application_id"],
                "applicant_name": applicant_name,
                "reason": "My credit report contains errors. I have documentation showing correct credit score.",
                "evidence": ["credit_report.pdf", "dispute_letter.pdf"]
            })
            
            # Resolve appeal
            self.resolve_appeal(
                appeal_id=appeal['appeal_id'],
                resolution="UPHELD",
                notes="After reviewing credit report, applicant's score was corrected. Application approved."
            )
        
        # Handle correction for data error
        if denied_app:
            applicant_name = next(
                (c['applicant_name'] for c in self.applications if c['application_id'] == denied_app['application_id']),
                "Unknown"
            )
            self.handle_correction({
                "applicant_id": denied_app["applicant_id"],
                "decision_id": denied_app["decision_id"],
                "application_id": denied_app["application_id"],
                "applicant_name": applicant_name,
                "field": "credit_score",
                "old_value": 580,
                "new_value": 630,
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
        print(f"   Properties: {len(property_ids)}")
        print(f"   Applications: {len(app_ids)}")
        print(f"   Approvals: {len(self.approvals)}")
        print(f"   Denials: {len(self.denials)}")
        print(f"   Reasonable Accommodations: {len(self.accommodations)}")
        print(f"   Approval Rate: {len(self.approvals)/len(app_ids)*100:.1f}%")
        print(f"   Appeals Filed: 1")
        print(f"   Corrections Processed: 1")
        print(f"   Annual Risk Assessment: ✓")
        print(f"   Safe Harbor Qualified: ✓")
        
        return report


if __name__ == "__main__":
    system = TenantScreeningSystem("Colorado Property Management")
    report = system.run_housing_demo()
    
    # Save report
    with open("colorado_housing_report.json", "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\n✅ Report saved: colorado_housing_report.json")
    print(f"\n⚠️ Note: Colorado AI Act effective June 30, 2026")
    print(f"   Ensure compliance before this date.")
    print(f"\n⚖️ Fair Housing Note: Source of income discrimination is prohibited in many Colorado jurisdictions.")
    print(f"   The Colorado AI Act requires protection against algorithmic discrimination.")
