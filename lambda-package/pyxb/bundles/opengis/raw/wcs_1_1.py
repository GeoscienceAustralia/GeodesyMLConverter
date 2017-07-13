# ./pyxb/bundles/opengis/raw/wcs_1_1.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:22a469f3e316cf44da81d828959bab128bf769b5
# Generated 2017-07-10 00:37:28.017773 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/wcs/1.1

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:f2a54040-6507-11e7-9446-0a55f9edafa5')

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
import pyxb.bundles.opengis.gml
import pyxb.bundles.common.xlink
import pyxb.bundles.opengis.ows_1_1

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/wcs/1.1', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gml = pyxb.bundles.opengis.gml.Namespace
_Namespace_gml.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ows = pyxb.bundles.opengis.ows_1_1.Namespace
_Namespace_ows.configureCategories(['typeBinding', 'elementBinding'])
_Namespace = pyxb.bundles.common.xlink.Namespace
_Namespace.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://www.opengis.net/wcs/1.1}IdentifierType
class IdentifierType (pyxb.binding.datatypes.string):

    """Unambiguous identifier. Although there is no formal restriction on characters included, these identifiers shall be directly usable in GetCoverage operation requests for the specific server, whether those requests are encoded in KVP or XML. Each of these encodings requires that certain characters be avoided, encoded, or escaped (TBR). """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IdentifierType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 46, 1)
    _Documentation = 'Unambiguous identifier. Although there is no formal restriction on characters included, these identifiers shall be directly usable in GetCoverage operation requests for the specific server, whether those requests are encoded in KVP or XML. Each of these encodings requires that certain characters be avoided, encoded, or escaped (TBR). '
IdentifierType._CF_pattern = pyxb.binding.facets.CF_pattern()
IdentifierType._CF_pattern.addPattern(pattern='.+')
IdentifierType._InitializeFacetMap(IdentifierType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'IdentifierType', IdentifierType)
_module_typeBindings.IdentifierType = IdentifierType

# Union simple type: {http://www.opengis.net/wcs/1.1}TimeDurationType
# superclasses pyxb.binding.datatypes.anySimpleType
class TimeDurationType (pyxb.binding.basis.STD_union):

    """
      Base type for describing temporal length or distance. The value space is further 
      constrained by subtypes that conform to the ISO 8601 or ISO 11404 standards.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeDurationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 78, 1)
    _Documentation = '\n      Base type for describing temporal length or distance. The value space is further \n      constrained by subtypes that conform to the ISO 8601 or ISO 11404 standards.\n      '

    _MemberTypes = ( pyxb.binding.datatypes.duration, pyxb.binding.datatypes.decimal, )
TimeDurationType._CF_pattern = pyxb.binding.facets.CF_pattern()
TimeDurationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TimeDurationType)
TimeDurationType._InitializeFacetMap(TimeDurationType._CF_pattern,
   TimeDurationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TimeDurationType', TimeDurationType)
_module_typeBindings.TimeDurationType = TimeDurationType

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 59, 1)
    _Documentation = None
STD_ANON._InitializeFacetMap()
_module_typeBindings.STD_ANON = STD_ANON

# Complex type {http://www.opengis.net/wcs/1.1}RequestBaseType with content type EMPTY
class RequestBaseType (pyxb.binding.basis.complexTypeDefinition):
    """XML encoded WCS operation request base, for all operations except GetCapabilities. In this XML encoding, no "request" parameter is included, since the element name specifies the specific operation. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 27, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__httpwww_opengis_netwcs1_1_RequestBaseType_service', pyxb.binding.datatypes.string, fixed=True, unicode_default='WCS', required=True)
    __service._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 32, 2)
    __service._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 32, 2)
    
    service = property(__service.value, __service.set, None, 'Service type identifier, where the value is the OWS type abbreviation. For WCS operation requests, the value is "WCS". ')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netwcs1_1_RequestBaseType_version', pyxb.binding.datatypes.string, fixed=True, unicode_default='1.1.2', required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 37, 2)
    __version._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 37, 2)
    
    version = property(__version.value, __version.set, None, 'Specification version for WCS version and operation. See Version parameter Subclause 7.3.1 of OWS Common for more information. ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __service.name() : __service,
        __version.name() : __version
    })
_module_typeBindings.RequestBaseType = RequestBaseType
Namespace.addCategoryObject('typeBinding', 'RequestBaseType', RequestBaseType)


