import arxiv
import requests
from xml.etree import ElementTree as ET

# Function to process arXiv data
def process_arxiv(arxiv_results):
    print("### arXiv Papers ###")
    for result in arxiv_results:
        print(f"Title: {result.title}")
        print(f"Authors: {', '.join(author.name for author in result.authors)}")
        print(f"Published: {result.published}")
        print("Summary:")
        print(result.summary)
        print("-" * 50)

# Function to process PubMed XML
def process_pubmed(pubmed_xml):
    print("### PubMed Papers ###")
    root = ET.fromstring(pubmed_xml)
    for article in root.findall(".//PubmedArticle"):
        title = article.findtext(".//ArticleTitle")
        authors = []
        for author in article.findall(".//Author"):
            last_name = author.findtext("LastName")
            fore_name = author.findtext("ForeName")
            if last_name and fore_name:
                authors.append(f"{fore_name} {last_name}")
        journal = article.findtext(".//Title")
        publication_date = article.findtext(".//PubDate/Year")
        doi = article.findtext(".//ELocationID[@EIdType='doi']")
        abstract = article.findtext(".//AbstractText")

        # Display the results
        print(f"Title: {title}")
        print(f"Authors: {', '.join(authors)}")
        print(f"Journal: {journal}")
        print(f"Published: {publication_date}")
        print(f"DOI: {doi}")
        print("Abstract:")
        print(abstract)
        print("-" * 50)

# Fetch data from arXiv
print("Fetching arXiv data...")
search = arxiv.Search(
    query="machine learning",
    max_results=2,
    sort_by=arxiv.SortCriterion.Relevance
)

arxiv_results = list(search.results())
process_arxiv(arxiv_results)

# Fetch data from PubMed
print("Fetching PubMed data...")
base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
ids = "39580609,39580589,39580531"  # Example IDs
params = {
    "db": "pubmed",
    "id": ids,
    "retmode": "xml"
}

response = requests.get(base_url, params=params)
if response.status_code == 200:
    process_pubmed(response.text)
else:
    print(f"Error fetching PubMed data: {response.status_code}")