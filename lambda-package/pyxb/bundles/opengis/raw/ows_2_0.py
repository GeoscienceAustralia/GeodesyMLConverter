# ./pyxb/bundles/opengis/raw/ows_2_0.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e3319bb01dca292d7dcb9d9ce743db7ca547bf84
# Generated 2017-07-10 00:36:49.701838 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/ows/2.0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:dc603862-6507-11e7-be4a-0a55f9edafa5')

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
import pyxb.bundles.common.xlink
import pyxb.binding.xml_

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/ows/2.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_xlink = pyxb.bundles.common.xlink.Namespace
_Namespace_xlink.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://www.opengis.net/ows/2.0}MimeType
class MimeType (pyxb.binding.datatypes.string):

    """XML encoded identifier of a standard MIME type, possibly
      a parameterized MIME type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MimeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 29, 2)
    _Documentation = 'XML encoded identifier of a standard MIME type, possibly\n      a parameterized MIME type.'
MimeType._CF_pattern = pyxb.binding.facets.CF_pattern()
MimeType._CF_pattern.addPattern(pattern='(application|audio|image|text|video|message|multipart|model)/.+(;\\s*.+=.+)*')
MimeType._InitializeFacetMap(MimeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'MimeType', MimeType)
_module_typeBindings.MimeType = MimeType

# Atomic simple type: {http://www.opengis.net/ows/2.0}VersionType
class VersionType (pyxb.binding.datatypes.string):

    """Specification version for OWS operation. The string value
      shall contain one x.y.z "version" value (e.g., "2.1.3"). A version
      number shall contain three non-negative integers separated by decimal
      points, in the form "x.y.z". The integers y and z shall not exceed 99.
      Each version shall be for the Implementation Specification (document)
      and the associated XML Schemas to which requested operations will
      conform. An Implementation Specification version normally specifies XML
      Schemas against which an XML encoded operation response must conform and
      should be validated. See Version negotiation subclause for more
      information."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VersionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 39, 2)
    _Documentation = 'Specification version for OWS operation. The string value\n      shall contain one x.y.z "version" value (e.g., "2.1.3"). A version\n      number shall contain three non-negative integers separated by decimal\n      points, in the form "x.y.z". The integers y and z shall not exceed 99.\n      Each version shall be for the Implementation Specification (document)\n      and the associated XML Schemas to which requested operations will\n      conform. An Implementation Specification version normally specifies XML\n      Schemas against which an XML encoded operation response must conform and\n      should be validated. See Version negotiation subclause for more\n      information.'
VersionType._CF_pattern = pyxb.binding.facets.CF_pattern()
VersionType._CF_pattern.addPattern(pattern='\\d+\\.\\d?\\d\\.\\d?\\d')
VersionType._InitializeFacetMap(VersionType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'VersionType', VersionType)
_module_typeBindings.VersionType = VersionType

# List simple type: {http://www.opengis.net/ows/2.0}PositionType
# superclasses pyxb.binding.datatypes.anySimpleType
class PositionType (pyxb.binding.basis.STD_list):

    """Position instances hold the coordinates of a position in
      a coordinate reference system (CRS) referenced by the related "crs"
      attribute or elsewhere. For an angular coordinate axis that is
      physically continuous for multiple revolutions, but whose recorded
      values can be discontinuous, special conditions apply when the bounding
      box is continuous across the value discontinuity: a) If the bounding box
      is continuous clear around this angular axis, then ordinate values of
      minus and plus infinity shall be used. b) If the bounding box is
      continuous across the value discontinuity but is not continuous clear
      around this angular axis, then some non-normal value can be used if
      specified for a specific OWS use of the BoundingBoxType. For more
      information, see Subclauses 10.2.5 and C.13.This type is adapted from DirectPositionType and
      doubleList of GML 3.1. The adaptations include omission of all the
      attributes, since the needed information is included in the
      BoundingBoxType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PositionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 170, 2)
    _Documentation = 'Position instances hold the coordinates of a position in\n      a coordinate reference system (CRS) referenced by the related "crs"\n      attribute or elsewhere. For an angular coordinate axis that is\n      physically continuous for multiple revolutions, but whose recorded\n      values can be discontinuous, special conditions apply when the bounding\n      box is continuous across the value discontinuity: a) If the bounding box\n      is continuous clear around this angular axis, then ordinate values of\n      minus and plus infinity shall be used. b) If the bounding box is\n      continuous across the value discontinuity but is not continuous clear\n      around this angular axis, then some non-normal value can be used if\n      specified for a specific OWS use of the BoundingBoxType. For more\n      information, see Subclauses 10.2.5 and C.13.This type is adapted from DirectPositionType and\n      doubleList of GML 3.1. The adaptations include omission of all the\n      attributes, since the needed information is included in the\n      BoundingBoxType.'

    _ItemType = pyxb.binding.datatypes.double
PositionType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PositionType', PositionType)
_module_typeBindings.PositionType = PositionType

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.NMTOKENS, pyxb.binding.basis.enumeration_mixin
class STD_ANON (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.NMTOKEN."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 281, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.NMTOKEN
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='closed', tag=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='open', tag=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='open-closed', tag=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='closed-open', tag=None)
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 60, 8)
    _Documentation = None
STD_ANON_._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_._CF_pattern.addPattern(pattern='\\d+\\.\\d?\\d\\.\\d?\\d')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_pattern)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: {http://www.opengis.net/ows/2.0}ServiceType
class ServiceType (pyxb.binding.datatypes.string):

    """Service type identifier, where the string value is the
      OWS type abbreviation, such as "WMS" or "WFS"."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ServiceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 158, 2)
    _Documentation = 'Service type identifier, where the string value is the\n      OWS type abbreviation, such as "WMS" or "WFS".'
ServiceType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ServiceType', ServiceType)
_module_typeBindings.ServiceType = ServiceType

# Atomic simple type: {http://www.opengis.net/ows/2.0}UpdateSequenceType
class UpdateSequenceType (pyxb.binding.datatypes.string):

    """Service metadata document version, having values that are
      "increased" whenever any change is made in service metadata document.
      Values are selected by each server, and are always opaque to clients.
      See updateSequence parameter use subclause for more
      information."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UpdateSequenceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 194, 2)
    _Documentation = 'Service metadata document version, having values that are\n      "increased" whenever any change is made in service metadata document.\n      Values are selected by each server, and are always opaque to clients.\n      See updateSequence parameter use subclause for more\n      information.'
UpdateSequenceType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'UpdateSequenceType', UpdateSequenceType)
_module_typeBindings.UpdateSequenceType = UpdateSequenceType

# List simple type: {http://www.opengis.net/ows/2.0}PositionType2D
# superclasses PositionType
class PositionType2D (pyxb.binding.basis.STD_list):

    """Two-dimensional position instances hold the longitude and
      latitude coordinates of a position in the 2D WGS 84 coordinate reference
      system. The longitude value shall be listed first, followed by the
      latitude value, both in decimal degrees. Latitude values shall range
      from -90 to +90 degrees, and longitude values shall normally range from
      -180 to +180 degrees. For the longitude axis, special conditions apply
      when the bounding box is continuous across the +/- 180 degrees meridian
      longitude value discontinuity: a) If the bounding box is continuous
      clear around the Earth, then longitude values of minus and plus infinity
      shall be used. b) If the bounding box is continuous across the value
      discontinuity but is not continuous clear around the Earth, then some
      non-normal value can be used if specified for a specific OWS use of the
      WGS84BoundingBoxType. For more information, see Subclauses 10.4.5 and
      C.13."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PositionType2D')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 254, 2)
    _Documentation = 'Two-dimensional position instances hold the longitude and\n      latitude coordinates of a position in the 2D WGS 84 coordinate reference\n      system. The longitude value shall be listed first, followed by the\n      latitude value, both in decimal degrees. Latitude values shall range\n      from -90 to +90 degrees, and longitude values shall normally range from\n      -180 to +180 degrees. For the longitude axis, special conditions apply\n      when the bounding box is continuous across the +/- 180 degrees meridian\n      longitude value discontinuity: a) If the bounding box is continuous\n      clear around the Earth, then longitude values of minus and plus infinity\n      shall be used. b) If the bounding box is continuous across the value\n      discontinuity but is not continuous clear around the Earth, then some\n      non-normal value can be used if specified for a specific OWS use of the\n      WGS84BoundingBoxType. For more information, see Subclauses 10.4.5 and\n      C.13.'

    _ItemType = pyxb.binding.datatypes.double
PositionType2D._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2))
PositionType2D._InitializeFacetMap(PositionType2D._CF_length)
Namespace.addCategoryObject('typeBinding', 'PositionType2D', PositionType2D)
_module_typeBindings.PositionType2D = PositionType2D

# Complex type {http://www.opengis.net/ows/2.0}LanguageStringType with content type SIMPLE
class LanguageStringType (pyxb.binding.basis.complexTypeDefinition):
    """Text string with the language of the string identified as
      recommended in the XML 1.0 W3C Recommendation, section
      2.12."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LanguageStringType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 37, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_opengis_netows2_0_LanguageStringType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 45, 8)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
_module_typeBindings.LanguageStringType = LanguageStringType
Namespace.addCategoryObject('typeBinding', 'LanguageStringType', LanguageStringType)


# Complex type {http://www.opengis.net/ows/2.0}KeywordsType with content type ELEMENT_ONLY
class KeywordsType (pyxb.binding.basis.complexTypeDefinition):
    """Unordered list of one or more commonly used or formalised
      word(s) or phrase(s) used to describe the subject. When needed, the
      optional "type" can name the type of the associated list of keywords
      that shall all have the same type. Also when needed, the codeSpace
      attribute of that "type" can reference the type name authority and/or
      thesaurus. If the xml:lang attribute is not included in a Keyword
      element, then no language is specified for that element unless specified
      by another means. All Keyword elements in the same Keywords element that
      share the same xml:lang attribute value represent different keywords in
      that language.For OWS use, the optional thesaurusName element was
      omitted as being complex information that could be referenced by the
      codeSpace attribute of the Type element."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'KeywordsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 70, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}Keyword uses Python identifier Keyword
    __Keyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Keyword'), 'Keyword', '__httpwww_opengis_netows2_0_KeywordsType_httpwww_opengis_netows2_0Keyword', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 87, 6), )

    
    Keyword = property(__Keyword.value, __Keyword.set, None, None)

    
    # Element {http://www.opengis.net/ows/2.0}Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Type'), 'Type', '__httpwww_opengis_netows2_0_KeywordsType_httpwww_opengis_netows2_0Type', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 90, 6), )

    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        __Keyword.name() : __Keyword,
        __Type.name() : __Type
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.KeywordsType = KeywordsType
Namespace.addCategoryObject('typeBinding', 'KeywordsType', KeywordsType)


