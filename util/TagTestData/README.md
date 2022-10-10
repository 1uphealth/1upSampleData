## Tag test data script
This script will iterate through all resource instances in each .json file in this repo and add a test security label(unless one already exists) to indicate that the resource is test data.  
See [Security Labels](https://www.hl7.org/fhir/security-labels.html) and [How to mark test resources](https://www.hl7.org/fhir/security-labels.html) for more info on security labels and marking test data.  

This script can be run after new sample data is added to the repo to ensure the data is marked as test data.

To run, cd into the util directory and run the following:

```
python3 tag_test_data.py
```