# Complex type {http://www.opengis.net/wcs/1.1}TimeSequenceType with content type ELEMENT_ONLY
class TimeSequenceType (pyxb.binding.basis.complexTypeDefinition):
    """List of time positions and periods. The time positions and periods should be ordered from the oldest to the newest, but this is not required. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeSequenceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 55, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml}timePosition uses Python identifier timePosition
    __timePosition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'timePosition'), 'timePosition', '__httpwww_opengis_netwcs1_1_TimeSequenceType_httpwww_opengis_netgmltimePosition', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/temporal.xsd', 262, 1), )

    
    timePosition = property(__timePosition.value, __timePosition.set, None, 'Direct representation of a temporal position')

    
    # Element {http://www.opengis.net/wcs/1.1}TimePeriod uses Python identifier TimePeriod
    __TimePeriod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TimePeriod'), 'TimePeriod', '__httpwww_opengis_netwcs1_1_TimeSequenceType_httpwww_opengis_netwcs1_1TimePeriod', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 61, 3), )

    
    TimePeriod = property(__TimePeriod.value, __TimePeriod.set, None, None)

    _ElementMap.update({
        __timePosition.name() : __timePosition,
        __TimePeriod.name() : __TimePeriod
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TimeSequenceType = TimeSequenceType
Namespace.addCategoryObject('typeBinding', 'TimeSequenceType', TimeSequenceType)


# Complex type {http://www.opengis.net/wcs/1.1}TimePeriodType with content type ELEMENT_ONLY
class TimePeriodType (pyxb.binding.basis.complexTypeDefinition):
    """This is a variation of the GML TimePeriod, which allows the beginning and end of a time-period to be expressed in short-form inline using the begin/endPosition element, which allows an identifiable TimeInstant to be defined simultaneously with using it, or by reference, using xlinks on the begin/end elements. (Arliss) What does this mean? What do the TimeResolution and "frame" mean? """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimePeriodType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 65, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wcs/1.1}BeginPosition uses Python identifier BeginPosition
    __BeginPosition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BeginPosition'), 'BeginPosition', '__httpwww_opengis_netwcs1_1_TimePeriodType_httpwww_opengis_netwcs1_1BeginPosition', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 71, 3), )

    
    BeginPosition = property(__BeginPosition.value, __BeginPosition.set, None, None)

    
    # Element {http://www.opengis.net/wcs/1.1}EndPosition uses Python identifier EndPosition
    __EndPosition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndPosition'), 'EndPosition', '__httpwww_opengis_netwcs1_1_TimePeriodType_httpwww_opengis_netwcs1_1EndPosition', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 72, 3), )

    
    EndPosition = property(__EndPosition.value, __EndPosition.set, None, None)

    
    # Element {http://www.opengis.net/wcs/1.1}TimeResolution uses Python identifier TimeResolution
    __TimeResolution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TimeResolution'), 'TimeResolution', '__httpwww_opengis_netwcs1_1_TimePeriodType_httpwww_opengis_netwcs1_1TimeResolution', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 73, 3), )

    
    TimeResolution = property(__TimeResolution.value, __TimeResolution.set, None, None)

    
    # Attribute frame uses Python identifier frame
    __frame = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'frame'), 'frame', '__httpwww_opengis_netwcs1_1_TimePeriodType_frame', pyxb.binding.datatypes.anyURI, unicode_default='#ISO-8601')
    __frame._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 75, 2)
    __frame._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 75, 2)
    
    frame = property(__frame.value, __frame.set, None, None)

    _ElementMap.update({
        __BeginPosition.name() : __BeginPosition,
        __EndPosition.name() : __EndPosition,
        __TimeResolution.name() : __TimeResolution
    })
    _AttributeMap.update({
        __frame.name() : __frame
    })
_module_typeBindings.TimePeriodType = TimePeriodType
Namespace.addCategoryObject('typeBinding', 'TimePeriodType', TimePeriodType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Contents section of WCS service metadata (or Capabilities) XML document. For the WCS, these contents are brief metadata about the coverages available from this server, or a reference to another source from which this metadata is available. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 29, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wcs/1.1}SupportedCRS uses Python identifier SupportedCRS
    __SupportedCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SupportedCRS'), 'SupportedCRS', '__httpwww_opengis_netwcs1_1_CTD_ANON_httpwww_opengis_netwcs1_1SupportedCRS', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 36, 4), )

    
    SupportedCRS = property(__SupportedCRS.value, __SupportedCRS.set, None, 'Unordered list of references to GridBaseCRSs in which GetCoverage operation requests and responses may be expressed. This list of SupportedCRSs shall be the union of all of the supported CRSs in all of the nested CoverageSummaries. Servers should include this list since it reduces the work clients need to do to determine that they can interoperate with the server. There may be a dependency of SupportedCRS on SupportedFormat, as described in Subclause 10.3.5. The full list of GridBaseCRSs supported by a coverage shall be the union of the CoverageSummary\u2019s own SupportedCRSs and those supported by all its ancestor CoverageSummaries. This full list shall be an exact copy of the equivalent parameters in the CoverageDescription, and shall include zero or more SupportedCRS elements. ')

    
    # Element {http://www.opengis.net/wcs/1.1}SupportedFormat uses Python identifier SupportedFormat
    __SupportedFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SupportedFormat'), 'SupportedFormat', '__httpwww_opengis_netwcs1_1_CTD_ANON_httpwww_opengis_netwcs1_1SupportedFormat', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 41, 4), )

    
    SupportedFormat = property(__SupportedFormat.value, __SupportedFormat.set, None, 'Unordered list of identifiers of formats in which GetCoverage operation response may be encoded. This list of SupportedFormats shall be the union of all of the supported formats in all of the nested CoverageSummaries. Servers should include this list since it reduces the work clients need to do to determine that they can interoperate with the server. There may be a dependency of SupportedCRS on SupportedFormat, as described in clause 10.3.5. The full list of formats supported by a coverage shall be the union of the CoverageSummary\u2019s own SupportedFormats and those supported by all its ancestor CoverageSummaries. ')

    
    # Element {http://www.opengis.net/wcs/1.1}OtherSource uses Python identifier OtherSource
    __OtherSource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OtherSource'), 'OtherSource', '__httpwww_opengis_netwcs1_1_CTD_ANON_httpwww_opengis_netwcs1_1OtherSource', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 46, 4), )

    
    OtherSource = property(__OtherSource.value, __OtherSource.set, None, 'Unordered list of references to other sources of coverage metadata. This list shall be included unless one or more CoverageSummaries are included. ')

    
    # Element {http://www.opengis.net/wcs/1.1}CoverageSummary uses Python identifier CoverageSummary
    __CoverageSummary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CoverageSummary'), 'CoverageSummary', '__httpwww_opengis_netwcs1_1_CTD_ANON_httpwww_opengis_netwcs1_1CoverageSummary', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 55, 1), )

    
    CoverageSummary = property(__CoverageSummary.value, __CoverageSummary.set, None, None)

    _ElementMap.update({
        __SupportedCRS.name() : __SupportedCRS,
        __SupportedFormat.name() : __SupportedFormat,
        __OtherSource.name() : __OtherSource,
        __CoverageSummary.name() : __CoverageSummary
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://www.opengis.net/wcs/1.1}CoverageSummaryType with content type ELEMENT_ONLY
class CoverageSummaryType (pyxb.bundles.opengis.ows_1_1.DescriptionType):
    """Brief metadata describing one or more coverages available from this WCS server. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CoverageSummaryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 57, 1)
    _ElementMap = pyxb.bundles.opengis.ows_1_1.DescriptionType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.ows_1_1.DescriptionType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.ows_1_1.DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/1.1}Keywords) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata'), 'Metadata', '__httpwww_opengis_netwcs1_1_CoverageSummaryType_httpwww_opengis_netows1_1Metadata', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 42, 1), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}WGS84BoundingBox uses Python identifier WGS84BoundingBox
    __WGS84BoundingBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'WGS84BoundingBox'), 'WGS84BoundingBox', '__httpwww_opengis_netwcs1_1_CoverageSummaryType_httpwww_opengis_netows1_1WGS84BoundingBox', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 113, 1), )

    
    WGS84BoundingBox = property(__WGS84BoundingBox.value, __WGS84BoundingBox.set, None, None)

    
    # Element {http://www.opengis.net/wcs/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), 'Identifier', '__httpwww_opengis_netwcs1_1_CoverageSummaryType_httpwww_opengis_netwcs1_1Identifier', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 44, 1), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)

    
    # Element {http://www.opengis.net/wcs/1.1}CoverageSummary uses Python identifier CoverageSummary
    __CoverageSummary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CoverageSummary'), 'CoverageSummary', '__httpwww_opengis_netwcs1_1_CoverageSummaryType_httpwww_opengis_netwcs1_1CoverageSummary', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 55, 1), )

    
    CoverageSummary = property(__CoverageSummary.value, __CoverageSummary.set, None, None)

    
    # Element {http://www.opengis.net/wcs/1.1}SupportedCRS uses Python identifier SupportedCRS
    __SupportedCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SupportedCRS'), 'SupportedCRS', '__httpwww_opengis_netwcs1_1_CoverageSummaryType_httpwww_opengis_netwcs1_1SupportedCRS', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 74, 5), )

    
    SupportedCRS = property(__SupportedCRS.value, __SupportedCRS.set, None, 'Unordered list of references to CRSs that may be referenced as a GridBaseCRS of a GridCRS in the Output part of a GetCoverage request. These CRSs shall also apply to all lower-level CoverageSummaries under this CoverageSummary, in addition to any other CRSs referenced. When included in a CoverageSummary with an Identifier, this list, including all values inherited from ancestor coverages, shall be an exact copy of the list of SupportedCRS parameters in the corresponding CoverageDescription. Each CoverageSummary shall list or inherit at least one SupportedCRS. ')

    
    # Element {http://www.opengis.net/wcs/1.1}SupportedFormat uses Python identifier SupportedFormat
    __SupportedFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SupportedFormat'), 'SupportedFormat', '__httpwww_opengis_netwcs1_1_CoverageSummaryType_httpwww_opengis_netwcs1_1SupportedFormat', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 79, 5), )

    
    SupportedFormat = property(__SupportedFormat.value, __SupportedFormat.set, None, 'Unordered list of identifiers of formats in which GetCoverage operation responses may be encoded. These formats shall also apply to all lower-level CoverageSummaries under this CoverageSummary, in addition to any other formats identified. When included in a CoverageSummary with an Identifier, this list, including all values inherited from ancestor coverages, shall be an exact copy of the list of SupportedFormat parameters in the corresponding CoverageDescription. Each CoverageSummary shall list or inherit at least one SupportedFormat. ')

    _ElementMap.update({
        __Metadata.name() : __Metadata,
        __WGS84BoundingBox.name() : __WGS84BoundingBox,
        __Identifier.name() : __Identifier,
        __CoverageSummary.name() : __CoverageSummary,
        __SupportedCRS.name() : __SupportedCRS,
        __SupportedFormat.name() : __SupportedFormat
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CoverageSummaryType = CoverageSummaryType
Namespace.addCategoryObject('typeBinding', 'CoverageSummaryType', CoverageSummaryType)


# Complex type {http://www.opengis.net/wcs/1.1}CoveragesType with content type ELEMENT_ONLY
class CoveragesType (pyxb.binding.basis.complexTypeDefinition):
    """Group of coverages that can be used as the response from the WCS GetCoverage operation, allowing each coverage to include or reference multiple files. This Coverages element may also be used for outputs from, or inputs to, other OWS operations. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CoveragesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCoverages.xsd', 26, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wcs/1.1}Coverage uses Python identifier Coverage
    __Coverage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Coverage'), 'Coverage', '__httpwww_opengis_netwcs1_1_CoveragesType_httpwww_opengis_netwcs1_1Coverage', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCoverages.xsd', 35, 1), )

    
    Coverage = property(__Coverage.value, __Coverage.set, None, 'Complete data for one coverage, referencing each coverage file either remotely or locally in the same message. ')

    _ElementMap.update({
        __Coverage.name() : __Coverage
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CoveragesType = CoveragesType
Namespace.addCategoryObject('typeBinding', 'CoveragesType', CoveragesType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Response from a WCS DescribeCoverage operation, containing one or more coverage descriptions. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 55, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wcs/1.1}CoverageDescription uses Python identifier CoverageDescription
    __CoverageDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CoverageDescription'), 'CoverageDescription', '__httpwww_opengis_netwcs1_1_CTD_ANON__httpwww_opengis_netwcs1_1CoverageDescription', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 57, 4), )

    
    CoverageDescription = property(__CoverageDescription.value, __CoverageDescription.set, None, None)

    _ElementMap.update({
        __CoverageDescription.name() : __CoverageDescription
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {http://www.opengis.net/wcs/1.1}CoverageDescriptionType with content type ELEMENT_ONLY
class CoverageDescriptionType (pyxb.bundles.opengis.ows_1_1.DescriptionType):
    """Full description of one coverage available from a WCS server. This description shall include sufficient information to allow all valid GetCoverage operation requests to be prepared by a WCS client. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CoverageDescriptionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 62, 1)
    _ElementMap = pyxb.bundles.opengis.ows_1_1.DescriptionType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.ows_1_1.DescriptionType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.ows_1_1.DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/1.1}Keywords) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata'), 'Metadata', '__httpwww_opengis_netwcs1_1_CoverageDescriptionType_httpwww_opengis_netows1_1Metadata', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 42, 1), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/wcs/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), 'Identifier', '__httpwww_opengis_netwcs1_1_CoverageDescriptionType_httpwww_opengis_netwcs1_1Identifier', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 44, 1), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)

    
    # Element {http://www.opengis.net/wcs/1.1}Domain uses Python identifier Domain
    __Domain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Domain'), 'Domain', '__httpwww_opengis_netwcs1_1_CoverageDescriptionType_httpwww_opengis_netwcs1_1Domain', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 79, 5), )

    
    Domain = property(__Domain.value, __Domain.set, None, None)

    
    # Element {http://www.opengis.net/wcs/1.1}Range uses Python identifier Range
    __Range = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Range'), 'Range', '__httpwww_opengis_netwcs1_1_CoverageDescriptionType_httpwww_opengis_netwcs1_1Range', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 80, 5), )

    
    Range = property(__Range.value, __Range.set, None, None)

    
    # Element {http://www.opengis.net/wcs/1.1}SupportedCRS uses Python identifier SupportedCRS
    __SupportedCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SupportedCRS'), 'SupportedCRS', '__httpwww_opengis_netwcs1_1_CoverageDescriptionType_httpwww_opengis_netwcs1_1SupportedCRS', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 81, 5), )

    
    SupportedCRS = property(__SupportedCRS.value, __SupportedCRS.set, None, 'Unordered list of references to all the coordinate reference systems that may be referenced as the GridBaseCRS of a GridCRS specified in the Output part of a GetCoverage operation request. The GridBaseCRS of the GridCRS of a georectified offered coverage shall be listed as a SupportedCRS. An ImageCRS for an unrectified offered image shall be listed as a SupportedCRS, so that it may be referenced as the GridBaseCRS of a GridCRS. This ImageCRS shall be the ImageCRS of that unrectified offered image, or the ImageCRS that is referenced as the GridBaseCRS of the GridCRS that is used by that unrectified offered image  In addition, the GetCoverage operation output may be expressed in the ImageCRS or GridCRS of an unrectified offered coverage, instead of in a specified GridCRS. These Supported\xacCRSs can also be referenced in the BoundingBox in the DomainSubset part of a GetCoverage request. ')

    
    # Element {http://www.opengis.net/wcs/1.1}SupportedFormat uses Python identifier SupportedFormat
    __SupportedFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SupportedFormat'), 'SupportedFormat', '__httpwww_opengis_netwcs1_1_CoverageDescriptionType_httpwww_opengis_netwcs1_1SupportedFormat', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 86, 5), )

    
    SupportedFormat = property(__SupportedFormat.value, __SupportedFormat.set, None, 'Unordered list of identifiers of all the formats in which GetCoverage operation responses can be encoded for this coverage. ')

    _ElementMap.update({
        __Metadata.name() : __Metadata,
        __Identifier.name() : __Identifier,
        __Domain.name() : __Domain,
        __Range.name() : __Range,
        __SupportedCRS.name() : __SupportedCRS,
        __SupportedFormat.name() : __SupportedFormat
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CoverageDescriptionType = CoverageDescriptionType
Namespace.addCategoryObject('typeBinding', 'CoverageDescriptionType', CoverageDescriptionType)


# Complex type {http://www.opengis.net/wcs/1.1}CoverageDomainType with content type ELEMENT_ONLY
class CoverageDomainType (pyxb.binding.basis.complexTypeDefinition):
    """Definition of the spatial-temporal domain of a coverage. The Domain shall include a SpatialDomain (describing the spatial locations for which coverages can be requested), and should included a TemporalDomain (describing the time instants or intervals for which coverages can be requested). """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CoverageDomainType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 98, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wcs/1.1}SpatialDomain uses Python identifier SpatialDomain
    __SpatialDomain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SpatialDomain'), 'SpatialDomain', '__httpwww_opengis_netwcs1_1_CoverageDomainType_httpwww_opengis_netwcs1_1SpatialDomain', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 103, 3), )

    
    SpatialDomain = property(__SpatialDomain.value, __SpatialDomain.set, None, None)

    
    # Element {http://www.opengis.net/wcs/1.1}TemporalDomain uses Python identifier TemporalDomain
    __TemporalDomain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemporalDomain'), 'TemporalDomain', '__httpwww_opengis_netwcs1_1_CoverageDomainType_httpwww_opengis_netwcs1_1TemporalDomain', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 164, 1), )

    
    TemporalDomain = property(__TemporalDomain.value, __TemporalDomain.set, None, 'Definition of the temporal domain of a coverage, the times for which valid data are available. The times should to be ordered from the oldest to the newest. ')

    _ElementMap.update({
        __SpatialDomain.name() : __SpatialDomain,
        __TemporalDomain.name() : __TemporalDomain
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CoverageDomainType = CoverageDomainType
Namespace.addCategoryObject('typeBinding', 'CoverageDomainType', CoverageDomainType)


# Complex type {http://www.opengis.net/wcs/1.1}SpatialDomainType with content type ELEMENT_ONLY
class SpatialDomainType (pyxb.binding.basis.complexTypeDefinition):
    """Definition of the spatial domain of a coverage. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpatialDomainType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 112, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml}_CoordinateOperation uses Python identifier CoordinateOperation
    __CoordinateOperation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, '_CoordinateOperation'), 'CoordinateOperation', '__httpwww_opengis_netwcs1_1_SpatialDomainType_httpwww_opengis_netgml_CoordinateOperation', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/coordinateOperations.xsd', 24, 1), )

    
    CoordinateOperation = property(__CoordinateOperation.value, __CoordinateOperation.set, None, None)

    
    # Element {http://www.opengis.net/gml}Polygon uses Python identifier Polygon
    __Polygon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'Polygon'), 'Polygon', '__httpwww_opengis_netwcs1_1_SpatialDomainType_httpwww_opengis_netgmlPolygon', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/geometryBasic2d.xsd', 72, 1), )

    
    Polygon = property(__Polygon.value, __Polygon.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}BoundingBox uses Python identifier BoundingBox
    __BoundingBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'BoundingBox'), 'BoundingBox', '__httpwww_opengis_netwcs1_1_SpatialDomainType_httpwww_opengis_netows1_1BoundingBox', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 70, 1), )

    
    BoundingBox = property(__BoundingBox.value, __BoundingBox.set, None, None)

    
    # Element {http://www.opengis.net/wcs/1.1}ImageCRS uses Python identifier ImageCRS
    __ImageCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ImageCRS'), 'ImageCRS', '__httpwww_opengis_netwcs1_1_SpatialDomainType_httpwww_opengis_netwcs1_1ImageCRS', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 135, 3), )

    
    ImageCRS = property(__ImageCRS.value, __ImageCRS.set, None, 'Association to ImageCRS of an unrectified offered coverage. The ImageCRS shall be referenced in the SpatialDomain when the offered coverage does not have a known GridCRS. Such a coverage is always unrectified, but an unrectified coverage may have a GridCRS instead of an ImageCRS. This ImageCRS applies to this offered coverage, but does not (normally) specify its spatial resolution. The ImageCRS and the GridCRS shall be mutually exclusive in this SpatialDomain. ')

    
    # Element {http://www.opengis.net/wcs/1.1}GridCRS uses Python identifier GridCRS
    __GridCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GridCRS'), 'GridCRS', '__httpwww_opengis_netwcs1_1_SpatialDomainType_httpwww_opengis_netwcs1_1GridCRS', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 28, 1), )

    
    GridCRS = property(__GridCRS.value, __GridCRS.set, None, None)

    _ElementMap.update({
        __CoordinateOperation.name() : __CoordinateOperation,
        __Polygon.name() : __Polygon,
        __BoundingBox.name() : __BoundingBox,
        __ImageCRS.name() : __ImageCRS,
        __GridCRS.name() : __GridCRS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SpatialDomainType = SpatialDomainType
Namespace.addCategoryObject('typeBinding', 'SpatialDomainType', SpatialDomainType)


# Complex type {http://www.opengis.net/wcs/1.1}ImageCRSRefType with content type ELEMENT_ONLY
class ImageCRSRefType (pyxb.binding.basis.complexTypeDefinition):
    """Association to an image coordinate reference system, either referencing or containing the definition of that reference system. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ImageCRSRefType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 154, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml}ImageCRS uses Python identifier ImageCRS
    __ImageCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'ImageCRS'), 'ImageCRS', '__httpwww_opengis_netwcs1_1_ImageCRSRefType_httpwww_opengis_netgmlImageCRS', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/coordinateReferenceSystems.xsd', 347, 1), )

    
    ImageCRS = property(__ImageCRS.value, __ImageCRS.set, None, None)

    
    # Attribute {http://www.opengis.net/gml}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netwcs1_1_ImageCRSRefType_httpwww_opengis_netgmlremoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 258, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 269, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, 'Reference to an XML Schema fragment that specifies the content model of the propertys value. This is in conformance with the XML Schema Section 4.14 Referencing Schemas from Elsewhere.')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netwcs1_1_ImageCRSRefType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netwcs1_1_ImageCRSRefType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netwcs1_1_ImageCRSRefType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netwcs1_1_ImageCRSRefType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netwcs1_1_ImageCRSRefType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netwcs1_1_ImageCRSRefType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netwcs1_1_ImageCRSRefType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __ImageCRS.name() : __ImageCRS
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.ImageCRSRefType = ImageCRSRefType
Namespace.addCategoryObject('typeBinding', 'ImageCRSRefType', ImageCRSRefType)


# Complex type {http://www.opengis.net/wcs/1.1}RangeType with content type ELEMENT_ONLY
class RangeType (pyxb.binding.basis.complexTypeDefinition):
    """Defines the fields (categories, measures, or values) in the range records available for each location in the coverage domain. Each such field may be a scalar (numeric or text) value, such as population density, or a vector (compound or tensor) of many similar values, such as incomes by race, or radiances by wavelength. Each range field is typically an observable whose meaning and reference system are referenced by URIs. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RangeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 172, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wcs/1.1}Field uses Python identifier Field
    __Field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Field'), 'Field', '__httpwww_opengis_netwcs1_1_RangeType_httpwww_opengis_netwcs1_1Field', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 177, 3), )

    
    Field = property(__Field.value, __Field.set, None, 'Unordered list of the Fields in the Range of a coverage. ')

    _ElementMap.update({
        __Field.name() : __Field
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RangeType = RangeType
Namespace.addCategoryObject('typeBinding', 'RangeType', RangeType)


# Complex type {http://www.opengis.net/wcs/1.1}FieldType with content type ELEMENT_ONLY
class FieldType (pyxb.bundles.opengis.ows_1_1.DescriptionType):
    """Description of an individual field in a coverage range record. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FieldType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 185, 1)
    _ElementMap = pyxb.bundles.opengis.ows_1_1.DescriptionType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.ows_1_1.DescriptionType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.ows_1_1.DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/1.1}Keywords) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element {http://www.opengis.net/wcs/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), 'Identifier', '__httpwww_opengis_netwcs1_1_FieldType_httpwww_opengis_netwcs1_1Identifier', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 44, 1), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)

    
    # Element {http://www.opengis.net/wcs/1.1}Definition uses Python identifier Definition
    __Definition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Definition'), 'Definition', '__httpwww_opengis_netwcs1_1_FieldType_httpwww_opengis_netwcs1_1Definition', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 197, 5), )

    
    Definition = property(__Definition.value, __Definition.set, None, 'Further definition of this field, including meaning, units, etc. In this Definition, the AllowedValues should be used to encode the extent of possible values for this field, excluding the Null Value. If the range is not known, AnyValue should be used. ')

    
    # Element {http://www.opengis.net/wcs/1.1}NullValue uses Python identifier NullValue
    __NullValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NullValue'), 'NullValue', '__httpwww_opengis_netwcs1_1_FieldType_httpwww_opengis_netwcs1_1NullValue', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 202, 5), )

    
    NullValue = property(__NullValue.value, __NullValue.set, None, 'Unordered list of the values used when valid Field values are not available for whatever reason. The coverage encoding itself may specify a fixed value for null (e.g. \u201c\u201399999\u201d or \u201cN/A\u201d), but often the choice is up to the provider and must be communicated to the client outside the coverage itself. Each null value shall be encoded as a string. The optional codeSpace attribute can reference a definition of the reason why this value is null. ')

    
    # Element {http://www.opengis.net/wcs/1.1}Axis uses Python identifier Axis
    __Axis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Axis'), 'Axis', '__httpwww_opengis_netwcs1_1_FieldType_httpwww_opengis_netwcs1_1Axis', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 212, 5), )

    
    Axis = property(__Axis.value, __Axis.set, None, 'Unordered list of the axes in a vector field for which there are Field values. This list shall be included when this Field has a vector of values. Notice that the axes can be listed here in any order; however, the axis order listed here shall be used in the KVP encoding of a GetCoverage operation request. ')

    
    # Element {http://www.opengis.net/wcs/1.1}InterpolationMethods uses Python identifier InterpolationMethods
    __InterpolationMethods = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InterpolationMethods'), 'InterpolationMethods', '__httpwww_opengis_netwcs1_1_FieldType_httpwww_opengis_netwcs1_1InterpolationMethods', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 24, 1), )

    
    InterpolationMethods = property(__InterpolationMethods.value, __InterpolationMethods.set, None, 'List of the interpolation method(s) that may be used when continuous grid coverage resampling is needed. ')

    _ElementMap.update({
        __Identifier.name() : __Identifier,
        __Definition.name() : __Definition,
        __NullValue.name() : __NullValue,
        __Axis.name() : __Axis,
        __InterpolationMethods.name() : __InterpolationMethods
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FieldType = FieldType
Namespace.addCategoryObject('typeBinding', 'FieldType', FieldType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """List of all the available (valid) key values for this axis. For numeric keys, signed values should be ordered from negative infinity to positive infinity. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 265, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wcs/1.1}Key uses Python identifier Key
    __Key = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Key'), 'Key', '__httpwww_opengis_netwcs1_1_CTD_ANON_2_httpwww_opengis_netwcs1_1Key', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 267, 4), )

    
    Key = property(__Key.value, __Key.set, None, 'Valid key value for this axis. There will normally be more than one key value for an axis, but one is allowed for special circumstances. ')

    _ElementMap.update({
        __Key.name() : __Key
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.bundles.opengis.ows_1_1.GetCapabilitiesType):
    """Request to a WCS server to perform the GetCapabilities operation. This operation allows a client to retrieve a Capabilities XML document providing metadata for the specific WCS server. In this XML encoding, no "request" parameter is included, since the element name specifies the specific operation. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCapabilities.xsd', 29, 2)
    _ElementMap = pyxb.bundles.opengis.ows_1_1.GetCapabilitiesType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.ows_1_1.GetCapabilitiesType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.ows_1_1.GetCapabilitiesType
    
    # Element AcceptVersions ({http://www.opengis.net/ows/1.1}AcceptVersions) inherited from {http://www.opengis.net/ows/1.1}GetCapabilitiesType
    
    # Element Sections ({http://www.opengis.net/ows/1.1}Sections) inherited from {http://www.opengis.net/ows/1.1}GetCapabilitiesType
    
    # Element AcceptFormats ({http://www.opengis.net/ows/1.1}AcceptFormats) inherited from {http://www.opengis.net/ows/1.1}GetCapabilitiesType
    
    # Attribute updateSequence inherited from {http://www.opengis.net/ows/1.1}GetCapabilitiesType
    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__httpwww_opengis_netwcs1_1_CTD_ANON_3_service', pyxb.bundles.opengis.ows_1_1.ServiceType, fixed=True, unicode_default='WCS', required=True)
    __service._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCapabilities.xsd', 33, 5)
    __service._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCapabilities.xsd', 33, 5)
    
    service = property(__service.value, __service.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __service.name() : __service
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.bundles.opengis.ows_1_1.CapabilitiesBaseType):
    """XML encoded WCS GetCapabilities operation response. The Capabilities document provides clients with service metadata about a specific service instance, including metadata about the coverages served. If the server does not implement the updateSequence parameter, the server shall always return the Capabilities document, without the updateSequence parameter. When the server implements the updateSequence parameter and the GetCapabilities operation request included the updateSequence parameter with the current value, the server shall return this element with only the "version" and "updateSequence" attributes. Otherwise, all optional sections shall be included or not depending on the actual value of the Contents parameter in the GetCapabilities operation request. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCapabilities.xsd', 43, 2)
    _ElementMap = pyxb.bundles.opengis.ows_1_1.CapabilitiesBaseType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.ows_1_1.CapabilitiesBaseType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.ows_1_1.CapabilitiesBaseType
    
    # Element OperationsMetadata ({http://www.opengis.net/ows/1.1}OperationsMetadata) inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Element ServiceIdentification ({http://www.opengis.net/ows/1.1}ServiceIdentification) inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Element ServiceProvider ({http://www.opengis.net/ows/1.1}ServiceProvider) inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Element {http://www.opengis.net/wcs/1.1}Contents uses Python identifier Contents
    __Contents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Contents'), 'Contents', '__httpwww_opengis_netwcs1_1_CTD_ANON_4_httpwww_opengis_netwcs1_1Contents', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 25, 1), )

    
    Contents = property(__Contents.value, __Contents.set, None, 'Contents section of WCS service metadata (or Capabilities) XML document. For the WCS, these contents are brief metadata about the coverages available from this server, or a reference to another source from which this metadata is available. ')

    
    # Attribute version inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Attribute updateSequence inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    _ElementMap.update({
        __Contents.name() : __Contents
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type {http://www.opengis.net/wcs/1.1}OutputType with content type ELEMENT_ONLY
class OutputType (pyxb.binding.basis.complexTypeDefinition):
    """Asks for the GetCoverage response to be expressed in a particular CRS and encoded in a particular format. Can also ask for the response coverage to be stored remotely from the client at a URL, instead of being returned in the operation response. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OutputType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 53, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wcs/1.1}GridCRS uses Python identifier GridCRS
    __GridCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GridCRS'), 'GridCRS', '__httpwww_opengis_netwcs1_1_OutputType_httpwww_opengis_netwcs1_1GridCRS', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 28, 1), )

    
    GridCRS = property(__GridCRS.value, __GridCRS.set, None, None)

    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'format'), 'format', '__httpwww_opengis_netwcs1_1_OutputType_format', pyxb.bundles.opengis.ows_1_1.MimeType, required=True)
    __format._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 64, 2)
    __format._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 64, 2)
    
    format = property(__format.value, __format.set, None, 'Identifier of the format in which GetCoverage response shall be encoded. This identifier value shall be among those listed as SupportedFormats in the DescribeCoverage operation response. ')

    
    # Attribute store uses Python identifier store
    __store = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'store'), 'store', '__httpwww_opengis_netwcs1_1_OutputType_store', pyxb.binding.datatypes.boolean, unicode_default='false')
    __store._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 69, 2)
    __store._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 69, 2)
    
    store = property(__store.value, __store.set, None, 'Specifies if the output coverage should be stored, remotely from the client at a network URL, instead of being returned with the operation response. This parameter should be included only if this operation parameter is supported by server, as encoded in the OperationsMetadata section of the Capabilities document. ')

    _ElementMap.update({
        __GridCRS.name() : __GridCRS
    })
    _AttributeMap.update({
        __format.name() : __format,
        __store.name() : __store
    })
