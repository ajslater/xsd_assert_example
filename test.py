#!/usr/bin/env python3


import xmlschema
schema = xmlschema.XMLSchema11('ids.xsd')

def main():
    print("This should pass:", flush=True)
    schema.validate("ids_pass.xml")

    print("This should fail:", flush=True)
    schema.validate("ids_fail.xml")


if __name__ == "__main__":
    main()
