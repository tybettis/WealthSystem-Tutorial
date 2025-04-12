class CPALegalTeam:
    def __init__(self, firm_name, lead_contact):
        self.firm_name = firm_name
        self.lead_contact = lead_contact
        self.compliance_reports = []

    def generate_report(self, report_name, entities):
        report = {
            "name": report_name,
            "entities_reviewed": entities,
            "status": "Compliant"
        }
        self.compliance_reports.append(report)
        return report

    def list_reports(self):
        return self.compliance_reports