_module_typeBindings.OutputType = OutputType
Namespace.addCategoryObject('typeBinding', 'OutputType', OutputType)


# Complex type {http://www.opengis.net/wcs/1.1}DomainSubsetType with content type ELEMENT_ONLY
class DomainSubsetType (pyxb.binding.basis.complexTypeDefinition):
    """Definition of the desired subset of the domain of the coverage. Contains a spatial BoundingBox and optionally a TemporalSubset. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DomainSubsetType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 78, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}BoundingBox uses Python identifier BoundingBox
    __BoundingBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'BoundingBox'), 'BoundingBox', '__httpwww_opengis_netwcs1_1_DomainSubsetType_httpwww_opengis_netows1_1BoundingBox', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 70, 1), )

    
    BoundingBox = property(__BoundingBox.value, __BoundingBox.set, None, None)

    
    # Element {http://www.opengis.net/wcs/1.1}TemporalSubset uses Python identifier TemporalSubset
    __TemporalSubset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemporalSubset'), 'TemporalSubset', '__httpwww_opengis_netwcs1_1_DomainSubsetType_httpwww_opengis_netwcs1_1TemporalSubset', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 96, 1), )

    
    TemporalSubset = property(__TemporalSubset.value, __TemporalSubset.set, None, 'Definition of subset of coverage temporal domain. ')

    _ElementMap.update({
        __BoundingBox.name() : __BoundingBox,
        __TemporalSubset.name() : __TemporalSubset
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DomainSubsetType = DomainSubsetType
Namespace.addCategoryObject('typeBinding', 'DomainSubsetType', DomainSubsetType)


# Complex type {http://www.opengis.net/wcs/1.1}RangeSubsetType with content type ELEMENT_ONLY
class RangeSubsetType (pyxb.binding.basis.complexTypeDefinition):
    """Selection of desired subset of the coverage's range fields, (optionally) the interpolation method applied to each field, and (optionally) field subsets. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RangeSubsetType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 104, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wcs/1.1}FieldSubset uses Python identifier FieldSubset
    __FieldSubset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FieldSubset'), 'FieldSubset', '__httpwww_opengis_netwcs1_1_RangeSubsetType_httpwww_opengis_netwcs1_1FieldSubset', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 109, 3), )

    
    FieldSubset = property(__FieldSubset.value, __FieldSubset.set, None, 'Unordered list of one or more desired subsets of range fields. TBD. ')

    _ElementMap.update({
        __FieldSubset.name() : __FieldSubset
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RangeSubsetType = RangeSubsetType
Namespace.addCategoryObject('typeBinding', 'RangeSubsetType', RangeSubsetType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Unordered list of one or more desired subsets of range fields. TBD. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 113, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier'), 'Identifier', '__httpwww_opengis_netwcs1_1_CTD_ANON_5_httpwww_opengis_netows1_1Identifier', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 87, 1), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, 'Unique identifier or name of this dataset. ')

    
    # Element {http://www.opengis.net/wcs/1.1}InterpolationType uses Python identifier InterpolationType
    __InterpolationType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InterpolationType'), 'InterpolationType', '__httpwww_opengis_netwcs1_1_CTD_ANON_5_httpwww_opengis_netwcs1_1InterpolationType', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 120, 6), )

    
    InterpolationType = property(__InterpolationType.value, __InterpolationType.set, None, 'Optional identifier of the spatial interpolation type to be applied to this range field. This interpolation type shall be one that is identified for this Field in the CoverageDescription. When this parameter is omitted, the interpolation method used shall be the default method specified for this Field, if any. ')

    
    # Element {http://www.opengis.net/wcs/1.1}AxisSubset uses Python identifier AxisSubset
    __AxisSubset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AxisSubset'), 'AxisSubset', '__httpwww_opengis_netwcs1_1_CTD_ANON_5_httpwww_opengis_netwcs1_1AxisSubset', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 136, 1), )

    
    AxisSubset = property(__AxisSubset.value, __AxisSubset.set, None, 'List of selected Keys for this axis, to be used for selecting values in a vector range field. TBD. ')

    _ElementMap.update({
        __Identifier.name() : __Identifier,
        __InterpolationType.name() : __InterpolationType,
        __AxisSubset.name() : __AxisSubset
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """List of selected Keys for this axis, to be used for selecting values in a vector range field. TBD. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 140, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wcs/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), 'Identifier', '__httpwww_opengis_netwcs1_1_CTD_ANON_6_httpwww_opengis_netwcs1_1Identifier', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 44, 1), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)

    
    # Element {http://www.opengis.net/wcs/1.1}Key uses Python identifier Key
    __Key = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Key'), 'Key', '__httpwww_opengis_netwcs1_1_CTD_ANON_6_httpwww_opengis_netwcs1_1Key', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 147, 4), )

    
    Key = property(__Key.value, __Key.set, None, 'Unordered list of (at least one) Key, to be used for selecting values in a range vector field. The Keys within this list shall be unique. ')

    _ElementMap.update({
        __Identifier.name() : __Identifier,
        __Key.name() : __Key
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type {http://www.opengis.net/wcs/1.1}GridCrsType with content type ELEMENT_ONLY
class GridCrsType (pyxb.binding.basis.complexTypeDefinition):
    """Definition of a coordinate reference system (CRS) for a quadrilateral grid that is defined in another CRS, where this grid is defined by its coordinate Conversion from the other CRS. This GridCRS is not a ProjectedCRS. However, like a ProjectedCRS, the coordinate system used is Cartesian. This GridCRS can use any type of GridBaseCRS, including GeographicCRS, ProjectedCRS, ImageCRS, or a different GridCRS. This GridCRS is a simplification and specialization of a gml:DerivedCRS. All elements and attributes not required to define this GridCRS are optional. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GridCrsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 30, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml}srsName uses Python identifier srsName
    __srsName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'srsName'), 'srsName', '__httpwww_opengis_netwcs1_1_GridCrsType_httpwww_opengis_netgmlsrsName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/referenceSystems.xsd', 40, 1), )

    
    srsName = property(__srsName.value, __srsName.set, None, 'The name by which this reference system is identified.')

    
    # Element {http://www.opengis.net/wcs/1.1}GridBaseCRS uses Python identifier GridBaseCRS
    __GridBaseCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GridBaseCRS'), 'GridBaseCRS', '__httpwww_opengis_netwcs1_1_GridCrsType_httpwww_opengis_netwcs1_1GridBaseCRS', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 58, 1), )

    
    GridBaseCRS = property(__GridBaseCRS.value, __GridBaseCRS.set, None, 'Association to the coordinate reference system (CRS) in which this Grid CRS is specified. A GridCRS can use any type of GridBaseCRS, including GeographicCRS, ProjectedCRS, ImageCRS, or a different GridCRS. For a GridCRS, this association is limited to a remote definition of the GridBaseCRS (not encoded in-line). ')

    
    # Element {http://www.opengis.net/wcs/1.1}GridType uses Python identifier GridType
    __GridType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GridType'), 'GridType', '__httpwww_opengis_netwcs1_1_GridCrsType_httpwww_opengis_netwcs1_1GridType', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 65, 1), )

    
    GridType = property(__GridType.value, __GridType.set, None, 'Association to the OperationMethod used to define this Grid CRS. This association defaults to an association to the most commonly used method, which is referenced by the URN "urn:ogc:def:method:WCS:1.1:2dSimpleGrid". For a GridCRS, this association is limited to a remote definition of a grid definition Method (not encoded in-line) that encodes a variation on the method implied by the CV_RectifiedGrid class in ISO 19123, without the inheritance from CV_Grid. ')

    
    # Element {http://www.opengis.net/wcs/1.1}GridOrigin uses Python identifier GridOrigin
    __GridOrigin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GridOrigin'), 'GridOrigin', '__httpwww_opengis_netwcs1_1_GridCrsType_httpwww_opengis_netwcs1_1GridOrigin', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 72, 1), )

    
    GridOrigin = property(__GridOrigin.value, __GridOrigin.set, None, 'Coordinates of the grid origin position in the GridBaseCRS of this GridCRS. This origin defaults be the most commonly used origin in a GridCRS used in the output part of a GetCapabilities operation request, namely "0 0". This element is adapted from gml:pos. ')

    
    # Element {http://www.opengis.net/wcs/1.1}GridOffsets uses Python identifier GridOffsets
    __GridOffsets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GridOffsets'), 'GridOffsets', '__httpwww_opengis_netwcs1_1_GridCrsType_httpwww_opengis_netwcs1_1GridOffsets', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 79, 1), )

    
    GridOffsets = property(__GridOffsets.value, __GridOffsets.set, None, 'Two or more grid position offsets from the grid origin in the GridBaseCRS of this GridCRS. Example: For the grid2dIn2dCRS OperationMethod, this Offsets element shall contain four values, the first two values shall specify the grid offset for the first grid axis in the 2D base CRS, and the second pair of values shall specify the grid offset for the second grid axis. In this case, the middle two values are zero for un-rotated and un-skewed grids. ')

    
    # Element {http://www.opengis.net/wcs/1.1}GridCS uses Python identifier GridCS
    __GridCS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GridCS'), 'GridCS', '__httpwww_opengis_netwcs1_1_GridCrsType_httpwww_opengis_netwcs1_1GridCS', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 85, 1), )

    
    GridCS = property(__GridCS.value, __GridCS.set, None, 'Association to the (Cartesian) grid coordinate system used by this Grid CRS. In this use of a (Cartesian) grid coordinate system, the grid positions shall be in the centers of the image or other grid coverage values (not between the grid values), as specified in ISO 19123. Also, the grid point indices at the origin shall be 0, 0 (not 1,1), as specified in ISO 19123. This GridCS defaults to the most commonly used grid coordinate system, which is referenced by the URN "urn:ogc:def:cs:OGC:0.0:Grid2dSquareCS". For a GridCRS, this association is limited to a remote definition of the GridCS (not encoded in-line). ')

    
    # Attribute {http://www.opengis.net/gml}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'id'), 'id', '__httpwww_opengis_netwcs1_1_GridCrsType_httpwww_opengis_netgmlid', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 252, 1)
    __id._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 55, 2)
    
    id = property(__id.value, __id.set, None, 'Database handle for the object.  It is of XML type ID, so is constrained to be unique in the XML document within which it occurs.  An external identifier for the object in the form of a URI may be constructed using standard XML and XPointer methods.  This is done by concatenating the URI for the document, a fragment separator, and the value of the id attribute.')

    _ElementMap.update({
        __srsName.name() : __srsName,
        __GridBaseCRS.name() : __GridBaseCRS,
        __GridType.name() : __GridType,
        __GridOrigin.name() : __GridOrigin,
        __GridOffsets.name() : __GridOffsets,
        __GridCS.name() : __GridCS
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.GridCrsType = GridCrsType
Namespace.addCategoryObject('typeBinding', 'GridCrsType', GridCrsType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """List of the interpolation method(s) that may be used when continuous grid coverage resampling is needed. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 28, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wcs/1.1}InterpolationMethod uses Python identifier InterpolationMethod
    __InterpolationMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InterpolationMethod'), 'InterpolationMethod', '__httpwww_opengis_netwcs1_1_CTD_ANON_7_httpwww_opengis_netwcs1_1InterpolationMethod', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 30, 4), )

    
    InterpolationMethod = property(__InterpolationMethod.value, __InterpolationMethod.set, None, 'Unordered list of identifiers of all other supported spatial interpolation methods. ')

    
    # Element {http://www.opengis.net/wcs/1.1}Default uses Python identifier Default
    __Default = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Default'), 'Default', '__httpwww_opengis_netwcs1_1_CTD_ANON_7_httpwww_opengis_netwcs1_1Default', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 35, 4), )

    
    Default = property(__Default.value, __Default.set, None, 'Identifier of interpolation method that will be used if the client does not specify one. ')

    _ElementMap.update({
        __InterpolationMethod.name() : __InterpolationMethod,
        __Default.name() : __Default
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type {http://www.opengis.net/wcs/1.1}InterpolationMethodBaseType with content type SIMPLE
class InterpolationMethodBaseType (pyxb.bundles.opengis.ows_1_1.CodeType):
    """Identifier of an interpolation method applicable to continuous grid coverages. The string in this type shall be one interpolation type identifier string, selected from the referenced dictionary. Adapts gml:CodeWithAuthorityType from GML 3.2 for this WCS purpose, allowing the codeSpace to be omitted but providing a default value for the standard interpolation methods defined in Annex C of ISO 19123: Geographic information - Schema for coverage geometry and functions. """
    _TypeDefinition = STD_ANON
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InterpolationMethodBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 59, 1)
    _ElementMap = pyxb.bundles.opengis.ows_1_1.CodeType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.ows_1_1.CodeType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.ows_1_1.CodeType
    
    # Attribute codeSpace is restricted from parent
    
    # Attribute codeSpace uses Python identifier codeSpace
    __codeSpace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'codeSpace'), 'codeSpace', '__httpwww_opengis_netows1_1_CodeType_codeSpace', pyxb.binding.datatypes.anyURI, unicode_default='http://schemas.opengis.net/wcs/1.1.0/interpolationMethods.xml')
    __codeSpace._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 66, 4)
    __codeSpace._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 66, 4)
    
    codeSpace = property(__codeSpace.value, __codeSpace.set, None, 'Reference to a dictionary that specifies allowed values for interpolation method identifier strings and nullResistance identifier strings. This reference defaults to the standard interpolation methods dictionary specified in WCS 1.1.0. ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __codeSpace.name() : __codeSpace
    })
_module_typeBindings.InterpolationMethodBaseType = InterpolationMethodBaseType
Namespace.addCategoryObject('typeBinding', 'InterpolationMethodBaseType', InterpolationMethodBaseType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (RequestBaseType):
    """Request to a WCS to perform the DescribeCoverage operation. This operation allows a client to retrieve descriptions of one or more coverages. In this XML encoding, no "request" parameter is included, since the element name specifies the specific operation. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 36, 2)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/wcs/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), 'Identifier', '__httpwww_opengis_netwcs1_1_CTD_ANON_8_httpwww_opengis_netwcs1_1Identifier', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 44, 1), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)

    
    # Attribute service inherited from {http://www.opengis.net/wcs/1.1}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/wcs/1.1}RequestBaseType
    _ElementMap.update({
        __Identifier.name() : __Identifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type {http://www.opengis.net/wcs/1.1}AxisType with content type ELEMENT_ONLY
class AxisType (pyxb.bundles.opengis.ows_1_1.DescriptionType):
    """Definition of one axis in a field for which there are a vector of values. This type is largely a subset of the ows:DomainType as needed for a range field axis. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AxisType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 222, 1)
    _ElementMap = pyxb.bundles.opengis.ows_1_1.DescriptionType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.ows_1_1.DescriptionType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.ows_1_1.DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/1.1}Keywords) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata'), 'Metadata', '__httpwww_opengis_netwcs1_1_AxisType_httpwww_opengis_netows1_1Metadata', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 42, 1), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}Meaning uses Python identifier Meaning
    __Meaning = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Meaning'), 'Meaning', '__httpwww_opengis_netwcs1_1_AxisType_httpwww_opengis_netows1_1Meaning', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDomainType.xsd', 256, 1), )

    
    Meaning = property(__Meaning.value, __Meaning.set, None, 'Definition of the meaning or semantics of this set of values. This Meaning can provide more specific, complete, precise, machine accessible, and machine understandable semantics about this quantity, relative to other available semantic information. For example, other semantic information is often provided in "documentation" elements in XML Schemas or "description" elements in GML objects. ')

    
    # Element {http://www.opengis.net/ows/1.1}DataType uses Python identifier DataType
    __DataType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'DataType'), 'DataType', '__httpwww_opengis_netwcs1_1_AxisType_httpwww_opengis_netows1_1DataType', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDomainType.xsd', 262, 1), )

    
    DataType = property(__DataType.value, __DataType.set, None, 'Definition of the data type of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known data type. For example, such a URN could be a data type identification URN defined in the "ogc" URN namespace. ')

    
    # Element {http://www.opengis.net/ows/1.1}ReferenceSystem uses Python identifier ReferenceSystem
    __ReferenceSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'ReferenceSystem'), 'ReferenceSystem', '__httpwww_opengis_netwcs1_1_AxisType_httpwww_opengis_netows1_1ReferenceSystem', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDomainType.xsd', 268, 1), )

    
    ReferenceSystem = property(__ReferenceSystem.value, __ReferenceSystem.set, None, 'Definition of the reference system used by this set of values, including the unit of measure whenever applicable (as is normal). In this case, the xlink:href attribute can reference a URN for a well-known reference system, such as for a coordinate reference system (CRS). For example, such a URN could be a CRS identification URN defined in the "ogc" URN namespace. ')

    
    # Element {http://www.opengis.net/ows/1.1}UOM uses Python identifier UOM
    __UOM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'UOM'), 'UOM', '__httpwww_opengis_netwcs1_1_AxisType_httpwww_opengis_netows1_1UOM', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDomainType.xsd', 274, 1), )

    
    UOM = property(__UOM.value, __UOM.set, None, 'Definition of the unit of measure of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known unit of measure (uom). For example, such a URN could be a UOM identification URN defined in the "ogc" URN namespace. ')

    
    # Element {http://www.opengis.net/wcs/1.1}AvailableKeys uses Python identifier AvailableKeys
    __AvailableKeys = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AvailableKeys'), 'AvailableKeys', '__httpwww_opengis_netwcs1_1_AxisType_httpwww_opengis_netwcs1_1AvailableKeys', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 261, 1), )

    
    AvailableKeys = property(__AvailableKeys.value, __AvailableKeys.set, None, 'List of all the available (valid) key values for this axis. For numeric keys, signed values should be ordered from negative infinity to positive infinity. ')

    
    # Attribute identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'identifier'), 'identifier', '__httpwww_opengis_netwcs1_1_AxisType_identifier', _module_typeBindings.IdentifierType, required=True)
    __identifier._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 252, 4)
    __identifier._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 252, 4)
    
    identifier = property(__identifier.value, __identifier.set, None, 'Name or identifier of this axis. ')

    _ElementMap.update({
        __Metadata.name() : __Metadata,
        __Meaning.name() : __Meaning,
        __DataType.name() : __DataType,
        __ReferenceSystem.name() : __ReferenceSystem,
        __UOM.name() : __UOM,
        __AvailableKeys.name() : __AvailableKeys
    })
    _AttributeMap.update({
        __identifier.name() : __identifier
    })
_module_typeBindings.AxisType = AxisType
Namespace.addCategoryObject('typeBinding', 'AxisType', AxisType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (RequestBaseType):
    """Request to a WCS to perform the GetCoverage operation. This operation allows a client to retrieve a subset of one coverage. In this XML encoding, no "request" parameter is included, since the element name specifies the specific operation. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 31, 2)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier'), 'Identifier', '__httpwww_opengis_netwcs1_1_CTD_ANON_9_httpwww_opengis_netows1_1Identifier', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 87, 1), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, 'Unique identifier or name of this dataset. ')

    
    # Element {http://www.opengis.net/wcs/1.1}DomainSubset uses Python identifier DomainSubset
    __DomainSubset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DomainSubset'), 'DomainSubset', '__httpwww_opengis_netwcs1_1_CTD_ANON_9_httpwww_opengis_netwcs1_1DomainSubset', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 40, 6), )

    
    DomainSubset = property(__DomainSubset.value, __DomainSubset.set, None, None)

    
    # Element {http://www.opengis.net/wcs/1.1}RangeSubset uses Python identifier RangeSubset
    __RangeSubset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RangeSubset'), 'RangeSubset', '__httpwww_opengis_netwcs1_1_CTD_ANON_9_httpwww_opengis_netwcs1_1RangeSubset', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 41, 6), )

    
    RangeSubset = property(__RangeSubset.value, __RangeSubset.set, None, "Optional selection of a subset of the coverage's range. ")

    
    # Element {http://www.opengis.net/wcs/1.1}Output uses Python identifier Output
    __Output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Output'), 'Output', '__httpwww_opengis_netwcs1_1_CTD_ANON_9_httpwww_opengis_netwcs1_1Output', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 46, 6), )

    
    Output = property(__Output.value, __Output.set, None, None)

    
    # Attribute service inherited from {http://www.opengis.net/wcs/1.1}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/wcs/1.1}RequestBaseType
    _ElementMap.update({
        __Identifier.name() : __Identifier,
        __DomainSubset.name() : __DomainSubset,
        __RangeSubset.name() : __RangeSubset,
        __Output.name() : __Output
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type {http://www.opengis.net/wcs/1.1}InterpolationMethodType with content type SIMPLE
class InterpolationMethodType (InterpolationMethodBaseType):
    """Identifier of a spatial interpolation method applicable to continuous grid coverages, plus the optional "null Resistance" parameter. """
    _TypeDefinition = STD_ANON
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InterpolationMethodType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 44, 1)
    _ElementMap = InterpolationMethodBaseType._ElementMap.copy()
    _AttributeMap = InterpolationMethodBaseType._AttributeMap.copy()
    # Base type is InterpolationMethodBaseType
    
    # Attribute nullResistance uses Python identifier nullResistance
    __nullResistance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nullResistance'), 'nullResistance', '__httpwww_opengis_netwcs1_1_InterpolationMethodType_nullResistance', pyxb.binding.datatypes.string)
    __nullResistance._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 50, 4)
    __nullResistance._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 50, 4)
    
    nullResistance = property(__nullResistance.value, __nullResistance.set, None, 'Identifier of how the server handles null values when spatially interpolating values in this field using this interpolation method. This identifier shall be selected from the referenced dictionary. This parameter shall be omitted when the rule for handling nulls is unknown. ')

    
    # Attribute codeSpace_ inherited from {http://www.opengis.net/wcs/1.1}InterpolationMethodBaseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __nullResistance.name() : __nullResistance
    })
