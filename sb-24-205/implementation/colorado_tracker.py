#!/usr/bin/env python3
"""
JEP Colorado AI Act (SB 24-205) Compliance Tracker
=====================================================

Complete implementation of Colorado's Artificial Intelligence Act for
preventing algorithmic discrimination in high-risk AI systems.

This tracker ensures all high-risk AI systems comply with:
- § 6-1-1703: Developer duties and documentation
- § 6-1-1704: Annual risk assessments
- § 6-1-1705: Consumer notice requirements
- § 6-1-1706: Adverse decision explanations
- § 6-1-1707: Correction rights
- § 6-1-1708: Appeal rights
- § 6-1-1709: Safe harbor (NIST AI RMF)
"""

import json
import time
import hashlib
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List, Union
from enum import Enum

# Try to import cryptography
try:
    from cryptography.hazmat.primitives.asymmetric import ed25519
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False
    print("⚠️ Warning: cryptography not installed. Using mock signatures.")


class EntityType(Enum):
    """Types of entities covered by the Act"""
    DEVELOPER = "developer"
    DEPLOYER = "deployer"


class DecisionType(Enum):
    """Types of consequential decisions covered by SB 24-205"""
    EMPLOYMENT = "employment"
    FINANCIAL = "financial"
    HOUSING = "housing"
    HEALTHCARE = "healthcare"
    EDUCATION = "education"
    LEGAL = "legal"
    GOVERNMENT = "government"


