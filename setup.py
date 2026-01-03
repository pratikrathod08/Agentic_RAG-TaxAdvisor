from setuptools import setup, find_packages

requirements_list = []

with open("requirements.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("-"):
            requirements_list.append(line)

setup(
    name="agentic-rag",
    version="0.0.1",
    description="Agentic RAG project for demonstration",
    author="Pratik Rathod",
    author_email="pratikr1521998@gmail.com",
    packages=find_packages(),
    install_requires=requirements_list,
    python_requires=">=3.9"
)