_module_typeBindings.InterpolationMethodType = InterpolationMethodType
Namespace.addCategoryObject('typeBinding', 'InterpolationMethodType', InterpolationMethodType)


Coverage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Coverage'), pyxb.bundles.opengis.ows_1_1.ReferenceGroupType, documentation='Complete data for one coverage, referencing each coverage file either remotely or locally in the same message. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCoverages.xsd', 35, 1))
Namespace.addCategoryObject('elementBinding', Coverage.name().localName(), Coverage)

Transformation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Transformation'), pyxb.bundles.opengis.gml.AbstractCoordinateOperationType, documentation='Georeferencing coordinate transformation for unrectified coverage. This georeferencing transformation can be specified as a Transformation, or a ConcatenatedOperation that includes at least one Transformation. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 148, 1))
Namespace.addCategoryObject('elementBinding', Transformation.name().localName(), Transformation)

GridBaseCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GridBaseCRS'), pyxb.binding.datatypes.anyURI, documentation='Association to the coordinate reference system (CRS) in which this Grid CRS is specified. A GridCRS can use any type of GridBaseCRS, including GeographicCRS, ProjectedCRS, ImageCRS, or a different GridCRS. For a GridCRS, this association is limited to a remote definition of the GridBaseCRS (not encoded in-line). ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 58, 1))
Namespace.addCategoryObject('elementBinding', GridBaseCRS.name().localName(), GridBaseCRS)

