from pyspark import pipelines as dl

@dl.table
def transformed():
    return spark.range(10)