# Complex type {http://www.opengis.net/ows/2.0}CodeType with content type SIMPLE
class CodeType (pyxb.binding.basis.complexTypeDefinition):
    """Name or code with an (optional) authority. If the
      codeSpace attribute is present, its value shall reference a dictionary,
      thesaurus, or authority for the name or code, such as the organisation
      who assigned the value, or the dictionary from which it is
      taken.Type copied from basicTypes.xsd of GML 3 with
      documentation edited, for possible use outside the ServiceIdentification
      section of a service metadata document."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 96, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute codeSpace uses Python identifier codeSpace
    __codeSpace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'codeSpace'), 'codeSpace', '__httpwww_opengis_netows2_0_CodeType_codeSpace', pyxb.binding.datatypes.anyURI)
    __codeSpace._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 109, 8)
    __codeSpace._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 109, 8)
    
    codeSpace = property(__codeSpace.value, __codeSpace.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __codeSpace.name() : __codeSpace
    })
_module_typeBindings.CodeType = CodeType
Namespace.addCategoryObject('typeBinding', 'CodeType', CodeType)


# Complex type {http://www.opengis.net/ows/2.0}ResponsiblePartyType with content type ELEMENT_ONLY
class ResponsiblePartyType (pyxb.binding.basis.complexTypeDefinition):
    """Identification of, and means of communication with,
      person responsible for the server. At least one of IndividualName,
      OrganisationName, or PositionName shall be included."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResponsiblePartyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 132, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}IndividualName uses Python identifier IndividualName
    __IndividualName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IndividualName'), 'IndividualName', '__httpwww_opengis_netows2_0_ResponsiblePartyType_httpwww_opengis_netows2_0IndividualName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 175, 2), )

    
    IndividualName = property(__IndividualName.value, __IndividualName.set, None, 'Name of the responsible person: surname, given name,\n      title separated by a delimiter.')

    
    # Element {http://www.opengis.net/ows/2.0}OrganisationName uses Python identifier OrganisationName
    __OrganisationName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrganisationName'), 'OrganisationName', '__httpwww_opengis_netows2_0_ResponsiblePartyType_httpwww_opengis_netows2_0OrganisationName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 183, 2), )

    
    OrganisationName = property(__OrganisationName.value, __OrganisationName.set, None, 'Name of the responsible organization.')

    
    # Element {http://www.opengis.net/ows/2.0}PositionName uses Python identifier PositionName
    __PositionName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PositionName'), 'PositionName', '__httpwww_opengis_netows2_0_ResponsiblePartyType_httpwww_opengis_netows2_0PositionName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 190, 2), )

    
    PositionName = property(__PositionName.value, __PositionName.set, None, 'Role or position of the responsible\n      person.')

    
    # Element {http://www.opengis.net/ows/2.0}Role uses Python identifier Role
    __Role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Role'), 'Role', '__httpwww_opengis_netows2_0_ResponsiblePartyType_httpwww_opengis_netows2_0Role', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 198, 2), )

    
    Role = property(__Role.value, __Role.set, None, 'Function performed by the responsible party. Possible\n      values of this Role shall include the values and the meanings listed in\n      Subclause B.5.5 of ISO 19115:2003.')

    
    # Element {http://www.opengis.net/ows/2.0}ContactInfo uses Python identifier ContactInfo
    __ContactInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo'), 'ContactInfo', '__httpwww_opengis_netows2_0_ResponsiblePartyType_httpwww_opengis_netows2_0ContactInfo', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 207, 2), )

    
    ContactInfo = property(__ContactInfo.value, __ContactInfo.set, None, 'Address of the responsible party.')

    _ElementMap.update({
        __IndividualName.name() : __IndividualName,
        __OrganisationName.name() : __OrganisationName,
        __PositionName.name() : __PositionName,
        __Role.name() : __Role,
        __ContactInfo.name() : __ContactInfo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ResponsiblePartyType = ResponsiblePartyType
Namespace.addCategoryObject('typeBinding', 'ResponsiblePartyType', ResponsiblePartyType)


# Complex type {http://www.opengis.net/ows/2.0}ResponsiblePartySubsetType with content type ELEMENT_ONLY
class ResponsiblePartySubsetType (pyxb.binding.basis.complexTypeDefinition):
    """Identification of, and means of communication with,
      person responsible for the server.For OWS use in the ServiceProvider section of a service
      metadata document, the optional organizationName element was removed,
      since this type is always used with the ProviderName element which
      provides that information. The mandatory "role" element was changed to
      optional, since no clear use of this information is known in the
      ServiceProvider section."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResponsiblePartySubsetType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 152, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}IndividualName uses Python identifier IndividualName
    __IndividualName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IndividualName'), 'IndividualName', '__httpwww_opengis_netows2_0_ResponsiblePartySubsetType_httpwww_opengis_netows2_0IndividualName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 175, 2), )

    
    IndividualName = property(__IndividualName.value, __IndividualName.set, None, 'Name of the responsible person: surname, given name,\n      title separated by a delimiter.')

    
    # Element {http://www.opengis.net/ows/2.0}PositionName uses Python identifier PositionName
    __PositionName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PositionName'), 'PositionName', '__httpwww_opengis_netows2_0_ResponsiblePartySubsetType_httpwww_opengis_netows2_0PositionName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 190, 2), )

    
    PositionName = property(__PositionName.value, __PositionName.set, None, 'Role or position of the responsible\n      person.')

    
    # Element {http://www.opengis.net/ows/2.0}Role uses Python identifier Role
    __Role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Role'), 'Role', '__httpwww_opengis_netows2_0_ResponsiblePartySubsetType_httpwww_opengis_netows2_0Role', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 198, 2), )

    
    Role = property(__Role.value, __Role.set, None, 'Function performed by the responsible party. Possible\n      values of this Role shall include the values and the meanings listed in\n      Subclause B.5.5 of ISO 19115:2003.')

    
    # Element {http://www.opengis.net/ows/2.0}ContactInfo uses Python identifier ContactInfo
    __ContactInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo'), 'ContactInfo', '__httpwww_opengis_netows2_0_ResponsiblePartySubsetType_httpwww_opengis_netows2_0ContactInfo', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 207, 2), )

    
    ContactInfo = property(__ContactInfo.value, __ContactInfo.set, None, 'Address of the responsible party.')

    _ElementMap.update({
        __IndividualName.name() : __IndividualName,
        __PositionName.name() : __PositionName,
        __Role.name() : __Role,
        __ContactInfo.name() : __ContactInfo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ResponsiblePartySubsetType = ResponsiblePartySubsetType
Namespace.addCategoryObject('typeBinding', 'ResponsiblePartySubsetType', ResponsiblePartySubsetType)


# Complex type {http://www.opengis.net/ows/2.0}ContactType with content type ELEMENT_ONLY
class ContactType (pyxb.binding.basis.complexTypeDefinition):
    """Information required to enable contact with the
      responsible person and/or organization.For OWS use in the service metadata document, the
      optional hoursOfService and contactInstructions elements were retained,
      as possibly being useful in the ServiceProvider section."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContactType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 214, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}Phone uses Python identifier Phone
    __Phone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Phone'), 'Phone', '__httpwww_opengis_netows2_0_ContactType_httpwww_opengis_netows2_0Phone', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 223, 6), )

    
    Phone = property(__Phone.value, __Phone.set, None, 'Telephone numbers at which the organization or\n          individual may be contacted.')

    
    # Element {http://www.opengis.net/ows/2.0}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Address'), 'Address', '__httpwww_opengis_netows2_0_ContactType_httpwww_opengis_netows2_0Address', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 231, 6), )

    
    Address = property(__Address.value, __Address.set, None, 'Physical and email address at which the organization\n          or individual may be contacted.')

    
    # Element {http://www.opengis.net/ows/2.0}OnlineResource uses Python identifier OnlineResource
    __OnlineResource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OnlineResource'), 'OnlineResource', '__httpwww_opengis_netows2_0_ContactType_httpwww_opengis_netows2_0OnlineResource', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 239, 6), )

    
    OnlineResource = property(__OnlineResource.value, __OnlineResource.set, None, 'On-line information that can be used to contact the\n          individual or organization. OWS specifics: The xlink:href attribute\n          in the xlink:simpleAttrs attribute group shall be used to reference\n          this resource. Whenever practical, the xlink:href attribute with\n          type anyURI should be a URL from which more contact information can\n          be electronically retrieved. The xlink:title attribute with type\n          "string" can be used to name this set of information. The other\n          attributes in the xlink:simpleAttrs attribute group should not be\n          used.')

    
    # Element {http://www.opengis.net/ows/2.0}HoursOfService uses Python identifier HoursOfService
    __HoursOfService = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HoursOfService'), 'HoursOfService', '__httpwww_opengis_netows2_0_ContactType_httpwww_opengis_netows2_0HoursOfService', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 254, 6), )

    
    HoursOfService = property(__HoursOfService.value, __HoursOfService.set, None, 'Time period (including time zone) when individuals\n          can contact the organization or individual.')

    
    # Element {http://www.opengis.net/ows/2.0}ContactInstructions uses Python identifier ContactInstructions
    __ContactInstructions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContactInstructions'), 'ContactInstructions', '__httpwww_opengis_netows2_0_ContactType_httpwww_opengis_netows2_0ContactInstructions', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 262, 6), )

    
    ContactInstructions = property(__ContactInstructions.value, __ContactInstructions.set, None, 'Supplemental instructions on how or when to contact\n          the individual or organization.')

    _ElementMap.update({
        __Phone.name() : __Phone,
        __Address.name() : __Address,
        __OnlineResource.name() : __OnlineResource,
        __HoursOfService.name() : __HoursOfService,
        __ContactInstructions.name() : __ContactInstructions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ContactType = ContactType
Namespace.addCategoryObject('typeBinding', 'ContactType', ContactType)


# Complex type {http://www.opengis.net/ows/2.0}OnlineResourceType with content type EMPTY
class OnlineResourceType (pyxb.binding.basis.complexTypeDefinition):
    """Reference to on-line resource from which data can be
      obtained.For OWS use in the service metadata document, the
      CI_OnlineResource class was XML encoded as the attributeGroup
      "xlink:simpleAttrs", as used in GML."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OnlineResourceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 273, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netows2_0_OnlineResourceType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netows2_0_OnlineResourceType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netows2_0_OnlineResourceType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netows2_0_OnlineResourceType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netows2_0_OnlineResourceType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netows2_0_OnlineResourceType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netows2_0_OnlineResourceType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.OnlineResourceType = OnlineResourceType
Namespace.addCategoryObject('typeBinding', 'OnlineResourceType', OnlineResourceType)


# Complex type {http://www.opengis.net/ows/2.0}TelephoneType with content type ELEMENT_ONLY
class TelephoneType (pyxb.binding.basis.complexTypeDefinition):
    """Telephone numbers for contacting the responsible
      individual or organization."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TelephoneType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 284, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}Voice uses Python identifier Voice
    __Voice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Voice'), 'Voice', '__httpwww_opengis_netows2_0_TelephoneType_httpwww_opengis_netows2_0Voice', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 290, 6), )

    
    Voice = property(__Voice.value, __Voice.set, None, 'Telephone number by which individuals can speak to\n          the responsible organization or individual.')

    
    # Element {http://www.opengis.net/ows/2.0}Facsimile uses Python identifier Facsimile
    __Facsimile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Facsimile'), 'Facsimile', '__httpwww_opengis_netows2_0_TelephoneType_httpwww_opengis_netows2_0Facsimile', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 299, 6), )

    
    Facsimile = property(__Facsimile.value, __Facsimile.set, None, 'Telephone number of a facsimile machine for the\n          responsible organization or individual.')

    _ElementMap.update({
        __Voice.name() : __Voice,
        __Facsimile.name() : __Facsimile
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TelephoneType = TelephoneType
Namespace.addCategoryObject('typeBinding', 'TelephoneType', TelephoneType)


# Complex type {http://www.opengis.net/ows/2.0}AddressType with content type ELEMENT_ONLY
class AddressType (pyxb.binding.basis.complexTypeDefinition):
    """Location of the responsible individual or
      organization."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddressType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 311, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}DeliveryPoint uses Python identifier DeliveryPoint
    __DeliveryPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DeliveryPoint'), 'DeliveryPoint', '__httpwww_opengis_netows2_0_AddressType_httpwww_opengis_netows2_0DeliveryPoint', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 317, 6), )

    
    DeliveryPoint = property(__DeliveryPoint.value, __DeliveryPoint.set, None, 'Address line for the location.')

    
    # Element {http://www.opengis.net/ows/2.0}City uses Python identifier City
    __City = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'City'), 'City', '__httpwww_opengis_netows2_0_AddressType_httpwww_opengis_netows2_0City', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 325, 6), )

    
    City = property(__City.value, __City.set, None, 'City of the location.')

    
    # Element {http://www.opengis.net/ows/2.0}AdministrativeArea uses Python identifier AdministrativeArea
    __AdministrativeArea = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeArea'), 'AdministrativeArea', '__httpwww_opengis_netows2_0_AddressType_httpwww_opengis_netows2_0AdministrativeArea', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 332, 6), )

    
    AdministrativeArea = property(__AdministrativeArea.value, __AdministrativeArea.set, None, 'State or province of the location.')

    
    # Element {http://www.opengis.net/ows/2.0}PostalCode uses Python identifier PostalCode
    __PostalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), 'PostalCode', '__httpwww_opengis_netows2_0_AddressType_httpwww_opengis_netows2_0PostalCode', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 339, 6), )

    
    PostalCode = property(__PostalCode.value, __PostalCode.set, None, 'ZIP or other postal code.')

    
    # Element {http://www.opengis.net/ows/2.0}Country uses Python identifier Country
    __Country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Country'), 'Country', '__httpwww_opengis_netows2_0_AddressType_httpwww_opengis_netows2_0Country', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 346, 6), )

    
    Country = property(__Country.value, __Country.set, None, 'Country of the physical address.')

    
    # Element {http://www.opengis.net/ows/2.0}ElectronicMailAddress uses Python identifier ElectronicMailAddress
    __ElectronicMailAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ElectronicMailAddress'), 'ElectronicMailAddress', '__httpwww_opengis_netows2_0_AddressType_httpwww_opengis_netows2_0ElectronicMailAddress', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 353, 6), )

    
    ElectronicMailAddress = property(__ElectronicMailAddress.value, __ElectronicMailAddress.set, None, 'Address of the electronic mailbox of the responsible\n          organization or individual.')

    _ElementMap.update({
        __DeliveryPoint.name() : __DeliveryPoint,
        __City.name() : __City,
        __AdministrativeArea.name() : __AdministrativeArea,
        __PostalCode.name() : __PostalCode,
        __Country.name() : __Country,
        __ElectronicMailAddress.name() : __ElectronicMailAddress
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AddressType = AddressType
Namespace.addCategoryObject('typeBinding', 'AddressType', AddressType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """One additional metadata parameter."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 71, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_opengis_netows2_0_CTD_ANON_httpwww_opengis_netows2_0Name', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 73, 8), )

    
    Name = property(__Name.value, __Name.set, None, 'Name or identifier of this AdditionalParameter,\n            unique for this OGC Web Service.')

    
    # Element {http://www.opengis.net/ows/2.0}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Value'), 'Value', '__httpwww_opengis_netows2_0_CTD_ANON_httpwww_opengis_netows2_0Value', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 80, 8), )

    
    Value = property(__Value.value, __Value.set, None, 'Unordered list of one or more values of this\n            AdditionalParameter.')

    _ElementMap.update({
        __Name.name() : __Name,
        __Value.name() : __Value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://www.opengis.net/ows/2.0}MetadataType with content type ELEMENT_ONLY
class MetadataType (pyxb.binding.basis.complexTypeDefinition):
    """This element either references or contains more metadata
      about the element that includes this element. To reference metadata
      stored remotely, at least the xlinks:href attribute in xlink:simpleAttrs
      shall be included. Either at least one of the attributes in
      xlink:simpleAttrs or a substitute for the AbstractMetaData element shall
      be included, but not both. An Implementation Specification can restrict
      the contents of this element to always be a reference or always contain
      metadata. (Informative: This element was adapted from the
      metaDataProperty element in GML 3.0.)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 60, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}AbstractMetaData uses Python identifier AbstractMetaData
    __AbstractMetaData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AbstractMetaData'), 'AbstractMetaData', '__httpwww_opengis_netows2_0_MetadataType_httpwww_opengis_netows2_0AbstractMetaData', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 95, 2), )

    
    AbstractMetaData = property(__AbstractMetaData.value, __AbstractMetaData.set, None, 'Abstract element containing more metadata about the\n      element that includes the containing "metadata" element. A specific\n      server implementation, or an Implementation Specification, can define\n      concrete elements in the AbstractMetaData substitution\n      group.')

    
    # Attribute about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'about'), 'about', '__httpwww_opengis_netows2_0_MetadataType_about', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 84, 4)
    __about._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 84, 4)
    
    about = property(__about.value, __about.set, None, 'Optional reference to the aspect of the element which\n        includes this "metadata" element that this metadata provides more\n        information about.')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netows2_0_MetadataType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netows2_0_MetadataType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netows2_0_MetadataType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netows2_0_MetadataType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netows2_0_MetadataType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netows2_0_MetadataType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netows2_0_MetadataType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __AbstractMetaData.name() : __AbstractMetaData
    })
    _AttributeMap.update({
        __about.name() : __about,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.MetadataType = MetadataType
Namespace.addCategoryObject('typeBinding', 'MetadataType', MetadataType)


# Complex type {http://www.opengis.net/ows/2.0}BoundingBoxType with content type ELEMENT_ONLY
class BoundingBoxType (pyxb.binding.basis.complexTypeDefinition):
    """XML encoded minimum rectangular bounding box (or region)
      parameter, surrounding all the associated data.This type is adapted from the EnvelopeType of GML 3.1,
      with modified contents and documentation for encoding a MINIMUM size box
      SURROUNDING all associated data."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoundingBoxType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 110, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}LowerCorner uses Python identifier LowerCorner
    __LowerCorner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LowerCorner'), 'LowerCorner', '__httpwww_opengis_netows2_0_BoundingBoxType_httpwww_opengis_netows2_0LowerCorner', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 119, 6), )

    
    LowerCorner = property(__LowerCorner.value, __LowerCorner.set, None, 'Position of the bounding box corner at which the\n          value of each coordinate normally is the algebraic minimum within\n          this bounding box. In some cases, this position is normally\n          displayed at the top, such as the top left for some image\n          coordinates. For more information, see Subclauses 10.2.5 and\n          C.13.')

    
    # Element {http://www.opengis.net/ows/2.0}UpperCorner uses Python identifier UpperCorner
    __UpperCorner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UpperCorner'), 'UpperCorner', '__httpwww_opengis_netows2_0_BoundingBoxType_httpwww_opengis_netows2_0UpperCorner', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 130, 6), )

    
    UpperCorner = property(__UpperCorner.value, __UpperCorner.set, None, 'Position of the bounding box corner at which the\n          value of each coordinate normally is the algebraic maximum within\n          this bounding box. In some cases, this position is normally\n          displayed at the bottom, such as the bottom right for some image\n          coordinates. For more information, see Subclauses 10.2.5 and\n          C.13.')

    
    # Attribute crs uses Python identifier crs
    __crs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'crs'), 'crs', '__httpwww_opengis_netows2_0_BoundingBoxType_crs', pyxb.binding.datatypes.anyURI)
    __crs._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 142, 4)
    __crs._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 142, 4)
    
    crs = property(__crs.value, __crs.set, None, 'Usually references the definition of a CRS, as\n        specified in [OGC Topic 2]. Such a CRS definition can be XML encoded\n        using the gml:CoordinateReferenceSystemType in [GML 3.1]. For well\n        known references, it is not required that a CRS definition exist at\n        the location the URI points to. If no anyURI value is included, the\n        applicable CRS must be either: a) Specified outside the bounding box,\n        but inside a data structure that includes this bounding box, as\n        specified for a specific OWS use of this bounding box type. b) Fixed\n        and specified in the Implementation Specification for a specific OWS\n        use of the bounding box type.')

    
    # Attribute dimensions uses Python identifier dimensions
    __dimensions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dimensions'), 'dimensions', '__httpwww_opengis_netows2_0_BoundingBoxType_dimensions', pyxb.binding.datatypes.positiveInteger)
    __dimensions._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 158, 4)
    __dimensions._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 158, 4)
    
    dimensions = property(__dimensions.value, __dimensions.set, None, 'The number of dimensions in this CRS (the length of a\n        coordinate sequence in this use of the PositionType). This number is\n        specified by the CRS definition, but can also be specified\n        here.')

    _ElementMap.update({
        __LowerCorner.name() : __LowerCorner,
        __UpperCorner.name() : __UpperCorner
    })
    _AttributeMap.update({
        __crs.name() : __crs,
        __dimensions.name() : __dimensions
    })
_module_typeBindings.BoundingBoxType = BoundingBoxType
Namespace.addCategoryObject('typeBinding', 'BoundingBoxType', BoundingBoxType)


# Complex type {http://www.opengis.net/ows/2.0}ContentsBaseType with content type ELEMENT_ONLY
class ContentsBaseType (pyxb.binding.basis.complexTypeDefinition):
    """Contents of typical Contents section of an OWS service
      metadata (Capabilities) document. This type shall be extended and/or
      restricted if needed for specific OWS use to include the specific
      metadata needed."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContentsBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 33, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}OtherSource uses Python identifier OtherSource
    __OtherSource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OtherSource'), 'OtherSource', '__httpwww_opengis_netows2_0_ContentsBaseType_httpwww_opengis_netows2_0OtherSource', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 63, 2), )

    
    OtherSource = property(__OtherSource.value, __OtherSource.set, None, 'Reference to a source of metadata describing coverage\n      offerings available from this server. This parameter can reference a\n      catalogue server from which dataset metadata is available. This ability\n      is expected to be used by servers with thousands or millions of\n      datasets, for which searching a catalogue is more feasible than fetching\n      a long Capabilities XML document. When no DatasetDescriptionSummaries\n      are included, and one or more catalogue servers are referenced, this set\n      of catalogues shall contain current metadata summaries for all the\n      datasets currently available from this OWS server, with the metadata for\n      each such dataset referencing this OWS server.')

    
    # Element {http://www.opengis.net/ows/2.0}DatasetDescriptionSummary uses Python identifier DatasetDescriptionSummary
    __DatasetDescriptionSummary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DatasetDescriptionSummary'), 'DatasetDescriptionSummary', '__httpwww_opengis_netows2_0_ContentsBaseType_httpwww_opengis_netows2_0DatasetDescriptionSummary', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 79, 2), )

    
    DatasetDescriptionSummary = property(__DatasetDescriptionSummary.value, __DatasetDescriptionSummary.set, None, None)

    _ElementMap.update({
        __OtherSource.name() : __OtherSource,
        __DatasetDescriptionSummary.name() : __DatasetDescriptionSummary
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ContentsBaseType = ContentsBaseType
Namespace.addCategoryObject('typeBinding', 'ContentsBaseType', ContentsBaseType)


# Complex type {http://www.opengis.net/ows/2.0}DescriptionType with content type ELEMENT_ONLY
class DescriptionType (pyxb.binding.basis.complexTypeDefinition):
    """Human-readable descriptive information for the object it
      is included within. This type shall be extended if needed for specific
      OWS use to include additional metadata for each type of information.
      This type shall not be restricted for a specific OWS to change the
      multiplicity (or optionality) of some elements. If the xml:lang
      attribute is not included in a Title, Abstract or Keyword element, then
      no language is specified for that element unless specified by another
      means. All Title, Abstract and Keyword elements in the same Description
      that share the same xml:lang attribute value represent the description
      of the parent object in that language. Multiple Title or Abstract
      elements shall not exist in the same Description with the same xml:lang
      attribute value unless otherwise specified."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DescriptionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 34, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Title'), 'Title', '__httpwww_opengis_netows2_0_DescriptionType_httpwww_opengis_netows2_0Title', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 51, 2), )

    
    Title = property(__Title.value, __Title.set, None, 'Title of this resource, normally used for display to\n      humans.')

    
    # Element {http://www.opengis.net/ows/2.0}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Abstract'), 'Abstract', '__httpwww_opengis_netows2_0_DescriptionType_httpwww_opengis_netows2_0Abstract', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 59, 2), )

    
    Abstract = property(__Abstract.value, __Abstract.set, None, 'Brief narrative description of this resource, normally\n      used for display to humans.')

    
    # Element {http://www.opengis.net/ows/2.0}Keywords uses Python identifier Keywords
    __Keywords = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Keywords'), 'Keywords', '__httpwww_opengis_netows2_0_DescriptionType_httpwww_opengis_netows2_0Keywords', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 67, 2), )

    
    Keywords = property(__Keywords.value, __Keywords.set, None, None)

    _ElementMap.update({
        __Title.name() : __Title,
        __Abstract.name() : __Abstract,
        __Keywords.name() : __Keywords
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DescriptionType = DescriptionType
Namespace.addCategoryObject('typeBinding', 'DescriptionType', DescriptionType)


# Complex type {http://www.opengis.net/ows/2.0}UnNamedDomainType with content type ELEMENT_ONLY
class UnNamedDomainType (pyxb.binding.basis.complexTypeDefinition):
    """Valid domain (or allowed set of values) of one quantity,
      with needed metadata but without a quantity name or
      identifier."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnNamedDomainType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 54, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), 'Metadata', '__httpwww_opengis_netows2_0_UnNamedDomainType_httpwww_opengis_netows2_0Metadata', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 57, 2), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows/2.0}AnyValue uses Python identifier AnyValue
    __AnyValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AnyValue'), 'AnyValue', '__httpwww_opengis_netows2_0_UnNamedDomainType_httpwww_opengis_netows2_0AnyValue', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 118, 2), )

    
    AnyValue = property(__AnyValue.value, __AnyValue.set, None, 'Specifies that any value is allowed for this\n      parameter.')

    
    # Element {http://www.opengis.net/ows/2.0}NoValues uses Python identifier NoValues
    __NoValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NoValues'), 'NoValues', '__httpwww_opengis_netows2_0_UnNamedDomainType_httpwww_opengis_netows2_0NoValues', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 126, 2), )

    
    NoValues = property(__NoValues.value, __NoValues.set, None, 'Specifies that no values are allowed for this parameter\n      or quantity.')

    
    # Element {http://www.opengis.net/ows/2.0}ValuesReference uses Python identifier ValuesReference
    __ValuesReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValuesReference'), 'ValuesReference', '__httpwww_opengis_netows2_0_UnNamedDomainType_httpwww_opengis_netows2_0ValuesReference', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 134, 2), )

    
    ValuesReference = property(__ValuesReference.value, __ValuesReference.set, None, 'Reference to externally specified list of all the valid\n      values and/or ranges of values for this quantity. (Informative: This\n      element was simplified from the metaDataProperty element in GML\n      3.0.)')

    
    # Element {http://www.opengis.net/ows/2.0}AllowedValues uses Python identifier AllowedValues
    __AllowedValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AllowedValues'), 'AllowedValues', '__httpwww_opengis_netows2_0_UnNamedDomainType_httpwww_opengis_netows2_0AllowedValues', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 181, 2), )

    
    AllowedValues = property(__AllowedValues.value, __AllowedValues.set, None, 'List of all the valid values and/or ranges of values for\n      this quantity. For numeric quantities, signed values should be ordered\n      from negative infinity to positive infinity.')

    
    # Element {http://www.opengis.net/ows/2.0}DefaultValue uses Python identifier DefaultValue
    __DefaultValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DefaultValue'), 'DefaultValue', '__httpwww_opengis_netows2_0_UnNamedDomainType_httpwww_opengis_netows2_0DefaultValue', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 209, 2), )

    
    DefaultValue = property(__DefaultValue.value, __DefaultValue.set, None, 'The default value for a quantity for which multiple\n      values are allowed.')

    
    # Element {http://www.opengis.net/ows/2.0}Meaning uses Python identifier Meaning
    __Meaning = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Meaning'), 'Meaning', '__httpwww_opengis_netows2_0_UnNamedDomainType_httpwww_opengis_netows2_0Meaning', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 344, 2), )

    
    Meaning = property(__Meaning.value, __Meaning.set, None, 'Definition of the meaning or semantics of this set of\n      values. This Meaning can provide more specific, complete, precise,\n      machine accessible, and machine understandable semantics about this\n      quantity, relative to other available semantic information. For example,\n      other semantic information is often provided in "documentation" elements\n      in XML Schemas or "description" elements in GML objects.')

    
    # Element {http://www.opengis.net/ows/2.0}DataType uses Python identifier DataType
    __DataType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataType'), 'DataType', '__httpwww_opengis_netows2_0_UnNamedDomainType_httpwww_opengis_netows2_0DataType', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 356, 2), )

    
    DataType = property(__DataType.value, __DataType.set, None, 'Definition of the data type of this set of values. In\n      this case, the xlink:href attribute can reference a URN for a well-known\n      data type. For example, such a URN could be a data type identification\n      URN defined in the "ogc" URN namespace.')

    
    # Element {http://www.opengis.net/ows/2.0}ReferenceSystem uses Python identifier ReferenceSystem
    __ReferenceSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReferenceSystem'), 'ReferenceSystem', '__httpwww_opengis_netows2_0_UnNamedDomainType_httpwww_opengis_netows2_0ReferenceSystem', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 366, 2), )

    
    ReferenceSystem = property(__ReferenceSystem.value, __ReferenceSystem.set, None, 'Definition of the reference system used by this set of\n      values, including the unit of measure whenever applicable (as is\n      normal). In this case, the xlink:href attribute can reference a URN for\n      a well-known reference system, such as for a coordinate reference system\n      (CRS). For example, such a URN could be a CRS identification URN defined\n      in the "ogc" URN namespace.')

    
    # Element {http://www.opengis.net/ows/2.0}UOM uses Python identifier UOM
    __UOM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UOM'), 'UOM', '__httpwww_opengis_netows2_0_UnNamedDomainType_httpwww_opengis_netows2_0UOM', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 378, 2), )

    
    UOM = property(__UOM.value, __UOM.set, None, 'Definition of the unit of measure of this set of values.\n      In this case, the xlink:href attribute can reference a URN for a\n      well-known unit of measure (uom). For example, such a URN could be a UOM\n      identification URN defined in the "ogc" URN namespace.')

    _ElementMap.update({
        __Metadata.name() : __Metadata,
        __AnyValue.name() : __AnyValue,
        __NoValues.name() : __NoValues,
        __ValuesReference.name() : __ValuesReference,
        __AllowedValues.name() : __AllowedValues,
        __DefaultValue.name() : __DefaultValue,
        __Meaning.name() : __Meaning,
        __DataType.name() : __DataType,
        __ReferenceSystem.name() : __ReferenceSystem,
        __UOM.name() : __UOM
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UnNamedDomainType = UnNamedDomainType
Namespace.addCategoryObject('typeBinding', 'UnNamedDomainType', UnNamedDomainType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Specifies that any value is allowed for this
      parameter."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 123, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Specifies that no values are allowed for this parameter
      or quantity."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 131, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Reference to externally specified list of all the valid
      values and/or ranges of values for this quantity. (Informative: This
      element was simplified from the metaDataProperty element in GML
      3.0.)"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 141, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.opengis.net/ows/2.0}reference uses Python identifier reference
    __reference = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'reference'), 'reference', '__httpwww_opengis_netows2_0_CTD_ANON_3_httpwww_opengis_netows2_0reference', pyxb.binding.datatypes.anyURI, required=True)
    __reference._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 332, 2)
    __reference._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 149, 10)
    
    reference = property(__reference.value, __reference.set, None, 'Reference to data or metadata recorded elsewhere, either\n      external to this XML document or within it. Whenever practical, this\n      attribute should be a URL from which this metadata can be electronically\n      retrieved. Alternately, this attribute can reference a URN for\n      well-known metadata. For example, such a URN could be a URN defined in\n      the "ogc" URN namespace.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __reference.name() : __reference
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """List of all the valid values and/or ranges of values for
      this quantity. For numeric quantities, signed values should be ordered
      from negative infinity to positive infinity."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 187, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Value'), 'Value', '__httpwww_opengis_netows2_0_CTD_ANON_4_httpwww_opengis_netows2_0Value', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 195, 2), )

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element {http://www.opengis.net/ows/2.0}Range uses Python identifier Range
    __Range = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Range'), 'Range', '__httpwww_opengis_netows2_0_CTD_ANON_4_httpwww_opengis_netows2_0Range', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 217, 2), )

    
    Range = property(__Range.value, __Range.set, None, None)

    _ElementMap.update({
        __Value.name() : __Value,
        __Range.name() : __Range
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type {http://www.opengis.net/ows/2.0}ValueType with content type SIMPLE
class ValueType (pyxb.binding.basis.complexTypeDefinition):
    """A single value, encoded as a string. This type can be
      used for one value, for a spacing between allowed values, or for the
      default value of a parameter."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValueType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 198, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ValueType = ValueType
Namespace.addCategoryObject('typeBinding', 'ValueType', ValueType)


# Complex type {http://www.opengis.net/ows/2.0}DomainMetadataType with content type SIMPLE
class DomainMetadataType (pyxb.binding.basis.complexTypeDefinition):
    """References metadata about a quantity, and provides a name
      for this metadata. (Informative: This element was simplified from the
      metaDataProperty element in GML 3.0.)"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DomainMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 314, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.opengis.net/ows/2.0}reference uses Python identifier reference
    __reference = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'reference'), 'reference', '__httpwww_opengis_netows2_0_DomainMetadataType_httpwww_opengis_netows2_0reference', pyxb.binding.datatypes.anyURI)
    __reference._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 332, 2)
    __reference._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 326, 8)
    
    reference = property(__reference.value, __reference.set, None, 'Reference to data or metadata recorded elsewhere, either\n      external to this XML document or within it. Whenever practical, this\n      attribute should be a URL from which this metadata can be electronically\n      retrieved. Alternately, this attribute can reference a URN for\n      well-known metadata. For example, such a URN could be a URN defined in\n      the "ogc" URN namespace.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __reference.name() : __reference
    })
_module_typeBindings.DomainMetadataType = DomainMetadataType
Namespace.addCategoryObject('typeBinding', 'DomainMetadataType', DomainMetadataType)


# Complex type {http://www.opengis.net/ows/2.0}ExceptionType with content type ELEMENT_ONLY
class ExceptionType (pyxb.binding.basis.complexTypeDefinition):
    """An Exception element describes one detected error that a
      server chooses to convey to the client."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExceptionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 81, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}ExceptionText uses Python identifier ExceptionText
    __ExceptionText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExceptionText'), 'ExceptionText', '__httpwww_opengis_netows2_0_ExceptionType_httpwww_opengis_netows2_0ExceptionText', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 87, 6), )

    
    ExceptionText = property(__ExceptionText.value, __ExceptionText.set, None, 'Ordered sequence of text strings that describe this\n          specific exception or error. The contents of these strings are left\n          open to definition by each server implementation. A server is\n          strongly encouraged to include at least one ExceptionText value, to\n          provide more information about the detected error than provided by\n          the exceptionCode. When included, multiple ExceptionText values\n          shall provide hierarchical information about one detected error,\n          with the most significant information listed first.')

    
    # Attribute exceptionCode uses Python identifier exceptionCode
    __exceptionCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'exceptionCode'), 'exceptionCode', '__httpwww_opengis_netows2_0_ExceptionType_exceptionCode', pyxb.binding.datatypes.string, required=True)
    __exceptionCode._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 103, 4)
    __exceptionCode._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 103, 4)
    
    exceptionCode = property(__exceptionCode.value, __exceptionCode.set, None, 'A code representing the type of this exception, which\n        shall be selected from a set of exceptionCode values specified for the\n        specific service operation and server.')

    
    # Attribute locator uses Python identifier locator
    __locator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'locator'), 'locator', '__httpwww_opengis_netows2_0_ExceptionType_locator', pyxb.binding.datatypes.string)
    __locator._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 112, 4)
    __locator._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 112, 4)
    
    locator = property(__locator.value, __locator.set, None, "When included, this locator shall indicate to the\n        client where an exception was encountered in servicing the client's\n        operation request. This locator should be included whenever meaningful\n        information can be provided by the server. The contents of this\n        locator will depend on the specific exceptionCode and OWS service, and\n        shall be specified in the OWS Implementation\n        Specification.")

    _ElementMap.update({
        __ExceptionText.name() : __ExceptionText
    })
    _AttributeMap.update({
        __exceptionCode.name() : __exceptionCode,
        __locator.name() : __locator
    })
_module_typeBindings.ExceptionType = ExceptionType
Namespace.addCategoryObject('typeBinding', 'ExceptionType', ExceptionType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """The list of languages that this service is able to
          fully support. That is, if one of the listed languages is requested
          using the AcceptLanguages parameter in future requests to the
          server, all text strings contained in the response are guaranteed to
          be in that language. This list does not necessarily constitute a
          complete list of all languages that may be (at least partially)
          supported by the server. It only states the languages that are fully
          supported. If a server cannot guarantee full support of any
          particular language, it shall omit it from the list of supported
          languages in the capabilities document."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 69, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}Language uses Python identifier Language
    __Language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Language'), 'Language', '__httpwww_opengis_netows2_0_CTD_ANON_5_httpwww_opengis_netows2_0Language', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 190, 2), )

    
    Language = property(__Language.value, __Language.set, None, 'Identifier of a language used by the data(set) contents.\n      This language identifier shall be as specified in IETF RFC 4646. The\n      language tags shall be either complete 5 character codes (e.g. "en-CA"),\n      or abbreviated 2 character codes (e.g. "en"). In addition to the RFC\n      4646 codes, the server shall support the single special value "*" which\n      is used to indicate "any language".')

    _ElementMap.update({
        __Language.name() : __Language
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Ordered list of languages desired by the client for
          all human readable text in the response, in order of preference. For
          every element, the first matching language available from the server
          shall be present in the response."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 140, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}Language uses Python identifier Language
    __Language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Language'), 'Language', '__httpwww_opengis_netows2_0_CTD_ANON_6_httpwww_opengis_netows2_0Language', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 190, 2), )

    
    Language = property(__Language.value, __Language.set, None, 'Identifier of a language used by the data(set) contents.\n      This language identifier shall be as specified in IETF RFC 4646. The\n      language tags shall be either complete 5 character codes (e.g. "en-CA"),\n      or abbreviated 2 character codes (e.g. "en"). In addition to the RFC\n      4646 codes, the server shall support the single special value "*" which\n      is used to indicate "any language".')

    _ElementMap.update({
        __Language.name() : __Language
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type {http://www.opengis.net/ows/2.0}AcceptVersionsType with content type ELEMENT_ONLY
class AcceptVersionsType (pyxb.binding.basis.complexTypeDefinition):
    """Prioritized sequence of one or more specification
      versions accepted by client, with preferred versions listed first. See
      Version negotiation subclause for more information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AcceptVersionsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 166, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Version'), 'Version', '__httpwww_opengis_netows2_0_AcceptVersionsType_httpwww_opengis_netows2_0Version', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 173, 6), )

    
    Version = property(__Version.value, __Version.set, None, None)

    _ElementMap.update({
        __Version.name() : __Version
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AcceptVersionsType = AcceptVersionsType
Namespace.addCategoryObject('typeBinding', 'AcceptVersionsType', AcceptVersionsType)


# Complex type {http://www.opengis.net/ows/2.0}SectionsType with content type ELEMENT_ONLY
class SectionsType (pyxb.binding.basis.complexTypeDefinition):
    """Unordered list of zero or more names of requested
      sections in complete service metadata document. Each Section value shall
      contain an allowed section name as specified by each OWS specification.
      See Sections parameter subclause for more information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SectionsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 179, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}Section uses Python identifier Section
    __Section = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Section'), 'Section', '__httpwww_opengis_netows2_0_SectionsType_httpwww_opengis_netows2_0Section', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 187, 6), )

    
    Section = property(__Section.value, __Section.set, None, None)

    _ElementMap.update({
        __Section.name() : __Section
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SectionsType = SectionsType
Namespace.addCategoryObject('typeBinding', 'SectionsType', SectionsType)


# Complex type {http://www.opengis.net/ows/2.0}AcceptFormatsType with content type ELEMENT_ONLY
class AcceptFormatsType (pyxb.binding.basis.complexTypeDefinition):
    """Prioritized sequence of zero or more GetCapabilities
      operation response formats desired by client, with preferred formats
      listed first. Each response format shall be identified by its MIME type.
      See AcceptFormats parameter use subclause for more
      information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AcceptFormatsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 205, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}OutputFormat uses Python identifier OutputFormat
    __OutputFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), 'OutputFormat', '__httpwww_opengis_netows2_0_AcceptFormatsType_httpwww_opengis_netows2_0OutputFormat', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 214, 6), )

    
    OutputFormat = property(__OutputFormat.value, __OutputFormat.set, None, None)

    _ElementMap.update({
        __OutputFormat.name() : __OutputFormat
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AcceptFormatsType = AcceptFormatsType
Namespace.addCategoryObject('typeBinding', 'AcceptFormatsType', AcceptFormatsType)


# Complex type {http://www.opengis.net/ows/2.0}AbstractReferenceBaseType with content type EMPTY
class AbstractReferenceBaseType (pyxb.binding.basis.complexTypeDefinition):
    """Base for a reference to a remote or local
      resource.This type contains only a restricted and annotated set of
      the attributes from the xlink:simpleAttrs attributeGroup."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractReferenceBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 37, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.opengis.net/ows/2.0}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__httpwww_opengis_netows2_0_AbstractReferenceBaseType_httpwww_opengis_netows2_0type', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 44, 4)
    __type._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 44, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netows2_0_AbstractReferenceBaseType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType, required=True)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 48, 4)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netows2_0_AbstractReferenceBaseType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 57, 4)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netows2_0_AbstractReferenceBaseType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 65, 4)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netows2_0_AbstractReferenceBaseType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 72, 4)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netows2_0_AbstractReferenceBaseType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 79, 4)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netows2_0_AbstractReferenceBaseType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 86, 4)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.AbstractReferenceBaseType = AbstractReferenceBaseType
Namespace.addCategoryObject('typeBinding', 'AbstractReferenceBaseType', AbstractReferenceBaseType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Metadata about the operations and related abilities
      specified by this service and implemented by this server, including the
      URLs for operation requests. The basic contents of this section shall be
      the same for all OWS types, but individual services can add elements
      and/or change the optionality of optional elements."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 38, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}Parameter uses Python identifier Parameter
    __Parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Parameter'), 'Parameter', '__httpwww_opengis_netows2_0_CTD_ANON_7_httpwww_opengis_netows2_0Parameter', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 50, 8), )

    
    Parameter = property(__Parameter.value, __Parameter.set, None, 'Optional unordered list of parameter valid domains\n            that each apply to one or more operations which this server\n            interface implements. The list of required and optional parameter\n            domain limitations shall be specified in the Implementation\n            Specification for this service.')

    
    # Element {http://www.opengis.net/ows/2.0}Constraint uses Python identifier Constraint
    __Constraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), 'Constraint', '__httpwww_opengis_netows2_0_CTD_ANON_7_httpwww_opengis_netows2_0Constraint', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 62, 8), )

    
    Constraint = property(__Constraint.value, __Constraint.set, None, 'Optional unordered list of valid domain constraints\n            on non-parameter quantities that each apply to this server. The\n            list of required and optional constraints shall be specified in\n            the Implementation Specification for this service.')

    
    # Element {http://www.opengis.net/ows/2.0}ExtendedCapabilities uses Python identifier ExtendedCapabilities
    __ExtendedCapabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExtendedCapabilities'), 'ExtendedCapabilities', '__httpwww_opengis_netows2_0_CTD_ANON_7_httpwww_opengis_netows2_0ExtendedCapabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 79, 2), )

    
    ExtendedCapabilities = property(__ExtendedCapabilities.value, __ExtendedCapabilities.set, None, 'Individual software vendors and servers can use this\n      element to provide metadata about any additional server\n      abilities.')

    
    # Element {http://www.opengis.net/ows/2.0}Operation uses Python identifier Operation
    __Operation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Operation'), 'Operation', '__httpwww_opengis_netows2_0_CTD_ANON_7_httpwww_opengis_netows2_0Operation', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 88, 2), )

    
    Operation = property(__Operation.value, __Operation.set, None, 'Metadata for one operation that this server\n      implements.')

    _ElementMap.update({
        __Parameter.name() : __Parameter,
        __Constraint.name() : __Constraint,
        __ExtendedCapabilities.name() : __ExtendedCapabilities,
        __Operation.name() : __Operation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Metadata for one operation that this server
      implements."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 93, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), 'Metadata', '__httpwww_opengis_netows2_0_CTD_ANON_8_httpwww_opengis_netows2_0Metadata', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 57, 2), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows/2.0}Parameter uses Python identifier Parameter
    __Parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Parameter'), 'Parameter', '__httpwww_opengis_netows2_0_CTD_ANON_8_httpwww_opengis_netows2_0Parameter', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 103, 8), )

    
    Parameter = property(__Parameter.value, __Parameter.set, None, 'Optional unordered list of parameter domains that\n            each apply to this operation which this server implements. If one\n            of these Parameter elements has the same "name" attribute as a\n            Parameter element in the OperationsMetadata element, this\n            Parameter element shall override the other one for this operation.\n            The list of required and optional parameter domain limitations for\n            this operation shall be specified in the Implementation\n            Specification for this service.')

    
    # Element {http://www.opengis.net/ows/2.0}Constraint uses Python identifier Constraint
    __Constraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), 'Constraint', '__httpwww_opengis_netows2_0_CTD_ANON_8_httpwww_opengis_netows2_0Constraint', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 118, 8), )

    
    Constraint = property(__Constraint.value, __Constraint.set, None, 'Optional unordered list of valid domain constraints\n            on non-parameter quantities that each apply to this operation. If\n            one of these Constraint elements has the same "name" attribute as\n            a Constraint element in the OperationsMetadata element, this\n            Constraint element shall override the other one for this\n            operation. The list of required and optional constraints for this\n            operation shall be specified in the Implementation Specification\n            for this service.')

    
    # Element {http://www.opengis.net/ows/2.0}DCP uses Python identifier DCP
    __DCP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DCP'), 'DCP', '__httpwww_opengis_netows2_0_CTD_ANON_8_httpwww_opengis_netows2_0DCP', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 160, 2), )

    
    DCP = property(__DCP.value, __DCP.set, None, 'Information for one distributed Computing Platform (DCP)\n      supported for this operation. At present, only the HTTP DCP is defined,\n      so this element only includes the HTTP element.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netows2_0_CTD_ANON_8_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 147, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 147, 6)
    
    name = property(__name.value, __name.set, None, 'Name or identifier of this operation (request) (for\n          example, GetCapabilities). The list of required and optional\n          operations implemented shall be specified in the Implementation\n          Specification for this service.')

    _ElementMap.update({
        __Metadata.name() : __Metadata,
        __Parameter.name() : __Parameter,
        __Constraint.name() : __Constraint,
        __DCP.name() : __DCP
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Information for one distributed Computing Platform (DCP)
      supported for this operation. At present, only the HTTP DCP is defined,
      so this element only includes the HTTP element."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 166, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}HTTP uses Python identifier HTTP
    __HTTP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HTTP'), 'HTTP', '__httpwww_opengis_netows2_0_CTD_ANON_9_httpwww_opengis_netows2_0HTTP', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 173, 2), )

    
    HTTP = property(__HTTP.value, __HTTP.set, None, 'Connect point URLs for the HTTP Distributed Computing\n      Platform (DCP). Normally, only one Get and/or one Post is included in\n      this element. More than one Get and/or Post is allowed to support\n      including alternative URLs for uses such as load balancing or\n      backup.')

    _ElementMap.update({
        __HTTP.name() : __HTTP
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Connect point URLs for the HTTP Distributed Computing
      Platform (DCP). Normally, only one Get and/or one Post is included in
      this element. More than one Get and/or Post is allowed to support
      including alternative URLs for uses such as load balancing or
      backup."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 181, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}Get uses Python identifier Get
    __Get = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Get'), 'Get', '__httpwww_opengis_netows2_0_CTD_ANON_10_httpwww_opengis_netows2_0Get', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 183, 8), )

    
    Get = property(__Get.value, __Get.set, None, 'Connect point URL prefix and any constraints for\n            the HTTP "Get" request method for this operation\n            request.')

    
    # Element {http://www.opengis.net/ows/2.0}Post uses Python identifier Post
    __Post = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Post'), 'Post', '__httpwww_opengis_netows2_0_CTD_ANON_10_httpwww_opengis_netows2_0Post', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 191, 8), )

    
    Post = property(__Post.value, __Post.set, None, 'Connect point URL and any constraints for the HTTP\n            "Post" request method for this operation request.')

    _ElementMap.update({
        __Get.name() : __Get,
        __Post.name() : __Post
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Metadata about the organization that provides this
      specific service instance or server."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceProvider.xsd', 35, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}ProviderName uses Python identifier ProviderName
    __ProviderName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProviderName'), 'ProviderName', '__httpwww_opengis_netows2_0_CTD_ANON_11_httpwww_opengis_netows2_0ProviderName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceProvider.xsd', 37, 8), )

    
    ProviderName = property(__ProviderName.value, __ProviderName.set, None, 'A unique identifier for the service provider\n            organization.')

    
    # Element {http://www.opengis.net/ows/2.0}ProviderSite uses Python identifier ProviderSite
    __ProviderSite = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProviderSite'), 'ProviderSite', '__httpwww_opengis_netows2_0_CTD_ANON_11_httpwww_opengis_netows2_0ProviderSite', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceProvider.xsd', 44, 8), )

    
    ProviderSite = property(__ProviderSite.value, __ProviderSite.set, None, 'Reference to the most relevant web site of the\n            service provider.')

    
    # Element {http://www.opengis.net/ows/2.0}ServiceContact uses Python identifier ServiceContact
    __ServiceContact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceContact'), 'ServiceContact', '__httpwww_opengis_netows2_0_CTD_ANON_11_httpwww_opengis_netows2_0ServiceContact', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceProvider.xsd', 52, 8), )

    
    ServiceContact = property(__ServiceContact.value, __ServiceContact.set, None, 'Information for contacting the service provider.\n            The OnlineResource element within this ServiceContact element\n            should not be used to reference a web site of the service\n            provider.')

    _ElementMap.update({
        __ProviderName.name() : __ProviderName,
        __ProviderSite.name() : __ProviderSite,
        __ServiceContact.name() : __ServiceContact
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type {http://www.opengis.net/ows/2.0}AdditionalParametersBaseType with content type ELEMENT_ONLY
class AdditionalParametersBaseType (MetadataType):
    """Complex type {http://www.opengis.net/ows/2.0}AdditionalParametersBaseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdditionalParametersBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 44, 2)
    _ElementMap = MetadataType._ElementMap.copy()
    _AttributeMap = MetadataType._AttributeMap.copy()
    # Base type is MetadataType
    
    # Element {http://www.opengis.net/ows/2.0}AdditionalParameter uses Python identifier AdditionalParameter
    __AdditionalParameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdditionalParameter'), 'AdditionalParameter', '__httpwww_opengis_netows2_0_AdditionalParametersBaseType_httpwww_opengis_netows2_0AdditionalParameter', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 66, 2), )

    
    AdditionalParameter = property(__AdditionalParameter.value, __AdditionalParameter.set, None, 'One additional metadata parameter.')

    
    # Attribute about inherited from {http://www.opengis.net/ows/2.0}MetadataType
    
    # Attribute type inherited from {http://www.opengis.net/ows/2.0}MetadataType
    
    # Attribute href inherited from {http://www.opengis.net/ows/2.0}MetadataType
    
    # Attribute role inherited from {http://www.opengis.net/ows/2.0}MetadataType
    
    # Attribute arcrole inherited from {http://www.opengis.net/ows/2.0}MetadataType
    
    # Attribute title inherited from {http://www.opengis.net/ows/2.0}MetadataType
    
    # Attribute show inherited from {http://www.opengis.net/ows/2.0}MetadataType
    
    # Attribute actuate inherited from {http://www.opengis.net/ows/2.0}MetadataType
    _ElementMap.update({
        __AdditionalParameter.name() : __AdditionalParameter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AdditionalParametersBaseType = AdditionalParametersBaseType
Namespace.addCategoryObject('typeBinding', 'AdditionalParametersBaseType', AdditionalParametersBaseType)


# Complex type {http://www.opengis.net/ows/2.0}NilValueType with content type SIMPLE
class NilValueType (CodeType):
    """The value used (e.g. -255) to represent a nil value with
      optional nilReason and codeSpace attributes."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NilValueType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 95, 2)
    _ElementMap = CodeType._ElementMap.copy()
    _AttributeMap = CodeType._AttributeMap.copy()
    # Base type is CodeType
    
    # Attribute codeSpace inherited from {http://www.opengis.net/ows/2.0}CodeType
    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netows2_0_NilValueType_nilReason', pyxb.binding.datatypes.anyURI)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 102, 8)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 102, 8)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, 'An anyURI value which refers to a resource that\n            describes the reason for the nil value')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason
    })
_module_typeBindings.NilValueType = NilValueType
Namespace.addCategoryObject('typeBinding', 'NilValueType', NilValueType)


# Complex type {http://www.opengis.net/ows/2.0}WGS84BoundingBoxType with content type ELEMENT_ONLY
class WGS84BoundingBoxType (BoundingBoxType):
    """XML encoded minimum rectangular bounding box (or region)
      parameter, surrounding all the associated data. This box is specialized
      for use with the 2D WGS 84 coordinate reference system with decimal
      values of longitude and latitude.This type is adapted from the general BoundingBoxType,
      with modified contents and documentation for use with the 2D WGS 84
      coordinate reference system."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WGS84BoundingBoxType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 196, 2)
    _ElementMap = BoundingBoxType._ElementMap.copy()
    _AttributeMap = BoundingBoxType._AttributeMap.copy()
    # Base type is BoundingBoxType
    
    # Element LowerCorner ({http://www.opengis.net/ows/2.0}LowerCorner) inherited from {http://www.opengis.net/ows/2.0}BoundingBoxType
    
    # Element UpperCorner ({http://www.opengis.net/ows/2.0}UpperCorner) inherited from {http://www.opengis.net/ows/2.0}BoundingBoxType
    
    # Attribute crs is restricted from parent
    
    # Attribute crs uses Python identifier crs
    __crs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'crs'), 'crs', '__httpwww_opengis_netows2_0_BoundingBoxType_crs', pyxb.binding.datatypes.anyURI, fixed=True, unicode_default='urn:ogc:def:crs:OGC:2:84')
    __crs._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 228, 8)
    __crs._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 228, 8)
    
    crs = property(__crs.value, __crs.set, None, 'This attribute can be included when considered\n            useful. When included, this attribute shall reference the 2D WGS\n            84 coordinate reference system with longitude before latitude and\n            decimal values of longitude and latitude.')

    
    # Attribute dimensions is restricted from parent
    
    # Attribute dimensions uses Python identifier dimensions
    __dimensions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dimensions'), 'dimensions', '__httpwww_opengis_netows2_0_BoundingBoxType_dimensions', pyxb.binding.datatypes.positiveInteger, fixed=True, unicode_default='2')
    __dimensions._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 239, 8)
    __dimensions._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 239, 8)
    
    dimensions = property(__dimensions.value, __dimensions.set, None, 'The number of dimensions in this CRS (the length of\n            a coordinate sequence in this use of the PositionType). This\n            number is specified by the CRS definition, but can also be\n            specified here.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __crs.name() : __crs,
        __dimensions.name() : __dimensions
    })
_module_typeBindings.WGS84BoundingBoxType = WGS84BoundingBoxType
Namespace.addCategoryObject('typeBinding', 'WGS84BoundingBoxType', WGS84BoundingBoxType)


# Complex type {http://www.opengis.net/ows/2.0}DatasetDescriptionSummaryBaseType with content type ELEMENT_ONLY
class DatasetDescriptionSummaryBaseType (DescriptionType):
    """Typical dataset metadata in typical Contents section of
      an OWS service metadata (Capabilities) document. This type shall be
      extended and/or restricted if needed for specific OWS use, to include
      the specific Dataset description metadata needed."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatasetDescriptionSummaryBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 82, 2)
    _ElementMap = DescriptionType._ElementMap.copy()
    _AttributeMap = DescriptionType._AttributeMap.copy()
    # Base type is DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/2.0}Title) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/2.0}Abstract) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/2.0}Keywords) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element {http://www.opengis.net/ows/2.0}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), 'Metadata', '__httpwww_opengis_netows2_0_DatasetDescriptionSummaryBaseType_httpwww_opengis_netows2_0Metadata', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 57, 2), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows/2.0}BoundingBox uses Python identifier BoundingBox
    __BoundingBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox'), 'BoundingBox', '__httpwww_opengis_netows2_0_DatasetDescriptionSummaryBaseType_httpwww_opengis_netows2_0BoundingBox', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 107, 2), )

    
    BoundingBox = property(__BoundingBox.value, __BoundingBox.set, None, None)

    
    # Element {http://www.opengis.net/ows/2.0}WGS84BoundingBox uses Python identifier WGS84BoundingBox
    __WGS84BoundingBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WGS84BoundingBox'), 'WGS84BoundingBox', '__httpwww_opengis_netows2_0_DatasetDescriptionSummaryBaseType_httpwww_opengis_netows2_0WGS84BoundingBox', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 192, 2), )

    
    WGS84BoundingBox = property(__WGS84BoundingBox.value, __WGS84BoundingBox.set, None, None)

    
    # Element {http://www.opengis.net/ows/2.0}DatasetDescriptionSummary uses Python identifier DatasetDescriptionSummary
    __DatasetDescriptionSummary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DatasetDescriptionSummary'), 'DatasetDescriptionSummary', '__httpwww_opengis_netows2_0_DatasetDescriptionSummaryBaseType_httpwww_opengis_netows2_0DatasetDescriptionSummary', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 79, 2), )

    
    DatasetDescriptionSummary = property(__DatasetDescriptionSummary.value, __DatasetDescriptionSummary.set, None, None)

    
    # Element {http://www.opengis.net/ows/2.0}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), 'Identifier', '__httpwww_opengis_netows2_0_DatasetDescriptionSummaryBaseType_httpwww_opengis_netows2_0Identifier', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 112, 10), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, 'Unambiguous identifier or name of this coverage,\n              unique for this server.')

    _ElementMap.update({
        __Metadata.name() : __Metadata,
        __BoundingBox.name() : __BoundingBox,
        __WGS84BoundingBox.name() : __WGS84BoundingBox,
        __DatasetDescriptionSummary.name() : __DatasetDescriptionSummary,
        __Identifier.name() : __Identifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DatasetDescriptionSummaryBaseType = DatasetDescriptionSummaryBaseType
Namespace.addCategoryObject('typeBinding', 'DatasetDescriptionSummaryBaseType', DatasetDescriptionSummaryBaseType)


# Complex type {http://www.opengis.net/ows/2.0}BasicIdentificationType with content type ELEMENT_ONLY
class BasicIdentificationType (DescriptionType):
    """Basic metadata identifying and describing a set of
      data."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BasicIdentificationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 62, 2)
    _ElementMap = DescriptionType._ElementMap.copy()
    _AttributeMap = DescriptionType._AttributeMap.copy()
    # Base type is DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/2.0}Title) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/2.0}Abstract) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/2.0}Keywords) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element {http://www.opengis.net/ows/2.0}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), 'Metadata', '__httpwww_opengis_netows2_0_BasicIdentificationType_httpwww_opengis_netows2_0Metadata', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 57, 2), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows/2.0}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), 'Identifier', '__httpwww_opengis_netows2_0_BasicIdentificationType_httpwww_opengis_netows2_0Identifier', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 133, 2), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, 'Unique identifier or name of this\n      dataset.')

    _ElementMap.update({
        __Metadata.name() : __Metadata,
        __Identifier.name() : __Identifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BasicIdentificationType = BasicIdentificationType
Namespace.addCategoryObject('typeBinding', 'BasicIdentificationType', BasicIdentificationType)


# Complex type {http://www.opengis.net/ows/2.0}DomainType with content type ELEMENT_ONLY
class DomainType (UnNamedDomainType):
    """Valid domain (or allowed set of values) of one quantity,
      with its name or identifier."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DomainType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 35, 2)
    _ElementMap = UnNamedDomainType._ElementMap.copy()
    _AttributeMap = UnNamedDomainType._AttributeMap.copy()
    # Base type is UnNamedDomainType
    
    # Element Metadata ({http://www.opengis.net/ows/2.0}Metadata) inherited from {http://www.opengis.net/ows/2.0}UnNamedDomainType
    
    # Element AnyValue ({http://www.opengis.net/ows/2.0}AnyValue) inherited from {http://www.opengis.net/ows/2.0}UnNamedDomainType
    
    # Element NoValues ({http://www.opengis.net/ows/2.0}NoValues) inherited from {http://www.opengis.net/ows/2.0}UnNamedDomainType
    
    # Element ValuesReference ({http://www.opengis.net/ows/2.0}ValuesReference) inherited from {http://www.opengis.net/ows/2.0}UnNamedDomainType
    
    # Element AllowedValues ({http://www.opengis.net/ows/2.0}AllowedValues) inherited from {http://www.opengis.net/ows/2.0}UnNamedDomainType
    
    # Element DefaultValue ({http://www.opengis.net/ows/2.0}DefaultValue) inherited from {http://www.opengis.net/ows/2.0}UnNamedDomainType
    
    # Element Meaning ({http://www.opengis.net/ows/2.0}Meaning) inherited from {http://www.opengis.net/ows/2.0}UnNamedDomainType
    
    # Element DataType ({http://www.opengis.net/ows/2.0}DataType) inherited from {http://www.opengis.net/ows/2.0}UnNamedDomainType
    
    # Element ReferenceSystem ({http://www.opengis.net/ows/2.0}ReferenceSystem) inherited from {http://www.opengis.net/ows/2.0}UnNamedDomainType
    
    # Element UOM ({http://www.opengis.net/ows/2.0}UOM) inherited from {http://www.opengis.net/ows/2.0}UnNamedDomainType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netows2_0_DomainType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 42, 8)
    __name._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 42, 8)
    
    name = property(__name.value, __name.set, None, 'Name or identifier of this\n            quantity.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.DomainType = DomainType
Namespace.addCategoryObject('typeBinding', 'DomainType', DomainType)


# Complex type {http://www.opengis.net/ows/2.0}RangeType with content type ELEMENT_ONLY
class RangeType (pyxb.binding.basis.complexTypeDefinition):
    """A range of values of a numeric parameter. This range can
      be continuous or discrete, defined by a fixed spacing between adjacent
      valid values. If the MinimumValue or MaximumValue is not included, there
      is no value limit in that direction. Inclusion of the specified minimum
      and maximum values in the range shall be defined by the
      rangeClosure."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RangeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 220, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}MinimumValue uses Python identifier MinimumValue
    __MinimumValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MinimumValue'), 'MinimumValue', '__httpwww_opengis_netows2_0_RangeType_httpwww_opengis_netows2_0MinimumValue', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 252, 2), )

    
    MinimumValue = property(__MinimumValue.value, __MinimumValue.set, None, 'Minimum value of this numeric parameter.')

    
    # Element {http://www.opengis.net/ows/2.0}MaximumValue uses Python identifier MaximumValue
    __MaximumValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MaximumValue'), 'MaximumValue', '__httpwww_opengis_netows2_0_RangeType_httpwww_opengis_netows2_0MaximumValue', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 259, 2), )

    
    MaximumValue = property(__MaximumValue.value, __MaximumValue.set, None, 'Maximum value of this numeric parameter.')

    
    # Element {http://www.opengis.net/ows/2.0}Spacing uses Python identifier Spacing
    __Spacing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Spacing'), 'Spacing', '__httpwww_opengis_netows2_0_RangeType_httpwww_opengis_netows2_0Spacing', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 266, 2), )

    
    Spacing = property(__Spacing.value, __Spacing.set, None, 'The regular distance or spacing between the allowed\n      values in a range.')

    
    # Attribute {http://www.opengis.net/ows/2.0}rangeClosure uses Python identifier rangeClosure
    __rangeClosure = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'rangeClosure'), 'rangeClosure', '__httpwww_opengis_netows2_0_RangeType_httpwww_opengis_netows2_0rangeClosure', _module_typeBindings.STD_ANON, unicode_default='closed')
    __rangeClosure._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 274, 2)
    __rangeClosure._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 243, 4)
    
    rangeClosure = property(__rangeClosure.value, __rangeClosure.set, None, 'Specifies which of the minimum and maximum values are\n      included in the range. Note that plus and minus infinity are considered\n      closed bounds.')

    _ElementMap.update({
        __MinimumValue.name() : __MinimumValue,
        __MaximumValue.name() : __MaximumValue,
        __Spacing.name() : __Spacing
    })
    _AttributeMap.update({
        __rangeClosure.name() : __rangeClosure
    })
_module_typeBindings.RangeType = RangeType
Namespace.addCategoryObject('typeBinding', 'RangeType', RangeType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Report message returned to the client that requested any
      OWS operation when the server detects an error while processing that
      operation request."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 34, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}Exception uses Python identifier Exception
    __Exception = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Exception'), 'Exception', '__httpwww_opengis_netows2_0_CTD_ANON_12_httpwww_opengis_netows2_0Exception', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 78, 2), )

    
    Exception = property(__Exception.value, __Exception.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_opengis_netows2_0_CTD_ANON_12_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 66, 6)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netows2_0_CTD_ANON_12_version', _module_typeBindings.STD_ANON_, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 46, 6)
    __version._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 46, 6)
    
    version = property(__version.value, __version.set, None, 'Specification version for OWS operation. The string\n          value shall contain one x.y.z "version" value (e.g., "2.1.3"). A\n          version number shall contain three non-negative integers separated\n          by decimal points, in the form "x.y.z". The integers y and z shall\n          not exceed 99. Each version shall be for the Implementation\n          Specification (document) and the associated XML Schemas to which\n          requested operations will conform. An Implementation Specification\n          version normally specifies XML Schemas against which an XML encoded\n          operation response must conform and should be validated. See Version\n          negotiation subclause for more information.')

    _ElementMap.update({
        __Exception.name() : __Exception
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __version.name() : __version
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type {http://www.opengis.net/ows/2.0}CapabilitiesBaseType with content type ELEMENT_ONLY
class CapabilitiesBaseType (pyxb.binding.basis.complexTypeDefinition):
    """XML encoded GetCapabilities operation response. This
      document provides clients with service metadata about a specific service
      instance, usually including metadata about the tightly-coupled data
      served. If the server does not implement the updateSequence parameter,
      the server shall always return the complete Capabilities document,
      without the updateSequence parameter. When the server implements the
      updateSequence parameter and the GetCapabilities operation request
      included the updateSequence parameter with the current value, the server
      shall return this element with only the "version" and "updateSequence"
      attributes. Otherwise, all optional elements shall be included or not
      depending on the actual value of the Contents parameter in the
      GetCapabilities operation request. This base type shall be extended by
      each specific OWS to include the additional contents
      needed."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CapabilitiesBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 31, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}Languages uses Python identifier Languages
    __Languages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Languages'), 'Languages', '__httpwww_opengis_netows2_0_CapabilitiesBaseType_httpwww_opengis_netows2_0Languages', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 55, 6), )

    
    Languages = property(__Languages.value, __Languages.set, None, 'The list of languages that this service is able to\n          fully support. That is, if one of the listed languages is requested\n          using the AcceptLanguages parameter in future requests to the\n          server, all text strings contained in the response are guaranteed to\n          be in that language. This list does not necessarily constitute a\n          complete list of all languages that may be (at least partially)\n          supported by the server. It only states the languages that are fully\n          supported. If a server cannot guarantee full support of any\n          particular language, it shall omit it from the list of supported\n          languages in the capabilities document.')

    
    # Element {http://www.opengis.net/ows/2.0}OperationsMetadata uses Python identifier OperationsMetadata
    __OperationsMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OperationsMetadata'), 'OperationsMetadata', '__httpwww_opengis_netows2_0_CapabilitiesBaseType_httpwww_opengis_netows2_0OperationsMetadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 30, 2), )

    
    OperationsMetadata = property(__OperationsMetadata.value, __OperationsMetadata.set, None, 'Metadata about the operations and related abilities\n      specified by this service and implemented by this server, including the\n      URLs for operation requests. The basic contents of this section shall be\n      the same for all OWS types, but individual services can add elements\n      and/or change the optionality of optional elements.')

    
    # Element {http://www.opengis.net/ows/2.0}ServiceIdentification uses Python identifier ServiceIdentification
    __ServiceIdentification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceIdentification'), 'ServiceIdentification', '__httpwww_opengis_netows2_0_CapabilitiesBaseType_httpwww_opengis_netows2_0ServiceIdentification', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 31, 2), )

    
    ServiceIdentification = property(__ServiceIdentification.value, __ServiceIdentification.set, None, 'General metadata for this specific server. This XML\n      Schema of this section shall be the same for all OWS.')

    
    # Element {http://www.opengis.net/ows/2.0}ServiceProvider uses Python identifier ServiceProvider
    __ServiceProvider = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceProvider'), 'ServiceProvider', '__httpwww_opengis_netows2_0_CapabilitiesBaseType_httpwww_opengis_netows2_0ServiceProvider', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceProvider.xsd', 30, 2), )

    
    ServiceProvider = property(__ServiceProvider.value, __ServiceProvider.set, None, 'Metadata about the organization that provides this\n      specific service instance or server.')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netows2_0_CapabilitiesBaseType_version', _module_typeBindings.VersionType, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 76, 4)
    __version._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 76, 4)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute updateSequence uses Python identifier updateSequence
    __updateSequence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'updateSequence'), 'updateSequence', '__httpwww_opengis_netows2_0_CapabilitiesBaseType_updateSequence', _module_typeBindings.UpdateSequenceType)
    __updateSequence._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 79, 4)
    __updateSequence._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 79, 4)
    
    updateSequence = property(__updateSequence.value, __updateSequence.set, None, 'Service metadata document version, having values that\n        are "increased" whenever any change is made in service metadata\n        document. Values are selected by each server, and are always opaque to\n        clients. When not supported by server, server shall not return this\n        attribute.')

    _ElementMap.update({
        __Languages.name() : __Languages,
        __OperationsMetadata.name() : __OperationsMetadata,
        __ServiceIdentification.name() : __ServiceIdentification,
        __ServiceProvider.name() : __ServiceProvider
    })
    _AttributeMap.update({
        __version.name() : __version,
        __updateSequence.name() : __updateSequence
    })
