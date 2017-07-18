# ./pyxb/bundles/opengis/raw/gmlsf.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ffd885422e381c03fb347f9c1941318d96f0b846
# Generated 2017-07-10 00:37:28.732285 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/gmlsf

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:f3c4e066-6507-11e7-945e-0a55f9edafa5')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/gmlsf', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.integer, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/profiles/gmlsfProfile/1.0.0/gmlsfLevels.xsd', 31, 6)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='0', tag=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='2', tag=None)
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

GMLProfileSchema = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GMLProfileSchema'), pyxb.binding.datatypes.anyURI, documentation='\n            This URI references the profile schema to which a GML\n            application schema conforms.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/profiles/gmlsfProfile/1.0.0/gmlsfLevels.xsd', 40, 3))
Namespace.addCategoryObject('elementBinding', GMLProfileSchema.name().localName(), GMLProfileSchema)

ComplianceLevel = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ComplianceLevel'), STD_ANON, documentation='\n            Level 0 = no complex-valued properties and minOccurs,maxOccurs\n                      have a value domain of 0 or 1\n            Level 1 = complex-valued properties with no restriction on\n                      minOccurs and maxOccurs\n            Level 2 = no restrictions on type of non-spatial scalar properties \n                      but must only support spatial properties declared in\n                      clause 8\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/profiles/gmlsfProfile/1.0.0/gmlsfLevels.xsd', 19, 3))
Namespace.addCategoryObject('elementBinding', ComplianceLevel.name().localName(), ComplianceLevel)
