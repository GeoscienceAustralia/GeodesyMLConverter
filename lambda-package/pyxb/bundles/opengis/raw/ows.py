# ./pyxb/bundles/opengis/raw/ows.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:0eaa86ae32cb3080e2342e92c025f322bb8eca15
# Generated 2017-07-10 00:36:48.505372 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/ows

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:dbb77a06-6507-11e7-b1fd-0a55f9edafa5')

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

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/ows', create_if_missing=True)
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


# Atomic simple type: {http://www.opengis.net/ows}MimeType
class MimeType (pyxb.binding.datatypes.string):

    """XML encoded identifier of a standard MIME type, possibly a parameterized MIME type. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MimeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 24, 1)
    _Documentation = 'XML encoded identifier of a standard MIME type, possibly a parameterized MIME type. '
MimeType._CF_pattern = pyxb.binding.facets.CF_pattern()
MimeType._CF_pattern.addPattern(pattern='(application|audio|image|text|video|message|multipart|model)/.+(;\\s*.+=.+)*')
MimeType._InitializeFacetMap(MimeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'MimeType', MimeType)
_module_typeBindings.MimeType = MimeType

# Atomic simple type: {http://www.opengis.net/ows}VersionType
class VersionType (pyxb.binding.datatypes.string):

    """Specification version for OWS operation. The string value shall contain one x.y.z "version" value (e.g., "2.1.3"). A version number shall contain three non-negative integers separated by decimal points, in the form "x.y.z". The integers y and z shall not exceed 99. Each version shall be for the Implementation Specification (document) and the associated XML Schemas to which requested operations will conform. An Implementation Specification version normally specifies XML Schemas against which an XML encoded operation response must conform and should be validated. See Version negotiation subclause for more information. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VersionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 33, 1)
    _Documentation = 'Specification version for OWS operation. The string value shall contain one x.y.z "version" value (e.g., "2.1.3"). A version number shall contain three non-negative integers separated by decimal points, in the form "x.y.z". The integers y and z shall not exceed 99. Each version shall be for the Implementation Specification (document) and the associated XML Schemas to which requested operations will conform. An Implementation Specification version normally specifies XML Schemas against which an XML encoded operation response must conform and should be validated. See Version negotiation subclause for more information. '
VersionType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'VersionType', VersionType)
_module_typeBindings.VersionType = VersionType

# List simple type: {http://www.opengis.net/ows}PositionType
# superclasses pyxb.binding.datatypes.anySimpleType
class PositionType (pyxb.binding.basis.STD_list):

    """Position instances hold the coordinates of a position in a coordinate reference system (CRS) referenced by the related "crs" attribute or elsewhere. For an angular coordinate axis that is physically continuous for multiple revolutions, but whose recorded values can be discontinuous, special conditions apply when the bounding box is continuous across the value discontinuity:
a)  If the bounding box is continuous clear around this angular axis, then ordinate values of minus and plus infinity shall be used.
b)  If the bounding box is continuous across the value discontinuity but is not continuous clear around this angular axis, then some non-normal value can be used if specified for a specific OWS use of the BoundingBoxType. For more information, see Subclauses 10.2.5 and C.13. This type is adapted from DirectPositionType and doubleList of GML 3.1. The adaptations include omission of all the attributes, since the needed information is included in the BoundingBoxType. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PositionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 101, 1)
    _Documentation = 'Position instances hold the coordinates of a position in a coordinate reference system (CRS) referenced by the related "crs" attribute or elsewhere. For an angular coordinate axis that is physically continuous for multiple revolutions, but whose recorded values can be discontinuous, special conditions apply when the bounding box is continuous across the value discontinuity:\na)  If the bounding box is continuous clear around this angular axis, then ordinate values of minus and plus infinity shall be used.\nb)  If the bounding box is continuous across the value discontinuity but is not continuous clear around this angular axis, then some non-normal value can be used if specified for a specific OWS use of the BoundingBoxType. For more information, see Subclauses 10.2.5 and C.13. This type is adapted from DirectPositionType and doubleList of GML 3.1. The adaptations include omission of all the attributes, since the needed information is included in the BoundingBoxType. '

    _ItemType = pyxb.binding.datatypes.double
PositionType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PositionType', PositionType)
_module_typeBindings.PositionType = PositionType

# Atomic simple type: {http://www.opengis.net/ows}ServiceType
class ServiceType (pyxb.binding.datatypes.string):

    """Service type identifier, where the string value is the OWS type abbreviation, such as "WMS" or "WFS". """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ServiceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 69, 1)
    _Documentation = 'Service type identifier, where the string value is the OWS type abbreviation, such as "WMS" or "WFS". '
ServiceType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ServiceType', ServiceType)
_module_typeBindings.ServiceType = ServiceType

# Atomic simple type: {http://www.opengis.net/ows}UpdateSequenceType
class UpdateSequenceType (pyxb.binding.datatypes.string):

    """Service metadata document version, having values that are "increased" whenever any change is made in service metadata document. Values are selected by each server, and are always opaque to clients. See updateSequence parameter use subclause for more information. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UpdateSequenceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 94, 1)
    _Documentation = 'Service metadata document version, having values that are "increased" whenever any change is made in service metadata document. Values are selected by each server, and are always opaque to clients. See updateSequence parameter use subclause for more information. '
UpdateSequenceType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'UpdateSequenceType', UpdateSequenceType)
_module_typeBindings.UpdateSequenceType = UpdateSequenceType

# List simple type: {http://www.opengis.net/ows}PositionType2D
# superclasses PositionType
class PositionType2D (pyxb.binding.basis.STD_list):

    """Two-dimensional position instances hold the longitude and latitude coordinates of a position in the 2D WGS 84 coordinate reference system. The longitude value shall be listed first, followed by the latitude value, both in decimal degrees. Latitude values shall range from -90 to +90 degrees, and longitude values shall normally range from -180 to +180 degrees. For the longitude axis, special conditions apply when the bounding box is continuous across the +/- 180 degrees meridian longitude value discontinuity:
a)  If the bounding box is continuous clear around the Earth, then longitude values of minus and plus infinity shall be used.
b)  If the bounding box is continuous across the value discontinuity but is not continuous clear around the Earth, then some non-normal value can be used if specified for a specific OWS use of the WGS84BoundingBoxType. For more information, see Subclauses 10.4.5 and C.13. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PositionType2D')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 146, 1)
    _Documentation = 'Two-dimensional position instances hold the longitude and latitude coordinates of a position in the 2D WGS 84 coordinate reference system. The longitude value shall be listed first, followed by the latitude value, both in decimal degrees. Latitude values shall range from -90 to +90 degrees, and longitude values shall normally range from -180 to +180 degrees. For the longitude axis, special conditions apply when the bounding box is continuous across the +/- 180 degrees meridian longitude value discontinuity:\na)  If the bounding box is continuous clear around the Earth, then longitude values of minus and plus infinity shall be used.\nb)  If the bounding box is continuous across the value discontinuity but is not continuous clear around the Earth, then some non-normal value can be used if specified for a specific OWS use of the WGS84BoundingBoxType. For more information, see Subclauses 10.4.5 and C.13. '

    _ItemType = pyxb.binding.datatypes.double
PositionType2D._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2))
PositionType2D._InitializeFacetMap(PositionType2D._CF_length)
Namespace.addCategoryObject('typeBinding', 'PositionType2D', PositionType2D)
_module_typeBindings.PositionType2D = PositionType2D

# Complex type {http://www.opengis.net/ows}KeywordsType with content type ELEMENT_ONLY
class KeywordsType (pyxb.binding.basis.complexTypeDefinition):
    """Unordered list of one or more commonly used or formalised word(s) or phrase(s) used to describe the subject. When needed, the optional "type" can name the type of the associated list of keywords that shall all have the same type. Also when needed, the codeSpace attribute of that "type" can reference the type name authority and/or thesaurus. For OWS use, the optional thesaurusName element was omitted as being complex information that could be referenced by the codeSpace attribute of the Type element. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'KeywordsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 38, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}Keyword uses Python identifier Keyword
    __Keyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Keyword'), 'Keyword', '__httpwww_opengis_netows_KeywordsType_httpwww_opengis_netowsKeyword', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 44, 3), )

    
    Keyword = property(__Keyword.value, __Keyword.set, None, None)

    
    # Element {http://www.opengis.net/ows}Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Type'), 'Type', '__httpwww_opengis_netows_KeywordsType_httpwww_opengis_netowsType', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 45, 3), )

    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        __Keyword.name() : __Keyword,
        __Type.name() : __Type
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.KeywordsType = KeywordsType
Namespace.addCategoryObject('typeBinding', 'KeywordsType', KeywordsType)


# Complex type {http://www.opengis.net/ows}CodeType with content type SIMPLE
class CodeType (pyxb.binding.basis.complexTypeDefinition):
    """Name or code with an (optional) authority. If the codeSpace attribute is present, its value should reference a dictionary, thesaurus, or authority for the name or code, such as the organisation who assigned the value, or the dictionary from which it is taken. Type copied from basicTypes.xsd of GML 3 with documentation edited, for possible use outside the ServiceIdentification section of a service metadata document. """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 49, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute codeSpace uses Python identifier codeSpace
    __codeSpace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'codeSpace'), 'codeSpace', '__httpwww_opengis_netows_CodeType_codeSpace', pyxb.binding.datatypes.anyURI)
    __codeSpace._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 56, 4)
    __codeSpace._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 56, 4)
    
    codeSpace = property(__codeSpace.value, __codeSpace.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __codeSpace.name() : __codeSpace
    })
_module_typeBindings.CodeType = CodeType
Namespace.addCategoryObject('typeBinding', 'CodeType', CodeType)


