from setuptools import setup, find_packages

lst_requirements = []

with open("requirement.txt", "r") as f: 
    for line in f.read(): 
        if line and line.startswith("-"):
            continue 
        lst_requirements.append(line)

setup(
    name="agentic_rag_demo", 
    version="0.0.1", 
    author="Pratik Rathod", 
    author_email="pratikr1521998@gmail.com", 
    packages=find_packages(), 
    required_installs=lst_requirements, 
    python_required=">=3.9"
)