GridType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GridType'), pyxb.binding.datatypes.anyURI, documentation='Association to the OperationMethod used to define this Grid CRS. This association defaults to an association to the most commonly used method, which is referenced by the URN "urn:ogc:def:method:WCS:1.1:2dSimpleGrid". For a GridCRS, this association is limited to a remote definition of a grid definition Method (not encoded in-line) that encodes a variation on the method implied by the CV_RectifiedGrid class in ISO 19123, without the inheritance from CV_Grid. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 65, 1), unicode_default='urn:ogc:def:method:WCS:1.1:2dSimpleGrid')
Namespace.addCategoryObject('elementBinding', GridType.name().localName(), GridType)

GridOrigin = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GridOrigin'), pyxb.bundles.opengis.gml.doubleList, documentation='Coordinates of the grid origin position in the GridBaseCRS of this GridCRS. This origin defaults be the most commonly used origin in a GridCRS used in the output part of a GetCapabilities operation request, namely "0 0". This element is adapted from gml:pos. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 72, 1), unicode_default='0 0')
Namespace.addCategoryObject('elementBinding', GridOrigin.name().localName(), GridOrigin)

GridOffsets = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GridOffsets'), pyxb.bundles.opengis.gml.doubleList, documentation='Two or more grid position offsets from the grid origin in the GridBaseCRS of this GridCRS. Example: For the grid2dIn2dCRS OperationMethod, this Offsets element shall contain four values, the first two values shall specify the grid offset for the first grid axis in the 2D base CRS, and the second pair of values shall specify the grid offset for the second grid axis. In this case, the middle two values are zero for un-rotated and un-skewed grids. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 79, 1))
Namespace.addCategoryObject('elementBinding', GridOffsets.name().localName(), GridOffsets)