# Complex type {http://www.opengis.net/ows}ResponsiblePartyType with content type ELEMENT_ONLY
class ResponsiblePartyType (pyxb.binding.basis.complexTypeDefinition):
    """Identification of, and means of communication with, person responsible for the server. At least one of IndividualName, OrganisationName, or PositionName shall be included. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResponsiblePartyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 68, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}IndividualName uses Python identifier IndividualName
    __IndividualName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IndividualName'), 'IndividualName', '__httpwww_opengis_netows_ResponsiblePartyType_httpwww_opengis_netowsIndividualName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 95, 1), )

    
    IndividualName = property(__IndividualName.value, __IndividualName.set, None, 'Name of the responsible person: surname, given name, title separated by a delimiter. ')

    
    # Element {http://www.opengis.net/ows}OrganisationName uses Python identifier OrganisationName
    __OrganisationName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrganisationName'), 'OrganisationName', '__httpwww_opengis_netows_ResponsiblePartyType_httpwww_opengis_netowsOrganisationName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 101, 1), )

    
    OrganisationName = property(__OrganisationName.value, __OrganisationName.set, None, 'Name of the responsible organization. ')

    
    # Element {http://www.opengis.net/ows}PositionName uses Python identifier PositionName
    __PositionName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PositionName'), 'PositionName', '__httpwww_opengis_netows_ResponsiblePartyType_httpwww_opengis_netowsPositionName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 107, 1), )

    
    PositionName = property(__PositionName.value, __PositionName.set, None, 'Role or position of the responsible person. ')

    
    # Element {http://www.opengis.net/ows}Role uses Python identifier Role
    __Role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Role'), 'Role', '__httpwww_opengis_netows_ResponsiblePartyType_httpwww_opengis_netowsRole', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 113, 1), )

    
    Role = property(__Role.value, __Role.set, None, 'Function performed by the responsible party. Possible values of this Role shall include the values and the meanings listed in Subclause B.5.5 of ISO 19115:2003. ')

    
    # Element {http://www.opengis.net/ows}ContactInfo uses Python identifier ContactInfo
    __ContactInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo'), 'ContactInfo', '__httpwww_opengis_netows_ResponsiblePartyType_httpwww_opengis_netowsContactInfo', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 119, 1), )

    
    ContactInfo = property(__ContactInfo.value, __ContactInfo.set, None, 'Address of the responsible party. ')

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


# Complex type {http://www.opengis.net/ows}ResponsiblePartySubsetType with content type ELEMENT_ONLY
class ResponsiblePartySubsetType (pyxb.binding.basis.complexTypeDefinition):
    """Identification of, and means of communication with, person responsible for the server. For OWS use in the ServiceProvider section of a service metadata document, the optional organizationName element was removed, since this type is always used with the ProviderName element which provides that information. The mandatory "role" element was changed to optional, since no clear use of this information is known in the ServiceProvider section. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResponsiblePartySubsetType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 82, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}IndividualName uses Python identifier IndividualName
    __IndividualName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IndividualName'), 'IndividualName', '__httpwww_opengis_netows_ResponsiblePartySubsetType_httpwww_opengis_netowsIndividualName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 95, 1), )

    
    IndividualName = property(__IndividualName.value, __IndividualName.set, None, 'Name of the responsible person: surname, given name, title separated by a delimiter. ')

    
    # Element {http://www.opengis.net/ows}PositionName uses Python identifier PositionName
    __PositionName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PositionName'), 'PositionName', '__httpwww_opengis_netows_ResponsiblePartySubsetType_httpwww_opengis_netowsPositionName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 107, 1), )

    
    PositionName = property(__PositionName.value, __PositionName.set, None, 'Role or position of the responsible person. ')

    
    # Element {http://www.opengis.net/ows}Role uses Python identifier Role
    __Role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Role'), 'Role', '__httpwww_opengis_netows_ResponsiblePartySubsetType_httpwww_opengis_netowsRole', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 113, 1), )

    
    Role = property(__Role.value, __Role.set, None, 'Function performed by the responsible party. Possible values of this Role shall include the values and the meanings listed in Subclause B.5.5 of ISO 19115:2003. ')

    
    # Element {http://www.opengis.net/ows}ContactInfo uses Python identifier ContactInfo
    __ContactInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo'), 'ContactInfo', '__httpwww_opengis_netows_ResponsiblePartySubsetType_httpwww_opengis_netowsContactInfo', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 119, 1), )

    
    ContactInfo = property(__ContactInfo.value, __ContactInfo.set, None, 'Address of the responsible party. ')

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


# Complex type {http://www.opengis.net/ows}ContactType with content type ELEMENT_ONLY
class ContactType (pyxb.binding.basis.complexTypeDefinition):
    """Information required to enable contact with the responsible person and/or organization. For OWS use in the service metadata document, the optional hoursOfService and contactInstructions elements were retained, as possibly being useful in the ServiceProvider section. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContactType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 125, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}Phone uses Python identifier Phone
    __Phone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Phone'), 'Phone', '__httpwww_opengis_netows_ContactType_httpwww_opengis_netowsPhone', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 131, 3), )

    
    Phone = property(__Phone.value, __Phone.set, None, 'Telephone numbers at which the organization or individual may be contacted. ')

    
    # Element {http://www.opengis.net/ows}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Address'), 'Address', '__httpwww_opengis_netows_ContactType_httpwww_opengis_netowsAddress', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 136, 3), )

    
    Address = property(__Address.value, __Address.set, None, 'Physical and email address at which the organization or individual may be contacted. ')

    
    # Element {http://www.opengis.net/ows}OnlineResource uses Python identifier OnlineResource
    __OnlineResource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OnlineResource'), 'OnlineResource', '__httpwww_opengis_netows_ContactType_httpwww_opengis_netowsOnlineResource', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 141, 3), )

    
    OnlineResource = property(__OnlineResource.value, __OnlineResource.set, None, 'On-line information that can be used to contact the individual or organization. OWS specifics: The xlink:href attribute in the xlink:simpleAttrs attribute group shall be used to reference this resource. Whenever practical, the xlink:href attribute with type anyURI should be a URL from which more contact information can be electronically retrieved. The xlink:title attribute with type "string" can be used to name this set of information. The other attributes in the xlink:simpleAttrs attribute group should not be used. ')

    
    # Element {http://www.opengis.net/ows}HoursOfService uses Python identifier HoursOfService
    __HoursOfService = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HoursOfService'), 'HoursOfService', '__httpwww_opengis_netows_ContactType_httpwww_opengis_netowsHoursOfService', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 146, 3), )

    
    HoursOfService = property(__HoursOfService.value, __HoursOfService.set, None, 'Time period (including time zone) when individuals can contact the organization or individual. ')

    
    # Element {http://www.opengis.net/ows}ContactInstructions uses Python identifier ContactInstructions
    __ContactInstructions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContactInstructions'), 'ContactInstructions', '__httpwww_opengis_netows_ContactType_httpwww_opengis_netowsContactInstructions', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 151, 3), )

    
    ContactInstructions = property(__ContactInstructions.value, __ContactInstructions.set, None, 'Supplemental instructions on how or when to contact the individual or organization. ')

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


# Complex type {http://www.opengis.net/ows}OnlineResourceType with content type EMPTY
class OnlineResourceType (pyxb.binding.basis.complexTypeDefinition):
    """Reference to on-line resource from which data can be obtained. For OWS use in the service metadata document, the CI_OnlineResource class was XML encoded as the attributeGroup "xlink:simpleAttrs", as used in GML. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OnlineResourceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 159, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netows_OnlineResourceType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netows_OnlineResourceType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netows_OnlineResourceType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netows_OnlineResourceType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netows_OnlineResourceType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netows_OnlineResourceType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netows_OnlineResourceType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
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


# Complex type {http://www.opengis.net/ows}TelephoneType with content type ELEMENT_ONLY
class TelephoneType (pyxb.binding.basis.complexTypeDefinition):
    """Telephone numbers for contacting the responsible individual or organization. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TelephoneType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 167, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}Voice uses Python identifier Voice
    __Voice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Voice'), 'Voice', '__httpwww_opengis_netows_TelephoneType_httpwww_opengis_netowsVoice', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 172, 3), )

    
    Voice = property(__Voice.value, __Voice.set, None, 'Telephone number by which individuals can speak to the responsible organization or individual. ')

    
    # Element {http://www.opengis.net/ows}Facsimile uses Python identifier Facsimile
    __Facsimile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Facsimile'), 'Facsimile', '__httpwww_opengis_netows_TelephoneType_httpwww_opengis_netowsFacsimile', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 177, 3), )

    
    Facsimile = property(__Facsimile.value, __Facsimile.set, None, 'Telephone number of a facsimile machine for the responsible\norganization or individual. ')

    _ElementMap.update({
        __Voice.name() : __Voice,
        __Facsimile.name() : __Facsimile
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TelephoneType = TelephoneType
Namespace.addCategoryObject('typeBinding', 'TelephoneType', TelephoneType)


# Complex type {http://www.opengis.net/ows}AddressType with content type ELEMENT_ONLY
class AddressType (pyxb.binding.basis.complexTypeDefinition):
    """Location of the responsible individual or organization. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddressType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 186, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}DeliveryPoint uses Python identifier DeliveryPoint
    __DeliveryPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DeliveryPoint'), 'DeliveryPoint', '__httpwww_opengis_netows_AddressType_httpwww_opengis_netowsDeliveryPoint', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 191, 3), )

    
    DeliveryPoint = property(__DeliveryPoint.value, __DeliveryPoint.set, None, 'Address line for the location. ')

    
    # Element {http://www.opengis.net/ows}City uses Python identifier City
    __City = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'City'), 'City', '__httpwww_opengis_netows_AddressType_httpwww_opengis_netowsCity', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 196, 3), )

    
    City = property(__City.value, __City.set, None, 'City of the location. ')

    
    # Element {http://www.opengis.net/ows}AdministrativeArea uses Python identifier AdministrativeArea
    __AdministrativeArea = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeArea'), 'AdministrativeArea', '__httpwww_opengis_netows_AddressType_httpwww_opengis_netowsAdministrativeArea', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 201, 3), )

    
    AdministrativeArea = property(__AdministrativeArea.value, __AdministrativeArea.set, None, 'State or province of the location. ')

    
    # Element {http://www.opengis.net/ows}PostalCode uses Python identifier PostalCode
    __PostalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), 'PostalCode', '__httpwww_opengis_netows_AddressType_httpwww_opengis_netowsPostalCode', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 206, 3), )

    
    PostalCode = property(__PostalCode.value, __PostalCode.set, None, 'ZIP or other postal code. ')

    
    # Element {http://www.opengis.net/ows}Country uses Python identifier Country
    __Country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Country'), 'Country', '__httpwww_opengis_netows_AddressType_httpwww_opengis_netowsCountry', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 211, 3), )

    
    Country = property(__Country.value, __Country.set, None, 'Country of the physical address. ')

    
    # Element {http://www.opengis.net/ows}ElectronicMailAddress uses Python identifier ElectronicMailAddress
    __ElectronicMailAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ElectronicMailAddress'), 'ElectronicMailAddress', '__httpwww_opengis_netows_AddressType_httpwww_opengis_netowsElectronicMailAddress', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 216, 3), )

    
    ElectronicMailAddress = property(__ElectronicMailAddress.value, __ElectronicMailAddress.set, None, 'Address of the electronic mailbox of the responsible organization or individual. ')

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


