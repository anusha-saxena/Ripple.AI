
from pymongo import MongoClient
MONGODB_URI = "mongodb+srv://anusha06:Akshat12!@cluster0.8ibtd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGODB_URI)
db = client["policy_database"]
collection = db["treaties"]
treaties = [
    {
    "title": "The Safe Drinking Water for First Nations Act",
    "text": "This act was introduced to establish regulations for water quality and sanitation in First Nations communities. It mandates the federal government to ensure safe drinking water infrastructure and maintenance.",
    "category": "Clean drinking water access",
    "date_signed": "2013-06-19",
    "location": "All First Nations communities in Canada",
    "government_commitment": "Ensure all First Nations communities have access to safe drinking water by setting enforceable standards.",
    "status": "pending"
  },
  {
    "title": "Treaty No. 6",
    "text": "An agreement between the Canadian Crown and various First Nations, which includes provisions for healthcare and water access.",
    "category": "Water rights",
    "date_signed": "1876-08-23",
    "location": "Alberta, Saskatchewan, and Manitoba",
    "government_commitment": "Provide clean water and healthcare to Indigenous communities.",
    "status": "unfulfilled"
  },
  {
    "title": "United Nations Declaration on the Rights of Indigenous Peoples (UNDRIP) - Canadian Adoption",
    "text": "Canada adopted UNDRIP, which recognizes the rights of Indigenous peoples to maintain access to clean water and sanitation as part of their inherent rights.",
    "category": "Legal framework for Indigenous water rights",
    "date_signed": "2021-06-21",
    "location": "All Indigenous communities in Canada",
    "government_commitment": "Align Canadian laws with UNDRIP, ensuring Indigenous communities have equal access to clean water.",
    "status": "pending"
  },
  {
    "title": "First Nations Water Management Strategy",
    "text": "A government initiative aimed at improving water infrastructure in First Nations communities, launched in partnership with Indigenous Services Canada.",
    "category": "Water infrastructure",
    "date_signed": "2001-03-15",
    "location": "All First Nations communities in Canada",
    "government_commitment": "Invest in new water treatment plants, upgrade existing infrastructure, and provide ongoing maintenance support.",
    "status": "pending"
  },
  {
    "title": "Jordan’s Principle",
    "text": "A legal rule ensuring that First Nations children receive government services without delay, including access to clean drinking water.",
    "category": "Children's rights and water access",
    "date_signed": "2007-12-12",
    "location": "All First Nations communities in Canada",
    "government_commitment": "Ensure First Nations children have immediate access to clean drinking water and essential services.",
    "status": "pending"
  },
  {
    "title": "Federal Budget 2021 - First Nations Water Infrastructure Commitment",
    "text": "The Canadian federal budget in 2021 included $1.5 billion in funding to eliminate all long-term drinking water advisories in First Nations communities.",
    "category": "Government funding for water access",
    "date_signed": "2021-04-19",
    "location": "First Nations communities with long-term water advisories",
    "government_commitment": "End all long-term drinking water advisories and improve water infrastructure in Indigenous communities.",
    "status": "pending"
  },
  {
    "title": "The Indian Act - Water Governance",
    "text": "The Indian Act provides some legal governance structures for reserve lands, including water management responsibilities of the federal government.",
    "category": "Legal framework for Indigenous governance",
    "date_signed": "1876-04-12",
    "location": "All Indigenous communities in Canada",
    "government_commitment": "Ensure the federal government remains responsible for water management on reserves.",
    "status": "ongoing"
  },
  {
    "title": "The First Nations Clean Water Initiative",
    "text": "A targeted initiative to improve access to clean water through collaboration with Indigenous communities and government agencies.",
    "category": "Water infrastructure improvements",
    "date_signed": "2016-11-01",
    "location": "First Nations communities across Canada",
    "government_commitment": "Accelerate investments in clean drinking water and sanitation projects for Indigenous communities.",
    "status": "pending",
  },
  {
    "title": "Treaty No. 8",
    "text": "A historical treaty signed between the Crown and various First Nations, which included provisions for land, healthcare, and water rights.",
    "category": "Water rights",
    "date_signed": "1899-06-21",
    "location": "Alberta, British Columbia, Saskatchewan, and Northwest Territories",
    "government_commitment": "Ensure Indigenous communities under this treaty have access to clean water and necessary resources.",
    "status": "unfulfilled"
  },
  {
    "title": "The First Nations Water and Wastewater Action Plan (FNWWAP)",
    "text": "A government program to improve water and wastewater infrastructure in First Nations communities.",
    "category": "Water infrastructure improvements",
    "date_signed": "2008-04-01",
    "location": "First Nations communities across Canada",
    "government_commitment": "Provide funding and support for water treatment facilities, wastewater management, and training for Indigenous water operators.",
    "status": "ongoing"
  },
  {
    "title": "The First Nations Drinking Water Settlement",
    "text": "A legal settlement providing compensation and commitments to fixing long-term drinking water advisories in First Nations communities.",
    "category": "Legal settlement for water rights",
    "date_signed": "2021-12-31",
    "location": "Affected First Nations communities across Canada",
    "government_commitment": "Provide financial compensation and long-term solutions for clean drinking water in affected communities.",
    "status": "ongoing"
  }
  

]

collection.insert_many(treaties)