GridCS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GridCS'), pyxb.binding.datatypes.anyURI, documentation='Association to the (Cartesian) grid coordinate system used by this Grid CRS. In this use of a (Cartesian) grid coordinate system, the grid positions shall be in the centers of the image or other grid coverage values (not between the grid values), as specified in ISO 19123. Also, the grid point indices at the origin shall be 0, 0 (not 1,1), as specified in ISO 19123. This GridCS defaults to the most commonly used grid coordinate system, which is referenced by the URN "urn:ogc:def:cs:OGC:0.0:Grid2dSquareCS". For a GridCRS, this association is limited to a remote definition of the GridCS (not encoded in-line). ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 85, 1), unicode_default='urn:ogc:def:cs:OGC:0.0:Grid2dSquareCS')
Namespace.addCategoryObject('elementBinding', GridCS.name().localName(), GridCS)

Identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), IdentifierType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 44, 1))
Namespace.addCategoryObject('elementBinding', Identifier.name().localName(), Identifier)

Contents = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contents'), CTD_ANON, documentation='Contents section of WCS service metadata (or Capabilities) XML document. For the WCS, these contents are brief metadata about the coverages available from this server, or a reference to another source from which this metadata is available. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 25, 1))
Namespace.addCategoryObject('elementBinding', Contents.name().localName(), Contents)

CoverageSummary = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CoverageSummary'), CoverageSummaryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 55, 1))
Namespace.addCategoryObject('elementBinding', CoverageSummary.name().localName(), CoverageSummary)

Coverages = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Coverages'), CoveragesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCoverages.xsd', 24, 1))
Namespace.addCategoryObject('elementBinding', Coverages.name().localName(), Coverages)

CoverageDescriptions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CoverageDescriptions'), CTD_ANON_, documentation='Response from a WCS DescribeCoverage operation, containing one or more coverage descriptions. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 51, 1))
Namespace.addCategoryObject('elementBinding', CoverageDescriptions.name().localName(), CoverageDescriptions)

TemporalDomain = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemporalDomain'), TimeSequenceType, documentation='Definition of the temporal domain of a coverage, the times for which valid data are available. The times should to be ordered from the oldest to the newest. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 164, 1))
Namespace.addCategoryObject('elementBinding', TemporalDomain.name().localName(), TemporalDomain)

AvailableKeys = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AvailableKeys'), CTD_ANON_2, documentation='List of all the available (valid) key values for this axis. For numeric keys, signed values should be ordered from negative infinity to positive infinity. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 261, 1))
Namespace.addCategoryObject('elementBinding', AvailableKeys.name().localName(), AvailableKeys)

GetCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetCapabilities'), CTD_ANON_3, documentation='Request to a WCS server to perform the GetCapabilities operation. This operation allows a client to retrieve a Capabilities XML document providing metadata for the specific WCS server. In this XML encoding, no "request" parameter is included, since the element name specifies the specific operation. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCapabilities.xsd', 25, 1))
Namespace.addCategoryObject('elementBinding', GetCapabilities.name().localName(), GetCapabilities)

Capabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Capabilities'), CTD_ANON_4, documentation='XML encoded WCS GetCapabilities operation response. The Capabilities document provides clients with service metadata about a specific service instance, including metadata about the coverages served. If the server does not implement the updateSequence parameter, the server shall always return the Capabilities document, without the updateSequence parameter. When the server implements the updateSequence parameter and the GetCapabilities operation request included the updateSequence parameter with the current value, the server shall return this element with only the "version" and "updateSequence" attributes. Otherwise, all optional sections shall be included or not depending on the actual value of the Contents parameter in the GetCapabilities operation request. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCapabilities.xsd', 39, 1))
Namespace.addCategoryObject('elementBinding', Capabilities.name().localName(), Capabilities)

TemporalSubset = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemporalSubset'), TimeSequenceType, documentation='Definition of subset of coverage temporal domain. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 96, 1))
Namespace.addCategoryObject('elementBinding', TemporalSubset.name().localName(), TemporalSubset)

AxisSubset = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AxisSubset'), CTD_ANON_6, documentation='List of selected Keys for this axis, to be used for selecting values in a vector range field. TBD. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 136, 1))
Namespace.addCategoryObject('elementBinding', AxisSubset.name().localName(), AxisSubset)

GridCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GridCRS'), GridCrsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 28, 1))
Namespace.addCategoryObject('elementBinding', GridCRS.name().localName(), GridCRS)

InterpolationMethods = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InterpolationMethods'), CTD_ANON_7, documentation='List of the interpolation method(s) that may be used when continuous grid coverage resampling is needed. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 24, 1))
Namespace.addCategoryObject('elementBinding', InterpolationMethods.name().localName(), InterpolationMethods)

DescribeCoverage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescribeCoverage'), CTD_ANON_8, documentation='Request to a WCS to perform the DescribeCoverage operation. This operation allows a client to retrieve descriptions of one or more coverages. In this XML encoding, no "request" parameter is included, since the element name specifies the specific operation. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 32, 1))
Namespace.addCategoryObject('elementBinding', DescribeCoverage.name().localName(), DescribeCoverage)

