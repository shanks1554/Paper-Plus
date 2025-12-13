from pathlib import Path
from tqdm import tqdm

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from RAG_system.config import DATA_ROOT, INDEX_ROOT
from RAG_system.embeddings import get_embedding_model

def load_domain_documents(domain_path: Path):
    documents = []

    for pdf_file in domain_path.glob("*.pdf"):
        loader = PyPDFLoader(str(pdf_file))
        pages = loader.load()

        for page in pages:
            page.metadata["domain"] = domain_path.name
            page.metadata["source"] = pdf_file.name

        documents.extend(pages)

    return documents

def build_all_indexes():
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    embedding_model = get_embedding_model()
    domains = [d for d in DATA_ROOT.iterdir() if d.is_dir()]

    for domain_path in tqdm(domains):
        print(f"\nIndexing domain: {domain_path.name}")

        docs = load_domain_documents(domain_path)
        if not docs:
            print("No documents found, skipping.")
            continue

        chunks = splitter.split_documents(docs)

        index_path = INDEX_ROOT / domain_path.name.lower().replace(" ", "_")
        index_path.mkdir(parents=True, exist_ok=True)

        FAISS.from_documents(chunks, embedding_model).save_local(index_path)

    print("\nAll vector databases created successfully.")
