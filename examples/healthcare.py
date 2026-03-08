#!/usr/bin/env python3
"""
Colorado AI Act - Healthcare Decisions Example
=================================================

This example demonstrates a complete clinical decision support system
that complies with Colorado's Artificial Intelligence Act (SB 24-205),
covering:

- Diagnosis assistance
- Treatment recommendations
- Patient risk stratification
- Insurance coverage determinations
- Clinical trial matching
- Health equity monitoring
- Appeal and second opinion workflows
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


class ClinicalDecisionSupportSystem:
    """
    Complete clinical decision support system with Colorado AI Act compliance.
    
    Features:
    - AI-assisted diagnosis
    - Treatment recommendations
    - Patient risk scoring
    - Insurance coverage decisions
    - Clinical trial matching
    - Health equity monitoring
    - Appeal and second opinion workflows
    - Annual risk assessments
    """
    
    def __init__(self, healthcare_system: str):
        self.healthcare_system = healthcare_system
        self.tracker = ColoradoAITracker(
            entity_type=EntityType.DEPLOYER,
            organization=healthcare_system,
            contact_email="clinical-ai-compliance@health.org"
        )
        
        self.patients = {}
        self.diagnoses = []
        self.treatment_plans = []
        self.insurance_decisions = []
        self.clinical_trials = {}
        self.appeals = []
        
        print("="*80)
        print(f"🏥 Clinical Decision Support System - {healthcare_system}")
        print("="*80)
        print(f"Colorado AI Act Effective: June 30, 2026")
    
    def setup_clinical_system(self):
        """Register the clinical decision support system with Colorado."""
        
        system = self.tracker.register_high_risk_system(
            system_id="CLINICAL-DSS-001",
            system_name="AI-Powered Clinical Decision Support System",
            system_type=DecisionType.HEALTHCARE,
            description="AI system for assisting clinicians with diagnosis, treatment recommendations, and patient risk assessment",
            intended_use=(
                "Assist healthcare providers by analyzing patient data, "
                "suggesting possible diagnoses, recommending evidence-based "
                "treatments, and identifying high-risk patients"
            ),
            limitations=[
                "Not a replacement for clinical judgment",
                "Requires regular validation on diverse populations",
                "May have lower accuracy for rare conditions",
                "Must be used by licensed healthcare providers",
                "Final medical decisions require physician review"
            ],
            training_data_summary={
                "size": 100000,
                "data_sources": ["EHR", "clinical_trials", "medical_literature"],
                "demographics": "broad",
                "date_range": "2015-2025"
            },
            performance_metrics={
                "diagnosis_accuracy": 0.94,
                "treatment_recommendation_accuracy": 0.91,
                "risk_prediction_accuracy": 0.89,
                "f1_score": 0.92
            },
            mitigation_strategies=[
                "Quarterly validation on diverse populations",
                "Physician review for all recommendations",
                "Continuous monitoring for bias",
                "Annual model validation",
                "Health equity training"
            ],
            responsible_officer="chief-medical-officer@health.org"
        )
        
        print(f"\n✅ Clinical decision system registered: {system['system_id']}")
        print(f"   Limitations documented: {len(system['limitations'])}")
        print(f"   Mitigation strategies: {len(system['mitigation_strategies'])}")
        
        return system
    
    def add_patient(self, patient_data: dict) -> str:
        """Add a patient to the system."""
        patient_id = f"PT-{int(time.time())}-{random.randint(1000, 9999)}"
        
        # Hash for privacy (HIPAA compliance)
        patient_hash = f"PT-{hash(patient_data['name'] + patient_data['mrn']) % 10000:04d}"
        
        self.patients[patient_id] = {
            "patient_id": patient_id,
            "hash": patient_hash,
            "name": patient_data['name'],
            "mrn": patient_data['mrn'],
            "age": patient_data['age'],
            "gender": patient_data.get('gender'),
            "race": patient_data.get('race'),
            "ethnicity": patient_data.get('ethnicity'),
            "zip_code": patient_data.get('zip_code'),
            "insurance": patient_data.get('insurance'),
            "primary_care_physician": patient_data.get('primary_care_physician'),
            "medical_history": patient_data.get('medical_history', []),
            "medications": patient_data.get('medications', []),
            "allergies": patient_data.get('allergies', []),
            "vital_signs": patient_data.get('vital_signs', {}),
            "lab_results": patient_data.get('lab_results', {}),
            "imaging_results": patient_data.get('imaging_results', {}),
            "created_date": time.time()
        }
        
        print(f"\n👤 Patient Added:")
        print(f"   Patient ID: {patient_id}")
        print(f"   Name: {patient_data['name']}")
        print(f"   Age: {patient_data['age']}")
        print(f"   Race: {patient_data.get('race', 'Unknown')}")
        print(f"   Insurance: {patient_data.get('insurance', 'Unknown')}")
        
        return patient_id
    
    def add_clinical_trial(self, trial_data: dict) -> str:
        """Add a clinical trial to the system."""
        trial_id = f"TRIAL-{int(time.time())}-{random.randint(10, 99)}"
        
        self.clinical_trials[trial_id] = {
            "trial_id": trial_id,
            "name": trial_data['name'],
            "phase": trial_data['phase'],
            "condition": trial_data['condition'],
            "eligibility_criteria": trial_data['eligibility_criteria'],
            "inclusion_criteria": trial_data.get('inclusion_criteria', []),
            "exclusion_criteria": trial_data.get('exclusion_criteria', []),
            "locations": trial_data.get('locations', []),
            "principal_investigator": trial_data.get('principal_investigator'),
            "sponsor": trial_data.get('sponsor'),
            "status": trial_data.get('status', 'RECRUITING'),
            "created_date": time.time()
        }
        
        print(f"\n🔬 Clinical Trial Added:")
        print(f"   Trial ID: {trial_id}")
        print(f"   Name: {trial_data['name']}")
        print(f"   Phase: {trial_data['phase']}")
        print(f"   Condition: {trial_data['condition']}")
        
        return trial_id
    
    def conduct_diagnosis_assistance(self, patient_id: str, symptoms: List[str], 
                                     physician: str) -> dict:
        """
        Provide AI-assisted diagnosis suggestions.
        """
        patient = self.patients.get(patient_id)
        if not patient:
            return {"error": "Patient not found"}
        
        print(f"\n🔍 Conducting Diagnosis Assistance:")
        print(f"   Patient: {patient['name']}")
        print(f"   Physician: {physician}")
        print(f"   Symptoms: {', '.join(symptoms)}")
        
        # Perform differential diagnosis
        diagnosis_result = self._generate_differential_diagnosis(patient, symptoms)
        
        # Prepare principal reasons (required by § 6-1-1706)
        principal_reasons = [
            f"Primary diagnosis: {diagnosis_result['primary_diagnosis']['name']} "
            f"(confidence: {diagnosis_result['primary_diagnosis']['confidence']:.1f}%)",
            f"Supported by: {', '.join(diagnosis_result['supporting_evidence'][:2])}"
        ]
        
        # Log the consequential decision
        decision = self.tracker.log_consequential_decision(
            system_id="CLINICAL-DSS-001",
            consumer_id=patient_id,
            decision_type=DecisionType.HEALTHCARE,
            decision=f"Diagnosis Suggestions",
            principal_reasons=principal_reasons,
            ai_was_determining_factor=False,  # AI assists, physician decides
            ai_role_description="AI system analyzed symptoms and patient data to suggest possible diagnoses",
            explanation=diagnosis_result['explanation'],
            decision_factors=diagnosis_result['factors'],
            notice_provided=True,
            notice_url=f"https://{self.healthcare_system}/ai-notice",
            is_ai_generated=True,
            human_review_available=True,
            appeal_rights_provided=True,
            appeal_deadline=time.time() + 2592000,  # 30 days
            metadata={
                "patient_id": patient_id,
                "patient_age": patient['age'],
                "patient_race": patient.get('race'),
                "patient_ethnicity": patient.get('ethnicity'),
                "symptoms": symptoms,
                "physician": physician,
                "primary_diagnosis": diagnosis_result['primary_diagnosis'],
                "differential_diagnoses": diagnosis_result['differential'][:3],
                "confidence_level": diagnosis_result['primary_diagnosis']['confidence'],
                "recommended_tests": diagnosis_result.get('recommended_tests', [])
            }
        )
        
        # Store diagnosis
        diagnosis_record = {
            "diagnosis_id": f"DX-{int(time.time())}",
            "patient_id": patient_id,
            "physician": physician,
            "symptoms": symptoms,
            "primary_diagnosis": diagnosis_result['primary_diagnosis'],
            "differential": diagnosis_result['differential'][:3],
            "decision_id": decision['decision_id'],
            "timestamp": time.time()
        }
        
        self.diagnoses.append(diagnosis_record)
        
        print(f"\n📋 Diagnosis Results:")
        print(f"   Primary: {diagnosis_result['primary_diagnosis']['name']} "
              f"({diagnosis_result['primary_diagnosis']['confidence']:.1f}% confidence)")
        print(f"   Differential: {', '.join([d['name'] for d in diagnosis_result['differential'][:2]])}")
        print(f"   Recommended Tests: {len(diagnosis_result.get('recommended_tests', []))}")
        
        return diagnosis_record
    
    def _generate_differential_diagnosis(self, patient: dict, symptoms: List[str]) -> dict:
        """Simulate AI differential diagnosis."""
        
        # Simplified diagnosis logic for demo
        conditions = {
            "chest pain": [
                {"name": "Acute Myocardial Infarction", "probability": 0.35, 
                 "risk_factors": ["age > 50", "smoking", "hypertension"]},
                {"name": "Unstable Angina", "probability": 0.25,
                 "risk_factors": ["CAD history", "diabetes"]},
                {"name": "Pulmonary Embolism", "probability": 0.15,
                 "risk_factors": ["recent surgery", "immobility"]},
                {"name": "Costochondritis", "probability": 0.10,
                 "risk_factors": ["recent exercise", "tenderness"]}
            ],
            "shortness of breath": [
                {"name": "Heart Failure", "probability": 0.30,
                 "risk_factors": ["CHF history", "orthopnea"]},
                {"name": "COPD Exacerbation", "probability": 0.25,
                 "risk_factors": ["smoking", "chronic bronchitis"]},
                {"name": "Pneumonia", "probability": 0.20,
                 "risk_factors": ["fever", "cough", "elderly"]},
                {"name": "Asthma", "probability": 0.15,
                 "risk_factors": ["wheezing", "allergies"]}
            ],
            "headache": [
                {"name": "Migraine", "probability": 0.35,
                 "risk_factors": ["photophobia", "nausea", "family history"]},
                {"name": "Tension Headache", "probability": 0.25,
                 "risk_factors": ["stress", "muscle tension"]},
                {"name": "Cluster Headache", "probability": 0.10,
                 "risk_factors": ["male", "smoking"]},
                {"name": "Subarachnoid Hemorrhage", "probability": 0.05,
                 "risk_factors": ["thunderclap onset", "hypertension"]}
            ],
            "fever": [
                {"name": "Viral Infection", "probability": 0.40,
                 "risk_factors": ["myalgia", "fatigue"]},
                {"name": "Bacterial Infection", "probability": 0.25,
                 "risk_factors": ["elevated WBC", "localized symptoms"]},
                {"name": "Urinary Tract Infection", "probability": 0.15,
                 "risk_factors": ["dysuria", "frequency"]},
                {"name": "Pneumonia", "probability": 0.10,
                 "risk_factors": ["cough", "shortness of breath"]}
            ]
        }
        
        # Match symptoms to conditions
        matched_conditions = []
        for symptom in symptoms:
            if symptom.lower() in conditions:
                matched_conditions.extend(conditions[symptom.lower()])
        
        if not matched_conditions:
            # Default conditions
            matched_conditions = [
                {"name": "Viral Syndrome", "probability": 0.40, "risk_factors": []},
                {"name": "Undifferentiated Condition", "probability": 0.30, "risk_factors": []},
                {"name": "Follow-up Required", "probability": 0.20, "risk_factors": []}
            ]
        
        # Adjust based on patient factors
        for condition in matched_conditions:
            if patient['age'] > 65:
                if 'elderly' in condition.get('risk_factors', []):
                    condition['probability'] *= 1.2
            if patient.get('medical_history'):
                for history in patient['medical_history']:
                    if history.lower() in str(condition.get('risk_factors', [])).lower():
                        condition['probability'] *= 1.1
        
        # Remove duplicates and sort by probability
        unique_conditions = {}
        for condition in matched_conditions:
            name = condition['name']
            if name not in unique_conditions or condition['probability'] > unique_conditions[name]['probability']:
                unique_conditions[name] = condition
        
        sorted_conditions = sorted(unique_conditions.values(), 
                                   key=lambda x: x['probability'], reverse=True)
        
        # Normalize probabilities
        total = sum(c['probability'] for c in sorted_conditions[:5])
        for condition in sorted_conditions[:5]:
            condition['probability'] = (condition['probability'] / total) * 100
        
        # Generate factors for explainability
        factors = {}
        for i, condition in enumerate(sorted_conditions[:3]):
            factors[f"diagnosis_{i+1}"] = {
                "name": condition['name'],
                "probability": condition['probability'],
                "supporting_factors": condition.get('risk_factors', [])[:2]
            }
        
        # Recommended tests
        recommended_tests = [
            "Complete Blood Count",
            "Basic Metabolic Panel",
            "Chest X-Ray",
            "ECG"
        ]
        
        # Supporting evidence
        supporting_evidence = [
            f"Patient age {patient['age']}",
            f"Matches {len(sorted_conditions)} conditions",
            f"Symptom pattern consistent with {sorted_conditions[0]['name'] if sorted_conditions else 'unknown'}"
        ]
        
        return {
            "primary_diagnosis": sorted_conditions[0] if sorted_conditions else {"name": "Unknown", "probability": 0},
            "differential": sorted_conditions[1:4] if len(sorted_conditions) > 1 else [],
            "supporting_evidence": supporting_evidence,
            "explanation": f"Based on symptoms and patient factors, the most likely diagnosis is "
                          f"{sorted_conditions[0]['name'] if sorted_conditions else 'unknown'} "
                          f"with {sorted_conditions[0]['probability']:.1f}% probability.",
            "factors": factors,
            "recommended_tests": recommended_tests[:random.randint(2, 4)]
        }
    
    def recommend_treatment(self, patient_id: str, diagnosis: str, 
                           physician: str) -> dict:
        """
        Recommend treatment options based on diagnosis.
        """
        patient = self.patients.get(patient_id)
        if not patient:
            return {"error": "Patient not found"}
        
        print(f"\n💊 Recommending Treatment:")
        print(f"   Patient: {patient['name']}")
        print(f"   Diagnosis: {diagnosis}")
        print(f"   Physician: {physician}")
        
        # Generate treatment options
        treatment_result = self._generate_treatment_options(patient, diagnosis)
        
        # Prepare principal reasons (required by § 6-1-1706)
        principal_reasons = [
            f"First-line treatment: {treatment_result['primary_treatment']['name']}",
            f"Evidence level: {treatment_result['primary_treatment']['evidence_level']}",
            f"Duration: {treatment_result['primary_treatment'].get('duration', 'Standard')}"
        ]
        
        # Log the consequential decision
        decision = self.tracker.log_consequential_decision(
            system_id="CLINICAL-DSS-001",
            consumer_id=patient_id,
            decision_type=DecisionType.HEALTHCARE,
            decision=f"Treatment Recommendations",
            principal_reasons=principal_reasons,
            ai_was_determining_factor=False,
            ai_role_description="AI system recommended evidence-based treatment options for physician review",
            explanation=treatment_result['explanation'],
            decision_factors=treatment_result['factors'],
            notice_provided=True,
            notice_url=f"https://{self.healthcare_system}/ai-notice",
            is_ai_generated=True,
            human_review_available=True,
            appeal_rights_provided=True,
            appeal_deadline=time.time() + 2592000,  # 30 days
            metadata={
                "patient_id": patient_id,
                "patient_age": patient['age'],
                "patient_race": patient.get('race'),
                "patient_ethnicity": patient.get('ethnicity'),
                "diagnosis": diagnosis,
                "physician": physician,
                "primary_treatment": treatment_result['primary_treatment'],
                "alternative_treatments": treatment_result['alternatives'][:2],
                "contraindications": treatment_result.get('contraindications', []),
                "requires_specialist": treatment_result.get('requires_specialist', False)
            }
        )
        
        # Store treatment plan
        treatment_record = {
            "treatment_id": f"TX-{int(time.time())}",
            "patient_id": patient_id,
            "diagnosis": diagnosis,
            "physician": physician,
            "primary_treatment": treatment_result['primary_treatment'],
            "alternatives": treatment_result['alternatives'][:2],
            "decision_id": decision['decision_id'],
            "timestamp": time.time()
        }
        
        self.treatment_plans.append(treatment_record)
        
        print(f"\n📋 Treatment Recommendations:")
        print(f"   Primary: {treatment_result['primary_treatment']['name']}")
        print(f"   Evidence: {treatment_result['primary_treatment']['evidence_level']}")
        print(f"   Alternatives: {len(treatment_result['alternatives'])}")
        print(f"   Contraindications: {len(treatment_result.get('contraindications', []))}")
        
        return treatment_record
    
    def _generate_treatment_options(self, patient: dict, diagnosis: str) -> dict:
        """Generate evidence-based treatment options."""
        
        # Treatment guidelines by condition (simplified)
        treatment_guidelines = {
            "Acute Myocardial Infarction": {
                "primary": {"name": "PCI with stenting", "evidence_level": "IA", "duration": "Immediate"},
                "alternatives": [
                    {"name": "Thrombolytics", "evidence_level": "IB", "duration": "30-60 minutes"},
                    {"name": "Medical Management", "evidence_level": "IIA", "duration": "Ongoing"}
                ],
                "contraindications": ["Active bleeding", "Recent surgery"],
                "requires_specialist": True
            },
            "Pneumonia": {
                "primary": {"name": "Antibiotics (macrolide)", "evidence_level": "IA", "duration": "7-10 days"},
                "alternatives": [
                    {"name": "Antibiotics (respiratory fluoroquinolone)", "evidence_level": "IA", "duration": "5-7 days"},
                    {"name": "Hospital admission", "evidence_level": "IB", "duration": "Variable"}
                ],
                "contraindications": ["Antibiotic allergy"],
                "requires_specialist": False
            },
            "Heart Failure": {
                "primary": {"name": "ACE Inhibitor + Beta Blocker", "evidence_level": "IA", "duration": "Long-term"},
                "alternatives": [
                    {"name": "ARB", "evidence_level": "IB", "duration": "Long-term"},
                    {"name": "Diuretics", "evidence_level": "IC", "duration": "As needed"}
                ],
                "contraindications": ["Hypotension", "Renal failure"],
                "requires_specialist": True
            },
            "Migraine": {
                "primary": {"name": "Triptans", "evidence_level": "IA", "duration": "As needed"},
                "alternatives": [
                    {"name": "NSAIDs", "evidence_level": "IA", "duration": "As needed"},
                    {"name": "Anti-emetics", "evidence_level": "IIA", "duration": "As needed"}
                ],
                "contraindications": ["Cardiovascular disease"],
                "requires_specialist": False
            },
            "Type 2 Diabetes": {
                "primary": {"name": "Metformin", "evidence_level": "IA", "duration": "Long-term"},
                "alternatives": [
                    {"name": "Sulfonylureas", "evidence_level": "IB", "duration": "Long-term"},
                    {"name": "DPP-4 Inhibitors", "evidence_level": "IIA", "duration": "Long-term"}
                ],
                "contraindications": ["Renal impairment", "Liver disease"],
                "requires_specialist": False
            },
            "Depression": {
                "primary": {"name": "SSRI (Sertraline)", "evidence_level": "IA", "duration": "6-12 months"},
                "alternatives": [
                    {"name": "SNRI", "evidence_level": "IA", "duration": "6-12 months"},
                    {"name": "CBT", "evidence_level": "IA", "duration": "12-16 sessions"}
                ],
                "contraindications": ["Bipolar disorder"],
                "requires_specialist": False
            }
        }
        
        # Match diagnosis to guidelines
        guidelines = treatment_guidelines.get(diagnosis, {
            "primary": {"name": "Supportive care", "evidence_level": "III", "duration": "As needed"},
            "alternatives": [
                {"name": "Symptomatic treatment", "evidence_level": "III", "duration": "As needed"},
                {"name": "Specialist referral", "evidence_level": "III", "duration": "Variable"}
            ],
            "contraindications": [],
            "requires_specialist": False
        })
        
        # Check for contraindications based on patient history
        active_contraindications = []
        for contra in guidelines.get('contraindications', []):
            if contra in str(patient.get('medical_history', [])):
                active_contraindications.append(contra)
        
        # Adjust based on patient age
        if patient['age'] > 75:
            guidelines['primary']['dose_adjustment'] = "Renal dose adjustment recommended"
        
        factors = {
            "diagnosis_match": {"score": 0.95, "details": f"Guidelines available for {diagnosis}"},
            "contraindication_check": {
                "score": 1.0 if not active_contraindications else 0.5,
                "details": f"{len(active_contraindications)} contraindications found"
            },
            "evidence_strength": {
                "score": 1.0 if guidelines['primary']['evidence_level'] in ['IA', 'IB'] else 0.7,
                "details": f"Evidence level: {guidelines['primary']['evidence_level']}"
            }
        }
        
        return {
            "primary_treatment": guidelines['primary'],
            "alternatives": guidelines['alternatives'],
            "contraindications": active_contraindications,
            "requires_specialist": guidelines.get('requires_specialist', False),
            "factors": factors,
            "explanation": f"Recommended treatment based on {diagnosis} guidelines. "
                          f"Primary option: {guidelines['primary']['name']} "
                          f"(Evidence level {guidelines['primary']['evidence_level']})."
        }
    
    def determine_insurance_coverage(self, patient_id: str, treatment: str,
                                    insurance_provider: str) -> dict:
        """
        Determine insurance coverage for treatment.
        """
        patient = self.patients.get(patient_id)
        if not patient:
            return {"error": "Patient not found"}
        
        print(f"\n💰 Insurance Coverage Determination:")
        print(f"   Patient: {patient['name']}")
        print(f"   Treatment: {treatment}")
        print(f"   Insurance: {insurance_provider}")
        
        # Determine coverage
        coverage_result = self._determine_coverage(patient, treatment, insurance_provider)
        
        # Prepare principal reasons
        principal_reasons = [
            f"Coverage: {coverage_result['decision']}",
            f"Patient responsibility: ${coverage_result['patient_responsibility']:,.0f}"
        ]
        
        # Log the consequential decision
        decision = self.tracker.log_consequential_decision(
            system_id="CLINICAL-DSS-001",
            consumer_id=patient_id,
            decision_type=DecisionType.HEALTHCARE,
            decision=f"Insurance Coverage: {coverage_result['decision']}",
            principal_reasons=principal_reasons,
            ai_was_determining_factor=True,
            ai_role_description="AI system evaluated medical necessity and plan coverage",
            explanation=coverage_result['explanation'],
            decision_factors=coverage_result['factors'],
            notice_provided=True,
            notice_url=f"https://{self.healthcare_system}/insurance-notice",
            is_ai_generated=True,
            human_review_available=True,
            appeal_rights_provided=True,
            appeal_deadline=coverage_result.get('appeal_deadline', time.time() + 2592000),
            metadata={
                "patient_id": patient_id,
                "patient_race": patient.get('race'),
                "patient_ethnicity": patient.get('ethnicity'),
                "treatment": treatment,
                "insurance_provider": insurance_provider,
                "coverage_decision": coverage_result['decision'],
                "covered_amount": coverage_result['covered_amount'],
                "patient_responsibility": coverage_result['patient_responsibility'],
                "denial_reason": coverage_result.get('denial_reason'),
                "appeal_deadline": coverage_result.get('appeal_deadline')
            }
        )
        
        # Store insurance decision
        insurance_record = {
            "insurance_id": f"INS-{int(time.time())}",
            "patient_id": patient_id,
            "treatment": treatment,
            "provider": insurance_provider,
            "decision": coverage_result['decision'],
            "covered_amount": coverage_result['covered_amount'],
            "patient_responsibility": coverage_result['patient_responsibility'],
            "decision_id": decision['decision_id'],
            "timestamp": time.time()
        }
        
        self.insurance_decisions.append(insurance_record)
        
        print(f"\n📋 Insurance Decision:")
        print(f"   Decision: {coverage_result['decision']}")
        print(f"   Covered Amount: ${coverage_result['covered_amount']:,.0f}")
        print(f"   Patient Responsibility: ${coverage_result['patient_responsibility']:,.0f}")
        print(f"   Appeal Deadline: {datetime.fromtimestamp(decision['appeal_deadline'])}")
        
        return insurance_record
    
    def _determine_coverage(self, patient: dict, treatment: str, 
                            provider: str) -> dict:
        """Simulate insurance coverage determination."""
        
        # Simplified coverage logic
        covered_treatments = [
            "PCI with stenting", "Antibiotics (macrolide)", "ACE Inhibitor",
            "Metformin", "SSRI (Sertraline)", "Triptans", "Surgery"
        ]
        
        experimental_treatments = [
            "Experimental therapy", "Gene therapy", "Investigational drug"
        ]
        
        if treatment in experimental_treatments:
            return {
                "decision": "DENIED",
                "covered_amount": 0,
                "patient_responsibility": 50000,
                "denial_reason": "Experimental treatment not covered",
                "appeal_deadline": time.time() + 2592000,  # 30 days
                "explanation": "This treatment is considered experimental and is not covered by your plan.",
                "factors": {
                    "medical_necessity": {"score": 0.3, "details": "Treatment considered experimental"},
                    "plan_coverage": {"score": 0.0, "details": "Excluded from coverage"}
                }
            }
        elif treatment in covered_treatments:
            # Check medical necessity based on diagnosis
            covered_amount = random.randint(5000, 50000)
            patient_responsibility = random.randint(500, 5000)
            
            return {
                "decision": "APPROVED",
                "covered_amount": covered_amount,
                "patient_responsibility": patient_responsibility,
                "explanation": f"Treatment approved. Plan covers ${covered_amount:,} "
                              f"with patient responsibility of ${patient_responsibility:,}.",
                "factors": {
                    "medical_necessity": {"score": 0.9, "details": "Treatment medically necessary"},
                    "plan_coverage": {"score": 0.8, "details": "Covered service"}
                }
            }
        else:
            return {
                "decision": "DENIED",
                "covered_amount": 0,
                "patient_responsibility": 25000,
                "denial_reason": "Not covered under plan",
                "appeal_deadline": time.time() + 2592000,
                "explanation": "The requested treatment is not covered under your current plan.",
                "factors": {
                    "medical_necessity": {"score": 0.5, "details": "Treatment may be medically necessary but not covered"},
                    "plan_coverage": {"score": 0.0, "details": "Excluded service"}
                }
            }
    
    def match_clinical_trials(self, patient_id: str, condition: str) -> dict:
        """
        Match patient to eligible clinical trials.
        """
        patient = self.patients.get(patient_id)
        if not patient:
            return {"error": "Patient not found"}
        
        print(f"\n🔬 Matching Clinical Trials:")
        print(f"   Patient: {patient['name']}")
        print(f"   Condition: {condition}")
        
        # Find matching trials
        matching_trials = []
        for trial_id, trial in self.clinical_trials.items():
            if condition.lower() in trial['condition'].lower():
                # Check eligibility (simplified)
                eligible = True
                reasons = []
                
                for criterion in trial.get('eligibility_criteria', []):
                    if 'age' in criterion.lower() and patient['age'] > 75:
                        eligible = False
                        reasons.append("Age exceeds trial criteria")
                
                if eligible:
                    matching_trials.append({
                        "trial_id": trial_id,
                        "name": trial['name'],
                        "phase": trial['phase'],
                        "location": trial.get('locations', ['Unknown'])[0],
                        "contact": trial.get('principal_investigator', 'Unknown'),
                        "eligibility_summary": ", ".join(trial.get('eligibility_criteria', [])[:2])
                    })
        
        # Log the decision
        decision = self.tracker.log_consequential_decision(
            system_id="CLINICAL-DSS-001",
            consumer_id=patient_id,
            decision_type=DecisionType.HEALTHCARE,
            decision=f"Clinical Trial Matches",
            principal_reasons=[f"Found {len(matching_trials)} matching trials"],
            ai_was_determining_factor=True,
            ai_role_description="AI system matched patient to eligible clinical trials",
            explanation=f"Based on your condition and eligibility criteria, we found {len(matching_trials)} potential clinical trials.",
            decision_factors={"trial_match": {"score": len(matching_trials)/5, "details": f"{len(matching_trials)} trials"}},
            human_review_available=True,
            appeal_rights_provided=False,
            metadata={
                "patient_id": patient_id,
                "patient_race": patient.get('race'),
                "patient_ethnicity": patient.get('ethnicity'),
                "condition": condition,
                "matching_trials": matching_trials,
                "trial_count": len(matching_trials)
            }
        )
        
        return {
            "patient_id": patient_id,
            "condition": condition,
            "matching_trials": matching_trials,
            "count": len(matching_trials),
            "decision_id": decision['decision_id']
        }
    
    def handle_appeal(self, appeal_data: dict) -> dict:
        """Handle an appeal of a treatment or coverage decision (§ 6-1-1708)."""
        
        appeal = self.tracker.handle_appeal(
            appeal_id=f"APPEAL-{int(time.time())}",
            consumer_id=appeal_data['patient_id'],
            decision_id=appeal_data['decision_id'],
            appeal_date=time.time(),
            appeal_reason=appeal_data['reason'],
            review_status="IN_PROGRESS",
            reviewer=appeal_data.get('reviewer', 'appeals-coordinator'),
            appeal_deadline=time.time() + 604800,  # 7 days
            evidence_submitted=appeal_data.get('evidence', []),
            metadata={
                "patient_name": appeal_data.get('patient_name'),
                "treatment": appeal_data.get('treatment'),
                "additional_info": appeal_data.get('additional_info'),
                "expedited": appeal_data.get('expedited', False)
            }
        )
        
        self.appeals.append(appeal)
        
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
            consumer_id=correction_data['patient_id'],
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
                "patient_name": correction_data.get('patient_name')
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
        demographic_data = {
            "race": {},
            "ethnicity": {},
            "insurance": {},
            "age_group": {}
        }
        
        for decision in all_decisions:
            demo = decision.get('metadata', {})
            patient_id = decision.get('consumer_id')
            
            # Find patient data
            patient = None
            for p in self.patients.values():
                if p['patient_id'] == patient_id:
                    patient = p
                    break
            
            if patient:
                # Race
                race = patient.get('race', 'unknown')
                if race not in demographic_data['race']:
                    demographic_data['race'][race] = {"total": 0, "positive": 0}
                demographic_data['race'][race]["total"] += 1
                if decision['decision'] in ['APPROVED', 'APPROVE', 'Diagnosis Suggestions', 'Treatment Recommendations']:
                    demographic_data['race'][race]["positive"] += 1
                
                # Ethnicity
                ethnicity = patient.get('ethnicity', 'unknown')
                if ethnicity not in demographic_data['ethnicity']:
                    demographic_data['ethnicity'][ethnicity] = {"total": 0, "positive": 0}
                demographic_data['ethnicity'][ethnicity]["total"] += 1
                if decision['decision'] in ['APPROVED', 'APPROVE', 'Diagnosis Suggestions', 'Treatment Recommendations']:
                    demographic_data['ethnicity'][ethnicity]["positive"] += 1
                
                # Insurance
                insurance = patient.get('insurance', 'unknown')
                if insurance not in demographic_data['insurance']:
                    demographic_data['insurance'][insurance] = {"total": 0, "positive": 0}
                demographic_data['insurance'][insurance]["total"] += 1
                if decision['decision'] in ['APPROVED', 'APPROVE', 'Diagnosis Suggestions', 'Treatment Recommendations']:
                    demographic_data['insurance'][insurance]["positive"] += 1
                
                # Age group
                age = patient.get('age', 0)
                age_group = "0-18" if age < 18 else "19-40" if age < 40 else "41-65" if age < 65 else "65+"
                if age_group not in demographic_data['age_group']:
                    demographic_data['age_group'][age_group] = {"total": 0, "positive": 0}
                demographic_data['age_group'][age_group]["total"] += 1
                if decision['decision'] in ['APPROVED', 'APPROVE', 'Diagnosis Suggestions', 'Treatment Recommendations']:
                    demographic_data['age_group'][age_group]["positive"] += 1
        
        # Calculate disparate impact
        disparate_impact = {}
        for dim, groups in demographic_data.items():
            if len(groups) > 1:
                rates = []
                group_names = []
                for group, stats in groups.items():
                    if stats["total"] > 0:
                        rate = stats["positive"] / stats["total"] if stats["total"] > 0 else 0
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
            system_id="CLINICAL-DSS-001",
            assessment_date=time.time(),
            fairness_metrics={
                "total_decisions": len(all_decisions),
                "positive_outcome_rate": len([d for d in all_decisions if d['decision'] in ['APPROVED', 'APPROVE']]) / len(all_decisions) if all_decisions else 0,
                "disparate_impact": disparate_impact,
                "demographic_breakdown": demographic_data
            },
            bias_test_results={
                "race": "PASS" if disparate_impact.get('race', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "ethnicity": "PASS" if disparate_impact.get('ethnicity', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "insurance": "PASS" if disparate_impact.get('insurance', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "age": "PASS_WITH_MONITORING" if disparate_impact.get('age_group', {}).get('ratio', 1.0) >= 0.75 else "FAIL"
            },
            risk_factors=[
                {"factor": k, "disparity": v['ratio'], "status": "monitor" if v['ratio'] < 0.85 else "acceptable"}
                for k, v in disparate_impact.items()
            ],
            mitigation_strategies=[
                "Quarterly health equity analysis",
                "Bias testing on diverse populations",
                "Physician review for all AI recommendations",
                "Continuous monitoring for disparate outcomes",
                "Annual model validation"
            ],
            residual_risk="LOW" if all(v.get('ratio', 1.0) >= 0.8 for v in disparate_impact.values()) else "MEDIUM",
            next_assessment_date=time.time() + 31536000,  # 1 year
            conducted_by="chief-medical-officer@health.org"
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
            certificate_url=f"https://{self.healthcare_system}/compliance/nist-certificate"
        )
        
        print(f"\n🛡️ Safe Harbor Certificate (§ 6-1-1709):")
        print(f"   Certificate ID: {certificate['certificate_id']}")
        print(f"   Framework: {certificate['framework']}")
        print(f"   Certified By: {certificate['certified_by']}")
        print(f"   Expires: {datetime.fromtimestamp(certificate['expiry_date'])}")
        
        return certificate
    
    def run_healthcare_demo(self):
        """Run complete healthcare demonstration with Colorado AI Act compliance."""
        
        # Register system
        self.setup_clinical_system()
        
        # Add clinical trials
        trials = [
            {
                "name": "Novel Anticoagulant for Atrial Fibrillation",
                "phase": "Phase III",
                "condition": "Atrial Fibrillation",
                "eligibility_criteria": ["Age 18-80", "Diagnosed AF", "No bleeding disorders"],
                "locations": ["Denver, CO", "Colorado Springs, CO"],
                "principal_investigator": "Dr. Sarah Chen"
            },
            {
                "name": "Immunotherapy for Lung Cancer",
                "phase": "Phase II",
                "condition": "Non-Small Cell Lung Cancer",
                "eligibility_criteria": ["Stage IIIB/IV", "ECOG 0-1", "No prior immunotherapy"],
                "locations": ["Aurora, CO"],
                "principal_investigator": "Dr. James Wilson"
            },
            {
                "name": "Diabetes Prevention Program",
                "phase": "Phase IV",
                "condition": "Type 2 Diabetes",
                "eligibility_criteria": ["Age 30-70", "BMI > 27", "Prediabetes"],
                "locations": ["Multiple sites in CO"],
                "principal_investigator": "Dr. Maria Rodriguez"
            }
        ]
        
        trial_ids = []
        for trial in trials:
            tid = self.add_clinical_trial(trial)
            trial_ids.append(tid)
        
        # Add patients with diverse demographics
        patients = [
            # White male, Medicare
            {
                "name": "Robert Johnson",
                "mrn": "MRN-10001",
                "age": 72,
                "gender": "Male",
                "race": "White",
                "ethnicity": "Not Hispanic",
                "insurance": "Medicare",
                "primary_care_physician": "Dr. Williams",
                "medical_history": ["Hypertension", "Diabetes", "CAD"],
                "medications": ["Lisinopril", "Metformin"],
                "vital_signs": {"bp": "145/90", "hr": 82, "temp": 98.6}
            },
            # Hispanic female, Medicaid
            {
                "name": "Maria Garcia",
                "mrn": "MRN-10002",
                "age": 45,
                "gender": "Female",
                "race": "Hispanic",
                "ethnicity": "Latina",
                "insurance": "Medicaid",
                "primary_care_physician": "Dr. Chen",
                "medical_history": ["Asthma", "Migraines"],
                "medications": ["Albuterol", "Sumatriptan"],
                "vital_signs": {"bp": "118/72", "hr": 76, "temp": 98.4}
            },
            # Black male, Private
            {
                "name": "James Smith",
                "mrn": "MRN-10003",
                "age": 58,
                "gender": "Male",
                "race": "Black",
                "ethnicity": "Not Hispanic",
                "insurance": "Private",
                "primary_care_physician": "Dr. Williams",
                "medical_history": ["COPD", "GERD"],
                "medications": ["Advair", "Omeprazole"],
                "vital_signs": {"bp": "132/84", "hr": 88, "temp": 98.8}
            },
            # White female, Private
            {
                "name": "Sarah Johnson",
                "mrn": "MRN-10004",
                "age": 35,
                "gender": "Female",
                "race": "White",
                "ethnicity": "Not Hispanic",
                "insurance": "Private",
                "primary_care_physician": "Dr. Chen",
                "medical_history": ["Anxiety", "IBS"],
                "medications": ["Escitalopram"],
                "vital_signs": {"bp": "122/78", "hr": 72, "temp": 98.6}
            },
            # Asian male, Medicare
            {
                "name": "William Lee",
                "mrn": "MRN-10005",
                "age": 68,
                "gender": "Male",
                "race": "Asian",
                "ethnicity": "Asian",
                "insurance": "Medicare",
                "primary_care_physician": "Dr. Patel",
                "medical_history": ["Heart Failure", "COPD"],
                "medications": ["Furosemide", "Lisinopril", "Metoprolol"],
                "vital_signs": {"bp": "128/76", "hr": 70, "temp": 98.4}
            }
        ]
        
        patient_ids = []
        for pat in patients:
            pid = self.add_patient(pat)
            patient_ids.append(pid)
        
        # Conduct diagnoses
        diagnoses_to_run = [
            {"patient_idx": 0, "symptoms": ["chest pain", "shortness of breath"], "physician": "Dr. Williams"},
            {"patient_idx": 1, "symptoms": ["headache", "photophobia"], "physician": "Dr. Chen"},
            {"patient_idx": 2, "symptoms": ["shortness of breath", "cough"], "physician": "Dr. Williams"},
            {"patient_idx": 3, "symptoms": ["headache", "fatigue"], "physician": "Dr. Chen"},
            {"patient_idx": 4, "symptoms": ["shortness of breath", "edema"], "physician": "Dr. Patel"}
        ]
        
        for diag in diagnoses_to_run:
            self.conduct_diagnosis_assistance(
                patient_ids[diag['patient_idx']],
                diag['symptoms'],
                diag['physician']
            )
        
        # Recommend treatments
        treatments_to_run = [
            {"patient_idx": 0, "diagnosis": "Acute Myocardial Infarction", "physician": "Dr. Williams"},
            {"patient_idx": 1, "diagnosis": "Migraine", "physician": "Dr. Chen"},
            {"patient_idx": 2, "diagnosis": "COPD Exacerbation", "physician": "Dr. Williams"},
            {"patient_idx": 3, "diagnosis": "Depression", "physician": "Dr. Chen"},
            {"patient_idx": 4, "diagnosis": "Heart Failure", "physician": "Dr. Patel"}
        ]
        
        for tx in treatments_to_run:
            self.recommend_treatment(
                patient_ids[tx['patient_idx']],
                tx['diagnosis'],
                tx['physician']
            )
        
        # Determine insurance coverage
        coverage_to_run = [
            {"patient_idx": 0, "treatment": "PCI with stenting", "provider": "Medicare"},
            {"patient_idx": 1, "treatment": "Triptans", "provider": "Medicaid"},
            {"patient_idx": 2, "treatment": "Antibiotics (macrolide)", "provider": "Private"},
            {"patient_idx": 3, "treatment": "SSRI (Sertraline)", "provider": "Private"},
            {"patient_idx": 4, "treatment": "ACE Inhibitor + Beta Blocker", "provider": "Medicare"}
        ]
        
        for cov in coverage_to_run:
            self.determine_insurance_coverage(
                patient_ids[cov['patient_idx']],
                cov['treatment'],
                cov['provider']
            )
        
        # Match clinical trials
        self.match_clinical_trials(patient_ids[0], "Atrial Fibrillation")
        self.match_clinical_trials(patient_ids[4], "Heart Failure")
        
        # Handle an appeal for denied coverage
        denied_insurance = next((i for i in self.insurance_decisions if i['decision'] == 'DENIED'), None)
        if denied_insurance:
            patient = next((p for p in self.patients.values() if p['patient_id'] == denied_insurance['patient_id']), None)
            if patient:
                self.handle_appeal({
                    "patient_id": denied_insurance['patient_id'],
                    "patient_name": patient['name'],
                    "decision_id": denied_insurance['decision_id'],
                    "reason": "Treatment is medically necessary based on specialist recommendation",
                    "treatment": denied_insurance['treatment'],
                    "additional_info": "Letter from cardiologist attached",
                    "reviewer": "appeals-physician",
                    "evidence": ["cardiologist_letter.pdf"]
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
        print(f"   Patients: {len(patient_ids)}")
        print(f"   Clinical Trials: {len(trial_ids)}")
        print(f"   Diagnoses: {len(self.diagnoses)}")
        print(f"   Treatments: {len(self.treatment_plans)}")
        print(f"   Insurance Decisions: {len(self.insurance_decisions)}")
        print(f"   Appeals: {len(self.appeals)}")
        print(f"   Annual Risk Assessment: ✓")
        print(f"   Safe Harbor Qualified: ✓")
        
        return report


if __name__ == "__main__":
    system = ClinicalDecisionSupportSystem("Colorado Health System")
    report = system.run_healthcare_demo()
    
    # Save report
    with open("colorado_healthcare_report.json", "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\n✅ Report saved: colorado_healthcare_report.json")
    print(f"\n⚠️ Note: Colorado AI Act effective June 30, 2026")
    print(f"   Ensure compliance before this date.")
    print(f"\n⚖️ Health Equity Note: The Colorado AI Act requires monitoring for algorithmic discrimination")
    print(f"   across protected classes including race, ethnicity, and insurance status.")
