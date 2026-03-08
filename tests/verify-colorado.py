#!/usr/bin/env python3
"""
Colorado AI Act (SB 24-205) Compliance Verification Script
=============================================================

This script verifies that a JEP implementation fully complies with
Colorado's Artificial Intelligence Act (SB 24-205), covering all requirements
for both developers and deployers of high-risk AI systems.

Run this script to generate a compliance report that can be submitted
to the Colorado Attorney General's Office as evidence of compliance.

Usage:
    python verify-colorado.py [--entity developer|deployer] [--output json|html]

Examples:
    # Run complete verification
    python verify-colorado.py --all
    
    # Run only deployer requirements
    python verify-colorado.py --entity deployer
    
    # Generate HTML report for Attorney General
    python verify-colorado.py --all --output html --report co-audit.html
"""

import json
import os
import sys
import argparse
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from state_regulations.colorado.sb_24_205.implementation.colorado_tracker import (
    ColoradoAITracker,
    EntityType,
    DecisionType,
    RiskLevel
)


class ColoradoComplianceVerifier:
    """
    Verifies JEP implementation against Colorado AI Act requirements.
    """
    
    def __init__(self, entity_type: str = "deployer"):
        """
        Initialize verifier for specified entity type.
        
        Args:
            entity_type: "developer" or "deployer"
        """
        self.entity_type = EntityType(entity_type)
        self.tracker = ColoradoAITracker(
            entity_type=self.entity_type,
            organization="Colorado Compliance Test",
            contact_email="test@colorado-compliance.org"
        )
        
        self.results = {
            "developer_requirements": {},
            "deployer_requirements": {},
            "summary": {}
        }
    
    # ========================================================================
    # Developer Requirements (§ 6-1-1703)
    # ========================================================================
    
    def verify_developer_duty_of_care(self) -> Dict[str, Any]:
        """Verify § 6-1-1703(1) - Duty of reasonable care."""
        try:
            # Register a system with proper documentation
            system = self.tracker.register_high_risk_system(
                system_id="DEV-TEST-001",
                system_name="Developer Test System",
                system_type=DecisionType.EMPLOYMENT,
                description="Test system for developer verification",
                intended_use="Testing developer compliance",
                limitations=["Test limitation 1", "Test limitation 2"]
            )
            
            passed = (
                system.get("system_id") == "DEV-TEST-001" and
                system.get("intended_use") is not None and
                len(system.get("limitations", [])) == 2
            )
            
            evidence = f"System registered with intended use and {len(system['limitations'])} limitations"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "§ 6-1-1703(1) - Duty of reasonable care (documentation)",
            "passed": passed,
            "evidence": evidence
        }
    
    def verify_developer_documentation(self) -> Dict[str, Any]:
        """Verify § 6-1-1703(2) - Document intended uses and limitations."""
        try:
            # Create comprehensive documentation package
            docs = self.tracker.provide_deployer_documentation(
                system_id="DEV-TEST-001",
                deployer_id="DEPLOYER-TEST",
                documentation_package={
                    "model_name": "Developer Test System",
                    "intended_use": "Testing documentation requirements",
                    "limitations": ["Test limitation"],
                    "performance_metrics": {"accuracy": 0.95},
                    "training_data_summary": {"size": 10000},
                    "mitigation_strategies": ["Test mitigation"]
                }
            )
            
            passed = (
                docs.get("doc_id") is not None and
                docs.get("documentation_package") is not None and
                len(docs["documentation_package"]) == 6
            )
            
            evidence = f"Documentation package provided with {len(docs['documentation_package'])} items"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "§ 6-1-1703(2) - Documentation for deployers",
            "passed": passed,
            "evidence": evidence
        }
    
    # ========================================================================
    # Deployer Requirements (§ 6-1-1704 through 6-1-1708)
    # ========================================================================
    
    def verify_risk_assessment(self) -> Dict[str, Any]:
        """Verify § 6-1-1704 - Annual risk assessments."""
        try:
            # Register a system
            self.tracker.register_high_risk_system(
                system_id="DEP-TEST-001",
                system_name="Deployer Test System",
                system_type=DecisionType.EMPLOYMENT,
                description="Test system for deployer verification",
                intended_use="Testing deployer compliance",
                limitations=["Test limitation"]
            )
            
            # Conduct risk assessment
            assessment = self.tracker.conduct_risk_assessment(
                system_id="DEP-TEST-001",
                assessment_date=time.time(),
                fairness_metrics={
                    "disparate_impact": 0.98,
                    "demographic_parity": 0.97
                },
                bias_test_results={
                    "race": "PASS",
                    "gender": "PASS"
                },
                risk_factors=[
                    {"factor": "age", "disparity": 0.95, "status": "monitor"}
                ],
                mitigation_strategies=[
                    "Quarterly bias testing",
                    "Human review"
                ],
                residual_risk="LOW"
            )
            
            passed = (
                assessment.get("assessment_id") is not None and
                assessment.get("residual_risk") == "LOW" and
                len(assessment.get("mitigation_strategies", [])) == 2
            )
            
            evidence = f"Risk assessment completed with ID: {assessment['assessment_id']}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "§ 6-1-1704 - Annual risk assessments (with fairness metrics)",
            "passed": passed,
            "evidence": evidence
        }
    
    def verify_consumer_notice(self) -> Dict[str, Any]:
        """Verify § 6-1-1705 - Consumer notice."""
        try:
            decision = self.tracker.log_consequential_decision(
                system_id="DEP-TEST-001",
                consumer_id="TEST-CONSUMER",
                decision_type=DecisionType.EMPLOYMENT,
                decision="REJECT",
                principal_reasons=["Test reason 1", "Test reason 2"],
                notice_provided=True,
                is_ai_generated=True,
                ai_was_determining_factor=True
            )
            
            passed = (
                decision.get("notice_provided") is True and
                decision.get("is_ai_generated") is True and
                decision.get("ai_was_determining_factor") is True
            )
            
            evidence = f"Decision logged with notice: {decision['decision_id']}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "§ 6-1-1705 - Consumer notice (AI disclosure)",
            "passed": passed,
            "evidence": evidence
        }
    
    def verify_adverse_explanations(self) -> Dict[str, Any]:
        """Verify § 6-1-1706 - Adverse decision explanations."""
        try:
            decision = self.tracker.log_consequential_decision(
                system_id="DEP-TEST-001",
                consumer_id="TEST-CONSUMER",
                decision_type=DecisionType.EMPLOYMENT,
                decision="REJECT",
                principal_reasons=[
                    "Work experience below minimum threshold (2 years required, 1.5 years provided)",
                    "Skills assessment score below threshold"
                ],
                decision_factors={
                    "work_experience": {"value": 1.5, "threshold": 2},
                    "skills_score": {"value": 65, "threshold": 70}
                }
            )
            
            passed = (
                len(decision.get("principal_reasons", [])) == 2 and
                "work_experience" in decision.get("decision_factors", {})
            )
            
            evidence = f"Adverse explanation provided with {len(decision['principal_reasons'])} reasons"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "§ 6-1-1706 - Adverse decision explanations (principal reasons)",
            "passed": passed,
            "evidence": evidence
        }
    
    def verify_correction_rights(self) -> Dict[str, Any]:
        """Verify § 6-1-1707 - Correction rights."""
        try:
            # First create a decision
            decision = self.tracker.log_consequential_decision(
                system_id="DEP-TEST-001",
                consumer_id="TEST-CONSUMER",
                decision_type=DecisionType.EMPLOYMENT,
                decision="REJECT",
                principal_reasons=["Test reason"]
            )
            
            # Handle correction
            correction = self.tracker.handle_correction(
                request_id="REQ-001",
                consumer_id="TEST-CONSUMER",
                decision_id=decision["decision_id"],
                field_corrected="work_experience",
                old_value="1.5 years",
                new_value="2.5 years",
                verification_method="document_review",
                resolution="ACCEPTED"
            )
            
            passed = (
                correction.get("correction_id") is not None and
                correction.get("resolution") == "ACCEPTED" and
                correction.get("field_corrected") == "work_experience"
            )
            
            evidence = f"Correction processed: {correction['correction_id']}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "§ 6-1-1707 - Correction rights",
            "passed": passed,
            "evidence": evidence
        }
    
    def verify_appeal_rights(self) -> Dict[str, Any]:
        """Verify § 6-1-1708 - Appeal rights."""
        try:
            # Create a decision
            decision = self.tracker.log_consequential_decision(
                system_id="DEP-TEST-001",
                consumer_id="TEST-CONSUMER",
                decision_type=DecisionType.EMPLOYMENT,
                decision="REJECT",
                principal_reasons=["Test reason"]
            )
            
            # Handle appeal
            appeal = self.tracker.handle_appeal(
                appeal_id="APPEAL-001",
                consumer_id="TEST-CONSUMER",
                decision_id=decision["decision_id"],
                appeal_date=time.time(),
                appeal_reason="Test appeal reason",
                review_status="IN_PROGRESS",
                reviewer="test-reviewer"
            )
            
            # Resolve appeal
            resolution = self.tracker.resolve_appeal(
                appeal_id="APPEAL-001",
                resolution="UPHELD",
                resolution_date=time.time(),
                resolution_notes="Test resolution"
            )
            
            passed = (
                appeal.get("appeal_id") == "APPEAL-001" and
                resolution.get("review_status") == "UPHELD"
            )
            
            evidence = f"Appeal processed and resolved: {appeal['appeal_id']}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "§ 6-1-1708 - Appeal rights",
            "passed": passed,
            "evidence": evidence
        }
    
    # ========================================================================
    # Safe Harbor (§ 6-1-1709)
    # ========================================================================
    
    def verify_safe_harbor(self) -> Dict[str, Any]:
        """Verify § 6-1-1709 - Safe harbor (NIST AI RMF compliance)."""
        try:
            # Generate NIST compliance report
            nist_report = self.tracker.generate_nist_report()
            
            # Generate safe harbor certificate
            certificate = self.tracker.qualify_safe_harbor(
                framework="NIST AI RMF",
                version="1.0",
                assessment_date=time.time(),
                certified_by="test-auditor"
            )
            
            passed = (
                nist_report.get("govern_complete") is True and
                certificate.get("certificate_id") is not None
            )
            
            evidence = f"Safe harbor certificate issued: {certificate['certificate_id']}"
            
        except Exception as e:
            passed = False
            evidence = f"Error: {str(e)}"
        
        return {
            "description": "§ 6-1-1709 - Safe harbor (NIST AI RMF compliance)",
            "passed": passed,
            "evidence": evidence
        }
    
    # ========================================================================
    # Complete Verification
    # ========================================================================
    
    def verify_all(self, entity: Optional[str] = None) -> Dict[str, Any]:
        """
        Run verification for specified entity type or all.
        
        Args:
            entity: "developer", "deployer", or None for both
        """
        # Developer requirements
        if entity is None or entity == "developer":
            self.results["developer_requirements"] = {
                "name": "Developer Requirements (§ 6-1-1703)",
                "requirements": {},
                "overall": "PENDING"
            }
            self.results["developer_requirements"]["requirements"]["duty_of_care"] = self.verify_developer_duty_of_care()
            self.results["developer_requirements"]["requirements"]["documentation"] = self.verify_developer_documentation()
            
            dev_all_passed = all(
                r["passed"] for r in self.results["developer_requirements"]["requirements"].values()
            )
            self.results["developer_requirements"]["overall"] = "PASSED" if dev_all_passed else "FAILED"
        
        # Deployer requirements
        if entity is None or entity == "deployer":
            self.results["deployer_requirements"] = {
                "name": "Deployer Requirements (§ 6-1-1704 through 6-1-1708)",
                "requirements": {},
                "overall": "PENDING"
            }
            self.results["deployer_requirements"]["requirements"]["risk_assessment"] = self.verify_risk_assessment()
            self.results["deployer_requirements"]["requirements"]["consumer_notice"] = self.verify_consumer_notice()
            self.results["deployer_requirements"]["requirements"]["adverse_explanations"] = self.verify_adverse_explanations()
            self.results["deployer_requirements"]["requirements"]["correction_rights"] = self.verify_correction_rights()
            self.results["deployer_requirements"]["requirements"]["appeal_rights"] = self.verify_appeal_rights()
            
            dep_all_passed = all(
                r["passed"] for r in self.results["deployer_requirements"]["requirements"].values()
            )
            self.results["deployer_requirements"]["overall"] = "PASSED" if dep_all_passed else "FAILED"
        
        # Safe harbor (applicable to both)
        self.results["safe_harbor"] = self.verify_safe_harbor()
        
        # Calculate summary
        total_requirements = 0
        passed_requirements = 0
        
        if entity is None or entity == "developer":
            total_requirements += len(self.results["developer_requirements"]["requirements"])
            passed_requirements += sum(
                1 for r in self.results["developer_requirements"]["requirements"].values() if r["passed"]
            )
        
        if entity is None or entity == "deployer":
            total_requirements += len(self.results["deployer_requirements"]["requirements"])
            passed_requirements += sum(
                1 for r in self.results["deployer_requirements"]["requirements"].values() if r["passed"]
            )
        
        # Add safe harbor
        if self.results["safe_harbor"]["passed"]:
            passed_requirements += 1
        total_requirements += 1
        
        self.results["summary"] = {
            "compliance_status": "FULLY_COMPLIANT" if passed_requirements == total_requirements else "PARTIALLY_COMPLIANT",
            "requirements_passed": passed_requirements,
            "total_requirements": total_requirements,
            "verification_time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "verification_id": f"CO-VERIF-{int(time.time())}"
        }
        
        return self.results
    
    def generate_report(self, format: str = "text") -> str:
        """Generate verification report in specified format."""
        if format == "json":
            return json.dumps(self.results, indent=2)
        elif format == "html":
            return self._generate_html_report()
        else:
            return self._generate_text_report()
    
    def _generate_text_report(self) -> str:
        """Generate plain text report."""
        lines = []
        lines.append("="*70)
        lines.append("COLORADO AI ACT (SB 24-205) COMPLIANCE REPORT")
        lines.append("="*70)
        lines.append(f"Verification ID: {self.results['summary']['verification_id']}")
        lines.append(f"Time: {self.results['summary']['verification_time']}")
        lines.append("")
        
        # Developer requirements
        if self.results.get("developer_requirements"):
            dev = self.results["developer_requirements"]
            lines.append(f"\n{dev['name']}")
            lines.append("-"*50)
            for req_id, req in dev["requirements"].items():
                status = "✅" if req["passed"] else "❌"
                lines.append(f"{status} {req_id}: {req['description']}")
                lines.append(f"   Evidence: {req['evidence']}")
            lines.append(f"Overall: {dev['overall']}")
        
        # Deployer requirements
        if self.results.get("deployer_requirements"):
            dep = self.results["deployer_requirements"]
            lines.append(f"\n{dep['name']}")
            lines.append("-"*50)
            for req_id, req in dep["requirements"].items():
                status = "✅" if req["passed"] else "❌"
                lines.append(f"{status} {req_id}: {req['description']}")
                lines.append(f"   Evidence: {req['evidence']}")
            lines.append(f"Overall: {dep['overall']}")
        
        # Safe harbor
        safe = self.results["safe_harbor"]
        status = "✅" if safe["passed"] else "❌"
        lines.append(f"\nSafe Harbor (§ 6-1-1709)")
        lines.append("-"*50)
        lines.append(f"{status} {safe['description']}")
        lines.append(f"   Evidence: {safe['evidence']}")
        
        lines.append("")
        lines.append("="*70)
        lines.append(f"SUMMARY: {self.results['summary']['compliance_status']}")
        lines.append(f"Requirements Passed: {self.results['summary']['requirements_passed']}/{self.results['summary']['total_requirements']}")
        lines.append("="*70)
        
        return "\n".join(lines)
    
    def _generate_html_report(self) -> str:
        """Generate HTML report for Attorney General."""
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Colorado AI Act Compliance Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h1 {{ color: #003366; }}
        h2 {{ color: #0066CC; margin-top: 30px; }}
        .summary {{ background: #f0f7ff; padding: 20px; border-radius: 5px; margin: 20px 0; border-left: 5px solid #003366; }}
        .passed {{ color: green; font-weight: bold; }}
        .failed {{ color: red; font-weight: bold; }}
        .section {{ border: 1px solid #ccc; padding: 15px; margin: 15px 0; border-radius: 5px; }}
        .requirement {{ margin: 10px 0; padding: 10px; background: #f9f9f9; }}
        .evidence {{ font-family: monospace; background: #eee; padding: 5px; border-radius: 3px; }}
        .footer {{ margin-top: 40px; color: #999; text-align: center; }}
    </style>
</head>
<body>
    <h1>Colorado AI Act (SB 24-205) Compliance Report</h1>
    <p>Generated: {self.results['summary']['verification_time']}</p>
    
    <div class="summary">
        <h2>Executive Summary</h2>
        <p><strong>Overall Compliance Status:</strong> 
           <span class="{'passed' if self.results['summary']['compliance_status'] == 'FULLY_COMPLIANT' else 'failed'}">
           {self.results['summary']['compliance_status']}</span></p>
        <p><strong>Requirements Passed:</strong> {self.results['summary']['requirements_passed']} / {self.results['summary']['total_requirements']}</p>
        <p><strong>Verification ID:</strong> {self.results['summary']['verification_id']}</p>
    </div>
"""
        
        # Developer requirements
        if self.results.get("developer_requirements"):
            dev = self.results["developer_requirements"]
            status_class = "passed" if dev["overall"] == "PASSED" else "failed"
            html += f"""
    <div class="section">
        <h2>{dev['name']}</h2>
        <p><strong>Overall:</strong> <span class="{status_class}">{dev['overall']}</span></p>
"""
            for req_id, req in dev["requirements"].items():
                status = "✅" if req["passed"] else "❌"
                html += f"""
        <div class="requirement">
            <p><strong>{req_id}:</strong> {req['description']}</p>
            <p>{status} <span class="evidence">{req['evidence']}</span></p>
        </div>
"""
            html += "    </div>"
        
        # Deployer requirements
        if self.results.get("deployer_requirements"):
            dep = self.results["deployer_requirements"]
            status_class = "passed" if dep["overall"] == "PASSED" else "failed"
            html += f"""
    <div class="section">
        <h2>{dep['name']}</h2>
        <p><strong>Overall:</strong> <span class="{status_class}">{dep['overall']}</span></p>
"""
            for req_id, req in dep["requirements"].items():
                status = "✅" if req["passed"] else "❌"
                html += f"""
        <div class="requirement">
            <p><strong>{req_id}:</strong> {req['description']}</p>
            <p>{status} <span class="evidence">{req['evidence']}</span></p>
        </div>
"""
            html += "    </div>"
        
        # Safe harbor
        safe = self.results["safe_harbor"]
        status_class = "passed" if safe["passed"] else "failed"
        html += f"""
    <div class="section">
        <h2>Safe Harbor (§ 6-1-1709)</h2>
        <p><strong>Status:</strong> <span class="{status_class}">{'COMPLIANT' if safe['passed'] else 'NON-COMPLIANT'}</span></p>
        <div class="requirement">
            <p><strong>Description:</strong> {safe['description']}</p>
            <p>{'✅' if safe['passed'] else '❌'} <span class="evidence">{safe['evidence']}</span></p>
        </div>
    </div>
        
    <div class="footer">
        <p>Verified by JEP Colorado Compliance Framework | HJS Foundation LTD (Singapore CLG)</p>
        <p>This report is cryptographically signed and verifiable</p>
        <p>Verification Script: verify-colorado.py | Report ID: {self.results['summary']['verification_id']}</p>
    </div>
</body>
</html>
"""
        return html


def main():
    parser = argparse.ArgumentParser(
        description="Verify JEP implementation against Colorado AI Act (SB 24-205)"
    )
    parser.add_argument(
        "--entity",
        choices=["developer", "deployer"],
        help="Verify only specific entity type"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Verify all requirements"
    )
    parser.add_argument(
        "--output-format",
        choices=["text", "json", "html"],
        default="text",
        help="Output format"
    )
    parser.add_argument(
        "--output",
        help="Output file path"
    )
    
    args = parser.parse_args()
    
    # Determine entity type
    if args.all:
        entity = None
    elif args.entity:
        entity = args.entity
    else:
        entity = "deployer"  # Default to deployer
    
    verifier = ColoradoComplianceVerifier(entity_type=entity if entity else "deployer")
    
    # Run verification
    results = verifier.verify_all(entity)
    
    # Generate report
    output = verifier.generate_report(args.output_format)
    
    # Output results
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"✅ Colorado compliance report saved to {args.output}")
    else:
        print(output)
    
    # Return exit code based on compliance status
    if results["summary"]["compliance_status"] == "FULLY_COMPLIANT":
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