# Complex type {http://www.opengis.net/ows}MetadataType with content type ELEMENT_ONLY
class MetadataType (pyxb.binding.basis.complexTypeDefinition):
    """This element either references or contains more metadata about the element that includes this element. To reference metadata stored remotely, at least the xlinks:href attribute in xlink:simpleAttrs shall be included. Either at least one of the attributes in xlink:simpleAttrs or a substitute for the AbstractMetaData element shall be included, but not both. An Implementation Specification can restrict the contents of this element to always be a reference or always contain metadata. (Informative: This element was adapted from the metaDataProperty element in GML 3.0.) """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 42, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}AbstractMetaData uses Python identifier AbstractMetaData
    __AbstractMetaData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AbstractMetaData'), 'AbstractMetaData', '__httpwww_opengis_netows_MetadataType_httpwww_opengis_netowsAbstractMetaData', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 61, 1), )

    
    AbstractMetaData = property(__AbstractMetaData.value, __AbstractMetaData.set, None, 'Abstract element containing more metadata about the element that includes the containing "metadata" element. A specific server implementation, or an Implementation Specification, can define concrete elements in the AbstractMetaData substitution group. ')

    
    # Attribute about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'about'), 'about', '__httpwww_opengis_netows_MetadataType_about', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 54, 2)
    __about._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 54, 2)
    
    about = property(__about.value, __about.set, None, 'Optional reference to the aspect of the element which includes this "metadata" element that this metadata provides more information about. ')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netows_MetadataType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netows_MetadataType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netows_MetadataType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netows_MetadataType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netows_MetadataType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netows_MetadataType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netows_MetadataType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
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


# Complex type {http://www.opengis.net/ows}BoundingBoxType with content type ELEMENT_ONLY
class BoundingBoxType (pyxb.binding.basis.complexTypeDefinition):
    """XML encoded minimum rectangular bounding box (or region) parameter, surrounding all the associated data. This type is adapted from the EnvelopeType of GML 3.1, with modified contents and documentation for encoding a MINIMUM size box SURROUNDING all associated data. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoundingBoxType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 70, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}LowerCorner uses Python identifier LowerCorner
    __LowerCorner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LowerCorner'), 'LowerCorner', '__httpwww_opengis_netows_BoundingBoxType_httpwww_opengis_netowsLowerCorner', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 76, 3), )

    
    LowerCorner = property(__LowerCorner.value, __LowerCorner.set, None, 'Position of the bounding box corner at which the value of each coordinate normally is the algebraic minimum within this bounding box. In some cases, this position is normally displayed at the top, such as the top left for some image coordinates. For more information, see Subclauses 10.2.5 and C.13. ')

    
    # Element {http://www.opengis.net/ows}UpperCorner uses Python identifier UpperCorner
    __UpperCorner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UpperCorner'), 'UpperCorner', '__httpwww_opengis_netows_BoundingBoxType_httpwww_opengis_netowsUpperCorner', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 81, 3), )

    
    UpperCorner = property(__UpperCorner.value, __UpperCorner.set, None, 'Position of the bounding box corner at which the value of each coordinate normally is the algebraic maximum within this bounding box. In some cases, this position is normally displayed at the bottom, such as the bottom right for some image coordinates. For more information, see Subclauses 10.2.5 and C.13. ')

    
    # Attribute crs uses Python identifier crs
    __crs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'crs'), 'crs', '__httpwww_opengis_netows_BoundingBoxType_crs', pyxb.binding.datatypes.anyURI)
    __crs._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 87, 2)
    __crs._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 87, 2)
    
    crs = property(__crs.value, __crs.set, None, 'Usually references the definition of a CRS, as specified in [OGC Topic 2]. Such a CRS definition can be XML encoded using the gml:CoordinateReferenceSystemType in [GML 3.1]. For well known references, it is not required that a CRS definition exist at the location the URI points to. If no anyURI value is included, the applicable CRS must be either:\na)\tSpecified outside the bounding box, but inside a data structure that includes this bounding box, as specified for a specific OWS use of this bounding box type.\nb)\tFixed and specified in the Implementation Specification for a specific OWS use of the bounding box type. ')

    
    # Attribute dimensions uses Python identifier dimensions
    __dimensions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dimensions'), 'dimensions', '__httpwww_opengis_netows_BoundingBoxType_dimensions', pyxb.binding.datatypes.positiveInteger)
    __dimensions._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 94, 2)
    __dimensions._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 94, 2)
    
    dimensions = property(__dimensions.value, __dimensions.set, None, 'The number of dimensions in this CRS (the length of a coordinate sequence in this use of the PositionType). This number is specified by the CRS definition, but can also be specified here. ')

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


# Complex type {http://www.opengis.net/ows}DescriptionType with content type ELEMENT_ONLY
class DescriptionType (pyxb.binding.basis.complexTypeDefinition):
    """Human-readable descriptive information for the object it is included within.
