

__author__ = 'schwa'

import Foundation
import PyObjCTools.Conversion
import json
import sys
import subprocess
import os

import StringIO
import pyaml
import difflib
import glob
import yaml
import json

########################################################################################################################

# Utilities

def listify(o):
    if isinstance(o, basestring):
        return [o]
    elif not o:
        return []
    else:
        return sorted(o)

def type_diff(a, b):
    s = StringIO.StringIO()
    pyaml.dump(a, s, safe = True)
    a = s.getvalue().splitlines()
    s = StringIO.StringIO()
    pyaml.dump(b, s, safe = True)
    b = s.getvalue().splitlines()
    return '\n'.join(difflib.Differ().compare(a, b))

def normalize_type(t):
    t = json.loads(json.dumps(PyObjCTools.Conversion.pythonCollectionFromPropertyList(t))) # Dont ask
    if 'UTTypeConformsTo' in t:
        t['UTTypeConformsTo'] = listify(t['UTTypeConformsTo'])
    if 'UTTypeTagSpecification' in t:
        all_tags = t['UTTypeTagSpecification']
        for tag_type, tags in all_tags.items():
            all_tags[tag_type] = listify(tags)
    return t

########################################################################################################################

all_types = {}


s = subprocess.check_output(['locate', 'Info.plist'])
s = s.splitlines()
for path in s:
    if os.path.split(path)[1] != 'Info.plist':
        continue
    if 'iPhoneSimulator.platform' in path:
        continue
    thePlist = Foundation.NSDictionary.dictionaryWithContentsOfFile_(path)
    if not thePlist:
        print("Could not parse plist: ", path)
        continue

    if 'UTExportedTypeDeclarations' not in thePlist and  'UTImportedTypeDeclarations' not in thePlist:
        continue

    if not 'CFBundleIdentifier' in thePlist:
        print("No bundle identifier in plist: ", path)
        continue
    if not 'CFBundleVersion' in thePlist:
        print("No bundle versionin plist: ", path)
        continue

    source = '%s:%s' % (thePlist['CFBundleIdentifier'], thePlist['CFBundleVersion'])

    if 'UTExportedTypeDeclarations' in thePlist:
        theTypes = thePlist['UTExportedTypeDeclarations']
        for t in theTypes:
            t = normalize_type(t)
            identifier = t['UTTypeIdentifier']
            if identifier not in all_types:
                all_types[identifier] = []
            all_types[identifier].append((source + '/Exported', t))
    if 'UTImportedTypeDeclarations' in thePlist:
        theTypes = thePlist['UTImportedTypeDeclarations']
        for t in theTypes:
            t = normalize_type(t)
            if 'UTTypeIdentifier' not in t:
                print 'No UTI type:', path,
                continue
            identifier = t['UTTypeIdentifier']
            if identifier not in all_types:
                all_types[identifier] = []
            all_types[identifier].append((source + '/Imported', t))


for types in all_types.values():
    if len(types) == 1:
        pass
    t = types[0][1]
    theOutputPath = os.path.join('..', 'Types', t['UTTypeIdentifier'] + '.yaml')
    if not os.path.exists(theOutputPath):
        pyaml.dump(t, file(theOutputPath, 'w'), safe = True)

types = {}
for path in glob.glob('../Types/*.yaml'):
    t = yaml.load(file(path))
    types[t['UTTypeIdentifier']] = t

for identifier, t in types.items():
    if 'UTTypeConformsTo' in t:
        for conforms_to in t['UTTypeConformsTo']:
            if conforms_to not in types:
                print identifier
                print('"{}"'.format(conforms_to))
                continue

            if 'UTTypeConformedBy' not in types[conforms_to]:
                types[conforms_to]['UTTypeConformedBy'] = []
            types[conforms_to]['UTTypeConformedBy'].append(identifier)

pyaml.dump(types, file('processed.yaml', 'w'))

json.dump(types, file('processed.json', 'w'))
