import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

class JSONFormat:
    def format_data(self, data):
        return json.dumps(data, indent=2)

class XMLFormat:
    def format_data(self, data):
        root = ET.Element("WeatherData")
        for key, value in data.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        xml_str = ET.tostring(root, encoding="utf-8")
        parsed_xml = minidom.parseString(xml_str)
        return parsed_xml.toprettyxml(indent="  ")
