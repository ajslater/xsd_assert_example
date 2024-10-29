#!/usr/bin/env python3


import xmlschema
schema = xmlschema.XMLSchema11('ids.xsd')

def main():
    schema.validate("ids.xml")


if __name__ == "__main__":
    main()
