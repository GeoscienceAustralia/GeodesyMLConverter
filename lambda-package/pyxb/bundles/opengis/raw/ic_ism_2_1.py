# ./pyxb/bundles/opengis/raw/ic_ism_2_1.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:6a2dbc65b53dd34df1735f2f95a5cdb99288cc6f
# Generated 2017-07-10 00:37:00.066461 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace urn:us:gov:ic:ism:v2

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:e2aac426-6507-11e7-8080-0a55f9edafa5')

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
Namespace = pyxb.namespace.NamespaceForURI('urn:us:gov:ic:ism:v2', create_if_missing=True)
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


# Atomic simple type: {urn:us:gov:ic:ism:v2}ClassificationType
class ClassificationType (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """
        This simple type is used by the classification attribute to identify the highest level of classification of the information being encoded. It is manifested in portion marks and security banners.

        PERMISSIBLE VALUES

        The permissible values for this simple type are defined in the Implementation Profile Supplement: Value Enumerations in the value sets:

         US Classification Markings - Authorized Portion Markings
         NATO Classification Markings - Authorized Portion Markings

      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClassificationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 119, 2)
    _Documentation = '\n        This simple type is used by the classification attribute to identify the highest level of classification of the information being encoded. It is manifested in portion marks and security banners.\n\n        PERMISSIBLE VALUES\n\n        The permissible values for this simple type are defined in the Implementation Profile Supplement: Value Enumerations in the value sets:\n\n         US Classification Markings - Authorized Portion Markings\n         NATO Classification Markings - Authorized Portion Markings\n\n      '
ClassificationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ClassificationType, enum_prefix=None)
ClassificationType.U = ClassificationType._CF_enumeration.addEnumeration(unicode_value='U', tag='U')
ClassificationType.C = ClassificationType._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
ClassificationType.S = ClassificationType._CF_enumeration.addEnumeration(unicode_value='S', tag='S')
ClassificationType.TS = ClassificationType._CF_enumeration.addEnumeration(unicode_value='TS', tag='TS')
ClassificationType.R = ClassificationType._CF_enumeration.addEnumeration(unicode_value='R', tag='R')
ClassificationType.CTS = ClassificationType._CF_enumeration.addEnumeration(unicode_value='CTS', tag='CTS')
ClassificationType.CTS_B = ClassificationType._CF_enumeration.addEnumeration(unicode_value='CTS-B', tag='CTS_B')
ClassificationType.CTS_BALK = ClassificationType._CF_enumeration.addEnumeration(unicode_value='CTS-BALK', tag='CTS_BALK')
ClassificationType.NU = ClassificationType._CF_enumeration.addEnumeration(unicode_value='NU', tag='NU')
ClassificationType.NR = ClassificationType._CF_enumeration.addEnumeration(unicode_value='NR', tag='NR')
ClassificationType.NC = ClassificationType._CF_enumeration.addEnumeration(unicode_value='NC', tag='NC')
ClassificationType.NS = ClassificationType._CF_enumeration.addEnumeration(unicode_value='NS', tag='NS')
ClassificationType.NS_S = ClassificationType._CF_enumeration.addEnumeration(unicode_value='NS-S', tag='NS_S')
ClassificationType.NS_A = ClassificationType._CF_enumeration.addEnumeration(unicode_value='NS-A', tag='NS_A')
ClassificationType.CTSA = ClassificationType._CF_enumeration.addEnumeration(unicode_value='CTSA', tag='CTSA')
ClassificationType.NSAT = ClassificationType._CF_enumeration.addEnumeration(unicode_value='NSAT', tag='NSAT')
ClassificationType.NCA = ClassificationType._CF_enumeration.addEnumeration(unicode_value='NCA', tag='NCA')
ClassificationType._InitializeFacetMap(ClassificationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ClassificationType', ClassificationType)
_module_typeBindings.ClassificationType = ClassificationType

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.NMTOKENS
class STD_ANON (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.NMTOKEN."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 278, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.NMTOKEN
STD_ANON._InitializeFacetMap()
_module_typeBindings.STD_ANON = STD_ANON

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.NMTOKENS
class STD_ANON_ (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.NMTOKEN."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 305, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.NMTOKEN
STD_ANON_._InitializeFacetMap()
_module_typeBindings.STD_ANON_ = STD_ANON_

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.NMTOKENS
class STD_ANON_2 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.NMTOKEN."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 330, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.NMTOKEN
STD_ANON_2._InitializeFacetMap()
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.NMTOKENS
class STD_ANON_3 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.NMTOKEN."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 355, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.NMTOKEN
STD_ANON_3._InitializeFacetMap()
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.NMTOKENS
class STD_ANON_4 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.NMTOKEN."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 385, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.NMTOKEN
STD_ANON_4._InitializeFacetMap()
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.NMTOKENS
class STD_ANON_5 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.NMTOKEN."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 421, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.NMTOKEN
STD_ANON_5._InitializeFacetMap()
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.NMTOKENS
class STD_ANON_6 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.NMTOKEN."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 447, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.NMTOKEN
STD_ANON_6._InitializeFacetMap()
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.NMTOKENS
class STD_ANON_7 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.NMTOKEN."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 475, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.NMTOKEN
STD_ANON_7._InitializeFacetMap()
_module_typeBindings.STD_ANON_7 = STD_ANON_7

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 494, 4)
    _Documentation = None
STD_ANON_8._InitializeFacetMap()
_module_typeBindings.STD_ANON_8 = STD_ANON_8

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 515, 4)
    _Documentation = None
STD_ANON_9._InitializeFacetMap()
_module_typeBindings.STD_ANON_9 = STD_ANON_9

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 534, 4)
    _Documentation = None
STD_ANON_10._InitializeFacetMap()
_module_typeBindings.STD_ANON_10 = STD_ANON_10

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 553, 4)
    _Documentation = None
STD_ANON_11._InitializeFacetMap()
_module_typeBindings.STD_ANON_11 = STD_ANON_11

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.date):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 572, 4)
    _Documentation = None
STD_ANON_12._InitializeFacetMap()
_module_typeBindings.STD_ANON_12 = STD_ANON_12

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 591, 4)
    _Documentation = None
STD_ANON_13._InitializeFacetMap()
_module_typeBindings.STD_ANON_13 = STD_ANON_13

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.NMTOKENS
class STD_ANON_14 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.NMTOKEN."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 618, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.NMTOKEN
STD_ANON_14._InitializeFacetMap()
_module_typeBindings.STD_ANON_14 = STD_ANON_14

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.NMTOKENS
class STD_ANON_15 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.NMTOKEN."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 646, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.NMTOKEN
STD_ANON_15._InitializeFacetMap()
_module_typeBindings.STD_ANON_15 = STD_ANON_15

# Atomic simple type: [anonymous]
class STD_ANON_16 (pyxb.binding.datatypes.date):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 665, 4)
    _Documentation = None
STD_ANON_16._InitializeFacetMap()
_module_typeBindings.STD_ANON_16 = STD_ANON_16

# Atomic simple type: [anonymous]
class STD_ANON_17 (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ic/2.1/IC-ISM-v2.1.xsd', 685, 4)
    _Documentation = None
STD_ANON_17._InitializeFacetMap()
_module_typeBindings.STD_ANON_17 = STD_ANON_17