This type shall be extended if needed for specific OWS use to include additional metadata for each type of information. This type shall not be restricted for a specific OWS to change the multiplicity (or optionality) of some elements. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DescriptionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 24, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Title'), 'Title', '__httpwww_opengis_netows_DescriptionType_httpwww_opengis_netowsTitle', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 24, 1), )

    
    Title = property(__Title.value, __Title.set, None, 'Title of this resource, normally used for display to a human. ')

    
    # Element {http://www.opengis.net/ows}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Abstract'), 'Abstract', '__httpwww_opengis_netows_DescriptionType_httpwww_opengis_netowsAbstract', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 30, 1), )

    
    Abstract = property(__Abstract.value, __Abstract.set, None, 'Brief narrative description of this resource, normally used for display to a human. ')

    
    # Element {http://www.opengis.net/ows}Keywords uses Python identifier Keywords
    __Keywords = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Keywords'), 'Keywords', '__httpwww_opengis_netows_DescriptionType_httpwww_opengis_netowsKeywords', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 36, 1), )

    
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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Report message returned to the client that requested any OWS operation when the server detects an error while processing that operation request. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 23, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}Exception uses Python identifier Exception
    __Exception = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Exception'), 'Exception', '__httpwww_opengis_netows_CTD_ANON_httpwww_opengis_netowsException', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 44, 1), )

    
    Exception = property(__Exception.value, __Exception.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netows_CTD_ANON_version', pyxb.binding.datatypes.string, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 31, 3)
    __version._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 31, 3)
    
    version = property(__version.value, __version.set, None, 'Specification version for OWS operation. The string value shall contain one x.y.z "version" value (e.g., "2.1.3"). A version number shall contain three non-negative integers separated by decimal points, in the form "x.y.z". The integers y and z shall not exceed 99. Each version shall be for the Implementation Specification (document) and the associated XML Schemas to which requested operations will conform. An Implementation Specification version normally specifies XML Schemas against which an XML encoded operation response must conform and should be validated. See Version negotiation subclause for more information. ')

    
    # Attribute language uses Python identifier language
    __language = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'language'), 'language', '__httpwww_opengis_netows_CTD_ANON_language', pyxb.binding.datatypes.language)
    __language._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 36, 3)
    __language._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 36, 3)
    
    language = property(__language.value, __language.set, None, 'Identifier of the language used by all included exception text values. These language identifiers shall be as specified in IETF RFC 1766. When this attribute is omitted, the language used is not identified. ')

    _ElementMap.update({
        __Exception.name() : __Exception
    })
    _AttributeMap.update({
        __version.name() : __version,
        __language.name() : __language
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://www.opengis.net/ows}ExceptionType with content type ELEMENT_ONLY
class ExceptionType (pyxb.binding.basis.complexTypeDefinition):
    """An Exception element describes one detected error that a server chooses to convey to the client. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExceptionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 46, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}ExceptionText uses Python identifier ExceptionText
    __ExceptionText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExceptionText'), 'ExceptionText', '__httpwww_opengis_netows_ExceptionType_httpwww_opengis_netowsExceptionText', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 51, 3), )

    
    ExceptionText = property(__ExceptionText.value, __ExceptionText.set, None, 'Ordered sequence of text strings that describe this specific exception or error. The contents of these strings are left open to definition by each server implementation. A server is strongly encouraged to include at least one ExceptionText value, to provide more information about the detected error than provided by the exceptionCode. When included, multiple ExceptionText values shall provide hierarchical information about one detected error, with the most significant information listed first. ')

    
    # Attribute exceptionCode uses Python identifier exceptionCode
    __exceptionCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'exceptionCode'), 'exceptionCode', '__httpwww_opengis_netows_ExceptionType_exceptionCode', pyxb.binding.datatypes.string, required=True)
    __exceptionCode._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 57, 2)
    __exceptionCode._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 57, 2)
    
    exceptionCode = property(__exceptionCode.value, __exceptionCode.set, None, 'A code representing the type of this exception, which shall be selected from a set of exceptionCode values specified for the specific service operation and server. ')

    
    # Attribute locator uses Python identifier locator
    __locator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'locator'), 'locator', '__httpwww_opengis_netows_ExceptionType_locator', pyxb.binding.datatypes.string)
    __locator._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 62, 2)
    __locator._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 62, 2)
    
    locator = property(__locator.value, __locator.set, None, "When included, this locator shall indicate to the client where an exception was encountered in servicing the client's operation request. This locator should be included whenever meaningful information can be provided by the server. The contents of this locator will depend on the specific exceptionCode and OWS service, and shall be specified in the OWS Implementation Specification. ")

    _ElementMap.update({
        __ExceptionText.name() : __ExceptionText
    })
    _AttributeMap.update({
        __exceptionCode.name() : __exceptionCode,
        __locator.name() : __locator
    })
_module_typeBindings.ExceptionType = ExceptionType
Namespace.addCategoryObject('typeBinding', 'ExceptionType', ExceptionType)


# Complex type {http://www.opengis.net/ows}AcceptVersionsType with content type ELEMENT_ONLY
class AcceptVersionsType (pyxb.binding.basis.complexTypeDefinition):
    """Prioritized sequence of one or more specification versions accepted by client, with preferred versions listed first. See Version negotiation subclause for more information. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AcceptVersionsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 76, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Version'), 'Version', '__httpwww_opengis_netows_AcceptVersionsType_httpwww_opengis_netowsVersion', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 81, 3), )

    
    Version = property(__Version.value, __Version.set, None, None)

    _ElementMap.update({
        __Version.name() : __Version
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AcceptVersionsType = AcceptVersionsType
Namespace.addCategoryObject('typeBinding', 'AcceptVersionsType', AcceptVersionsType)


# Complex type {http://www.opengis.net/ows}SectionsType with content type ELEMENT_ONLY
class SectionsType (pyxb.binding.basis.complexTypeDefinition):
    """Unordered list of zero or more names of requested sections in complete service metadata document. Each Section value shall contain an allowed section name as specified by each OWS specification. See Sections parameter subclause for more information.  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SectionsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 85, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}Section uses Python identifier Section
    __Section = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Section'), 'Section', '__httpwww_opengis_netows_SectionsType_httpwww_opengis_netowsSection', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 90, 3), )

    
    Section = property(__Section.value, __Section.set, None, None)

    _ElementMap.update({
        __Section.name() : __Section
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SectionsType = SectionsType
Namespace.addCategoryObject('typeBinding', 'SectionsType', SectionsType)


# Complex type {http://www.opengis.net/ows}AcceptFormatsType with content type ELEMENT_ONLY
class AcceptFormatsType (pyxb.binding.basis.complexTypeDefinition):
    """Prioritized sequence of zero or more GetCapabilities operation response formats desired by client, with preferred formats listed first. Each response format shall be identified by its MIME type. See AcceptFormats parameter use subclause for more information. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AcceptFormatsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 101, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}OutputFormat uses Python identifier OutputFormat
    __OutputFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), 'OutputFormat', '__httpwww_opengis_netows_AcceptFormatsType_httpwww_opengis_netowsOutputFormat', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 106, 3), )

    
    OutputFormat = property(__OutputFormat.value, __OutputFormat.set, None, None)

    _ElementMap.update({
        __OutputFormat.name() : __OutputFormat
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AcceptFormatsType = AcceptFormatsType
Namespace.addCategoryObject('typeBinding', 'AcceptFormatsType', AcceptFormatsType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Metadata about the operations and related abilities specified by this service and implemented by this server, including the URLs for operation requests. The basic contents of this section shall be the same for all OWS types, but individual services can add elements and/or change the optionality of optional elements. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 28, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}Parameter uses Python identifier Parameter
    __Parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Parameter'), 'Parameter', '__httpwww_opengis_netows_CTD_ANON__httpwww_opengis_netowsParameter', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 35, 4), )

    
    Parameter = property(__Parameter.value, __Parameter.set, None, 'Optional unordered list of parameter valid domains that each apply to one or more operations which this server interface implements. The list of required and optional parameter domain limitations shall be specified in the Implementation Specification for this service. ')

    
    # Element {http://www.opengis.net/ows}Constraint uses Python identifier Constraint
    __Constraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), 'Constraint', '__httpwww_opengis_netows_CTD_ANON__httpwww_opengis_netowsConstraint', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 40, 4), )

    
    Constraint = property(__Constraint.value, __Constraint.set, None, 'Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this server. The list of required and optional constraints shall be specified in the Implementation Specification for this service. ')

    
    # Element {http://www.opengis.net/ows}ExtendedCapabilities uses Python identifier ExtendedCapabilities
    __ExtendedCapabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExtendedCapabilities'), 'ExtendedCapabilities', '__httpwww_opengis_netows_CTD_ANON__httpwww_opengis_netowsExtendedCapabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 50, 1), )

    
    ExtendedCapabilities = property(__ExtendedCapabilities.value, __ExtendedCapabilities.set, None, 'Individual software vendors and servers can use this element to provide metadata about any additional server abilities. ')

    
    # Element {http://www.opengis.net/ows}Operation uses Python identifier Operation
    __Operation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Operation'), 'Operation', '__httpwww_opengis_netows_CTD_ANON__httpwww_opengis_netowsOperation', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 56, 1), )

    
    Operation = property(__Operation.value, __Operation.set, None, 'Metadata for one operation that this server implements. ')

    _ElementMap.update({
        __Parameter.name() : __Parameter,
        __Constraint.name() : __Constraint,
        __ExtendedCapabilities.name() : __ExtendedCapabilities,
        __Operation.name() : __Operation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Metadata for one operation that this server implements. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 60, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), 'Metadata', '__httpwww_opengis_netows_CTD_ANON_2_httpwww_opengis_netowsMetadata', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 40, 1), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows}Parameter uses Python identifier Parameter
    __Parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Parameter'), 'Parameter', '__httpwww_opengis_netows_CTD_ANON_2_httpwww_opengis_netowsParameter', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 67, 4), )

    
    Parameter = property(__Parameter.value, __Parameter.set, None, 'Optional unordered list of parameter domains that each apply to this operation which this server implements. If one of these Parameter elements has the same "name" attribute as a Parameter element in the OperationsMetadata element, this Parameter element shall override the other one for this operation. The list of required and optional parameter domain limitations for this operation shall be specified in the Implementation Specification for this service. ')

    
    # Element {http://www.opengis.net/ows}Constraint uses Python identifier Constraint
    __Constraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), 'Constraint', '__httpwww_opengis_netows_CTD_ANON_2_httpwww_opengis_netowsConstraint', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 72, 4), )

    
    Constraint = property(__Constraint.value, __Constraint.set, None, 'Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this operation. If one of these Constraint elements has the same "name" attribute as a Constraint element in the OperationsMetadata element, this Constraint element shall override the other one for this operation. The list of required and optional constraints for this operation shall be specified in the Implementation Specification for this service. ')

    
    # Element {http://www.opengis.net/ows}DCP uses Python identifier DCP
    __DCP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DCP'), 'DCP', '__httpwww_opengis_netows_CTD_ANON_2_httpwww_opengis_netowsDCP', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 91, 1), )

    
    DCP = property(__DCP.value, __DCP.set, None, 'Information for one distributed Computing Platform (DCP) supported for this operation. At present, only the HTTP DCP is defined, so this element only includes the HTTP element.\n')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netows_CTD_ANON_2_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 83, 3)
    __name._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 83, 3)
    
    name = property(__name.value, __name.set, None, 'Name or identifier of this operation (request) (for example, GetCapabilities). The list of required and optional operations implemented shall be specified in the Implementation Specification for this service. ')

    _ElementMap.update({
        __Metadata.name() : __Metadata,
        __Parameter.name() : __Parameter,
        __Constraint.name() : __Constraint,
        __DCP.name() : __DCP
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Information for one distributed Computing Platform (DCP) supported for this operation. At present, only the HTTP DCP is defined, so this element only includes the HTTP element.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 96, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}HTTP uses Python identifier HTTP
    __HTTP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HTTP'), 'HTTP', '__httpwww_opengis_netows_CTD_ANON_3_httpwww_opengis_netowsHTTP', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 103, 1), )

    
    HTTP = property(__HTTP.value, __HTTP.set, None, 'Connect point URLs for the HTTP Distributed Computing Platform (DCP). Normally, only one Get and/or one Post is included in this element. More than one Get and/or Post is allowed to support including alternative URLs for uses such as load balancing or backup. ')

    _ElementMap.update({
        __HTTP.name() : __HTTP
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Connect point URLs for the HTTP Distributed Computing Platform (DCP). Normally, only one Get and/or one Post is included in this element. More than one Get and/or Post is allowed to support including alternative URLs for uses such as load balancing or backup. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 107, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}Get uses Python identifier Get
    __Get = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Get'), 'Get', '__httpwww_opengis_netows_CTD_ANON_4_httpwww_opengis_netowsGet', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 109, 4), )

    
    Get = property(__Get.value, __Get.set, None, 'Connect point URL prefix and any constraints for the HTTP "Get" request method for this operation request. ')

    
    # Element {http://www.opengis.net/ows}Post uses Python identifier Post
    __Post = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Post'), 'Post', '__httpwww_opengis_netows_CTD_ANON_4_httpwww_opengis_netowsPost', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 114, 4), )

    
    Post = property(__Post.value, __Post.set, None, 'Connect point URL and any constraints for the HTTP "Post" request method for this operation request. ')

    _ElementMap.update({
        __Get.name() : __Get,
        __Post.name() : __Post
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type {http://www.opengis.net/ows}DomainType with content type ELEMENT_ONLY
class DomainType (pyxb.binding.basis.complexTypeDefinition):
    """Valid domain (or set of values) of one parameter or other quantity used by this server. A non-parameter quantity may not be explicitly represented in the server software. (Informative: An example is the outputFormat parameter of a WFS. Each WFS server should provide a Parameter element for the outputFormat parameter that lists the supported output formats, such as GML2, GML3, etc. as the allowed "Value" elements.) """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DomainType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 140, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), 'Metadata', '__httpwww_opengis_netows_DomainType_httpwww_opengis_netowsMetadata', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 40, 1), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Value'), 'Value', '__httpwww_opengis_netows_DomainType_httpwww_opengis_netowsValue', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 145, 3), )

    
    Value = property(__Value.value, __Value.set, None, 'Unordered list of all the valid values for this parameter or other quantity. For those parameters that contain a list or sequence of values, these values shall be for individual values in the list. The allowed set of values and the allowed server restrictions on that set of values shall be specified in the Implementation Specification for this service. ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netows_DomainType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 156, 2)
    __name._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 156, 2)
    
    name = property(__name.value, __name.set, None, 'Name or identifier of this parameter or other quantity. ')

    _ElementMap.update({
        __Metadata.name() : __Metadata,
        __Value.name() : __Value
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.DomainType = DomainType
Namespace.addCategoryObject('typeBinding', 'DomainType', DomainType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Metadata about the organization that provides this specific service instance or server. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceProvider.xsd', 27, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}ProviderName uses Python identifier ProviderName
    __ProviderName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProviderName'), 'ProviderName', '__httpwww_opengis_netows_CTD_ANON_5_httpwww_opengis_netowsProviderName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceProvider.xsd', 29, 4), )

    
    ProviderName = property(__ProviderName.value, __ProviderName.set, None, 'A unique identifier for the service provider organization. ')

    
    # Element {http://www.opengis.net/ows}ProviderSite uses Python identifier ProviderSite
    __ProviderSite = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProviderSite'), 'ProviderSite', '__httpwww_opengis_netows_CTD_ANON_5_httpwww_opengis_netowsProviderSite', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceProvider.xsd', 34, 4), )

    
    ProviderSite = property(__ProviderSite.value, __ProviderSite.set, None, 'Reference to the most relevant web site of the service provider. ')

    
    # Element {http://www.opengis.net/ows}ServiceContact uses Python identifier ServiceContact
    __ServiceContact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceContact'), 'ServiceContact', '__httpwww_opengis_netows_CTD_ANON_5_httpwww_opengis_netowsServiceContact', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceProvider.xsd', 39, 4), )

    
    ServiceContact = property(__ServiceContact.value, __ServiceContact.set, None, 'Information for contacting the service provider. The OnlineResource element within this ServiceContact element should not be used to reference a web site of the service provider. ')

    _ElementMap.update({
        __ProviderName.name() : __ProviderName,
        __ProviderSite.name() : __ProviderSite,
        __ServiceContact.name() : __ServiceContact
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type {http://www.opengis.net/ows}WGS84BoundingBoxType with content type ELEMENT_ONLY
class WGS84BoundingBoxType (BoundingBoxType):
    """XML encoded minimum rectangular bounding box (or region) parameter, surrounding all the associated data. This box is specialized for use with the 2D WGS 84 coordinate reference system with decimal values of longitude and latitude. This type is adapted from the general BoundingBoxType, with modified contents and documentation for use with the 2D WGS 84 coordinate reference system. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WGS84BoundingBoxType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 113, 1)
    _ElementMap = BoundingBoxType._ElementMap.copy()
    _AttributeMap = BoundingBoxType._AttributeMap.copy()
    # Base type is BoundingBoxType
    
    # Element LowerCorner ({http://www.opengis.net/ows}LowerCorner) inherited from {http://www.opengis.net/ows}BoundingBoxType
    
    # Element UpperCorner ({http://www.opengis.net/ows}UpperCorner) inherited from {http://www.opengis.net/ows}BoundingBoxType
    
    # Attribute crs is restricted from parent
    
    # Attribute crs uses Python identifier crs
    __crs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'crs'), 'crs', '__httpwww_opengis_netows_BoundingBoxType_crs', pyxb.binding.datatypes.anyURI, fixed=True, unicode_default='urn:ogc:def:crs:OGC:2:84')
    __crs._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 132, 4)
    __crs._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 132, 4)
    
    crs = property(__crs.value, __crs.set, None, 'This attribute can be included when considered useful. When included, this attribute shall reference the 2D WGS 84 coordinate reference system with longitude before latitude and decimal values of longitude and latitude. ')

    
    # Attribute dimensions is restricted from parent
    
    # Attribute dimensions uses Python identifier dimensions
    __dimensions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dimensions'), 'dimensions', '__httpwww_opengis_netows_BoundingBoxType_dimensions', pyxb.binding.datatypes.positiveInteger, fixed=True, unicode_default='2')
    __dimensions._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 137, 4)
    __dimensions._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 137, 4)
    
    dimensions = property(__dimensions.value, __dimensions.set, None, 'The number of dimensions in this CRS (the length of a coordinate sequence in this use of the PositionType). This number is specified by the CRS definition, but can also be specified here. ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __crs.name() : __crs,
        __dimensions.name() : __dimensions
    })
_module_typeBindings.WGS84BoundingBoxType = WGS84BoundingBoxType
Namespace.addCategoryObject('typeBinding', 'WGS84BoundingBoxType', WGS84BoundingBoxType)


# Complex type {http://www.opengis.net/ows}IdentificationType with content type ELEMENT_ONLY
class IdentificationType (DescriptionType):
    """General metadata identifying and describing a set of data. This type shall be extended if needed for each specific OWS to include additional metadata for each type of dataset. If needed, this type should first be restricted for each specific OWS to change the multiplicity (or optionality) of some elements. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IdentificationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 36, 1)
    _ElementMap = DescriptionType._ElementMap.copy()
    _AttributeMap = DescriptionType._AttributeMap.copy()
    # Base type is DescriptionType
    
    # Element Title ({http://www.opengis.net/ows}Title) inherited from {http://www.opengis.net/ows}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows}Abstract) inherited from {http://www.opengis.net/ows}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows}Keywords) inherited from {http://www.opengis.net/ows}DescriptionType
    
    # Element {http://www.opengis.net/ows}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), 'Metadata', '__httpwww_opengis_netows_IdentificationType_httpwww_opengis_netowsMetadata', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 40, 1), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows}BoundingBox uses Python identifier BoundingBox
    __BoundingBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox'), 'BoundingBox', '__httpwww_opengis_netows_IdentificationType_httpwww_opengis_netowsBoundingBox', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 68, 1), )

    
    BoundingBox = property(__BoundingBox.value, __BoundingBox.set, None, None)

    
    # Element {http://www.opengis.net/ows}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), 'Identifier', '__httpwww_opengis_netows_IdentificationType_httpwww_opengis_netowsIdentifier', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 73, 1), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, 'Unique identifier or name of this dataset. ')

    
    # Element {http://www.opengis.net/ows}OutputFormat uses Python identifier OutputFormat
    __OutputFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), 'OutputFormat', '__httpwww_opengis_netows_IdentificationType_httpwww_opengis_netowsOutputFormat', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 79, 1), )

    
    OutputFormat = property(__OutputFormat.value, __OutputFormat.set, None, 'Reference to a format in which this data can be encoded and transferred. More specific parameter names should be used by specific OWS specifications wherever applicable. More than one such parameter can be included for different purposes. ')

    
    # Element {http://www.opengis.net/ows}AvailableCRS uses Python identifier AvailableCRS
    __AvailableCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AvailableCRS'), 'AvailableCRS', '__httpwww_opengis_netows_IdentificationType_httpwww_opengis_netowsAvailableCRS', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 85, 1), )

    
    AvailableCRS = property(__AvailableCRS.value, __AvailableCRS.set, None, None)

    _ElementMap.update({
        __Metadata.name() : __Metadata,
        __BoundingBox.name() : __BoundingBox,
        __Identifier.name() : __Identifier,
        __OutputFormat.name() : __OutputFormat,
        __AvailableCRS.name() : __AvailableCRS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.IdentificationType = IdentificationType
Namespace.addCategoryObject('typeBinding', 'IdentificationType', IdentificationType)


# Complex type {http://www.opengis.net/ows}CapabilitiesBaseType with content type ELEMENT_ONLY
class CapabilitiesBaseType (pyxb.binding.basis.complexTypeDefinition):
    """XML encoded GetCapabilities operation response. This document provides clients with service metadata about a specific service instance, usually including metadata about the tightly-coupled data served. If the server does not implement the updateSequence parameter, the server shall always return the complete Capabilities document, without the updateSequence parameter. When the server implements the updateSequence parameter and the GetCapabilities operation request included the updateSequence parameter with the current value, the server shall return this element with only the "version" and "updateSequence" attributes. Otherwise, all optional elements shall be included or not depending on the actual value of the Contents parameter in the GetCapabilities operation request. This base type shall be extended by each specific OWS to include the additional contents needed. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CapabilitiesBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 25, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}OperationsMetadata uses Python identifier OperationsMetadata
    __OperationsMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OperationsMetadata'), 'OperationsMetadata', '__httpwww_opengis_netows_CapabilitiesBaseType_httpwww_opengis_netowsOperationsMetadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 24, 1), )

    
    OperationsMetadata = property(__OperationsMetadata.value, __OperationsMetadata.set, None, 'Metadata about the operations and related abilities specified by this service and implemented by this server, including the URLs for operation requests. The basic contents of this section shall be the same for all OWS types, but individual services can add elements and/or change the optionality of optional elements. ')

    
    # Element {http://www.opengis.net/ows}ServiceIdentification uses Python identifier ServiceIdentification
    __ServiceIdentification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceIdentification'), 'ServiceIdentification', '__httpwww_opengis_netows_CapabilitiesBaseType_httpwww_opengis_netowsServiceIdentification', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceIdentification.xsd', 23, 1), )

    
    ServiceIdentification = property(__ServiceIdentification.value, __ServiceIdentification.set, None, 'General metadata for this specific server. This XML Schema of this section shall be the same for all OWS. ')

    
    # Element {http://www.opengis.net/ows}ServiceProvider uses Python identifier ServiceProvider
    __ServiceProvider = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceProvider'), 'ServiceProvider', '__httpwww_opengis_netows_CapabilitiesBaseType_httpwww_opengis_netowsServiceProvider', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceProvider.xsd', 23, 1), )

    
    ServiceProvider = property(__ServiceProvider.value, __ServiceProvider.set, None, 'Metadata about the organization that provides this specific service instance or server. ')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netows_CapabilitiesBaseType_version', _module_typeBindings.VersionType, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 34, 2)
    __version._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 34, 2)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute updateSequence uses Python identifier updateSequence
    __updateSequence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'updateSequence'), 'updateSequence', '__httpwww_opengis_netows_CapabilitiesBaseType_updateSequence', _module_typeBindings.UpdateSequenceType)
    __updateSequence._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 35, 2)
    __updateSequence._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 35, 2)
    
    updateSequence = property(__updateSequence.value, __updateSequence.set, None, None)

    _ElementMap.update({
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


# Complex type {http://www.opengis.net/ows}GetCapabilitiesType with content type ELEMENT_ONLY
class GetCapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    """XML encoded GetCapabilities operation request. This operation allows clients to retrieve service metadata about a specific service instance. In this XML encoding, no "request" parameter is included, since the element name specifies the specific operation. This base type shall be extended by each specific OWS to include the additional required "service" attribute, with the correct value for that OWS. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetCapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 40, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}AcceptVersions uses Python identifier AcceptVersions
    __AcceptVersions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AcceptVersions'), 'AcceptVersions', '__httpwww_opengis_netows_GetCapabilitiesType_httpwww_opengis_netowsAcceptVersions', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 45, 3), )

    
    AcceptVersions = property(__AcceptVersions.value, __AcceptVersions.set, None, 'When omitted, server shall return latest supported version. ')

    
    # Element {http://www.opengis.net/ows}Sections uses Python identifier Sections
    __Sections = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Sections'), 'Sections', '__httpwww_opengis_netows_GetCapabilitiesType_httpwww_opengis_netowsSections', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 50, 3), )

    
    Sections = property(__Sections.value, __Sections.set, None, 'When omitted or not supported by server, server shall return complete service metadata (Capabilities) document. ')

    
    # Element {http://www.opengis.net/ows}AcceptFormats uses Python identifier AcceptFormats
    __AcceptFormats = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AcceptFormats'), 'AcceptFormats', '__httpwww_opengis_netows_GetCapabilitiesType_httpwww_opengis_netowsAcceptFormats', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 55, 3), )

    
    AcceptFormats = property(__AcceptFormats.value, __AcceptFormats.set, None, 'When omitted or not supported by server, server shall return service metadata document using the MIME type "text/xml". ')

    
    # Attribute updateSequence uses Python identifier updateSequence
    __updateSequence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'updateSequence'), 'updateSequence', '__httpwww_opengis_netows_GetCapabilitiesType_updateSequence', _module_typeBindings.UpdateSequenceType)
    __updateSequence._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 61, 2)
    __updateSequence._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 61, 2)
    
    updateSequence = property(__updateSequence.value, __updateSequence.set, None, 'When omitted or not supported by server, server shall return latest complete service metadata document. ')

    _ElementMap.update({
        __AcceptVersions.name() : __AcceptVersions,
        __Sections.name() : __Sections,
        __AcceptFormats.name() : __AcceptFormats
    })
    _AttributeMap.update({
        __updateSequence.name() : __updateSequence
    })