GetCoverage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetCoverage'), CTD_ANON_9, documentation='Request to a WCS to perform the GetCoverage operation. This operation allows a client to retrieve a subset of one coverage. In this XML encoding, no "request" parameter is included, since the element name specifies the specific operation. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 27, 1))
Namespace.addCategoryObject('elementBinding', GetCoverage.name().localName(), GetCoverage)



TimeSequenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'timePosition'), pyxb.bundles.opengis.gml.TimePositionType, scope=TimeSequenceType, documentation='Direct representation of a temporal position', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/temporal.xsd', 262, 1)))

TimeSequenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimePeriod'), TimePeriodType, scope=TimeSequenceType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 61, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TimeSequenceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'timePosition')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 60, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TimeSequenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimePeriod')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 61, 3))
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
TimeSequenceType._Automaton = _BuildAutomaton()




TimePeriodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BeginPosition'), pyxb.bundles.opengis.gml.TimePositionType, scope=TimePeriodType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 71, 3)))

TimePeriodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndPosition'), pyxb.bundles.opengis.gml.TimePositionType, scope=TimePeriodType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 72, 3)))

TimePeriodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeResolution'), TimeDurationType, scope=TimePeriodType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 73, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 73, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TimePeriodType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BeginPosition')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 71, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TimePeriodType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndPosition')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 72, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TimePeriodType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimeResolution')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 73, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TimePeriodType._Automaton = _BuildAutomaton_()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SupportedCRS'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON, documentation='Unordered list of references to GridBaseCRSs in which GetCoverage operation requests and responses may be expressed. This list of SupportedCRSs shall be the union of all of the supported CRSs in all of the nested CoverageSummaries. Servers should include this list since it reduces the work clients need to do to determine that they can interoperate with the server. There may be a dependency of SupportedCRS on SupportedFormat, as described in Subclause 10.3.5. The full list of GridBaseCRSs supported by a coverage shall be the union of the CoverageSummary\u2019s own SupportedCRSs and those supported by all its ancestor CoverageSummaries. This full list shall be an exact copy of the equivalent parameters in the CoverageDescription, and shall include zero or more SupportedCRS elements. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 36, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SupportedFormat'), pyxb.bundles.opengis.ows_1_1.MimeType, scope=CTD_ANON, documentation='Unordered list of identifiers of formats in which GetCoverage operation response may be encoded. This list of SupportedFormats shall be the union of all of the supported formats in all of the nested CoverageSummaries. Servers should include this list since it reduces the work clients need to do to determine that they can interoperate with the server. There may be a dependency of SupportedCRS on SupportedFormat, as described in clause 10.3.5. The full list of formats supported by a coverage shall be the union of the CoverageSummary\u2019s own SupportedFormats and those supported by all its ancestor CoverageSummaries. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 41, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OtherSource'), pyxb.bundles.opengis.ows_1_1.OnlineResourceType, scope=CTD_ANON, documentation='Unordered list of references to other sources of coverage metadata. This list shall be included unless one or more CoverageSummaries are included. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 46, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CoverageSummary'), CoverageSummaryType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 55, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 31, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 36, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 41, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 46, 4))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CoverageSummary')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 31, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SupportedCRS')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 36, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SupportedFormat')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 41, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OtherSource')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 46, 4))
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
CTD_ANON._Automaton = _BuildAutomaton_2()




CoverageSummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata'), pyxb.bundles.opengis.ows_1_1.MetadataType, scope=CoverageSummaryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 42, 1)))

CoverageSummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'WGS84BoundingBox'), pyxb.bundles.opengis.ows_1_1.WGS84BoundingBoxType, scope=CoverageSummaryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 113, 1)))

CoverageSummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), IdentifierType, scope=CoverageSummaryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 44, 1)))

CoverageSummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CoverageSummary'), CoverageSummaryType, scope=CoverageSummaryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 55, 1)))

CoverageSummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SupportedCRS'), pyxb.binding.datatypes.anyURI, scope=CoverageSummaryType, documentation='Unordered list of references to CRSs that may be referenced as a GridBaseCRS of a GridCRS in the Output part of a GetCoverage request. These CRSs shall also apply to all lower-level CoverageSummaries under this CoverageSummary, in addition to any other CRSs referenced. When included in a CoverageSummary with an Identifier, this list, including all values inherited from ancestor coverages, shall be an exact copy of the list of SupportedCRS parameters in the corresponding CoverageDescription. Each CoverageSummary shall list or inherit at least one SupportedCRS. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 74, 5)))

CoverageSummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SupportedFormat'), pyxb.bundles.opengis.ows_1_1.MimeType, scope=CoverageSummaryType, documentation='Unordered list of identifiers of formats in which GetCoverage operation responses may be encoded. These formats shall also apply to all lower-level CoverageSummaries under this CoverageSummary, in addition to any other formats identified. When included in a CoverageSummary with an Identifier, this list, including all values inherited from ancestor coverages, shall be an exact copy of the list of SupportedFormat parameters in the corresponding CoverageDescription. Each CoverageSummary shall list or inherit at least one SupportedFormat. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 79, 5)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 64, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 69, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 74, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 79, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 94, 7))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoverageSummaryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoverageSummaryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoverageSummaryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Keywords')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoverageSummaryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 64, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoverageSummaryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'WGS84BoundingBox')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 69, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoverageSummaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SupportedCRS')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 74, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoverageSummaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SupportedFormat')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 79, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CoverageSummaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CoverageSummary')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 89, 7))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CoverageSummaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 94, 7))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CoverageSummaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 100, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
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
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CoverageSummaryType._Automaton = _BuildAutomaton_3()




CoveragesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Coverage'), pyxb.bundles.opengis.ows_1_1.ReferenceGroupType, scope=CoveragesType, documentation='Complete data for one coverage, referencing each coverage file either remotely or locally in the same message. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCoverages.xsd', 35, 1)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CoveragesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Coverage')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCoverages.xsd', 31, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CoveragesType._Automaton = _BuildAutomaton_4()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CoverageDescription'), CoverageDescriptionType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 57, 4)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CoverageDescription')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 57, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_5()




CoverageDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata'), pyxb.bundles.opengis.ows_1_1.MetadataType, scope=CoverageDescriptionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 42, 1)))

CoverageDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), IdentifierType, scope=CoverageDescriptionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 44, 1)))

CoverageDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Domain'), CoverageDomainType, scope=CoverageDescriptionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 79, 5)))

CoverageDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Range'), RangeType, scope=CoverageDescriptionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 80, 5)))

CoverageDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SupportedCRS'), pyxb.binding.datatypes.anyURI, scope=CoverageDescriptionType, documentation='Unordered list of references to all the coordinate reference systems that may be referenced as the GridBaseCRS of a GridCRS specified in the Output part of a GetCoverage operation request. The GridBaseCRS of the GridCRS of a georectified offered coverage shall be listed as a SupportedCRS. An ImageCRS for an unrectified offered image shall be listed as a SupportedCRS, so that it may be referenced as the GridBaseCRS of a GridCRS. This ImageCRS shall be the ImageCRS of that unrectified offered image, or the ImageCRS that is referenced as the GridBaseCRS of the GridCRS that is used by that unrectified offered image  In addition, the GetCoverage operation output may be expressed in the ImageCRS or GridCRS of an unrectified offered coverage, instead of in a specified GridCRS. These Supported\xacCRSs can also be referenced in the BoundingBox in the DomainSubset part of a GetCoverage request. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 81, 5)))

CoverageDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SupportedFormat'), pyxb.bundles.opengis.ows_1_1.MimeType, scope=CoverageDescriptionType, documentation='Unordered list of identifiers of all the formats in which GetCoverage operation responses can be encoded for this coverage. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 86, 5)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 74, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 81, 5))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoverageDescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoverageDescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoverageDescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Keywords')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoverageDescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 69, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoverageDescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 74, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoverageDescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Domain')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 79, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoverageDescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Range')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 80, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoverageDescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SupportedCRS')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 81, 5))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CoverageDescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SupportedFormat')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 86, 5))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CoverageDescriptionType._Automaton = _BuildAutomaton_6()




CoverageDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SpatialDomain'), SpatialDomainType, scope=CoverageDomainType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 103, 3)))

CoverageDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemporalDomain'), TimeSequenceType, scope=CoverageDomainType, documentation='Definition of the temporal domain of a coverage, the times for which valid data are available. The times should to be ordered from the oldest to the newest. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 164, 1)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 104, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CoverageDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SpatialDomain')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 103, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CoverageDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemporalDomain')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 104, 3))
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
CoverageDomainType._Automaton = _BuildAutomaton_7()




SpatialDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, '_CoordinateOperation'), pyxb.bundles.opengis.gml.AbstractCoordinateOperationType, abstract=pyxb.binding.datatypes.boolean(1), scope=SpatialDomainType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/coordinateOperations.xsd', 24, 1)))

SpatialDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'Polygon'), pyxb.bundles.opengis.gml.PolygonType, scope=SpatialDomainType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/geometryBasic2d.xsd', 72, 1)))

SpatialDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'BoundingBox'), pyxb.bundles.opengis.ows_1_1.BoundingBoxType, scope=SpatialDomainType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 70, 1)))

SpatialDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ImageCRS'), ImageCRSRefType, scope=SpatialDomainType, documentation='Association to ImageCRS of an unrectified offered coverage. The ImageCRS shall be referenced in the SpatialDomain when the offered coverage does not have a known GridCRS. Such a coverage is always unrectified, but an unrectified coverage may have a GridCRS instead of an ImageCRS. This ImageCRS applies to this offered coverage, but does not (normally) specify its spatial resolution. The ImageCRS and the GridCRS shall be mutually exclusive in this SpatialDomain. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 135, 3)))

SpatialDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GridCRS'), GridCrsType, scope=SpatialDomainType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 28, 1)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 124, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 129, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 135, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 140, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SpatialDomainType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'BoundingBox')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 117, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SpatialDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GridCRS')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 124, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SpatialDomainType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, '_CoordinateOperation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 129, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SpatialDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ImageCRS')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 135, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SpatialDomainType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'Polygon')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 140, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
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
SpatialDomainType._Automaton = _BuildAutomaton_8()




ImageCRSRefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'ImageCRS'), pyxb.bundles.opengis.gml.ImageCRSType, scope=ImageCRSRefType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/coordinateReferenceSystems.xsd', 347, 1)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 159, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ImageCRSRefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'ImageCRS')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 159, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ImageCRSRefType._Automaton = _BuildAutomaton_9()




RangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Field'), FieldType, scope=RangeType, documentation='Unordered list of the Fields in the Range of a coverage. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 177, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Field')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 177, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RangeType._Automaton = _BuildAutomaton_10()




FieldType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), IdentifierType, scope=FieldType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 44, 1)))

FieldType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Definition'), pyxb.bundles.opengis.ows_1_1.UnNamedDomainType, scope=FieldType, documentation='Further definition of this field, including meaning, units, etc. In this Definition, the AllowedValues should be used to encode the extent of possible values for this field, excluding the Null Value. If the range is not known, AnyValue should be used. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 197, 5)))