_module_typeBindings.CapabilitiesBaseType = CapabilitiesBaseType
Namespace.addCategoryObject('typeBinding', 'CapabilitiesBaseType', CapabilitiesBaseType)


# Complex type {http://www.opengis.net/ows/2.0}GetCapabilitiesType with content type ELEMENT_ONLY
class GetCapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    """XML encoded GetCapabilities operation request. This
      operation allows clients to retrieve service metadata about a specific
      service instance. In this XML encoding, no "request" parameter is
      included, since the element name specifies the specific operation. This
      base type shall be extended by each specific OWS to include the
      additional required "service" attribute, with the correct value for that
      OWS."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetCapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 95, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}AcceptVersions uses Python identifier AcceptVersions
    __AcceptVersions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AcceptVersions'), 'AcceptVersions', '__httpwww_opengis_netows2_0_GetCapabilitiesType_httpwww_opengis_netows2_0AcceptVersions', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 106, 6), )

    
    AcceptVersions = property(__AcceptVersions.value, __AcceptVersions.set, None, 'When omitted, server shall return latest supported\n          version.')

    
    # Element {http://www.opengis.net/ows/2.0}Sections uses Python identifier Sections
    __Sections = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Sections'), 'Sections', '__httpwww_opengis_netows2_0_GetCapabilitiesType_httpwww_opengis_netows2_0Sections', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 114, 6), )

    
    Sections = property(__Sections.value, __Sections.set, None, 'When omitted or not supported by server, server shall\n          return complete service metadata (Capabilities)\n          document.')

    
    # Element {http://www.opengis.net/ows/2.0}AcceptFormats uses Python identifier AcceptFormats
    __AcceptFormats = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AcceptFormats'), 'AcceptFormats', '__httpwww_opengis_netows2_0_GetCapabilitiesType_httpwww_opengis_netows2_0AcceptFormats', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 123, 6), )

    
    AcceptFormats = property(__AcceptFormats.value, __AcceptFormats.set, None, 'When omitted or not supported by server, server shall\n          return service metadata document using the MIME type\n          "text/xml".')

    
    # Element {http://www.opengis.net/ows/2.0}AcceptLanguages uses Python identifier AcceptLanguages
    __AcceptLanguages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AcceptLanguages'), 'AcceptLanguages', '__httpwww_opengis_netows2_0_GetCapabilitiesType_httpwww_opengis_netows2_0AcceptLanguages', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 132, 6), )

    
    AcceptLanguages = property(__AcceptLanguages.value, __AcceptLanguages.set, None, 'Ordered list of languages desired by the client for\n          all human readable text in the response, in order of preference. For\n          every element, the first matching language available from the server\n          shall be present in the response.')

    
    # Attribute updateSequence uses Python identifier updateSequence
    __updateSequence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'updateSequence'), 'updateSequence', '__httpwww_opengis_netows2_0_GetCapabilitiesType_updateSequence', _module_typeBindings.UpdateSequenceType)
    __updateSequence._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 147, 4)
    __updateSequence._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 147, 4)
    
    updateSequence = property(__updateSequence.value, __updateSequence.set, None, 'When omitted or not supported by server, server shall\n        return latest complete service metadata document.')

    _ElementMap.update({
        __AcceptVersions.name() : __AcceptVersions,
        __Sections.name() : __Sections,
        __AcceptFormats.name() : __AcceptFormats,
        __AcceptLanguages.name() : __AcceptLanguages
    })
    _AttributeMap.update({
        __updateSequence.name() : __updateSequence
    })
_module_typeBindings.GetCapabilitiesType = GetCapabilitiesType
Namespace.addCategoryObject('typeBinding', 'GetCapabilitiesType', GetCapabilitiesType)


# Complex type {http://www.opengis.net/ows/2.0}GetResourceByIdType with content type ELEMENT_ONLY
class GetResourceByIdType (pyxb.binding.basis.complexTypeDefinition):
    """Request to a service to perform the GetResourceByID
      operation. This operation allows a client to retrieve one or more
      identified resources, including datasets and resources that describe
      datasets or parameters. In this XML encoding, no "request" parameter is
      included, since the element name specifies the specific
      operation."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetResourceByIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetResourceByID.xsd', 42, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/2.0}OutputFormat uses Python identifier OutputFormat
    __OutputFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), 'OutputFormat', '__httpwww_opengis_netows2_0_GetResourceByIdType_httpwww_opengis_netows2_0OutputFormat', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 141, 2), )

    
    OutputFormat = property(__OutputFormat.value, __OutputFormat.set, None, 'Reference to a format in which this data can be encoded\n      and transferred. More specific parameter names should be used by\n      specific OWS specifications wherever applicable. More than one such\n      parameter can be included for different purposes.')

    
    # Element {http://www.opengis.net/ows/2.0}ResourceID uses Python identifier ResourceID
    __ResourceID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResourceID'), 'ResourceID', '__httpwww_opengis_netows2_0_GetResourceByIdType_httpwww_opengis_netows2_0ResourceID', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetResourceByID.xsd', 52, 6), )

    
    ResourceID = property(__ResourceID.value, __ResourceID.set, None, 'Unordered list of zero or more resource identifiers.\n          These identifiers can be listed in the Contents section of the\n          service metadata (Capabilities) document. For more information on\n          this parameter, see Subclause 9.4.2.1 of the OWS Common\n          specification.')

    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__httpwww_opengis_netows2_0_GetResourceByIdType_service', _module_typeBindings.ServiceType, required=True)
    __service._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetResourceByID.xsd', 75, 4)
    __service._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetResourceByID.xsd', 75, 4)
    
    service = property(__service.value, __service.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netows2_0_GetResourceByIdType_version', _module_typeBindings.VersionType, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetResourceByID.xsd', 78, 4)
    __version._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetResourceByID.xsd', 78, 4)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __OutputFormat.name() : __OutputFormat,
        __ResourceID.name() : __ResourceID
    })
    _AttributeMap.update({
        __service.name() : __service,
        __version.name() : __version
    })