_module_typeBindings.GetCapabilitiesType = GetCapabilitiesType
Namespace.addCategoryObject('typeBinding', 'GetCapabilitiesType', GetCapabilitiesType)


# Complex type {http://www.opengis.net/ows}RequestMethodType with content type ELEMENT_ONLY
class RequestMethodType (OnlineResourceType):
    """Connect point URL and any constraints for this HTTP request method for this operation request. In the OnlineResourceType, the xlink:href attribute in the xlink:simpleAttrs attribute group shall be used to contain this URL. The other attributes in the xlink:simpleAttrs attribute group should not be used. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestMethodType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 123, 1)
    _ElementMap = OnlineResourceType._ElementMap.copy()
    _AttributeMap = OnlineResourceType._AttributeMap.copy()
    # Base type is OnlineResourceType
    
    # Element {http://www.opengis.net/ows}Constraint uses Python identifier Constraint
    __Constraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), 'Constraint', '__httpwww_opengis_netows_RequestMethodType_httpwww_opengis_netowsConstraint', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 130, 5), )

    
    Constraint = property(__Constraint.value, __Constraint.set, None, 'Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this request method for this operation. If one of these Constraint elements has the same "name" attribute as a Constraint element in the OperationsMetadata or Operation element, this Constraint element shall override the other one for this operation. The list of required and optional constraints for this request method for this operation shall be specified in the Implementation Specification for this service. ')

    
    # Attribute type inherited from {http://www.opengis.net/ows}OnlineResourceType
    
    # Attribute href inherited from {http://www.opengis.net/ows}OnlineResourceType
    
    # Attribute role inherited from {http://www.opengis.net/ows}OnlineResourceType
    
    # Attribute arcrole inherited from {http://www.opengis.net/ows}OnlineResourceType
    
    # Attribute title inherited from {http://www.opengis.net/ows}OnlineResourceType
    
    # Attribute show inherited from {http://www.opengis.net/ows}OnlineResourceType
    
    # Attribute actuate inherited from {http://www.opengis.net/ows}OnlineResourceType
    _ElementMap.update({
        __Constraint.name() : __Constraint
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RequestMethodType = RequestMethodType
Namespace.addCategoryObject('typeBinding', 'RequestMethodType', RequestMethodType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (DescriptionType):
    """General metadata for this specific server. This XML Schema of this section shall be the same for all OWS. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceIdentification.xsd', 27, 2)
    _ElementMap = DescriptionType._ElementMap.copy()
    _AttributeMap = DescriptionType._AttributeMap.copy()
    # Base type is DescriptionType
    
    # Element Title ({http://www.opengis.net/ows}Title) inherited from {http://www.opengis.net/ows}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows}Abstract) inherited from {http://www.opengis.net/ows}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows}Keywords) inherited from {http://www.opengis.net/ows}DescriptionType
    
    # Element {http://www.opengis.net/ows}AccessConstraints uses Python identifier AccessConstraints
    __AccessConstraints = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AccessConstraints'), 'AccessConstraints', '__httpwww_opengis_netows_CTD_ANON_6_httpwww_opengis_netowsAccessConstraints', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 96, 1), )

    
    AccessConstraints = property(__AccessConstraints.value, __AccessConstraints.set, None, 'Access constraint applied to assure the protection of privacy or intellectual property, or any other restrictions on retrieving or using data from or otherwise using this server. The reserved value NONE (case insensitive) shall be used to mean no access constraints are imposed. ')

    
    # Element {http://www.opengis.net/ows}Fees uses Python identifier Fees
    __Fees = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Fees'), 'Fees', '__httpwww_opengis_netows_CTD_ANON_6_httpwww_opengis_netowsFees', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 102, 1), )

    
    Fees = property(__Fees.value, __Fees.set, None, 'Fees and terms for retrieving data from or otherwise using this server, including the monetary units as specified in ISO 4217. The reserved value NONE (case insensitive) shall be used to mean no fees or terms. ')

    
    # Element {http://www.opengis.net/ows}ServiceType uses Python identifier ServiceType
    __ServiceType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceType'), 'ServiceType', '__httpwww_opengis_netows_CTD_ANON_6_httpwww_opengis_netowsServiceType', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceIdentification.xsd', 31, 6), )

    
    ServiceType = property(__ServiceType.value, __ServiceType.set, None, 'A service type name from a registry of services. For example, the values of the codeSpace URI and name and code string may be "OGC" and "catalogue." This type name is normally used for machine-to-machine communication. ')

    
    # Element {http://www.opengis.net/ows}ServiceTypeVersion uses Python identifier ServiceTypeVersion
    __ServiceTypeVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceTypeVersion'), 'ServiceTypeVersion', '__httpwww_opengis_netows_CTD_ANON_6_httpwww_opengis_netowsServiceTypeVersion', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceIdentification.xsd', 36, 6), )

    
    ServiceTypeVersion = property(__ServiceTypeVersion.value, __ServiceTypeVersion.set, None, 'Unordered list of one or more versions of this service type implemented by this server. This information is not adequate for version negotiation, and shall not be used for that purpose. ')

    _ElementMap.update({
        __AccessConstraints.name() : __AccessConstraints,
        __Fees.name() : __Fees,
        __ServiceType.name() : __ServiceType,
        __ServiceTypeVersion.name() : __ServiceTypeVersion
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


Title = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Title'), pyxb.binding.datatypes.string, documentation='Title of this resource, normally used for display to a human. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 24, 1))
Namespace.addCategoryObject('elementBinding', Title.name().localName(), Title)