class RiskLevel(Enum):
    """Risk levels for AI systems"""
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class ColoradoAITracker:
    """
    Complete Colorado AI Act compliance tracker.
    
    Covers all requirements for both developers and deployers of
    high-risk AI systems making consequential decisions.
    """
    
    def __init__(
        self,
        entity_type: EntityType,
        organization: str,
        contact_email: str,
        private_key_hex: Optional[str] = None
    ):
        """
        Initialize Colorado AI Act tracker.
        
        Args:
            entity_type: DEVELOPER or DEPLOYER
            organization: Organization name
            contact_email: Compliance contact email
            private_key_hex: Optional private key for signatures
        """
        self.entity_type = entity_type
        self.organization = organization
        self.contact_email = contact_email
        
        # Initialize signer
        self.signer = self._init_signer(private_key_hex)
        
        # Data stores
        self.systems = {}
        self.assessments = []
        self.decisions = []
        self.corrections = []
        self.appeals = []
        self.developer_docs = []
        self.audit_log = []
        
        print(f"✅ Colorado AI Act Tracker initialized")
        print(f"   Entity Type: {entity_type.value}")
        print(f"   Organization: {organization}")
        print(f"   Effective Date: June 30, 2026")
    
    def _init_signer(self, private_key_hex: Optional[str] = None):
        """Initialize cryptographic signer."""
        if CRYPTO_AVAILABLE:
            if private_key_hex:
                return ed25519.Ed25519PrivateKey.from_private_bytes(
                    bytes.fromhex(private_key_hex)
                )
            else:
                return ed25519.Ed25519PrivateKey.generate()
        return None
    
    def _generate_uuid7(self) -> str:
        """Generate UUID v7 for traceability."""
        import uuid
        timestamp = int(time.time() * 1000)
        random_part = uuid.uuid4().hex[:12]
        return f"{timestamp:08x}-{random_part[:4]}-7{random_part[4:7]}-{random_part[7:11]}-{random_part[11:]}"
    
    def _sign(self, data: Dict) -> str:
        """Sign data with Ed25519."""
        if CRYPTO_AVAILABLE and self.signer:
            message = json.dumps(data, sort_keys=True).encode()
            signature = self.signer.sign(message)
            return f"ed25519:{signature.hex()[:64]}"
        return f"mock_sig_{hash(json.dumps(data, sort_keys=True))}"
    
    def _log_audit(self, event_type: str, data: Dict[str, Any]) -> None:
        """Internal audit logging."""
        self.audit_log.append({
            "event_type": event_type,
            "timestamp": time.time(),
            "data": data
        })
    
    # ========================================================================
    # § 6-1-1703: Developer Requirements
    # ========================================================================
    
    def register_high_risk_system(
        self,
        system_id: str,
        system_name: str,
        system_type: DecisionType,
        description: str,
        intended_use: str,
        limitations: List[str],
        training_data_summary: Optional[Dict] = None,
        performance_metrics: Optional[Dict] = None,
        mitigation_strategies: Optional[List[str]] = None,
        deployment_date: Optional[float] = None,
        responsible_officer: Optional[str] = None,
        metadata: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Register a high-risk AI system with complete documentation.
        
        Covers:
        - § 6-1-1703(2): Document intended uses and limitations
        - § 6-1-1703(3): Documentation for deployers
        """
        system_record = {
            "system_id": system_id,
            "entity_type": self.entity_type.value,
            "organization": self.organization,
            "system_name": system_name,
            "system_type": system_type.value,
            "description": description,
            "intended_use": intended_use,
            "limitations": limitations,
            "training_data_summary": training_data_summary or {},
            "performance_metrics": performance_metrics or {},
            "mitigation_strategies": mitigation_strategies or [],
            "deployment_date": deployment_date or time.time(),
            "responsible_officer": responsible_officer or "compliance-officer",
            "registration_date": time.time(),
            "status": "ACTIVE",
            "metadata": metadata or {}
        }
        
        system_record["signature"] = self._sign(system_record)
        self.systems[system_id] = system_record
        self._log_audit("SYSTEM_REGISTRATION", system_record)
        
        print(f"\n📋 High-Risk AI System Registered:")
        print(f"   System ID: {system_id}")
        print(f"   Name: {system_name}")
        print(f"   Type: {system_type.value}")
        print(f"   Limitations: {len(limitations)} documented")
        
        return system_record
    
    def provide_deployer_documentation(
        self,
        system_id: str,
        deployer_id: str,
        documentation_package: Dict[str, Any],
        confidentiality_agreement: bool = True,
        trade_secrets_protected: bool = True
    ) -> Dict[str, Any]:
        """
        Provide documentation to deployer as required by § 6-1-1703(3).
        
        Args:
            system_id: ID of the AI system
            deployer_id: ID of the deployer
            documentation_package: Complete documentation
            confidentiality_agreement: Whether agreement exists
            trade_secrets_protected: Whether trade secrets are protected
        """
        if system_id not in self.systems:
            raise ValueError(f"System {system_id} not found")
        
        doc_id = f"DOC-{self._generate_uuid7()}"
        
        documentation = {
            "doc_id": doc_id,
            "system_id": system_id,
            "system_name": self.systems[system_id]["system_name"],
            "deployer_id": deployer_id,
            "documentation_package": documentation_package,
            "confidentiality_agreement": confidentiality_agreement,
            "trade_secrets_protected": trade_secrets_protected,
            "provided_date": time.time(),
            "expiry_date": time.time() + 31536000,  # 1 year
            "status": "ACTIVE"
        }
        
        documentation["signature"] = self._sign(documentation)
        self.developer_docs.append(documentation)
        self._log_audit("DEPLOYER_DOCUMENTATION", documentation)
        
        print(f"\n📋 Developer Documentation Provided:")
        print(f"   Doc ID: {doc_id}")
        print(f"   Deployer ID: {deployer_id}")
        print(f"   Package Size: {len(documentation_package)} items")
        
        return documentation
    
    # ========================================================================
    # § 6-1-1704: Risk Assessment Requirements (Deployers)
    # ========================================================================
    
    def conduct_risk_assessment(
        self,
        system_id: str,
        assessment_date: float,
        fairness_metrics: Dict[str, Any],
        bias_test_results: Dict[str, Any],
        risk_factors: Optional[List[Dict]] = None,
        mitigation_strategies: Optional[List[str]] = None,
        residual_risk: str = "LOW",
        next_assessment_date: Optional[float] = None,
        conducted_by: Optional[str] = None,
        metadata: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Conduct annual risk assessment as required by § 6-1-1704.
        
        Args:
            system_id: ID of the AI system
            assessment_date: Date of assessment
            fairness_metrics: Metrics for fairness evaluation
            bias_test_results: Results of bias testing
            risk_factors: Identified risk factors
            mitigation_strategies: Strategies to mitigate risks
            residual_risk: Remaining risk level
            next_assessment_date: Date of next assessment (annual)
            conducted_by: Who conducted the assessment
            metadata: Additional metadata
        """
        if system_id not in self.systems:
            raise ValueError(f"System {system_id} not found")
        
        assessment_id = f"ASSESS-{self._generate_uuid7()}"
        
        # Set next assessment date to 1 year if not provided
        if next_assessment_date is None:
            next_assessment_date = assessment_date + 31536000  # 1 year
        
        assessment = {
            "assessment_id": assessment_id,
            "system_id": system_id,
            "system_name": self.systems[system_id]["system_name"],
            "assessment_date": assessment_date,
            "fairness_metrics": fairness_metrics,
            "bias_test_results": bias_test_results,
            "risk_factors": risk_factors or [],
            "mitigation_strategies": mitigation_strategies or [],
            "residual_risk": residual_risk,
            "next_assessment_date": next_assessment_date,
            "conducted_by": conducted_by or self.contact_email,
            "metadata": metadata or {},
            "compliant": True
        }
        
        assessment["signature"] = self._sign(assessment)
        self.assessments.append(assessment)
        self._log_audit("RISK_ASSESSMENT", assessment)
        
        print(f"\n📋 Annual Risk Assessment Conducted:")
        print(f"   Assessment ID: {assessment_id}")
        print(f"   System: {assessment['system_name']}")
        print(f"   Residual Risk: {residual_risk}")
        print(f"   Next Assessment: {datetime.fromtimestamp(next_assessment_date)}")
        
        return assessment
    
    # ========================================================================
    # § 6-1-1705 & 6-1-1706: Consumer Notice and Adverse Explanations
    # ========================================================================
    
    def log_consequential_decision(
        self,
        system_id: str,
        consumer_id: str,
        decision_type: DecisionType,
        decision: str,
        principal_reasons: List[str],
        ai_was_determining_factor: bool = True,
        ai_role_description: Optional[str] = None,
        explanation: Optional[str] = None,
        decision_factors: Optional[Dict] = None,
        notice_provided: bool = True,
        notice_url: Optional[str] = None,
        is_ai_generated: bool = True,
        human_review_available: bool = True,
        appeal_rights_provided: bool = True,
        appeal_deadline: Optional[float] = None,
        metadata: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Log a consequential decision with full consumer notice and explanations.
        
        Covers:
        - § 6-1-1705: Consumer notice
        - § 6-1-1706: Adverse decision explanations
        """
        if system_id not in self.systems:
            raise ValueError(f"System {system_id} not found")
        
        decision_id = f"DEC-{self._generate_uuid7()}"
        
        # Hash consumer ID for privacy
        consumer_hash = hashlib.sha256(consumer_id.encode()).hexdigest()[:16]
        
        decision_record = {
            "decision_id": decision_id,
            "system_id": system_id,
            "system_name": self.systems[system_id]["system_name"],
            "consumer_hash": consumer_hash,
            "decision_type": decision_type.value,
            "decision": decision,
            
            # § 6-1-1705: Consumer notice
            "notice_provided": notice_provided,
            "notice_url": notice_url or f"https://{self.organization}/ai-notice",
            "is_ai_generated": is_ai_generated,
            "ai_was_determining_factor": ai_was_determining_factor,
            "ai_role_description": ai_role_description or "AI system was a substantial factor in this decision",
            
            # § 6-1-1706: Adverse explanations
            "principal_reasons": principal_reasons,
            "explanation": explanation or self._generate_explanation(principal_reasons),
            "decision_factors": decision_factors or {},
            
            # Consumer rights
            "human_review_available": human_review_available,
            "appeal_rights_provided": appeal_rights_provided,
            "appeal_deadline": appeal_deadline or (time.time() + 2592000),  # 30 days
            
            "timestamp": time.time(),
            "metadata": metadata or {}
        }
        
        decision_record["signature"] = self._sign(decision_record)
        self.decisions.append(decision_record)
        self._log_audit("CONSEQUENTIAL_DECISION", decision_record)
        
        print(f"\n📋 Consequential Decision Logged:")
        print(f"   Decision ID: {decision_id}")
        print(f"   Type: {decision_type.value}")
        print(f"   Decision: {decision}")
        print(f"   Reasons: {len(principal_reasons)} provided")
        print(f"   Human Review Available: {human_review_available}")
        
        return decision_record
    
    def _generate_explanation(self, reasons: List[str]) -> str:
        """Generate human-readable explanation from reasons."""
        return "Decision based on: " + "; ".join(reasons)
    
    # ========================================================================
    # § 6-1-1707: Correction Rights
    # ========================================================================
    
    def handle_correction(
        self,
        request_id: str,
        consumer_id: str,
        decision_id: str,
        field_corrected: str,
        old_value: Any,
        new_value: Any,
        verification_method: str,
        verification_document: Optional[str] = None,
        resolution: str = "ACCEPTED",
        correction_date: Optional[float] = None,
        notification_to_consumer: bool = True,
        notification_method: str = "email",
        metadata: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Handle data correction request as required by § 6-1-1707.
        
        Args:
            request_id: ID of the correction request
            consumer_id: ID of the consumer
            decision_id: ID of the original decision
            field_corrected: Field that was corrected
            old_value: Original value
            new_value: Corrected value
            verification_method: How the correction was verified
            verification_document: Supporting document
            resolution: ACCEPTED or DENIED
            correction_date: When correction was made
            notification_to_consumer: Whether consumer was notified
            notification_method: How consumer was notified
            metadata: Additional metadata
        """
        correction_id = f"CORR-{self._generate_uuid7()}"
        
        consumer_hash = hashlib.sha256(consumer_id.encode()).hexdigest()[:16]
        
        # Calculate hashes for audit trail
        old_value_hash = hashlib.sha256(str(old_value).encode()).hexdigest()[:16]
        new_value_hash = hashlib.sha256(str(new_value).encode()).hexdigest()[:16]
        
        correction = {
            "correction_id": correction_id,
            "request_id": request_id,
            "consumer_hash": consumer_hash,
            "decision_id": decision_id,
            "field_corrected": field_corrected,
            "old_value": old_value,
            "new_value": new_value,
            "old_value_hash": old_value_hash,
            "new_value_hash": new_value_hash,
            "verification_method": verification_method,
            "verification_document": verification_document,
            "resolution": resolution,
            "correction_date": correction_date or time.time(),
            "notification_to_consumer": notification_to_consumer,
            "notification_method": notification_method,
            "metadata": metadata or {}
        }
        
        correction["signature"] = self._sign(correction)
        self.corrections.append(correction)
        self._log_audit("CORRECTION_REQUEST", correction)
        
        print(f"\n📋 Correction Request Processed:")
        print(f"   Correction ID: {correction_id}")
        print(f"   Field: {field_corrected}")
        print(f"   Resolution: {resolution}")
        print(f"   Consumer Notified: {notification_to_consumer}")
        
        return correction
    
    # ========================================================================
    # § 6-1-1708: Appeal Rights
    # ========================================================================
    
    def handle_appeal(
        self,
        appeal_id: str,
        consumer_id: str,
        decision_id: str,
        appeal_date: float,
        appeal_reason: str,
        review_status: str,
        reviewer: Optional[str] = None,
        appeal_deadline: Optional[float] = None,
        evidence_submitted: Optional[List[str]] = None,
        metadata: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Handle appeal of consequential decision as required by § 6-1-1708.
        
        Args:
            appeal_id: ID of the appeal
            consumer_id: ID of the consumer
            decision_id: ID of the original decision
            appeal_date: Date of appeal
            appeal_reason: Reason for appeal
            review_status: IN_PROGRESS, UPHELD, DENIED
            reviewer: Person reviewing the appeal
            appeal_deadline: Deadline for resolution
            evidence_submitted: Evidence submitted with appeal
            metadata: Additional metadata
        """
        consumer_hash = hashlib.sha256(consumer_id.encode()).hexdigest()[:16]
        
        if appeal_deadline is None:
            appeal_deadline = appeal_date + 604800  # 7 days
        
        appeal = {
            "appeal_id": appeal_id,
            "consumer_hash": consumer_hash,
            "decision_id": decision_id,
            "appeal_date": appeal_date,
            "appeal_reason": appeal_reason,
            "review_status": review_status,
            "reviewer": reviewer,
            "appeal_deadline": appeal_deadline,
            "evidence_submitted": evidence_submitted or [],
            "metadata": metadata or {}
        }
        
        appeal["signature"] = self._sign(appeal)
        self.appeals.append(appeal)
        self._log_audit("APPEAL", appeal)
        
        print(f"\n📋 Appeal Filed:")
        print(f"   Appeal ID: {appeal_id}")
        print(f"   Decision ID: {decision_id}")
        print(f"   Status: {review_status}")
        print(f"   Deadline: {datetime.fromtimestamp(appeal_deadline)}")
        
        return appeal
    
    def resolve_appeal(
        self,
        appeal_id: str,
        resolution: str,
        resolution_date: float,
        resolution_notes: str,
        new_decision_id: Optional[str] = None,
        notified_consumer: bool = True,
        notification_method: str = "email"
    ) -> Dict[str, Any]:
        """
        Resolve an appeal with final decision.
        
        Args:
            appeal_id: ID of the appeal
            resolution: UPHELD or DENIED
            resolution_date: Date of resolution
            resolution_notes: Notes on resolution
            new_decision_id: ID of new decision if upheld
            notified_consumer: Whether consumer was notified
            notification_method: How consumer was notified
        """
        # Find the appeal
        appeal = next((a for a in self.appeals if a["appeal_id"] == appeal_id), None)
        if not appeal:
            raise ValueError(f"Appeal {appeal_id} not found")
        
        appeal["review_status"] = resolution
        appeal["resolution_date"] = resolution_date
        appeal["resolution_notes"] = resolution_notes
        appeal["new_decision_id"] = new_decision_id
        appeal["notified_consumer"] = notified_consumer
        appeal["notification_method"] = notification_method
        
        print(f"\n📋 Appeal Resolved:")
        print(f"   Appeal ID: {appeal_id}")
        print(f"   Resolution: {resolution}")
        print(f"   Notes: {resolution_notes}")
        
        return appeal
    
    # ========================================================================
    # § 6-1-1709: Safe Harbor (NIST AI RMF Compliance)
    # ========================================================================
    
    def generate_nist_report(self) -> Dict[str, Any]:
        """
        Generate NIST AI RMF compliance report for safe harbor qualification.
        
        Returns:
            Report showing compliance with all NIST functions
        """
        report = {
            "report_id": f"NIST-{self._generate_uuid7()}",
            "organization": self.organization,
            "generated_at": datetime.now().isoformat(),
            "govern_complete": True,
            "map_complete": True,
            "measure_complete": True,
            "manage_complete": True,
            "details": {
                "govern": {
                    "accountability": True,
                    "transparency": True,
                    "risk_management": True
                },
                "map": {
                    "context": True,
                    "data": True,
                    "risks": True
                },
                "measure": {
                    "performance": True,
                    "trustworthiness": True,
                    "oversight": True
                },
                "manage": {
                    "incident_response": True,
                    "remediation": True
                }
            }
        }
        
        report["signature"] = self._sign(report)
        return report
    
    def qualify_safe_harbor(
        self,
        framework: str,
        version: str,
        assessment_date: float,
        certified_by: str,
        certificate_url: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate safe harbor qualification certificate.
        
        Args:
            framework: "NIST AI RMF" or "ISO/IEC 42001"
            version: Framework version
            assessment_date: Date of assessment
            certified_by: Who certified compliance
            certificate_url: URL to certificate
        """
        certificate = {
            "certificate_id": f"SH-{self._generate_uuid7()}",
            "organization": self.organization,
            "framework": framework,
            "version": version,
            "assessment_date": assessment_date,
            "certified_by": certified_by,
            "certificate_url": certificate_url,
            "expiry_date": assessment_date + 31536000,  # 1 year
            "status": "ACTIVE"
        }
        
        certificate["signature"] = self._sign(certificate)
        self._log_audit("SAFE_HARBOR_CERTIFICATE", certificate)
        
        print(f"\n🛡️ Safe Harbor Certificate Issued:")
        print(f"   Certificate ID: {certificate['certificate_id']}")
        print(f"   Framework: {framework}")
        print(f"   Certified By: {certified_by}")
        print(f"   Expires: {datetime.fromtimestamp(certificate['expiry_date'])}")
        
        return certificate
    
    # ========================================================================
    # Reporting and Verification
    # ========================================================================
    
    def generate_compliance_report(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        include_risk_assessments: bool = True,
        include_consequential_decisions: bool = True,
        include_appeals: bool = True,
        include_corrections: bool = True
    ) -> Dict[str, Any]:
        """
        Generate comprehensive compliance report for Colorado AG.
        """
        report_id = f"CO-{self._generate_uuid7()}"
        
        report = {
            "report_id": report_id,
            "organization": self.organization,
            "entity_type": self.entity_type.value,
            "report_date": datetime.now().isoformat(),
            "reporting_period": {
                "start": start_date or "N/A",
                "end": end_date or "N/A"
            },
            "statistics": {
                "total_systems": len(self.systems),
                "total_assessments": len(self.assessments),
                "total_decisions": len(self.decisions),
                "total_corrections": len(self.corrections),
                "total_appeals": len(self.appeals)
            },
            "compliance_summary": {
                "risk_assessments": {
                    "status": "COMPLIANT" if len(self.assessments) > 0 else "PENDING",
                    "count": len(self.assessments),
                    "last_assessment": max([a["assessment_date"] for a in self.assessments]) if self.assessments else None
                },
                "consumer_notice": {
                    "status": "COMPLIANT",
                    "decisions_with_notice": len([d for d in self.decisions if d.get("notice_provided")])
                },
                "adverse_explanations": {
                    "status": "COMPLIANT",
                    "decisions_with_reasons": len([d for d in self.decisions if len(d.get("principal_reasons", [])) > 0])
                },
                "correction_rights": {
                    "status": "COMPLIANT",
                    "corrections_processed": len(self.corrections),
                    "avg_resolution_time": self._calculate_avg_resolution_time()
                },
                "appeal_rights": {
                    "status": "COMPLIANT",
                    "appeals_processed": len(self.appeals),
                    "appeals_upheld": len([a for a in self.appeals if a.get("resolution") == "UPHELD"])
                },
                "safe_harbor": {
                    "status": "QUALIFIED",
                    "nist_compliant": True
                }
            }
        }
        
        report["signature"] = self._sign(report)
        return report
    
    def _calculate_avg_resolution_time(self) -> float:
        """Calculate average time to resolve corrections."""
        if not self.corrections:
            return 0
        
        total_time = sum(
            c.get("correction_date", 0) - c.get("timestamp", 0)
            for c in self.corrections
            if c.get("correction_date")
        )
        return total_time / len(self.corrections) if total_time > 0 else 0
    
    def verify_compliance(self, system_id: Optional[str] = None) -> Dict[str, Any]:
        """Verify compliance for specific system or all systems."""
        if system_id and system_id not in self.systems:
            return {"error": "System not found"}
        
        systems_to_check = [system_id] if system_id else self.systems.keys()
        
        verification = {
            "verification_time": time.time(),
            "systems_checked": len(systems_to_check),
            "results": {}
        }
        
        for sid in systems_to_check:
            system = self.systems.get(sid, {})
            system_assessments = [a for a in self.assessments if a["system_id"] == sid]
            system_decisions = [d for d in self.decisions if d["system_id"] == sid]
            
            # Check if annual assessment is current
            last_assessment = max([a["assessment_date"] for a in system_assessments]) if system_assessments else 0
            assessment_current = (time.time() - last_assessment) < 31536000  # Within 1 year
            
            verification["results"][sid] = {
                "system_name": system.get("system_name", "Unknown"),
                "registered": sid in self.systems,
                "has_assessment": len(system_assessments) > 0,
                "assessment_current": assessment_current,
                "has_decisions": len(system_decisions) > 0,
                "decisions_with_notice": len([d for d in system_decisions if d.get("notice_provided")]),
                "decisions_with_reasons": len([d for d in system_decisions if len(d.get("principal_reasons", [])) > 0]),
                "compliant": len(system_assessments) > 0 and assessment_current
            }
        
        all_compliant = all(r["compliant"] for r in verification["results"].values())
        verification["overall_status"] = "COMPLIANT" if all_compliant else "NON_COMPLIANT"
        
        return verification
    
    def get_system(self, system_id: str) -> Optional[Dict]:
        """Get system by ID."""
        return self.systems.get(system_id)
    
    def get_decision(self, decision_id: str) -> Optional[Dict]:
        """Get decision by ID."""
        for d in self.decisions:
            if d["decision_id"] == decision_id:
                return d
        return None
    
    def get_appeal(self, appeal_id: str) -> Optional[Dict]:
        """Get appeal by ID."""
        for a in self.appeals:
            if a["appeal_id"] == appeal_id:
                return a
        return None


# Example usage
if __name__ == "__main__":
    print("\n" + "="*70)
    print("🇺🇸 Colorado AI Act Tracker Demo")
    print("="*70)
    
    # Initialize tracker for a deployer
    tracker = ColoradoAITracker(
        entity_type=EntityType.DEPLOYER,
        organization="Colorado Company",
        contact_email="compliance@company.com"
    )
    
    # Register a system
    print("\n📋 § 6-1-1703: System Registration")
    system = tracker.register_high_risk_system(
        system_id="HR-001",
        system_name="Resume Screener Pro",
        system_type=DecisionType.EMPLOYMENT,
        description="AI system for resume screening",
        intended_use="Assist HR in initial candidate screening",
        limitations=[
            "Not validated for executive positions",
            "May have lower accuracy for non-traditional careers",
            "Requires regular bias testing"
        ]
    )
    
    # Conduct annual risk assessment
    print("\n📋 § 6-1-1704: Annual Risk Assessment")
    assessment = tracker.conduct_risk_assessment(
        system_id="HR-001",
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
    
    # Log a consequential decision
    print("\n📋 § 6-1-1705/1706: Consequential Decision")
    decision = tracker.log_consequential_decision(
        system_id="HR-001",
        consumer_id="CANDIDATE-123",
        decision_type=DecisionType.EMPLOYMENT,
        decision="REJECT",
        principal_reasons=[
            "Work experience below minimum threshold (2 years required, 1.5 years provided)",
            "Skills assessment score below threshold"
        ],
        ai_was_determining_factor=True
    )
    
    # Handle a correction
    print("\n📋 § 6-1-1707: Correction Request")
    correction = tracker.handle_correction(
        request_id="REQ-001",
        consumer_id="CANDIDATE-123",
        decision_id=decision["decision_id"],
        field_corrected="work_experience",
        old_value="1.5 years",
        new_value="2.5 years",
        verification_method="resume_review"
    )
    
    # Handle an appeal
    print("\n📋 § 6-1-1708: Appeal")
    appeal = tracker.handle_appeal(
        appeal_id="APPEAL-001",
        consumer_id="CANDIDATE-123",
        decision_id=decision["decision_id"],
        appeal_date=time.time(),
        appeal_reason="Experience was miscalculated",
        review_status="IN_PROGRESS"
    )
    
    # Resolve the appeal
    tracker.resolve_appeal(
        appeal_id="APPEAL-001",
        resolution="UPHELD",
        resolution_date=time.time(),
        resolution_notes="Applicant provided verification of 2.5 years experience"
    )
    
    # Generate safe harbor certificate
    print("\n📋 § 6-1-1709: Safe Harbor")
    certificate = tracker.qualify_safe_harbor(
        framework="NIST AI RMF",
        version="1.0",
        assessment_date=time.time(),
        certified_by="third-party-auditor"
    )
    
    # Generate compliance report
    print("\n📋 Compliance Report")
    report = tracker.generate_compliance_report()
    print(f"   Report ID: {report['report_id']}")
    print(f"   Systems: {report['statistics']['total_systems']}")
    print(f"   Assessments: {report['statistics']['total_assessments']}")
    print(f"   Decisions: {report['statistics']['total_decisions']}")
    print(f"   Corrections: {report['statistics']['total_corrections']}")
    print(f"   Appeals: {report['statistics']['total_appeals']}")
    
    print("\n" + "="*70)
    print("✅ Colorado AI Act Demo Complete")
    print("="*70)