_module_typeBindings.GetResourceByIdType = GetResourceByIdType
Namespace.addCategoryObject('typeBinding', 'GetResourceByIdType', GetResourceByIdType)


# Complex type {http://www.opengis.net/ows/2.0}ReferenceType with content type ELEMENT_ONLY
class ReferenceType (AbstractReferenceBaseType):
    """Complete reference to a remote or local resource,
      allowing including metadata about that resource."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 99, 2)
    _ElementMap = AbstractReferenceBaseType._ElementMap.copy()
    _AttributeMap = AbstractReferenceBaseType._AttributeMap.copy()
    # Base type is AbstractReferenceBaseType
    
    # Element {http://www.opengis.net/ows/2.0}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Abstract'), 'Abstract', '__httpwww_opengis_netows2_0_ReferenceType_httpwww_opengis_netows2_0Abstract', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 59, 2), )

    
    Abstract = property(__Abstract.value, __Abstract.set, None, 'Brief narrative description of this resource, normally\n      used for display to humans.')

    
    # Element {http://www.opengis.net/ows/2.0}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), 'Metadata', '__httpwww_opengis_netows2_0_ReferenceType_httpwww_opengis_netows2_0Metadata', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 57, 2), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows/2.0}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), 'Identifier', '__httpwww_opengis_netows2_0_ReferenceType_httpwww_opengis_netows2_0Identifier', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 133, 2), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, 'Unique identifier or name of this\n      dataset.')

    
    # Element {http://www.opengis.net/ows/2.0}Format uses Python identifier Format
    __Format = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Format'), 'Format', '__httpwww_opengis_netows2_0_ReferenceType_httpwww_opengis_netows2_0Format', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 117, 10), )

    
    Format = property(__Format.value, __Format.set, None, 'The format of the referenced resource. This\n              element is omitted when the mime type is indicated in the http\n              header of the reference.')

    
    # Attribute type inherited from {http://www.opengis.net/ows/2.0}AbstractReferenceBaseType
    
    # Attribute href inherited from {http://www.opengis.net/ows/2.0}AbstractReferenceBaseType
    
    # Attribute role inherited from {http://www.opengis.net/ows/2.0}AbstractReferenceBaseType
    
    # Attribute arcrole inherited from {http://www.opengis.net/ows/2.0}AbstractReferenceBaseType
    
    # Attribute title inherited from {http://www.opengis.net/ows/2.0}AbstractReferenceBaseType
    
    # Attribute show inherited from {http://www.opengis.net/ows/2.0}AbstractReferenceBaseType
    
    # Attribute actuate inherited from {http://www.opengis.net/ows/2.0}AbstractReferenceBaseType
    _ElementMap.update({
        __Abstract.name() : __Abstract,
        __Metadata.name() : __Metadata,
        __Identifier.name() : __Identifier,
        __Format.name() : __Format
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReferenceType = ReferenceType
Namespace.addCategoryObject('typeBinding', 'ReferenceType', ReferenceType)


# Complex type {http://www.opengis.net/ows/2.0}RequestMethodType with content type ELEMENT_ONLY
class RequestMethodType (OnlineResourceType):
    """Connect point URL and any constraints for this HTTP
      request method for this operation request. In the OnlineResourceType,
      the xlink:href attribute in the xlink:simpleAttrs attribute group shall
      be used to contain this URL. The other attributes in the
      xlink:simpleAttrs attribute group should not be used."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestMethodType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 202, 2)
    _ElementMap = OnlineResourceType._ElementMap.copy()
    _AttributeMap = OnlineResourceType._AttributeMap.copy()
    # Base type is OnlineResourceType
    
    # Element {http://www.opengis.net/ows/2.0}Constraint uses Python identifier Constraint
    __Constraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), 'Constraint', '__httpwww_opengis_netows2_0_RequestMethodType_httpwww_opengis_netows2_0Constraint', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 213, 10), )

    
    Constraint = property(__Constraint.value, __Constraint.set, None, 'Optional unordered list of valid domain\n              constraints on non-parameter quantities that each apply to this\n              request method for this operation. If one of these Constraint\n              elements has the same "name" attribute as a Constraint element\n              in the OperationsMetadata or Operation element, this Constraint\n              element shall override the other one for this operation. The\n              list of required and optional constraints for this request\n              method for this operation shall be specified in the\n              Implementation Specification for this service.')

    
    # Attribute type inherited from {http://www.opengis.net/ows/2.0}OnlineResourceType
    
    # Attribute href inherited from {http://www.opengis.net/ows/2.0}OnlineResourceType
    
    # Attribute role inherited from {http://www.opengis.net/ows/2.0}OnlineResourceType
    
    # Attribute arcrole inherited from {http://www.opengis.net/ows/2.0}OnlineResourceType
    
    # Attribute title inherited from {http://www.opengis.net/ows/2.0}OnlineResourceType
    
    # Attribute show inherited from {http://www.opengis.net/ows/2.0}OnlineResourceType
    
    # Attribute actuate inherited from {http://www.opengis.net/ows/2.0}OnlineResourceType
    _ElementMap.update({
        __Constraint.name() : __Constraint
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RequestMethodType = RequestMethodType
Namespace.addCategoryObject('typeBinding', 'RequestMethodType', RequestMethodType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (DescriptionType):
    """General metadata for this specific server. This XML
      Schema of this section shall be the same for all OWS."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 36, 4)
    _ElementMap = DescriptionType._ElementMap.copy()
    _AttributeMap = DescriptionType._AttributeMap.copy()
    # Base type is DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/2.0}Title) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/2.0}Abstract) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/2.0}Keywords) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element {http://www.opengis.net/ows/2.0}AccessConstraints uses Python identifier AccessConstraints
    __AccessConstraints = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AccessConstraints'), 'AccessConstraints', '__httpwww_opengis_netows2_0_CTD_ANON_13_httpwww_opengis_netows2_0AccessConstraints', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 169, 2), )

    
    AccessConstraints = property(__AccessConstraints.value, __AccessConstraints.set, None, 'Access constraint applied to assure the protection of\n      privacy or intellectual property, or any other restrictions on\n      retrieving or using data from or otherwise using this server. The\n      reserved value NONE (case insensitive) shall be used to mean no access\n      constraints are imposed.')

    
    # Element {http://www.opengis.net/ows/2.0}Fees uses Python identifier Fees
    __Fees = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Fees'), 'Fees', '__httpwww_opengis_netows2_0_CTD_ANON_13_httpwww_opengis_netows2_0Fees', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 180, 2), )

    
    Fees = property(__Fees.value, __Fees.set, None, 'Fees and terms for retrieving data from or otherwise\n      using this server, including the monetary units as specified in ISO\n      4217. The reserved value NONE (case insensitive) shall be used to mean\n      no fees or terms.')

    
    # Element {http://www.opengis.net/ows/2.0}ServiceType uses Python identifier ServiceType
    __ServiceType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceType'), 'ServiceType', '__httpwww_opengis_netows2_0_CTD_ANON_13_httpwww_opengis_netows2_0ServiceType', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 40, 12), )

    
    ServiceType = property(__ServiceType.value, __ServiceType.set, None, 'A service type name from a registry of\n                services. For example, the values of the codeSpace URI and\n                name and code string may be "OGC" and "catalogue." This type\n                name is normally used for machine-to-machine\n                communication.')

    
    # Element {http://www.opengis.net/ows/2.0}ServiceTypeVersion uses Python identifier ServiceTypeVersion
    __ServiceTypeVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceTypeVersion'), 'ServiceTypeVersion', '__httpwww_opengis_netows2_0_CTD_ANON_13_httpwww_opengis_netows2_0ServiceTypeVersion', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 50, 12), )

    
    ServiceTypeVersion = property(__ServiceTypeVersion.value, __ServiceTypeVersion.set, None, 'Unordered list of one or more versions of this\n                service type implemented by this server. This information is\n                not adequate for version negotiation, and shall not be used\n                for that purpose.')

    
    # Element {http://www.opengis.net/ows/2.0}Profile uses Python identifier Profile
    __Profile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Profile'), 'Profile', '__httpwww_opengis_netows2_0_CTD_ANON_13_httpwww_opengis_netows2_0Profile', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 60, 12), )

    
    Profile = property(__Profile.value, __Profile.set, None, 'Unordered list of identifiers of Application\n                Profiles that are implemented by this server. This element\n                should be included for each specified application profile\n                implemented by this server. The identifier value should be\n                specified by each Application Profile. If this element is\n                omitted, no meaning is implied.')

    _ElementMap.update({
        __AccessConstraints.name() : __AccessConstraints,
        __Fees.name() : __Fees,
        __ServiceType.name() : __ServiceType,
        __ServiceTypeVersion.name() : __ServiceTypeVersion,
        __Profile.name() : __Profile
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type {http://www.opengis.net/ows/2.0}AdditionalParametersType with content type ELEMENT_ONLY
class AdditionalParametersType (AdditionalParametersBaseType):
    """Complex type {http://www.opengis.net/ows/2.0}AdditionalParametersType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdditionalParametersType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 54, 2)
    _ElementMap = AdditionalParametersBaseType._ElementMap.copy()
    _AttributeMap = AdditionalParametersBaseType._AttributeMap.copy()
    # Base type is AdditionalParametersBaseType
    
    # Element AdditionalParameter ({http://www.opengis.net/ows/2.0}AdditionalParameter) inherited from {http://www.opengis.net/ows/2.0}AdditionalParametersBaseType
    
    # Attribute about inherited from {http://www.opengis.net/ows/2.0}MetadataType
    
    # Attribute type inherited from {http://www.opengis.net/ows/2.0}MetadataType
    
    # Attribute href inherited from {http://www.opengis.net/ows/2.0}MetadataType
    
    # Attribute role inherited from {http://www.opengis.net/ows/2.0}MetadataType
    
    # Attribute arcrole inherited from {http://www.opengis.net/ows/2.0}MetadataType
    
    # Attribute title inherited from {http://www.opengis.net/ows/2.0}MetadataType
    
    # Attribute show inherited from {http://www.opengis.net/ows/2.0}MetadataType
    
    # Attribute actuate inherited from {http://www.opengis.net/ows/2.0}MetadataType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AdditionalParametersType = AdditionalParametersType
Namespace.addCategoryObject('typeBinding', 'AdditionalParametersType', AdditionalParametersType)


# Complex type {http://www.opengis.net/ows/2.0}IdentificationType with content type ELEMENT_ONLY
class IdentificationType (BasicIdentificationType):
    """Extended metadata identifying and describing a set of
      data. This type shall be extended if needed for each specific OWS to
      include additional metadata for each type of dataset. If needed, this
      type should first be restricted for each specific OWS to change the
      multiplicity (or optionality) of some elements."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IdentificationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 92, 2)
    _ElementMap = BasicIdentificationType._ElementMap.copy()
    _AttributeMap = BasicIdentificationType._AttributeMap.copy()
    # Base type is BasicIdentificationType
    
    # Element Title ({http://www.opengis.net/ows/2.0}Title) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/2.0}Abstract) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/2.0}Keywords) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/2.0}Metadata) inherited from {http://www.opengis.net/ows/2.0}BasicIdentificationType
    
    # Element {http://www.opengis.net/ows/2.0}BoundingBox uses Python identifier BoundingBox
    __BoundingBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox'), 'BoundingBox', '__httpwww_opengis_netows2_0_IdentificationType_httpwww_opengis_netows2_0BoundingBox', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 107, 2), )

    
    BoundingBox = property(__BoundingBox.value, __BoundingBox.set, None, None)

    
    # Element Identifier ({http://www.opengis.net/ows/2.0}Identifier) inherited from {http://www.opengis.net/ows/2.0}BasicIdentificationType
    
    # Element {http://www.opengis.net/ows/2.0}OutputFormat uses Python identifier OutputFormat
    __OutputFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), 'OutputFormat', '__httpwww_opengis_netows2_0_IdentificationType_httpwww_opengis_netows2_0OutputFormat', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 141, 2), )

    
    OutputFormat = property(__OutputFormat.value, __OutputFormat.set, None, 'Reference to a format in which this data can be encoded\n      and transferred. More specific parameter names should be used by\n      specific OWS specifications wherever applicable. More than one such\n      parameter can be included for different purposes.')

    
    # Element {http://www.opengis.net/ows/2.0}AvailableCRS uses Python identifier AvailableCRS
    __AvailableCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AvailableCRS'), 'AvailableCRS', '__httpwww_opengis_netows2_0_IdentificationType_httpwww_opengis_netows2_0AvailableCRS', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 151, 2), )

    
    AvailableCRS = property(__AvailableCRS.value, __AvailableCRS.set, None, None)

    _ElementMap.update({
        __BoundingBox.name() : __BoundingBox,
        __OutputFormat.name() : __OutputFormat,
        __AvailableCRS.name() : __AvailableCRS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.IdentificationType = IdentificationType
Namespace.addCategoryObject('typeBinding', 'IdentificationType', IdentificationType)


# Complex type {http://www.opengis.net/ows/2.0}ServiceReferenceType with content type ELEMENT_ONLY
class ServiceReferenceType (ReferenceType):
    """Complete reference to a remote resource that needs to be
      retrieved from an OWS using an XML-encoded operation request. This
      element shall be used, within an InputData or Manifest element that is
      used for input data, when that input data needs to be retrieved from
      another web service using a XML-encoded OWS operation request. This
      element shall not be used for local payload input data or for requesting
      the resource from a web server using HTTP Get."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ServiceReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsInputOutputData.xsd', 62, 2)
    _ElementMap = ReferenceType._ElementMap.copy()
    _AttributeMap = ReferenceType._AttributeMap.copy()
    # Base type is ReferenceType
    
    # Element Abstract ({http://www.opengis.net/ows/2.0}Abstract) inherited from {http://www.opengis.net/ows/2.0}ReferenceType
    
    # Element Metadata ({http://www.opengis.net/ows/2.0}Metadata) inherited from {http://www.opengis.net/ows/2.0}ReferenceType
    
    # Element Identifier ({http://www.opengis.net/ows/2.0}Identifier) inherited from {http://www.opengis.net/ows/2.0}ReferenceType
    
    # Element {http://www.opengis.net/ows/2.0}RequestMessage uses Python identifier RequestMessage
    __RequestMessage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RequestMessage'), 'RequestMessage', '__httpwww_opengis_netows2_0_ServiceReferenceType_httpwww_opengis_netows2_0RequestMessage', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsInputOutputData.xsd', 75, 10), )

    
    RequestMessage = property(__RequestMessage.value, __RequestMessage.set, None, 'The XML-encoded operation request message to be\n              sent to request this input data from another web server using\n              HTTP Post.')

    
    # Element {http://www.opengis.net/ows/2.0}RequestMessageReference uses Python identifier RequestMessageReference
    __RequestMessageReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RequestMessageReference'), 'RequestMessageReference', '__httpwww_opengis_netows2_0_ServiceReferenceType_httpwww_opengis_netows2_0RequestMessageReference', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsInputOutputData.xsd', 83, 10), )

    
    RequestMessageReference = property(__RequestMessageReference.value, __RequestMessageReference.set, None, 'Reference to the XML-encoded operation request\n              message to be sent to request this input data from another web\n              server using HTTP Post. The referenced message shall be attached\n              to the same message (using the cid scheme), or be accessible\n              using a URL.')

    
    # Element Format ({http://www.opengis.net/ows/2.0}Format) inherited from {http://www.opengis.net/ows/2.0}ReferenceType
    
    # Attribute type inherited from {http://www.opengis.net/ows/2.0}AbstractReferenceBaseType
    
    # Attribute href inherited from {http://www.opengis.net/ows/2.0}AbstractReferenceBaseType
    
    # Attribute role inherited from {http://www.opengis.net/ows/2.0}AbstractReferenceBaseType
    
    # Attribute arcrole inherited from {http://www.opengis.net/ows/2.0}AbstractReferenceBaseType
    
    # Attribute title inherited from {http://www.opengis.net/ows/2.0}AbstractReferenceBaseType
    
    # Attribute show inherited from {http://www.opengis.net/ows/2.0}AbstractReferenceBaseType
    
    # Attribute actuate inherited from {http://www.opengis.net/ows/2.0}AbstractReferenceBaseType
    _ElementMap.update({
        __RequestMessage.name() : __RequestMessage,
        __RequestMessageReference.name() : __RequestMessageReference
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ServiceReferenceType = ServiceReferenceType
Namespace.addCategoryObject('typeBinding', 'ServiceReferenceType', ServiceReferenceType)


# Complex type {http://www.opengis.net/ows/2.0}ReferenceGroupType with content type ELEMENT_ONLY
class ReferenceGroupType (BasicIdentificationType):
    """Logical group of one or more references to remote and/or
      local resources, allowing including metadata about that group. A Group
      can be used instead of a Manifest that can only contain one
      group."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferenceGroupType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 146, 2)
    _ElementMap = BasicIdentificationType._ElementMap.copy()
    _AttributeMap = BasicIdentificationType._AttributeMap.copy()
    # Base type is BasicIdentificationType
    
    # Element Title ({http://www.opengis.net/ows/2.0}Title) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/2.0}Abstract) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/2.0}Keywords) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/2.0}Metadata) inherited from {http://www.opengis.net/ows/2.0}BasicIdentificationType
    
    # Element Identifier ({http://www.opengis.net/ows/2.0}Identifier) inherited from {http://www.opengis.net/ows/2.0}BasicIdentificationType
    
    # Element {http://www.opengis.net/ows/2.0}AbstractReferenceBase uses Python identifier AbstractReferenceBase
    __AbstractReferenceBase = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AbstractReferenceBase'), 'AbstractReferenceBase', '__httpwww_opengis_netows2_0_ReferenceGroupType_httpwww_opengis_netows2_0AbstractReferenceBase', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 33, 2), )

    
    AbstractReferenceBase = property(__AbstractReferenceBase.value, __AbstractReferenceBase.set, None, None)

    _ElementMap.update({
        __AbstractReferenceBase.name() : __AbstractReferenceBase
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReferenceGroupType = ReferenceGroupType
Namespace.addCategoryObject('typeBinding', 'ReferenceGroupType', ReferenceGroupType)


# Complex type {http://www.opengis.net/ows/2.0}ManifestType with content type ELEMENT_ONLY
class ManifestType (BasicIdentificationType):
    """Unordered list of one or more groups of references to
      remote and/or local resources."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ManifestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 166, 2)
    _ElementMap = BasicIdentificationType._ElementMap.copy()
    _AttributeMap = BasicIdentificationType._AttributeMap.copy()
    # Base type is BasicIdentificationType
    
    # Element Title ({http://www.opengis.net/ows/2.0}Title) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/2.0}Abstract) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/2.0}Keywords) inherited from {http://www.opengis.net/ows/2.0}DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/2.0}Metadata) inherited from {http://www.opengis.net/ows/2.0}BasicIdentificationType
    
    # Element Identifier ({http://www.opengis.net/ows/2.0}Identifier) inherited from {http://www.opengis.net/ows/2.0}BasicIdentificationType
    
    # Element {http://www.opengis.net/ows/2.0}ReferenceGroup uses Python identifier ReferenceGroup
    __ReferenceGroup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReferenceGroup'), 'ReferenceGroup', '__httpwww_opengis_netows2_0_ManifestType_httpwww_opengis_netows2_0ReferenceGroup', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 143, 2), )

    
    ReferenceGroup = property(__ReferenceGroup.value, __ReferenceGroup.set, None, None)

    _ElementMap.update({
        __ReferenceGroup.name() : __ReferenceGroup
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ManifestType = ManifestType
Namespace.addCategoryObject('typeBinding', 'ManifestType', ManifestType)


IndividualName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IndividualName'), pyxb.binding.datatypes.string, documentation='Name of the responsible person: surname, given name,\n      title separated by a delimiter.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 175, 2))
Namespace.addCategoryObject('elementBinding', IndividualName.name().localName(), IndividualName)

OrganisationName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrganisationName'), pyxb.binding.datatypes.string, documentation='Name of the responsible organization.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 183, 2))
Namespace.addCategoryObject('elementBinding', OrganisationName.name().localName(), OrganisationName)