Abstract = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Abstract'), pyxb.binding.datatypes.string, documentation='Brief narrative description of this resource, normally used for display to a human. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 30, 1))
Namespace.addCategoryObject('elementBinding', Abstract.name().localName(), Abstract)

IndividualName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IndividualName'), pyxb.binding.datatypes.string, documentation='Name of the responsible person: surname, given name, title separated by a delimiter. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 95, 1))
Namespace.addCategoryObject('elementBinding', IndividualName.name().localName(), IndividualName)

OrganisationName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrganisationName'), pyxb.binding.datatypes.string, documentation='Name of the responsible organization. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 101, 1))
Namespace.addCategoryObject('elementBinding', OrganisationName.name().localName(), OrganisationName)

PositionName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PositionName'), pyxb.binding.datatypes.string, documentation='Role or position of the responsible person. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 107, 1))
Namespace.addCategoryObject('elementBinding', PositionName.name().localName(), PositionName)

AbstractMetaData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractMetaData'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), documentation='Abstract element containing more metadata about the element that includes the containing "metadata" element. A specific server implementation, or an Implementation Specification, can define concrete elements in the AbstractMetaData substitution group. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 61, 1))
Namespace.addCategoryObject('elementBinding', AbstractMetaData.name().localName(), AbstractMetaData)

AvailableCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AvailableCRS'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 85, 1))
Namespace.addCategoryObject('elementBinding', AvailableCRS.name().localName(), AvailableCRS)

SupportedCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SupportedCRS'), pyxb.binding.datatypes.anyURI, documentation='Coordinate reference system in which data from this data(set) or resource is available or supported. More specific parameter names should be used by specific OWS specifications wherever applicable. More than one such parameter can be included for different purposes. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 86, 1))
Namespace.addCategoryObject('elementBinding', SupportedCRS.name().localName(), SupportedCRS)

AccessConstraints = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AccessConstraints'), pyxb.binding.datatypes.string, documentation='Access constraint applied to assure the protection of privacy or intellectual property, or any other restrictions on retrieving or using data from or otherwise using this server. The reserved value NONE (case insensitive) shall be used to mean no access constraints are imposed. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 96, 1))
Namespace.addCategoryObject('elementBinding', AccessConstraints.name().localName(), AccessConstraints)

Fees = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Fees'), pyxb.binding.datatypes.string, documentation='Fees and terms for retrieving data from or otherwise using this server, including the monetary units as specified in ISO 4217. The reserved value NONE (case insensitive) shall be used to mean no fees or terms. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 102, 1))
Namespace.addCategoryObject('elementBinding', Fees.name().localName(), Fees)

Language = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Language'), pyxb.binding.datatypes.language, documentation='Identifier of a language used by the data(set) contents. This language identifier shall be as specified in IETF RFC 1766. When this element is omitted, the language used is not identified. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 108, 1))
Namespace.addCategoryObject('elementBinding', Language.name().localName(), Language)

ExtendedCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtendedCapabilities'), pyxb.binding.datatypes.anyType, documentation='Individual software vendors and servers can use this element to provide metadata about any additional server abilities. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 50, 1))
Namespace.addCategoryObject('elementBinding', ExtendedCapabilities.name().localName(), ExtendedCapabilities)

Keywords = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Keywords'), KeywordsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 36, 1))
Namespace.addCategoryObject('elementBinding', Keywords.name().localName(), Keywords)

PointOfContact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PointOfContact'), ResponsiblePartyType, documentation='Identification of, and means of communication with, person(s) responsible for the resource(s). For OWS use in the ServiceProvider section of a service metadata document, the optional organizationName element was removed, since this type is always used with the ProviderName element which provides that information. The optional individualName element was made mandatory, since either the organizationName or individualName element is mandatory. The mandatory "role" element was changed to optional, since no clear use of this information is known in the ServiceProvider section. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 61, 1))
Namespace.addCategoryObject('elementBinding', PointOfContact.name().localName(), PointOfContact)

