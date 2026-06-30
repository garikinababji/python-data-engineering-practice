=============================================
# Topic:  validator
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
=============================================



# Real-Time GCP Example  Imagine Customer Validator

class CustomerValidator:


    def validate(self, customer):

        if customer["status"] == "Active":
            return True

        return False
    

# Production ETL projects లో ఇలాంటి classes ఉంటాయి.

# Another Example

class BigQueryLoader:

    def load(self):

        print("Loading data into BigQuery")
