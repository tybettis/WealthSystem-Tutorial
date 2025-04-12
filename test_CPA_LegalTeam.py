from CPA_LegalTeam import CPALegalTeam

# Create team instance
team = CPALegalTeam("Legacy Compliance LLC", "Sarah Thompson")

# Simulate reviewing entities
entities = ["Tyson Wealth Holdings", "Tyson Legacy Trust", "IP Holdings"]

# Generate a compliance report
report = team.generate_report("Q2 Trust Audit", entities)

# Output the results
print("CPA Firm:", team.firm_name)
print("Lead Contact:", team.lead_contact)
print("Report Generated:", report)
print("All Reports:", team.list_reports())