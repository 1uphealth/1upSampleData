# Tag test data script
This script will loop through all resource instances in each file in this repo and add a test security label(unless one already exists) to indicate that the resource is test data.  
See [Security Labels](https://www.hl7.org/fhir/security-labels.html) and [How to mark test resources](https://www.hl7.org/fhir/security-labels.html) for more info on security labels and marking test data.  

This script should be run after new sample data is added to the repo to ensure that all data is taggged appropriately.

To run, cd into util/ and run

```
python3 tag_test_data.py
```

