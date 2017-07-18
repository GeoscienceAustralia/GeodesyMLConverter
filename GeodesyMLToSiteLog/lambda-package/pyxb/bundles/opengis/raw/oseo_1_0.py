# ./pyxb/bundles/opengis/raw/oseo_1_0.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:9f0a1f4261996e90274543ada2e4394f480b8d14
# Generated 2017-07-10 00:37:58.105949 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/oseo/1.0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:036459de-6508-11e7-ad42-0a55f9edafa5')

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
import pyxb.bundles.opengis.ows_2_0
import pyxb.bundles.opengis.swe_2_0
import pyxb.bundles.opengis.swes_2_0

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/oseo/1.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ows = pyxb.bundles.opengis.ows_2_0.Namespace
_Namespace_ows.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_swe = pyxb.bundles.opengis.swe_2_0.Namespace
_Namespace_swe.configureCategories(['typeBinding', 'elementBinding'])

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
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 87, 2)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.None_ = STD_ANON._CF_enumeration.addEnumeration(unicode_value='None', tag='None_')
STD_ANON.Final = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Final', tag='Final')
STD_ANON.All = STD_ANON._CF_enumeration.addEnumeration(unicode_value='All', tag='All')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 96, 2)
    _Documentation = None
STD_ANON_._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
STD_ANON_._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_maxLength,
   STD_ANON_._CF_minLength)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 119, 3)
    _Documentation = None
STD_ANON_2._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(5))
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_maxLength)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 136, 4)
    _Documentation = None
STD_ANON_3._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_maxLength)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: {http://www.opengis.net/oseo/1.0}SWEEncoding
class SWEEncoding (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SWEEncoding')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 256, 1)
    _Documentation = None
SWEEncoding._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SWEEncoding, enum_prefix=None)
SWEEncoding.XMLEncoding = SWEEncoding._CF_enumeration.addEnumeration(unicode_value='XMLEncoding', tag='XMLEncoding')
SWEEncoding.TextEncoding = SWEEncoding._CF_enumeration.addEnumeration(unicode_value='TextEncoding', tag='TextEncoding')
SWEEncoding._InitializeFacetMap(SWEEncoding._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SWEEncoding', SWEEncoding)
_module_typeBindings.SWEEncoding = SWEEncoding

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 306, 4)
    _Documentation = None
STD_ANON_4._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_4._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_maxLength,
   STD_ANON_4._CF_minLength)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 347, 5)
    _Documentation = None
STD_ANON_5._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_5._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_maxLength,
   STD_ANON_5._CF_minLength)
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 358, 5)
    _Documentation = None
STD_ANON_6._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_maxLength)
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 427, 4)
    _Documentation = None
STD_ANON_7._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_maxLength)
_module_typeBindings.STD_ANON_7 = STD_ANON_7

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 479, 8)
    _Documentation = None
STD_ANON_8._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_8, enum_prefix=None)
STD_ANON_8.as_each_product_is_ready = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='as each product is ready', tag='as_each_product_is_ready')
STD_ANON_8.once_all_products_are_ready = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='once all products are ready', tag='once_all_products_are_ready')
STD_ANON_8.other = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_enumeration)
_module_typeBindings.STD_ANON_8 = STD_ANON_8

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 493, 4)
    _Documentation = None
STD_ANON_9._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_maxLength)
_module_typeBindings.STD_ANON_9 = STD_ANON_9

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 500, 4)
    _Documentation = None
STD_ANON_10._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_maxLength)
_module_typeBindings.STD_ANON_10 = STD_ANON_10

# Atomic simple type: {http://www.opengis.net/oseo/1.0}PackageMedium
class PackageMedium (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PackageMedium')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 572, 1)
    _Documentation = None
PackageMedium._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PackageMedium, enum_prefix=None)
PackageMedium.NTP = PackageMedium._CF_enumeration.addEnumeration(unicode_value='NTP', tag='NTP')
PackageMedium.DAT = PackageMedium._CF_enumeration.addEnumeration(unicode_value='DAT', tag='DAT')
PackageMedium.Exabyte = PackageMedium._CF_enumeration.addEnumeration(unicode_value='Exabyte', tag='Exabyte')
PackageMedium.CD_ROM = PackageMedium._CF_enumeration.addEnumeration(unicode_value='CD-ROM', tag='CD_ROM')
PackageMedium.DLT = PackageMedium._CF_enumeration.addEnumeration(unicode_value='DLT', tag='DLT')
PackageMedium.D1 = PackageMedium._CF_enumeration.addEnumeration(unicode_value='D1', tag='D1')
PackageMedium.DVD = PackageMedium._CF_enumeration.addEnumeration(unicode_value='DVD', tag='DVD')
PackageMedium.BD = PackageMedium._CF_enumeration.addEnumeration(unicode_value='BD', tag='BD')
PackageMedium.LTO = PackageMedium._CF_enumeration.addEnumeration(unicode_value='LTO', tag='LTO')
PackageMedium.LTO2 = PackageMedium._CF_enumeration.addEnumeration(unicode_value='LTO2', tag='LTO2')
PackageMedium.LTO4 = PackageMedium._CF_enumeration.addEnumeration(unicode_value='LTO4', tag='LTO4')
PackageMedium._InitializeFacetMap(PackageMedium._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PackageMedium', PackageMedium)
_module_typeBindings.PackageMedium = PackageMedium

# Atomic simple type: {http://www.opengis.net/oseo/1.0}ProtocolType
class ProtocolType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProtocolType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 587, 1)
    _Documentation = None
ProtocolType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ProtocolType, enum_prefix=None)
ProtocolType.ftp = ProtocolType._CF_enumeration.addEnumeration(unicode_value='ftp', tag='ftp')
ProtocolType.ftps = ProtocolType._CF_enumeration.addEnumeration(unicode_value='ftps', tag='ftps')
ProtocolType.sftp = ProtocolType._CF_enumeration.addEnumeration(unicode_value='sftp', tag='sftp')
ProtocolType.P2P = ProtocolType._CF_enumeration.addEnumeration(unicode_value='P2P', tag='P2P')
ProtocolType.wcs = ProtocolType._CF_enumeration.addEnumeration(unicode_value='wcs', tag='wcs')
ProtocolType.wms = ProtocolType._CF_enumeration.addEnumeration(unicode_value='wms', tag='wms')
ProtocolType.e_mail = ProtocolType._CF_enumeration.addEnumeration(unicode_value='e-mail', tag='e_mail')
ProtocolType.dds = ProtocolType._CF_enumeration.addEnumeration(unicode_value='dds', tag='dds')
ProtocolType.http = ProtocolType._CF_enumeration.addEnumeration(unicode_value='http', tag='http')
ProtocolType.https = ProtocolType._CF_enumeration.addEnumeration(unicode_value='https', tag='https')
ProtocolType._InitializeFacetMap(ProtocolType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ProtocolType', ProtocolType)
_module_typeBindings.ProtocolType = ProtocolType

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 629, 4)
    _Documentation = None
STD_ANON_11._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_maxLength)
_module_typeBindings.STD_ANON_11 = STD_ANON_11

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 683, 7)
    _Documentation = None
STD_ANON_12._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_maxLength)
_module_typeBindings.STD_ANON_12 = STD_ANON_12

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 690, 7)
    _Documentation = None
STD_ANON_13._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_maxLength)
_module_typeBindings.STD_ANON_13 = STD_ANON_13

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 721, 6)
    _Documentation = None
STD_ANON_14._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_maxLength)
_module_typeBindings.STD_ANON_14 = STD_ANON_14

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 799, 6)
    _Documentation = None
STD_ANON_15._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_maxLength)
_module_typeBindings.STD_ANON_15 = STD_ANON_15

# Atomic simple type: [anonymous]
class STD_ANON_16 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 861, 4)
    _Documentation = None
STD_ANON_16._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
STD_ANON_16._InitializeFacetMap(STD_ANON_16._CF_maxLength)
_module_typeBindings.STD_ANON_16 = STD_ANON_16

# Atomic simple type: [anonymous]
class STD_ANON_17 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 877, 4)
    _Documentation = None
STD_ANON_17._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
STD_ANON_17._InitializeFacetMap(STD_ANON_17._CF_maxLength)
_module_typeBindings.STD_ANON_17 = STD_ANON_17

# Atomic simple type: [anonymous]
class STD_ANON_18 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 888, 4)
    _Documentation = None
STD_ANON_18._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
STD_ANON_18._InitializeFacetMap(STD_ANON_18._CF_maxLength)
_module_typeBindings.STD_ANON_18 = STD_ANON_18

# Atomic simple type: [anonymous]
class STD_ANON_19 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 895, 4)
    _Documentation = None
STD_ANON_19._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
STD_ANON_19._InitializeFacetMap(STD_ANON_19._CF_maxLength)
_module_typeBindings.STD_ANON_19 = STD_ANON_19

# Atomic simple type: {http://www.opengis.net/oseo/1.0}QuotationIdType
class QuotationIdType (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QuotationIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 903, 1)
    _Documentation = None
QuotationIdType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'QuotationIdType', QuotationIdType)
_module_typeBindings.QuotationIdType = QuotationIdType

# Atomic simple type: [anonymous]
class STD_ANON_20 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 916, 6)
    _Documentation = None
STD_ANON_20._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_20, enum_prefix=None)
STD_ANON_20.allReady = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='allReady', tag='allReady')
STD_ANON_20.nextReady = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='nextReady', tag='nextReady')
STD_ANON_20._InitializeFacetMap(STD_ANON_20._CF_enumeration)
_module_typeBindings.STD_ANON_20 = STD_ANON_20

# Atomic simple type: {http://www.opengis.net/oseo/1.0}EnumStatusType
class EnumStatusType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EnumStatusType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 939, 1)
    _Documentation = None
EnumStatusType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EnumStatusType, enum_prefix=None)
EnumStatusType.Submitted = EnumStatusType._CF_enumeration.addEnumeration(unicode_value='Submitted', tag='Submitted')
EnumStatusType.Accepted = EnumStatusType._CF_enumeration.addEnumeration(unicode_value='Accepted', tag='Accepted')
EnumStatusType.Cancelled = EnumStatusType._CF_enumeration.addEnumeration(unicode_value='Cancelled', tag='Cancelled')
EnumStatusType.Completed = EnumStatusType._CF_enumeration.addEnumeration(unicode_value='Completed', tag='Completed')
EnumStatusType.InProduction = EnumStatusType._CF_enumeration.addEnumeration(unicode_value='InProduction', tag='InProduction')
EnumStatusType.Suspended = EnumStatusType._CF_enumeration.addEnumeration(unicode_value='Suspended', tag='Suspended')
EnumStatusType.Failed = EnumStatusType._CF_enumeration.addEnumeration(unicode_value='Failed', tag='Failed')
EnumStatusType.Terminated = EnumStatusType._CF_enumeration.addEnumeration(unicode_value='Terminated', tag='Terminated')
EnumStatusType.Downloaded = EnumStatusType._CF_enumeration.addEnumeration(unicode_value='Downloaded', tag='Downloaded')
EnumStatusType._InitializeFacetMap(EnumStatusType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EnumStatusType', EnumStatusType)
_module_typeBindings.EnumStatusType = EnumStatusType

# Atomic simple type: [anonymous]
class STD_ANON_21 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 956, 4)
    _Documentation = None
STD_ANON_21._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_21._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_21._InitializeFacetMap(STD_ANON_21._CF_maxLength,
   STD_ANON_21._CF_minLength)
_module_typeBindings.STD_ANON_21 = STD_ANON_21

# Atomic simple type: [anonymous]
class STD_ANON_22 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 964, 4)
    _Documentation = None
STD_ANON_22._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_22._InitializeFacetMap(STD_ANON_22._CF_maxLength)
_module_typeBindings.STD_ANON_22 = STD_ANON_22

# Atomic simple type: [anonymous]
class STD_ANON_23 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 984, 4)
    _Documentation = None
STD_ANON_23._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
STD_ANON_23._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_23._InitializeFacetMap(STD_ANON_23._CF_maxLength,
   STD_ANON_23._CF_minLength)
_module_typeBindings.STD_ANON_23 = STD_ANON_23

# Atomic simple type: [anonymous]
class STD_ANON_24 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 995, 4)
    _Documentation = None
STD_ANON_24._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
STD_ANON_24._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_24._InitializeFacetMap(STD_ANON_24._CF_maxLength,
   STD_ANON_24._CF_minLength)
_module_typeBindings.STD_ANON_24 = STD_ANON_24

# Atomic simple type: [anonymous]
class STD_ANON_25 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1003, 4)
    _Documentation = None
STD_ANON_25._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
STD_ANON_25._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_25._InitializeFacetMap(STD_ANON_25._CF_maxLength,
   STD_ANON_25._CF_minLength)
_module_typeBindings.STD_ANON_25 = STD_ANON_25

# Atomic simple type: [anonymous]
class STD_ANON_26 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1014, 7)
    _Documentation = None
STD_ANON_26._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
STD_ANON_26._InitializeFacetMap(STD_ANON_26._CF_maxLength)
_module_typeBindings.STD_ANON_26 = STD_ANON_26

# Atomic simple type: [anonymous]
class STD_ANON_27 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1021, 7)
    _Documentation = None
STD_ANON_27._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
STD_ANON_27._InitializeFacetMap(STD_ANON_27._CF_maxLength)
_module_typeBindings.STD_ANON_27 = STD_ANON_27

# Atomic simple type: [anonymous]
class STD_ANON_28 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1028, 7)
    _Documentation = None
STD_ANON_28._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
STD_ANON_28._InitializeFacetMap(STD_ANON_28._CF_maxLength)
_module_typeBindings.STD_ANON_28 = STD_ANON_28

# Atomic simple type: [anonymous]
class STD_ANON_29 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1035, 7)
    _Documentation = None
STD_ANON_29._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12))
STD_ANON_29._InitializeFacetMap(STD_ANON_29._CF_maxLength)
_module_typeBindings.STD_ANON_29 = STD_ANON_29

# Atomic simple type: [anonymous]
class STD_ANON_30 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1042, 7)
    _Documentation = None
STD_ANON_30._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
STD_ANON_30._InitializeFacetMap(STD_ANON_30._CF_maxLength)
_module_typeBindings.STD_ANON_30 = STD_ANON_30

# Atomic simple type: [anonymous]
class STD_ANON_31 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1052, 7)
    _Documentation = None
STD_ANON_31._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12))
STD_ANON_31._InitializeFacetMap(STD_ANON_31._CF_maxLength)
_module_typeBindings.STD_ANON_31 = STD_ANON_31

# Atomic simple type: [anonymous]
class STD_ANON_32 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1065, 4)
    _Documentation = None
STD_ANON_32._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(18))
STD_ANON_32._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_32._InitializeFacetMap(STD_ANON_32._CF_maxLength,
   STD_ANON_32._CF_minLength)
_module_typeBindings.STD_ANON_32 = STD_ANON_32

# Atomic simple type: [anonymous]
class STD_ANON_33 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1076, 4)
    _Documentation = None
STD_ANON_33._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(18))
STD_ANON_33._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_33._InitializeFacetMap(STD_ANON_33._CF_maxLength,
   STD_ANON_33._CF_minLength)
_module_typeBindings.STD_ANON_33 = STD_ANON_33

# Atomic simple type: [anonymous]
class STD_ANON_34 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1120, 4)
    _Documentation = None
STD_ANON_34._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
STD_ANON_34._InitializeFacetMap(STD_ANON_34._CF_maxLength)
_module_typeBindings.STD_ANON_34 = STD_ANON_34

# Atomic simple type: [anonymous]
class STD_ANON_35 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1127, 4)
    _Documentation = None
STD_ANON_35._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8))
STD_ANON_35._InitializeFacetMap(STD_ANON_35._CF_maxLength)
_module_typeBindings.STD_ANON_35 = STD_ANON_35

# Atomic simple type: [anonymous]
class STD_ANON_36 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1134, 4)
    _Documentation = None
STD_ANON_36._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_36._InitializeFacetMap(STD_ANON_36._CF_maxLength)
_module_typeBindings.STD_ANON_36 = STD_ANON_36

# Atomic simple type: [anonymous]
class STD_ANON_37 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1141, 4)
    _Documentation = None
STD_ANON_37._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1024))
STD_ANON_37._InitializeFacetMap(STD_ANON_37._CF_maxLength)
_module_typeBindings.STD_ANON_37 = STD_ANON_37

# Atomic simple type: {http://www.opengis.net/oseo/1.0}EnumOrderType
class EnumOrderType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EnumOrderType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1223, 1)
    _Documentation = None
EnumOrderType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EnumOrderType, enum_prefix=None)
EnumOrderType.PRODUCT_ORDER = EnumOrderType._CF_enumeration.addEnumeration(unicode_value='PRODUCT_ORDER', tag='PRODUCT_ORDER')
EnumOrderType.SUBSCRIPTION_ORDER = EnumOrderType._CF_enumeration.addEnumeration(unicode_value='SUBSCRIPTION_ORDER', tag='SUBSCRIPTION_ORDER')
EnumOrderType.TASKING_ORDER = EnumOrderType._CF_enumeration.addEnumeration(unicode_value='TASKING_ORDER', tag='TASKING_ORDER')
EnumOrderType._InitializeFacetMap(EnumOrderType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EnumOrderType', EnumOrderType)
_module_typeBindings.EnumOrderType = EnumOrderType

# Atomic simple type: {http://www.opengis.net/oseo/1.0}EnumPackagingType
class EnumPackagingType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EnumPackagingType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1233, 1)
    _Documentation = None
EnumPackagingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EnumPackagingType, enum_prefix=None)
EnumPackagingType.zip = EnumPackagingType._CF_enumeration.addEnumeration(unicode_value='zip', tag='zip')
EnumPackagingType.tar = EnumPackagingType._CF_enumeration.addEnumeration(unicode_value='tar', tag='tar')
EnumPackagingType.tgz = EnumPackagingType._CF_enumeration.addEnumeration(unicode_value='tgz', tag='tgz')
EnumPackagingType.compress = EnumPackagingType._CF_enumeration.addEnumeration(unicode_value='compress', tag='compress')
EnumPackagingType.bzip = EnumPackagingType._CF_enumeration.addEnumeration(unicode_value='bzip', tag='bzip')
EnumPackagingType.bzip2 = EnumPackagingType._CF_enumeration.addEnumeration(unicode_value='bzip2', tag='bzip2')
EnumPackagingType.gzip = EnumPackagingType._CF_enumeration.addEnumeration(unicode_value='gzip', tag='gzip')
EnumPackagingType.rar = EnumPackagingType._CF_enumeration.addEnumeration(unicode_value='rar', tag='rar')
EnumPackagingType.n7z = EnumPackagingType._CF_enumeration.addEnumeration(unicode_value='7z', tag='n7z')
EnumPackagingType._InitializeFacetMap(EnumPackagingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EnumPackagingType', EnumPackagingType)
_module_typeBindings.EnumPackagingType = EnumPackagingType

# Atomic simple type: {http://www.opengis.net/oseo/1.0}OrderResponseStatusType
class OrderResponseStatusType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrderResponseStatusType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1246, 1)
    _Documentation = None
OrderResponseStatusType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=OrderResponseStatusType, enum_prefix=None)
OrderResponseStatusType.success = OrderResponseStatusType._CF_enumeration.addEnumeration(unicode_value='success', tag='success')
OrderResponseStatusType.partial = OrderResponseStatusType._CF_enumeration.addEnumeration(unicode_value='partial', tag='partial')
OrderResponseStatusType._InitializeFacetMap(OrderResponseStatusType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'OrderResponseStatusType', OrderResponseStatusType)
_module_typeBindings.OrderResponseStatusType = OrderResponseStatusType

# Atomic simple type: {http://www.opengis.net/oseo/1.0}PresentationType
class PresentationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PresentationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1252, 1)
    _Documentation = None
PresentationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PresentationType, enum_prefix=None)
PresentationType.brief = PresentationType._CF_enumeration.addEnumeration(unicode_value='brief', tag='brief')
PresentationType.full = PresentationType._CF_enumeration.addEnumeration(unicode_value='full', tag='full')
PresentationType._InitializeFacetMap(PresentationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PresentationType', PresentationType)
_module_typeBindings.PresentationType = PresentationType

# Atomic simple type: {http://www.opengis.net/oseo/1.0}PriorityType
class PriorityType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PriorityType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1258, 1)
    _Documentation = None
PriorityType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PriorityType, enum_prefix=None)
PriorityType.STANDARD = PriorityType._CF_enumeration.addEnumeration(unicode_value='STANDARD', tag='STANDARD')
PriorityType.FAST_TRACK = PriorityType._CF_enumeration.addEnumeration(unicode_value='FAST_TRACK', tag='FAST_TRACK')
PriorityType._InitializeFacetMap(PriorityType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PriorityType', PriorityType)
_module_typeBindings.PriorityType = PriorityType

# Atomic simple type: [anonymous]
class STD_ANON_38 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1274, 2)
    _Documentation = None
STD_ANON_38._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(80))
STD_ANON_38._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_38._InitializeFacetMap(STD_ANON_38._CF_maxLength,
   STD_ANON_38._CF_minLength)
_module_typeBindings.STD_ANON_38 = STD_ANON_38

# Atomic simple type: [anonymous]
class STD_ANON_39 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1286, 2)
    _Documentation = None
STD_ANON_39._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
STD_ANON_39._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_39._InitializeFacetMap(STD_ANON_39._CF_maxLength,
   STD_ANON_39._CF_minLength)
_module_typeBindings.STD_ANON_39 = STD_ANON_39

# Atomic simple type: [anonymous]
class STD_ANON_40 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1294, 2)
    _Documentation = None
STD_ANON_40._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1024))
STD_ANON_40._InitializeFacetMap(STD_ANON_40._CF_maxLength)
_module_typeBindings.STD_ANON_40 = STD_ANON_40

# Atomic simple type: [anonymous]
class STD_ANON_41 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1301, 2)
    _Documentation = None
STD_ANON_41._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
STD_ANON_41._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_41._InitializeFacetMap(STD_ANON_41._CF_maxLength,
   STD_ANON_41._CF_minLength)
_module_typeBindings.STD_ANON_41 = STD_ANON_41

# Atomic simple type: [anonymous]
class STD_ANON_42 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1309, 2)
    _Documentation = None
STD_ANON_42._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
STD_ANON_42._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_42._InitializeFacetMap(STD_ANON_42._CF_maxLength,
   STD_ANON_42._CF_minLength)
