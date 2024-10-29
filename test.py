#!/usr/bin/env python3
"""Run validation on an xsd:assert example."""

import xmlschema

def main():
    schema = xmlschema.XMLSchema11('ids.xsd')

    print("This should pass:", flush=True)
    schema.validate("ids_pass.xml")

    print("This should fail:", flush=True)
    schema.validate("ids_fail.xml")


if __name__ == "__main__":
    main()