PositionName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PositionName'), pyxb.binding.datatypes.string, documentation='Role or position of the responsible\n      person.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 190, 2))
Namespace.addCategoryObject('elementBinding', PositionName.name().localName(), PositionName)

AbstractMetaData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractMetaData'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), documentation='Abstract element containing more metadata about the\n      element that includes the containing "metadata" element. A specific\n      server implementation, or an Implementation Specification, can define\n      concrete elements in the AbstractMetaData substitution\n      group.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 95, 2))
Namespace.addCategoryObject('elementBinding', AbstractMetaData.name().localName(), AbstractMetaData)

AvailableCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AvailableCRS'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 151, 2))
Namespace.addCategoryObject('elementBinding', AvailableCRS.name().localName(), AvailableCRS)

SupportedCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SupportedCRS'), pyxb.binding.datatypes.anyURI, documentation='Coordinate reference system in which data from this\n      data(set) or resource is available or supported. More specific parameter\n      names should be used by specific OWS specifications wherever applicable.\n      More than one such parameter can be included for different\n      purposes.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 153, 2))
Namespace.addCategoryObject('elementBinding', SupportedCRS.name().localName(), SupportedCRS)

AccessConstraints = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AccessConstraints'), pyxb.binding.datatypes.string, documentation='Access constraint applied to assure the protection of\n      privacy or intellectual property, or any other restrictions on\n      retrieving or using data from or otherwise using this server. The\n      reserved value NONE (case insensitive) shall be used to mean no access\n      constraints are imposed.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 169, 2))
Namespace.addCategoryObject('elementBinding', AccessConstraints.name().localName(), AccessConstraints)

