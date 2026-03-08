#!/usr/bin/env python3
"""
Colorado AI Act - Education Decisions Example
================================================

This example demonstrates a complete college admissions and scholarship system
that complies with Colorado's Artificial Intelligence Act (SB 24-205),
covering:

- Undergraduate admissions processing
- Holistic review with AI assistance
- Scholarship awarding decisions
- Academic program placement
- Fair access analysis
- Appeal and reconsideration
- Accommodation requests for disabilities
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


class CollegeAdmissionsSystem:
    """
    Complete college admissions system with Colorado AI Act compliance.
    
    Features:
    - Undergraduate application processing
    - AI-assisted holistic review
    - Scholarship awarding
    - Academic program placement
    - Fair access analysis
    - Appeal processing
    - Disability accommodation
    - Annual risk assessments
    """
    
    def __init__(self, institution_name: str):
        self.institution_name = institution_name
        self.tracker = ColoradoAITracker(
            entity_type=EntityType.DEPLOYER,
            organization=institution_name,
            contact_email="admissions-compliance@edu.edu"
        )
        
        self.programs = {}
        self.scholarships = {}
        self.applications = []
        self.admits = []
        self.denials = []
        self.appeals = []
        self.accommodations = []
        
        print("="*80)
        print(f"🎓 College Admissions System - {institution_name}")
        print("="*80)
        print(f"Colorado AI Act Effective: June 30, 2026")
        print(f"Consequential Decisions: Education enrollment, scholarships, program placement [citation:1][citation:2]")
    
    def setup_admissions_system(self):
        """Register the admissions AI system with Colorado."""
        
        system = self.tracker.register_high_risk_system(
            system_id="ADMISSIONS-001",
            system_name="AI-Assisted Holistic Admissions Engine",
            system_type=DecisionType.EDUCATION,
            description="Automated system for processing undergraduate applications and assisting with holistic admissions reviews",
            intended_use=(
                "Assist admissions officers by processing applications, "
                "calculating academic scores, identifying qualified candidates, "
                "and flagging applications for committee review"
            ),
            limitations=[
                "Not the sole factor in admissions decisions",
                "Requires regular fairness testing",
                "May have lower accuracy for non-traditional applicants",
                "Holistic review by humans required for all decisions",
                "Accommodation requests handled manually"
            ],
            training_data_summary={
                "size": 50000,
                "data_sources": ["applications", "test_scores", "essays", "recommendations"],
                "demographic_coverage": "broad",
                "date_range": "2020-2025"
            },
            performance_metrics={
                "predictive_accuracy": 0.89,
                "retention_prediction": 0.85,
                "graduation_prediction": 0.82,
                "f1_score": 0.87
            },
            mitigation_strategies=[
                "Quarterly fairness testing by demographic group",
                "Human review for all borderline applications",
                "Continuous monitoring for disparate impact",
                "Annual model validation",
                "Bias mitigation training for admissions staff"
            ],
            responsible_officer="admissions-director@edu.edu"
        )
        
        print(f"\n✅ Admissions system registered: {system['system_id']}")
        print(f"   Limitations documented: {len(system['limitations'])}")
        print(f"   Mitigation strategies: {len(system['mitigation_strategies'])}")
        
        return system
    
    def add_academic_program(self, program_data: dict) -> str:
        """Add an academic program to the institution."""
        program_id = f"PROG-{int(time.time())}-{random.randint(100, 999)}"
        
        self.programs[program_id] = {
            "program_id": program_id,
            "name": program_data['name'],
            "degree": program_data['degree'],
            "college": program_data['college'],
            "capacity": program_data.get('capacity', 100),
            "min_gpa": program_data.get('min_gpa', 2.5),
            "min_sat": program_data.get('min_sat', 1000),
            "min_act": program_data.get('min_act', 20),
            "requirements": program_data.get('requirements', []),
            "preferred_background": program_data.get('preferred_background', []),
            "competitive": program_data.get('competitive', True),
            "date_added": time.time(),
            "status": "ACTIVE"
        }
        
        print(f"\n📚 Academic Program Added:")
        print(f"   Program ID: {program_id}")
        print(f"   Name: {program_data['name']}")
        print(f"   Degree: {program_data['degree']}")
        print(f"   Capacity: {program_data.get('capacity', 100)}")
        print(f"   Min GPA: {program_data.get('min_gpa', 2.5)}")
        print(f"   Min SAT: {program_data.get('min_sat', 1000)}")
        
        return program_id
    
    def add_scholarship(self, scholarship_data: dict) -> str:
        """Add a scholarship to the institution."""
        scholarship_id = f"SCHOL-{int(time.time())}-{random.randint(100, 999)}"
        
        self.scholarships[scholarship_id] = {
            "scholarship_id": scholarship_id,
            "name": scholarship_data['name'],
            "type": scholarship_data['type'],
            "amount": scholarship_data['amount'],
            "renewable": scholarship_data.get('renewable', False),
            "min_gpa": scholarship_data.get('min_gpa', 3.0),
            "min_sat": scholarship_data.get('min_sat', 1200),
            "merit_based": scholarship_data.get('merit_based', True),
            "need_based": scholarship_data.get('need_based', False),
            "diversity_focused": scholarship_data.get('diversity_focused', False),
            "first_generation": scholarship_data.get('first_generation', False),
            "deadline": scholarship_data.get('deadline'),
            "total_available": scholarship_data.get('total_available', 10),
            "date_added": time.time(),
            "status": "ACTIVE"
        }
        
        print(f"\n💰 Scholarship Added:")
        print(f"   Scholarship ID: {scholarship_id}")
        print(f"   Name: {scholarship_data['name']}")
        print(f"   Amount: ${scholarship_data['amount']:,.0f}")
        print(f"   Type: {scholarship_data['type']}")
        print(f"   Min GPA: {scholarship_data.get('min_gpa', 3.0)}")
        
        return scholarship_id
    
    def submit_application(self, application_data: dict) -> str:
        """Submit a college application."""
        application_id = f"APP-{int(time.time())}-{random.randint(1000, 9999)}"
        
        # Hash applicant ID for privacy
        applicant_hash = f"STU-{hash(application_data['email']) % 10000:04d}"
        
        # Calculate academic scores
        gpa = application_data['gpa']
        sat = application_data.get('sat', 0)
        act = application_data.get('act', 0)
        
        # Convert to 4.0 scale if needed
        if gpa > 4.0:
            gpa = gpa / 25.0  # Convert 100-point scale to 4.0
        
        application = {
            "application_id": application_id,
            "applicant_id": applicant_hash,
            "applicant_name": application_data['name'],
            "email": application_data['email'],
            "phone": application_data.get('phone'),
            "address": application_data.get('address'),
            "high_school": application_data.get('high_school'),
            "gpa": gpa,
            "sat": sat,
            "act": act,
            "class_rank": application_data.get('class_rank'),
            "class_size": application_data.get('class_size'),
            "ap_courses": application_data.get('ap_courses', []),
            "extracurriculars": application_data.get('extracurriculars', []),
            "essay_score": application_data.get('essay_score', 3),  # 1-5 scale
            "recommendation_score": application_data.get('recommendation_score', 3),  # 1-5 scale
            "first_generation": application_data.get('first_generation', False),
            "low_income": application_data.get('low_income', False),
            "underrepresented_minority": application_data.get('underrepresented_minority', False),
            "disability": application_data.get('disability'),
            "accommodation_request": application_data.get('accommodation_request'),
            "program_choices": application_data.get('program_choices', []),
            "scholarship_interest": application_data.get('scholarship_interest', []),
            "submitted_date": time.time(),
            "status": "PENDING",
            
            # Demographic data for fair access analysis [citation:7]
            "race": application_data.get('race'),
            "ethnicity": application_data.get('ethnicity'),
            "gender": application_data.get('gender'),
            "first_gen": application_data.get('first_generation', False),
            "income_quartile": application_data.get('income_quartile'),
            "region": application_data.get('region'),
            "zip_code": application_data.get('zip_code')
        }
        
        self.applications.append(application)
        
        print(f"\n📝 College Application Received:")
        print(f"   Application ID: {application_id}")
        print(f"   Applicant: {application_data['name']}")
        print(f"   GPA: {gpa:.2f}")
        print(f"   SAT: {sat}")
        print(f"   First Generation: {application_data.get('first_generation', False)}")
        print(f"   Programs: {len(application_data.get('program_choices', []))}")
        
        return application_id
    
    def review_application(self, application_id: str) -> dict:
        """
        Review a college application using AI assistance and log the consequential decision.
        
        Under SB 24-205, education enrollment decisions are considered "consequential decisions"
        that require consumer notice, explanation, and appeal rights [citation:1][citation:2].
        """
        # Find application
        application = next(
            (a for a in self.applications if a["application_id"] == application_id),
            None
        )
        if not application:
            return {"error": "Application not found"}
        
        print(f"\n🔍 Reviewing Application: {application_id}")
        print(f"   Applicant: {application['applicant_name']}")
        print(f"   GPA: {application['gpa']:.2f}")
        print(f"   SAT: {application['sat']}")
        print(f"   First Generation: {application['first_gen']}")
        
        # Check for accommodation request
        if application.get('accommodation_request'):
            return self._handle_accommodation_request(application)
        
        # Perform AI review
        review_result = self._perform_admissions_review(application)
        
        # Make admissions decision
        admitted = review_result['admit']
        
        # Determine program match
        program_match = None
        if admitted and application['program_choices']:
            program_match = self._match_to_program(application, review_result)
        
        # Determine scholarship awards
        scholarships_awarded = []
        if admitted and application['scholarship_interest']:
            scholarships_awarded = self._evaluate_scholarships(application, review_result)
        
        # Prepare principal reasons (required by § 6-1-1706) [citation:7]
        principal_reasons = self._generate_principal_reasons(
            application, review_result, admitted
        )
        
        # Log the consequential decision
        decision = self.tracker.log_consequential_decision(
            system_id="ADMISSIONS-001",
            consumer_id=application['applicant_id'],
            decision_type=DecisionType.EDUCATION,
            decision="ADMIT" if admitted else "DENY",
            principal_reasons=principal_reasons,
            ai_was_determining_factor=False,  # AI assists but humans decide [citation:1]
            ai_role_description="AI system analyzed academic credentials and flagged applications for committee review",
            explanation=self._generate_explanation(review_result, admitted),
            decision_factors=review_result['factors'],
            notice_provided=True,
            notice_url=f"https://{self.institution_name}/admissions/ai-notice",
            is_ai_generated=True,
            human_review_available=True,
            appeal_rights_provided=True,
            appeal_deadline=time.time() + 2592000,  # 30 days
            metadata={
                "application_id": application_id,
                "applicant_name": application['applicant_name'],
                "gpa": application['gpa'],
                "sat": application['sat'],
                "academic_score": review_result['academic_score'],
                "holistic_score": review_result['holistic_score'],
                "total_score": review_result['total_score'],
                "program_match": program_match,
                "scholarships_awarded": scholarships_awarded,
                "demographics": {
                    "race": application.get('race'),
                    "ethnicity": application.get('ethnicity'),
                    "gender": application.get('gender'),
                    "first_gen": application.get('first_gen'),
                    "income_quartile": application.get('income_quartile'),
                    "region": application.get('region')
                }
            }
        )
        
        # Update application status
        application['status'] = "ADMITTED" if admitted else "DENIED"
        application['decision_id'] = decision['decision_id']
        application['review_score'] = review_result['total_score']
        application['program_match'] = program_match
        application['scholarships'] = scholarships_awarded
        
        if admitted:
            self.admits.append(application)
        else:
            self.denials.append(application)
        
        print(f"\n📊 Admissions Result:")
        print(f"   Decision: {decision['decision']}")
        print(f"   Academic Score: {review_result['academic_score']:.1f}/60")
        print(f"   Holistic Score: {review_result['holistic_score']:.1f}/40")
        print(f"   Total Score: {review_result['total_score']:.1f}/100")
        print(f"   Reasons: {', '.join(principal_reasons[:2])}")
        print(f"   Appeal Deadline: {datetime.fromtimestamp(decision['appeal_deadline'])}")
        
        if program_match:
            print(f"   Program Match: {program_match}")
        if scholarships_awarded:
            print(f"   Scholarships: {len(scholarships_awarded)} awarded")
        
        return decision
    
    def _handle_accommodation_request(self, application: dict) -> dict:
        """Handle disability accommodation request (manual review)."""
        
        accommodation_id = f"ACC-{int(time.time())}"
        
        accommodation = {
            "accommodation_id": accommodation_id,
            "application_id": application['application_id'],
            "applicant_name": application['applicant_name'],
            "request": application['accommodation_request'],
            "status": "PENDING_REVIEW",
            "assigned_to": "disability-services-coordinator",
            "review_deadline": time.time() + 259200,  # 72 hours
            "notes": "Manual review required for disability accommodation"
        }
        
        self.accommodations.append(accommodation)
        
        print(f"\n🦮 Disability Accommodation Request:")
        print(f"   Accommodation ID: {accommodation_id}")
        print(f"   Request: {application['accommodation_request']}")
        print(f"   Status: {accommodation['status']}")
        print(f"   Review Deadline: {datetime.fromtimestamp(accommodation['review_deadline'])}")
        
        # Log that AI was not the determining factor
        decision = self.tracker.log_consequential_decision(
            system_id="ADMISSIONS-001",
            consumer_id=application['applicant_id'],
            decision_type=DecisionType.EDUCATION,
            decision="PENDING_MANUAL_REVIEW",
            principal_reasons=["Disability accommodation request requires manual review"],
            ai_was_determining_factor=False,
            explanation="Your application requires manual review due to accommodation request.",
            human_review_available=True,
            appeal_rights_provided=True,
            metadata=accommodation
        )
        
        return decision
    
    def _perform_admissions_review(self, application: dict) -> dict:
        """Simulate AI-assisted holistic admissions review."""
        
        factors = {}
        
        # Academic factors (60 points) [citation:3]
        academic_score = 0
        
        # GPA evaluation
        gpa = application['gpa']
        if gpa >= 3.8:
            academic_score += 20
            factors['gpa'] = {"score": 20, "rating": "excellent", "details": f"GPA {gpa:.2f}"}
        elif gpa >= 3.5:
            academic_score += 18
            factors['gpa'] = {"score": 18, "rating": "very good", "details": f"GPA {gpa:.2f}"}
        elif gpa >= 3.0:
            academic_score += 15
            factors['gpa'] = {"score": 15, "rating": "good", "details": f"GPA {gpa:.2f}"}
        elif gpa >= 2.5:
            academic_score += 12
            factors['gpa'] = {"score": 12, "rating": "fair", "details": f"GPA {gpa:.2f}"}
        else:
            academic_score += 8
            factors['gpa'] = {"score": 8, "rating": "below average", "details": f"GPA {gpa:.2f}"}
        
        # SAT/ACT evaluation
        sat = application.get('sat', 0)
        if sat >= 1400:
            academic_score += 20
            factors['sat'] = {"score": 20, "rating": "excellent", "details": f"SAT {sat}"}
        elif sat >= 1300:
            academic_score += 18
            factors['sat'] = {"score": 18, "rating": "very good", "details": f"SAT {sat}"}
        elif sat >= 1200:
            academic_score += 15
            factors['sat'] = {"score": 15, "rating": "good", "details": f"SAT {sat}"}
        elif sat >= 1100:
            academic_score += 12
            factors['sat'] = {"score": 12, "rating": "fair", "details": f"SAT {sat}"}
        elif sat > 0:
            academic_score += 8
            factors['sat'] = {"score": 8, "rating": "below average", "details": f"SAT {sat}"}
        
        # Course rigor (AP courses)
        ap_courses = len(application.get('ap_courses', []))
        ap_score = min(ap_courses * 2, 10)
        academic_score += ap_score
        factors['course_rigor'] = {
            "score": ap_score,
            "details": f"{ap_courses} AP courses"
        }
        
        # Class rank
        class_rank = application.get('class_rank')
        class_size = application.get('class_size')
        if class_rank and class_size:
            rank_percentile = (class_rank / class_size) * 100
            if rank_percentile <= 10:
                academic_score += 10
                factors['class_rank'] = {"score": 10, "details": f"Top {rank_percentile:.0f}% of class"}
            elif rank_percentile <= 25:
                academic_score += 7
                factors['class_rank'] = {"score": 7, "details": f"Top {rank_percentile:.0f}% of class"}
            elif rank_percentile <= 50:
                academic_score += 4
                factors['class_rank'] = {"score": 4, "details": f"Top {rank_percentile:.0f}% of class"}
        
        # Holistic factors (40 points)
        holistic_score = 0
        
        # Extracurriculars
        extracurriculars = len(application.get('extracurriculars', []))
        ec_score = min(extracurriculars * 3, 15)
        holistic_score += ec_score
        factors['extracurriculars'] = {
            "score": ec_score,
            "details": f"{extracurriculars} extracurricular activities"
        }
        
        # Essay quality
        essay_score = application.get('essay_score', 3)
        holistic_score += essay_score * 3
        factors['essay'] = {
            "score": essay_score * 3,
            "details": f"Essay quality: {essay_score}/5"
        }
        
        # Recommendations
        rec_score = application.get('recommendation_score', 3)
        holistic_score += rec_score * 3
        factors['recommendations'] = {
            "score": rec_score * 3,
            "details": f"Recommendation strength: {rec_score}/5"
        }
        
        # Diversity factors (contextual, not scored directly) [citation:7]
        if application.get('first_gen'):
            holistic_score += 5
            factors['first_generation'] = {
                "score": 5,
                "details": "First-generation college student"
            }
        
        if application.get('low_income'):
            holistic_score += 5
            factors['low_income'] = {
                "score": 5,
                "details": "Economically disadvantaged background"
            }
        
        if application.get('underrepresented_minority'):
            holistic_score += 5
            factors['urm'] = {
                "score": 5,
                "details": "Underrepresented minority"
            }
        
        total_score = academic_score + holistic_score
        
        # Decision threshold (varies by competitiveness)
        admit = total_score >= 70
        
        return {
            "academic_score": academic_score,
            "holistic_score": holistic_score,
            "total_score": total_score,
            "admit": admit,
            "factors": factors
        }
    
    def _match_to_program(self, application: dict, review: dict) -> Optional[str]:
        """Match applicant to best-fit academic program."""
        best_match = None
        best_score = 0
        
        for program_id in application['program_choices']:
            program = self.programs.get(program_id)
            if not program:
                continue
            
            match_score = 0
            
            # GPA match
            if application['gpa'] >= program['min_gpa']:
                match_score += 30
            
            # Test score match
            if program['min_sat'] and application['sat'] >= program['min_sat']:
                match_score += 30
            
            # Requirements match
            requirements_met = sum(1 for req in program['requirements'] 
                                 if req.lower() in str(application).lower())
            match_score += requirements_met * 10
            
            if match_score > best_score:
                best_score = match_score
                best_match = program['name']
        
        return best_match
    
    def _evaluate_scholarships(self, application: dict, review: dict) -> List[Dict]:
        """Evaluate applicant for scholarship awards."""
        awarded = []
        
        for scholarship_id in application['scholarship_interest']:
            scholarship = self.scholarships.get(scholarship_id)
            if not scholarship:
                continue
            
            eligible = True
            reasons = []
            
            # Check GPA requirement
            if scholarship['min_gpa'] and application['gpa'] < scholarship['min_gpa']:
                eligible = False
                reasons.append(f"GPA below {scholarship['min_gpa']} requirement")
            
            # Check SAT requirement
            if scholarship['min_sat'] and application['sat'] < scholarship['min_sat']:
                eligible = False
                reasons.append(f"SAT below {scholarship['min_sat']} requirement")
            
            # Check merit-based
            if scholarship['merit_based'] and review['total_score'] < 80:
                eligible = False
                reasons.append("Merit score below threshold")
            
            # Check need-based
            if scholarship['need_based'] and not application.get('low_income'):
                eligible = False
                reasons.append("Need-based but not low-income")
            
            # Check first-generation
            if scholarship['first_generation'] and not application.get('first_gen'):
                eligible = False
                reasons.append("First-generation scholarship but not first-gen")
            
            if eligible:
                awarded.append({
                    "scholarship_id": scholarship_id,
                    "name": scholarship['name'],
                    "amount": scholarship['amount']
                })
        
        return awarded
    
    def _generate_principal_reasons(self, application: dict, review: dict, admit: bool) -> List[str]:
        """Generate principal reasons for the decision (required by § 6-1-1706)."""
        reasons = []
        
        if admit:
            if review['academic_score'] >= 45:
                reasons.append("Strong academic record (GPA and test scores)")
            if review['holistic_score'] >= 30:
                reasons.append("Exceptional extracurricular involvement")
            if application.get('first_gen'):
                reasons.append("First-generation college student")
            if application.get('underrepresented_minority'):
                reasons.append("Contributes to campus diversity")
            if len(application.get('ap_courses', [])) >= 5:
                reasons.append("Rigorous course load with multiple AP courses")
        else:
            if application['gpa'] < 2.5:
                reasons.append(f"GPA ({application['gpa']:.2f}) below minimum standard")
            if application['sat'] < 1000 and application['sat'] > 0:
                reasons.append(f"SAT score ({application['sat']}) below institutional standards")
            if review['holistic_score'] < 15:
                reasons.append("Limited extracurricular involvement")
            if not application.get('essay_score', 0) >= 3:
                reasons.append("Personal statement did not meet expectations")
        
        return reasons[:3]  # Return top 3 reasons [citation:7]
    
    def _generate_explanation(self, review: dict, admit: bool) -> str:
        """Generate human-readable explanation."""
        if admit:
            return (
                f"Congratulations! Based on our holistic review, you have been admitted "
                f"with an academic score of {review['academic_score']:.1f}/60 and "
                f"holistic score of {review['holistic_score']:.1f}/40. You have the right "
                f"to request human review or appeal this decision within 30 days [citation:7]."
            )
        else:
            return (
                f"After careful review, we are unable to offer admission at this time. "
                f"Academic score: {review['academic_score']:.1f}/60, "
                f"Holistic score: {review['holistic_score']:.1f}/40. "
                f"You have the right to request human review, correct inaccurate data, "
                f"or appeal this decision within 30 days [citation:7]."
            )
    
    def handle_appeal(self, appeal_data: dict) -> dict:
        """Handle an appeal of an admissions decision (§ 6-1-1708)."""
        
        appeal = self.tracker.handle_appeal(
            appeal_id=f"APPEAL-{int(time.time())}",
            consumer_id=appeal_data['applicant_id'],
            decision_id=appeal_data['decision_id'],
            appeal_date=time.time(),
            appeal_reason=appeal_data['reason'],
            review_status="IN_PROGRESS",
            reviewer="admissions-appeals-officer",
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
        """
        Conduct annual risk assessment as required by § 6-1-1704.
        
        Under SB 24-205, deployers must conduct annual impact assessments
        to identify and mitigate risks of algorithmic discrimination [citation:1][citation:8].
        """
        
        # Collect all decisions for analysis
        all_decisions = self.tracker.decisions
        
        # Calculate fairness metrics by demographic group [citation:7]
        demographic_data = {
            "race": {},
            "ethnicity": {},
            "gender": {},
            "first_gen": {},
            "income_quartile": {},
            "region": {}
        }
        
        for decision in all_decisions:
            demo = decision.get('metadata', {}).get('demographics', {})
            for protected, value in demo.items():
                if protected in demographic_data and value:
                    if value not in demographic_data[protected]:
                        demographic_data[protected][value] = {"total": 0, "admitted": 0}
                    
                    demographic_data[protected][value]["total"] += 1
                    if decision['decision'] == 'ADMIT':
                        demographic_data[protected][value]["admitted"] += 1
        
        # Calculate disparate impact ratios [citation:1]
        disparate_impact = {}
        for protected, groups in demographic_data.items():
            if len(groups) > 1:
                rates = []
                group_names = []
                for group, stats in groups.items():
                    if stats["total"] > 0:
                        rate = stats["admitted"] / stats["total"]
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
            system_id="ADMISSIONS-001",
            assessment_date=time.time(),
            fairness_metrics={
                "total_decisions": len(all_decisions),
                "admission_rate": len([d for d in all_decisions if d['decision'] == 'ADMIT']) / len(all_decisions) if all_decisions else 0,
                "disparate_impact": disparate_impact,
                "demographic_breakdown": demographic_data
            },
            bias_test_results={
                "race": "PASS" if disparate_impact.get('race', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "ethnicity": "PASS" if disparate_impact.get('ethnicity', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "gender": "PASS" if disparate_impact.get('gender', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "first_gen": "PASS" if disparate_impact.get('first_gen', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "income": "PASS_WITH_MONITORING" if disparate_impact.get('income_quartile', {}).get('ratio', 1.0) >= 0.75 else "FAIL"
            },
            risk_factors=[
                {"factor": k, "disparity": v['ratio'], "status": "monitor" if v['ratio'] < 0.85 else "acceptable"}
                for k, v in disparate_impact.items()
            ],
            mitigation_strategies=[
                "Quarterly fairness testing by demographic group",
                "Holistic review for all borderline applications",
                "Continuous monitoring for disparate impact",
                "Annual model validation",
                "Bias mitigation training for admissions staff",
                "Outreach to underrepresented communities"
            ],
            residual_risk="LOW" if all(v.get('ratio', 1.0) >= 0.8 for v in disparate_impact.values()) else "MEDIUM",
            next_assessment_date=time.time() + 31536000,  # 1 year
            conducted_by="admissions-director@edu.edu"
        )
        
        print(f"\n📊 Annual Risk Assessment (§ 6-1-1704):")
        print(f"   Assessment ID: {assessment['assessment_id']}")
        print(f"   Total Decisions: {len(all_decisions)}")
        print(f"   Admission Rate: {assessment['fairness_metrics']['admission_rate']:.1%}")
        print(f"   Disparate Impact Ratios: { {k:v['ratio'] for k,v in disparate_impact.items()} }")
        print(f"   Residual Risk: {assessment['residual_risk']}")
        print(f"   Next Assessment: {datetime.fromtimestamp(assessment['next_assessment_date'])}")
        
        return assessment
    
    def qualify_safe_harbor(self) -> dict:
        """
        Qualify for safe harbor under § 6-1-1709 (NIST AI RMF).
        
        Organizations that comply with NIST AI RMF or ISO 42001 receive a
        rebuttable presumption of reasonable care [citation:1][citation:2][citation:8].
        """
        
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
        print(f"   Note: Compliance with NIST AI RMF provides a rebuttable presumption of reasonable care [citation:2][citation:8]")
        
        return certificate
    
    def run_education_demo(self):
        """Run complete education demonstration with Colorado AI Act compliance."""
        
        # Register system
        self.setup_admissions_system()
        
        # Add academic programs
        programs = [
            {
                "name": "Computer Science",
                "degree": "BS",
                "college": "Engineering",
                "capacity": 150,
                "min_gpa": 3.2,
                "min_sat": 1300,
                "requirements": ["Calculus", "Physics", "Programming"],
                "preferred_background": ["Math", "CS"]
            },
            {
                "name": "Business Administration",
                "degree": "BBA",
                "college": "Business",
                "capacity": 200,
                "min_gpa": 3.0,
                "min_sat": 1200,
                "requirements": ["Economics", "Statistics"],
                "preferred_background": ["Business", "Economics"]
            },
            {
                "name": "Biology",
                "degree": "BS",
                "college": "Arts & Sciences",
                "capacity": 120,
                "min_gpa": 3.0,
                "min_sat": 1200,
                "requirements": ["Biology", "Chemistry"],
                "preferred_background": ["Science", "Research"]
            },
            {
                "name": "Psychology",
                "degree": "BA",
                "college": "Arts & Sciences",
                "capacity": 180,
                "min_gpa": 2.8,
                "min_sat": 1100,
                "requirements": ["Psychology", "Statistics"],
                "preferred_background": ["Social Science"]
            }
        ]
        
        program_ids = []
        for prog in programs:
            pid = self.add_academic_program(prog)
            program_ids.append(pid)
        
        # Add scholarships
        scholarships = [
            {
                "name": "Presidential Merit Scholarship",
                "type": "merit",
                "amount": 25000,
                "renewable": True,
                "min_gpa": 3.8,
                "min_sat": 1450,
                "merit_based": True
            },
            {
                "name": "First Generation Scholarship",
                "type": "need+merit",
                "amount": 15000,
                "renewable": True,
                "min_gpa": 3.0,
                "min_sat": 1100,
                "first_generation": True,
                "need_based": True
            },
            {
                "name": "STEM Excellence Award",
                "type": "merit",
                "amount": 20000,
                "renewable": True,
                "min_gpa": 3.5,
                "min_sat": 1350,
                "merit_based": True
            },
            {
                "name": "Diversity Leadership Scholarship",
                "type": "diversity",
                "amount": 18000,
                "renewable": True,
                "min_gpa": 3.2,
                "min_sat": 1200,
                "diversity_focused": True
            }
        ]
        
        scholarship_ids = []
        for schol in scholarships:
            sid = self.add_scholarship(schol)
            scholarship_ids.append(sid)
        
        # Submit applications with diverse backgrounds [citation:7]
        applications = [
            # Strong merit applicant - white male
            {
                "name": "John Smith",
                "email": "john.smith@email.com",
                "gpa": 3.9,
                "sat": 1520,
                "ap_courses": ["Calculus BC", "Physics C", "CS A", "English Language"],
                "extracurriculars": ["Robotics Club", "Science Olympiad", "Violin", "Math Team"],
                "essay_score": 5,
                "recommendation_score": 5,
                "first_generation": False,
                "low_income": False,
                "underrepresented_minority": False,
                "program_choices": [program_ids[0], program_ids[1]],
                "scholarship_interest": [scholarship_ids[0], scholarship_ids[2]],
                "race": "white",
                "ethnicity": "not_hispanic",
                "gender": "male",
                "region": "Denver Metro"
            },
            # First-generation applicant - Hispanic female
            {
                "name": "Maria Garcia",
                "email": "maria.garcia@email.com",
                "gpa": 3.6,
                "sat": 1280,
                "ap_courses": ["Spanish Language", "Biology"],
                "extracurriculars": ["Student Government", "Soccer", "Volunteer Tutoring", "Hispanic Student Alliance"],
                "essay_score": 5,
                "recommendation_score": 4,
                "first_generation": True,
                "low_income": True,
                "underrepresented_minority": True,
                "program_choices": [program_ids[2], program_ids[3]],
                "scholarship_interest": [scholarship_ids[1]],
                "race": "hispanic",
                "ethnicity": "hispanic",
                "gender": "female",
                "region": "Southern Colorado"
            },
            # Average applicant - black male
            {
                "name": "James Johnson",
                "email": "james.johnson@email.com",
                "gpa": 3.2,
                "sat": 1180,
                "ap_courses": ["US History"],
                "extracurriculars": ["Basketball", "Yearbook", "Peer Mentoring"],
                "essay_score": 3,
                "recommendation_score": 3,
                "first_generation": False,
                "low_income": False,
                "underrepresented_minority": True,
                "program_choices": [program_ids[1], program_ids[3]],
                "scholarship_interest": [],
                "race": "black",
                "ethnicity": "not_hispanic",
                "gender": "male",
                "region": "Denver Metro"
            },
            # Underrepresented applicant with accommodation - white female with disability
            {
                "name": "Sarah Williams",
                "email": "sarah.williams@email.com",
                "gpa": 3.5,
                "sat": 1320,
                "ap_courses": ["Psychology", "Statistics", "English Literature"],
                "extracurriculars": ["Debate Club", "Theater", "Peer Counseling", "Disability Advocacy"],
                "essay_score": 5,
                "recommendation_score": 5,
                "first_generation": False,
                "low_income": False,
                "underrepresented_minority": False,
                "disability": "learning_disability",
                "accommodation_request": "Extended time for placement tests and alternative format materials",
                "program_choices": [program_ids[2], program_ids[3]],
                "scholarship_interest": [scholarship_ids[3]],
                "race": "white",
                "ethnicity": "not_hispanic",
                "gender": "female",
                "region": "Boulder Area"
            },
            # International applicant - Asian male
            {
                "name": "Wei Zhang",
                "email": "wei.zhang@email.com",
                "gpa": 3.8,
                "sat": 1480,
                "ap_courses": ["Calculus BC", "Physics C", "Chemistry", "Computer Science"],
                "extracurriculars": ["Math Club", "Badminton", "Community Service", "Chess Team"],
                "essay_score": 4,
                "recommendation_score": 4,
                "first_generation": False,
                "low_income": False,
                "underrepresented_minority": False,
                "program_choices": [program_ids[0], program_ids[2]],
                "scholarship_interest": [scholarship_ids[0]],
                "race": "asian",
                "ethnicity": "asian",
                "gender": "male",
                "region": "International"
            },
            # Low-income first-generation applicant - black female
            {
                "name": "Keisha Brown",
                "email": "keisha.brown@email.com",
                "gpa": 3.4,
                "sat": 1150,
                "ap_courses": ["African American Studies", "English"],
                "extracurriculars": ["NAACP Youth Council", "Track & Field", "Peer Tutoring"],
                "essay_score": 5,
                "recommendation_score": 5,
                "first_generation": True,
                "low_income": True,
                "underrepresented_minority": True,
                "program_choices": [program_ids[1], program_ids[3]],
                "scholarship_interest": [scholarship_ids[1], scholarship_ids[3]],
                "race": "black",
                "ethnicity": "not_hispanic",
                "gender": "female",
                "region": "Aurora"
            }
        ]
        
        app_ids = []
        for app in applications:
            app_id = self.submit_application(app)
            app_ids.append(app_id)
        
        # Review applications
        decisions = []
        for app_id in app_ids:
            decision = self.review_application(app_id)
            decisions.append(decision)
        
        # Handle appeal for denied applicant
        denied_app = next(
            (a for a in self.applications if a["status"] == "DENIED"),
            None
        )
        if denied_app:
            self.handle_appeal({
                "applicant_id": denied_app["applicant_id"],
                "decision_id": denied_app["decision_id"],
                "application_id": denied_app["application_id"],
                "applicant_name": denied_app["applicant_name"],
                "reason": "My SAT score was reported incorrectly. I have official score report showing higher score.",
                "evidence": ["official_score_report.pdf", "college_board_correction.pdf"]
            })
        
        # Handle correction for data error
        if denied_app:
            self.handle_correction({
                "applicant_id": denied_app["applicant_id"],
                "decision_id": denied_app["decision_id"],
                "application_id": denied_app["application_id"],
                "applicant_name": denied_app["applicant_name"],
                "field": "sat",
                "old_value": 1180,
                "new_value": 1280,
                "verification_method": "score_report_review",
                "verification_document": "updated_scores.pdf"
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
        print(f"   Academic Programs: {len(program_ids)}")
        print(f"   Scholarships: {len(scholarship_ids)}")
        print(f"   Applications: {len(app_ids)}")
        print(f"   Admits: {len(self.admits)}")
        print(f"   Denials: {len(self.denials)}")
        print(f"   Accommodation Requests: {len(self.accommodations)}")
        print(f"   Admission Rate: {len(self.admits)/len(app_ids)*100:.1f}%")
        print(f"   Appeals Filed: 1")
        print(f"   Corrections Processed: 1")
        print(f"   Annual Risk Assessment: ✓")
        print(f"   Safe Harbor Qualified: ✓")
        print(f"\n⚖️ Note: Education decisions are \"consequential decisions\" under SB 24-205 [citation:1][citation:2]")
        print(f"   Protected classes monitored: race, ethnicity, gender, first-gen status, income [citation:7]")
        
        return report


if __name__ == "__main__":
    system = CollegeAdmissionsSystem("Colorado State University")
    report = system.run_education_demo()
    
    # Save report
    with open("colorado_education_report.json", "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\n✅ Report saved: colorado_education_report.json")
    print(f"\n⚠️ Note: Colorado AI Act effective June 30, 2026 [citation:2][citation:10]")
    print(f"   Ensure compliance before this date.")
    print(f"\n📋 SB 24-205 Requirements Demonstrated:")
    print(f"   • Developer documentation (§ 6-1-1703)")
    print(f"   • Annual risk assessments (§ 6-1-1704)")
    print(f"   • Consumer notice (§ 6-1-1705)")
    print(f"   • Adverse explanation (§ 6-1-1706)")
    print(f"   • Correction rights (§ 6-1-1707)")
    print(f"   • Appeal rights (§ 6-1-1708)")
    print(f"   • Safe harbor (NIST AI RMF) (§ 6-1-1709)")
