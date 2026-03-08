#!/usr/bin/env python3
"""
Colorado AI Act - Employment Decisions Example
=================================================

This example demonstrates a complete employment screening system
that complies with Colorado's Artificial Intelligence Act (SB 24-205),
covering:

- Resume screening and candidate ranking
- Hiring decisions and adverse actions
- Annual risk assessments
- Consumer notice and explanations
- Correction and appeal rights
- Safe harbor qualification (NIST AI RMF)
"""

import json
import time
import sys
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


class EmploymentScreeningSystem:
    """
    Complete employment screening system with Colorado AI Act compliance.
    
    Features:
    - Resume screening and ranking
    - Candidate shortlisting
    - Adverse action notifications
    - Appeal processing
    - Data correction
    - Annual risk assessments
    - Fair hiring metrics
    """
    
    def __init__(self, company_name: str):
        self.company_name = company_name
        self.tracker = ColoradoAITracker(
            entity_type=EntityType.DEPLOYER,
            organization=company_name,
            contact_email="hr-compliance@company.com"
        )
        
        self.job_postings = {}
        self.candidates = {}
        self.applications = []
        
        print("="*80)
        print(f"👔 Employment Screening System - {company_name}")
        print("="*80)
        print(f"Colorado AI Act Effective: June 30, 2026")
    
    def setup_hiring_system(self):
        """Register the hiring AI system with Colorado."""
        
        system = self.tracker.register_high_risk_system(
            system_id="HR-SCREEN-001",
            system_name="AI-Powered Resume Screener",
            system_type=DecisionType.EMPLOYMENT,
            description="Automated system for screening and ranking job applicants",
            intended_use=(
                "Assist HR professionals by screening resumes, "
                "ranking candidates, and identifying top candidates "
                "for further review"
            ),
            limitations=[
                "Not validated for executive-level positions",
                "May have lower accuracy for non-traditional career paths",
                "Requires regular bias testing",
                "Should not be the sole factor in hiring decisions",
                "Not suitable for positions requiring human judgment assessment"
            ],
            training_data_summary={
                "size": 50000,
                "demographics": "broad",
                "industries": ["tech", "finance", "healthcare", "retail"],
                "date_range": "2020-2025"
            },
            performance_metrics={
                "accuracy": 0.94,
                "precision": 0.93,
                "recall": 0.95,
                "f1_score": 0.94
            },
            mitigation_strategies=[
                "Quarterly bias testing",
                "Human review for all final decisions",
                "Continuous monitoring for drift",
                "Annual fairness audit"
            ],
            responsible_officer="hr-director@company.com"
        )
        
        print(f"\n✅ Hiring system registered: {system['system_id']}")
        print(f"   Limitations documented: {len(system['limitations'])}")
        print(f"   Mitigation strategies: {len(system['mitigation_strategies'])}")
        
        return system
    
    def create_job_posting(self, job_data: dict) -> str:
        """Create a new job posting."""
        job_id = f"JOB-{int(time.time())}-{hash(job_data['title']) % 1000:03d}"
        
        self.job_postings[job_id] = {
            "job_id": job_id,
            "title": job_data['title'],
            "department": job_data['department'],
            "location": job_data['location'],
            "requirements": job_data['requirements'],
            "preferred_qualifications": job_data.get('preferred', []),
            "salary_range": job_data.get('salary_range'),
            "posted_date": time.time(),
            "status": "OPEN"
        }
        
        print(f"\n📋 Job Posted: {job_data['title']}")
        print(f"   Job ID: {job_id}")
        print(f"   Location: {job_data['location']}")
        print(f"   Requirements: {len(job_data['requirements'])} items")
        
        return job_id
    
    def submit_application(self, application_data: dict) -> str:
        """Submit a job application."""
        application_id = f"APP-{int(time.time())}-{hash(application_data['email']) % 10000:04d}"
        
        # Hash candidate ID for privacy
        candidate_hash = f"CAND-{hash(application_data['email']) % 10000:04d}"
        
        self.candidates[candidate_hash] = {
            "candidate_id": candidate_hash,
            "name": application_data['name'],
            "email": application_data['email'],
            "phone": application_data.get('phone'),
            "location": application_data.get('location'),
            "resume_text": application_data['resume_text'],
            "years_experience": application_data['years_experience'],
            "education": application_data['education'],
            "skills": application_data['skills'],
            "current_title": application_data.get('current_title'),
            "notice_period": application_data.get('notice_period', 30),
            
            # Demographic data for fair hiring analysis
            "race": application_data.get('race'),
            "gender": application_data.get('gender'),
            "age": application_data.get('age'),
            "veteran_status": application_data.get('veteran_status'),
            "disability": application_data.get('disability')
        }
        
        self.applications.append({
            "application_id": application_id,
            "job_id": application_data['job_id'],
            "candidate_id": candidate_hash,
            "submitted_date": time.time(),
            "status": "PENDING"
        })
        
        print(f"\n📝 Application Received:")
        print(f"   Application ID: {application_id}")
        print(f"   Candidate: {application_data['name']}")
        print(f"   Job: {self.job_postings[application_data['job_id']]['title']}")
        print(f"   Experience: {application_data['years_experience']} years")
        
        return application_id
    
    def screen_application(self, application_id: str) -> dict:
        """
        Screen an application using AI and log the consequential decision.
        """
        # Find application
        application = next(
            (a for a in self.applications if a["application_id"] == application_id),
            None
        )
        if not application:
            return {"error": "Application not found"}
        
        candidate = self.candidates.get(application["candidate_id"])
        job = self.job_postings.get(application["job_id"])
        
        print(f"\n🔍 Screening Application: {application_id}")
        print(f"   Candidate: {candidate['name']}")
        print(f"   Job: {job['title']}")
        print(f"   Experience: {candidate['years_experience']} years")
        
        # Perform AI screening
        screening_result = self._perform_ai_screening(candidate, job)
        
        # Determine if advanced to next round
        advances = screening_result['score'] >= 70
        
        # Prepare principal reasons (required by § 6-1-1706)
        principal_reasons = self._generate_principal_reasons(
            candidate, job, screening_result, advances
        )
        
        # Log the consequential decision with full compliance
        decision = self.tracker.log_consequential_decision(
            system_id="HR-SCREEN-001",
            consumer_id=candidate['candidate_id'],
            decision_type=DecisionType.EMPLOYMENT,
            decision="ADVANCE" if advances else "REJECT",
            principal_reasons=principal_reasons,
            ai_was_determining_factor=True,
            ai_role_description="AI system screened resumes and ranked candidates based on job requirements",
            explanation=self._generate_explanation(screening_result, advances),
            decision_factors=screening_result['factors'],
            notice_provided=True,
            notice_url=f"https://{self.company_name}/ai-notice",
            is_ai_generated=True,
            human_review_available=True,
            appeal_rights_provided=True,
            appeal_deadline=time.time() + 2592000,  # 30 days
            metadata={
                "application_id": application_id,
                "job_id": job['job_id'],
                "job_title": job['title'],
                "candidate_name": candidate['name'],
                "screening_score": screening_result['score'],
                "screening_details": screening_result,
                "demographics": {
                    "race": candidate.get('race'),
                    "gender": candidate.get('gender'),
                    "age": candidate.get('age'),
                    "veteran_status": candidate.get('veteran_status'),
                    "disability": candidate.get('disability')
                }
            }
        )
        
        # Update application status
        application['status'] = "ADVANCED" if advances else "REJECTED"
        application['decision_id'] = decision['decision_id']
        application['screening_score'] = screening_result['score']
        
        print(f"\n📊 Screening Result:")
        print(f"   Decision: {decision['decision']}")
        print(f"   Score: {screening_result['score']:.1f}/100")
        print(f"   Reasons: {', '.join(principal_reasons[:2])}...")
        print(f"   Appeal Deadline: {datetime.fromtimestamp(decision['appeal_deadline'])}")
        
        return decision
    
    def _perform_ai_screening(self, candidate: dict, job: dict) -> dict:
        """Simulate AI screening of candidate against job requirements."""
        
        score = 0
        factors = {}
        
        # Experience match (0-40 points)
        required_exp = job['requirements'].get('min_experience', 2)
        exp_match = min(candidate['years_experience'] / required_exp, 1.5)
        exp_score = min(exp_match * 30, 40)
        score += exp_score
        factors['experience'] = {
            "score": exp_score,
            "value": candidate['years_experience'],
            "threshold": required_exp,
            "details": f"{candidate['years_experience']} years vs {required_exp} required"
        }
        
        # Education match (0-25 points)
        edu_levels = {"high_school": 1, "associate": 2, "bachelor": 3, "master": 4, "phd": 5}
        required_edu = edu_levels.get(job['requirements'].get('education', 'bachelor'), 3)
        candidate_edu = edu_levels.get(candidate['education'], 0)
        edu_match = min(candidate_edu / required_edu, 1.0)
        edu_score = edu_match * 25
        score += edu_score
        factors['education'] = {
            "score": edu_score,
            "value": candidate['education'],
            "threshold": job['requirements'].get('education', 'bachelor'),
            "details": f"Education: {candidate['education']} vs {job['requirements'].get('education', 'bachelor')}"
        }
        
        # Skills match (0-25 points)
        required_skills = set(job['requirements'].get('skills', []))
        candidate_skills = set(candidate['skills'])
        matching_skills = required_skills.intersection(candidate_skills)
        skills_match = len(matching_skills) / len(required_skills) if required_skills else 1.0
        skills_score = skills_match * 25
        score += skills_score
        factors['skills'] = {
            "score": skills_score,
            "matching": list(matching_skills),
            "missing": list(required_skills - candidate_skills),
            "details": f"{len(matching_skills)}/{len(required_skills)} required skills matched"
        }
        
        # Location preference (0-10 points)
        if job['location'] in candidate.get('location', ''):
            score += 10
            factors['location'] = {
                "score": 10,
                "details": "Local candidate"
            }
        else:
            factors['location'] = {
                "score": 0,
                "details": "Non-local candidate"
            }
        
        return {
            "score": score,
            "factors": factors,
            "experience_match": exp_match,
            "education_match": edu_match,
            "skills_match": skills_match
        }
    
    def _generate_principal_reasons(self, candidate: dict, job: dict,
                                   screening: dict, advances: bool) -> List[str]:
        """Generate principal reasons for the decision (required by § 6-1-1706)."""
        reasons = []
        
        if advances:
            if screening['experience_match'] >= 1.0:
                reasons.append(f"Meets or exceeds experience requirements ({candidate['years_experience']} years)")
            if screening['education_match'] >= 1.0:
                reasons.append(f"Meets education requirements ({candidate['education']})")
            if screening['skills_match'] >= 0.8:
                reasons.append(f"Matches {screening['skills_match']*100:.0f}% of required skills")
        else:
            if screening['experience_match'] < 0.8:
                reasons.append(f"Experience ({candidate['years_experience']} years) below minimum requirement ({job['requirements'].get('min_experience', 2)} years)")
            if screening['education_match'] < 0.8:
                reasons.append(f"Education ({candidate['education']}) below preferred level ({job['requirements'].get('education', 'bachelor')})")
            if screening['skills_match'] < 0.6:
                reasons.append(f"Only {screening['skills_match']*100:.0f}% of required skills matched")
        
        return reasons[:3]  # Return top 3 reasons
    
    def _generate_explanation(self, screening: dict, advances: bool) -> str:
        """Generate human-readable explanation."""
        if advances:
            return (
                f"Your application advanced to the next round with a score of "
                f"{screening['score']:.1f}/100. You meet or exceed the minimum requirements "
                f"for this position based on the criteria above."
            )
        else:
            return (
                f"Your application was not selected to advance at this time. "
                f"Score: {screening['score']:.1f}/100. Please see the principal "
                f"reasons above for more information. You have the right to request "
                f"human review or appeal this decision within 30 days."
            )
    
    def handle_appeal(self, appeal_data: dict) -> dict:
        """Handle an appeal from a rejected candidate (§ 6-1-1708)."""
        
        appeal = self.tracker.handle_appeal(
            appeal_id=f"APPEAL-{int(time.time())}",
            consumer_id=appeal_data['candidate_id'],
            decision_id=appeal_data['decision_id'],
            appeal_date=time.time(),
            appeal_reason=appeal_data['reason'],
            review_status="IN_PROGRESS",
            reviewer="hr-appeals-officer",
            appeal_deadline=time.time() + 604800,  # 7 days
            evidence_submitted=appeal_data.get('evidence', []),
            metadata={
                "application_id": appeal_data['application_id'],
                "candidate_name": appeal_data['candidate_name']
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
            consumer_id=correction_data['candidate_id'],
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
                "candidate_name": correction_data['candidate_name']
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
        
        # Calculate fairness metrics
        total_decisions = len(all_decisions)
        approvals = len([d for d in all_decisions if d['decision'] == 'ADVANCE'])
        
        # Demographic breakdown
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
                    if decision['decision'] == 'ADVANCE':
                        demographic_data[key][value]["approved"] += 1
        
        # Calculate disparate impact
        disparate_impact = {}
        for dim, groups in demographic_data.items():
            if len(groups) > 1:
                rates = []
                for group, stats in groups.items():
                    if stats["total"] > 0:
                        rate = stats["approved"] / stats["total"]
                        rates.append(rate)
                if len(rates) > 1:
                    disparate_impact[dim] = min(rates) / max(rates) if max(rates) > 0 else 1.0
        
        assessment = self.tracker.conduct_risk_assessment(
            system_id="HR-SCREEN-001",
            assessment_date=time.time(),
            fairness_metrics={
                "total_decisions": total_decisions,
                "approval_rate": approvals / total_decisions if total_decisions > 0 else 0,
                "disparate_impact": disparate_impact,
                "demographic_breakdown": demographic_data
            },
            bias_test_results={
                "race": "PASS" if disparate_impact.get('race', 1.0) >= 0.8 else "FAIL",
                "gender": "PASS" if disparate_impact.get('gender', 1.0) >= 0.8 else "FAIL",
                "age": "PASS_WITH_MONITORING" if disparate_impact.get('age', 1.0) >= 0.75 else "FAIL"
            },
            risk_factors=[
                {"factor": k, "disparity": v, "status": "monitor" if v < 0.85 else "acceptable"}
                for k, v in disparate_impact.items()
            ],
            mitigation_strategies=[
                "Quarterly bias testing",
                "Human review for all final decisions",
                "Continuous monitoring for drift",
                "Annual fairness audit",
                "Bias mitigation training for model"
            ],
            residual_risk="LOW" if all(v >= 0.8 for v in disparate_impact.values()) else "MEDIUM",
            next_assessment_date=time.time() + 31536000,  # 1 year
            conducted_by="compliance-officer@company.com"
        )
        
        print(f"\n📊 Annual Risk Assessment (§ 6-1-1704):")
        print(f"   Assessment ID: {assessment['assessment_id']}")
        print(f"   Total Decisions: {total_decisions}")
        print(f"   Approval Rate: {approvals/total_decisions*100:.1f}%")
        print(f"   Disparate Impact Ratios: {disparate_impact}")
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
            certificate_url=f"https://{self.company_name}/compliance/nist-certificate"
        )
        
        print(f"\n🛡️ Safe Harbor Certificate (§ 6-1-1709):")
        print(f"   Certificate ID: {certificate['certificate_id']}")
        print(f"   Framework: {certificate['framework']}")
        print(f"   Certified By: {certificate['certified_by']}")
        print(f"   Expires: {datetime.fromtimestamp(certificate['expiry_date'])}")
        
        return certificate
    
    def generate_attorney_general_report(self) -> dict:
        """Generate comprehensive report for Colorado Attorney General."""
        
        report = self.tracker.generate_compliance_report(
            start_date="2026-01-01",
            end_date="2026-12-31",
            include_risk_assessments=True,
            include_consequential_decisions=True,
            include_appeals=True,
            include_corrections=True
        )
        
        print(f"\n📋 Attorney General Report Generated:")
        print(f"   Report ID: {report['report_id']}")
        print(f"   Systems: {report['statistics']['total_systems']}")
        print(f"   Assessments: {report['statistics']['total_assessments']}")
        print(f"   Decisions: {report['statistics']['total_decisions']}")
        print(f"   Corrections: {report['statistics']['total_corrections']}")
        print(f"   Appeals: {report['statistics']['total_appeals']}")
        print(f"   Compliance Status: {report['compliance_summary']['risk_assessments']['status']}")
        
        return report
    
    def run_hiring_demo(self):
        """Run complete hiring demonstration with Colorado AI Act compliance."""
        
        # Register system
        self.setup_hiring_system()
        
        # Create job postings
        jobs = [
            {
                "title": "Senior Software Engineer",
                "department": "Engineering",
                "location": "Denver, CO",
                "requirements": {
                    "min_experience": 5,
                    "education": "bachelor",
                    "skills": ["Python", "JavaScript", "AWS", "Docker", "Kubernetes"]
                },
                "preferred": ["Go", "Rust", "Machine Learning"],
                "salary_range": "120000-160000"
            },
            {
                "title": "Product Manager",
                "department": "Product",
                "location": "Boulder, CO",
                "requirements": {
                    "min_experience": 3,
                    "education": "bachelor",
                    "skills": ["Product Strategy", "Agile", "User Research", "Analytics"]
                },
                "preferred": ["PMP", "CSPO", "Technical Background"],
                "salary_range": "100000-140000"
            },
            {
                "title": "Data Scientist",
                "department": "Analytics",
                "location": "Colorado Springs, CO",
                "requirements": {
                    "min_experience": 2,
                    "education": "master",
                    "skills": ["Python", "SQL", "Machine Learning", "Statistics"]
                },
                "preferred": ["TensorFlow", "PyTorch", "Spark"],
                "salary_range": "110000-150000"
            }
        ]
        
        job_ids = []
        for job in jobs:
            job_id = self.create_job_posting(job)
            job_ids.append(job_id)
        
        # Submit applications with diverse demographics
        applications = [
            # Strong candidate
            {
                "job_id": job_ids[0],
                "name": "John Smith",
                "email": "john.smith@email.com",
                "phone": "303-555-1234",
                "location": "Denver, CO",
                "resume_text": "...",
                "years_experience": 8,
                "education": "master",
                "skills": ["Python", "JavaScript", "AWS", "Docker", "Kubernetes", "Go"],
                "current_title": "Lead Engineer",
                "race": "white",
                "gender": "male",
                "age": 42
            },
            # Qualified candidate
            {
                "job_id": job_ids[0],
                "name": "Maria Garcia",
                "email": "maria.garcia@email.com",
                "phone": "720-555-5678",
                "location": "Boulder, CO",
                "resume_text": "...",
                "years_experience": 6,
                "education": "bachelor",
                "skills": ["Python", "JavaScript", "AWS", "Docker"],
                "current_title": "Software Engineer",
                "race": "hispanic",
                "gender": "female",
                "age": 35
            },
            # Underrepresented candidate
            {
                "job_id": job_ids[0],
                "name": "James Johnson",
                "email": "james.johnson@email.com",
                "phone": "719-555-9012",
                "location": "Colorado Springs, CO",
                "resume_text": "...",
                "years_experience": 5,
                "education": "bachelor",
                "skills": ["Python", "JavaScript", "AWS"],
                "current_title": "Software Developer",
                "race": "black",
                "gender": "male",
                "age": 38
            },
            # Entry-level candidate (may be rejected)
            {
                "job_id": job_ids[2],
                "name": "Sarah Chen",
                "email": "sarah.chen@email.com",
                "phone": "970-555-3456",
                "location": "Fort Collins, CO",
                "resume_text": "...",
                "years_experience": 1,
                "education": "bachelor",
                "skills": ["Python", "SQL", "Statistics"],
                "current_title": "Junior Analyst",
                "race": "asian",
                "gender": "female",
                "age": 24
            }
        ]
        
        app_ids = []
        for app in applications:
            app_id = self.submit_application(app)
            app_ids.append(app_id)
        
        # Screen applications
        decisions = []
        for app_id in app_ids:
            decision = self.screen_application(app_id)
            decisions.append(decision)
        
        # Handle appeal for rejected candidate
        rejected_app = next(
            (a for a in self.applications if a["status"] == "REJECTED"),
            None
        )
        if rejected_app:
            candidate = self.candidates.get(rejected_app["candidate_id"])
            if candidate:
                appeal = self.handle_appeal({
                    "candidate_id": rejected_app["candidate_id"],
                    "decision_id": rejected_app["decision_id"],
                    "application_id": rejected_app["application_id"],
                    "candidate_name": candidate['name'],
                    "reason": "My experience was miscalculated. I have 2 years of relevant internship experience.",
                    "evidence": ["internship_letters.pdf", "project_portfolio.pdf"]
                })
                
                # Resolve appeal
                self.resolve_appeal(
                    appeal_id=appeal['appeal_id'],
                    resolution="UPHELD",
                    notes="Candidate's internship experience qualifies as relevant experience. Original decision overturned."
                )
        
        # Handle correction for data error
        if rejected_app and candidate:
            self.handle_correction({
                "candidate_id": rejected_app["candidate_id"],
                "decision_id": rejected_app["decision_id"],
                "application_id": rejected_app["application_id"],
                "candidate_name": candidate['name'],
                "field": "years_experience",
                "old_value": 1,
                "new_value": 2,
                "verification_method": "document_review",
                "verification_document": "internship_letters.pdf"
            })
        
        # Conduct annual risk assessment
        self.conduct_annual_risk_assessment()
        
        # Qualify for safe harbor
        self.qualify_safe_harbor()
        
        # Generate Attorney General report
        report = self.generate_attorney_general_report()
        
        print("\n" + "="*80)
        print("📊 Colorado AI Act Compliance Summary")
        print("="*80)
        print(f"   Job Postings: {len(job_ids)}")
        print(f"   Applications: {len(app_ids)}")
        print(f"   Advanced: {len([d for d in decisions if d['decision'] == 'ADVANCE'])}")
        print(f"   Rejected: {len([d for d in decisions if d['decision'] == 'REJECT'])}")
        print(f"   Appeals Filed: 1")
        print(f"   Corrections Processed: 1")
        print(f"   Annual Risk Assessment: ✓")
        print(f"   Safe Harbor Qualified: ✓")
        
        return report


if __name__ == "__main__":
    system = EmploymentScreeningSystem("Colorado Tech Solutions")
    report = system.run_hiring_demo()
    
    # Save report
    with open("colorado_employment_report.json", "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\n✅ Report saved: colorado_employment_report.json")
    print(f"\n⚠️ Note: Colorado AI Act effective June 30, 2026")
    print(f"   Ensure compliance before this date.")