Fees = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Fees'), pyxb.binding.datatypes.string, documentation='Fees and terms for retrieving data from or otherwise\n      using this server, including the monetary units as specified in ISO\n      4217. The reserved value NONE (case insensitive) shall be used to mean\n      no fees or terms.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 180, 2))
Namespace.addCategoryObject('elementBinding', Fees.name().localName(), Fees)

Language = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Language'), pyxb.binding.datatypes.language, documentation='Identifier of a language used by the data(set) contents.\n      This language identifier shall be as specified in IETF RFC 4646. The\n      language tags shall be either complete 5 character codes (e.g. "en-CA"),\n      or abbreviated 2 character codes (e.g. "en"). In addition to the RFC\n      4646 codes, the server shall support the single special value "*" which\n      is used to indicate "any language".', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 190, 2))
Namespace.addCategoryObject('elementBinding', Language.name().localName(), Language)

Resource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Resource'), pyxb.binding.datatypes.anyType, documentation='XML encoded GetResourceByID operation response. The\n      complexType used by this element shall be specified by each specific\n      OWS.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetResourceByID.xsd', 31, 2))
Namespace.addCategoryObject('elementBinding', Resource.name().localName(), Resource)

ExtendedCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtendedCapabilities'), pyxb.binding.datatypes.anyType, documentation='Individual software vendors and servers can use this\n      element to provide metadata about any additional server\n      abilities.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 79, 2))
Namespace.addCategoryObject('elementBinding', ExtendedCapabilities.name().localName(), ExtendedCapabilities)

Title = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Title'), LanguageStringType, documentation='Title of this resource, normally used for display to\n      humans.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 51, 2))
Namespace.addCategoryObject('elementBinding', Title.name().localName(), Title)

Abstract = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Abstract'), LanguageStringType, documentation='Brief narrative description of this resource, normally\n      used for display to humans.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 59, 2))
Namespace.addCategoryObject('elementBinding', Abstract.name().localName(), Abstract)

Keywords = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Keywords'), KeywordsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 67, 2))
Namespace.addCategoryObject('elementBinding', Keywords.name().localName(), Keywords)

PointOfContact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PointOfContact'), ResponsiblePartyType, documentation='Identification of, and means of communication with,\n      person(s) responsible for the resource(s).For OWS use in the ServiceProvider section of a service\n      metadata document, the optional organizationName element was removed,\n      since this type is always used with the ProviderName element which\n      provides that information. The optional individualName element was made\n      mandatory, since either the organizationName or individualName element\n      is mandatory. The mandatory "role" element was changed to optional,\n      since no clear use of this information is known in the ServiceProvider\n      section.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 116, 2))
Namespace.addCategoryObject('elementBinding', PointOfContact.name().localName(), PointOfContact)

Role = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Role'), CodeType, documentation='Function performed by the responsible party. Possible\n      values of this Role shall include the values and the meanings listed in\n      Subclause B.5.5 of ISO 19115:2003.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 198, 2))
Namespace.addCategoryObject('elementBinding', Role.name().localName(), Role)

ContactInfo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo'), ContactType, documentation='Address of the responsible party.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 207, 2))
Namespace.addCategoryObject('elementBinding', ContactInfo.name().localName(), ContactInfo)

AdditionalParameter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdditionalParameter'), CTD_ANON, documentation='One additional metadata parameter.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 66, 2))
Namespace.addCategoryObject('elementBinding', AdditionalParameter.name().localName(), AdditionalParameter)

Metadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), MetadataType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 57, 2))
Namespace.addCategoryObject('elementBinding', Metadata.name().localName(), Metadata)

BoundingBox = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox'), BoundingBoxType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 107, 2))
Namespace.addCategoryObject('elementBinding', BoundingBox.name().localName(), BoundingBox)

OtherSource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OtherSource'), MetadataType, documentation='Reference to a source of metadata describing coverage\n      offerings available from this server. This parameter can reference a\n      catalogue server from which dataset metadata is available. This ability\n      is expected to be used by servers with thousands or millions of\n      datasets, for which searching a catalogue is more feasible than fetching\n      a long Capabilities XML document. When no DatasetDescriptionSummaries\n      are included, and one or more catalogue servers are referenced, this set\n      of catalogues shall contain current metadata summaries for all the\n      datasets currently available from this OWS server, with the metadata for\n      each such dataset referencing this OWS server.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 63, 2))
Namespace.addCategoryObject('elementBinding', OtherSource.name().localName(), OtherSource)

Identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), CodeType, documentation='Unique identifier or name of this\n      dataset.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 133, 2))
Namespace.addCategoryObject('elementBinding', Identifier.name().localName(), Identifier)

OutputFormat = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), MimeType, documentation='Reference to a format in which this data can be encoded\n      and transferred. More specific parameter names should be used by\n      specific OWS specifications wherever applicable. More than one such\n      parameter can be included for different purposes.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 141, 2))
Namespace.addCategoryObject('elementBinding', OutputFormat.name().localName(), OutputFormat)

AnyValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AnyValue'), CTD_ANON_, documentation='Specifies that any value is allowed for this\n      parameter.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 118, 2))
Namespace.addCategoryObject('elementBinding', AnyValue.name().localName(), AnyValue)

NoValues = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NoValues'), CTD_ANON_2, documentation='Specifies that no values are allowed for this parameter\n      or quantity.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 126, 2))
Namespace.addCategoryObject('elementBinding', NoValues.name().localName(), NoValues)

ValuesReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValuesReference'), CTD_ANON_3, documentation='Reference to externally specified list of all the valid\n      values and/or ranges of values for this quantity. (Informative: This\n      element was simplified from the metaDataProperty element in GML\n      3.0.)', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 134, 2))
Namespace.addCategoryObject('elementBinding', ValuesReference.name().localName(), ValuesReference)

AllowedValues = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AllowedValues'), CTD_ANON_4, documentation='List of all the valid values and/or ranges of values for\n      this quantity. For numeric quantities, signed values should be ordered\n      from negative infinity to positive infinity.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 181, 2))
Namespace.addCategoryObject('elementBinding', AllowedValues.name().localName(), AllowedValues)

Value = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Value'), ValueType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 195, 2))
Namespace.addCategoryObject('elementBinding', Value.name().localName(), Value)

DefaultValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DefaultValue'), ValueType, documentation='The default value for a quantity for which multiple\n      values are allowed.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 209, 2))
Namespace.addCategoryObject('elementBinding', DefaultValue.name().localName(), DefaultValue)

MinimumValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MinimumValue'), ValueType, documentation='Minimum value of this numeric parameter.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 252, 2))
Namespace.addCategoryObject('elementBinding', MinimumValue.name().localName(), MinimumValue)

MaximumValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MaximumValue'), ValueType, documentation='Maximum value of this numeric parameter.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 259, 2))
Namespace.addCategoryObject('elementBinding', MaximumValue.name().localName(), MaximumValue)

Spacing = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Spacing'), ValueType, documentation='The regular distance or spacing between the allowed\n      values in a range.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 266, 2))
Namespace.addCategoryObject('elementBinding', Spacing.name().localName(), Spacing)

Meaning = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Meaning'), DomainMetadataType, documentation='Definition of the meaning or semantics of this set of\n      values. This Meaning can provide more specific, complete, precise,\n      machine accessible, and machine understandable semantics about this\n      quantity, relative to other available semantic information. For example,\n      other semantic information is often provided in "documentation" elements\n      in XML Schemas or "description" elements in GML objects.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 344, 2))
Namespace.addCategoryObject('elementBinding', Meaning.name().localName(), Meaning)

DataType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataType'), DomainMetadataType, documentation='Definition of the data type of this set of values. In\n      this case, the xlink:href attribute can reference a URN for a well-known\n      data type. For example, such a URN could be a data type identification\n      URN defined in the "ogc" URN namespace.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 356, 2))
Namespace.addCategoryObject('elementBinding', DataType.name().localName(), DataType)

ReferenceSystem = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferenceSystem'), DomainMetadataType, documentation='Definition of the reference system used by this set of\n      values, including the unit of measure whenever applicable (as is\n      normal). In this case, the xlink:href attribute can reference a URN for\n      a well-known reference system, such as for a coordinate reference system\n      (CRS). For example, such a URN could be a CRS identification URN defined\n      in the "ogc" URN namespace.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 366, 2))
Namespace.addCategoryObject('elementBinding', ReferenceSystem.name().localName(), ReferenceSystem)

UOM = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UOM'), DomainMetadataType, documentation='Definition of the unit of measure of this set of values.\n      In this case, the xlink:href attribute can reference a URN for a\n      well-known unit of measure (uom). For example, such a URN could be a UOM\n      identification URN defined in the "ogc" URN namespace.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 378, 2))
Namespace.addCategoryObject('elementBinding', UOM.name().localName(), UOM)

Exception = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Exception'), ExceptionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 78, 2))
Namespace.addCategoryObject('elementBinding', Exception.name().localName(), Exception)

AbstractReferenceBase = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractReferenceBase'), AbstractReferenceBaseType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 33, 2))
Namespace.addCategoryObject('elementBinding', AbstractReferenceBase.name().localName(), AbstractReferenceBase)

OperationsMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OperationsMetadata'), CTD_ANON_7, documentation='Metadata about the operations and related abilities\n      specified by this service and implemented by this server, including the\n      URLs for operation requests. The basic contents of this section shall be\n      the same for all OWS types, but individual services can add elements\n      and/or change the optionality of optional elements.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 30, 2))
Namespace.addCategoryObject('elementBinding', OperationsMetadata.name().localName(), OperationsMetadata)

Operation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Operation'), CTD_ANON_8, documentation='Metadata for one operation that this server\n      implements.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 88, 2))
Namespace.addCategoryObject('elementBinding', Operation.name().localName(), Operation)

DCP = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DCP'), CTD_ANON_9, documentation='Information for one distributed Computing Platform (DCP)\n      supported for this operation. At present, only the HTTP DCP is defined,\n      so this element only includes the HTTP element.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 160, 2))
Namespace.addCategoryObject('elementBinding', DCP.name().localName(), DCP)

HTTP = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HTTP'), CTD_ANON_10, documentation='Connect point URLs for the HTTP Distributed Computing\n      Platform (DCP). Normally, only one Get and/or one Post is included in\n      this element. More than one Get and/or Post is allowed to support\n      including alternative URLs for uses such as load balancing or\n      backup.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 173, 2))
Namespace.addCategoryObject('elementBinding', HTTP.name().localName(), HTTP)

ServiceProvider = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceProvider'), CTD_ANON_11, documentation='Metadata about the organization that provides this\n      specific service instance or server.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceProvider.xsd', 30, 2))
Namespace.addCategoryObject('elementBinding', ServiceProvider.name().localName(), ServiceProvider)

nilValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nilValue'), NilValueType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 92, 2))
Namespace.addCategoryObject('elementBinding', nilValue.name().localName(), nilValue)

WGS84BoundingBox = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WGS84BoundingBox'), WGS84BoundingBoxType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 192, 2))
Namespace.addCategoryObject('elementBinding', WGS84BoundingBox.name().localName(), WGS84BoundingBox)

DatasetDescriptionSummary = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DatasetDescriptionSummary'), DatasetDescriptionSummaryBaseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 79, 2))
Namespace.addCategoryObject('elementBinding', DatasetDescriptionSummary.name().localName(), DatasetDescriptionSummary)

Range = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Range'), RangeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 217, 2))
Namespace.addCategoryObject('elementBinding', Range.name().localName(), Range)

ExceptionReport = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExceptionReport'), CTD_ANON_12, documentation='Report message returned to the client that requested any\n      OWS operation when the server detects an error while processing that\n      operation request.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 28, 2))
Namespace.addCategoryObject('elementBinding', ExceptionReport.name().localName(), ExceptionReport)

GetCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetCapabilities'), GetCapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 92, 2))
Namespace.addCategoryObject('elementBinding', GetCapabilities.name().localName(), GetCapabilities)

GetResourceByID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetResourceByID'), GetResourceByIdType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetResourceByID.xsd', 39, 2))
Namespace.addCategoryObject('elementBinding', GetResourceByID.name().localName(), GetResourceByID)

Reference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reference'), ReferenceType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 95, 2))
Namespace.addCategoryObject('elementBinding', Reference.name().localName(), Reference)

ServiceIdentification = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceIdentification'), CTD_ANON_13, documentation='General metadata for this specific server. This XML\n      Schema of this section shall be the same for all OWS.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 31, 2))
Namespace.addCategoryObject('elementBinding', ServiceIdentification.name().localName(), ServiceIdentification)

AdditionalParameters = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdditionalParameters'), AdditionalParametersType, documentation='Unordered list of one or more\n      AdditionalParameters.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 35, 2))
Namespace.addCategoryObject('elementBinding', AdditionalParameters.name().localName(), AdditionalParameters)

OperationResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OperationResponse'), ManifestType, documentation='Response from an OWS operation, allowing including\n      multiple output data items with each item either included or referenced.\n      This OperationResponse element, or an element using the ManifestType\n      with a more specific element name, shall be used whenever applicable for\n      responses from OWS operations.This element is specified for use where the ManifestType\n      contents are needed for an operation response, but the Manifest element\n      name is not fully applicable. This element or the ManifestType shall be\n      used instead of using the ows:ReferenceType proposed in OGC\n      04-105.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsInputOutputData.xsd', 30, 2))
Namespace.addCategoryObject('elementBinding', OperationResponse.name().localName(), OperationResponse)

InputData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InputData'), ManifestType, documentation='Input data in a XML-encoded OWS operation request,\n      allowing including multiple data items with each data item either\n      included or referenced. This InputData element, or an element using the\n      ManifestType with a more-specific element name (TBR), shall be used\n      whenever applicable within XML-encoded OWS operation\n      requests.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsInputOutputData.xsd', 46, 2))
Namespace.addCategoryObject('elementBinding', InputData.name().localName(), InputData)

ServiceReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceReference'), ServiceReferenceType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsInputOutputData.xsd', 58, 2))
Namespace.addCategoryObject('elementBinding', ServiceReference.name().localName(), ServiceReference)

ReferenceGroup = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferenceGroup'), ReferenceGroupType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 143, 2))
Namespace.addCategoryObject('elementBinding', ReferenceGroup.name().localName(), ReferenceGroup)

Manifest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Manifest'), ManifestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 163, 2))
Namespace.addCategoryObject('elementBinding', Manifest.name().localName(), Manifest)



KeywordsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Keyword'), LanguageStringType, scope=KeywordsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 87, 6)))

KeywordsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Type'), CodeType, scope=KeywordsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 90, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 90, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(KeywordsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keyword')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 87, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(KeywordsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Type')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 90, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
KeywordsType._Automaton = _BuildAutomaton()




ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IndividualName'), pyxb.binding.datatypes.string, scope=ResponsiblePartyType, documentation='Name of the responsible person: surname, given name,\n      title separated by a delimiter.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 175, 2)))

ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrganisationName'), pyxb.binding.datatypes.string, scope=ResponsiblePartyType, documentation='Name of the responsible organization.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 183, 2)))

ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PositionName'), pyxb.binding.datatypes.string, scope=ResponsiblePartyType, documentation='Role or position of the responsible\n      person.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 190, 2)))

ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Role'), CodeType, scope=ResponsiblePartyType, documentation='Function performed by the responsible party. Possible\n      values of this Role shall include the values and the meanings listed in\n      Subclause B.5.5 of ISO 19115:2003.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 198, 2)))

ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo'), ContactType, scope=ResponsiblePartyType, documentation='Address of the responsible party.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 207, 2)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 139, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 141, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 143, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 145, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IndividualName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 139, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrganisationName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 141, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PositionName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 143, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 145, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Role')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 147, 6))
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
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ResponsiblePartyType._Automaton = _BuildAutomaton_()




ResponsiblePartySubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IndividualName'), pyxb.binding.datatypes.string, scope=ResponsiblePartySubsetType, documentation='Name of the responsible person: surname, given name,\n      title separated by a delimiter.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 175, 2)))

ResponsiblePartySubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PositionName'), pyxb.binding.datatypes.string, scope=ResponsiblePartySubsetType, documentation='Role or position of the responsible\n      person.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 190, 2)))

ResponsiblePartySubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Role'), CodeType, scope=ResponsiblePartySubsetType, documentation='Function performed by the responsible party. Possible\n      values of this Role shall include the values and the meanings listed in\n      Subclause B.5.5 of ISO 19115:2003.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 198, 2)))

ResponsiblePartySubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo'), ContactType, scope=ResponsiblePartySubsetType, documentation='Address of the responsible party.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 207, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 164, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 166, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 168, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 170, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IndividualName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 164, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PositionName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 166, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 168, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Role')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 170, 6))
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
ResponsiblePartySubsetType._Automaton = _BuildAutomaton_2()




ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Phone'), TelephoneType, scope=ContactType, documentation='Telephone numbers at which the organization or\n          individual may be contacted.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 223, 6)))

ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Address'), AddressType, scope=ContactType, documentation='Physical and email address at which the organization\n          or individual may be contacted.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 231, 6)))

ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OnlineResource'), OnlineResourceType, scope=ContactType, documentation='On-line information that can be used to contact the\n          individual or organization. OWS specifics: The xlink:href attribute\n          in the xlink:simpleAttrs attribute group shall be used to reference\n          this resource. Whenever practical, the xlink:href attribute with\n          type anyURI should be a URL from which more contact information can\n          be electronically retrieved. The xlink:title attribute with type\n          "string" can be used to name this set of information. The other\n          attributes in the xlink:simpleAttrs attribute group should not be\n          used.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 239, 6)))

ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HoursOfService'), pyxb.binding.datatypes.string, scope=ContactType, documentation='Time period (including time zone) when individuals\n          can contact the organization or individual.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 254, 6)))

ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContactInstructions'), pyxb.binding.datatypes.string, scope=ContactType, documentation='Supplemental instructions on how or when to contact\n          the individual or organization.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 262, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 223, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 231, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 239, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 254, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 262, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Phone')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 223, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Address')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 231, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OnlineResource')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 239, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HoursOfService')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 254, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContactInstructions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 262, 6))
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
ContactType._Automaton = _BuildAutomaton_3()




TelephoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Voice'), pyxb.binding.datatypes.string, scope=TelephoneType, documentation='Telephone number by which individuals can speak to\n          the responsible organization or individual.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 290, 6)))

TelephoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Facsimile'), pyxb.binding.datatypes.string, scope=TelephoneType, documentation='Telephone number of a facsimile machine for the\n          responsible organization or individual.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 299, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 290, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 299, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TelephoneType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Voice')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 290, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TelephoneType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Facsimile')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 299, 6))
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
TelephoneType._Automaton = _BuildAutomaton_4()




AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DeliveryPoint'), pyxb.binding.datatypes.string, scope=AddressType, documentation='Address line for the location.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 317, 6)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'City'), pyxb.binding.datatypes.string, scope=AddressType, documentation='City of the location.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 325, 6)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeArea'), pyxb.binding.datatypes.string, scope=AddressType, documentation='State or province of the location.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 332, 6)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), pyxb.binding.datatypes.string, scope=AddressType, documentation='ZIP or other postal code.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 339, 6)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Country'), pyxb.binding.datatypes.string, scope=AddressType, documentation='Country of the physical address.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 346, 6)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ElectronicMailAddress'), pyxb.binding.datatypes.string, scope=AddressType, documentation='Address of the electronic mailbox of the responsible\n          organization or individual.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 353, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 317, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 325, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 332, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 339, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 346, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 353, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DeliveryPoint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 317, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'City')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 325, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeArea')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 332, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCode')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 339, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Country')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 346, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ElectronicMailAddress')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 353, 6))
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
AddressType._Automaton = _BuildAutomaton_5()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), CodeType, scope=CTD_ANON, documentation='Name or identifier of this AdditionalParameter,\n            unique for this OGC Web Service.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 73, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Value'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, documentation='Unordered list of one or more values of this\n            AdditionalParameter.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 80, 8)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 73, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Value')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 80, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_6()




MetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractMetaData'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=MetadataType, documentation='Abstract element containing more metadata about the\n      element that includes the containing "metadata" element. A specific\n      server implementation, or an Implementation Specification, can define\n      concrete elements in the AbstractMetaData substitution\n      group.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 95, 2)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 73, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AbstractMetaData')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 73, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MetadataType._Automaton = _BuildAutomaton_7()




BoundingBoxType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LowerCorner'), PositionType, scope=BoundingBoxType, documentation='Position of the bounding box corner at which the\n          value of each coordinate normally is the algebraic minimum within\n          this bounding box. In some cases, this position is normally\n          displayed at the top, such as the top left for some image\n          coordinates. For more information, see Subclauses 10.2.5 and\n          C.13.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 119, 6)))

BoundingBoxType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UpperCorner'), PositionType, scope=BoundingBoxType, documentation='Position of the bounding box corner at which the\n          value of each coordinate normally is the algebraic maximum within\n          this bounding box. In some cases, this position is normally\n          displayed at the bottom, such as the bottom right for some image\n          coordinates. For more information, see Subclauses 10.2.5 and\n          C.13.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 130, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BoundingBoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LowerCorner')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 119, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BoundingBoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UpperCorner')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 130, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BoundingBoxType._Automaton = _BuildAutomaton_8()




ContentsBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OtherSource'), MetadataType, scope=ContentsBaseType, documentation='Reference to a source of metadata describing coverage\n      offerings available from this server. This parameter can reference a\n      catalogue server from which dataset metadata is available. This ability\n      is expected to be used by servers with thousands or millions of\n      datasets, for which searching a catalogue is more feasible than fetching\n      a long Capabilities XML document. When no DatasetDescriptionSummaries\n      are included, and one or more catalogue servers are referenced, this set\n      of catalogues shall contain current metadata summaries for all the\n      datasets currently available from this OWS server, with the metadata for\n      each such dataset referencing this OWS server.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 63, 2)))

ContentsBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DatasetDescriptionSummary'), DatasetDescriptionSummaryBaseType, scope=ContentsBaseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 79, 2)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 41, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 51, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ContentsBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DatasetDescriptionSummary')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 41, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ContentsBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OtherSource')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 51, 6))
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
ContentsBaseType._Automaton = _BuildAutomaton_9()




DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Title'), LanguageStringType, scope=DescriptionType, documentation='Title of this resource, normally used for display to\n      humans.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 51, 2)))

DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Abstract'), LanguageStringType, scope=DescriptionType, documentation='Brief narrative description of this resource, normally\n      used for display to humans.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 59, 2)))

DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Keywords'), KeywordsType, scope=DescriptionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 67, 2)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 50, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 53, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 56, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 50, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 53, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keywords')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 56, 6))
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
DescriptionType._Automaton = _BuildAutomaton_10()




UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), MetadataType, scope=UnNamedDomainType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 57, 2)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AnyValue'), CTD_ANON_, scope=UnNamedDomainType, documentation='Specifies that any value is allowed for this\n      parameter.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 118, 2)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NoValues'), CTD_ANON_2, scope=UnNamedDomainType, documentation='Specifies that no values are allowed for this parameter\n      or quantity.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 126, 2)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValuesReference'), CTD_ANON_3, scope=UnNamedDomainType, documentation='Reference to externally specified list of all the valid\n      values and/or ranges of values for this quantity. (Informative: This\n      element was simplified from the metaDataProperty element in GML\n      3.0.)', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 134, 2)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AllowedValues'), CTD_ANON_4, scope=UnNamedDomainType, documentation='List of all the valid values and/or ranges of values for\n      this quantity. For numeric quantities, signed values should be ordered\n      from negative infinity to positive infinity.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 181, 2)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DefaultValue'), ValueType, scope=UnNamedDomainType, documentation='The default value for a quantity for which multiple\n      values are allowed.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 209, 2)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Meaning'), DomainMetadataType, scope=UnNamedDomainType, documentation='Definition of the meaning or semantics of this set of\n      values. This Meaning can provide more specific, complete, precise,\n      machine accessible, and machine understandable semantics about this\n      quantity, relative to other available semantic information. For example,\n      other semantic information is often provided in "documentation" elements\n      in XML Schemas or "description" elements in GML objects.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 344, 2)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataType'), DomainMetadataType, scope=UnNamedDomainType, documentation='Definition of the data type of this set of values. In\n      this case, the xlink:href attribute can reference a URN for a well-known\n      data type. For example, such a URN could be a data type identification\n      URN defined in the "ogc" URN namespace.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 356, 2)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferenceSystem'), DomainMetadataType, scope=UnNamedDomainType, documentation='Definition of the reference system used by this set of\n      values, including the unit of measure whenever applicable (as is\n      normal). In this case, the xlink:href attribute can reference a URN for\n      a well-known reference system, such as for a coordinate reference system\n      (CRS). For example, such a URN could be a CRS identification URN defined\n      in the "ogc" URN namespace.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 366, 2)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UOM'), DomainMetadataType, scope=UnNamedDomainType, documentation='Definition of the unit of measure of this set of values.\n      In this case, the xlink:href attribute can reference a URN for a\n      well-known unit of measure (uom). For example, such a URN could be a UOM\n      identification URN defined in the "ogc" URN namespace.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 378, 2)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 62, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 70, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 77, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 84, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 92, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AllowedValues')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 111, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AnyValue')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 112, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NoValues')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 113, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValuesReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 114, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DefaultValue')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 62, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Meaning')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 70, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 77, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UOM')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 163, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReferenceSystem')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 170, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 92, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
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
    st_0._set_transitionSet(transitions)
    transitions = []
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
    st_1._set_transitionSet(transitions)
    transitions = []
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
    st_2._set_transitionSet(transitions)
    transitions = []
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UnNamedDomainType._Automaton = _BuildAutomaton_11()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Value'), ValueType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 195, 2)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Range'), RangeType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 217, 2)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Value')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 189, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Range')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 190, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_12()




ExceptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExceptionText'), pyxb.binding.datatypes.string, scope=ExceptionType, documentation='Ordered sequence of text strings that describe this\n          specific exception or error. The contents of these strings are left\n          open to definition by each server implementation. A server is\n          strongly encouraged to include at least one ExceptionText value, to\n          provide more information about the detected error than provided by\n          the exceptionCode. When included, multiple ExceptionText values\n          shall provide hierarchical information about one detected error,\n          with the most significant information listed first.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 87, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 87, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExceptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExceptionText')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 87, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ExceptionType._Automaton = _BuildAutomaton_13()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Language'), pyxb.binding.datatypes.language, scope=CTD_ANON_5, documentation='Identifier of a language used by the data(set) contents.\n      This language identifier shall be as specified in IETF RFC 4646. The\n      language tags shall be either complete 5 character codes (e.g. "en-CA"),\n      or abbreviated 2 character codes (e.g. "en"). In addition to the RFC\n      4646 codes, the server shall support the single special value "*" which\n      is used to indicate "any language".', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 190, 2)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Language')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 71, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_14()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Language'), pyxb.binding.datatypes.language, scope=CTD_ANON_6, documentation='Identifier of a language used by the data(set) contents.\n      This language identifier shall be as specified in IETF RFC 4646. The\n      language tags shall be either complete 5 character codes (e.g. "en-CA"),\n      or abbreviated 2 character codes (e.g. "en"). In addition to the RFC\n      4646 codes, the server shall support the single special value "*" which\n      is used to indicate "any language".', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 190, 2)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Language')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 142, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_15()




AcceptVersionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Version'), VersionType, scope=AcceptVersionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 173, 6)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AcceptVersionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Version')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 173, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AcceptVersionsType._Automaton = _BuildAutomaton_16()




SectionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Section'), pyxb.binding.datatypes.string, scope=SectionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 187, 6)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 187, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SectionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Section')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 187, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SectionsType._Automaton = _BuildAutomaton_17()




AcceptFormatsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), MimeType, scope=AcceptFormatsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 214, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 214, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AcceptFormatsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 214, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AcceptFormatsType._Automaton = _BuildAutomaton_18()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Parameter'), DomainType, scope=CTD_ANON_7, documentation='Optional unordered list of parameter valid domains\n            that each apply to one or more operations which this server\n            interface implements. The list of required and optional parameter\n            domain limitations shall be specified in the Implementation\n            Specification for this service.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 50, 8)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), DomainType, scope=CTD_ANON_7, documentation='Optional unordered list of valid domain constraints\n            on non-parameter quantities that each apply to this server. The\n            list of required and optional constraints shall be specified in\n            the Implementation Specification for this service.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 62, 8)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtendedCapabilities'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_7, documentation='Individual software vendors and servers can use this\n      element to provide metadata about any additional server\n      abilities.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 79, 2)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Operation'), CTD_ANON_8, scope=CTD_ANON_7, documentation='Metadata for one operation that this server\n      implements.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 88, 2)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 40, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 50, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 62, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 73, 8))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Operation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 40, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Parameter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 50, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Constraint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 62, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExtendedCapabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 73, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
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
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_19()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), MetadataType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 57, 2)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Parameter'), DomainType, scope=CTD_ANON_8, documentation='Optional unordered list of parameter domains that\n            each apply to this operation which this server implements. If one\n            of these Parameter elements has the same "name" attribute as a\n            Parameter element in the OperationsMetadata element, this\n            Parameter element shall override the other one for this operation.\n            The list of required and optional parameter domain limitations for\n            this operation shall be specified in the Implementation\n            Specification for this service.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 103, 8)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), DomainType, scope=CTD_ANON_8, documentation='Optional unordered list of valid domain constraints\n            on non-parameter quantities that each apply to this operation. If\n            one of these Constraint elements has the same "name" attribute as\n            a Constraint element in the OperationsMetadata element, this\n            Constraint element shall override the other one for this\n            operation. The list of required and optional constraints for this\n            operation shall be specified in the Implementation Specification\n            for this service.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 118, 8)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DCP'), CTD_ANON_9, scope=CTD_ANON_8, documentation='Information for one distributed Computing Platform (DCP)\n      supported for this operation. At present, only the HTTP DCP is defined,\n      so this element only includes the HTTP element.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 160, 2)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 103, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 118, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 133, 8))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DCP')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 95, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Parameter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 103, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Constraint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 118, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 133, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
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
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_20()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HTTP'), CTD_ANON_10, scope=CTD_ANON_9, documentation='Connect point URLs for the HTTP Distributed Computing\n      Platform (DCP). Normally, only one Get and/or one Post is included in\n      this element. More than one Get and/or Post is allowed to support\n      including alternative URLs for uses such as load balancing or\n      backup.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 173, 2)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HTTP')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 168, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_21()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Get'), RequestMethodType, scope=CTD_ANON_10, documentation='Connect point URL prefix and any constraints for\n            the HTTP "Get" request method for this operation\n            request.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 183, 8)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Post'), RequestMethodType, scope=CTD_ANON_10, documentation='Connect point URL and any constraints for the HTTP\n            "Post" request method for this operation request.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 191, 8)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Get')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 183, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Post')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 191, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_22()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProviderName'), pyxb.binding.datatypes.string, scope=CTD_ANON_11, documentation='A unique identifier for the service provider\n            organization.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceProvider.xsd', 37, 8)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProviderSite'), OnlineResourceType, scope=CTD_ANON_11, documentation='Reference to the most relevant web site of the\n            service provider.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceProvider.xsd', 44, 8)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceContact'), ResponsiblePartySubsetType, scope=CTD_ANON_11, documentation='Information for contacting the service provider.\n            The OnlineResource element within this ServiceContact element\n            should not be used to reference a web site of the service\n            provider.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceProvider.xsd', 52, 8)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceProvider.xsd', 44, 8))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProviderName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceProvider.xsd', 37, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProviderSite')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceProvider.xsd', 44, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceContact')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceProvider.xsd', 52, 8))
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
CTD_ANON_11._Automaton = _BuildAutomaton_23()




AdditionalParametersBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdditionalParameter'), CTD_ANON, scope=AdditionalParametersBaseType, documentation='One additional metadata parameter.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 66, 2)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AdditionalParametersBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdditionalParameter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 48, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AdditionalParametersBaseType._Automaton = _BuildAutomaton_24()




def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WGS84BoundingBoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LowerCorner')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 209, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(WGS84BoundingBoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UpperCorner')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 218, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
WGS84BoundingBoxType._Automaton = _BuildAutomaton_25()




DatasetDescriptionSummaryBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), MetadataType, scope=DatasetDescriptionSummaryBaseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 57, 2)))

DatasetDescriptionSummaryBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox'), BoundingBoxType, scope=DatasetDescriptionSummaryBaseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 107, 2)))

DatasetDescriptionSummaryBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WGS84BoundingBox'), WGS84BoundingBoxType, scope=DatasetDescriptionSummaryBaseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 192, 2)))

DatasetDescriptionSummaryBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DatasetDescriptionSummary'), DatasetDescriptionSummaryBaseType, scope=DatasetDescriptionSummaryBaseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 79, 2)))

DatasetDescriptionSummaryBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), CodeType, scope=DatasetDescriptionSummaryBaseType, documentation='Unambiguous identifier or name of this coverage,\n              unique for this server.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 112, 10)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 50, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 53, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 56, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 92, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 119, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 140, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 150, 10))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 50, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 53, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keywords')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 56, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WGS84BoundingBox')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 92, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 112, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 119, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 140, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DatasetDescriptionSummary')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsContents.xsd', 150, 10))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DatasetDescriptionSummaryBaseType._Automaton = _BuildAutomaton_26()




BasicIdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), MetadataType, scope=BasicIdentificationType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 57, 2)))

BasicIdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), CodeType, scope=BasicIdentificationType, documentation='Unique identifier or name of this\n      dataset.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 133, 2)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 50, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 53, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 56, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 70, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 77, 10))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BasicIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 50, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BasicIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 53, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BasicIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keywords')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 56, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BasicIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 70, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(BasicIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 77, 10))
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
BasicIdentificationType._Automaton = _BuildAutomaton_27()




def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 62, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 70, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 77, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 84, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 92, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AllowedValues')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 111, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AnyValue')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 112, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NoValues')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 113, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValuesReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 114, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DefaultValue')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 62, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Meaning')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 70, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 77, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UOM')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 163, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReferenceSystem')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 170, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 92, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
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
    st_0._set_transitionSet(transitions)
    transitions = []
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
    st_1._set_transitionSet(transitions)
    transitions = []
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
    st_2._set_transitionSet(transitions)
    transitions = []
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DomainType._Automaton = _BuildAutomaton_28()




RangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MinimumValue'), ValueType, scope=RangeType, documentation='Minimum value of this numeric parameter.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 252, 2)))

RangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MaximumValue'), ValueType, scope=RangeType, documentation='Maximum value of this numeric parameter.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 259, 2)))

RangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Spacing'), ValueType, scope=RangeType, documentation='The regular distance or spacing between the allowed\n      values in a range.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 266, 2)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 230, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 232, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 234, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MinimumValue')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 230, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MaximumValue')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 232, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Spacing')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDomainType.xsd', 234, 6))
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
RangeType._Automaton = _BuildAutomaton_29()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Exception'), ExceptionType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 78, 2)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Exception')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsExceptionReport.xsd', 36, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_30()




CapabilitiesBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Languages'), CTD_ANON_5, scope=CapabilitiesBaseType, documentation='The list of languages that this service is able to\n          fully support. That is, if one of the listed languages is requested\n          using the AcceptLanguages parameter in future requests to the\n          server, all text strings contained in the response are guaranteed to\n          be in that language. This list does not necessarily constitute a\n          complete list of all languages that may be (at least partially)\n          supported by the server. It only states the languages that are fully\n          supported. If a server cannot guarantee full support of any\n          particular language, it shall omit it from the list of supported\n          languages in the capabilities document.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 55, 6)))

CapabilitiesBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OperationsMetadata'), CTD_ANON_7, scope=CapabilitiesBaseType, documentation='Metadata about the operations and related abilities\n      specified by this service and implemented by this server, including the\n      URLs for operation requests. The basic contents of this section shall be\n      the same for all OWS types, but individual services can add elements\n      and/or change the optionality of optional elements.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 30, 2)))

CapabilitiesBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceIdentification'), CTD_ANON_13, scope=CapabilitiesBaseType, documentation='General metadata for this specific server. This XML\n      Schema of this section shall be the same for all OWS.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 31, 2)))

CapabilitiesBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceProvider'), CTD_ANON_11, scope=CapabilitiesBaseType, documentation='Metadata about the organization that provides this\n      specific service instance or server.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceProvider.xsd', 30, 2)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
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
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CapabilitiesBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceIdentification')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 49, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CapabilitiesBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceProvider')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 51, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CapabilitiesBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OperationsMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 53, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CapabilitiesBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Languages')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 55, 6))
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
CapabilitiesBaseType._Automaton = _BuildAutomaton_31()




GetCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AcceptVersions'), AcceptVersionsType, scope=GetCapabilitiesType, documentation='When omitted, server shall return latest supported\n          version.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 106, 6)))

GetCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Sections'), SectionsType, scope=GetCapabilitiesType, documentation='When omitted or not supported by server, server shall\n          return complete service metadata (Capabilities)\n          document.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 114, 6)))

GetCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AcceptFormats'), AcceptFormatsType, scope=GetCapabilitiesType, documentation='When omitted or not supported by server, server shall\n          return service metadata document using the MIME type\n          "text/xml".', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 123, 6)))

GetCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AcceptLanguages'), CTD_ANON_6, scope=GetCapabilitiesType, documentation='Ordered list of languages desired by the client for\n          all human readable text in the response, in order of preference. For\n          every element, the first matching language available from the server\n          shall be present in the response.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 132, 6)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
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
    symbol = pyxb.binding.content.ElementUse(GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AcceptVersions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 106, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Sections')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 114, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AcceptFormats')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 123, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AcceptLanguages')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetCapabilities.xsd', 132, 6))
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
GetCapabilitiesType._Automaton = _BuildAutomaton_32()




GetResourceByIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), MimeType, scope=GetResourceByIdType, documentation='Reference to a format in which this data can be encoded\n      and transferred. More specific parameter names should be used by\n      specific OWS specifications wherever applicable. More than one such\n      parameter can be included for different purposes.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 141, 2)))

GetResourceByIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResourceID'), pyxb.binding.datatypes.anyURI, scope=GetResourceByIdType, documentation='Unordered list of zero or more resource identifiers.\n          These identifiers can be listed in the Contents section of the\n          service metadata (Capabilities) document. For more information on\n          this parameter, see Subclause 9.4.2.1 of the OWS Common\n          specification.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetResourceByID.xsd', 52, 6)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetResourceByID.xsd', 52, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetResourceByID.xsd', 64, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GetResourceByIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResourceID')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetResourceByID.xsd', 52, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GetResourceByIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsGetResourceByID.xsd', 64, 6))
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
GetResourceByIdType._Automaton = _BuildAutomaton_33()




ReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Abstract'), LanguageStringType, scope=ReferenceType, documentation='Brief narrative description of this resource, normally\n      used for display to humans.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/ows19115subset.xsd', 59, 2)))

ReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), MetadataType, scope=ReferenceType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 57, 2)))

ReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), CodeType, scope=ReferenceType, documentation='Unique identifier or name of this\n      dataset.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 133, 2)))

ReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Format'), MimeType, scope=ReferenceType, documentation='The format of the referenced resource. This\n              element is omitted when the mime type is indicated in the http\n              header of the reference.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 117, 10)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 107, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 114, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 117, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 126, 10))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 107, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 114, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Format')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 117, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 126, 10))
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
ReferenceType._Automaton = _BuildAutomaton_34()




RequestMethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), DomainType, scope=RequestMethodType, documentation='Optional unordered list of valid domain\n              constraints on non-parameter quantities that each apply to this\n              request method for this operation. If one of these Constraint\n              elements has the same "name" attribute as a Constraint element\n              in the OperationsMetadata or Operation element, this Constraint\n              element shall override the other one for this operation. The\n              list of required and optional constraints for this request\n              method for this operation shall be specified in the\n              Implementation Specification for this service.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 213, 10)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 213, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RequestMethodType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Constraint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsOperationsMetadata.xsd', 213, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RequestMethodType._Automaton = _BuildAutomaton_35()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AccessConstraints'), pyxb.binding.datatypes.string, scope=CTD_ANON_13, documentation='Access constraint applied to assure the protection of\n      privacy or intellectual property, or any other restrictions on\n      retrieving or using data from or otherwise using this server. The\n      reserved value NONE (case insensitive) shall be used to mean no access\n      constraints are imposed.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 169, 2)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Fees'), pyxb.binding.datatypes.string, scope=CTD_ANON_13, documentation='Fees and terms for retrieving data from or otherwise\n      using this server, including the monetary units as specified in ISO\n      4217. The reserved value NONE (case insensitive) shall be used to mean\n      no fees or terms.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 180, 2)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceType'), CodeType, scope=CTD_ANON_13, documentation='A service type name from a registry of\n                services. For example, the values of the codeSpace URI and\n                name and code string may be "OGC" and "catalogue." This type\n                name is normally used for machine-to-machine\n                communication.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 40, 12)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceTypeVersion'), VersionType, scope=CTD_ANON_13, documentation='Unordered list of one or more versions of this\n                service type implemented by this server. This information is\n                not adequate for version negotiation, and shall not be used\n                for that purpose.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 50, 12)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Profile'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_13, documentation='Unordered list of identifiers of Application\n                Profiles that are implemented by this server. This element\n                should be included for each specified application profile\n                implemented by this server. The identifier value should be\n                specified by each Application Profile. If this element is\n                omitted, no meaning is implied.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 60, 12)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 50, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 53, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 56, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 60, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 73, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 80, 12))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 50, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 53, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keywords')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 56, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 40, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceTypeVersion')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 50, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Profile')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 60, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Fees')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 73, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AccessConstraints')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsServiceIdentification.xsd', 80, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_36()




def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 58, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AdditionalParametersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdditionalParameter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 48, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AdditionalParametersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdditionalParameter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsAdditionalParameters.xsd', 58, 10))
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
AdditionalParametersType._Automaton = _BuildAutomaton_37()




IdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox'), BoundingBoxType, scope=IdentificationType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsCommon.xsd', 107, 2)))

IdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), MimeType, scope=IdentificationType, documentation='Reference to a format in which this data can be encoded\n      and transferred. More specific parameter names should be used by\n      specific OWS specifications wherever applicable. More than one such\n      parameter can be included for different purposes.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 141, 2)))

IdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AvailableCRS'), pyxb.binding.datatypes.anyURI, scope=IdentificationType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 151, 2)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 50, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 53, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 56, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 70, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 77, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 103, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 112, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 120, 10))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 50, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 53, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keywords')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 56, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 70, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 77, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 103, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 112, 10))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AvailableCRS')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 120, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IdentificationType._Automaton = _BuildAutomaton_38()




ServiceReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequestMessage'), pyxb.binding.datatypes.anyType, scope=ServiceReferenceType, documentation='The XML-encoded operation request message to be\n              sent to request this input data from another web server using\n              HTTP Post.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsInputOutputData.xsd', 75, 10)))

ServiceReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequestMessageReference'), pyxb.binding.datatypes.anyURI, scope=ServiceReferenceType, documentation='Reference to the XML-encoded operation request\n              message to be sent to request this input data from another web\n              server using HTTP Post. The referenced message shall be attached\n              to the same message (using the cid scheme), or be accessible\n              using a URL.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsInputOutputData.xsd', 83, 10)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 107, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 114, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 117, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 126, 10))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 107, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 114, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Format')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 117, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 126, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RequestMessage')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsInputOutputData.xsd', 75, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RequestMessageReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsInputOutputData.xsd', 83, 10))
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
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ServiceReferenceType._Automaton = _BuildAutomaton_39()




ReferenceGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractReferenceBase'), AbstractReferenceBaseType, abstract=pyxb.binding.datatypes.boolean(1), scope=ReferenceGroupType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 33, 2)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 50, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 53, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 56, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 70, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 77, 10))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 50, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 53, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keywords')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 56, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 70, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 77, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AbstractReferenceBase')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 156, 10))
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
         ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReferenceGroupType._Automaton = _BuildAutomaton_40()




ManifestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferenceGroup'), ReferenceGroupType, scope=ManifestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 143, 2)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 50, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 53, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 56, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 70, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 77, 10))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 50, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 53, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keywords')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 56, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 70, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsDataIdentification.xsd', 77, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReferenceGroup')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/2.0/owsManifest.xsd', 174, 10))
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
         ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ManifestType._Automaton = _BuildAutomaton_41()


SupportedCRS._setSubstitutionGroup(AvailableCRS)

AdditionalParameter._setSubstitutionGroup(AbstractMetaData)

WGS84BoundingBox._setSubstitutionGroup(BoundingBox)

Reference._setSubstitutionGroup(AbstractReferenceBase)

AdditionalParameters._setSubstitutionGroup(Metadata)

ServiceReference._setSubstitutionGroup(Reference)
