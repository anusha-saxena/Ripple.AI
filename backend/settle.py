
from pymongo import MongoClient
MONGODB_URI = "mongodb+srv://anusha06:Akshat12!@cluster0.8ibtd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGODB_URI)
db = client["policy_database"]
collection = db["settlements"]
settlements = [ 
    {
    "title": "Treaty No. 6 - Water Commitments",
    "treaty_commitment": "Provide clean water and healthcare to Indigenous communities.",
    "policy_reference": "Treaty No. 6 (1876)",
    "government_action": "Multiple long-term drinking water advisories remain in Treaty 6 territories.",
    "status": "Unfulfilled",
    "verification_source": "Indigenous Services Canada - Drinking Water Advisories Report (2024)",
    "last_updated": "2024-11-22"
  },
  {
    "title": "Safe Drinking Water for First Nations Act",
    "treaty_commitment": "Establish enforceable water quality standards for First Nations.",
    "policy_reference": "Safe Drinking Water for First Nations Act (2013)",
    "government_action": "Legislation passed but lacking adequate funding and implementation.",
    "status": "Partially Fulfilled",
    "verification_source": "Office of the Auditor General of Canada Report (2021)",
    "last_updated": "2024-11-22"
  },
  {
    "title": "Federal Budget 2021 - First Nations Water Infrastructure Commitment",
    "treaty_commitment": "End all long-term drinking water advisories and improve water infrastructure.",
    "policy_reference": "Federal Budget 2021 Commitment",
    "government_action": "As of 2024, 147 long-term advisories lifted, but 31 remain.",
    "status": "Partially Fulfilled",
    "verification_source": "Indigenous Services Canada - November 2024 Advisory Update",
    "last_updated": "2024-11-22"
  },
  {
    "title": "First Nations Drinking Water Settlement",
    "treaty_commitment": "Provide financial compensation and long-term solutions for clean water.",
    "policy_reference": "Legal Settlement (2021)",
    "government_action": "Compensation delivered to some affected communities, but delays persist in infrastructure improvements.",
    "status": "Ongoing",
    "verification_source": "Human Rights Watch - ‘Make It Safe’ Report (2024)",
    "last_updated": "2024-11-22"
  },
  {
    "title": "Bill C-61: First Nations Clean Water Act",
    "treaty_commitment": "Ensure long-term access to clean drinking water for First Nations.",
    "policy_reference": "Proposed Legislation (2023)",
    "government_action": "Bill introduced but not yet passed into law.",
    "status": "Pending",
    "verification_source": "Government of Canada - Bill C-61 Legislative Status",
    "last_updated": "2024-11-22"
  }
]

collection.insert_many(settlements)
