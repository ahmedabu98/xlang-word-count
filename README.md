# Beam Cross-language WordCount 
This project provides an example of a SchemaTransform use-case with Java's WordCount transform.

Setup needed:

- Python virtual environment for Beam. See [Python quickstart](https://beam.apache.org/get-started/quickstart-py/)
for more information.

Steps:
- Build the project:

`./gradlew build`

- Run the expansion service:

`./gradlew runExpansionService`

- While the expansion service is running, run the Python pipeline in a separate terminal:

`python xlang_wordcount.py`