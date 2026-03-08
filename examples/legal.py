#!/usr/bin/env python3
"""
Colorado AI Act - Legal Services Example
===========================================

This example demonstrates a complete AI-powered legal services system
that complies with Colorado's Artificial Intelligence Act (SB 24-205),
covering:

- Case outcome prediction
- Legal document review
- Settlement recommendation
- Client intake and eligibility
- Legal research assistance
- Bias monitoring across protected classes
- Appeal and human review processes
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


class LegalAIAssistant:
    """
    Complete legal AI assistant with Colorado AI Act compliance.
    
    Under SB 24-205, legal services are explicitly designated as "consequential decisions"
    requiring consumer protections [citation:1][citation:2][citation:4].
    
    Features:
    - Case outcome prediction
    - Document review and analysis
    - Settlement recommendations
    - Client eligibility screening
    - Legal research assistance
    - Bias monitoring across protected classes
    - Appeal and human review processes
    - Annual risk assessments
    """
    
    def __init__(self, firm_name: str):
        self.firm_name = firm_name
        self.tracker = ColoradoAITracker(
            entity_type=EntityType.DEPLOYER,
            organization=firm_name,
            contact_email="ai-compliance@legalfirm.com"
        )
        
        self.clients = {}
        self.cases = []
        self.predictions = []
        self.settlement_recommendations = []
        self.document_reviews = []
        self.appeals = []
        
        print("="*80)
        print(f"⚖️ Legal AI Assistant - {firm_name}")
        print("="*80)
        print(f"Colorado AI Act Effective: June 30, 2026")
        print(f"Consequential Decisions: Legal services (case outcomes, settlements, eligibility) [citation:2]")
    
    def setup_legal_ai_system(self):
        """Register the legal AI system with Colorado."""
        
        system = self.tracker.register_high_risk_system(
            system_id="LEGAL-AI-001",
            system_name="Legal Outcome Predictor & Document Analyzer",
            system_type=DecisionType.LEGAL,
            description="AI system for predicting case outcomes, reviewing legal documents, and recommending settlement amounts",
            intended_use=(
                "Assist attorneys by predicting case outcomes, "
                "analyzing legal documents for risks, recommending "
                "settlement ranges, and screening client eligibility"
            ),
            limitations=[
                "Not a replacement for attorney judgment",
                "Predictions based on historical data may not account for novel legal arguments",
                "Requires regular validation across case types",
                "May have lower accuracy for pro se litigants",
                "Final legal decisions require attorney review"
            ],
            training_data_summary={
                "size": 50000,
                "data_sources": ["court_records", "settlement_databases", "legal_documents"],
                "case_types": ["personal_injury", "contract", "employment", "civil_rights"],
                "jurisdictions": ["federal", "state"],
                "date_range": "2015-2025"
            },
            performance_metrics={
                "outcome_prediction_accuracy": 0.86,
                "settlement_recommendation_accuracy": 0.82,
                "document_review_precision": 0.91,
                "recall": 0.88,
                "f1_score": 0.89
            },
            mitigation_strategies=[
                "Quarterly fairness testing across protected classes",
                "Attorney review for all predictions and recommendations",
                "Continuous monitoring for disparate outcomes",
                "Annual model validation",
                "Bias mitigation training",
                "Regular calibration with actual case outcomes"
            ],
            responsible_officer="managing-partner@legalfirm.com"
        )
        
        print(f"\n✅ Legal AI system registered: {system['system_id']}")
        print(f"   Limitations documented: {len(system['limitations'])}")
        print(f"   Mitigation strategies: {len(system['mitigation_strategies'])}")
        print(f"   Note: Legal services are \"consequential decisions\" under SB 24-205 [citation:1][citation:4]")
        
        return system
    
    def add_client(self, client_data: dict) -> str:
        """Add a client to the system."""
        client_id = f"CL-{int(time.time())}-{random.randint(1000, 9999)}"
        
        # Hash for privacy
        client_hash = f"CL-{hash(client_data['name'] + client_data.get('email', '')) % 10000:04d}"
        
        self.clients[client_id] = {
            "client_id": client_id,
            "hash": client_hash,
            "name": client_data['name'],
            "age": client_data.get('age'),
            "gender": client_data.get('gender'),
            "race": client_data.get('race'),
            "ethnicity": client_data.get('ethnicity'),
            "income_level": client_data.get('income_level'),
            "education_level": client_data.get('education_level'),
            "prior_legal_history": client_data.get('prior_legal_history', False),
            "representation_type": client_data.get('representation_type', 'private'),
            "created_date": time.time()
        }
        
        print(f"\n👤 Client Added:")
        print(f"   Client ID: {client_id}")
        print(f"   Name: {client_data['name']}")
        print(f"   Representation Type: {client_data.get('representation_type', 'private')}")
        
        return client_id
    
    def create_case(self, case_data: dict) -> str:
        """Create a new legal case."""
        case_id = f"CASE-{int(time.time())}-{random.randint(100, 999)}"
        
        case = {
            "case_id": case_id,
            "client_id": case_data['client_id'],
            "case_type": case_data['case_type'],
            "jurisdiction": case_data['jurisdiction'],
            "court_level": case_data.get('court_level', 'trial'),
            "filing_date": case_data.get('filing_date', time.time()),
            "opposing_party": case_data.get('opposing_party'),
            "legal_claims": case_data.get('legal_claims', []),
            "damages_sought": case_data.get('damages_sought'),
            "liability_assessment": case_data.get('liability_assessment', 0.5),
            "case_complexity": case_data.get('case_complexity', 'medium'),
            "assigned_attorney": case_data.get('assigned_attorney'),
            "status": "ACTIVE",
            "created_date": time.time()
        }
        
        self.cases.append(case)
        
        print(f"\n📁 Case Created:")
        print(f"   Case ID: {case_id}")
        print(f"   Type: {case_data['case_type']}")
        print(f"   Jurisdiction: {case_data['jurisdiction']}")
        print(f"   Damages Sought: ${case_data.get('damages_sought', 0):,.0f}")
        
        return case_id
    
    def predict_case_outcome(self, case_id: str, attorney_id: str) -> dict:
        """
        Predict case outcome using AI and log the consequential decision.
        
        Under SB 24-205, case outcome predictions are "consequential decisions"
        affecting legal services [citation:2][citation:4].
        """
        # Find case
        case = next((c for c in self.cases if c["case_id"] == case_id), None)
        if not case:
            return {"error": "Case not found"}
        
        client = self.clients.get(case["client_id"])
        
        print(f"\n🔮 Predicting Case Outcome: {case_id}")
        print(f"   Client: {client['name']}")
        print(f"   Case Type: {case['case_type']}")
        print(f"   Damages Sought: ${case.get('damages_sought', 0):,.0f}")
        
        # Perform outcome prediction
        prediction_result = self._predict_outcome(case, client)
        
        # Prepare principal reasons (required by § 6-1-1706)
        principal_reasons = self._generate_prediction_reasons(prediction_result, case)
        
        # Log the consequential decision
        decision = self.tracker.log_consequential_decision(
            system_id="LEGAL-AI-001",
            consumer_id=client['client_id'],
            decision_type=DecisionType.LEGAL,
            decision=f"Outcome Prediction: {prediction_result['predicted_outcome']}",
            principal_reasons=principal_reasons,
            ai_was_determining_factor=False,  # AI assists, attorney decides
            ai_role_description="AI system predicted case outcome based on historical case data and legal factors",
            explanation=prediction_result['explanation'],
            decision_factors=prediction_result['factors'],
            notice_provided=True,
            notice_url=f"https://{self.firm_name}/ai-legal-notice",
            is_ai_generated=True,
            human_review_available=True,
            appeal_rights_provided=True,
            appeal_deadline=time.time() + 2592000,  # 30 days
            metadata={
                "case_id": case_id,
                "client_id": client['client_id'],
                "client_demographics": {
                    "race": client.get('race'),
                    "ethnicity": client.get('ethnicity'),
                    "gender": client.get('gender'),
                    "age": client.get('age'),
                    "income_level": client.get('income_level'),
                    "representation_type": client.get('representation_type')
                },
                "case_type": case['case_type'],
                "predicted_outcome": prediction_result['predicted_outcome'],
                "confidence": prediction_result['confidence'],
                "settlement_range": prediction_result.get('settlement_range'),
                "probability_plaintiff": prediction_result.get('probability_plaintiff'),
                "attorney_id": attorney_id
            }
        )
        
        # Store prediction
        prediction = {
            "prediction_id": f"PRED-{int(time.time())}",
            "case_id": case_id,
            "client_id": client['client_id'],
            "predicted_outcome": prediction_result['predicted_outcome'],
            "confidence": prediction_result['confidence'],
            "decision_id": decision['decision_id'],
            "timestamp": time.time()
        }
        
        self.predictions.append(prediction)
        
        print(f"\n📊 Outcome Prediction:")
        print(f"   Predicted: {prediction_result['predicted_outcome']}")
        print(f"   Confidence: {prediction_result['confidence']:.1f}%")
        print(f"   Probability Plaintiff Wins: {prediction_result.get('probability_plaintiff', 0):.1f}%")
        if prediction_result.get('settlement_range'):
            print(f"   Settlement Range: ${prediction_result['settlement_range']['low']:,.0f} - ${prediction_result['settlement_range']['high']:,.0f}")
        print(f"   Appeal Deadline: {datetime.fromtimestamp(decision['appeal_deadline'])}")
        
        return prediction
    
    def _predict_outcome(self, case: dict, client: dict) -> dict:
        """Simulate AI case outcome prediction."""
        
        factors = {}
        
        # Base probability by case type (simplified model)
        case_type_probabilities = {
            "personal_injury": 0.65,
            "contract": 0.55,
            "employment": 0.60,
            "civil_rights": 0.50,
            "medical_malpractice": 0.40,
            "product_liability": 0.58
        }
        
        base_prob = case_type_probabilities.get(case['case_type'], 0.5)
        factors['case_type'] = {
            "score": base_prob * 100,
            "weight": 0.3,
            "details": f"Case type: {case['case_type']}"
        }
        
        # Adjust based on liability assessment
        liability = case.get('liability_assessment', 0.5)
        prob = base_prob * (0.5 + liability)
        factors['liability'] = {
            "score": liability * 100,
            "weight": 0.25,
            "details": f"Liability assessment: {liability:.1%}"
        }
        
        # Adjust based on damages sought
        damages = case.get('damages_sought', 100000)
        if damages > 1000000:
            prob *= 1.1  # High damages often lead to more aggressive defense
            factors['damages'] = {
                "score": 55,
                "weight": 0.15,
                "details": f"High damages (${damages:,.0f}) may increase defense intensity"
            }
        elif damages < 50000:
            prob *= 0.9  # Low damages may settle quickly
            factors['damages'] = {
                "score": 45,
                "weight": 0.15,
                "details": f"Lower damages (${damages:,.0f}) may facilitate settlement"
            }
        else:
            factors['damages'] = {
                "score": 50,
                "weight": 0.15,
                "details": f"Damages: ${damages:,.0f}"
            }
        
        # Court level adjustment
        if case.get('court_level') == 'appellate':
            prob *= 0.8  # Appeals have lower success rates
            factors['court_level'] = {
                "score": 40,
                "weight": 0.1,
                "details": "Appellate court - lower success probability"
            }
        elif case.get('court_level') == 'federal':
            prob *= 1.05
            factors['court_level'] = {
                "score": 52,
                "weight": 0.1,
                "details": "Federal court - slight advantage for certain cases"
            }
        else:
            factors['court_level'] = {
                "score": 50,
                "weight": 0.1,
                "details": f"Court level: {case.get('court_level', 'trial')}"
            }
        
        # Representation type adjustment
        rep_type = client.get('representation_type', 'private')
        if rep_type == 'pro_bono':
            prob *= 1.1  # Pro bono often means strong case
            factors['representation'] = {
                "score": 55,
                "weight": 0.1,
                "details": "Pro bono representation - case likely has merit"
            }
        elif rep_type == 'legal_aid':
            prob *= 0.95
            factors['representation'] = {
                "score": 47,
                "weight": 0.1,
                "details": "Legal aid representation - resource constraints may affect outcome"
            }
        else:
            factors['representation'] = {
                "score": 50,
                "weight": 0.1,
                "details": f"Representation: {rep_type}"
            }
        
        # Normalize probability
        prob = max(0.1, min(0.9, prob))
        
        # Determine outcome
        if prob >= 0.6:
            predicted_outcome = "Plaintiff Likely to Prevail"
        elif prob >= 0.4:
            predicted_outcome = "Uncertain - Further Analysis Needed"
        else:
            predicted_outcome = "Defendant Likely to Prevail"
        
        # Settlement range based on probability
        if damages:
            settlement_low = damages * prob * 0.5
            settlement_high = damages * prob * 0.8
        else:
            settlement_low = 25000
            settlement_high = 75000
        
        return {
            "predicted_outcome": predicted_outcome,
            "probability_plaintiff": prob * 100,
            "confidence": min(85, 50 + (abs(prob - 0.5) * 100)),  # Higher confidence when clear
            "settlement_range": {
                "low": settlement_low,
                "high": settlement_high
            },
            "factors": factors,
            "explanation": f"Based on case type ({case['case_type']}) and liability assessment ({case.get('liability_assessment', 0.5):.0%}), the predicted outcome is {predicted_outcome.lower()} with {prob:.0%} probability of plaintiff success."
        }
    
    def _generate_prediction_reasons(self, prediction: dict, case: dict) -> List[str]:
        """Generate principal reasons for outcome prediction."""
        reasons = []
        
        reasons.append(f"Case type: {case['case_type']}")
        reasons.append(f"Liability assessment: {case.get('liability_assessment', 0.5):.0%}")
        
        if prediction['probability_plaintiff'] >= 60:
            reasons.append(f"Strong plaintiff position ({prediction['probability_plaintiff']:.0f}% success probability)")
        elif prediction['probability_plaintiff'] <= 40:
            reasons.append(f"Challenging plaintiff position ({prediction['probability_plaintiff']:.0f}% success probability)")
        
        return reasons[:3]
    
    def recommend_settlement(self, case_id: str, attorney_id: str) -> dict:
        """
        Recommend settlement amount using AI.
        
        Under SB 24-205, settlement recommendations are "consequential decisions"
        affecting legal services [citation:1][citation:2].
        """
        case = next((c for c in self.cases if c["case_id"] == case_id), None)
        if not case:
            return {"error": "Case not found"}
        
        client = self.clients.get(case["client_id"])
        
        print(f"\n💰 Recommending Settlement: {case_id}")
        print(f"   Case Type: {case['case_type']}")
        print(f"   Damages Sought: ${case.get('damages_sought', 0):,.0f}")
        
        # Find most recent prediction
        case_predictions = [p for p in self.predictions if p["case_id"] == case_id]
        latest_prediction = case_predictions[-1] if case_predictions else None
        
        # Generate settlement recommendation
        settlement = self._generate_settlement_recommendation(case, client, latest_prediction)
        
        # Prepare principal reasons
        principal_reasons = [
            f"Recommended settlement: ${settlement['recommended_amount']:,.0f}",
            f"Range: ${settlement['range_low']:,.0f} - ${settlement['range_high']:,.0f}",
            f"Confidence: {settlement['confidence']:.0f}%"
        ]
        
        # Log the consequential decision
        decision = self.tracker.log_consequential_decision(
            system_id="LEGAL-AI-001",
            consumer_id=client['client_id'],
            decision_type=DecisionType.LEGAL,
            decision=f"Settlement Recommendation: ${settlement['recommended_amount']:,.0f}",
            principal_reasons=principal_reasons,
            ai_was_determining_factor=False,
            ai_role_description="AI system recommended settlement range based on case value and probability of success",
            explanation=settlement['explanation'],
            decision_factors=settlement['factors'],
            notice_provided=True,
            notice_url=f"https://{self.firm_name}/ai-legal-notice",
            is_ai_generated=True,
            human_review_available=True,
            appeal_rights_provided=True,
            appeal_deadline=time.time() + 2592000,
            metadata={
                "case_id": case_id,
                "client_id": client['client_id'],
                "client_demographics": {
                    "race": client.get('race'),
                    "ethnicity": client.get('ethnicity'),
                    "gender": client.get('gender'),
                    "income_level": client.get('income_level')
                },
                "recommended_amount": settlement['recommended_amount'],
                "range_low": settlement['range_low'],
                "range_high": settlement['range_high'],
                "confidence": settlement['confidence'],
                "attorney_id": attorney_id
            }
        )
        
        # Store recommendation
        recommendation = {
            "recommendation_id": f"SETTLE-{int(time.time())}",
            "case_id": case_id,
            "client_id": client['client_id'],
            "recommended_amount": settlement['recommended_amount'],
            "range_low": settlement['range_low'],
            "range_high": settlement['range_high'],
            "confidence": settlement['confidence'],
            "decision_id": decision['decision_id'],
            "timestamp": time.time()
        }
        
        self.settlement_recommendations.append(recommendation)
        
        print(f"\n📊 Settlement Recommendation:")
        print(f"   Recommended: ${settlement['recommended_amount']:,.0f}")
        print(f"   Range: ${settlement['range_low']:,.0f} - ${settlement['range_high']:,.0f}")
        print(f"   Confidence: {settlement['confidence']:.0f}%")
        
        return recommendation
    
    def _generate_settlement_recommendation(self, case: dict, client: dict, 
                                           prediction: Optional[dict]) -> dict:
        """Generate AI settlement recommendation."""
        
        factors = {}
        damages = case.get('damages_sought', 100000)
        
        # Base settlement on prediction if available
        if prediction and 'settlement_range' in prediction:
            settlement_range = prediction['settlement_range']
            recommended = (settlement_range['low'] + settlement_range['high']) / 2
            confidence = prediction.get('confidence', 70)
        else:
            # Default calculation
            prob = case.get('liability_assessment', 0.5)
            recommended = damages * prob * 0.65
            confidence = 60
        
        # Calculate range
        range_low = recommended * 0.7
        range_high = recommended * 1.3
        
        # Adjust based on case complexity
        complexity = case.get('case_complexity', 'medium')
        if complexity == 'high':
            range_low *= 0.8
            range_high *= 1.2
            confidence -= 10
            factors['complexity'] = {
                "score": 40,
                "details": "High complexity case - wider settlement range"
            }
        elif complexity == 'low':
            range_low *= 0.9
            range_high *= 1.1
            confidence += 5
            factors['complexity'] = {
                "score": 55,
                "details": "Low complexity case - narrower settlement range"
            }
        
        factors['base_calculation'] = {
            "score": 50,
            "details": f"Base settlement: {recommended:,.0f} (damages: ${damages:,.0f}, liability: {case.get('liability_assessment', 0.5):.0%})"
        }
        
        return {
            "recommended_amount": round(recommended, -2),
            "range_low": round(range_low, -2),
            "range_high": round(range_high, -2),
            "confidence": confidence,
            "factors": factors,
            "explanation": f"Recommended settlement of ${round(recommended, -2):,.0f} based on case value and probability of success. Range: ${round(range_low, -2):,.0f} - ${round(range_high, -2):,.0f}."
        }
    
    def review_document(self, client_id: str, document_type: str, 
                       document_content: str, attorney_id: str) -> dict:
        """
        Review legal document using AI.
        
        Document review may be considered a "consequential decision" if it
        materially affects legal outcomes [citation:1].
        """
        client = self.clients.get(client_id)
        if not client:
            return {"error": "Client not found"}
        
        print(f"\n📄 Document Review:")
        print(f"   Client: {client['name']}")
        print(f"   Document Type: {document_type}")
        
        # Perform document review
        review_result = self._review_document(document_type, document_content, client)
        
        # Prepare principal reasons
        principal_reasons = [
            f"Risk Level: {review_result['risk_level']}",
            f"Issues Found: {review_result['issue_count']}"
        ]
        
        # Log the decision
        decision = self.tracker.log_consequential_decision(
            system_id="LEGAL-AI-001",
            consumer_id=client['client_id'],
            decision_type=DecisionType.LEGAL,
            decision=f"Document Review: {review_result['risk_level']} Risk",
            principal_reasons=principal_reasons,
            ai_was_determining_factor=False,
            ai_role_description="AI system reviewed legal document for potential issues",
            explanation=review_result['explanation'],
            decision_factors=review_result['factors'],
            notice_provided=True,
            is_ai_generated=True,
            human_review_available=True,
            appeal_rights_provided=True,
            metadata={
                "client_id": client_id,
                "client_demographics": {
                    "race": client.get('race'),
                    "gender": client.get('gender'),
                    "income_level": client.get('income_level')
                },
                "document_type": document_type,
                "risk_level": review_result['risk_level'],
                "issue_count": review_result['issue_count'],
                "attorney_id": attorney_id
            }
        )
        
        # Store review
        review = {
            "review_id": f"REVIEW-{int(time.time())}",
            "client_id": client_id,
            "document_type": document_type,
            "risk_level": review_result['risk_level'],
            "issue_count": review_result['issue_count'],
            "decision_id": decision['decision_id'],
            "timestamp": time.time()
        }
        
        self.document_reviews.append(review)
        
        print(f"\n📊 Document Review Result:")
        print(f"   Risk Level: {review_result['risk_level']}")
        print(f"   Issues Found: {review_result['issue_count']}")
        print(f"   Key Issues: {', '.join(review_result['key_issues'][:2])}")
        
        return review
    
    def _review_document(self, doc_type: str, content: str, client: dict) -> dict:
        """Simulate AI document review."""
        
        risk_levels = ["Low", "Medium", "High", "Critical"]
        risk_level = random.choice(risk_levels)
        issue_count = random.randint(0, 8)
        
        key_issues = [
            "Ambiguous liability clause",
            "Missing indemnification provision",
            "Unfavorable jurisdiction selection",
            "Insufficient damages cap",
            "Vague dispute resolution terms",
            "One-sided termination clause",
            "Missing confidentiality agreement",
            "Unreasonable indemnity obligations"
        ]
        
        selected_issues = random.sample(key_issues, min(issue_count, len(key_issues)))
        
        factors = {
            "document_complexity": {
                "score": random.randint(30, 90),
                "details": f"Document complexity assessed"
            },
            "risk_assessment": {
                "score": 100 - (issue_count * 10),
                "details": f"{issue_count} potential issues identified"
            }
        }
        
        return {
            "risk_level": risk_level,
            "issue_count": issue_count,
            "key_issues": selected_issues,
            "factors": factors,
            "explanation": f"Document review complete. {issue_count} potential issues identified. Overall risk level: {risk_level}."
        }
    
    def conduct_annual_risk_assessment(self) -> dict:
        """
        Conduct annual risk assessment as required by § 6-1-1704.
        
        The assessment must evaluate potential algorithmic discrimination
        across protected classes in legal AI outcomes [citation:1][citation:2][citation:4].
        """
        
        # Collect all predictions and recommendations for analysis
        all_decisions = self.tracker.decisions
        legal_decisions = [d for d in all_decisions if d['decision_type'] == DecisionType.LEGAL.value]
        
        # Analyze outcomes by demographic group
        demographic_data = {
            "race": {},
            "ethnicity": {},
            "gender": {},
            "income_level": {},
            "representation_type": {}
        }
        
        for decision in legal_decisions:
            demo = decision.get('metadata', {}).get('client_demographics', {})
            for protected, value in demo.items():
                if protected in demographic_data and value:
                    if value not in demographic_data[protected]:
                        demographic_data[protected][value] = {
                            "total": 0, 
                            "favorable": 0,
                            "avg_settlement": 0,
                            "settlement_sum": 0
                        }
                    
                    demographic_data[protected][value]["total"] += 1
                    
                    # Count favorable outcomes
                    if 'Plaintiff Likely to Prevail' in decision.get('decision', ''):
                        demographic_data[protected][value]["favorable"] += 1
                    
                    # Track settlement amounts
                    if 'Settlement' in decision.get('decision', ''):
                        # Extract amount from decision string
                        import re
                        amounts = re.findall(r'\$([0-9,]+)', decision.get('decision', ''))
                        if amounts:
                            amount = float(amounts[0].replace(',', ''))
                            demographic_data[protected][value]["settlement_sum"] += amount
        
        # Calculate average settlements
        for protected, groups in demographic_data.items():
            for group, stats in groups.items():
                if stats["total"] > 0:
                    stats["avg_settlement"] = stats["settlement_sum"] / stats["total"] if stats["settlement_sum"] > 0 else 0
        
        # Calculate disparate impact ratios
        disparate_impact = {}
        for protected, groups in demographic_data.items():
            if len(groups) > 1:
                favorable_rates = []
                group_names = []
                for group, stats in groups.items():
                    if stats["total"] > 0:
                        rate = stats["favorable"] / stats["total"] if stats["total"] > 0 else 0
                        favorable_rates.append(rate)
                        group_names.append(group)
                
                if len(favorable_rates) > 1:
                    disparate_impact[protected] = {
                        "min_rate": min(favorable_rates),
                        "max_rate": max(favorable_rates),
                        "ratio": min(favorable_rates) / max(favorable_rates) if max(favorable_rates) > 0 else 1.0,
                        "groups": group_names
                    }
        
        # Settlement disparity analysis
        settlement_disparity = {}
        for protected, groups in demographic_data.items():
            if len(groups) > 1:
                settlements = [stats["avg_settlement"] for stats in groups.values() if stats["total"] > 0]
                if len(settlements) > 1 and max(settlements) > 0:
                    settlement_disparity[protected] = {
                        "min_avg": min(settlements),
                        "max_avg": max(settlements),
                        "ratio": min(settlements) / max(settlements) if max(settlements) > 0 else 1.0
                    }
        
        assessment = self.tracker.conduct_risk_assessment(
            system_id="LEGAL-AI-001",
            assessment_date=time.time(),
            fairness_metrics={
                "total_decisions": len(legal_decisions),
                "favorable_outcome_rate": len([d for d in legal_decisions if 'Plaintiff Likely' in d.get('decision', '')]) / len(legal_decisions) if legal_decisions else 0,
                "disparate_impact": disparate_impact,
                "settlement_disparity": settlement_disparity,
                "demographic_breakdown": demographic_data
            },
            bias_test_results={
                "race": "PASS" if disparate_impact.get('race', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "ethnicity": "PASS" if disparate_impact.get('ethnicity', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "gender": "PASS" if disparate_impact.get('gender', {}).get('ratio', 1.0) >= 0.8 else "FAIL",
                "income": "PASS_WITH_MONITORING" if disparate_impact.get('income_level', {}).get('ratio', 1.0) >= 0.75 else "FAIL",
                "representation": "PASS" if disparate_impact.get('representation_type', {}).get('ratio', 1.0) >= 0.8 else "FAIL"
            },
            risk_factors=[
                {"factor": k, "disparity": v['ratio'], "status": "monitor" if v['ratio'] < 0.85 else "acceptable"}
                for k, v in disparate_impact.items()
            ],
            mitigation_strategies=[
                "Quarterly fairness testing across protected classes",
                "Attorney review for all predictions and recommendations",
                "Continuous monitoring for disparate outcomes",
                "Annual model validation",
                "Bias mitigation training for legal AI tools",
                "Regular calibration with actual case outcomes"
            ],
            residual_risk="LOW" if all(v.get('ratio', 1.0) >= 0.8 for v in disparate_impact.values()) else "MEDIUM",
            next_assessment_date=time.time() + 31536000,  # 1 year
            conducted_by="managing-partner@legalfirm.com"
        )
        
        print(f"\n📊 Annual Risk Assessment (§ 6-1-1704):")
        print(f"   Assessment ID: {assessment['assessment_id']}")
        print(f"   Total Legal Decisions: {len(legal_decisions)}")
        print(f"   Disparate Impact Ratios: { {k:v['ratio'] for k,v in disparate_impact.items()} }")
        print(f"   Settlement Disparity Ratios: { {k:v['ratio'] for k,v in settlement_disparity.items()} }")
        print(f"   Residual Risk: {assessment['residual_risk']}")
        print(f"   Next Assessment: {datetime.fromtimestamp(assessment['next_assessment_date'])}")
        print(f"\n⚖️ Note: Under SB 24-205, legal services are \"consequential decisions\" requiring annual risk assessments [citation:1][citation:2]")
        
        return assessment
    
    def handle_appeal(self, appeal_data: dict) -> dict:
        """Handle an appeal of a legal AI decision (§ 6-1-1708)."""
        
        appeal = self.tracker.handle_appeal(
            appeal_id=f"APPEAL-{int(time.time())}",
            consumer_id=appeal_data['client_id'],
            decision_id=appeal_data['decision_id'],
            appeal_date=time.time(),
            appeal_reason=appeal_data['reason'],
            review_status="IN_PROGRESS",
            reviewer="managing-partner",
            appeal_deadline=time.time() + 604800,  # 7 days
            evidence_submitted=appeal_data.get('evidence', []),
            metadata={
                "case_id": appeal_data.get('case_id'),
                "client_name": appeal_data.get('client_name')
            }
        )
        
        print(f"\n⚖️ Appeal Filed (§ 6-1-1708):")
        print(f"   Appeal ID: {appeal['appeal_id']}")
        print(f"   Reason: {appeal_data['reason'][:100]}...")
        print(f"   Status: {appeal['review_status']}")
        print(f"   Deadline: {datetime.fromtimestamp(appeal['appeal_deadline'])}")
        
        return appeal
    
    def qualify_safe_harbor(self) -> dict:
        """
        Qualify for safe harbor under § 6-1-1709 (NIST AI RMF).
        
        Organizations that comply with NIST AI RMF receive a rebuttable presumption
        of reasonable care [citation:1][citation:2][citation:6].
        """
        
        certificate = self.tracker.qualify_safe_harbor(
            framework="NIST AI RMF",
            version="1.0",
            assessment_date=time.time(),
            certified_by="third-party-auditor",
            certificate_url=f"https://{self.firm_name}/compliance/nist-certificate"
        )
        
        print(f"\n🛡️ Safe Harbor Certificate (§ 6-1-1709):")
        print(f"   Certificate ID: {certificate['certificate_id']}")
        print(f"   Framework: {certificate['framework']}")
        print(f"   Certified By: {certificate['certified_by']}")
        print(f"   Expires: {datetime.fromtimestamp(certificate['expiry_date'])}")
        print(f"   Note: Compliance with NIST AI RMF provides a rebuttable presumption of reasonable care [citation:1][citation:2]")
        
        return certificate
    
    def run_legal_ai_demo(self):
        """Run complete legal AI demonstration with Colorado AI Act compliance."""
        
        # Register system
        self.setup_legal_ai_system()
        
        # Add clients with diverse demographics
        clients = [
            {
                "name": "John Smith",
                "age": 45,
                "gender": "male",
                "race": "white",
                "ethnicity": "non-hispanic",
                "income_level": "middle",
                "education_level": "college",
                "representation_type": "private"
            },
            {
                "name": "Maria Garcia",
                "age": 38,
                "gender": "female",
                "race": "hispanic",
                "ethnicity": "hispanic",
                "income_level": "low",
                "education_level": "high_school",
                "representation_type": "legal_aid"
            },
            {
                "name": "James Johnson",
                "age": 52,
                "gender": "male",
                "race": "black",
                "ethnicity": "non-hispanic",
                "income_level": "middle",
                "education_level": "college",
                "representation_type": "private"
            },
            {
                "name": "Sarah Williams",
                "age": 34,
                "gender": "female",
                "race": "white",
                "ethnicity": "non-hispanic",
                "income_level": "low",
                "education_level": "associates",
                "representation_type": "pro_bono"
            },
            {
                "name": "Wei Chen",
                "age": 41,
                "gender": "male",
                "race": "asian",
                "ethnicity": "asian",
                "income_level": "middle",
                "education_level": "graduate",
                "representation_type": "private"
            }
        ]
        
        client_ids = []
        for client_data in clients:
            cid = self.add_client(client_data)
            client_ids.append(cid)
        
        # Create cases
        cases = [
            {
                "client_id": client_ids[0],
                "case_type": "personal_injury",
                "jurisdiction": "state",
                "court_level": "trial",
                "liability_assessment": 0.7,
                "damages_sought": 250000,
                "case_complexity": "medium",
                "legal_claims": ["negligence"],
                "assigned_attorney": "Attorney Williams"
            },
            {
                "client_id": client_ids[1],
                "case_type": "employment",
                "jurisdiction": "federal",
                "court_level": "trial",
                "liability_assessment": 0.6,
                "damages_sought": 150000,
                "case_complexity": "high",
                "legal_claims": ["discrimination", "retaliation"],
                "assigned_attorney": "Attorney Garcia"
            },
            {
                "client_id": client_ids[2],
                "case_type": "contract",
                "jurisdiction": "state",
                "court_level": "trial",
                "liability_assessment": 0.8,
                "damages_sought": 500000,
                "case_complexity": "medium",
                "legal_claims": ["breach_of_contract"],
                "assigned_attorney": "Attorney Chen"
            },
            {
                "client_id": client_ids[3],
                "case_type": "civil_rights",
                "jurisdiction": "federal",
                "court_level": "trial",
                "liability_assessment": 0.5,
                "damages_sought": 300000,
                "case_complexity": "high",
                "legal_claims": ["civil_rights_violation"],
                "assigned_attorney": "Attorney Smith"
            }
        ]
        
        case_ids = []
        for case_data in cases:
            case_id = self.create_case(case_data)
            case_ids.append(case_id)
        
        # Predict outcomes
        predictions = []
        for case_id in case_ids[:3]:
            pred = self.predict_case_outcome(case_id, "Attorney Williams")
            predictions.append(pred)
        
        # Generate settlement recommendations
        for case_id in case_ids[:2]:
            self.recommend_settlement(case_id, "Attorney Garcia")
        
        # Review documents
        doc_content = "Sample legal document content for review..."
        for client_id in client_ids[:3]:
            self.review_document(client_id, "contract", doc_content, "Attorney Chen")
        
        # Handle an appeal
        if predictions:
            appeal = self.handle_appeal({
                "client_id": client_ids[0],
                "decision_id": predictions[0].get('decision_id', 'unknown'),
                "case_id": case_ids[0],
                "client_name": clients[0]['name'],
                "reason": "The outcome prediction does not account for new precedent in similar cases.",
                "evidence": ["case_law_citation.pdf"]
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
        print(f"   Clients: {len(client_ids)}")
        print(f"   Cases: {len(case_ids)}")
        print(f"   Outcome Predictions: {len(self.predictions)}")
        print(f"   Settlement Recommendations: {len(self.settlement_recommendations)}")
        print(f"   Document Reviews: {len(self.document_reviews)}")
        print(f"   Appeals: {len(self.appeals)}")
        print(f"   Annual Risk Assessment: ✓")
        print(f"   Safe Harbor Qualified: ✓")
        print(f"\n⚖️ Legal Services as Consequential Decisions [citation:1][citation:2][citation:4]:")
        print(f"   • Case outcome predictions")
        print(f"   • Settlement recommendations")
        print(f"   • Document review")
        print(f"   • Client eligibility screening")
        
        return report


if __name__ == "__main__":
    system = LegalAIAssistant("Colorado Legal Partners")
    report = system.run_legal_ai_demo()
    
    # Save report
    with open("colorado_legal_report.json", "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\n✅ Report saved: colorado_legal_report.json")
    print(f"\n⚠️ Note: Colorado AI Act effective June 30, 2026 [citation:1][citation:7]")
    print(f"   Legal services are explicitly designated as \"consequential decisions\" under SB 24-205 [citation:2][citation:4]")
    print(f"\n📋 SB 24-205 Requirements Demonstrated:")
    print(f"   • Developer documentation (§ 6-1-1703)")
    print(f"   • Annual risk assessments (§ 6-1-1704)")
    print(f"   • Consumer notice (§ 6-1-1705)")
    print(f"   • Adverse explanation (§ 6-1-1706)")
    print(f"   • Correction rights (§ 6-1-1707)")
    print(f"   • Appeal rights (§ 6-1-1708)")
    print(f"   • Safe harbor (NIST AI RMF) (§ 6-1-1709)")