Role = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Role'), CodeType, documentation='Function performed by the responsible party. Possible values of this Role shall include the values and the meanings listed in Subclause B.5.5 of ISO 19115:2003. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 113, 1))
Namespace.addCategoryObject('elementBinding', Role.name().localName(), Role)

ContactInfo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo'), ContactType, documentation='Address of the responsible party. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 119, 1))
Namespace.addCategoryObject('elementBinding', ContactInfo.name().localName(), ContactInfo)

Metadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), MetadataType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 40, 1))
Namespace.addCategoryObject('elementBinding', Metadata.name().localName(), Metadata)

BoundingBox = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox'), BoundingBoxType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 68, 1))
Namespace.addCategoryObject('elementBinding', BoundingBox.name().localName(), BoundingBox)

Identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), CodeType, documentation='Unique identifier or name of this dataset. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 73, 1))
Namespace.addCategoryObject('elementBinding', Identifier.name().localName(), Identifier)

OutputFormat = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), MimeType, documentation='Reference to a format in which this data can be encoded and transferred. More specific parameter names should be used by specific OWS specifications wherever applicable. More than one such parameter can be included for different purposes. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 79, 1))
Namespace.addCategoryObject('elementBinding', OutputFormat.name().localName(), OutputFormat)

ExceptionReport = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExceptionReport'), CTD_ANON, documentation='Report message returned to the client that requested any OWS operation when the server detects an error while processing that operation request. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 19, 1))
Namespace.addCategoryObject('elementBinding', ExceptionReport.name().localName(), ExceptionReport)

Exception = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Exception'), ExceptionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 44, 1))
Namespace.addCategoryObject('elementBinding', Exception.name().localName(), Exception)

OperationsMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OperationsMetadata'), CTD_ANON_, documentation='Metadata about the operations and related abilities specified by this service and implemented by this server, including the URLs for operation requests. The basic contents of this section shall be the same for all OWS types, but individual services can add elements and/or change the optionality of optional elements. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 24, 1))
Namespace.addCategoryObject('elementBinding', OperationsMetadata.name().localName(), OperationsMetadata)

Operation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Operation'), CTD_ANON_2, documentation='Metadata for one operation that this server implements. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 56, 1))
Namespace.addCategoryObject('elementBinding', Operation.name().localName(), Operation)

DCP = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DCP'), CTD_ANON_3, documentation='Information for one distributed Computing Platform (DCP) supported for this operation. At present, only the HTTP DCP is defined, so this element only includes the HTTP element.\n', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 91, 1))
Namespace.addCategoryObject('elementBinding', DCP.name().localName(), DCP)

HTTP = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HTTP'), CTD_ANON_4, documentation='Connect point URLs for the HTTP Distributed Computing Platform (DCP). Normally, only one Get and/or one Post is included in this element. More than one Get and/or Post is allowed to support including alternative URLs for uses such as load balancing or backup. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 103, 1))
Namespace.addCategoryObject('elementBinding', HTTP.name().localName(), HTTP)

ServiceProvider = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceProvider'), CTD_ANON_5, documentation='Metadata about the organization that provides this specific service instance or server. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceProvider.xsd', 23, 1))
Namespace.addCategoryObject('elementBinding', ServiceProvider.name().localName(), ServiceProvider)

WGS84BoundingBox = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WGS84BoundingBox'), WGS84BoundingBoxType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 111, 1))
Namespace.addCategoryObject('elementBinding', WGS84BoundingBox.name().localName(), WGS84BoundingBox)

GetCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetCapabilities'), GetCapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 38, 1))
Namespace.addCategoryObject('elementBinding', GetCapabilities.name().localName(), GetCapabilities)

ServiceIdentification = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceIdentification'), CTD_ANON_6, documentation='General metadata for this specific server. This XML Schema of this section shall be the same for all OWS. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceIdentification.xsd', 23, 1))
Namespace.addCategoryObject('elementBinding', ServiceIdentification.name().localName(), ServiceIdentification)



KeywordsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Keyword'), pyxb.binding.datatypes.string, scope=KeywordsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 44, 3)))

KeywordsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Type'), CodeType, scope=KeywordsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 45, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 45, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(KeywordsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keyword')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 44, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(KeywordsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Type')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 45, 3))
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




ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IndividualName'), pyxb.binding.datatypes.string, scope=ResponsiblePartyType, documentation='Name of the responsible person: surname, given name, title separated by a delimiter. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 95, 1)))

ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrganisationName'), pyxb.binding.datatypes.string, scope=ResponsiblePartyType, documentation='Name of the responsible organization. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 101, 1)))

ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PositionName'), pyxb.binding.datatypes.string, scope=ResponsiblePartyType, documentation='Role or position of the responsible person. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 107, 1)))

ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Role'), CodeType, scope=ResponsiblePartyType, documentation='Function performed by the responsible party. Possible values of this Role shall include the values and the meanings listed in Subclause B.5.5 of ISO 19115:2003. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 113, 1)))

ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo'), ContactType, scope=ResponsiblePartyType, documentation='Address of the responsible party. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 119, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 73, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 74, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 75, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 76, 3))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IndividualName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 73, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrganisationName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 74, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PositionName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 75, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 76, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Role')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 77, 3))
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




ResponsiblePartySubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IndividualName'), pyxb.binding.datatypes.string, scope=ResponsiblePartySubsetType, documentation='Name of the responsible person: surname, given name, title separated by a delimiter. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 95, 1)))

ResponsiblePartySubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PositionName'), pyxb.binding.datatypes.string, scope=ResponsiblePartySubsetType, documentation='Role or position of the responsible person. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 107, 1)))

ResponsiblePartySubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Role'), CodeType, scope=ResponsiblePartySubsetType, documentation='Function performed by the responsible party. Possible values of this Role shall include the values and the meanings listed in Subclause B.5.5 of ISO 19115:2003. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 113, 1)))

ResponsiblePartySubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo'), ContactType, scope=ResponsiblePartySubsetType, documentation='Address of the responsible party. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 119, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 88, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 89, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 90, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 91, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IndividualName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 88, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PositionName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 89, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 90, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Role')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 91, 3))
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




ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Phone'), TelephoneType, scope=ContactType, documentation='Telephone numbers at which the organization or individual may be contacted. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 131, 3)))

ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Address'), AddressType, scope=ContactType, documentation='Physical and email address at which the organization or individual may be contacted. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 136, 3)))

ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OnlineResource'), OnlineResourceType, scope=ContactType, documentation='On-line information that can be used to contact the individual or organization. OWS specifics: The xlink:href attribute in the xlink:simpleAttrs attribute group shall be used to reference this resource. Whenever practical, the xlink:href attribute with type anyURI should be a URL from which more contact information can be electronically retrieved. The xlink:title attribute with type "string" can be used to name this set of information. The other attributes in the xlink:simpleAttrs attribute group should not be used. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 141, 3)))

ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HoursOfService'), pyxb.binding.datatypes.string, scope=ContactType, documentation='Time period (including time zone) when individuals can contact the organization or individual. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 146, 3)))

ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContactInstructions'), pyxb.binding.datatypes.string, scope=ContactType, documentation='Supplemental instructions on how or when to contact the individual or organization. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 151, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 131, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 136, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 141, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 146, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 151, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Phone')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 131, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Address')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 136, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OnlineResource')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 141, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HoursOfService')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 146, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContactInstructions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 151, 3))
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




TelephoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Voice'), pyxb.binding.datatypes.string, scope=TelephoneType, documentation='Telephone number by which individuals can speak to the responsible organization or individual. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 172, 3)))

TelephoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Facsimile'), pyxb.binding.datatypes.string, scope=TelephoneType, documentation='Telephone number of a facsimile machine for the responsible\norganization or individual. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 177, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 172, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 177, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TelephoneType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Voice')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 172, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TelephoneType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Facsimile')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 177, 3))
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




AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DeliveryPoint'), pyxb.binding.datatypes.string, scope=AddressType, documentation='Address line for the location. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 191, 3)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'City'), pyxb.binding.datatypes.string, scope=AddressType, documentation='City of the location. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 196, 3)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeArea'), pyxb.binding.datatypes.string, scope=AddressType, documentation='State or province of the location. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 201, 3)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), pyxb.binding.datatypes.string, scope=AddressType, documentation='ZIP or other postal code. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 206, 3)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Country'), pyxb.binding.datatypes.string, scope=AddressType, documentation='Country of the physical address. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 211, 3)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ElectronicMailAddress'), pyxb.binding.datatypes.string, scope=AddressType, documentation='Address of the electronic mailbox of the responsible organization or individual. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 216, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 191, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 196, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 201, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 206, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 211, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 216, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DeliveryPoint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 191, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'City')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 196, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeArea')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 201, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCode')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 206, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Country')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 211, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ElectronicMailAddress')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 216, 3))
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




MetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractMetaData'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=MetadataType, documentation='Abstract element containing more metadata about the element that includes the containing "metadata" element. A specific server implementation, or an Implementation Specification, can define concrete elements in the AbstractMetaData substitution group. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 61, 1)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 47, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AbstractMetaData')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 47, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MetadataType._Automaton = _BuildAutomaton_6()




BoundingBoxType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LowerCorner'), PositionType, scope=BoundingBoxType, documentation='Position of the bounding box corner at which the value of each coordinate normally is the algebraic minimum within this bounding box. In some cases, this position is normally displayed at the top, such as the top left for some image coordinates. For more information, see Subclauses 10.2.5 and C.13. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 76, 3)))

BoundingBoxType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UpperCorner'), PositionType, scope=BoundingBoxType, documentation='Position of the bounding box corner at which the value of each coordinate normally is the algebraic maximum within this bounding box. In some cases, this position is normally displayed at the bottom, such as the bottom right for some image coordinates. For more information, see Subclauses 10.2.5 and C.13. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 81, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BoundingBoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LowerCorner')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 76, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BoundingBoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UpperCorner')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 81, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BoundingBoxType._Automaton = _BuildAutomaton_7()




DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Title'), pyxb.binding.datatypes.string, scope=DescriptionType, documentation='Title of this resource, normally used for display to a human. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 24, 1)))

DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Abstract'), pyxb.binding.datatypes.string, scope=DescriptionType, documentation='Brief narrative description of this resource, normally used for display to a human. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 30, 1)))

DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Keywords'), KeywordsType, scope=DescriptionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 36, 1)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 30, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 31, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 32, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 30, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keywords')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 32, 3))
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
DescriptionType._Automaton = _BuildAutomaton_8()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Exception'), ExceptionType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 44, 1)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Exception')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 25, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_9()




ExceptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExceptionText'), pyxb.binding.datatypes.string, scope=ExceptionType, documentation='Ordered sequence of text strings that describe this specific exception or error. The contents of these strings are left open to definition by each server implementation. A server is strongly encouraged to include at least one ExceptionText value, to provide more information about the detected error than provided by the exceptionCode. When included, multiple ExceptionText values shall provide hierarchical information about one detected error, with the most significant information listed first. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 51, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 51, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExceptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExceptionText')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsExceptionReport.xsd', 51, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ExceptionType._Automaton = _BuildAutomaton_10()




AcceptVersionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Version'), VersionType, scope=AcceptVersionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 81, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AcceptVersionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Version')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 81, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AcceptVersionsType._Automaton = _BuildAutomaton_11()




SectionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Section'), pyxb.binding.datatypes.string, scope=SectionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 90, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 90, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SectionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Section')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 90, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SectionsType._Automaton = _BuildAutomaton_12()




AcceptFormatsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), MimeType, scope=AcceptFormatsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 106, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 106, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AcceptFormatsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 106, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AcceptFormatsType._Automaton = _BuildAutomaton_13()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Parameter'), DomainType, scope=CTD_ANON_, documentation='Optional unordered list of parameter valid domains that each apply to one or more operations which this server interface implements. The list of required and optional parameter domain limitations shall be specified in the Implementation Specification for this service. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 35, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), DomainType, scope=CTD_ANON_, documentation='Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this server. The list of required and optional constraints shall be specified in the Implementation Specification for this service. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 40, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtendedCapabilities'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_, documentation='Individual software vendors and servers can use this element to provide metadata about any additional server abilities. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 50, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Operation'), CTD_ANON_2, scope=CTD_ANON_, documentation='Metadata for one operation that this server implements. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 56, 1)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 30, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 35, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 40, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 45, 4))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Operation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 30, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Parameter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 35, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Constraint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 40, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExtendedCapabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 45, 4))
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
CTD_ANON_._Automaton = _BuildAutomaton_14()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), MetadataType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 40, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Parameter'), DomainType, scope=CTD_ANON_2, documentation='Optional unordered list of parameter domains that each apply to this operation which this server implements. If one of these Parameter elements has the same "name" attribute as a Parameter element in the OperationsMetadata element, this Parameter element shall override the other one for this operation. The list of required and optional parameter domain limitations for this operation shall be specified in the Implementation Specification for this service. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 67, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), DomainType, scope=CTD_ANON_2, documentation='Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this operation. If one of these Constraint elements has the same "name" attribute as a Constraint element in the OperationsMetadata element, this Constraint element shall override the other one for this operation. The list of required and optional constraints for this operation shall be specified in the Implementation Specification for this service. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 72, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DCP'), CTD_ANON_3, scope=CTD_ANON_2, documentation='Information for one distributed Computing Platform (DCP) supported for this operation. At present, only the HTTP DCP is defined, so this element only includes the HTTP element.\n', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 91, 1)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 67, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 72, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 77, 4))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DCP')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 62, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Parameter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 67, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Constraint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 72, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 77, 4))
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
CTD_ANON_2._Automaton = _BuildAutomaton_15()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HTTP'), CTD_ANON_4, scope=CTD_ANON_3, documentation='Connect point URLs for the HTTP Distributed Computing Platform (DCP). Normally, only one Get and/or one Post is included in this element. More than one Get and/or Post is allowed to support including alternative URLs for uses such as load balancing or backup. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 103, 1)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HTTP')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 98, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_16()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Get'), RequestMethodType, scope=CTD_ANON_4, documentation='Connect point URL prefix and any constraints for the HTTP "Get" request method for this operation request. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 109, 4)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Post'), RequestMethodType, scope=CTD_ANON_4, documentation='Connect point URL and any constraints for the HTTP "Post" request method for this operation request. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 114, 4)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Get')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 109, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Post')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 114, 4))
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
CTD_ANON_4._Automaton = _BuildAutomaton_17()




DomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), MetadataType, scope=DomainType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 40, 1)))

DomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Value'), pyxb.binding.datatypes.string, scope=DomainType, documentation='Unordered list of all the valid values for this parameter or other quantity. For those parameters that contain a list or sequence of values, these values shall be for individual values in the list. The allowed set of values and the allowed server restrictions on that set of values shall be specified in the Implementation Specification for this service. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 145, 3)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 150, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Value')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 145, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 150, 3))
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
DomainType._Automaton = _BuildAutomaton_18()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProviderName'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, documentation='A unique identifier for the service provider organization. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceProvider.xsd', 29, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProviderSite'), OnlineResourceType, scope=CTD_ANON_5, documentation='Reference to the most relevant web site of the service provider. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceProvider.xsd', 34, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceContact'), ResponsiblePartySubsetType, scope=CTD_ANON_5, documentation='Information for contacting the service provider. The OnlineResource element within this ServiceContact element should not be used to reference a web site of the service provider. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceProvider.xsd', 39, 4)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceProvider.xsd', 34, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProviderName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceProvider.xsd', 29, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProviderSite')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceProvider.xsd', 34, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceContact')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceProvider.xsd', 39, 4))
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
CTD_ANON_5._Automaton = _BuildAutomaton_19()




def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WGS84BoundingBoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LowerCorner')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 121, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(WGS84BoundingBoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UpperCorner')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 126, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
WGS84BoundingBoxType._Automaton = _BuildAutomaton_20()




IdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), MetadataType, scope=IdentificationType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 40, 1)))

IdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox'), BoundingBoxType, scope=IdentificationType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 68, 1)))

IdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), CodeType, scope=IdentificationType, documentation='Unique identifier or name of this dataset. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 73, 1)))

IdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), MimeType, scope=IdentificationType, documentation='Reference to a format in which this data can be encoded and transferred. More specific parameter names should be used by specific OWS specifications wherever applicable. More than one such parameter can be included for different purposes. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 79, 1)))

IdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AvailableCRS'), pyxb.binding.datatypes.anyURI, scope=IdentificationType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 85, 1)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 30, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 31, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 32, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 43, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 48, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 53, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 58, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 63, 5))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 30, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keywords')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 32, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 43, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 48, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 53, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AvailableCRS')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 58, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 63, 5))
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
IdentificationType._Automaton = _BuildAutomaton_21()




CapabilitiesBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OperationsMetadata'), CTD_ANON_, scope=CapabilitiesBaseType, documentation='Metadata about the operations and related abilities specified by this service and implemented by this server, including the URLs for operation requests. The basic contents of this section shall be the same for all OWS types, but individual services can add elements and/or change the optionality of optional elements. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 24, 1)))

CapabilitiesBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceIdentification'), CTD_ANON_6, scope=CapabilitiesBaseType, documentation='General metadata for this specific server. This XML Schema of this section shall be the same for all OWS. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceIdentification.xsd', 23, 1)))

CapabilitiesBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceProvider'), CTD_ANON_5, scope=CapabilitiesBaseType, documentation='Metadata about the organization that provides this specific service instance or server. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceProvider.xsd', 23, 1)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 30, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 31, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 32, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CapabilitiesBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceIdentification')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 30, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CapabilitiesBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceProvider')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CapabilitiesBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OperationsMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 32, 3))
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
CapabilitiesBaseType._Automaton = _BuildAutomaton_22()




GetCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AcceptVersions'), AcceptVersionsType, scope=GetCapabilitiesType, documentation='When omitted, server shall return latest supported version. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 45, 3)))

GetCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Sections'), SectionsType, scope=GetCapabilitiesType, documentation='When omitted or not supported by server, server shall return complete service metadata (Capabilities) document. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 50, 3)))

GetCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AcceptFormats'), AcceptFormatsType, scope=GetCapabilitiesType, documentation='When omitted or not supported by server, server shall return service metadata document using the MIME type "text/xml". ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 55, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 45, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 50, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 55, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AcceptVersions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 45, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Sections')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 50, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AcceptFormats')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 55, 3))
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
GetCapabilitiesType._Automaton = _BuildAutomaton_23()




RequestMethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), DomainType, scope=RequestMethodType, documentation='Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this request method for this operation. If one of these Constraint elements has the same "name" attribute as a Constraint element in the OperationsMetadata or Operation element, this Constraint element shall override the other one for this operation. The list of required and optional constraints for this request method for this operation shall be specified in the Implementation Specification for this service. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 130, 5)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 130, 5))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RequestMethodType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Constraint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsOperationsMetadata.xsd', 130, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RequestMethodType._Automaton = _BuildAutomaton_24()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AccessConstraints'), pyxb.binding.datatypes.string, scope=CTD_ANON_6, documentation='Access constraint applied to assure the protection of privacy or intellectual property, or any other restrictions on retrieving or using data from or otherwise using this server. The reserved value NONE (case insensitive) shall be used to mean no access constraints are imposed. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 96, 1)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Fees'), pyxb.binding.datatypes.string, scope=CTD_ANON_6, documentation='Fees and terms for retrieving data from or otherwise using this server, including the monetary units as specified in ISO 4217. The reserved value NONE (case insensitive) shall be used to mean no fees or terms. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 102, 1)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceType'), CodeType, scope=CTD_ANON_6, documentation='A service type name from a registry of services. For example, the values of the codeSpace URI and name and code string may be "OGC" and "catalogue." This type name is normally used for machine-to-machine communication. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceIdentification.xsd', 31, 6)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceTypeVersion'), VersionType, scope=CTD_ANON_6, documentation='Unordered list of one or more versions of this service type implemented by this server. This information is not adequate for version negotiation, and shall not be used for that purpose. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceIdentification.xsd', 36, 6)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 30, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 31, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 32, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceIdentification.xsd', 41, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceIdentification.xsd', 46, 6))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 30, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keywords')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsDataIdentification.xsd', 32, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceIdentification.xsd', 31, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceTypeVersion')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceIdentification.xsd', 36, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Fees')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceIdentification.xsd', 41, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AccessConstraints')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsServiceIdentification.xsd', 46, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_25()


SupportedCRS._setSubstitutionGroup(AvailableCRS)

WGS84BoundingBox._setSubstitutionGroup(BoundingBox)
