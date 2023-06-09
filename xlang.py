import apache_beam as beam
from apache_beam.transforms.external import SchemaAwareExternalTransform

with beam.Pipeline() as p:
  _ = (
      p
      | SchemaAwareExternalTransform(
          identifier="beam:schematransform:org.apache.beam:wordcount:v1",
          expansion_service="localhost:8099",
          inputFile="gs://apache-beam-samples/shakespeare/kinglear.txt")
      | beam.Map(lambda row: row.wordCount)
      | beam.io.WriteToText(file_path_prefix="wordcounts"))