_module_typeBindings.STD_ANON_42 = STD_ANON_42

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.bundles.opengis.ows_2_0.GetCapabilitiesType):
    """Request to a Order Service to perform the GetCapabilities operation. This operation allows a client to retrieve service metadata (capabilities XML) providing metadata for the specific Order server. In this XML encoding, no "request" parameter is included, since the element name specifies the specific operation. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 20, 2)
    _ElementMap = pyxb.bundles.opengis.ows_2_0.GetCapabilitiesType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.ows_2_0.GetCapabilitiesType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.ows_2_0.GetCapabilitiesType
    
    # Element AcceptVersions ({http://www.opengis.net/ows/2.0}AcceptVersions) inherited from {http://www.opengis.net/ows/2.0}GetCapabilitiesType
    
    # Element Sections ({http://www.opengis.net/ows/2.0}Sections) inherited from {http://www.opengis.net/ows/2.0}GetCapabilitiesType
    
    # Element AcceptFormats ({http://www.opengis.net/ows/2.0}AcceptFormats) inherited from {http://www.opengis.net/ows/2.0}GetCapabilitiesType
    
    # Element AcceptLanguages ({http://www.opengis.net/ows/2.0}AcceptLanguages) inherited from {http://www.opengis.net/ows/2.0}GetCapabilitiesType
    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__httpwww_opengis_netoseo1_0_CTD_ANON_service', pyxb.bundles.opengis.ows_2_0.ServiceType, fixed=True, unicode_default='OS', required=True)
    __service._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 23, 5)
    __service._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 23, 5)
    
    service = property(__service.value, __service.set, None, None)

    
    # Attribute updateSequence inherited from {http://www.opengis.net/ows/2.0}GetCapabilitiesType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __service.name() : __service
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.bundles.opengis.ows_2_0.CapabilitiesBaseType):
    """XML encoded Order Service GetCapabilities operation response. This document provides clients with service metadata about a specific service instance. If the server does not implement the updateSequence parameter, the server shall always return the complete Capabilities document, without the updateSequence parameter. When the server implements the updateSequence parameter and the GetCapabilities operation request included the updateSequence parameter with the current value, the server shall return this element with only the "version" and "updateSequence" attributes. Otherwise, all optional elements shall be included or not depending on the actual value of the Sections parameter in the GetCapabilities operation request. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 32, 2)
    _ElementMap = pyxb.bundles.opengis.ows_2_0.CapabilitiesBaseType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.ows_2_0.CapabilitiesBaseType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.ows_2_0.CapabilitiesBaseType
    
    # Element {http://www.opengis.net/oseo/1.0}Contents uses Python identifier Contents
    __Contents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Contents'), 'Contents', '__httpwww_opengis_netoseo1_0_CTD_ANON__httpwww_opengis_netoseo1_0Contents', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 36, 6), )

    
    Contents = property(__Contents.value, __Contents.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}Notifications uses Python identifier Notifications
    __Notifications = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Notifications'), 'Notifications', '__httpwww_opengis_netoseo1_0_CTD_ANON__httpwww_opengis_netoseo1_0Notifications', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 37, 6), )

    
    Notifications = property(__Notifications.value, __Notifications.set, None, None)

    
    # Element Languages ({http://www.opengis.net/ows/2.0}Languages) inherited from {http://www.opengis.net/ows/2.0}CapabilitiesBaseType
    
    # Element OperationsMetadata ({http://www.opengis.net/ows/2.0}OperationsMetadata) inherited from {http://www.opengis.net/ows/2.0}CapabilitiesBaseType
    
    # Element ServiceIdentification ({http://www.opengis.net/ows/2.0}ServiceIdentification) inherited from {http://www.opengis.net/ows/2.0}CapabilitiesBaseType
    
    # Element ServiceProvider ({http://www.opengis.net/ows/2.0}ServiceProvider) inherited from {http://www.opengis.net/ows/2.0}CapabilitiesBaseType
    
    # Attribute version inherited from {http://www.opengis.net/ows/2.0}CapabilitiesBaseType
    
    # Attribute updateSequence inherited from {http://www.opengis.net/ows/2.0}CapabilitiesBaseType
    _ElementMap.update({
        __Contents.name() : __Contents,
        __Notifications.name() : __Notifications
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {http://www.opengis.net/oseo/1.0}OrderResponseBaseType with content type ELEMENT_ONLY
class OrderResponseBaseType (pyxb.binding.basis.complexTypeDefinition):
    """Base type for all Ordering Service operation responses."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrderResponseBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 126, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__httpwww_opengis_netoseo1_0_OrderResponseBaseType_httpwww_opengis_netoseo1_0status', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 131, 3), )

    
    status = property(__status.value, __status.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}errorMessage uses Python identifier errorMessage
    __errorMessage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'errorMessage'), 'errorMessage', '__httpwww_opengis_netoseo1_0_OrderResponseBaseType_httpwww_opengis_netoseo1_0errorMessage', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3), )

    
    errorMessage = property(__errorMessage.value, __errorMessage.set, None, 'This field is set when status element is different from success. It provides some information about the occurred problem.')

    _ElementMap.update({
        __status.name() : __status,
        __errorMessage.name() : __errorMessage
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrderResponseBaseType = OrderResponseBaseType
Namespace.addCategoryObject('typeBinding', 'OrderResponseBaseType', OrderResponseBaseType)


# Complex type {http://www.opengis.net/oseo/1.0}OrderingServiceContentsType with content type ELEMENT_ONLY
class OrderingServiceContentsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}OrderingServiceContentsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrderingServiceContentsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 144, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}ProductOrders uses Python identifier ProductOrders
    __ProductOrders = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProductOrders'), 'ProductOrders', '__httpwww_opengis_netoseo1_0_OrderingServiceContentsType_httpwww_opengis_netoseo1_0ProductOrders', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 146, 3), )

    
    ProductOrders = property(__ProductOrders.value, __ProductOrders.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}SubscriptionOrders uses Python identifier SubscriptionOrders
    __SubscriptionOrders = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubscriptionOrders'), 'SubscriptionOrders', '__httpwww_opengis_netoseo1_0_OrderingServiceContentsType_httpwww_opengis_netoseo1_0SubscriptionOrders', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 151, 3), )

    
    SubscriptionOrders = property(__SubscriptionOrders.value, __SubscriptionOrders.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}ProgrammingOrders uses Python identifier ProgrammingOrders
    __ProgrammingOrders = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProgrammingOrders'), 'ProgrammingOrders', '__httpwww_opengis_netoseo1_0_OrderingServiceContentsType_httpwww_opengis_netoseo1_0ProgrammingOrders', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 156, 3), )

    
    ProgrammingOrders = property(__ProgrammingOrders.value, __ProgrammingOrders.set, None, 'Specifies whether the Ordering Services supports future products ordering and the corresponding SPS URL.')

    
    # Element {http://www.opengis.net/oseo/1.0}GetQuotationCapabilities uses Python identifier GetQuotationCapabilities
    __GetQuotationCapabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GetQuotationCapabilities'), 'GetQuotationCapabilities', '__httpwww_opengis_netoseo1_0_OrderingServiceContentsType_httpwww_opengis_netoseo1_0GetQuotationCapabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 165, 3), )

    
    GetQuotationCapabilities = property(__GetQuotationCapabilities.value, __GetQuotationCapabilities.set, None, 'This element specifies if and how the order quotation is supported: synchronously, asynchronously, synchronous with polling.')

    
    # Element {http://www.opengis.net/oseo/1.0}SubmitCapabilities uses Python identifier SubmitCapabilities
    __SubmitCapabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubmitCapabilities'), 'SubmitCapabilities', '__httpwww_opengis_netoseo1_0_OrderingServiceContentsType_httpwww_opengis_netoseo1_0SubmitCapabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 177, 3), )

    
    SubmitCapabilities = property(__SubmitCapabilities.value, __SubmitCapabilities.set, None, 'This element specifies the capabilities of Submit Operation e.g. synchronous, async, max number of products, etc.')

    
    # Element {http://www.opengis.net/oseo/1.0}GetStatusCapabilities uses Python identifier GetStatusCapabilities
    __GetStatusCapabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GetStatusCapabilities'), 'GetStatusCapabilities', '__httpwww_opengis_netoseo1_0_OrderingServiceContentsType_httpwww_opengis_netoseo1_0GetStatusCapabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 190, 3), )

    
    GetStatusCapabilities = property(__GetStatusCapabilities.value, __GetStatusCapabilities.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}DescribeResultAccessCapabilities uses Python identifier DescribeResultAccessCapabilities
    __DescribeResultAccessCapabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DescribeResultAccessCapabilities'), 'DescribeResultAccessCapabilities', '__httpwww_opengis_netoseo1_0_OrderingServiceContentsType_httpwww_opengis_netoseo1_0DescribeResultAccessCapabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 197, 3), )

    
    DescribeResultAccessCapabilities = property(__DescribeResultAccessCapabilities.value, __DescribeResultAccessCapabilities.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}CancelCapabilities uses Python identifier CancelCapabilities
    __CancelCapabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CancelCapabilities'), 'CancelCapabilities', '__httpwww_opengis_netoseo1_0_OrderingServiceContentsType_httpwww_opengis_netoseo1_0CancelCapabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 202, 3), )

    
    CancelCapabilities = property(__CancelCapabilities.value, __CancelCapabilities.set, None, 'This element specifies the capabilities of Submit Operation e.g. synchronous, async, max number of products, etc.')

    
    # Element {http://www.opengis.net/oseo/1.0}SupportedCollection uses Python identifier SupportedCollection
    __SupportedCollection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SupportedCollection'), 'SupportedCollection', '__httpwww_opengis_netoseo1_0_OrderingServiceContentsType_httpwww_opengis_netoseo1_0SupportedCollection', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 211, 3), )

    
    SupportedCollection = property(__SupportedCollection.value, __SupportedCollection.set, None, 'List of collections allowed for ordering.')

    
    # Element {http://www.opengis.net/oseo/1.0}ContentsType uses Python identifier ContentsType
    __ContentsType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContentsType'), 'ContentsType', '__httpwww_opengis_netoseo1_0_OrderingServiceContentsType_httpwww_opengis_netoseo1_0ContentsType', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 216, 3), )

    
    ContentsType = property(__ContentsType.value, __ContentsType.set, None, None)

    _ElementMap.update({
        __ProductOrders.name() : __ProductOrders,
        __SubscriptionOrders.name() : __SubscriptionOrders,
        __ProgrammingOrders.name() : __ProgrammingOrders,
        __GetQuotationCapabilities.name() : __GetQuotationCapabilities,
        __SubmitCapabilities.name() : __SubmitCapabilities,
        __GetStatusCapabilities.name() : __GetStatusCapabilities,
        __DescribeResultAccessCapabilities.name() : __DescribeResultAccessCapabilities,
        __CancelCapabilities.name() : __CancelCapabilities,
        __SupportedCollection.name() : __SupportedCollection,
        __ContentsType.name() : __ContentsType
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrderingServiceContentsType = OrderingServiceContentsType
Namespace.addCategoryObject('typeBinding', 'OrderingServiceContentsType', OrderingServiceContentsType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 147, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute supported uses Python identifier supported
    __supported = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'supported'), 'supported', '__httpwww_opengis_netoseo1_0_CTD_ANON_2_supported', pyxb.binding.datatypes.boolean, required=True)
    __supported._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 148, 5)
    __supported._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 148, 5)
    
    supported = property(__supported.value, __supported.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __supported.name() : __supported
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 152, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute supported uses Python identifier supported
    __supported = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'supported'), 'supported', '__httpwww_opengis_netoseo1_0_CTD_ANON_3_supported', pyxb.binding.datatypes.boolean, required=True)
    __supported._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 153, 5)
    __supported._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 153, 5)
    
    supported = property(__supported.value, __supported.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __supported.name() : __supported
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Specifies whether the Ordering Services supports future products ordering and the corresponding SPS URL."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 160, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute supported uses Python identifier supported
    __supported = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'supported'), 'supported', '__httpwww_opengis_netoseo1_0_CTD_ANON_4_supported', pyxb.binding.datatypes.boolean, required=True)
    __supported._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 161, 5)
    __supported._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 161, 5)
    
    supported = property(__supported.value, __supported.set, None, None)

    
    # Attribute SPS_URL uses Python identifier SPS_URL
    __SPS_URL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SPS_URL'), 'SPS_URL', '__httpwww_opengis_netoseo1_0_CTD_ANON_4_SPS_URL', pyxb.binding.datatypes.anyURI)
    __SPS_URL._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 162, 5)
    __SPS_URL._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 162, 5)
    
    SPS_URL = property(__SPS_URL.value, __SPS_URL.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __supported.name() : __supported,
        __SPS_URL.name() : __SPS_URL
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """This element specifies if and how the order quotation is supported: synchronously, asynchronously, synchronous with polling."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 169, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute supported uses Python identifier supported
    __supported = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'supported'), 'supported', '__httpwww_opengis_netoseo1_0_CTD_ANON_5_supported', pyxb.binding.datatypes.boolean, required=True)
    __supported._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 170, 5)
    __supported._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 170, 5)
    
    supported = property(__supported.value, __supported.set, None, None)

    
    # Attribute synchronous uses Python identifier synchronous
    __synchronous = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'synchronous'), 'synchronous', '__httpwww_opengis_netoseo1_0_CTD_ANON_5_synchronous', pyxb.binding.datatypes.boolean, required=True)
    __synchronous._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 171, 5)
    __synchronous._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 171, 5)
    
    synchronous = property(__synchronous.value, __synchronous.set, None, None)

    
    # Attribute asynchronous uses Python identifier asynchronous
    __asynchronous = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'asynchronous'), 'asynchronous', '__httpwww_opengis_netoseo1_0_CTD_ANON_5_asynchronous', pyxb.binding.datatypes.boolean, required=True)
    __asynchronous._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 172, 5)
    __asynchronous._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 172, 5)
    
    asynchronous = property(__asynchronous.value, __asynchronous.set, None, None)

    
    # Attribute monitoring uses Python identifier monitoring
    __monitoring = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'monitoring'), 'monitoring', '__httpwww_opengis_netoseo1_0_CTD_ANON_5_monitoring', pyxb.binding.datatypes.boolean, required=True)
    __monitoring._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 173, 5)
    __monitoring._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 173, 5)
    
    monitoring = property(__monitoring.value, __monitoring.set, None, None)

    
    # Attribute off-line uses Python identifier off_line
    __off_line = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'off-line'), 'off_line', '__httpwww_opengis_netoseo1_0_CTD_ANON_5_off_line', pyxb.binding.datatypes.boolean, required=True)
    __off_line._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 174, 5)
    __off_line._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 174, 5)
    
    off_line = property(__off_line.value, __off_line.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __supported.name() : __supported,
        __synchronous.name() : __synchronous,
        __asynchronous.name() : __asynchronous,
        __monitoring.name() : __monitoring,
        __off_line.name() : __off_line
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """This element specifies the capabilities of Submit Operation e.g. synchronous, async, max number of products, etc."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 181, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute asynchronous uses Python identifier asynchronous
    __asynchronous = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'asynchronous'), 'asynchronous', '__httpwww_opengis_netoseo1_0_CTD_ANON_6_asynchronous', pyxb.binding.datatypes.boolean, required=True)
    __asynchronous._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 182, 5)
    __asynchronous._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 182, 5)
    
    asynchronous = property(__asynchronous.value, __asynchronous.set, None, None)

    
    # Attribute maxNumberOfProducts uses Python identifier maxNumberOfProducts
    __maxNumberOfProducts = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxNumberOfProducts'), 'maxNumberOfProducts', '__httpwww_opengis_netoseo1_0_CTD_ANON_6_maxNumberOfProducts', pyxb.binding.datatypes.integer)
    __maxNumberOfProducts._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 183, 5)
    __maxNumberOfProducts._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 183, 5)
    
    maxNumberOfProducts = property(__maxNumberOfProducts.value, __maxNumberOfProducts.set, None, None)

    
    # Attribute globalDeliveryOptions uses Python identifier globalDeliveryOptions
    __globalDeliveryOptions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'globalDeliveryOptions'), 'globalDeliveryOptions', '__httpwww_opengis_netoseo1_0_CTD_ANON_6_globalDeliveryOptions', pyxb.binding.datatypes.boolean, required=True)
    __globalDeliveryOptions._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 184, 5)
    __globalDeliveryOptions._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 184, 5)
    
    globalDeliveryOptions = property(__globalDeliveryOptions.value, __globalDeliveryOptions.set, None, None)

    
    # Attribute localDeliveryOptions uses Python identifier localDeliveryOptions
    __localDeliveryOptions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'localDeliveryOptions'), 'localDeliveryOptions', '__httpwww_opengis_netoseo1_0_CTD_ANON_6_localDeliveryOptions', pyxb.binding.datatypes.boolean, required=True)
    __localDeliveryOptions._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 185, 5)
    __localDeliveryOptions._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 185, 5)
    
    localDeliveryOptions = property(__localDeliveryOptions.value, __localDeliveryOptions.set, None, None)

    
    # Attribute globalOrderOptions uses Python identifier globalOrderOptions
    __globalOrderOptions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'globalOrderOptions'), 'globalOrderOptions', '__httpwww_opengis_netoseo1_0_CTD_ANON_6_globalOrderOptions', pyxb.binding.datatypes.boolean, required=True)
    __globalOrderOptions._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 186, 5)
    __globalOrderOptions._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 186, 5)
    
    globalOrderOptions = property(__globalOrderOptions.value, __globalOrderOptions.set, None, None)

    
    # Attribute localOrderOptions uses Python identifier localOrderOptions
    __localOrderOptions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'localOrderOptions'), 'localOrderOptions', '__httpwww_opengis_netoseo1_0_CTD_ANON_6_localOrderOptions', pyxb.binding.datatypes.boolean, required=True)
    __localOrderOptions._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 187, 5)
    __localOrderOptions._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 187, 5)
    
    localOrderOptions = property(__localOrderOptions.value, __localOrderOptions.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __asynchronous.name() : __asynchronous,
        __maxNumberOfProducts.name() : __maxNumberOfProducts,
        __globalDeliveryOptions.name() : __globalDeliveryOptions,
        __localDeliveryOptions.name() : __localDeliveryOptions,
        __globalOrderOptions.name() : __globalOrderOptions,
        __localOrderOptions.name() : __localOrderOptions
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 191, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute orderSearch uses Python identifier orderSearch
    __orderSearch = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'orderSearch'), 'orderSearch', '__httpwww_opengis_netoseo1_0_CTD_ANON_7_orderSearch', pyxb.binding.datatypes.boolean, required=True)
    __orderSearch._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 192, 5)
    __orderSearch._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 192, 5)
    
    orderSearch = property(__orderSearch.value, __orderSearch.set, None, None)

    
    # Attribute orderRetrieve uses Python identifier orderRetrieve
    __orderRetrieve = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'orderRetrieve'), 'orderRetrieve', '__httpwww_opengis_netoseo1_0_CTD_ANON_7_orderRetrieve', pyxb.binding.datatypes.boolean, required=True)
    __orderRetrieve._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 193, 5)
    __orderRetrieve._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 193, 5)
    
    orderRetrieve = property(__orderRetrieve.value, __orderRetrieve.set, None, None)

    
    # Attribute full uses Python identifier full
    __full = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'full'), 'full', '__httpwww_opengis_netoseo1_0_CTD_ANON_7_full', pyxb.binding.datatypes.boolean, required=True)
    __full._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 194, 5)
    __full._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 194, 5)
    
    full = property(__full.value, __full.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __orderSearch.name() : __orderSearch,
        __orderRetrieve.name() : __orderRetrieve,
        __full.name() : __full
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 198, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute supported uses Python identifier supported
    __supported = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'supported'), 'supported', '__httpwww_opengis_netoseo1_0_CTD_ANON_8_supported', pyxb.binding.datatypes.boolean, required=True)
    __supported._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 199, 5)
    __supported._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 199, 5)
    
    supported = property(__supported.value, __supported.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __supported.name() : __supported
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """This element specifies the capabilities of Submit Operation e.g. synchronous, async, max number of products, etc."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 206, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute supported uses Python identifier supported
    __supported = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'supported'), 'supported', '__httpwww_opengis_netoseo1_0_CTD_ANON_9_supported', pyxb.binding.datatypes.boolean, required=True)
    __supported._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 207, 5)
    __supported._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 207, 5)
    
    supported = property(__supported.value, __supported.set, None, None)

    
    # Attribute asynchronous uses Python identifier asynchronous
    __asynchronous = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'asynchronous'), 'asynchronous', '__httpwww_opengis_netoseo1_0_CTD_ANON_9_asynchronous', pyxb.binding.datatypes.boolean, required=True)
    __asynchronous._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 208, 5)
    __asynchronous._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 208, 5)
    
    asynchronous = property(__asynchronous.value, __asynchronous.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __supported.name() : __supported,
        __asynchronous.name() : __asynchronous
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type {http://www.opengis.net/oseo/1.0}CollectionCapability with content type ELEMENT_ONLY
class CollectionCapability (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}CollectionCapability with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CollectionCapability')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 219, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}collectionId uses Python identifier collectionId
    __collectionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'collectionId'), 'collectionId', '__httpwww_opengis_netoseo1_0_CollectionCapability_httpwww_opengis_netoseo1_0collectionId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 95, 1), )

    
    collectionId = property(__collectionId.value, __collectionId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}ProductOrders uses Python identifier ProductOrders
    __ProductOrders = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProductOrders'), 'ProductOrders', '__httpwww_opengis_netoseo1_0_CollectionCapability_httpwww_opengis_netoseo1_0ProductOrders', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 222, 3), )

    
    ProductOrders = property(__ProductOrders.value, __ProductOrders.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}SubscriptionOrders uses Python identifier SubscriptionOrders
    __SubscriptionOrders = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubscriptionOrders'), 'SubscriptionOrders', '__httpwww_opengis_netoseo1_0_CollectionCapability_httpwww_opengis_netoseo1_0SubscriptionOrders', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 227, 3), )

    
    SubscriptionOrders = property(__SubscriptionOrders.value, __SubscriptionOrders.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}DescribeResultAccessCapabilities uses Python identifier DescribeResultAccessCapabilities
    __DescribeResultAccessCapabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DescribeResultAccessCapabilities'), 'DescribeResultAccessCapabilities', '__httpwww_opengis_netoseo1_0_CollectionCapability_httpwww_opengis_netoseo1_0DescribeResultAccessCapabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 232, 3), )

    
    DescribeResultAccessCapabilities = property(__DescribeResultAccessCapabilities.value, __DescribeResultAccessCapabilities.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}CancelCapabilities uses Python identifier CancelCapabilities
    __CancelCapabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CancelCapabilities'), 'CancelCapabilities', '__httpwww_opengis_netoseo1_0_CollectionCapability_httpwww_opengis_netoseo1_0CancelCapabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 237, 3), )

    
    CancelCapabilities = property(__CancelCapabilities.value, __CancelCapabilities.set, None, 'This element specifies the capabilities of Submit Operation e.g. synchronous, async, max number of products, etc.')

    _ElementMap.update({
        __collectionId.name() : __collectionId,
        __ProductOrders.name() : __ProductOrders,
        __SubscriptionOrders.name() : __SubscriptionOrders,
        __DescribeResultAccessCapabilities.name() : __DescribeResultAccessCapabilities,
        __CancelCapabilities.name() : __CancelCapabilities
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CollectionCapability = CollectionCapability
Namespace.addCategoryObject('typeBinding', 'CollectionCapability', CollectionCapability)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 223, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute supported uses Python identifier supported
    __supported = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'supported'), 'supported', '__httpwww_opengis_netoseo1_0_CTD_ANON_10_supported', pyxb.binding.datatypes.boolean, required=True)
    __supported._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 224, 5)
    __supported._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 224, 5)
    
    supported = property(__supported.value, __supported.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __supported.name() : __supported
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 228, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute supported uses Python identifier supported
    __supported = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'supported'), 'supported', '__httpwww_opengis_netoseo1_0_CTD_ANON_11_supported', pyxb.binding.datatypes.boolean, required=True)
    __supported._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 229, 5)
    __supported._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 229, 5)
    
    supported = property(__supported.value, __supported.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __supported.name() : __supported
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 233, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute supported uses Python identifier supported
    __supported = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'supported'), 'supported', '__httpwww_opengis_netoseo1_0_CTD_ANON_12_supported', pyxb.binding.datatypes.boolean, required=True)
    __supported._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 234, 5)
    __supported._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 234, 5)
    
    supported = property(__supported.value, __supported.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __supported.name() : __supported
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """This element specifies the capabilities of Submit Operation e.g. synchronous, async, max number of products, etc."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 241, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute supported uses Python identifier supported
    __supported = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'supported'), 'supported', '__httpwww_opengis_netoseo1_0_CTD_ANON_13_supported', pyxb.binding.datatypes.boolean, required=True)
    __supported._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 242, 5)
    __supported._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 242, 5)
    
    supported = property(__supported.value, __supported.set, None, None)

    
    # Attribute asynchronous uses Python identifier asynchronous
    __asynchronous = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'asynchronous'), 'asynchronous', '__httpwww_opengis_netoseo1_0_CTD_ANON_13_asynchronous', pyxb.binding.datatypes.boolean, required=True)
    __asynchronous._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 243, 5)
    __asynchronous._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 243, 5)
    
    asynchronous = property(__asynchronous.value, __asynchronous.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __supported.name() : __supported,
        __asynchronous.name() : __asynchronous
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type {http://www.opengis.net/oseo/1.0}EncodingType with content type ELEMENT_ONLY
class EncodingType (pyxb.binding.basis.complexTypeDefinition):
    """Type of encoding provided by the server"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EncodingType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 248, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}supportedEncoding uses Python identifier supportedEncoding
    __supportedEncoding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supportedEncoding'), 'supportedEncoding', '__httpwww_opengis_netoseo1_0_EncodingType_httpwww_opengis_netoseo1_0supportedEncoding', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 253, 3), )

    
    supportedEncoding = property(__supportedEncoding.value, __supportedEncoding.set, None, None)

    _ElementMap.update({
        __supportedEncoding.name() : __supportedEncoding
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EncodingType = EncodingType
Namespace.addCategoryObject('typeBinding', 'EncodingType', EncodingType)


# Complex type {http://www.opengis.net/oseo/1.0}CommonOrderSpecification with content type ELEMENT_ONLY
class CommonOrderSpecification (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}CommonOrderSpecification with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommonOrderSpecification')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 302, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}priority uses Python identifier priority
    __priority = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'priority'), 'priority', '__httpwww_opengis_netoseo1_0_CommonOrderSpecification_httpwww_opengis_netoseo1_0priority', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 85, 1), )

    
    priority = property(__priority.value, __priority.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}orderRemark uses Python identifier orderRemark
    __orderRemark = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderRemark'), 'orderRemark', '__httpwww_opengis_netoseo1_0_CommonOrderSpecification_httpwww_opengis_netoseo1_0orderRemark', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 305, 3), )

    
    orderRemark = property(__orderRemark.value, __orderRemark.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}deliveryInformation uses Python identifier deliveryInformation
    __deliveryInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'deliveryInformation'), 'deliveryInformation', '__httpwww_opengis_netoseo1_0_CommonOrderSpecification_httpwww_opengis_netoseo1_0deliveryInformation', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 313, 3), )

    
    deliveryInformation = property(__deliveryInformation.value, __deliveryInformation.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}invoiceAddress uses Python identifier invoiceAddress
    __invoiceAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invoiceAddress'), 'invoiceAddress', '__httpwww_opengis_netoseo1_0_CommonOrderSpecification_httpwww_opengis_netoseo1_0invoiceAddress', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 314, 3), )

    
    invoiceAddress = property(__invoiceAddress.value, __invoiceAddress.set, None, 'Address for sending the invoice.')

    
    # Element {http://www.opengis.net/oseo/1.0}packaging uses Python identifier packaging
    __packaging = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'packaging'), 'packaging', '__httpwww_opengis_netoseo1_0_CommonOrderSpecification_httpwww_opengis_netoseo1_0packaging', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 319, 3), )

    
    packaging = property(__packaging.value, __packaging.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}option uses Python identifier option
    __option = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'option'), 'option', '__httpwww_opengis_netoseo1_0_CommonOrderSpecification_httpwww_opengis_netoseo1_0option', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 320, 3), )

    
    option = property(__option.value, __option.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}orderType uses Python identifier orderType
    __orderType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderType'), 'orderType', '__httpwww_opengis_netoseo1_0_CommonOrderSpecification_httpwww_opengis_netoseo1_0orderType', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 329, 3), )

    
    orderType = property(__orderType.value, __orderType.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}orderReference uses Python identifier orderReference
    __orderReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderReference'), 'orderReference', '__httpwww_opengis_netoseo1_0_CommonOrderSpecification_httpwww_opengis_netoseo1_0orderReference', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1300, 1), )

    
    orderReference = property(__orderReference.value, __orderReference.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}deliveryOptions uses Python identifier deliveryOptions
    __deliveryOptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'deliveryOptions'), 'deliveryOptions', '__httpwww_opengis_netoseo1_0_CommonOrderSpecification_httpwww_opengis_netoseo1_0deliveryOptions', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1316, 1), )

    
    deliveryOptions = property(__deliveryOptions.value, __deliveryOptions.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}extension uses Python identifier extension
    __extension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extension'), 'extension', '__httpwww_opengis_netoseo1_0_CommonOrderSpecification_httpwww_opengis_netoseo1_0extension', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1318, 1), )

    
    extension = property(__extension.value, __extension.set, None, None)

    _ElementMap.update({
        __priority.name() : __priority,
        __orderRemark.name() : __orderRemark,
        __deliveryInformation.name() : __deliveryInformation,
        __invoiceAddress.name() : __invoiceAddress,
        __packaging.name() : __packaging,
        __option.name() : __option,
        __orderType.name() : __orderType,
        __orderReference.name() : __orderReference,
        __deliveryOptions.name() : __deliveryOptions,
        __extension.name() : __extension
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CommonOrderSpecification = CommonOrderSpecification
Namespace.addCategoryObject('typeBinding', 'CommonOrderSpecification', CommonOrderSpecification)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 321, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}ParameterData uses Python identifier ParameterData
    __ParameterData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ParameterData'), 'ParameterData', '__httpwww_opengis_netoseo1_0_CTD_ANON_14_httpwww_opengis_netoseo1_0ParameterData', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 565, 1), )

    
    ParameterData = property(__ParameterData.value, __ParameterData.set, None, None)

    _ElementMap.update({
        __ParameterData.name() : __ParameterData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type {http://www.opengis.net/oseo/1.0}CreditCardInfoType with content type ELEMENT_ONLY
class CreditCardInfoType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}CreditCardInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CreditCardInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 334, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}creditCardInstitute uses Python identifier creditCardInstitute
    __creditCardInstitute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'creditCardInstitute'), 'creditCardInstitute', '__httpwww_opengis_netoseo1_0_CreditCardInfoType_httpwww_opengis_netoseo1_0creditCardInstitute', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 336, 3), )

    
    creditCardInstitute = property(__creditCardInstitute.value, __creditCardInstitute.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}nameOnCard uses Python identifier nameOnCard
    __nameOnCard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nameOnCard'), 'nameOnCard', '__httpwww_opengis_netoseo1_0_CreditCardInfoType_httpwww_opengis_netoseo1_0nameOnCard', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 337, 3), )

    
    nameOnCard = property(__nameOnCard.value, __nameOnCard.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}cardNumber uses Python identifier cardNumber
    __cardNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cardNumber'), 'cardNumber', '__httpwww_opengis_netoseo1_0_CreditCardInfoType_httpwww_opengis_netoseo1_0cardNumber', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 338, 3), )

    
    cardNumber = property(__cardNumber.value, __cardNumber.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}expirationDate uses Python identifier expirationDate
    __expirationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expirationDate'), 'expirationDate', '__httpwww_opengis_netoseo1_0_CreditCardInfoType_httpwww_opengis_netoseo1_0expirationDate', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 339, 3), )

    
    expirationDate = property(__expirationDate.value, __expirationDate.set, None, None)

    _ElementMap.update({
        __creditCardInstitute.name() : __creditCardInstitute,
        __nameOnCard.name() : __nameOnCard,
        __cardNumber.name() : __cardNumber,
        __expirationDate.name() : __expirationDate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CreditCardInfoType = CreditCardInfoType
Namespace.addCategoryObject('typeBinding', 'CreditCardInfoType', CreditCardInfoType)


# Complex type {http://www.opengis.net/oseo/1.0}PaymentOptionSelectedValue with content type ELEMENT_ONLY
class PaymentOptionSelectedValue (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}PaymentOptionSelectedValue with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PaymentOptionSelectedValue')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 342, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}orderAccount uses Python identifier orderAccount
    __orderAccount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderAccount'), 'orderAccount', '__httpwww_opengis_netoseo1_0_PaymentOptionSelectedValue_httpwww_opengis_netoseo1_0orderAccount', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 346, 4), )

    
    orderAccount = property(__orderAccount.value, __orderAccount.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}creditCardInfo uses Python identifier creditCardInfo
    __creditCardInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'creditCardInfo'), 'creditCardInfo', '__httpwww_opengis_netoseo1_0_PaymentOptionSelectedValue_httpwww_opengis_netoseo1_0creditCardInfo', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 354, 4), )

    
    creditCardInfo = property(__creditCardInfo.value, __creditCardInfo.set, None, 'This element should be managed in more secure way')

    
    # Element {http://www.opengis.net/oseo/1.0}paymentMethod uses Python identifier paymentMethod
    __paymentMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paymentMethod'), 'paymentMethod', '__httpwww_opengis_netoseo1_0_PaymentOptionSelectedValue_httpwww_opengis_netoseo1_0paymentMethod', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1281, 1), )

    
    paymentMethod = property(__paymentMethod.value, __paymentMethod.set, None, 'Examples:\nquota, invoice, prepay (to be indicated for free products), deposit account, credit card, credit card previously supplied')

    _ElementMap.update({
        __orderAccount.name() : __orderAccount,
        __creditCardInfo.name() : __creditCardInfo,
        __paymentMethod.name() : __paymentMethod
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PaymentOptionSelectedValue = PaymentOptionSelectedValue
Namespace.addCategoryObject('typeBinding', 'PaymentOptionSelectedValue', PaymentOptionSelectedValue)


# Complex type {http://www.opengis.net/oseo/1.0}OrderSearchCriteriaType with content type ELEMENT_ONLY
class OrderSearchCriteriaType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}OrderSearchCriteriaType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrderSearchCriteriaType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 410, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}lastUpdate uses Python identifier lastUpdate
    __lastUpdate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastUpdate'), 'lastUpdate', '__httpwww_opengis_netoseo1_0_OrderSearchCriteriaType_httpwww_opengis_netoseo1_0lastUpdate', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 412, 3), )

    
    lastUpdate = property(__lastUpdate.value, __lastUpdate.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}lastUpdateEnd uses Python identifier lastUpdateEnd
    __lastUpdateEnd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastUpdateEnd'), 'lastUpdateEnd', '__httpwww_opengis_netoseo1_0_OrderSearchCriteriaType_httpwww_opengis_netoseo1_0lastUpdateEnd', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 413, 3), )

    
    lastUpdateEnd = property(__lastUpdateEnd.value, __lastUpdateEnd.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}orderStatus uses Python identifier orderStatus
    __orderStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderStatus'), 'orderStatus', '__httpwww_opengis_netoseo1_0_OrderSearchCriteriaType_httpwww_opengis_netoseo1_0orderStatus', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 414, 3), )

    
    orderStatus = property(__orderStatus.value, __orderStatus.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}orderReference uses Python identifier orderReference
    __orderReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderReference'), 'orderReference', '__httpwww_opengis_netoseo1_0_OrderSearchCriteriaType_httpwww_opengis_netoseo1_0orderReference', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1300, 1), )

    
    orderReference = property(__orderReference.value, __orderReference.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}extension uses Python identifier extension
    __extension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extension'), 'extension', '__httpwww_opengis_netoseo1_0_OrderSearchCriteriaType_httpwww_opengis_netoseo1_0extension', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1318, 1), )

    
    extension = property(__extension.value, __extension.set, None, None)

    _ElementMap.update({
        __lastUpdate.name() : __lastUpdate,
        __lastUpdateEnd.name() : __lastUpdateEnd,
        __orderStatus.name() : __orderStatus,
        __orderReference.name() : __orderReference,
        __extension.name() : __extension
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrderSearchCriteriaType = OrderSearchCriteriaType
Namespace.addCategoryObject('typeBinding', 'OrderSearchCriteriaType', OrderSearchCriteriaType)


# Complex type {http://www.opengis.net/oseo/1.0}CommonOrderItemType with content type ELEMENT_ONLY
class CommonOrderItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}CommonOrderItemType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommonOrderItemType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 422, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}orderItemRemark uses Python identifier orderItemRemark
    __orderItemRemark = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderItemRemark'), 'orderItemRemark', '__httpwww_opengis_netoseo1_0_CommonOrderItemType_httpwww_opengis_netoseo1_0orderItemRemark', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 426, 3), )

    
    orderItemRemark = property(__orderItemRemark.value, __orderItemRemark.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}option uses Python identifier option
    __option = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'option'), 'option', '__httpwww_opengis_netoseo1_0_CommonOrderItemType_httpwww_opengis_netoseo1_0option', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 433, 3), )

    
    option = property(__option.value, __option.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}sceneSelection uses Python identifier sceneSelection
    __sceneSelection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sceneSelection'), 'sceneSelection', '__httpwww_opengis_netoseo1_0_CommonOrderItemType_httpwww_opengis_netoseo1_0sceneSelection', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 440, 3), )

    
    sceneSelection = property(__sceneSelection.value, __sceneSelection.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}payment uses Python identifier payment
    __payment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'payment'), 'payment', '__httpwww_opengis_netoseo1_0_CommonOrderItemType_httpwww_opengis_netoseo1_0payment', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 448, 3), )

    
    payment = property(__payment.value, __payment.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}productId uses Python identifier productId
    __productId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productId'), 'productId', '__httpwww_opengis_netoseo1_0_CommonOrderItemType_httpwww_opengis_netoseo1_0productId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 526, 1), )

    
    productId = property(__productId.value, __productId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}taskingRequestId uses Python identifier taskingRequestId
    __taskingRequestId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taskingRequestId'), 'taskingRequestId', '__httpwww_opengis_netoseo1_0_CommonOrderItemType_httpwww_opengis_netoseo1_0taskingRequestId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 548, 1), )

    
    taskingRequestId = property(__taskingRequestId.value, __taskingRequestId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}subscriptionId uses Python identifier subscriptionId
    __subscriptionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subscriptionId'), 'subscriptionId', '__httpwww_opengis_netoseo1_0_CommonOrderItemType_httpwww_opengis_netoseo1_0subscriptionId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 549, 1), )

    
    subscriptionId = property(__subscriptionId.value, __subscriptionId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}itemId uses Python identifier itemId
    __itemId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'itemId'), 'itemId', '__httpwww_opengis_netoseo1_0_CommonOrderItemType_httpwww_opengis_netoseo1_0itemId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1270, 1), )

    
    itemId = property(__itemId.value, __itemId.set, None, 'string identifying the order item within the order.')

    
    # Element {http://www.opengis.net/oseo/1.0}productOrderOptionsId uses Python identifier productOrderOptionsId
    __productOrderOptionsId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productOrderOptionsId'), 'productOrderOptionsId', '__httpwww_opengis_netoseo1_0_CommonOrderItemType_httpwww_opengis_netoseo1_0productOrderOptionsId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1308, 1), )

    
    productOrderOptionsId = property(__productOrderOptionsId.value, __productOrderOptionsId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}deliveryOptions uses Python identifier deliveryOptions
    __deliveryOptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'deliveryOptions'), 'deliveryOptions', '__httpwww_opengis_netoseo1_0_CommonOrderItemType_httpwww_opengis_netoseo1_0deliveryOptions', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1316, 1), )

    
    deliveryOptions = property(__deliveryOptions.value, __deliveryOptions.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}extension uses Python identifier extension
    __extension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extension'), 'extension', '__httpwww_opengis_netoseo1_0_CommonOrderItemType_httpwww_opengis_netoseo1_0extension', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1318, 1), )

    
    extension = property(__extension.value, __extension.set, None, None)

    _ElementMap.update({
        __orderItemRemark.name() : __orderItemRemark,
        __option.name() : __option,
        __sceneSelection.name() : __sceneSelection,
        __payment.name() : __payment,
        __productId.name() : __productId,
        __taskingRequestId.name() : __taskingRequestId,
        __subscriptionId.name() : __subscriptionId,
        __itemId.name() : __itemId,
        __productOrderOptionsId.name() : __productOrderOptionsId,
        __deliveryOptions.name() : __deliveryOptions,
        __extension.name() : __extension
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CommonOrderItemType = CommonOrderItemType
Namespace.addCategoryObject('typeBinding', 'CommonOrderItemType', CommonOrderItemType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 434, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}ParameterData uses Python identifier ParameterData
    __ParameterData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ParameterData'), 'ParameterData', '__httpwww_opengis_netoseo1_0_CTD_ANON_15_httpwww_opengis_netoseo1_0ParameterData', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 565, 1), )

    
    ParameterData = property(__ParameterData.value, __ParameterData.set, None, None)

    _ElementMap.update({
        __ParameterData.name() : __ParameterData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 441, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}ParameterData uses Python identifier ParameterData
    __ParameterData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ParameterData'), 'ParameterData', '__httpwww_opengis_netoseo1_0_CTD_ANON_16_httpwww_opengis_netoseo1_0ParameterData', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 565, 1), )

    
    ParameterData = property(__ParameterData.value, __ParameterData.set, None, None)

    _ElementMap.update({
        __ParameterData.name() : __ParameterData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_16 = CTD_ANON_16


# Complex type {http://www.opengis.net/oseo/1.0}DeliveryOptionsType with content type ELEMENT_ONLY
class DeliveryOptionsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}DeliveryOptionsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeliveryOptionsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 457, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}onlineDataAccess uses Python identifier onlineDataAccess
    __onlineDataAccess = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'onlineDataAccess'), 'onlineDataAccess', '__httpwww_opengis_netoseo1_0_DeliveryOptionsType_httpwww_opengis_netoseo1_0onlineDataAccess', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 460, 4), )

    
    onlineDataAccess = property(__onlineDataAccess.value, __onlineDataAccess.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}onlineDataDelivery uses Python identifier onlineDataDelivery
    __onlineDataDelivery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'onlineDataDelivery'), 'onlineDataDelivery', '__httpwww_opengis_netoseo1_0_DeliveryOptionsType_httpwww_opengis_netoseo1_0onlineDataDelivery', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 467, 4), )

    
    onlineDataDelivery = property(__onlineDataDelivery.value, __onlineDataDelivery.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}mediaDelivery uses Python identifier mediaDelivery
    __mediaDelivery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mediaDelivery'), 'mediaDelivery', '__httpwww_opengis_netoseo1_0_DeliveryOptionsType_httpwww_opengis_netoseo1_0mediaDelivery', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 474, 4), )

    
    mediaDelivery = property(__mediaDelivery.value, __mediaDelivery.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}numberOfCopies uses Python identifier numberOfCopies
    __numberOfCopies = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'numberOfCopies'), 'numberOfCopies', '__httpwww_opengis_netoseo1_0_DeliveryOptionsType_httpwww_opengis_netoseo1_0numberOfCopies', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 491, 3), )

    
    numberOfCopies = property(__numberOfCopies.value, __numberOfCopies.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}productAnnotation uses Python identifier productAnnotation
    __productAnnotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productAnnotation'), 'productAnnotation', '__httpwww_opengis_netoseo1_0_DeliveryOptionsType_httpwww_opengis_netoseo1_0productAnnotation', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 492, 3), )

    
    productAnnotation = property(__productAnnotation.value, __productAnnotation.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}specialInstructions uses Python identifier specialInstructions
    __specialInstructions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'specialInstructions'), 'specialInstructions', '__httpwww_opengis_netoseo1_0_DeliveryOptionsType_httpwww_opengis_netoseo1_0specialInstructions', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 499, 3), )

    
    specialInstructions = property(__specialInstructions.value, __specialInstructions.set, None, None)

    _ElementMap.update({
        __onlineDataAccess.name() : __onlineDataAccess,
        __onlineDataDelivery.name() : __onlineDataDelivery,
        __mediaDelivery.name() : __mediaDelivery,
        __numberOfCopies.name() : __numberOfCopies,
        __productAnnotation.name() : __productAnnotation,
        __specialInstructions.name() : __specialInstructions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DeliveryOptionsType = DeliveryOptionsType
Namespace.addCategoryObject('typeBinding', 'DeliveryOptionsType', DeliveryOptionsType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 461, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'protocol'), 'protocol', '__httpwww_opengis_netoseo1_0_CTD_ANON_17_httpwww_opengis_netoseo1_0protocol', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1317, 1), )

    
    protocol = property(__protocol.value, __protocol.set, None, None)

    _ElementMap.update({
        __protocol.name() : __protocol
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_17 = CTD_ANON_17


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 468, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'protocol'), 'protocol', '__httpwww_opengis_netoseo1_0_CTD_ANON_18_httpwww_opengis_netoseo1_0protocol', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1317, 1), )

    
    protocol = property(__protocol.value, __protocol.set, None, None)

    _ElementMap.update({
        __protocol.name() : __protocol
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_18 = CTD_ANON_18


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 475, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}packageMedium uses Python identifier packageMedium
    __packageMedium = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'packageMedium'), 'packageMedium', '__httpwww_opengis_netoseo1_0_CTD_ANON_19_httpwww_opengis_netoseo1_0packageMedium', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 477, 7), )

    
    packageMedium = property(__packageMedium.value, __packageMedium.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}shippingInstructions uses Python identifier shippingInstructions
    __shippingInstructions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shippingInstructions'), 'shippingInstructions', '__httpwww_opengis_netoseo1_0_CTD_ANON_19_httpwww_opengis_netoseo1_0shippingInstructions', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 478, 7), )

    
    shippingInstructions = property(__shippingInstructions.value, __shippingInstructions.set, None, None)

    _ElementMap.update({
        __packageMedium.name() : __packageMedium,
        __shippingInstructions.name() : __shippingInstructions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_19 = CTD_ANON_19


# Complex type {http://www.opengis.net/oseo/1.0}OrderItemIdType with content type EMPTY
class OrderItemIdType (pyxb.binding.basis.complexTypeDefinition):
    """Root type of the hierarchy of order item identifiers"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrderItemIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 508, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrderItemIdType = OrderItemIdType
Namespace.addCategoryObject('typeBinding', 'OrderItemIdType', OrderItemIdType)


# Complex type {http://www.opengis.net/oseo/1.0}ParameterDataType with content type ELEMENT_ONLY
class ParameterDataType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}ParameterDataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ParameterDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 566, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}encoding uses Python identifier encoding
    __encoding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'encoding'), 'encoding', '__httpwww_opengis_netoseo1_0_ParameterDataType_httpwww_opengis_netoseo1_0encoding', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 568, 3), )

    
    encoding = property(__encoding.value, __encoding.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}values uses Python identifier values
    __values = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'values'), 'values', '__httpwww_opengis_netoseo1_0_ParameterDataType_httpwww_opengis_netoseo1_0values', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 569, 3), )

    
    values = property(__values.value, __values.set, None, None)

    _ElementMap.update({
        __encoding.name() : __encoding,
        __values.name() : __values
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ParameterDataType = ParameterDataType
Namespace.addCategoryObject('typeBinding', 'ParameterDataType', ParameterDataType)


# Complex type {http://www.opengis.net/oseo/1.0}CommonOrderOptionsType with content type ELEMENT_ONLY
class CommonOrderOptionsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}CommonOrderOptionsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommonOrderOptionsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 624, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httpwww_opengis_netoseo1_0_CommonOrderOptionsType_httpwww_opengis_netoseo1_0description', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 628, 3), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}orderType uses Python identifier orderType
    __orderType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderType'), 'orderType', '__httpwww_opengis_netoseo1_0_CommonOrderOptionsType_httpwww_opengis_netoseo1_0orderType', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 635, 3), )

    
    orderType = property(__orderType.value, __orderType.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}option uses Python identifier option
    __option = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'option'), 'option', '__httpwww_opengis_netoseo1_0_CommonOrderOptionsType_httpwww_opengis_netoseo1_0option', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 636, 3), )

    
    option = property(__option.value, __option.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}productDeliveryOptions uses Python identifier productDeliveryOptions
    __productDeliveryOptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productDeliveryOptions'), 'productDeliveryOptions', '__httpwww_opengis_netoseo1_0_CommonOrderOptionsType_httpwww_opengis_netoseo1_0productDeliveryOptions', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 637, 3), )

    
    productDeliveryOptions = property(__productDeliveryOptions.value, __productDeliveryOptions.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}orderOptionInfoURL uses Python identifier orderOptionInfoURL
    __orderOptionInfoURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderOptionInfoURL'), 'orderOptionInfoURL', '__httpwww_opengis_netoseo1_0_CommonOrderOptionsType_httpwww_opengis_netoseo1_0orderOptionInfoURL', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 670, 3), )

    
    orderOptionInfoURL = property(__orderOptionInfoURL.value, __orderOptionInfoURL.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}paymentOptions uses Python identifier paymentOptions
    __paymentOptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paymentOptions'), 'paymentOptions', '__httpwww_opengis_netoseo1_0_CommonOrderOptionsType_httpwww_opengis_netoseo1_0paymentOptions', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 671, 3), )

    
    paymentOptions = property(__paymentOptions.value, __paymentOptions.set, None, 'List of possible payment options for ordering the product. This element is not specified if the payment options are defined in the user profile.')

    
    # Element {http://www.opengis.net/oseo/1.0}sceneSelectionOption uses Python identifier sceneSelectionOption
    __sceneSelectionOption = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sceneSelectionOption'), 'sceneSelectionOption', '__httpwww_opengis_netoseo1_0_CommonOrderOptionsType_httpwww_opengis_netoseo1_0sceneSelectionOption', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 676, 3), )

    
    sceneSelectionOption = property(__sceneSelectionOption.value, __sceneSelectionOption.set, None, 'Each istance represents a valid combination of scene selection options parameters. Several istances are possible because different policies are possible for the same product (e.g. floating scene, floating pass, full pass)')

    
    # Element {http://www.opengis.net/oseo/1.0}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'identifier'), 'identifier', '__httpwww_opengis_netoseo1_0_CommonOrderOptionsType_httpwww_opengis_netoseo1_0identifier', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1269, 1), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}productOrderOptionsId uses Python identifier productOrderOptionsId
    __productOrderOptionsId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productOrderOptionsId'), 'productOrderOptionsId', '__httpwww_opengis_netoseo1_0_CommonOrderOptionsType_httpwww_opengis_netoseo1_0productOrderOptionsId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1308, 1), )

    
    productOrderOptionsId = property(__productOrderOptionsId.value, __productOrderOptionsId.set, None, None)

    _ElementMap.update({
        __description.name() : __description,
        __orderType.name() : __orderType,
        __option.name() : __option,
        __productDeliveryOptions.name() : __productDeliveryOptions,
        __orderOptionInfoURL.name() : __orderOptionInfoURL,
        __paymentOptions.name() : __paymentOptions,
        __sceneSelectionOption.name() : __sceneSelectionOption,
        __identifier.name() : __identifier,
        __productOrderOptionsId.name() : __productOrderOptionsId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CommonOrderOptionsType = CommonOrderOptionsType
Namespace.addCategoryObject('typeBinding', 'CommonOrderOptionsType', CommonOrderOptionsType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 638, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}onlineDataAccess uses Python identifier onlineDataAccess
    __onlineDataAccess = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'onlineDataAccess'), 'onlineDataAccess', '__httpwww_opengis_netoseo1_0_CTD_ANON_20_httpwww_opengis_netoseo1_0onlineDataAccess', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 640, 6), )

    
    onlineDataAccess = property(__onlineDataAccess.value, __onlineDataAccess.set, None, 'This option says that the Server will specify the URL for accessing the products via DescribeResultAccess operation.')

    
    # Element {http://www.opengis.net/oseo/1.0}onlineDataDelivery uses Python identifier onlineDataDelivery
    __onlineDataDelivery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'onlineDataDelivery'), 'onlineDataDelivery', '__httpwww_opengis_netoseo1_0_CTD_ANON_20_httpwww_opengis_netoseo1_0onlineDataDelivery', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 650, 6), )

    
    onlineDataDelivery = property(__onlineDataDelivery.value, __onlineDataDelivery.set, None, 'This option says that the URLs for deliverying the products are defined by the client. No DescribeResultAccess operation to be called.')

    
    # Element {http://www.opengis.net/oseo/1.0}mediaDelivery uses Python identifier mediaDelivery
    __mediaDelivery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mediaDelivery'), 'mediaDelivery', '__httpwww_opengis_netoseo1_0_CTD_ANON_20_httpwww_opengis_netoseo1_0mediaDelivery', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 660, 6), )

    
    mediaDelivery = property(__mediaDelivery.value, __mediaDelivery.set, None, None)

    _ElementMap.update({
        __onlineDataAccess.name() : __onlineDataAccess,
        __onlineDataDelivery.name() : __onlineDataDelivery,
        __mediaDelivery.name() : __mediaDelivery
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_20 = CTD_ANON_20


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """This option says that the Server will specify the URL for accessing the products via DescribeResultAccess operation."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 644, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'protocol'), 'protocol', '__httpwww_opengis_netoseo1_0_CTD_ANON_21_httpwww_opengis_netoseo1_0protocol', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1317, 1), )

    
    protocol = property(__protocol.value, __protocol.set, None, None)

    _ElementMap.update({
        __protocol.name() : __protocol
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_21 = CTD_ANON_21


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """This option says that the URLs for deliverying the products are defined by the client. No DescribeResultAccess operation to be called."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 654, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'protocol'), 'protocol', '__httpwww_opengis_netoseo1_0_CTD_ANON_22_httpwww_opengis_netoseo1_0protocol', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1317, 1), )

    
    protocol = property(__protocol.value, __protocol.set, None, None)

    _ElementMap.update({
        __protocol.name() : __protocol
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_22 = CTD_ANON_22


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 661, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}packageMedium uses Python identifier packageMedium
    __packageMedium = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'packageMedium'), 'packageMedium', '__httpwww_opengis_netoseo1_0_CTD_ANON_23_httpwww_opengis_netoseo1_0packageMedium', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 663, 9), )

    
    packageMedium = property(__packageMedium.value, __packageMedium.set, None, None)

    _ElementMap.update({
        __packageMedium.name() : __packageMedium
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_23 = CTD_ANON_23


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """Each istance represents a valid combination of scene selection options parameters. Several istances are possible because different policies are possible for the same product (e.g. floating scene, floating pass, full pass)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 680, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpwww_opengis_netoseo1_0_CTD_ANON_24_httpwww_opengis_netoseo1_0name', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 682, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httpwww_opengis_netoseo1_0_CTD_ANON_24_httpwww_opengis_netoseo1_0description', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 689, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}sceneSelectionParameter uses Python identifier sceneSelectionParameter
    __sceneSelectionParameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sceneSelectionParameter'), 'sceneSelectionParameter', '__httpwww_opengis_netoseo1_0_CTD_ANON_24_httpwww_opengis_netoseo1_0sceneSelectionParameter', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 696, 6), )

    
    sceneSelectionParameter = property(__sceneSelectionParameter.value, __sceneSelectionParameter.set, None, 'Each istance represents a scene selection parameter with its description and constraints. It is possible a sceneSelectionOption with no parameters because in some cases the product can be ordered in scenes or as it is. In the second case no scene selection parameters can be provided.')

    _ElementMap.update({
        __name.name() : __name,
        __description.name() : __description,
        __sceneSelectionParameter.name() : __sceneSelectionParameter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_24 = CTD_ANON_24


# Complex type {http://www.opengis.net/oseo/1.0}PaymentOptionDefinitionType with content type ELEMENT_ONLY
class PaymentOptionDefinitionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}PaymentOptionDefinitionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PaymentOptionDefinitionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 707, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}paymentOptionInfoURL uses Python identifier paymentOptionInfoURL
    __paymentOptionInfoURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paymentOptionInfoURL'), 'paymentOptionInfoURL', '__httpwww_opengis_netoseo1_0_PaymentOptionDefinitionType_httpwww_opengis_netoseo1_0paymentOptionInfoURL', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 710, 3), )

    
    paymentOptionInfoURL = property(__paymentOptionInfoURL.value, __paymentOptionInfoURL.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}paymentMethod uses Python identifier paymentMethod
    __paymentMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paymentMethod'), 'paymentMethod', '__httpwww_opengis_netoseo1_0_PaymentOptionDefinitionType_httpwww_opengis_netoseo1_0paymentMethod', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1281, 1), )

    
    paymentMethod = property(__paymentMethod.value, __paymentMethod.set, None, 'Examples:\nquota, invoice, prepay (to be indicated for free products), deposit account, credit card, credit card previously supplied')

    _ElementMap.update({
        __paymentOptionInfoURL.name() : __paymentOptionInfoURL,
        __paymentMethod.name() : __paymentMethod
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PaymentOptionDefinitionType = PaymentOptionDefinitionType
Namespace.addCategoryObject('typeBinding', 'PaymentOptionDefinitionType', PaymentOptionDefinitionType)


# Complex type {http://www.opengis.net/oseo/1.0}ParameterDescriptorType with content type ELEMENT_ONLY
class ParameterDescriptorType (pyxb.bundles.opengis.swe_2_0.AbstractDataComponentPropertyType):
    """Complex type {http://www.opengis.net/oseo/1.0}ParameterDescriptorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ParameterDescriptorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 713, 1)
    _ElementMap = pyxb.bundles.opengis.swe_2_0.AbstractDataComponentPropertyType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.swe_2_0.AbstractDataComponentPropertyType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.swe_2_0.AbstractDataComponentPropertyType
    
    # Element {http://www.opengis.net/oseo/1.0}grouping uses Python identifier grouping
    __grouping = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'grouping'), 'grouping', '__httpwww_opengis_netoseo1_0_ParameterDescriptorType_httpwww_opengis_netoseo1_0grouping', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 717, 5), )

    
    grouping = property(__grouping.value, __grouping.set, None, 'It identifies the group the option belong to e.g. processing option, etc.')

    
    # Element AbstractDataComponent ({http://www.opengis.net/swe/2.0}AbstractDataComponent) inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute type inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute href inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute role inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute arcrole inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute title inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute show inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute actuate inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    _ElementMap.update({
        __grouping.name() : __grouping
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ParameterDescriptorType = ParameterDescriptorType
Namespace.addCategoryObject('typeBinding', 'ParameterDescriptorType', ParameterDescriptorType)


# Complex type {http://www.opengis.net/oseo/1.0}SceneSelectionDescriptorType with content type ELEMENT_ONLY
class SceneSelectionDescriptorType (pyxb.bundles.opengis.swe_2_0.AbstractDataComponentPropertyType):
    """Complex type {http://www.opengis.net/oseo/1.0}SceneSelectionDescriptorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SceneSelectionDescriptorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 731, 1)
    _ElementMap = pyxb.bundles.opengis.swe_2_0.AbstractDataComponentPropertyType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.swe_2_0.AbstractDataComponentPropertyType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.swe_2_0.AbstractDataComponentPropertyType
    
    # Element {http://www.opengis.net/oseo/1.0}sceneRestriction uses Python identifier sceneRestriction
    __sceneRestriction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sceneRestriction'), 'sceneRestriction', '__httpwww_opengis_netoseo1_0_SceneSelectionDescriptorType_httpwww_opengis_netoseo1_0sceneRestriction', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 735, 5), )

    
    sceneRestriction = property(__sceneRestriction.value, __sceneRestriction.set, None, None)

    
    # Element AbstractDataComponent ({http://www.opengis.net/swe/2.0}AbstractDataComponent) inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute type inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute href inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute role inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute arcrole inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute title inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute show inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute actuate inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    _ElementMap.update({
        __sceneRestriction.name() : __sceneRestriction
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SceneSelectionDescriptorType = SceneSelectionDescriptorType
Namespace.addCategoryObject('typeBinding', 'SceneSelectionDescriptorType', SceneSelectionDescriptorType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25 (pyxb.bundles.opengis.swe_2_0.AbstractDataComponentPropertyType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 736, 6)
    _ElementMap = pyxb.bundles.opengis.swe_2_0.AbstractDataComponentPropertyType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.swe_2_0.AbstractDataComponentPropertyType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.swe_2_0.AbstractDataComponentPropertyType
    
    # Element AbstractDataComponent ({http://www.opengis.net/swe/2.0}AbstractDataComponent) inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute type inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute href inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute role inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute arcrole inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute title inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute show inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    
    # Attribute actuate inherited from {http://www.opengis.net/swe/2.0}AbstractDataComponentPropertyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_25 = CTD_ANON_25


# Complex type {http://www.opengis.net/oseo/1.0}OrderQuotation with content type ELEMENT_ONLY
class OrderQuotation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}OrderQuotation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrderQuotation')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 815, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}quotationId uses Python identifier quotationId
    __quotationId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'quotationId'), 'quotationId', '__httpwww_opengis_netoseo1_0_OrderQuotation_httpwww_opengis_netoseo1_0quotationId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 817, 3), )

    
    quotationId = property(__quotationId.value, __quotationId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}validityTime uses Python identifier validityTime
    __validityTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'validityTime'), 'validityTime', '__httpwww_opengis_netoseo1_0_OrderQuotation_httpwww_opengis_netoseo1_0validityTime', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 818, 3), )

    
    validityTime = property(__validityTime.value, __validityTime.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}price uses Python identifier price
    __price = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'price'), 'price', '__httpwww_opengis_netoseo1_0_OrderQuotation_httpwww_opengis_netoseo1_0price', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 819, 3), )

    
    price = property(__price.value, __price.set, None, 'Price of the whole order; mandatory unless the provider uses quota concept or products are free of charge.')

    
    # Element {http://www.opengis.net/oseo/1.0}orderItemGroupPrice uses Python identifier orderItemGroupPrice
    __orderItemGroupPrice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderItemGroupPrice'), 'orderItemGroupPrice', '__httpwww_opengis_netoseo1_0_OrderQuotation_httpwww_opengis_netoseo1_0orderItemGroupPrice', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 824, 3), )

    
    orderItemGroupPrice = property(__orderItemGroupPrice.value, __orderItemGroupPrice.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}contractInformation uses Python identifier contractInformation
    __contractInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contractInformation'), 'contractInformation', '__httpwww_opengis_netoseo1_0_OrderQuotation_httpwww_opengis_netoseo1_0contractInformation', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1293, 1), )

    
    contractInformation = property(__contractInformation.value, __contractInformation.set, None, None)

    _ElementMap.update({
        __quotationId.name() : __quotationId,
        __validityTime.name() : __validityTime,
        __price.name() : __price,
        __orderItemGroupPrice.name() : __orderItemGroupPrice,
        __contractInformation.name() : __contractInformation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrderQuotation = OrderQuotation
Namespace.addCategoryObject('typeBinding', 'OrderQuotation', OrderQuotation)


# Complex type {http://www.opengis.net/oseo/1.0}OrderItemGroupPrice with content type ELEMENT_ONLY
class OrderItemGroupPrice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}OrderItemGroupPrice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrderItemGroupPrice')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 828, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}provider uses Python identifier provider
    __provider = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'provider'), 'provider', '__httpwww_opengis_netoseo1_0_OrderItemGroupPrice_httpwww_opengis_netoseo1_0provider', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 830, 3), )

    
    provider = property(__provider.value, __provider.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}quotationId uses Python identifier quotationId
    __quotationId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'quotationId'), 'quotationId', '__httpwww_opengis_netoseo1_0_OrderItemGroupPrice_httpwww_opengis_netoseo1_0quotationId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 831, 3), )

    
    quotationId = property(__quotationId.value, __quotationId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}validityTime uses Python identifier validityTime
    __validityTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'validityTime'), 'validityTime', '__httpwww_opengis_netoseo1_0_OrderItemGroupPrice_httpwww_opengis_netoseo1_0validityTime', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 832, 3), )

    
    validityTime = property(__validityTime.value, __validityTime.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}price uses Python identifier price
    __price = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'price'), 'price', '__httpwww_opengis_netoseo1_0_OrderItemGroupPrice_httpwww_opengis_netoseo1_0price', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 833, 3), )

    
    price = property(__price.value, __price.set, None, 'Price of the whole order item gruop.')

    
    # Element {http://www.opengis.net/oseo/1.0}balance uses Python identifier balance
    __balance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'balance'), 'balance', '__httpwww_opengis_netoseo1_0_OrderItemGroupPrice_httpwww_opengis_netoseo1_0balance', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 838, 3), )

    
    balance = property(__balance.value, __balance.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}orderItemPrice uses Python identifier orderItemPrice
    __orderItemPrice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderItemPrice'), 'orderItemPrice', '__httpwww_opengis_netoseo1_0_OrderItemGroupPrice_httpwww_opengis_netoseo1_0orderItemPrice', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 839, 3), )

    
    orderItemPrice = property(__orderItemPrice.value, __orderItemPrice.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}contractInformation uses Python identifier contractInformation
    __contractInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contractInformation'), 'contractInformation', '__httpwww_opengis_netoseo1_0_OrderItemGroupPrice_httpwww_opengis_netoseo1_0contractInformation', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1293, 1), )

    
    contractInformation = property(__contractInformation.value, __contractInformation.set, None, None)

    _ElementMap.update({
        __provider.name() : __provider,
        __quotationId.name() : __quotationId,
        __validityTime.name() : __validityTime,
        __price.name() : __price,
        __balance.name() : __balance,
        __orderItemPrice.name() : __orderItemPrice,
        __contractInformation.name() : __contractInformation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrderItemGroupPrice = OrderItemGroupPrice
Namespace.addCategoryObject('typeBinding', 'OrderItemGroupPrice', OrderItemGroupPrice)


# Complex type {http://www.opengis.net/oseo/1.0}OrderItemPrice with content type ELEMENT_ONLY
class OrderItemPrice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}OrderItemPrice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrderItemPrice')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 843, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}productId uses Python identifier productId
    __productId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productId'), 'productId', '__httpwww_opengis_netoseo1_0_OrderItemPrice_httpwww_opengis_netoseo1_0productId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 526, 1), )

    
    productId = property(__productId.value, __productId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}taskingRequestId uses Python identifier taskingRequestId
    __taskingRequestId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taskingRequestId'), 'taskingRequestId', '__httpwww_opengis_netoseo1_0_OrderItemPrice_httpwww_opengis_netoseo1_0taskingRequestId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 548, 1), )

    
    taskingRequestId = property(__taskingRequestId.value, __taskingRequestId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}subscriptionId uses Python identifier subscriptionId
    __subscriptionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subscriptionId'), 'subscriptionId', '__httpwww_opengis_netoseo1_0_OrderItemPrice_httpwww_opengis_netoseo1_0subscriptionId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 549, 1), )

    
    subscriptionId = property(__subscriptionId.value, __subscriptionId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}price uses Python identifier price
    __price = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'price'), 'price', '__httpwww_opengis_netoseo1_0_OrderItemPrice_httpwww_opengis_netoseo1_0price', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 855, 3), )

    
    price = property(__price.value, __price.set, None, 'Price of the item; is optional if the price at group level is provided; not supported in case the products are free of charge.')

    
    # Element {http://www.opengis.net/oseo/1.0}priceInformation uses Python identifier priceInformation
    __priceInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'priceInformation'), 'priceInformation', '__httpwww_opengis_netoseo1_0_OrderItemPrice_httpwww_opengis_netoseo1_0priceInformation', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 860, 3), )

    
    priceInformation = property(__priceInformation.value, __priceInformation.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}itemId uses Python identifier itemId
    __itemId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'itemId'), 'itemId', '__httpwww_opengis_netoseo1_0_OrderItemPrice_httpwww_opengis_netoseo1_0itemId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1270, 1), )

    
    itemId = property(__itemId.value, __itemId.set, None, 'string identifying the order item within the order.')

    
    # Element {http://www.opengis.net/oseo/1.0}contractInformation uses Python identifier contractInformation
    __contractInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contractInformation'), 'contractInformation', '__httpwww_opengis_netoseo1_0_OrderItemPrice_httpwww_opengis_netoseo1_0contractInformation', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1293, 1), )

    
    contractInformation = property(__contractInformation.value, __contractInformation.set, None, None)

    _ElementMap.update({
        __productId.name() : __productId,
        __taskingRequestId.name() : __taskingRequestId,
        __subscriptionId.name() : __subscriptionId,
        __price.name() : __price,
        __priceInformation.name() : __priceInformation,
        __itemId.name() : __itemId,
        __contractInformation.name() : __contractInformation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrderItemPrice = OrderItemPrice
Namespace.addCategoryObject('typeBinding', 'OrderItemPrice', OrderItemPrice)


# Complex type {http://www.opengis.net/oseo/1.0}CurrencyType with content type ELEMENT_ONLY
class CurrencyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}CurrencyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurrencyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 870, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__httpwww_opengis_netoseo1_0_CurrencyType_httpwww_opengis_netoseo1_0value', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 872, 3), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}currency uses Python identifier currency
    __currency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'currency'), 'currency', '__httpwww_opengis_netoseo1_0_CurrencyType_httpwww_opengis_netoseo1_0currency', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 873, 3), )

    
    currency = property(__currency.value, __currency.set, None, 'Currency including ISO 4217 (e.g.: EUR, USD (US Dollar), CAD (Canada Dollar), AUD (Australia Dollar), GBP (United Kindom Pounds), etc.) and also special values for representing quota.')

    _ElementMap.update({
        __value.name() : __value,
        __currency.name() : __currency
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CurrencyType = CurrencyType
Namespace.addCategoryObject('typeBinding', 'CurrencyType', CurrencyType)


# Complex type {http://www.opengis.net/oseo/1.0}ProviderType with content type ELEMENT_ONLY
class ProviderType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}ProviderType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProviderType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 885, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}serviceName uses Python identifier serviceName
    __serviceName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'serviceName'), 'serviceName', '__httpwww_opengis_netoseo1_0_ProviderType_httpwww_opengis_netoseo1_0serviceName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 887, 3), )

    
    serviceName = property(__serviceName.value, __serviceName.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}organization uses Python identifier organization
    __organization = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'organization'), 'organization', '__httpwww_opengis_netoseo1_0_ProviderType_httpwww_opengis_netoseo1_0organization', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 894, 3), )

    
    organization = property(__organization.value, __organization.set, None, None)

    _ElementMap.update({
        __serviceName.name() : __serviceName,
        __organization.name() : __organization
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProviderType = ProviderType
Namespace.addCategoryObject('typeBinding', 'ProviderType', ProviderType)


# Complex type {http://www.opengis.net/oseo/1.0}StatusType with content type ELEMENT_ONLY
class StatusType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}StatusType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StatusType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 952, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__httpwww_opengis_netoseo1_0_StatusType_httpwww_opengis_netoseo1_0status', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 954, 3), )

    
    status = property(__status.value, __status.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}additionalStatusInfo uses Python identifier additionalStatusInfo
    __additionalStatusInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'additionalStatusInfo'), 'additionalStatusInfo', '__httpwww_opengis_netoseo1_0_StatusType_httpwww_opengis_netoseo1_0additionalStatusInfo', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 955, 3), )

    
    additionalStatusInfo = property(__additionalStatusInfo.value, __additionalStatusInfo.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}missionSpecificStatusInfo uses Python identifier missionSpecificStatusInfo
    __missionSpecificStatusInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'missionSpecificStatusInfo'), 'missionSpecificStatusInfo', '__httpwww_opengis_netoseo1_0_StatusType_httpwww_opengis_netoseo1_0missionSpecificStatusInfo', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 963, 3), )

    
    missionSpecificStatusInfo = property(__missionSpecificStatusInfo.value, __missionSpecificStatusInfo.set, None, None)

    _ElementMap.update({
        __status.name() : __status,
        __additionalStatusInfo.name() : __additionalStatusInfo,
        __missionSpecificStatusInfo.name() : __missionSpecificStatusInfo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StatusType = StatusType
Namespace.addCategoryObject('typeBinding', 'StatusType', StatusType)


# Complex type {http://www.opengis.net/oseo/1.0}DeliveryInformationType with content type ELEMENT_ONLY
class DeliveryInformationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}DeliveryInformationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeliveryInformationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 972, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}onlineAddress uses Python identifier onlineAddress
    __onlineAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'onlineAddress'), 'onlineAddress', '__httpwww_opengis_netoseo1_0_DeliveryInformationType_httpwww_opengis_netoseo1_0onlineAddress', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 974, 3), )

    
    onlineAddress = property(__onlineAddress.value, __onlineAddress.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}mailAddress uses Python identifier mailAddress
    __mailAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mailAddress'), 'mailAddress', '__httpwww_opengis_netoseo1_0_DeliveryInformationType_httpwww_opengis_netoseo1_0mailAddress', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 975, 3), )

    
    mailAddress = property(__mailAddress.value, __mailAddress.set, None, None)

    _ElementMap.update({
        __onlineAddress.name() : __onlineAddress,
        __mailAddress.name() : __mailAddress
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DeliveryInformationType = DeliveryInformationType
Namespace.addCategoryObject('typeBinding', 'DeliveryInformationType', DeliveryInformationType)


# Complex type {http://www.opengis.net/oseo/1.0}DeliveryAddressType with content type ELEMENT_ONLY
class DeliveryAddressType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}DeliveryAddressType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeliveryAddressType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 978, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'firstName'), 'firstName', '__httpwww_opengis_netoseo1_0_DeliveryAddressType_httpwww_opengis_netoseo1_0firstName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 980, 3), )

    
    firstName = property(__firstName.value, __firstName.set, None, 'FirstName to identify the receiving person')

    
    # Element {http://www.opengis.net/oseo/1.0}lastName uses Python identifier lastName
    __lastName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastName'), 'lastName', '__httpwww_opengis_netoseo1_0_DeliveryAddressType_httpwww_opengis_netoseo1_0lastName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 991, 3), )

    
    lastName = property(__lastName.value, __lastName.set, None, 'Last Name to identify the receiving person')

    
    # Element {http://www.opengis.net/oseo/1.0}companyRef uses Python identifier companyRef
    __companyRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'companyRef'), 'companyRef', '__httpwww_opengis_netoseo1_0_DeliveryAddressType_httpwww_opengis_netoseo1_0companyRef', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1002, 3), )

    
    companyRef = property(__companyRef.value, __companyRef.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}postalAddress uses Python identifier postalAddress
    __postalAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'postalAddress'), 'postalAddress', '__httpwww_opengis_netoseo1_0_DeliveryAddressType_httpwww_opengis_netoseo1_0postalAddress', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1010, 3), )

    
    postalAddress = property(__postalAddress.value, __postalAddress.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}telephoneNumber uses Python identifier telephoneNumber
    __telephoneNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'telephoneNumber'), 'telephoneNumber', '__httpwww_opengis_netoseo1_0_DeliveryAddressType_httpwww_opengis_netoseo1_0telephoneNumber', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1061, 3), )

    
    telephoneNumber = property(__telephoneNumber.value, __telephoneNumber.set, None, 'including country code, prefix, without special sign or intermediate blanks')

    
    # Element {http://www.opengis.net/oseo/1.0}facsimileTelephoneNumber uses Python identifier facsimileTelephoneNumber
    __facsimileTelephoneNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'facsimileTelephoneNumber'), 'facsimileTelephoneNumber', '__httpwww_opengis_netoseo1_0_DeliveryAddressType_httpwww_opengis_netoseo1_0facsimileTelephoneNumber', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1072, 3), )

    
    facsimileTelephoneNumber = property(__facsimileTelephoneNumber.value, __facsimileTelephoneNumber.set, None, 'including country code, prefix, without special sign or intermediate blanks')

    _ElementMap.update({
        __firstName.name() : __firstName,
        __lastName.name() : __lastName,
        __companyRef.name() : __companyRef,
        __postalAddress.name() : __postalAddress,
        __telephoneNumber.name() : __telephoneNumber,
        __facsimileTelephoneNumber.name() : __facsimileTelephoneNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DeliveryAddressType = DeliveryAddressType
Namespace.addCategoryObject('typeBinding', 'DeliveryAddressType', DeliveryAddressType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1011, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}streetAddress uses Python identifier streetAddress
    __streetAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetAddress'), 'streetAddress', '__httpwww_opengis_netoseo1_0_CTD_ANON_26_httpwww_opengis_netoseo1_0streetAddress', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1013, 6), )

    
    streetAddress = property(__streetAddress.value, __streetAddress.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__httpwww_opengis_netoseo1_0_CTD_ANON_26_httpwww_opengis_netoseo1_0city', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1020, 6), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'state'), 'state', '__httpwww_opengis_netoseo1_0_CTD_ANON_26_httpwww_opengis_netoseo1_0state', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1027, 6), )

    
    state = property(__state.value, __state.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}postalCode uses Python identifier postalCode
    __postalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'postalCode'), 'postalCode', '__httpwww_opengis_netoseo1_0_CTD_ANON_26_httpwww_opengis_netoseo1_0postalCode', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1034, 6), )

    
    postalCode = property(__postalCode.value, __postalCode.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'country'), 'country', '__httpwww_opengis_netoseo1_0_CTD_ANON_26_httpwww_opengis_netoseo1_0country', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1041, 6), )

    
    country = property(__country.value, __country.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}postBox uses Python identifier postBox
    __postBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'postBox'), 'postBox', '__httpwww_opengis_netoseo1_0_CTD_ANON_26_httpwww_opengis_netoseo1_0postBox', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1048, 6), )

    
    postBox = property(__postBox.value, __postBox.set, None, 'only number part, only digits allowed')

    _ElementMap.update({
        __streetAddress.name() : __streetAddress,
        __city.name() : __city,
        __state.name() : __state,
        __postalCode.name() : __postalCode,
        __country.name() : __country,
        __postBox.name() : __postBox
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_26 = CTD_ANON_26


# Complex type {http://www.opengis.net/oseo/1.0}OnlineAddressType with content type ELEMENT_ONLY
class OnlineAddressType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}OnlineAddressType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OnlineAddressType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1116, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}serverAddress uses Python identifier serverAddress
    __serverAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'serverAddress'), 'serverAddress', '__httpwww_opengis_netoseo1_0_OnlineAddressType_httpwww_opengis_netoseo1_0serverAddress', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1119, 3), )

    
    serverAddress = property(__serverAddress.value, __serverAddress.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}userName uses Python identifier userName
    __userName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'userName'), 'userName', '__httpwww_opengis_netoseo1_0_OnlineAddressType_httpwww_opengis_netoseo1_0userName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1126, 3), )

    
    userName = property(__userName.value, __userName.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}userPassword uses Python identifier userPassword
    __userPassword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'userPassword'), 'userPassword', '__httpwww_opengis_netoseo1_0_OnlineAddressType_httpwww_opengis_netoseo1_0userPassword', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1133, 3), )

    
    userPassword = property(__userPassword.value, __userPassword.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}path uses Python identifier path
    __path = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'path'), 'path', '__httpwww_opengis_netoseo1_0_OnlineAddressType_httpwww_opengis_netoseo1_0path', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1140, 3), )

    
    path = property(__path.value, __path.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'protocol'), 'protocol', '__httpwww_opengis_netoseo1_0_OnlineAddressType_httpwww_opengis_netoseo1_0protocol', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1317, 1), )

    
    protocol = property(__protocol.value, __protocol.set, None, None)

    _ElementMap.update({
        __serverAddress.name() : __serverAddress,
        __userName.name() : __userName,
        __userPassword.name() : __userPassword,
        __path.name() : __path,
        __protocol.name() : __protocol
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OnlineAddressType = OnlineAddressType
Namespace.addCategoryObject('typeBinding', 'OnlineAddressType', OnlineAddressType)


# Complex type {http://www.opengis.net/oseo/1.0}OnLineAccessAddressType with content type ELEMENT_ONLY
class OnLineAccessAddressType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}OnLineAccessAddressType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OnLineAccessAddressType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1149, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}ServiceAddress uses Python identifier ServiceAddress
    __ServiceAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceAddress'), 'ServiceAddress', '__httpwww_opengis_netoseo1_0_OnLineAccessAddressType_httpwww_opengis_netoseo1_0ServiceAddress', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1151, 3), )

    
    ServiceAddress = property(__ServiceAddress.value, __ServiceAddress.set, None, 'Address information related to the Server hosting the item to be accessed.')

    
    # Element {http://www.opengis.net/oseo/1.0}ResourceAddress uses Python identifier ResourceAddress
    __ResourceAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResourceAddress'), 'ResourceAddress', '__httpwww_opengis_netoseo1_0_OnLineAccessAddressType_httpwww_opengis_netoseo1_0ResourceAddress', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1185, 3), )

    
    ResourceAddress = property(__ResourceAddress.value, __ResourceAddress.set, None, 'Address information of the resource to be accessed.')

    _ElementMap.update({
        __ServiceAddress.name() : __ServiceAddress,
        __ResourceAddress.name() : __ResourceAddress
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OnLineAccessAddressType = OnLineAccessAddressType
Namespace.addCategoryObject('typeBinding', 'OnLineAccessAddressType', OnLineAccessAddressType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    """Address information related to the Server hosting the item to be accessed."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1155, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__httpwww_opengis_netoseo1_0_CTD_ANON_27_httpwww_opengis_netoseo1_0type', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1157, 6), )

    
    type = property(__type.value, __type.set, None, 'It specifies the type of the service hosting the resource e.g. WCS, WMS, etc. This field is optional, since full information about the server can be retrieved from info_URL and infoRequest elements.')

    
    # Element {http://www.opengis.net/oseo/1.0}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'URL'), 'URL', '__httpwww_opengis_netoseo1_0_CTD_ANON_27_httpwww_opengis_netoseo1_0URL', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1162, 6), )

    
    URL = property(__URL.value, __URL.set, None, 'Address of the Server')

    
    # Element {http://www.opengis.net/oseo/1.0}info_URL uses Python identifier info_URL
    __info_URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'info_URL'), 'info_URL', '__httpwww_opengis_netoseo1_0_CTD_ANON_27_httpwww_opengis_netoseo1_0info_URL', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1167, 6), )

    
    info_URL = property(__info_URL.value, __info_URL.set, None, 'Address for getting information about the server. In case of OGC Web Services it can refer to GetCapabilities operation with HTTP GET binding.')

    
    # Element {http://www.opengis.net/oseo/1.0}infoRequest uses Python identifier infoRequest
    __infoRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'infoRequest'), 'infoRequest', '__httpwww_opengis_netoseo1_0_CTD_ANON_27_httpwww_opengis_netoseo1_0infoRequest', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1172, 6), )

    
    infoRequest = property(__infoRequest.value, __infoRequest.set, None, 'In case the information can be retrieved by sending a request message, this field stores the message to be sent. In case of OGC Web Services supporitng SOAP GetCapabilities, this field specifies the GetCapabilities message to send at the address specified in info_URL element.')

    _ElementMap.update({
        __type.name() : __type,
        __URL.name() : __URL,
        __info_URL.name() : __info_URL,
        __infoRequest.name() : __infoRequest
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_27 = CTD_ANON_27


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_28 (pyxb.binding.basis.complexTypeDefinition):
    """In case the information can be retrieved by sending a request message, this field stores the message to be sent. In case of OGC Web Services supporitng SOAP GetCapabilities, this field specifies the GetCapabilities message to send at the address specified in info_URL element."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1176, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_28 = CTD_ANON_28


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_29 (pyxb.binding.basis.complexTypeDefinition):
    """Address information of the resource to be accessed."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1189, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'URL'), 'URL', '__httpwww_opengis_netoseo1_0_CTD_ANON_29_httpwww_opengis_netoseo1_0URL', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1191, 6), )

    
    URL = property(__URL.value, __URL.set, None, 'URL for accessing the resource.')

    
    # Element {http://www.opengis.net/oseo/1.0}serviceRequest uses Python identifier serviceRequest
    __serviceRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'serviceRequest'), 'serviceRequest', '__httpwww_opengis_netoseo1_0_CTD_ANON_29_httpwww_opengis_netoseo1_0serviceRequest', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1196, 6), )

    
    serviceRequest = property(__serviceRequest.value, __serviceRequest.set, None, 'In case the resource cannot be accessed simply via the URL, but a message needs to be sent, then this field specifies the message to send.')

    _ElementMap.update({
        __URL.name() : __URL,
        __serviceRequest.name() : __serviceRequest
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_29 = CTD_ANON_29


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_30 (pyxb.binding.basis.complexTypeDefinition):
    """In case the resource cannot be accessed simply via the URL, but a message needs to be sent, then this field specifies the message to send."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1200, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_30 = CTD_ANON_30


# Complex type {http://www.opengis.net/oseo/1.0}ItemURLType with content type ELEMENT_ONLY
class ItemURLType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/oseo/1.0}ItemURLType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ItemURLType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1211, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/oseo/1.0}productId uses Python identifier productId
    __productId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productId'), 'productId', '__httpwww_opengis_netoseo1_0_ItemURLType_httpwww_opengis_netoseo1_0productId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 526, 1), )

    
    productId = property(__productId.value, __productId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}itemAddress uses Python identifier itemAddress
    __itemAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'itemAddress'), 'itemAddress', '__httpwww_opengis_netoseo1_0_ItemURLType_httpwww_opengis_netoseo1_0itemAddress', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1215, 3), )

    
    itemAddress = property(__itemAddress.value, __itemAddress.set, None, 'This field specifies the full information for accessing the ordered item.')

    
    # Element {http://www.opengis.net/oseo/1.0}expirationDate uses Python identifier expirationDate
    __expirationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expirationDate'), 'expirationDate', '__httpwww_opengis_netoseo1_0_ItemURLType_httpwww_opengis_netoseo1_0expirationDate', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1220, 3), )

    
    expirationDate = property(__expirationDate.value, __expirationDate.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}itemId uses Python identifier itemId
    __itemId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'itemId'), 'itemId', '__httpwww_opengis_netoseo1_0_ItemURLType_httpwww_opengis_netoseo1_0itemId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1270, 1), )

    
    itemId = property(__itemId.value, __itemId.set, None, 'string identifying the order item within the order.')

    _ElementMap.update({
        __productId.name() : __productId,
        __itemAddress.name() : __itemAddress,
        __expirationDate.name() : __expirationDate,
        __itemId.name() : __itemId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ItemURLType = ItemURLType
Namespace.addCategoryObject('typeBinding', 'ItemURLType', ItemURLType)


# Complex type {http://www.opengis.net/oseo/1.0}OrderRequestBaseType with content type EMPTY
class OrderRequestBaseType (pyxb.binding.basis.complexTypeDefinition):
    """XML encoded SPS operation request base, for all operations except Get Capabilities. In this XML encoding, no "request" parameter is included, since the element name specifies the specific operation. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrderRequestBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 106, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__httpwww_opengis_netoseo1_0_OrderRequestBaseType_service', pyxb.binding.datatypes.string, fixed=True, unicode_default='OS', required=True)
    __service._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 110, 2)
    __service._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 110, 2)
    
    service = property(__service.value, __service.set, None, 'Service type identifier. ')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netoseo1_0_OrderRequestBaseType_version', _module_typeBindings.STD_ANON_2, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 115, 2)
    __version._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 115, 2)
    
    version = property(__version.value, __version.set, None, 'Specification version for SPS version and operation.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __service.name() : __service,
        __version.name() : __version
    })
_module_typeBindings.OrderRequestBaseType = OrderRequestBaseType
Namespace.addCategoryObject('typeBinding', 'OrderRequestBaseType', OrderRequestBaseType)


# Complex type {http://www.opengis.net/oseo/1.0}SubmitOrderResponseType with content type ELEMENT_ONLY
class SubmitOrderResponseType (OrderResponseBaseType):
    """Complex type {http://www.opengis.net/oseo/1.0}SubmitOrderResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SubmitOrderResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 283, 1)
    _ElementMap = OrderResponseBaseType._ElementMap.copy()
    _AttributeMap = OrderResponseBaseType._AttributeMap.copy()
    # Base type is OrderResponseBaseType
    
    # Element {http://www.opengis.net/oseo/1.0}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderId'), 'orderId', '__httpwww_opengis_netoseo1_0_SubmitOrderResponseType_httpwww_opengis_netoseo1_0orderId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 84, 1), )

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element status ({http://www.opengis.net/oseo/1.0}status) inherited from {http://www.opengis.net/oseo/1.0}OrderResponseBaseType
    
    # Element errorMessage ({http://www.opengis.net/oseo/1.0}errorMessage) inherited from {http://www.opengis.net/oseo/1.0}OrderResponseBaseType
    
    # Element {http://www.opengis.net/oseo/1.0}orderReference uses Python identifier orderReference
    __orderReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderReference'), 'orderReference', '__httpwww_opengis_netoseo1_0_SubmitOrderResponseType_httpwww_opengis_netoseo1_0orderReference', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1300, 1), )

    
    orderReference = property(__orderReference.value, __orderReference.set, None, None)

    _ElementMap.update({
        __orderId.name() : __orderId,
        __orderReference.name() : __orderReference
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SubmitOrderResponseType = SubmitOrderResponseType
Namespace.addCategoryObject('typeBinding', 'SubmitOrderResponseType', SubmitOrderResponseType)


# Complex type {http://www.opengis.net/oseo/1.0}OrderSpecification with content type ELEMENT_ONLY
class OrderSpecification (CommonOrderSpecification):
    """Complex type {http://www.opengis.net/oseo/1.0}OrderSpecification with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrderSpecification')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 293, 1)
    _ElementMap = CommonOrderSpecification._ElementMap.copy()
    _AttributeMap = CommonOrderSpecification._AttributeMap.copy()
    # Base type is CommonOrderSpecification
    
    # Element priority ({http://www.opengis.net/oseo/1.0}priority) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element {http://www.opengis.net/oseo/1.0}orderItem uses Python identifier orderItem
    __orderItem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderItem'), 'orderItem', '__httpwww_opengis_netoseo1_0_OrderSpecification_httpwww_opengis_netoseo1_0orderItem', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 297, 5), )

    
    orderItem = property(__orderItem.value, __orderItem.set, None, None)

    
    # Element orderRemark ({http://www.opengis.net/oseo/1.0}orderRemark) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element deliveryInformation ({http://www.opengis.net/oseo/1.0}deliveryInformation) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element invoiceAddress ({http://www.opengis.net/oseo/1.0}invoiceAddress) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element packaging ({http://www.opengis.net/oseo/1.0}packaging) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element option ({http://www.opengis.net/oseo/1.0}option) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element orderType ({http://www.opengis.net/oseo/1.0}orderType) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element orderReference ({http://www.opengis.net/oseo/1.0}orderReference) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element deliveryOptions ({http://www.opengis.net/oseo/1.0}deliveryOptions) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element extension ({http://www.opengis.net/oseo/1.0}extension) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    _ElementMap.update({
        __orderItem.name() : __orderItem
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrderSpecification = OrderSpecification
Namespace.addCategoryObject('typeBinding', 'OrderSpecification', OrderSpecification)


# Complex type {http://www.opengis.net/oseo/1.0}GetStatusResponseType with content type ELEMENT_ONLY
class GetStatusResponseType (OrderResponseBaseType):
    """Complex type {http://www.opengis.net/oseo/1.0}GetStatusResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetStatusResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 384, 1)
    _ElementMap = OrderResponseBaseType._ElementMap.copy()
    _AttributeMap = OrderResponseBaseType._AttributeMap.copy()
    # Base type is OrderResponseBaseType
    
    # Element status ({http://www.opengis.net/oseo/1.0}status) inherited from {http://www.opengis.net/oseo/1.0}OrderResponseBaseType
    
    # Element errorMessage ({http://www.opengis.net/oseo/1.0}errorMessage) inherited from {http://www.opengis.net/oseo/1.0}OrderResponseBaseType
    
    # Element {http://www.opengis.net/oseo/1.0}orderMonitorSpecification uses Python identifier orderMonitorSpecification
    __orderMonitorSpecification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderMonitorSpecification'), 'orderMonitorSpecification', '__httpwww_opengis_netoseo1_0_GetStatusResponseType_httpwww_opengis_netoseo1_0orderMonitorSpecification', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 409, 1), )

    
    orderMonitorSpecification = property(__orderMonitorSpecification.value, __orderMonitorSpecification.set, None, None)

    _ElementMap.update({
        __orderMonitorSpecification.name() : __orderMonitorSpecification
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GetStatusResponseType = GetStatusResponseType
Namespace.addCategoryObject('typeBinding', 'GetStatusResponseType', GetStatusResponseType)


# Complex type {http://www.opengis.net/oseo/1.0}CommonOrderMonitorSpecification with content type ELEMENT_ONLY
class CommonOrderMonitorSpecification (CommonOrderSpecification):
    """Complex type {http://www.opengis.net/oseo/1.0}CommonOrderMonitorSpecification with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommonOrderMonitorSpecification')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 393, 1)
    _ElementMap = CommonOrderSpecification._ElementMap.copy()
    _AttributeMap = CommonOrderSpecification._AttributeMap.copy()
    # Base type is CommonOrderSpecification
    
    # Element {http://www.opengis.net/oseo/1.0}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderId'), 'orderId', '__httpwww_opengis_netoseo1_0_CommonOrderMonitorSpecification_httpwww_opengis_netoseo1_0orderId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 84, 1), )

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element priority ({http://www.opengis.net/oseo/1.0}priority) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element orderRemark ({http://www.opengis.net/oseo/1.0}orderRemark) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element deliveryInformation ({http://www.opengis.net/oseo/1.0}deliveryInformation) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element invoiceAddress ({http://www.opengis.net/oseo/1.0}invoiceAddress) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element packaging ({http://www.opengis.net/oseo/1.0}packaging) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element option ({http://www.opengis.net/oseo/1.0}option) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element orderType ({http://www.opengis.net/oseo/1.0}orderType) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element {http://www.opengis.net/oseo/1.0}orderStatusInfo uses Python identifier orderStatusInfo
    __orderStatusInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderStatusInfo'), 'orderStatusInfo', '__httpwww_opengis_netoseo1_0_CommonOrderMonitorSpecification_httpwww_opengis_netoseo1_0orderStatusInfo', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 398, 5), )

    
    orderStatusInfo = property(__orderStatusInfo.value, __orderStatusInfo.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}orderDateTime uses Python identifier orderDateTime
    __orderDateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderDateTime'), 'orderDateTime', '__httpwww_opengis_netoseo1_0_CommonOrderMonitorSpecification_httpwww_opengis_netoseo1_0orderDateTime', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 399, 5), )

    
    orderDateTime = property(__orderDateTime.value, __orderDateTime.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}orderItem uses Python identifier orderItem
    __orderItem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderItem'), 'orderItem', '__httpwww_opengis_netoseo1_0_CommonOrderMonitorSpecification_httpwww_opengis_netoseo1_0orderItem', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 400, 5), )

    
    orderItem = property(__orderItem.value, __orderItem.set, None, 'The orderItem has been defined optional in order to  perform GetStatus request with brief presentation. Of course orders without order items cannot be submitted.')

    
    # Element orderReference ({http://www.opengis.net/oseo/1.0}orderReference) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element deliveryOptions ({http://www.opengis.net/oseo/1.0}deliveryOptions) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    
    # Element extension ({http://www.opengis.net/oseo/1.0}extension) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderSpecification
    _ElementMap.update({
        __orderId.name() : __orderId,
        __orderStatusInfo.name() : __orderStatusInfo,
        __orderDateTime.name() : __orderDateTime,
        __orderItem.name() : __orderItem
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CommonOrderMonitorSpecification = CommonOrderMonitorSpecification
Namespace.addCategoryObject('typeBinding', 'CommonOrderMonitorSpecification', CommonOrderMonitorSpecification)


# Complex type {http://www.opengis.net/oseo/1.0}ProductIdType with content type ELEMENT_ONLY
class ProductIdType (OrderItemIdType):
    """Identifier of catalogued product"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProductIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 513, 1)
    _ElementMap = OrderItemIdType._ElementMap.copy()
    _AttributeMap = OrderItemIdType._AttributeMap.copy()
    # Base type is OrderItemIdType
    
    # Element {http://www.opengis.net/oseo/1.0}collectionId uses Python identifier collectionId
    __collectionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'collectionId'), 'collectionId', '__httpwww_opengis_netoseo1_0_ProductIdType_httpwww_opengis_netoseo1_0collectionId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 95, 1), )

    
    collectionId = property(__collectionId.value, __collectionId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'identifier'), 'identifier', '__httpwww_opengis_netoseo1_0_ProductIdType_httpwww_opengis_netoseo1_0identifier', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1269, 1), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    _ElementMap.update({
        __collectionId.name() : __collectionId,
        __identifier.name() : __identifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProductIdType = ProductIdType
Namespace.addCategoryObject('typeBinding', 'ProductIdType', ProductIdType)


# Complex type {http://www.opengis.net/oseo/1.0}SubscriptionIdType with content type ELEMENT_ONLY
class SubscriptionIdType (OrderItemIdType):
    """Identifier of subscription"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SubscriptionIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 527, 1)
    _ElementMap = OrderItemIdType._ElementMap.copy()
    _AttributeMap = OrderItemIdType._AttributeMap.copy()
    # Base type is OrderItemIdType
    
    # Element {http://www.opengis.net/oseo/1.0}collectionId uses Python identifier collectionId
    __collectionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'collectionId'), 'collectionId', '__httpwww_opengis_netoseo1_0_SubscriptionIdType_httpwww_opengis_netoseo1_0collectionId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 95, 1), )

    
    collectionId = property(__collectionId.value, __collectionId.set, None, None)

    _ElementMap.update({
        __collectionId.name() : __collectionId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SubscriptionIdType = SubscriptionIdType
Namespace.addCategoryObject('typeBinding', 'SubscriptionIdType', SubscriptionIdType)


# Complex type {http://www.opengis.net/oseo/1.0}TaskingRequestIdType with content type ELEMENT_ONLY
class TaskingRequestIdType (OrderItemIdType):
    """Complex type {http://www.opengis.net/oseo/1.0}TaskingRequestIdType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaskingRequestIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 539, 1)
    _ElementMap = OrderItemIdType._ElementMap.copy()
    _AttributeMap = OrderItemIdType._AttributeMap.copy()
    # Base type is OrderItemIdType
    
    # Element {http://www.opengis.net/oseo/1.0}ID uses Python identifier ID
    __ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ID'), 'ID', '__httpwww_opengis_netoseo1_0_TaskingRequestIdType_httpwww_opengis_netoseo1_0ID', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 543, 5), )

    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __ID.name() : __ID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TaskingRequestIdType = TaskingRequestIdType
Namespace.addCategoryObject('typeBinding', 'TaskingRequestIdType', TaskingRequestIdType)


# Complex type {http://www.opengis.net/oseo/1.0}CommonOrderStatusItemType with content type ELEMENT_ONLY
class CommonOrderStatusItemType (CommonOrderItemType):
    """Complex type {http://www.opengis.net/oseo/1.0}CommonOrderStatusItemType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommonOrderStatusItemType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 553, 1)
    _ElementMap = CommonOrderItemType._ElementMap.copy()
    _AttributeMap = CommonOrderItemType._AttributeMap.copy()
    # Base type is CommonOrderItemType
    
    # Element orderItemRemark ({http://www.opengis.net/oseo/1.0}orderItemRemark) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderItemType
    
    # Element option ({http://www.opengis.net/oseo/1.0}option) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderItemType
    
    # Element sceneSelection ({http://www.opengis.net/oseo/1.0}sceneSelection) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderItemType
    
    # Element payment ({http://www.opengis.net/oseo/1.0}payment) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderItemType
    
    # Element productId ({http://www.opengis.net/oseo/1.0}productId) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderItemType
    
    # Element taskingRequestId ({http://www.opengis.net/oseo/1.0}taskingRequestId) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderItemType
    
    # Element subscriptionId ({http://www.opengis.net/oseo/1.0}subscriptionId) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderItemType
    
    # Element {http://www.opengis.net/oseo/1.0}orderItemStatusInfo uses Python identifier orderItemStatusInfo
    __orderItemStatusInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderItemStatusInfo'), 'orderItemStatusInfo', '__httpwww_opengis_netoseo1_0_CommonOrderStatusItemType_httpwww_opengis_netoseo1_0orderItemStatusInfo', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 557, 5), )

    
    orderItemStatusInfo = property(__orderItemStatusInfo.value, __orderItemStatusInfo.set, None, None)

    
    # Element itemId ({http://www.opengis.net/oseo/1.0}itemId) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderItemType
    
    # Element productOrderOptionsId ({http://www.opengis.net/oseo/1.0}productOrderOptionsId) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderItemType
    
    # Element deliveryOptions ({http://www.opengis.net/oseo/1.0}deliveryOptions) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderItemType
    
    # Element extension ({http://www.opengis.net/oseo/1.0}extension) inherited from {http://www.opengis.net/oseo/1.0}CommonOrderItemType
    _ElementMap.update({
        __orderItemStatusInfo.name() : __orderItemStatusInfo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CommonOrderStatusItemType = CommonOrderStatusItemType
Namespace.addCategoryObject('typeBinding', 'CommonOrderStatusItemType', CommonOrderStatusItemType)


# Complex type {http://www.opengis.net/oseo/1.0}OrderOptionsResponseType with content type ELEMENT_ONLY
class OrderOptionsResponseType (OrderResponseBaseType):
    """Complex type {http://www.opengis.net/oseo/1.0}OrderOptionsResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrderOptionsResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 615, 1)
    _ElementMap = OrderResponseBaseType._ElementMap.copy()
    _AttributeMap = OrderResponseBaseType._AttributeMap.copy()
    # Base type is OrderResponseBaseType
    
    # Element status ({http://www.opengis.net/oseo/1.0}status) inherited from {http://www.opengis.net/oseo/1.0}OrderResponseBaseType
    
    # Element errorMessage ({http://www.opengis.net/oseo/1.0}errorMessage) inherited from {http://www.opengis.net/oseo/1.0}OrderResponseBaseType
    
    # Element {http://www.opengis.net/oseo/1.0}orderOptions uses Python identifier orderOptions
    __orderOptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderOptions'), 'orderOptions', '__httpwww_opengis_netoseo1_0_OrderOptionsResponseType_httpwww_opengis_netoseo1_0orderOptions', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 706, 1), )

    
    orderOptions = property(__orderOptions.value, __orderOptions.set, None, None)

    _ElementMap.update({
        __orderOptions.name() : __orderOptions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrderOptionsResponseType = OrderOptionsResponseType
Namespace.addCategoryObject('typeBinding', 'OrderOptionsResponseType', OrderOptionsResponseType)


# Complex type {http://www.opengis.net/oseo/1.0}GetQuotationAckType with content type ELEMENT_ONLY
class GetQuotationAckType (OrderResponseBaseType):
    """Complex type {http://www.opengis.net/oseo/1.0}GetQuotationAckType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetQuotationAckType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 770, 1)
    _ElementMap = OrderResponseBaseType._ElementMap.copy()
    _AttributeMap = OrderResponseBaseType._AttributeMap.copy()
    # Base type is OrderResponseBaseType
    
    # Element status ({http://www.opengis.net/oseo/1.0}status) inherited from {http://www.opengis.net/oseo/1.0}OrderResponseBaseType
    
    # Element errorMessage ({http://www.opengis.net/oseo/1.0}errorMessage) inherited from {http://www.opengis.net/oseo/1.0}OrderResponseBaseType
    
    # Element {http://www.opengis.net/oseo/1.0}quotationId uses Python identifier quotationId
    __quotationId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'quotationId'), 'quotationId', '__httpwww_opengis_netoseo1_0_GetQuotationAckType_httpwww_opengis_netoseo1_0quotationId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 775, 6), )

    
    quotationId = property(__quotationId.value, __quotationId.set, None, 'This choice is set in case of non sync quotations.')

    
    # Element {http://www.opengis.net/oseo/1.0}quotation uses Python identifier quotation
    __quotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'quotation'), 'quotation', '__httpwww_opengis_netoseo1_0_GetQuotationAckType_httpwww_opengis_netoseo1_0quotation', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 780, 6), )

    
    quotation = property(__quotation.value, __quotation.set, None, 'This choice is set in case of synchronous quotations or as answer to quotation monitoring.')

    _ElementMap.update({
        __quotationId.name() : __quotationId,
        __quotation.name() : __quotation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GetQuotationAckType = GetQuotationAckType
Namespace.addCategoryObject('typeBinding', 'GetQuotationAckType', GetQuotationAckType)


# Complex type {http://www.opengis.net/oseo/1.0}GetQuotationResponseAckType with content type ELEMENT_ONLY
class GetQuotationResponseAckType (OrderResponseBaseType):
    """Complex type {http://www.opengis.net/oseo/1.0}GetQuotationResponseAckType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetQuotationResponseAckType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 810, 1)
    _ElementMap = OrderResponseBaseType._ElementMap.copy()
    _AttributeMap = OrderResponseBaseType._AttributeMap.copy()
    # Base type is OrderResponseBaseType
    
    # Element status ({http://www.opengis.net/oseo/1.0}status) inherited from {http://www.opengis.net/oseo/1.0}OrderResponseBaseType
    
    # Element errorMessage ({http://www.opengis.net/oseo/1.0}errorMessage) inherited from {http://www.opengis.net/oseo/1.0}OrderResponseBaseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GetQuotationResponseAckType = GetQuotationResponseAckType
Namespace.addCategoryObject('typeBinding', 'GetQuotationResponseAckType', GetQuotationResponseAckType)


# Complex type {http://www.opengis.net/oseo/1.0}DescribeResultAccessResponseType with content type ELEMENT_ONLY
class DescribeResultAccessResponseType (OrderResponseBaseType):
    """Complex type {http://www.opengis.net/oseo/1.0}DescribeResultAccessResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DescribeResultAccessResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 927, 1)
    _ElementMap = OrderResponseBaseType._ElementMap.copy()
    _AttributeMap = OrderResponseBaseType._AttributeMap.copy()
    # Base type is OrderResponseBaseType
    
    # Element status ({http://www.opengis.net/oseo/1.0}status) inherited from {http://www.opengis.net/oseo/1.0}OrderResponseBaseType
    
    # Element errorMessage ({http://www.opengis.net/oseo/1.0}errorMessage) inherited from {http://www.opengis.net/oseo/1.0}OrderResponseBaseType
    
    # Element {http://www.opengis.net/oseo/1.0}URLs uses Python identifier URLs
    __URLs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'URLs'), 'URLs', '__httpwww_opengis_netoseo1_0_DescribeResultAccessResponseType_httpwww_opengis_netoseo1_0URLs', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 931, 5), )

    
    URLs = property(__URLs.value, __URLs.set, None, None)

    _ElementMap.update({
        __URLs.name() : __URLs
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DescribeResultAccessResponseType = DescribeResultAccessResponseType
Namespace.addCategoryObject('typeBinding', 'DescribeResultAccessResponseType', DescribeResultAccessResponseType)


# Complex type {http://www.opengis.net/oseo/1.0}CancelRequestAckType with content type ELEMENT_ONLY
class CancelRequestAckType (OrderResponseBaseType):
    """Complex type {http://www.opengis.net/oseo/1.0}CancelRequestAckType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CancelRequestAckType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1096, 1)
    _ElementMap = OrderResponseBaseType._ElementMap.copy()
    _AttributeMap = OrderResponseBaseType._AttributeMap.copy()
    # Base type is OrderResponseBaseType
    
    # Element status ({http://www.opengis.net/oseo/1.0}status) inherited from {http://www.opengis.net/oseo/1.0}OrderResponseBaseType
    
    # Element errorMessage ({http://www.opengis.net/oseo/1.0}errorMessage) inherited from {http://www.opengis.net/oseo/1.0}OrderResponseBaseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CancelRequestAckType = CancelRequestAckType
Namespace.addCategoryObject('typeBinding', 'CancelRequestAckType', CancelRequestAckType)


# Complex type {http://www.opengis.net/oseo/1.0}StatusNotificationAckType with content type ELEMENT_ONLY
class StatusNotificationAckType (OrderResponseBaseType):
    """Complex type {http://www.opengis.net/oseo/1.0}StatusNotificationAckType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StatusNotificationAckType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1111, 1)
    _ElementMap = OrderResponseBaseType._ElementMap.copy()
    _AttributeMap = OrderResponseBaseType._AttributeMap.copy()
    # Base type is OrderResponseBaseType
    
    # Element status ({http://www.opengis.net/oseo/1.0}status) inherited from {http://www.opengis.net/oseo/1.0}OrderResponseBaseType
    
    # Element errorMessage ({http://www.opengis.net/oseo/1.0}errorMessage) inherited from {http://www.opengis.net/oseo/1.0}OrderResponseBaseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StatusNotificationAckType = StatusNotificationAckType
Namespace.addCategoryObject('typeBinding', 'StatusNotificationAckType', StatusNotificationAckType)


# Complex type {http://www.opengis.net/oseo/1.0}SubmitOrderRequestType with content type ELEMENT_ONLY
class SubmitOrderRequestType (OrderRequestBaseType):
    """Complex type {http://www.opengis.net/oseo/1.0}SubmitOrderRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SubmitOrderRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 265, 1)
    _ElementMap = OrderRequestBaseType._ElementMap.copy()
    _AttributeMap = OrderRequestBaseType._AttributeMap.copy()
    # Base type is OrderRequestBaseType
    
    # Element {http://www.opengis.net/oseo/1.0}statusNotification uses Python identifier statusNotification
    __statusNotification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'statusNotification'), 'statusNotification', '__httpwww_opengis_netoseo1_0_SubmitOrderRequestType_httpwww_opengis_netoseo1_0statusNotification', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 86, 1), )

    
    statusNotification = property(__statusNotification.value, __statusNotification.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}timeStamp uses Python identifier timeStamp
    __timeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timeStamp'), 'timeStamp', '__httpwww_opengis_netoseo1_0_SubmitOrderRequestType_httpwww_opengis_netoseo1_0timeStamp', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 269, 5), )

    
    timeStamp = property(__timeStamp.value, __timeStamp.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}quotationId uses Python identifier quotationId
    __quotationId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'quotationId'), 'quotationId', '__httpwww_opengis_netoseo1_0_SubmitOrderRequestType_httpwww_opengis_netoseo1_0quotationId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 272, 6), )

    
    quotationId = property(__quotationId.value, __quotationId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}orderSpecification uses Python identifier orderSpecification
    __orderSpecification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderSpecification'), 'orderSpecification', '__httpwww_opengis_netoseo1_0_SubmitOrderRequestType_httpwww_opengis_netoseo1_0orderSpecification', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 333, 1), )

    
    orderSpecification = property(__orderSpecification.value, __orderSpecification.set, None, None)

    
    # Attribute service inherited from {http://www.opengis.net/oseo/1.0}OrderRequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/oseo/1.0}OrderRequestBaseType
    _ElementMap.update({
        __statusNotification.name() : __statusNotification,
        __timeStamp.name() : __timeStamp,
        __quotationId.name() : __quotationId,
        __orderSpecification.name() : __orderSpecification
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SubmitOrderRequestType = SubmitOrderRequestType
Namespace.addCategoryObject('typeBinding', 'SubmitOrderRequestType', SubmitOrderRequestType)


# Complex type {http://www.opengis.net/oseo/1.0}GetStatusRequestType with content type ELEMENT_ONLY
class GetStatusRequestType (OrderRequestBaseType):
    """Complex type {http://www.opengis.net/oseo/1.0}GetStatusRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetStatusRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 370, 1)
    _ElementMap = OrderRequestBaseType._ElementMap.copy()
    _AttributeMap = OrderRequestBaseType._AttributeMap.copy()
    # Base type is OrderRequestBaseType
    
    # Element {http://www.opengis.net/oseo/1.0}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderId'), 'orderId', '__httpwww_opengis_netoseo1_0_GetStatusRequestType_httpwww_opengis_netoseo1_0orderId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 84, 1), )

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}timeStamp uses Python identifier timeStamp
    __timeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timeStamp'), 'timeStamp', '__httpwww_opengis_netoseo1_0_GetStatusRequestType_httpwww_opengis_netoseo1_0timeStamp', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 374, 5), )

    
    timeStamp = property(__timeStamp.value, __timeStamp.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}filteringCriteria uses Python identifier filteringCriteria
    __filteringCriteria = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'filteringCriteria'), 'filteringCriteria', '__httpwww_opengis_netoseo1_0_GetStatusRequestType_httpwww_opengis_netoseo1_0filteringCriteria', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 377, 6), )

    
    filteringCriteria = property(__filteringCriteria.value, __filteringCriteria.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}presentation uses Python identifier presentation
    __presentation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'presentation'), 'presentation', '__httpwww_opengis_netoseo1_0_GetStatusRequestType_httpwww_opengis_netoseo1_0presentation', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 379, 5), )

    
    presentation = property(__presentation.value, __presentation.set, None, None)

    
    # Attribute service inherited from {http://www.opengis.net/oseo/1.0}OrderRequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/oseo/1.0}OrderRequestBaseType
    _ElementMap.update({
        __orderId.name() : __orderId,
        __timeStamp.name() : __timeStamp,
        __filteringCriteria.name() : __filteringCriteria,
        __presentation.name() : __presentation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GetStatusRequestType = GetStatusRequestType
Namespace.addCategoryObject('typeBinding', 'GetStatusRequestType', GetStatusRequestType)


# Complex type {http://www.opengis.net/oseo/1.0}OrderOptionsRequestType with content type ELEMENT_ONLY
class OrderOptionsRequestType (OrderRequestBaseType):
    """Complex type {http://www.opengis.net/oseo/1.0}OrderOptionsRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrderOptionsRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 601, 1)
    _ElementMap = OrderRequestBaseType._ElementMap.copy()
    _AttributeMap = OrderRequestBaseType._AttributeMap.copy()
    # Base type is OrderRequestBaseType
    
    # Element {http://www.opengis.net/oseo/1.0}collectionId uses Python identifier collectionId
    __collectionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'collectionId'), 'collectionId', '__httpwww_opengis_netoseo1_0_OrderOptionsRequestType_httpwww_opengis_netoseo1_0collectionId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 95, 1), )

    
    collectionId = property(__collectionId.value, __collectionId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}taskingRequestId uses Python identifier taskingRequestId
    __taskingRequestId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taskingRequestId'), 'taskingRequestId', '__httpwww_opengis_netoseo1_0_OrderOptionsRequestType_httpwww_opengis_netoseo1_0taskingRequestId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 548, 1), )

    
    taskingRequestId = property(__taskingRequestId.value, __taskingRequestId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}timeStamp uses Python identifier timeStamp
    __timeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timeStamp'), 'timeStamp', '__httpwww_opengis_netoseo1_0_OrderOptionsRequestType_httpwww_opengis_netoseo1_0timeStamp', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 605, 5), )

    
    timeStamp = property(__timeStamp.value, __timeStamp.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'identifier'), 'identifier', '__httpwww_opengis_netoseo1_0_OrderOptionsRequestType_httpwww_opengis_netoseo1_0identifier', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1269, 1), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Attribute service inherited from {http://www.opengis.net/oseo/1.0}OrderRequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/oseo/1.0}OrderRequestBaseType
    _ElementMap.update({
        __collectionId.name() : __collectionId,
        __taskingRequestId.name() : __taskingRequestId,
        __timeStamp.name() : __timeStamp,
        __identifier.name() : __identifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrderOptionsRequestType = OrderOptionsRequestType
Namespace.addCategoryObject('typeBinding', 'OrderOptionsRequestType', OrderOptionsRequestType)


# Complex type {http://www.opengis.net/oseo/1.0}GetQuotationRequestType with content type ELEMENT_ONLY
class GetQuotationRequestType (OrderRequestBaseType):
    """Complex type {http://www.opengis.net/oseo/1.0}GetQuotationRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetQuotationRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 749, 1)
    _ElementMap = OrderRequestBaseType._ElementMap.copy()
    _AttributeMap = OrderRequestBaseType._AttributeMap.copy()
    # Base type is OrderRequestBaseType
    
    # Element {http://www.opengis.net/oseo/1.0}orderSpecification uses Python identifier orderSpecification
    __orderSpecification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderSpecification'), 'orderSpecification', '__httpwww_opengis_netoseo1_0_GetQuotationRequestType_httpwww_opengis_netoseo1_0orderSpecification', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 333, 1), )

    
    orderSpecification = property(__orderSpecification.value, __orderSpecification.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}timeStamp uses Python identifier timeStamp
    __timeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timeStamp'), 'timeStamp', '__httpwww_opengis_netoseo1_0_GetQuotationRequestType_httpwww_opengis_netoseo1_0timeStamp', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 753, 5), )

    
    timeStamp = property(__timeStamp.value, __timeStamp.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}quotationId uses Python identifier quotationId
    __quotationId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'quotationId'), 'quotationId', '__httpwww_opengis_netoseo1_0_GetQuotationRequestType_httpwww_opengis_netoseo1_0quotationId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 760, 6), )

    
    quotationId = property(__quotationId.value, __quotationId.set, None, 'This choice is set when quotation monitoring is supported and a quotation request has been already submitted.')

    
    # Attribute service inherited from {http://www.opengis.net/oseo/1.0}OrderRequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/oseo/1.0}OrderRequestBaseType
    _ElementMap.update({
        __orderSpecification.name() : __orderSpecification,
        __timeStamp.name() : __timeStamp,
        __quotationId.name() : __quotationId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GetQuotationRequestType = GetQuotationRequestType
Namespace.addCategoryObject('typeBinding', 'GetQuotationRequestType', GetQuotationRequestType)


# Complex type {http://www.opengis.net/oseo/1.0}GetQuotationResponseRequestType with content type ELEMENT_ONLY
class GetQuotationResponseRequestType (OrderRequestBaseType):
    """Complex type {http://www.opengis.net/oseo/1.0}GetQuotationResponseRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetQuotationResponseRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 790, 1)
    _ElementMap = OrderRequestBaseType._ElementMap.copy()
    _AttributeMap = OrderRequestBaseType._AttributeMap.copy()
    # Base type is OrderRequestBaseType
    
    # Element {http://www.opengis.net/oseo/1.0}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__httpwww_opengis_netoseo1_0_GetQuotationResponseRequestType_httpwww_opengis_netoseo1_0status', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 794, 5), )

    
    status = property(__status.value, __status.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}errorMessage uses Python identifier errorMessage
    __errorMessage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'errorMessage'), 'errorMessage', '__httpwww_opengis_netoseo1_0_GetQuotationResponseRequestType_httpwww_opengis_netoseo1_0errorMessage', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 795, 5), )

    
    errorMessage = property(__errorMessage.value, __errorMessage.set, None, 'This field is set when status element is different from success. It provides some information about the occurred problem.')

    
    # Element {http://www.opengis.net/oseo/1.0}quotation uses Python identifier quotation
    __quotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'quotation'), 'quotation', '__httpwww_opengis_netoseo1_0_GetQuotationResponseRequestType_httpwww_opengis_netoseo1_0quotation', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 805, 5), )

    
    quotation = property(__quotation.value, __quotation.set, None, None)

    
    # Attribute service inherited from {http://www.opengis.net/oseo/1.0}OrderRequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/oseo/1.0}OrderRequestBaseType
    _ElementMap.update({
        __status.name() : __status,
        __errorMessage.name() : __errorMessage,
        __quotation.name() : __quotation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GetQuotationResponseRequestType = GetQuotationResponseRequestType
Namespace.addCategoryObject('typeBinding', 'GetQuotationResponseRequestType', GetQuotationResponseRequestType)


# Complex type {http://www.opengis.net/oseo/1.0}DescribeResultAccessRequestType with content type ELEMENT_ONLY
class DescribeResultAccessRequestType (OrderRequestBaseType):
    """Complex type {http://www.opengis.net/oseo/1.0}DescribeResultAccessRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DescribeResultAccessRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 909, 1)
    _ElementMap = OrderRequestBaseType._ElementMap.copy()
    _AttributeMap = OrderRequestBaseType._AttributeMap.copy()
    # Base type is OrderRequestBaseType
    
    # Element {http://www.opengis.net/oseo/1.0}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderId'), 'orderId', '__httpwww_opengis_netoseo1_0_DescribeResultAccessRequestType_httpwww_opengis_netoseo1_0orderId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 84, 1), )

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}timeStamp uses Python identifier timeStamp
    __timeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timeStamp'), 'timeStamp', '__httpwww_opengis_netoseo1_0_DescribeResultAccessRequestType_httpwww_opengis_netoseo1_0timeStamp', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 913, 5), )

    
    timeStamp = property(__timeStamp.value, __timeStamp.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}subFunction uses Python identifier subFunction
    __subFunction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subFunction'), 'subFunction', '__httpwww_opengis_netoseo1_0_DescribeResultAccessRequestType_httpwww_opengis_netoseo1_0subFunction', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 915, 5), )

    
    subFunction = property(__subFunction.value, __subFunction.set, None, None)

    
    # Attribute service inherited from {http://www.opengis.net/oseo/1.0}OrderRequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/oseo/1.0}OrderRequestBaseType
    _ElementMap.update({
        __orderId.name() : __orderId,
        __timeStamp.name() : __timeStamp,
        __subFunction.name() : __subFunction
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DescribeResultAccessRequestType = DescribeResultAccessRequestType
Namespace.addCategoryObject('typeBinding', 'DescribeResultAccessRequestType', DescribeResultAccessRequestType)


# Complex type {http://www.opengis.net/oseo/1.0}CancelRequestType with content type ELEMENT_ONLY
class CancelRequestType (OrderRequestBaseType):
    """Complex type {http://www.opengis.net/oseo/1.0}CancelRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CancelRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1085, 1)
    _ElementMap = OrderRequestBaseType._ElementMap.copy()
    _AttributeMap = OrderRequestBaseType._AttributeMap.copy()
    # Base type is OrderRequestBaseType
    
    # Element {http://www.opengis.net/oseo/1.0}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderId'), 'orderId', '__httpwww_opengis_netoseo1_0_CancelRequestType_httpwww_opengis_netoseo1_0orderId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 84, 1), )

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}statusNotification uses Python identifier statusNotification
    __statusNotification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'statusNotification'), 'statusNotification', '__httpwww_opengis_netoseo1_0_CancelRequestType_httpwww_opengis_netoseo1_0statusNotification', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 86, 1), )

    
    statusNotification = property(__statusNotification.value, __statusNotification.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}timeStamp uses Python identifier timeStamp
    __timeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timeStamp'), 'timeStamp', '__httpwww_opengis_netoseo1_0_CancelRequestType_httpwww_opengis_netoseo1_0timeStamp', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1089, 5), )

    
    timeStamp = property(__timeStamp.value, __timeStamp.set, None, None)

    
    # Attribute service inherited from {http://www.opengis.net/oseo/1.0}OrderRequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/oseo/1.0}OrderRequestBaseType
    _ElementMap.update({
        __orderId.name() : __orderId,
        __statusNotification.name() : __statusNotification,
        __timeStamp.name() : __timeStamp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CancelRequestType = CancelRequestType
Namespace.addCategoryObject('typeBinding', 'CancelRequestType', CancelRequestType)


# Complex type {http://www.opengis.net/oseo/1.0}StatusNotificationType with content type ELEMENT_ONLY
class StatusNotificationType (OrderRequestBaseType):
    """Complex type {http://www.opengis.net/oseo/1.0}StatusNotificationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StatusNotificationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1101, 1)
    _ElementMap = OrderRequestBaseType._ElementMap.copy()
    _AttributeMap = OrderRequestBaseType._AttributeMap.copy()
    # Base type is OrderRequestBaseType
    
    # Element {http://www.opengis.net/oseo/1.0}orderMonitorSpecification uses Python identifier orderMonitorSpecification
    __orderMonitorSpecification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderMonitorSpecification'), 'orderMonitorSpecification', '__httpwww_opengis_netoseo1_0_StatusNotificationType_httpwww_opengis_netoseo1_0orderMonitorSpecification', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 409, 1), )

    
    orderMonitorSpecification = property(__orderMonitorSpecification.value, __orderMonitorSpecification.set, None, None)

    
    # Element {http://www.opengis.net/oseo/1.0}timeStamp uses Python identifier timeStamp
    __timeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timeStamp'), 'timeStamp', '__httpwww_opengis_netoseo1_0_StatusNotificationType_httpwww_opengis_netoseo1_0timeStamp', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1105, 5), )

    
    timeStamp = property(__timeStamp.value, __timeStamp.set, None, None)

    
    # Attribute service inherited from {http://www.opengis.net/oseo/1.0}OrderRequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/oseo/1.0}OrderRequestBaseType
    _ElementMap.update({
        __orderMonitorSpecification.name() : __orderMonitorSpecification,
        __timeStamp.name() : __timeStamp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StatusNotificationType = StatusNotificationType
Namespace.addCategoryObject('typeBinding', 'StatusNotificationType', StatusNotificationType)


orderId = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderId'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 84, 1))
Namespace.addCategoryObject('elementBinding', orderId.name().localName(), orderId)

identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'identifier'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1269, 1))
Namespace.addCategoryObject('elementBinding', identifier.name().localName(), identifier)

extension = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extension'), pyxb.binding.datatypes.anySimpleType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1318, 1))
Namespace.addCategoryObject('elementBinding', extension.name().localName(), extension)

GetCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetCapabilities'), CTD_ANON, documentation='Request to a Order Service to perform the GetCapabilities operation. This operation allows a client to retrieve service metadata (capabilities XML) providing metadata for the specific Order server. In this XML encoding, no "request" parameter is included, since the element name specifies the specific operation. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 16, 1))
Namespace.addCategoryObject('elementBinding', GetCapabilities.name().localName(), GetCapabilities)

Capabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Capabilities'), CTD_ANON_, documentation='XML encoded Order Service GetCapabilities operation response. This document provides clients with service metadata about a specific service instance. If the server does not implement the updateSequence parameter, the server shall always return the complete Capabilities document, without the updateSequence parameter. When the server implements the updateSequence parameter and the GetCapabilities operation request included the updateSequence parameter with the current value, the server shall return this element with only the "version" and "updateSequence" attributes. Otherwise, all optional elements shall be included or not depending on the actual value of the Sections parameter in the GetCapabilities operation request. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 28, 1))
Namespace.addCategoryObject('elementBinding', Capabilities.name().localName(), Capabilities)

priority = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'priority'), PriorityType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 85, 1))
Namespace.addCategoryObject('elementBinding', priority.name().localName(), priority)

statusNotification = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'statusNotification'), STD_ANON, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 86, 1))
Namespace.addCategoryObject('elementBinding', statusNotification.name().localName(), statusNotification)

collectionId = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'collectionId'), STD_ANON_, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 95, 1))
Namespace.addCategoryObject('elementBinding', collectionId.name().localName(), collectionId)

ParameterData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ParameterData'), ParameterDataType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 565, 1))
Namespace.addCategoryObject('elementBinding', ParameterData.name().localName(), ParameterData)

orderOptions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderOptions'), CommonOrderOptionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 706, 1))
Namespace.addCategoryObject('elementBinding', orderOptions.name().localName(), orderOptions)

itemId = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'itemId'), STD_ANON_38, documentation='string identifying the order item within the order.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1270, 1))
Namespace.addCategoryObject('elementBinding', itemId.name().localName(), itemId)

paymentMethod = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentMethod'), STD_ANON_39, documentation='Examples:\nquota, invoice, prepay (to be indicated for free products), deposit account, credit card, credit card previously supplied', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1281, 1))
Namespace.addCategoryObject('elementBinding', paymentMethod.name().localName(), paymentMethod)

contractInformation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contractInformation'), STD_ANON_40, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1293, 1))
Namespace.addCategoryObject('elementBinding', contractInformation.name().localName(), contractInformation)

orderReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderReference'), STD_ANON_41, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1300, 1))
Namespace.addCategoryObject('elementBinding', orderReference.name().localName(), orderReference)

productOrderOptionsId = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productOrderOptionsId'), STD_ANON_42, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1308, 1))
Namespace.addCategoryObject('elementBinding', productOrderOptionsId.name().localName(), productOrderOptionsId)

deliveryOptions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'deliveryOptions'), DeliveryOptionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1316, 1))
Namespace.addCategoryObject('elementBinding', deliveryOptions.name().localName(), deliveryOptions)

protocol = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'protocol'), ProtocolType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1317, 1))
Namespace.addCategoryObject('elementBinding', protocol.name().localName(), protocol)

GetOptionsResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetOptionsResponse'), OrderOptionsResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 44, 1))
Namespace.addCategoryObject('elementBinding', GetOptionsResponse.name().localName(), GetOptionsResponse)

GetQuotationAck = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetQuotationAck'), GetQuotationAckType, documentation='GetQuotation operation - response message', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 50, 1))
Namespace.addCategoryObject('elementBinding', GetQuotationAck.name().localName(), GetQuotationAck)

GetQuotationResponseAck = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetQuotationResponseAck'), GetQuotationResponseAckType, documentation='Response to acknowledge the receiption of quotation.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 60, 1))
Namespace.addCategoryObject('elementBinding', GetQuotationResponseAck.name().localName(), GetQuotationResponseAck)

SubmitAck = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubmitAck'), SubmitOrderResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 66, 1))
Namespace.addCategoryObject('elementBinding', SubmitAck.name().localName(), SubmitAck)

SubmitResponseAck = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubmitResponseAck'), StatusNotificationAckType, documentation='Response to acknowledge the receiption of order status notification.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 68, 1))
Namespace.addCategoryObject('elementBinding', SubmitResponseAck.name().localName(), SubmitResponseAck)

GetStatusResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetStatusResponse'), GetStatusResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 74, 1))
Namespace.addCategoryObject('elementBinding', GetStatusResponse.name().localName(), GetStatusResponse)

DescribeResultAccessResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescribeResultAccessResponse'), DescribeResultAccessResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 76, 1))
Namespace.addCategoryObject('elementBinding', DescribeResultAccessResponse.name().localName(), DescribeResultAccessResponse)

CancelAck = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CancelAck'), CancelRequestAckType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 78, 1))
Namespace.addCategoryObject('elementBinding', CancelAck.name().localName(), CancelAck)

CancelResponseAck = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CancelResponseAck'), StatusNotificationAckType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 80, 1))
Namespace.addCategoryObject('elementBinding', CancelResponseAck.name().localName(), CancelResponseAck)

orderSpecification = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderSpecification'), OrderSpecification, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 333, 1))
Namespace.addCategoryObject('elementBinding', orderSpecification.name().localName(), orderSpecification)

orderMonitorSpecification = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderMonitorSpecification'), CommonOrderMonitorSpecification, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 409, 1))
Namespace.addCategoryObject('elementBinding', orderMonitorSpecification.name().localName(), orderMonitorSpecification)

productId = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productId'), ProductIdType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 526, 1))
Namespace.addCategoryObject('elementBinding', productId.name().localName(), productId)

taskingRequestId = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taskingRequestId'), TaskingRequestIdType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 548, 1))
Namespace.addCategoryObject('elementBinding', taskingRequestId.name().localName(), taskingRequestId)

subscriptionId = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subscriptionId'), SubscriptionIdType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 549, 1))
Namespace.addCategoryObject('elementBinding', subscriptionId.name().localName(), subscriptionId)

GetOptions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetOptions'), OrderOptionsRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 43, 1))
Namespace.addCategoryObject('elementBinding', GetOptions.name().localName(), GetOptions)

GetQuotation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetQuotation'), GetQuotationRequestType, documentation='GetQuotation operation - request message', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 45, 1))
Namespace.addCategoryObject('elementBinding', GetQuotation.name().localName(), GetQuotation)

GetQuotationResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetQuotationResponse'), GetQuotationResponseRequestType, documentation='Async reply to GetQuotation  - This message carries on the quotation.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 55, 1))
Namespace.addCategoryObject('elementBinding', GetQuotationResponse.name().localName(), GetQuotationResponse)

Submit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Submit'), SubmitOrderRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 65, 1))
Namespace.addCategoryObject('elementBinding', Submit.name().localName(), Submit)

SubmitResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubmitResponse'), StatusNotificationType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 67, 1))
Namespace.addCategoryObject('elementBinding', SubmitResponse.name().localName(), SubmitResponse)

GetStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetStatus'), GetStatusRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 73, 1))
Namespace.addCategoryObject('elementBinding', GetStatus.name().localName(), GetStatus)

DescribeResultAccess = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescribeResultAccess'), DescribeResultAccessRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 75, 1))
Namespace.addCategoryObject('elementBinding', DescribeResultAccess.name().localName(), DescribeResultAccess)

Cancel = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cancel'), CancelRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 77, 1))
Namespace.addCategoryObject('elementBinding', Cancel.name().localName(), Cancel)

CancelResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CancelResponse'), StatusNotificationType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 79, 1))
Namespace.addCategoryObject('elementBinding', CancelResponse.name().localName(), CancelResponse)



def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 106, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 114, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 123, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 132, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'AcceptVersions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 106, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Sections')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 114, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'AcceptFormats')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 123, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'AcceptLanguages')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 132, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contents'), OrderingServiceContentsType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 36, 6)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Notifications'), pyxb.bundles.opengis.swes_2_0.NotificationProducerMetadataPropertyType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 37, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 49, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 51, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 53, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 55, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 36, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 37, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'ServiceIdentification')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 49, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'ServiceProvider')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 51, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'OperationsMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 53, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Languages')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 55, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contents')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 36, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Notifications')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 37, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




OrderResponseBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'status'), OrderResponseStatusType, scope=OrderResponseBaseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 131, 3)))

OrderResponseBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'errorMessage'), STD_ANON_3, scope=OrderResponseBaseType, documentation='This field is set when status element is different from success. It provides some information about the occurred problem.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrderResponseBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 131, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrderResponseBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorMessage')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OrderResponseBaseType._Automaton = _BuildAutomaton_2()




OrderingServiceContentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProductOrders'), CTD_ANON_2, scope=OrderingServiceContentsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 146, 3)))

OrderingServiceContentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubscriptionOrders'), CTD_ANON_3, scope=OrderingServiceContentsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 151, 3)))

OrderingServiceContentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProgrammingOrders'), CTD_ANON_4, scope=OrderingServiceContentsType, documentation='Specifies whether the Ordering Services supports future products ordering and the corresponding SPS URL.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 156, 3)))

OrderingServiceContentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetQuotationCapabilities'), CTD_ANON_5, scope=OrderingServiceContentsType, documentation='This element specifies if and how the order quotation is supported: synchronously, asynchronously, synchronous with polling.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 165, 3)))

OrderingServiceContentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubmitCapabilities'), CTD_ANON_6, scope=OrderingServiceContentsType, documentation='This element specifies the capabilities of Submit Operation e.g. synchronous, async, max number of products, etc.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 177, 3)))

OrderingServiceContentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetStatusCapabilities'), CTD_ANON_7, scope=OrderingServiceContentsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 190, 3)))

OrderingServiceContentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescribeResultAccessCapabilities'), CTD_ANON_8, scope=OrderingServiceContentsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 197, 3)))

OrderingServiceContentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CancelCapabilities'), CTD_ANON_9, scope=OrderingServiceContentsType, documentation='This element specifies the capabilities of Submit Operation e.g. synchronous, async, max number of products, etc.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 202, 3)))

OrderingServiceContentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SupportedCollection'), CollectionCapability, scope=OrderingServiceContentsType, documentation='List of collections allowed for ordering.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 211, 3)))

OrderingServiceContentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContentsType'), EncodingType, scope=OrderingServiceContentsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 216, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 211, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 216, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderingServiceContentsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProductOrders')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 146, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderingServiceContentsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubscriptionOrders')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 151, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderingServiceContentsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProgrammingOrders')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 156, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderingServiceContentsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GetQuotationCapabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 165, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderingServiceContentsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubmitCapabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 177, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderingServiceContentsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GetStatusCapabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 190, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderingServiceContentsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DescribeResultAccessCapabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 197, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrderingServiceContentsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CancelCapabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 202, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrderingServiceContentsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SupportedCollection')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 211, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(OrderingServiceContentsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContentsType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 216, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OrderingServiceContentsType._Automaton = _BuildAutomaton_3()




CollectionCapability._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'collectionId'), STD_ANON_, scope=CollectionCapability, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 95, 1)))

CollectionCapability._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProductOrders'), CTD_ANON_10, scope=CollectionCapability, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 222, 3)))

CollectionCapability._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubscriptionOrders'), CTD_ANON_11, scope=CollectionCapability, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 227, 3)))

CollectionCapability._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescribeResultAccessCapabilities'), CTD_ANON_12, scope=CollectionCapability, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 232, 3)))

CollectionCapability._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CancelCapabilities'), CTD_ANON_13, scope=CollectionCapability, documentation='This element specifies the capabilities of Submit Operation e.g. synchronous, async, max number of products, etc.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 237, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 222, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 227, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 232, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 237, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CollectionCapability._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'collectionId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 221, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CollectionCapability._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProductOrders')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 222, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CollectionCapability._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubscriptionOrders')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 227, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CollectionCapability._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DescribeResultAccessCapabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 232, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CollectionCapability._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CancelCapabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 237, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CollectionCapability._Automaton = _BuildAutomaton_4()




EncodingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supportedEncoding'), SWEEncoding, scope=EncodingType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 253, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EncodingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supportedEncoding')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 253, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EncodingType._Automaton = _BuildAutomaton_5()




CommonOrderSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'priority'), PriorityType, scope=CommonOrderSpecification, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 85, 1)))

CommonOrderSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderRemark'), STD_ANON_4, scope=CommonOrderSpecification, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 305, 3)))

CommonOrderSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'deliveryInformation'), DeliveryInformationType, scope=CommonOrderSpecification, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 313, 3)))

CommonOrderSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invoiceAddress'), DeliveryAddressType, scope=CommonOrderSpecification, documentation='Address for sending the invoice.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 314, 3)))

CommonOrderSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'packaging'), EnumPackagingType, nillable=pyxb.binding.datatypes.boolean(1), scope=CommonOrderSpecification, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 319, 3)))

CommonOrderSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'option'), CTD_ANON_14, scope=CommonOrderSpecification, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 320, 3)))

CommonOrderSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderType'), EnumOrderType, scope=CommonOrderSpecification, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 329, 3)))

CommonOrderSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderReference'), STD_ANON_41, scope=CommonOrderSpecification, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1300, 1)))

CommonOrderSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'deliveryOptions'), DeliveryOptionsType, scope=CommonOrderSpecification, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1316, 1)))

CommonOrderSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extension'), pyxb.binding.datatypes.anySimpleType, scope=CommonOrderSpecification, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1318, 1)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 304, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 305, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 313, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 314, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 319, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 320, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 327, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 328, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 330, 3))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 304, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderRemark')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 305, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deliveryInformation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 313, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceAddress')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 314, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'packaging')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 319, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'option')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 320, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deliveryOptions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 327, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'priority')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 328, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CommonOrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 329, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CommonOrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extension')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 330, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CommonOrderSpecification._Automaton = _BuildAutomaton_6()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ParameterData'), ParameterDataType, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 565, 1)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ParameterData')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 323, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_7()




CreditCardInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'creditCardInstitute'), pyxb.binding.datatypes.anyType, scope=CreditCardInfoType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 336, 3)))

CreditCardInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nameOnCard'), pyxb.binding.datatypes.anyType, scope=CreditCardInfoType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 337, 3)))

CreditCardInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cardNumber'), pyxb.binding.datatypes.anyType, scope=CreditCardInfoType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 338, 3)))

CreditCardInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expirationDate'), pyxb.binding.datatypes.anyType, scope=CreditCardInfoType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 339, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CreditCardInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'creditCardInstitute')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 336, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CreditCardInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nameOnCard')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 337, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CreditCardInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cardNumber')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 338, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CreditCardInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expirationDate')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 339, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CreditCardInfoType._Automaton = _BuildAutomaton_8()




PaymentOptionSelectedValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderAccount'), STD_ANON_5, scope=PaymentOptionSelectedValue, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 346, 4)))

PaymentOptionSelectedValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'creditCardInfo'), STD_ANON_6, scope=PaymentOptionSelectedValue, documentation='This element should be managed in more secure way', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 354, 4)))

PaymentOptionSelectedValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentMethod'), STD_ANON_39, scope=PaymentOptionSelectedValue, documentation='Examples:\nquota, invoice, prepay (to be indicated for free products), deposit account, credit card, credit card previously supplied', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1281, 1)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 346, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 354, 4))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PaymentOptionSelectedValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paymentMethod')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 344, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PaymentOptionSelectedValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderAccount')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 346, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PaymentOptionSelectedValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'creditCardInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 354, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PaymentOptionSelectedValue._Automaton = _BuildAutomaton_9()




OrderSearchCriteriaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastUpdate'), pyxb.binding.datatypes.dateTime, scope=OrderSearchCriteriaType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 412, 3)))

OrderSearchCriteriaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastUpdateEnd'), pyxb.binding.datatypes.anyType, scope=OrderSearchCriteriaType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 413, 3)))

OrderSearchCriteriaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderStatus'), EnumStatusType, scope=OrderSearchCriteriaType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 414, 3)))

OrderSearchCriteriaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderReference'), STD_ANON_41, scope=OrderSearchCriteriaType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1300, 1)))

OrderSearchCriteriaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extension'), pyxb.binding.datatypes.anySimpleType, scope=OrderSearchCriteriaType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1318, 1)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 412, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 413, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 414, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 415, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 416, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrderSearchCriteriaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastUpdate')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 412, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(OrderSearchCriteriaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastUpdateEnd')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 413, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(OrderSearchCriteriaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderStatus')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 414, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(OrderSearchCriteriaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 415, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(OrderSearchCriteriaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extension')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 416, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
OrderSearchCriteriaType._Automaton = _BuildAutomaton_10()




CommonOrderItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderItemRemark'), STD_ANON_7, scope=CommonOrderItemType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 426, 3)))

CommonOrderItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'option'), CTD_ANON_15, scope=CommonOrderItemType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 433, 3)))

CommonOrderItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sceneSelection'), CTD_ANON_16, scope=CommonOrderItemType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 440, 3)))

CommonOrderItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'payment'), PaymentOptionSelectedValue, scope=CommonOrderItemType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 448, 3)))

CommonOrderItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productId'), ProductIdType, scope=CommonOrderItemType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 526, 1)))

CommonOrderItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taskingRequestId'), TaskingRequestIdType, scope=CommonOrderItemType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 548, 1)))

CommonOrderItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subscriptionId'), SubscriptionIdType, scope=CommonOrderItemType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 549, 1)))

CommonOrderItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'itemId'), STD_ANON_38, scope=CommonOrderItemType, documentation='string identifying the order item within the order.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1270, 1)))

CommonOrderItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productOrderOptionsId'), STD_ANON_42, scope=CommonOrderItemType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1308, 1)))

CommonOrderItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'deliveryOptions'), DeliveryOptionsType, scope=CommonOrderItemType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1316, 1)))

CommonOrderItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extension'), pyxb.binding.datatypes.anySimpleType, scope=CommonOrderItemType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1318, 1)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 425, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 426, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 433, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 440, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 447, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 448, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 449, 3))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'itemId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 424, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productOrderOptionsId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 425, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderItemRemark')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 426, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'option')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 433, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sceneSelection')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 440, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deliveryOptions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 447, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'payment')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 448, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extension')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 449, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CommonOrderItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 451, 4))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CommonOrderItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taskingRequestId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 452, 4))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CommonOrderItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subscriptionId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 453, 4))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CommonOrderItemType._Automaton = _BuildAutomaton_11()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ParameterData'), ParameterDataType, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 565, 1)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ParameterData')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 436, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_12()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ParameterData'), ParameterDataType, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 565, 1)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ParameterData')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 443, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_13()




DeliveryOptionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'onlineDataAccess'), CTD_ANON_17, scope=DeliveryOptionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 460, 4)))

DeliveryOptionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'onlineDataDelivery'), CTD_ANON_18, scope=DeliveryOptionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 467, 4)))

DeliveryOptionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mediaDelivery'), CTD_ANON_19, scope=DeliveryOptionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 474, 4)))

DeliveryOptionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'numberOfCopies'), pyxb.binding.datatypes.int, scope=DeliveryOptionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 491, 3)))

DeliveryOptionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productAnnotation'), STD_ANON_9, scope=DeliveryOptionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 492, 3)))

DeliveryOptionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'specialInstructions'), STD_ANON_10, scope=DeliveryOptionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 499, 3)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 491, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 492, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 499, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DeliveryOptionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'onlineDataAccess')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 460, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DeliveryOptionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'onlineDataDelivery')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 467, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DeliveryOptionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mediaDelivery')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 474, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DeliveryOptionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'numberOfCopies')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 491, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DeliveryOptionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productAnnotation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 492, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DeliveryOptionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'specialInstructions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 499, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DeliveryOptionsType._Automaton = _BuildAutomaton_14()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'protocol'), ProtocolType, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1317, 1)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'protocol')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 463, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_15()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'protocol'), ProtocolType, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1317, 1)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'protocol')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 470, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_16()




CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'packageMedium'), PackageMedium, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 477, 7)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shippingInstructions'), STD_ANON_8, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 478, 7)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 478, 7))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'packageMedium')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 477, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shippingInstructions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 478, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_17()




ParameterDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'encoding'), SWEEncoding, scope=ParameterDataType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 568, 3)))

ParameterDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'values'), pyxb.binding.datatypes.anyType, scope=ParameterDataType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 569, 3)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ParameterDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'encoding')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 568, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ParameterDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'values')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 569, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ParameterDataType._Automaton = _BuildAutomaton_18()




CommonOrderOptionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), STD_ANON_11, scope=CommonOrderOptionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 628, 3)))

CommonOrderOptionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderType'), EnumOrderType, scope=CommonOrderOptionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 635, 3)))

CommonOrderOptionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'option'), ParameterDescriptorType, scope=CommonOrderOptionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 636, 3)))

CommonOrderOptionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productDeliveryOptions'), CTD_ANON_20, scope=CommonOrderOptionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 637, 3)))

CommonOrderOptionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderOptionInfoURL'), pyxb.binding.datatypes.anyURI, scope=CommonOrderOptionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 670, 3)))

CommonOrderOptionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentOptions'), PaymentOptionDefinitionType, scope=CommonOrderOptionsType, documentation='List of possible payment options for ordering the product. This element is not specified if the payment options are defined in the user profile.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 671, 3)))

CommonOrderOptionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sceneSelectionOption'), CTD_ANON_24, scope=CommonOrderOptionsType, documentation='Each istance represents a valid combination of scene selection options parameters. Several istances are possible because different policies are possible for the same product (e.g. floating scene, floating pass, full pass)', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 676, 3)))

CommonOrderOptionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'identifier'), pyxb.binding.datatypes.string, scope=CommonOrderOptionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1269, 1)))

CommonOrderOptionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productOrderOptionsId'), STD_ANON_42, scope=CommonOrderOptionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1308, 1)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 627, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 628, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 636, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 670, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 671, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 676, 3))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderOptionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productOrderOptionsId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 626, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderOptionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 627, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderOptionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 628, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderOptionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 635, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderOptionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'option')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 636, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CommonOrderOptionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productDeliveryOptions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 637, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CommonOrderOptionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderOptionInfoURL')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 670, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CommonOrderOptionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paymentOptions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 671, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CommonOrderOptionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sceneSelectionOption')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 676, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CommonOrderOptionsType._Automaton = _BuildAutomaton_19()




CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'onlineDataAccess'), CTD_ANON_21, scope=CTD_ANON_20, documentation='This option says that the Server will specify the URL for accessing the products via DescribeResultAccess operation.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 640, 6)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'onlineDataDelivery'), CTD_ANON_22, scope=CTD_ANON_20, documentation='This option says that the URLs for deliverying the products are defined by the client. No DescribeResultAccess operation to be called.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 650, 6)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mediaDelivery'), CTD_ANON_23, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 660, 6)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'onlineDataAccess')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 640, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'onlineDataDelivery')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 650, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mediaDelivery')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 660, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_20()




CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'protocol'), ProtocolType, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1317, 1)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'protocol')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 646, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_21._Automaton = _BuildAutomaton_21()




CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'protocol'), ProtocolType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1317, 1)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'protocol')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 656, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_22()




CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'packageMedium'), PackageMedium, scope=CTD_ANON_23, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 663, 9)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'packageMedium')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 663, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_23._Automaton = _BuildAutomaton_23()




CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), STD_ANON_12, scope=CTD_ANON_24, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 682, 6)))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), STD_ANON_13, scope=CTD_ANON_24, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 689, 6)))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sceneSelectionParameter'), SceneSelectionDescriptorType, scope=CTD_ANON_24, documentation='Each istance represents a scene selection parameter with its description and constraints. It is possible a sceneSelectionOption with no parameters because in some cases the product can be ordered in scenes or as it is. In the second case no scene selection parameters can be provided.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 696, 6)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 682, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 689, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 696, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 682, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 689, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sceneSelectionParameter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 696, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_24._Automaton = _BuildAutomaton_24()




PaymentOptionDefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentOptionInfoURL'), pyxb.binding.datatypes.anyURI, scope=PaymentOptionDefinitionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 710, 3)))

PaymentOptionDefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentMethod'), STD_ANON_39, scope=PaymentOptionDefinitionType, documentation='Examples:\nquota, invoice, prepay (to be indicated for free products), deposit account, credit card, credit card previously supplied', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1281, 1)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 710, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PaymentOptionDefinitionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paymentMethod')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 709, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PaymentOptionDefinitionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paymentOptionInfoURL')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 710, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PaymentOptionDefinitionType._Automaton = _BuildAutomaton_25()




ParameterDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'grouping'), STD_ANON_14, scope=ParameterDescriptorType, documentation='It identifies the group the option belong to e.g. processing option, etc.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 717, 5)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sweCommon/2.0/simple_components.xsd', 341, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 717, 5))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ParameterDescriptorType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_swe, 'AbstractDataComponent')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sweCommon/2.0/simple_components.xsd', 342, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ParameterDescriptorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'grouping')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 717, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ParameterDescriptorType._Automaton = _BuildAutomaton_26()




SceneSelectionDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sceneRestriction'), CTD_ANON_25, scope=SceneSelectionDescriptorType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 735, 5)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sweCommon/2.0/simple_components.xsd', 341, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 735, 5))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SceneSelectionDescriptorType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_swe, 'AbstractDataComponent')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sweCommon/2.0/simple_components.xsd', 342, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SceneSelectionDescriptorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sceneRestriction')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 735, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SceneSelectionDescriptorType._Automaton = _BuildAutomaton_27()




def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sweCommon/2.0/simple_components.xsd', 341, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(_Namespace_swe, 'AbstractDataComponent')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sweCommon/2.0/simple_components.xsd', 342, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_28()




OrderQuotation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'quotationId'), QuotationIdType, scope=OrderQuotation, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 817, 3)))

OrderQuotation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'validityTime'), pyxb.binding.datatypes.dateTime, scope=OrderQuotation, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 818, 3)))

OrderQuotation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'price'), CurrencyType, scope=OrderQuotation, documentation='Price of the whole order; mandatory unless the provider uses quota concept or products are free of charge.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 819, 3)))

OrderQuotation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderItemGroupPrice'), OrderItemGroupPrice, scope=OrderQuotation, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 824, 3)))

OrderQuotation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contractInformation'), STD_ANON_40, scope=OrderQuotation, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1293, 1)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 818, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 819, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 825, 3))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderQuotation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'quotationId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 817, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderQuotation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validityTime')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 818, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderQuotation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'price')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 819, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrderQuotation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderItemGroupPrice')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 824, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(OrderQuotation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contractInformation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 825, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OrderQuotation._Automaton = _BuildAutomaton_29()




OrderItemGroupPrice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'provider'), ProviderType, scope=OrderItemGroupPrice, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 830, 3)))

OrderItemGroupPrice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'quotationId'), QuotationIdType, scope=OrderItemGroupPrice, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 831, 3)))

OrderItemGroupPrice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'validityTime'), pyxb.binding.datatypes.dateTime, scope=OrderItemGroupPrice, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 832, 3)))

OrderItemGroupPrice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'price'), CurrencyType, scope=OrderItemGroupPrice, documentation='Price of the whole order item gruop.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 833, 3)))

OrderItemGroupPrice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'balance'), CurrencyType, scope=OrderItemGroupPrice, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 838, 3)))

OrderItemGroupPrice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderItemPrice'), OrderItemPrice, scope=OrderItemGroupPrice, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 839, 3)))

OrderItemGroupPrice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contractInformation'), STD_ANON_40, scope=OrderItemGroupPrice, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1293, 1)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 831, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 832, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 838, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 840, 3))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderItemGroupPrice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'provider')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 830, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderItemGroupPrice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'quotationId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 831, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderItemGroupPrice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validityTime')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 832, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderItemGroupPrice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'price')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 833, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderItemGroupPrice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'balance')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 838, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrderItemGroupPrice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderItemPrice')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 839, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(OrderItemGroupPrice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contractInformation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 840, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OrderItemGroupPrice._Automaton = _BuildAutomaton_30()




OrderItemPrice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productId'), ProductIdType, scope=OrderItemPrice, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 526, 1)))

OrderItemPrice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taskingRequestId'), TaskingRequestIdType, scope=OrderItemPrice, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 548, 1)))

OrderItemPrice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subscriptionId'), SubscriptionIdType, scope=OrderItemPrice, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 549, 1)))

OrderItemPrice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'price'), CurrencyType, scope=OrderItemPrice, documentation='Price of the item; is optional if the price at group level is provided; not supported in case the products are free of charge.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 855, 3)))

OrderItemPrice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'priceInformation'), STD_ANON_16, scope=OrderItemPrice, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 860, 3)))

OrderItemPrice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'itemId'), STD_ANON_38, scope=OrderItemPrice, documentation='string identifying the order item within the order.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1270, 1)))

OrderItemPrice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contractInformation'), STD_ANON_40, scope=OrderItemPrice, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1293, 1)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 855, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 860, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 867, 3))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderItemPrice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'itemId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 845, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrderItemPrice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 851, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrderItemPrice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taskingRequestId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 852, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrderItemPrice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subscriptionId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 853, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrderItemPrice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'price')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 855, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(OrderItemPrice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'priceInformation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 860, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(OrderItemPrice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contractInformation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 867, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OrderItemPrice._Automaton = _BuildAutomaton_31()




CurrencyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), pyxb.binding.datatypes.double, scope=CurrencyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 872, 3)))

CurrencyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'currency'), STD_ANON_17, scope=CurrencyType, documentation='Currency including ISO 4217 (e.g.: EUR, USD (US Dollar), CAD (Canada Dollar), AUD (Australia Dollar), GBP (United Kindom Pounds), etc.) and also special values for representing quota.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 873, 3)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrencyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 872, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CurrencyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currency')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 873, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CurrencyType._Automaton = _BuildAutomaton_32()




ProviderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serviceName'), STD_ANON_18, scope=ProviderType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 887, 3)))

ProviderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'organization'), STD_ANON_19, scope=ProviderType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 894, 3)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProviderType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serviceName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 887, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProviderType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'organization')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 894, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProviderType._Automaton = _BuildAutomaton_33()




StatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'status'), EnumStatusType, scope=StatusType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 954, 3)))

StatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'additionalStatusInfo'), STD_ANON_21, scope=StatusType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 955, 3)))

StatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'missionSpecificStatusInfo'), STD_ANON_22, scope=StatusType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 963, 3)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 955, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 963, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 954, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'additionalStatusInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 955, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(StatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'missionSpecificStatusInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 963, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StatusType._Automaton = _BuildAutomaton_34()




DeliveryInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'onlineAddress'), OnlineAddressType, scope=DeliveryInformationType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 974, 3)))

DeliveryInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mailAddress'), DeliveryAddressType, scope=DeliveryInformationType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 975, 3)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 974, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 975, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DeliveryInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'onlineAddress')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 974, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DeliveryInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mailAddress')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 975, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DeliveryInformationType._Automaton = _BuildAutomaton_35()




DeliveryAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'firstName'), STD_ANON_23, scope=DeliveryAddressType, documentation='FirstName to identify the receiving person', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 980, 3)))

DeliveryAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastName'), STD_ANON_24, scope=DeliveryAddressType, documentation='Last Name to identify the receiving person', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 991, 3)))

DeliveryAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'companyRef'), STD_ANON_25, scope=DeliveryAddressType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1002, 3)))

DeliveryAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postalAddress'), CTD_ANON_26, scope=DeliveryAddressType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1010, 3)))

DeliveryAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'telephoneNumber'), STD_ANON_32, scope=DeliveryAddressType, documentation='including country code, prefix, without special sign or intermediate blanks', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1061, 3)))

DeliveryAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facsimileTelephoneNumber'), STD_ANON_33, scope=DeliveryAddressType, documentation='including country code, prefix, without special sign or intermediate blanks', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1072, 3)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 980, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 991, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1002, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1010, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1061, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1072, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DeliveryAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'firstName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 980, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DeliveryAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 991, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DeliveryAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'companyRef')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1002, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DeliveryAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'postalAddress')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1010, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DeliveryAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'telephoneNumber')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1061, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(DeliveryAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facsimileTelephoneNumber')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1072, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DeliveryAddressType._Automaton = _BuildAutomaton_36()




CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetAddress'), STD_ANON_26, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1013, 6)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), STD_ANON_27, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1020, 6)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'state'), STD_ANON_28, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1027, 6)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postalCode'), STD_ANON_29, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1034, 6)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'country'), STD_ANON_30, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1041, 6)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postBox'), STD_ANON_31, scope=CTD_ANON_26, documentation='only number part, only digits allowed', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1048, 6)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1048, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetAddress')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1013, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'city')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1020, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'state')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1027, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'postalCode')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1034, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'country')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1041, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'postBox')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1048, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_26._Automaton = _BuildAutomaton_37()




OnlineAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serverAddress'), STD_ANON_34, scope=OnlineAddressType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1119, 3)))

OnlineAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'userName'), STD_ANON_35, scope=OnlineAddressType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1126, 3)))

OnlineAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'userPassword'), STD_ANON_36, scope=OnlineAddressType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1133, 3)))

OnlineAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'path'), STD_ANON_37, scope=OnlineAddressType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1140, 3)))

OnlineAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'protocol'), ProtocolType, scope=OnlineAddressType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1317, 1)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1126, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1133, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1140, 3))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OnlineAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'protocol')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1118, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OnlineAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serverAddress')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1119, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OnlineAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'userName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1126, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(OnlineAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'userPassword')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1133, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(OnlineAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'path')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1140, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OnlineAddressType._Automaton = _BuildAutomaton_38()




OnLineAccessAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceAddress'), CTD_ANON_27, scope=OnLineAccessAddressType, documentation='Address information related to the Server hosting the item to be accessed.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1151, 3)))

OnLineAccessAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResourceAddress'), CTD_ANON_29, scope=OnLineAccessAddressType, documentation='Address information of the resource to be accessed.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1185, 3)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1151, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OnLineAccessAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceAddress')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1151, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OnLineAccessAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResourceAddress')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1185, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OnLineAccessAddressType._Automaton = _BuildAutomaton_39()




CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), pyxb.binding.datatypes.string, scope=CTD_ANON_27, documentation='It specifies the type of the service hosting the resource e.g. WCS, WMS, etc. This field is optional, since full information about the server can be retrieved from info_URL and infoRequest elements.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1157, 6)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'URL'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_27, documentation='Address of the Server', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1162, 6)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'info_URL'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_27, documentation='Address for getting information about the server. In case of OGC Web Services it can refer to GetCapabilities operation with HTTP GET binding.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1167, 6)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'infoRequest'), CTD_ANON_28, scope=CTD_ANON_27, documentation='In case the information can be retrieved by sending a request message, this field stores the message to be sent. In case of OGC Web Services supporitng SOAP GetCapabilities, this field specifies the GetCapabilities message to send at the address specified in info_URL element.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1172, 6)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1157, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1172, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1157, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'URL')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1162, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'info_URL')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1167, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'infoRequest')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1172, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_27._Automaton = _BuildAutomaton_40()




def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1178, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_28._Automaton = _BuildAutomaton_41()




CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'URL'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_29, documentation='URL for accessing the resource.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1191, 6)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serviceRequest'), CTD_ANON_30, scope=CTD_ANON_29, documentation='In case the resource cannot be accessed simply via the URL, but a message needs to be sent, then this field specifies the message to send.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1196, 6)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1196, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'URL')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1191, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serviceRequest')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1196, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_29._Automaton = _BuildAutomaton_42()




def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1202, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_30._Automaton = _BuildAutomaton_43()




ItemURLType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productId'), ProductIdType, scope=ItemURLType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 526, 1)))

ItemURLType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'itemAddress'), OnLineAccessAddressType, scope=ItemURLType, documentation='This field specifies the full information for accessing the ordered item.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1215, 3)))

ItemURLType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expirationDate'), pyxb.binding.datatypes.dateTime, scope=ItemURLType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1220, 3)))

ItemURLType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'itemId'), STD_ANON_38, scope=ItemURLType, documentation='string identifying the order item within the order.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1270, 1)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1214, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1220, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ItemURLType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'itemId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1213, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ItemURLType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1214, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ItemURLType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'itemAddress')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1215, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ItemURLType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expirationDate')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1220, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ItemURLType._Automaton = _BuildAutomaton_44()




SubmitOrderResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderId'), pyxb.binding.datatypes.anyURI, scope=SubmitOrderResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 84, 1)))

SubmitOrderResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderReference'), STD_ANON_41, scope=SubmitOrderResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1300, 1)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 288, 5))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SubmitOrderResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 131, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SubmitOrderResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorMessage')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SubmitOrderResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 287, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SubmitOrderResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 288, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SubmitOrderResponseType._Automaton = _BuildAutomaton_45()




OrderSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderItem'), CommonOrderItemType, scope=OrderSpecification, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 297, 5)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 304, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 305, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 313, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 314, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 319, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 320, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 327, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 328, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 330, 3))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 304, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderRemark')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 305, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deliveryInformation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 313, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceAddress')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 314, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'packaging')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 319, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'option')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 320, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deliveryOptions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 327, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'priority')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 328, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 329, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extension')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 330, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrderSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderItem')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 297, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OrderSpecification._Automaton = _BuildAutomaton_46()




GetStatusResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderMonitorSpecification'), CommonOrderMonitorSpecification, scope=GetStatusResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 409, 1)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 388, 5))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetStatusResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 131, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GetStatusResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorMessage')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GetStatusResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderMonitorSpecification')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 388, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GetStatusResponseType._Automaton = _BuildAutomaton_47()




CommonOrderMonitorSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderId'), pyxb.binding.datatypes.anyURI, scope=CommonOrderMonitorSpecification, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 84, 1)))

CommonOrderMonitorSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderStatusInfo'), StatusType, scope=CommonOrderMonitorSpecification, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 398, 5)))

CommonOrderMonitorSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderDateTime'), pyxb.binding.datatypes.dateTime, scope=CommonOrderMonitorSpecification, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 399, 5)))

CommonOrderMonitorSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderItem'), CommonOrderStatusItemType, scope=CommonOrderMonitorSpecification, documentation='The orderItem has been defined optional in order to  perform GetStatus request with brief presentation. Of course orders without order items cannot be submitted.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 400, 5)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 304, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 305, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 313, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 314, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 319, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 320, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 327, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 328, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 330, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 399, 5))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 400, 5))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderMonitorSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 304, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderMonitorSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderRemark')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 305, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderMonitorSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deliveryInformation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 313, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderMonitorSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invoiceAddress')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 314, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderMonitorSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'packaging')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 319, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderMonitorSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'option')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 320, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderMonitorSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deliveryOptions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 327, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderMonitorSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'priority')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 328, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderMonitorSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 329, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderMonitorSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extension')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 330, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderMonitorSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 397, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CommonOrderMonitorSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderStatusInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 398, 5))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CommonOrderMonitorSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderDateTime')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 399, 5))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CommonOrderMonitorSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderItem')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 400, 5))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CommonOrderMonitorSpecification._Automaton = _BuildAutomaton_48()




ProductIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'collectionId'), STD_ANON_, scope=ProductIdType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 95, 1)))

ProductIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'identifier'), pyxb.binding.datatypes.string, scope=ProductIdType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1269, 1)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 521, 5))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProductIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 520, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProductIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'collectionId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 521, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProductIdType._Automaton = _BuildAutomaton_49()




SubscriptionIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'collectionId'), STD_ANON_, scope=SubscriptionIdType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 95, 1)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SubscriptionIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'collectionId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 534, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SubscriptionIdType._Automaton = _BuildAutomaton_50()




TaskingRequestIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ID'), pyxb.binding.datatypes.anyURI, scope=TaskingRequestIdType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 543, 5)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TaskingRequestIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ID')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 543, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TaskingRequestIdType._Automaton = _BuildAutomaton_51()




CommonOrderStatusItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderItemStatusInfo'), StatusType, scope=CommonOrderStatusItemType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 557, 5)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 425, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 426, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 433, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 440, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 447, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 448, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 449, 3))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderStatusItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'itemId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 424, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderStatusItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productOrderOptionsId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 425, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderStatusItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderItemRemark')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 426, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderStatusItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'option')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 433, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderStatusItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sceneSelection')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 440, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderStatusItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deliveryOptions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 447, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderStatusItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'payment')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 448, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderStatusItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extension')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 449, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderStatusItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 451, 4))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderStatusItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taskingRequestId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 452, 4))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommonOrderStatusItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subscriptionId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 453, 4))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CommonOrderStatusItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderItemStatusInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 557, 5))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CommonOrderStatusItemType._Automaton = _BuildAutomaton_52()




OrderOptionsResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderOptions'), CommonOrderOptionsType, scope=OrderOptionsResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 706, 1)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 619, 5))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrderOptionsResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 131, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrderOptionsResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorMessage')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(OrderOptionsResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderOptions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 619, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OrderOptionsResponseType._Automaton = _BuildAutomaton_53()




GetQuotationAckType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'quotationId'), QuotationIdType, scope=GetQuotationAckType, documentation='This choice is set in case of non sync quotations.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 775, 6)))

GetQuotationAckType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'quotation'), OrderQuotation, scope=GetQuotationAckType, documentation='This choice is set in case of synchronous quotations or as answer to quotation monitoring.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 780, 6)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 773, 4))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetQuotationAckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 131, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GetQuotationAckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorMessage')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GetQuotationAckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'quotationId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 775, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GetQuotationAckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'quotation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 780, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GetQuotationAckType._Automaton = _BuildAutomaton_54()




def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetQuotationResponseAckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 131, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GetQuotationResponseAckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorMessage')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GetQuotationResponseAckType._Automaton = _BuildAutomaton_55()




DescribeResultAccessResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'URLs'), ItemURLType, scope=DescribeResultAccessResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 931, 5)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 931, 5))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DescribeResultAccessResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 131, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DescribeResultAccessResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorMessage')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DescribeResultAccessResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'URLs')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 931, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DescribeResultAccessResponseType._Automaton = _BuildAutomaton_56()




def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CancelRequestAckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 131, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CancelRequestAckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorMessage')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CancelRequestAckType._Automaton = _BuildAutomaton_57()




def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StatusNotificationAckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 131, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StatusNotificationAckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorMessage')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 132, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StatusNotificationAckType._Automaton = _BuildAutomaton_58()




SubmitOrderRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'statusNotification'), STD_ANON, scope=SubmitOrderRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 86, 1)))

SubmitOrderRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timeStamp'), pyxb.binding.datatypes.dateTime, scope=SubmitOrderRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 269, 5)))

SubmitOrderRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'quotationId'), QuotationIdType, scope=SubmitOrderRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 272, 6)))

SubmitOrderRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderSpecification'), OrderSpecification, scope=SubmitOrderRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 333, 1)))

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 269, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SubmitOrderRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timeStamp')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 269, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SubmitOrderRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderSpecification')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 271, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SubmitOrderRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'quotationId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 272, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SubmitOrderRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'statusNotification')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 274, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SubmitOrderRequestType._Automaton = _BuildAutomaton_59()




GetStatusRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderId'), pyxb.binding.datatypes.anyURI, scope=GetStatusRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 84, 1)))

GetStatusRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timeStamp'), pyxb.binding.datatypes.dateTime, scope=GetStatusRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 374, 5)))

GetStatusRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'filteringCriteria'), OrderSearchCriteriaType, scope=GetStatusRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 377, 6)))

GetStatusRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'presentation'), PresentationType, scope=GetStatusRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 379, 5)))

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 374, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GetStatusRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timeStamp')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 374, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GetStatusRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 376, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GetStatusRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'filteringCriteria')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 377, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetStatusRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'presentation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 379, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GetStatusRequestType._Automaton = _BuildAutomaton_60()




OrderOptionsRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'collectionId'), STD_ANON_, scope=OrderOptionsRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 95, 1)))

OrderOptionsRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taskingRequestId'), TaskingRequestIdType, scope=OrderOptionsRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 548, 1)))

OrderOptionsRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timeStamp'), pyxb.binding.datatypes.dateTime, scope=OrderOptionsRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 605, 5)))

OrderOptionsRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'identifier'), pyxb.binding.datatypes.string, scope=OrderOptionsRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1269, 1)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 605, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderOptionsRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timeStamp')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 605, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrderOptionsRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'collectionId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 607, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrderOptionsRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 608, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrderOptionsRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taskingRequestId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 609, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OrderOptionsRequestType._Automaton = _BuildAutomaton_61()




GetQuotationRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderSpecification'), OrderSpecification, scope=GetQuotationRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 333, 1)))

GetQuotationRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timeStamp'), pyxb.binding.datatypes.dateTime, scope=GetQuotationRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 753, 5)))

GetQuotationRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'quotationId'), QuotationIdType, scope=GetQuotationRequestType, documentation='This choice is set when quotation monitoring is supported and a quotation request has been already submitted.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 760, 6)))

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 753, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GetQuotationRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timeStamp')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 753, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetQuotationRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderSpecification')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 755, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetQuotationRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'quotationId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 760, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GetQuotationRequestType._Automaton = _BuildAutomaton_62()




GetQuotationResponseRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'status'), OrderResponseStatusType, scope=GetQuotationResponseRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 794, 5)))

GetQuotationResponseRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'errorMessage'), STD_ANON_15, scope=GetQuotationResponseRequestType, documentation='This field is set when status element is different from success. It provides some information about the occurred problem.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 795, 5)))

GetQuotationResponseRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'quotation'), OrderQuotation, scope=GetQuotationResponseRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 805, 5)))

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 795, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GetQuotationResponseRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 794, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GetQuotationResponseRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorMessage')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 795, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetQuotationResponseRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'quotation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 805, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GetQuotationResponseRequestType._Automaton = _BuildAutomaton_63()




DescribeResultAccessRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderId'), pyxb.binding.datatypes.anyURI, scope=DescribeResultAccessRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 84, 1)))

DescribeResultAccessRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timeStamp'), pyxb.binding.datatypes.dateTime, scope=DescribeResultAccessRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 913, 5)))

DescribeResultAccessRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subFunction'), STD_ANON_20, scope=DescribeResultAccessRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 915, 5)))

def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 913, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescribeResultAccessRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timeStamp')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 913, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescribeResultAccessRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 914, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DescribeResultAccessRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subFunction')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 915, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DescribeResultAccessRequestType._Automaton = _BuildAutomaton_64()




CancelRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderId'), pyxb.binding.datatypes.anyURI, scope=CancelRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 84, 1)))

CancelRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'statusNotification'), STD_ANON, scope=CancelRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 86, 1)))

CancelRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timeStamp'), pyxb.binding.datatypes.dateTime, scope=CancelRequestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1089, 5)))

def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1089, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CancelRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timeStamp')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1089, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CancelRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1090, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CancelRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'statusNotification')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1091, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CancelRequestType._Automaton = _BuildAutomaton_65()




StatusNotificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderMonitorSpecification'), CommonOrderMonitorSpecification, scope=StatusNotificationType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 409, 1)))

StatusNotificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timeStamp'), pyxb.binding.datatypes.dateTime, scope=StatusNotificationType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1105, 5)))

def _BuildAutomaton_66 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1105, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatusNotificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timeStamp')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1105, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StatusNotificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderMonitorSpecification')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/oseo/1.0/oseo.xsd', 1106, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StatusNotificationType._Automaton = _BuildAutomaton_66()