FieldType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NullValue'), pyxb.bundles.opengis.ows_1_1.CodeType, scope=FieldType, documentation='Unordered list of the values used when valid Field values are not available for whatever reason. The coverage encoding itself may specify a fixed value for null (e.g. \u201c\u201399999\u201d or \u201cN/A\u201d), but often the choice is up to the provider and must be communicated to the client outside the coverage itself. Each null value shall be encoded as a string. The optional codeSpace attribute can reference a definition of the reason why this value is null. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 202, 5)))

FieldType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Axis'), AxisType, scope=FieldType, documentation='Unordered list of the axes in a vector field for which there are Field values. This list shall be included when this Field has a vector of values. Notice that the axes can be listed here in any order; however, the axis order listed here shall be used in the KVP encoding of a GetCoverage operation request. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 212, 5)))

FieldType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InterpolationMethods'), CTD_ANON_7, scope=FieldType, documentation='List of the interpolation method(s) that may be used when continuous grid coverage resampling is needed. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 24, 1)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 202, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 212, 5))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FieldType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FieldType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FieldType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Keywords')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FieldType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 192, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FieldType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Definition')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 197, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FieldType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NullValue')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 202, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FieldType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InterpolationMethods')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 207, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(FieldType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Axis')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 212, 5))
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
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FieldType._Automaton = _BuildAutomaton_11()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Key'), IdentifierType, scope=CTD_ANON_2, documentation='Valid key value for this axis. There will normally be more than one key value for an axis, but one is allowed for special circumstances. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 267, 4)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Key')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 267, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_12()




def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 49, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 54, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 59, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'AcceptVersions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 49, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Sections')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 54, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'AcceptFormats')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 59, 3))
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
CTD_ANON_3._Automaton = _BuildAutomaton_13()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contents'), CTD_ANON, scope=CTD_ANON_4, documentation='Contents section of WCS service metadata (or Capabilities) XML document. For the WCS, these contents are brief metadata about the coverages available from this server, or a reference to another source from which this metadata is available. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsContents.xsd', 25, 1)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 30, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 31, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 32, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCapabilities.xsd', 47, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'ServiceIdentification')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 30, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'ServiceProvider')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'OperationsMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 32, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contents')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCapabilities.xsd', 47, 6))
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
CTD_ANON_4._Automaton = _BuildAutomaton_14()




OutputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GridCRS'), GridCrsType, scope=OutputType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 28, 1)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 58, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OutputType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GridCRS')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 58, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
OutputType._Automaton = _BuildAutomaton_15()




DomainSubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'BoundingBox'), pyxb.bundles.opengis.ows_1_1.BoundingBoxType, scope=DomainSubsetType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 70, 1)))

DomainSubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemporalSubset'), TimeSequenceType, scope=DomainSubsetType, documentation='Definition of subset of coverage temporal domain. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 96, 1)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 88, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DomainSubsetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'BoundingBox')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 83, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DomainSubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemporalSubset')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 88, 3))
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
DomainSubsetType._Automaton = _BuildAutomaton_16()




RangeSubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FieldSubset'), CTD_ANON_5, scope=RangeSubsetType, documentation='Unordered list of one or more desired subsets of range fields. TBD. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 109, 3)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RangeSubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FieldSubset')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 109, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RangeSubsetType._Automaton = _BuildAutomaton_17()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier'), pyxb.bundles.opengis.ows_1_1.CodeType, scope=CTD_ANON_5, documentation='Unique identifier or name of this dataset. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 87, 1)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InterpolationType'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, documentation='Optional identifier of the spatial interpolation type to be applied to this range field. This interpolation type shall be one that is identified for this Field in the CoverageDescription. When this parameter is omitted, the interpolation method used shall be the default method specified for this Field, if any. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 120, 6)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AxisSubset'), CTD_ANON_6, scope=CTD_ANON_5, documentation='List of selected Keys for this axis, to be used for selecting values in a vector range field. TBD. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 136, 1)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 120, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 125, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 115, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InterpolationType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 120, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AxisSubset')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 125, 6))
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
CTD_ANON_5._Automaton = _BuildAutomaton_18()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), IdentifierType, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 44, 1)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Key'), IdentifierType, scope=CTD_ANON_6, documentation='Unordered list of (at least one) Key, to be used for selecting values in a range vector field. The Keys within this list shall be unique. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 147, 4)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 142, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Key')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 147, 4))
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
CTD_ANON_6._Automaton = _BuildAutomaton_19()




GridCrsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'srsName'), pyxb.bundles.opengis.gml.CodeType, scope=GridCrsType, documentation='The name by which this reference system is identified.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/referenceSystems.xsd', 40, 1)))

GridCrsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GridBaseCRS'), pyxb.binding.datatypes.anyURI, scope=GridCrsType, documentation='Association to the coordinate reference system (CRS) in which this Grid CRS is specified. A GridCRS can use any type of GridBaseCRS, including GeographicCRS, ProjectedCRS, ImageCRS, or a different GridCRS. For a GridCRS, this association is limited to a remote definition of the GridBaseCRS (not encoded in-line). ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 58, 1)))

GridCrsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GridType'), pyxb.binding.datatypes.anyURI, scope=GridCrsType, documentation='Association to the OperationMethod used to define this Grid CRS. This association defaults to an association to the most commonly used method, which is referenced by the URN "urn:ogc:def:method:WCS:1.1:2dSimpleGrid". For a GridCRS, this association is limited to a remote definition of a grid definition Method (not encoded in-line) that encodes a variation on the method implied by the CV_RectifiedGrid class in ISO 19123, without the inheritance from CV_Grid. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 65, 1), unicode_default='urn:ogc:def:method:WCS:1.1:2dSimpleGrid'))

GridCrsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GridOrigin'), pyxb.bundles.opengis.gml.doubleList, scope=GridCrsType, documentation='Coordinates of the grid origin position in the GridBaseCRS of this GridCRS. This origin defaults be the most commonly used origin in a GridCRS used in the output part of a GetCapabilities operation request, namely "0 0". This element is adapted from gml:pos. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 72, 1), unicode_default='0 0'))

GridCrsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GridOffsets'), pyxb.bundles.opengis.gml.doubleList, scope=GridCrsType, documentation='Two or more grid position offsets from the grid origin in the GridBaseCRS of this GridCRS. Example: For the grid2dIn2dCRS OperationMethod, this Offsets element shall contain four values, the first two values shall specify the grid offset for the first grid axis in the 2D base CRS, and the second pair of values shall specify the grid offset for the second grid axis. In this case, the middle two values are zero for un-rotated and un-skewed grids. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 79, 1)))

GridCrsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GridCS'), pyxb.binding.datatypes.anyURI, scope=GridCrsType, documentation='Association to the (Cartesian) grid coordinate system used by this Grid CRS. In this use of a (Cartesian) grid coordinate system, the grid positions shall be in the centers of the image or other grid coverage values (not between the grid values), as specified in ISO 19123. Also, the grid point indices at the origin shall be 0, 0 (not 1,1), as specified in ISO 19123. This GridCS defaults to the most commonly used grid coordinate system, which is referenced by the URN "urn:ogc:def:cs:OGC:0.0:Grid2dSquareCS". For a GridCRS, this association is limited to a remote definition of the GridCS (not encoded in-line). ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 85, 1), unicode_default='urn:ogc:def:cs:OGC:0.0:Grid2dSquareCS'))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 36, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 38, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 43, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 49, 3))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GridCrsType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'srsName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 36, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GridCrsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GridBaseCRS')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 37, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GridCrsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GridType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 38, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GridCrsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GridOrigin')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 43, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GridCrsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GridOffsets')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 48, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(GridCrsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GridCS')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGridCRS.xsd', 49, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GridCrsType._Automaton = _BuildAutomaton_20()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InterpolationMethod'), InterpolationMethodType, scope=CTD_ANON_7, documentation='Unordered list of identifiers of all other supported spatial interpolation methods. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 30, 4)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Default'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, documentation='Identifier of interpolation method that will be used if the client does not specify one. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 35, 4)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 30, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InterpolationMethod')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 30, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Default')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsInterpolationMethod.xsd', 35, 4))
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
CTD_ANON_7._Automaton = _BuildAutomaton_21()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), IdentifierType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsCommon.xsd', 44, 1)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 40, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_22()




AxisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata'), pyxb.bundles.opengis.ows_1_1.MetadataType, scope=AxisType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 42, 1)))

AxisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Meaning'), pyxb.bundles.opengis.ows_1_1.DomainMetadataType, scope=AxisType, documentation='Definition of the meaning or semantics of this set of values. This Meaning can provide more specific, complete, precise, machine accessible, and machine understandable semantics about this quantity, relative to other available semantic information. For example, other semantic information is often provided in "documentation" elements in XML Schemas or "description" elements in GML objects. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDomainType.xsd', 256, 1)))

AxisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'DataType'), pyxb.bundles.opengis.ows_1_1.DomainMetadataType, scope=AxisType, documentation='Definition of the data type of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known data type. For example, such a URN could be a data type identification URN defined in the "ogc" URN namespace. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDomainType.xsd', 262, 1)))

AxisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'ReferenceSystem'), pyxb.bundles.opengis.ows_1_1.DomainMetadataType, scope=AxisType, documentation='Definition of the reference system used by this set of values, including the unit of measure whenever applicable (as is normal). In this case, the xlink:href attribute can reference a URN for a well-known reference system, such as for a coordinate reference system (CRS). For example, such a URN could be a CRS identification URN defined in the "ogc" URN namespace. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDomainType.xsd', 268, 1)))

AxisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'UOM'), pyxb.bundles.opengis.ows_1_1.DomainMetadataType, scope=AxisType, documentation='Definition of the unit of measure of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known unit of measure (uom). For example, such a URN could be a UOM identification URN defined in the "ogc" URN namespace. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDomainType.xsd', 274, 1)))

AxisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AvailableKeys'), CTD_ANON_2, scope=AxisType, documentation='List of all the available (valid) key values for this axis. For numeric keys, signed values should be ordered from negative infinity to positive infinity. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 261, 1)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 231, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 236, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 241, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 246, 5))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Keywords')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AxisType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AvailableKeys')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 230, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Meaning')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 231, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'DataType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 236, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'UOM')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDomainType.xsd', 122, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'ReferenceSystem')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDomainType.xsd', 127, 4))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AxisType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsDescribeCoverage.xsd', 246, 5))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AxisType._Automaton = _BuildAutomaton_23()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier'), pyxb.bundles.opengis.ows_1_1.CodeType, scope=CTD_ANON_9, documentation='Unique identifier or name of this dataset. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsDataIdentification.xsd', 87, 1)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DomainSubset'), DomainSubsetType, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 40, 6)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RangeSubset'), RangeSubsetType, scope=CTD_ANON_9, documentation="Optional selection of a subset of the coverage's range. ", location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 41, 6)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Output'), OutputType, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 46, 6)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 41, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 35, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DomainSubset')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 40, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RangeSubset')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 41, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Output')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wcs/1.1/wcsGetCoverage.xsd', 46, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_24()


Coverage._setSubstitutionGroup(pyxb.bundles.opengis.ows_1_1.ReferenceGroup)

Transformation._setSubstitutionGroup(pyxb.bundles.opengis.gml.CoordinateOperation)
