# 1upSampleData - PUBLIC repository of sample data

This is just a repository to put sample data for different purposes
The structure will evolve.  For now, simply place new sample data in
a well named directory.  The data can be JSON bundles or ndjson files.

**This contain only synthetic test data, not real data or any company sensitive content**

* uscore 
  - A collection of individual patient bundles with resources (500-2000 in each patient bundle) that comply with USCDI profiles.

* carin 
  - A collection of 6 individual patient bundles with resources (200-400 in each patient bundle) that comply with CARIN Blue Button ID profiles.
  - The Touchstone data set passes the validation in their _/FHIRSandbox/CARIN/CARIN-4-BlueButton_ suite.

* pdex
  - PlanNet - Touchstone data set passes 80% of the the validation in their _/FHIRSandbox/DaVinci/FHIR4-0-1-Test/PDEX/PlanNet_ suite.
  (tbd to confirm in a new environment like 1up-stage)
