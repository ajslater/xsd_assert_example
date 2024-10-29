#!/usr/bin/env python3
"""Run validation on an xsd:assert example."""
from pprint import pprint
from xmlschema import XMLSchema11


def test(schema, xml_fn):
    """Validate and parse one xml file."""
    schema.validate(xml_fn)
    pprint(schema.to_dict(xml_fn))

def main():
    """Run all tests."""
    schema = XMLSchema11('ids.xsd')
    print("This should pass:")
    test(schema, "ids_pass.xml")
    print()
    print("This should fail:")
    test(schema, "ids_fail.xml")


if __name__ == "__main__":
    main()
