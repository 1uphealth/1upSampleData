import json
import glob

HTEST_LABEL = {
    'system': 'http://hl7.org/fhir/v3/ActReason',
    'code': 'HTEST',
    'display': 'test health data'
}

def isBundle(resourceType):
    return resourceType == 'Bundle'

def existingMetaTag(resource):
    return 'meta' in resource

def existingSecurityLabel(meta):
    return 'security' in meta

def existingTestPatientLabel(metaSecurity):
    return any(label['code'] == 'HTEST' for label in metaSecurity) 

for filename in glob.glob('../**/*.json', recursive=True):
    resource = json.load(
        open(filename, 'r'))
    if isBundle(resource['resourceType']):
        for entry in resource['entry']:
            if existingMetaTag(entry['resource']):
                if existingSecurityLabel(entry['resource']['meta']):
                    if not existingTestPatientLabel(entry['resource']['meta']['security']):
                        entry['resource']['meta']['security'].append(HTEST_LABEL)
                else:
                    entry['resource']['meta']['security'] = [HTEST_LABEL]
            else:
                entry['resource']['meta'] = {'security': [HTEST_LABEL]}
    else:
        if existingMetaTag(resource):
            if existingSecurityLabel(resource['meta']):
                if not existingTestPatientLabel(resource['meta']['security']):
                        resource['meta']['security'].append(HTEST_LABEL)
            else:
                resource['meta']['security'] = [HTEST_LABEL]
        else:
            resource['meta'] = {'security': [HTEST_LABEL]}
    with open(filename, 'w') as filename:
        json.dump(resource, filename, indent=4)
