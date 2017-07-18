# ./pyxb/bundles/opengis/raw/wfs.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:eac7f5293585184de4c856df1b5ca308e1a93caf
# Generated 2017-07-10 00:37:26.146433 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/wfs

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:f1834126-6507-11e7-9eb6-0a55f9edafa5')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.bundles.opengis.gml
import pyxb.binding.datatypes
import pyxb.bundles.opengis.ows
import pyxb.bundles.opengis.filter

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/wfs', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ows = pyxb.bundles.opengis.ows.Namespace
_Namespace_ows.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ogc = pyxb.bundles.opengis.filter.Namespace
_Namespace_ogc.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gml = pyxb.bundles.opengis.gml.Namespace
_Namespace_gml.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://www.opengis.net/wfs}OperationType
class OperationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OperationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 330, 3)
    _Documentation = None
OperationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=OperationType, enum_prefix=None)
OperationType.Insert = OperationType._CF_enumeration.addEnumeration(unicode_value='Insert', tag='Insert')
OperationType.Update = OperationType._CF_enumeration.addEnumeration(unicode_value='Update', tag='Update')
OperationType.Delete = OperationType._CF_enumeration.addEnumeration(unicode_value='Delete', tag='Delete')
OperationType.Query = OperationType._CF_enumeration.addEnumeration(unicode_value='Query', tag='Query')
OperationType.Lock = OperationType._CF_enumeration.addEnumeration(unicode_value='Lock', tag='Lock')
OperationType.GetGmlObject = OperationType._CF_enumeration.addEnumeration(unicode_value='GetGmlObject', tag='GetGmlObject')
OperationType._InitializeFacetMap(OperationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'OperationType', OperationType)
_module_typeBindings.OperationType = OperationType

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 362, 15)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.TC211 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='TC211', tag='TC211')
STD_ANON.FGDC = STD_ANON._CF_enumeration.addEnumeration(unicode_value='FGDC', tag='FGDC')
STD_ANON.n19115 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='19115', tag='n19115')
STD_ANON.n19139 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='19139', tag='n19139')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 372, 15)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.textxml = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='text/xml', tag='textxml')
STD_ANON_.texthtml = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='text/html', tag='texthtml')
STD_ANON_.textsgml = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='text/sgml', tag='textsgml')
STD_ANON_.textplain = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='text/plain', tag='textplain')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: {http://www.opengis.net/wfs}ResultTypeType
class ResultTypeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResultTypeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 655, 3)
    _Documentation = None
ResultTypeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ResultTypeType, enum_prefix=None)
ResultTypeType.results = ResultTypeType._CF_enumeration.addEnumeration(unicode_value='results', tag='results')
ResultTypeType.hits = ResultTypeType._CF_enumeration.addEnumeration(unicode_value='hits', tag='hits')
ResultTypeType._InitializeFacetMap(ResultTypeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ResultTypeType', ResultTypeType)
_module_typeBindings.ResultTypeType = ResultTypeType

# List simple type: {http://www.opengis.net/wfs}Base_TypeNameListType
# superclasses pyxb.binding.datatypes.anySimpleType
class Base_TypeNameListType (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.QName."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Base_TypeNameListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 816, 3)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.QName
Base_TypeNameListType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Base_TypeNameListType', Base_TypeNameListType)
_module_typeBindings.Base_TypeNameListType = Base_TypeNameListType

# Atomic simple type: {http://www.opengis.net/wfs}AllSomeType
class AllSomeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AllSomeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1137, 3)
    _Documentation = None
AllSomeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AllSomeType, enum_prefix=None)
AllSomeType.ALL = AllSomeType._CF_enumeration.addEnumeration(unicode_value='ALL', tag='ALL')
AllSomeType.SOME = AllSomeType._CF_enumeration.addEnumeration(unicode_value='SOME', tag='SOME')
AllSomeType._InitializeFacetMap(AllSomeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AllSomeType', AllSomeType)
_module_typeBindings.AllSomeType = AllSomeType

# Atomic simple type: {http://www.opengis.net/wfs}IdentifierGenerationOptionType
class IdentifierGenerationOptionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IdentifierGenerationOptionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1431, 3)
    _Documentation = None
IdentifierGenerationOptionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IdentifierGenerationOptionType, enum_prefix=None)
IdentifierGenerationOptionType.UseExisting = IdentifierGenerationOptionType._CF_enumeration.addEnumeration(unicode_value='UseExisting', tag='UseExisting')
IdentifierGenerationOptionType.ReplaceDuplicate = IdentifierGenerationOptionType._CF_enumeration.addEnumeration(unicode_value='ReplaceDuplicate', tag='ReplaceDuplicate')
IdentifierGenerationOptionType.GenerateNew = IdentifierGenerationOptionType._CF_enumeration.addEnumeration(unicode_value='GenerateNew', tag='GenerateNew')
IdentifierGenerationOptionType._InitializeFacetMap(IdentifierGenerationOptionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'IdentifierGenerationOptionType', IdentifierGenerationOptionType)
_module_typeBindings.IdentifierGenerationOptionType = IdentifierGenerationOptionType

# List simple type: {http://www.opengis.net/wfs}TypeNameListType
# superclasses Base_TypeNameListType
class TypeNameListType (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.QName."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TypeNameListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 819, 3)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.QName
TypeNameListType._CF_pattern = pyxb.binding.facets.CF_pattern()
TypeNameListType._CF_pattern.addPattern(pattern='((\\w:)?\\w(=\\w)?){1,}')
TypeNameListType._InitializeFacetMap(TypeNameListType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TypeNameListType', TypeNameListType)
_module_typeBindings.TypeNameListType = TypeNameListType

# Complex type {http://www.opengis.net/wfs}BaseRequestType with content type EMPTY
class BaseRequestType (pyxb.binding.basis.complexTypeDefinition):
    """
            XML encoded WFS operation request base, for all operations
            except GetCapabilities.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BaseRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 28, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__httpwww_opengis_netwfs_BaseRequestType_service', pyxb.bundles.opengis.ows.ServiceType, unicode_default='WFS')
    __service._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 35, 6)
    __service._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 35, 6)
    
    service = property(__service.value, __service.set, None, '\n              The service attribute is included to support service \n              endpoints that implement more than one OGC service.\n              For example, a single CGI that implements WMS, WFS\n              and WCS services. \n              The endpoint can inspect the value of this attribute \n              to figure out which service should process the request.\n              The value WFS indicates that a web feature service should\n              process the request.\n              This parameter is somewhat redundant in the XML encoding\n              since the request namespace can be used to determine\n              which service should process any give request.  For example,\n              wfs:GetCapabilities and easily be distinguished from\n              wcs:GetCapabilities using the namespaces.\n           ')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netwfs_BaseRequestType_version', pyxb.binding.datatypes.string, unicode_default='1.1.0')
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 55, 6)
    __version._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 55, 6)
    
    version = property(__version.value, __version.set, None, '\n               The version attribute is used to indicate the version of the\n               WFS specification that a request conforms to.  All requests in\n               this schema conform to V1.1 of the WFS specification.\n               For WFS implementations that support more than one version of\n               a WFS sepcification ... if the version attribute is not \n               specified then the service should assume that the request\n               conforms to greatest available specification version.\n           ')

    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'handle'), 'handle', '__httpwww_opengis_netwfs_BaseRequestType_handle', pyxb.binding.datatypes.string)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 69, 6)
    __handle._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 69, 6)
    
    handle = property(__handle.value, __handle.set, None, '\n               The handle attribute allows a client application\n               to assign a client-generated request identifier\n               to a WFS request.  The handle is included to\n               facilitate error reporting.  A WFS may report the\n               handle in an exception report to identify the\n               offending request or action.  If the handle is not\n               present, then the WFS may employ other means to\n               localize the error (e.g. line numbers).\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __service.name() : __service,
        __version.name() : __version,
        __handle.name() : __handle
    })
_module_typeBindings.BaseRequestType = BaseRequestType
Namespace.addCategoryObject('typeBinding', 'BaseRequestType', BaseRequestType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """
            This element may be used in place of an wfs:PropertyName element
            in a wfs:Query element in a wfs:GetFeature element to selectively
            request the traversal of nested XLinks in the returned element for
            the named property. This element may not be used in other requests
            -- GetFeatureWithLock, LockFeature, Insert, Update, Delete -- in
            this version of the WFS specification.
         """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 125, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute traverseXlinkDepth uses Python identifier traverseXlinkDepth
    __traverseXlinkDepth = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'traverseXlinkDepth'), 'traverseXlinkDepth', '__httpwww_opengis_netwfs_CTD_ANON_traverseXlinkDepth', pyxb.binding.datatypes.string, required=True)
    __traverseXlinkDepth._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 128, 15)
    __traverseXlinkDepth._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 128, 15)
    
    traverseXlinkDepth = property(__traverseXlinkDepth.value, __traverseXlinkDepth.set, None, '\n                  This attribute indicates the depth to which nested property\n                  XLink linking element locator attribute (href) XLinks are\n                  traversed and resolved if possible.  A value of "1" indicates\n                  that one linking element locator attribute (href) Xlink\n                  will be traversed and the referenced element returned if\n                  possible, but nested property XLink linking element locator\n                  attribute (href) XLinks in the returned element are not\n                  traversed.  A value of  "*" indicates that all nested property\n                  XLink linking element locator attribute (href) XLinks will be\n                  traversed and the referenced elements returned if possible.\n                  The range of valid values for this attribute consists of\n                  positive integers plus "*".\n                     ')

    
    # Attribute traverseXlinkExpiry uses Python identifier traverseXlinkExpiry
    __traverseXlinkExpiry = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'traverseXlinkExpiry'), 'traverseXlinkExpiry', '__httpwww_opengis_netwfs_CTD_ANON_traverseXlinkExpiry', pyxb.binding.datatypes.positiveInteger)
    __traverseXlinkExpiry._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 147, 15)
    __traverseXlinkExpiry._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 147, 15)
    
    traverseXlinkExpiry = property(__traverseXlinkExpiry.value, __traverseXlinkExpiry.set, None, '\n                  The traverseXlinkExpiry attribute value is specified in\n                  minutes It indicates how long a Web Feature Service should\n                  wait to receive a response to a nested GetGmlObject request.\t\n                     ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __traverseXlinkDepth.name() : __traverseXlinkDepth,
        __traverseXlinkExpiry.name() : __traverseXlinkExpiry
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://www.opengis.net/wfs}GetCapabilitiesType with content type ELEMENT_ONLY
class GetCapabilitiesType (pyxb.bundles.opengis.ows.GetCapabilitiesType):
    """
          Request to a WFS to perform the GetCapabilities operation.
          This operation allows a client to retrieve a Capabilities
          XML document providing metadata for the specific WFS server.

          The GetCapapbilities element is used to request that a Web Feature
          Service generate an XML document describing the organization
          providing the service, the WFS operations that the service
          supports, a list of feature types that the service can operate
          on and list of filtering capabilities that the service support.
          Such an XML document is called a capabilities document.
       """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetCapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 168, 3)
    _ElementMap = pyxb.bundles.opengis.ows.GetCapabilitiesType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.ows.GetCapabilitiesType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.ows.GetCapabilitiesType
    
    # Element AcceptVersions ({http://www.opengis.net/ows}AcceptVersions) inherited from {http://www.opengis.net/ows}GetCapabilitiesType
    
    # Element Sections ({http://www.opengis.net/ows}Sections) inherited from {http://www.opengis.net/ows}GetCapabilitiesType
    
    # Element AcceptFormats ({http://www.opengis.net/ows}AcceptFormats) inherited from {http://www.opengis.net/ows}GetCapabilitiesType
    
    # Attribute updateSequence inherited from {http://www.opengis.net/ows}GetCapabilitiesType
    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__httpwww_opengis_netwfs_GetCapabilitiesType_service', pyxb.bundles.opengis.ows.ServiceType, unicode_default='WFS')
    __service._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 185, 9)
    __service._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 185, 9)
    
    service = property(__service.value, __service.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __service.name() : __service
    })
_module_typeBindings.GetCapabilitiesType = GetCapabilitiesType
Namespace.addCategoryObject('typeBinding', 'GetCapabilitiesType', GetCapabilitiesType)


# Complex type {http://www.opengis.net/wfs}WFS_CapabilitiesType with content type ELEMENT_ONLY
class WFS_CapabilitiesType (pyxb.bundles.opengis.ows.CapabilitiesBaseType):
    """
            XML encoded WFS GetCapabilities operation response. This
            document provides clients with service metadata about a
            specific service instance, including metadata about the
            tightly-coupled data served. If the server does not implement
            the updateSequence parameter, the server shall always return
            the complete Capabilities document, without the updateSequence
            parameter. When the server implements the updateSequence
            parameter and the GetCapabilities operation request included
            the updateSequence parameter with the current value, the server
            shall return this element with only the "version" and
            "updateSequence" attributes. Otherwise, all optional elements
            shall be included or not depending on the actual value of the
            Contents parameter in the GetCapabilities operation request.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WFS_CapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 194, 3)
    _ElementMap = pyxb.bundles.opengis.ows.CapabilitiesBaseType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.ows.CapabilitiesBaseType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.ows.CapabilitiesBaseType
    
    # Element {http://www.opengis.net/ogc}Filter_Capabilities uses Python identifier Filter_Capabilities
    __Filter_Capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter_Capabilities'), 'Filter_Capabilities', '__httpwww_opengis_netwfs_WFS_CapabilitiesType_httpwww_opengis_netogcFilter_Capabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 20, 3), )

    
    Filter_Capabilities = property(__Filter_Capabilities.value, __Filter_Capabilities.set, None, None)

    
    # Element OperationsMetadata ({http://www.opengis.net/ows}OperationsMetadata) inherited from {http://www.opengis.net/ows}CapabilitiesBaseType
    
    # Element ServiceIdentification ({http://www.opengis.net/ows}ServiceIdentification) inherited from {http://www.opengis.net/ows}CapabilitiesBaseType
    
    # Element ServiceProvider ({http://www.opengis.net/ows}ServiceProvider) inherited from {http://www.opengis.net/ows}CapabilitiesBaseType
    
    # Element {http://www.opengis.net/wfs}FeatureTypeList uses Python identifier FeatureTypeList
    __FeatureTypeList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FeatureTypeList'), 'FeatureTypeList', '__httpwww_opengis_netwfs_WFS_CapabilitiesType_httpwww_opengis_netwfsFeatureTypeList', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 223, 3), )

    
    FeatureTypeList = property(__FeatureTypeList.value, __FeatureTypeList.set, None, None)

    
    # Element {http://www.opengis.net/wfs}ServesGMLObjectTypeList uses Python identifier ServesGMLObjectTypeList
    __ServesGMLObjectTypeList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServesGMLObjectTypeList'), 'ServesGMLObjectTypeList', '__httpwww_opengis_netwfs_WFS_CapabilitiesType_httpwww_opengis_netwfsServesGMLObjectTypeList', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 384, 3), )

    
    ServesGMLObjectTypeList = property(__ServesGMLObjectTypeList.value, __ServesGMLObjectTypeList.set, None, '\n            List of GML Object types available for GetGmlObject requests\n         ')

    
    # Element {http://www.opengis.net/wfs}SupportsGMLObjectTypeList uses Python identifier SupportsGMLObjectTypeList
    __SupportsGMLObjectTypeList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SupportsGMLObjectTypeList'), 'SupportsGMLObjectTypeList', '__httpwww_opengis_netwfs_WFS_CapabilitiesType_httpwww_opengis_netwfsSupportsGMLObjectTypeList', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 392, 3), )

    
    SupportsGMLObjectTypeList = property(__SupportsGMLObjectTypeList.value, __SupportsGMLObjectTypeList.set, None, '\n            List of GML Object types that WFS is capable of serving, either\n            directly, or as validly derived types defined in a GML application\n            schema.\n         ')

    
    # Attribute version inherited from {http://www.opengis.net/ows}CapabilitiesBaseType
    
    # Attribute updateSequence inherited from {http://www.opengis.net/ows}CapabilitiesBaseType
    _ElementMap.update({
        __Filter_Capabilities.name() : __Filter_Capabilities,
        __FeatureTypeList.name() : __FeatureTypeList,
        __ServesGMLObjectTypeList.name() : __ServesGMLObjectTypeList,
        __SupportsGMLObjectTypeList.name() : __SupportsGMLObjectTypeList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.WFS_CapabilitiesType = WFS_CapabilitiesType
Namespace.addCategoryObject('typeBinding', 'WFS_CapabilitiesType', WFS_CapabilitiesType)


# Complex type {http://www.opengis.net/wfs}FeatureTypeListType with content type ELEMENT_ONLY
class FeatureTypeListType (pyxb.binding.basis.complexTypeDefinition):
    """
            A list of feature types available from  this server.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FeatureTypeListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 224, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wfs}Operations uses Python identifier Operations
    __Operations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Operations'), 'Operations', '__httpwww_opengis_netwfs_FeatureTypeListType_httpwww_opengis_netwfsOperations', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 231, 9), )

    
    Operations = property(__Operations.value, __Operations.set, None, None)

    
    # Element {http://www.opengis.net/wfs}FeatureType uses Python identifier FeatureType
    __FeatureType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FeatureType'), 'FeatureType', '__httpwww_opengis_netwfs_FeatureTypeListType_httpwww_opengis_netwfsFeatureType', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 234, 9), )

    
    FeatureType = property(__FeatureType.value, __FeatureType.set, None, None)

    _ElementMap.update({
        __Operations.name() : __Operations,
        __FeatureType.name() : __FeatureType
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FeatureTypeListType = FeatureTypeListType
Namespace.addCategoryObject('typeBinding', 'FeatureTypeListType', FeatureTypeListType)


# Complex type {http://www.opengis.net/wfs}FeatureTypeType with content type ELEMENT_ONLY
class FeatureTypeType (pyxb.binding.basis.complexTypeDefinition):
    """
            An element of this type that describes a feature in an application
            namespace shall have an xml xmlns specifier, e.g.
            xmlns:bo="http://www.BlueOx.org/BlueOx"
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FeatureTypeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 239, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}Keywords uses Python identifier Keywords
    __Keywords = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Keywords'), 'Keywords', '__httpwww_opengis_netwfs_FeatureTypeType_httpwww_opengis_netowsKeywords', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 36, 1), )

    
    Keywords = property(__Keywords.value, __Keywords.set, None, None)

    
    # Element {http://www.opengis.net/ows}WGS84BoundingBox uses Python identifier WGS84BoundingBox
    __WGS84BoundingBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'WGS84BoundingBox'), 'WGS84BoundingBox', '__httpwww_opengis_netwfs_FeatureTypeType_httpwww_opengis_netowsWGS84BoundingBox', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 111, 1), )

    
    WGS84BoundingBox = property(__WGS84BoundingBox.value, __WGS84BoundingBox.set, None, None)

    
    # Element {http://www.opengis.net/wfs}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_opengis_netwfs_FeatureTypeType_httpwww_opengis_netwfsName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 248, 9), )

    
    Name = property(__Name.value, __Name.set, None, '\n                  Name of this feature type, including any namespace prefix\n               ')

    
    # Element {http://www.opengis.net/wfs}Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Title'), 'Title', '__httpwww_opengis_netwfs_FeatureTypeType_httpwww_opengis_netwfsTitle', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 255, 9), )

    
    Title = property(__Title.value, __Title.set, None, '\n                  Title of this feature type, normally used for display\n                  to a human.\n               ')

    
    # Element {http://www.opengis.net/wfs}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Abstract'), 'Abstract', '__httpwww_opengis_netwfs_FeatureTypeType_httpwww_opengis_netwfsAbstract', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 263, 9), )

    
    Abstract = property(__Abstract.value, __Abstract.set, None, '\n                  Brief narrative description of this feature type, normally\n                  used for display to a human.\n               ')

    
    # Element {http://www.opengis.net/wfs}DefaultSRS uses Python identifier DefaultSRS
    __DefaultSRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DefaultSRS'), 'DefaultSRS', '__httpwww_opengis_netwfs_FeatureTypeType_httpwww_opengis_netwfsDefaultSRS', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 274, 15), )

    
    DefaultSRS = property(__DefaultSRS.value, __DefaultSRS.set, None, '\n                        The DefaultSRS element indicated which spatial\n                        reference system shall be used by a WFS to\n                        express the state of a spatial feature if not\n                        otherwise explicitly identified within a query\n                        or transaction request.  The SRS may be indicated\n                        using either the EPSG form (EPSG:posc code) or\n                        the URL form defined in subclause 4.3.2 of\n                        refernce[2].\n                     ')

    
    # Element {http://www.opengis.net/wfs}OtherSRS uses Python identifier OtherSRS
    __OtherSRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OtherSRS'), 'OtherSRS', '__httpwww_opengis_netwfs_FeatureTypeType_httpwww_opengis_netwfsOtherSRS', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 289, 15), )

    
    OtherSRS = property(__OtherSRS.value, __OtherSRS.set, None, '\n                        The OtherSRS element is used to indicate other \n                        supported SRSs within query and transaction \n                        operations.  A supported SRS means that the \n                        WFS supports the transformation of spatial\n                        properties between the OtherSRS and the internal\n                        storage SRS.  The effects of such transformations \n                        must be considered when determining and declaring \n                        the guaranteed data accuracy.\n                     ')

    
    # Element {http://www.opengis.net/wfs}NoSRS uses Python identifier NoSRS
    __NoSRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NoSRS'), 'NoSRS', '__httpwww_opengis_netwfs_FeatureTypeType_httpwww_opengis_netwfsNoSRS', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 306, 12), )

    
    NoSRS = property(__NoSRS.value, __NoSRS.set, None, None)

    
    # Element {http://www.opengis.net/wfs}Operations uses Python identifier Operations
    __Operations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Operations'), 'Operations', '__httpwww_opengis_netwfs_FeatureTypeType_httpwww_opengis_netwfsOperations', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 310, 9), )

    
    Operations = property(__Operations.value, __Operations.set, None, None)

    
    # Element {http://www.opengis.net/wfs}OutputFormats uses Python identifier OutputFormats
    __OutputFormats = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OutputFormats'), 'OutputFormats', '__httpwww_opengis_netwfs_FeatureTypeType_httpwww_opengis_netwfsOutputFormats', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 313, 9), )

    
    OutputFormats = property(__OutputFormats.value, __OutputFormats.set, None, None)

    
    # Element {http://www.opengis.net/wfs}MetadataURL uses Python identifier MetadataURL
    __MetadataURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MetadataURL'), 'MetadataURL', '__httpwww_opengis_netwfs_FeatureTypeType_httpwww_opengis_netwfsMetadataURL', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 318, 9), )

    
    MetadataURL = property(__MetadataURL.value, __MetadataURL.set, None, None)

    _ElementMap.update({
        __Keywords.name() : __Keywords,
        __WGS84BoundingBox.name() : __WGS84BoundingBox,
        __Name.name() : __Name,
        __Title.name() : __Title,
        __Abstract.name() : __Abstract,
        __DefaultSRS.name() : __DefaultSRS,
        __OtherSRS.name() : __OtherSRS,
        __NoSRS.name() : __NoSRS,
        __Operations.name() : __Operations,
        __OutputFormats.name() : __OutputFormats,
        __MetadataURL.name() : __MetadataURL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FeatureTypeType = FeatureTypeType
Namespace.addCategoryObject('typeBinding', 'FeatureTypeType', FeatureTypeType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 307, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {http://www.opengis.net/wfs}OperationsType with content type ELEMENT_ONLY
class OperationsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/wfs}OperationsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OperationsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 323, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wfs}Operation uses Python identifier Operation
    __Operation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Operation'), 'Operation', '__httpwww_opengis_netwfs_OperationsType_httpwww_opengis_netwfsOperation', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 325, 9), )

    
    Operation = property(__Operation.value, __Operation.set, None, None)

    _ElementMap.update({
        __Operation.name() : __Operation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OperationsType = OperationsType
Namespace.addCategoryObject('typeBinding', 'OperationsType', OperationsType)


# Complex type {http://www.opengis.net/wfs}OutputFormatListType with content type ELEMENT_ONLY
class OutputFormatListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/wfs}OutputFormatListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OutputFormatListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 340, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wfs}Format uses Python identifier Format
    __Format = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Format'), 'Format', '__httpwww_opengis_netwfs_OutputFormatListType_httpwww_opengis_netwfsFormat', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 342, 9), )

    
    Format = property(__Format.value, __Format.set, None, None)

    _ElementMap.update({
        __Format.name() : __Format
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OutputFormatListType = OutputFormatListType
Namespace.addCategoryObject('typeBinding', 'OutputFormatListType', OutputFormatListType)


# Complex type {http://www.opengis.net/wfs}GMLObjectTypeListType with content type ELEMENT_ONLY
class GMLObjectTypeListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/wfs}GMLObjectTypeListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GMLObjectTypeListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 402, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wfs}GMLObjectType uses Python identifier GMLObjectType
    __GMLObjectType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GMLObjectType'), 'GMLObjectType', '__httpwww_opengis_netwfs_GMLObjectTypeListType_httpwww_opengis_netwfsGMLObjectType', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 404, 9), )

    
    GMLObjectType = property(__GMLObjectType.value, __GMLObjectType.set, None, '\n                  Name of this GML object type, including any namespace prefix\n               ')

    _ElementMap.update({
        __GMLObjectType.name() : __GMLObjectType
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GMLObjectTypeListType = GMLObjectTypeListType
Namespace.addCategoryObject('typeBinding', 'GMLObjectTypeListType', GMLObjectTypeListType)


# Complex type {http://www.opengis.net/wfs}GMLObjectTypeType with content type ELEMENT_ONLY
class GMLObjectTypeType (pyxb.binding.basis.complexTypeDefinition):
    """
            An element of this type that describes a GML object in an
            application namespace shall have an xml xmlns specifier,
            e.g. xmlns:bo="http://www.BlueOx.org/BlueOx"
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GMLObjectTypeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 414, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows}Keywords uses Python identifier Keywords
    __Keywords = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Keywords'), 'Keywords', '__httpwww_opengis_netwfs_GMLObjectTypeType_httpwww_opengis_netowsKeywords', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 36, 1), )

    
    Keywords = property(__Keywords.value, __Keywords.set, None, None)

    
    # Element {http://www.opengis.net/wfs}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_opengis_netwfs_GMLObjectTypeType_httpwww_opengis_netwfsName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 423, 9), )

    
    Name = property(__Name.value, __Name.set, None, '\n                  Name of this GML Object type, including any namespace prefix.\n               ')

    
    # Element {http://www.opengis.net/wfs}Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Title'), 'Title', '__httpwww_opengis_netwfs_GMLObjectTypeType_httpwww_opengis_netwfsTitle', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 430, 9), )

    
    Title = property(__Title.value, __Title.set, None, '\n                  Title of this GML Object type, normally used for display\n                  to a human.\n               ')

    
    # Element {http://www.opengis.net/wfs}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Abstract'), 'Abstract', '__httpwww_opengis_netwfs_GMLObjectTypeType_httpwww_opengis_netwfsAbstract', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 438, 9), )

    
    Abstract = property(__Abstract.value, __Abstract.set, None, '\n                  Brief narrative description of this GML Object type, normally\n                  used for display to a human.\n               ')

    
    # Element {http://www.opengis.net/wfs}OutputFormats uses Python identifier OutputFormats
    __OutputFormats = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OutputFormats'), 'OutputFormats', '__httpwww_opengis_netwfs_GMLObjectTypeType_httpwww_opengis_netwfsOutputFormats', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 448, 9), )

    
    OutputFormats = property(__OutputFormats.value, __OutputFormats.set, None, None)

    _ElementMap.update({
        __Keywords.name() : __Keywords,
        __Name.name() : __Name,
        __Title.name() : __Title,
        __Abstract.name() : __Abstract,
        __OutputFormats.name() : __OutputFormats
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GMLObjectTypeType = GMLObjectTypeType
Namespace.addCategoryObject('typeBinding', 'GMLObjectTypeType', GMLObjectTypeType)


# Complex type {http://www.opengis.net/wfs}FeatureCollectionType with content type ELEMENT_ONLY
class FeatureCollectionType (pyxb.bundles.opengis.gml.AbstractFeatureCollectionType):
    """
            This type defines a container for the response to a 
            GetFeature or GetFeatureWithLock request.  If the
            request is GetFeatureWithLock, the lockId attribute
            must be populated.  The lockId attribute can otherwise
            be safely ignored.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FeatureCollectionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 846, 3)
    _ElementMap = pyxb.bundles.opengis.gml.AbstractFeatureCollectionType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml.AbstractFeatureCollectionType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml.AbstractFeatureCollectionType
    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element featureMember ({http://www.opengis.net/gml}featureMember) inherited from {http://www.opengis.net/gml}AbstractFeatureCollectionType
    
    # Element featureMembers ({http://www.opengis.net/gml}featureMembers) inherited from {http://www.opengis.net/gml}AbstractFeatureCollectionType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute lockId uses Python identifier lockId
    __lockId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lockId'), 'lockId', '__httpwww_opengis_netwfs_FeatureCollectionType_lockId', pyxb.binding.datatypes.string)
    __lockId._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 858, 9)
    __lockId._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 858, 9)
    
    lockId = property(__lockId.value, __lockId.set, None, '\n                  The value of the lockId attribute is an identifier\n                  that a Web Feature Service generates when responding\n                  to a GetFeatureWithLock request.  A client application\n                  can use this value in subsequent operations (such as a\n                  Transaction request) to reference the set of locked\n                  features.\n               ')

    
    # Attribute timeStamp uses Python identifier timeStamp
    __timeStamp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timeStamp'), 'timeStamp', '__httpwww_opengis_netwfs_FeatureCollectionType_timeStamp', pyxb.binding.datatypes.dateTime)
    __timeStamp._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 870, 9)
    __timeStamp._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 870, 9)
    
    timeStamp = property(__timeStamp.value, __timeStamp.set, None, '\n                  The timeStamp attribute should contain the date and time\n                  that the response was generated.\n               ')

    
    # Attribute numberOfFeatures uses Python identifier numberOfFeatures
    __numberOfFeatures = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numberOfFeatures'), 'numberOfFeatures', '__httpwww_opengis_netwfs_FeatureCollectionType_numberOfFeatures', pyxb.binding.datatypes.nonNegativeInteger)
    __numberOfFeatures._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 878, 9)
    __numberOfFeatures._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 878, 9)
    
    numberOfFeatures = property(__numberOfFeatures.value, __numberOfFeatures.set, None, '\n                  The numberOfFeatures attribute should contain a\n                  count of the number of features in the response.\n                  That is a count of all features elements dervied\n                  from gml:AbstractFeatureType.\n               ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lockId.name() : __lockId,
        __timeStamp.name() : __timeStamp,
        __numberOfFeatures.name() : __numberOfFeatures
    })
_module_typeBindings.FeatureCollectionType = FeatureCollectionType
Namespace.addCategoryObject('typeBinding', 'FeatureCollectionType', FeatureCollectionType)


# Complex type {http://www.opengis.net/wfs}LockType with content type ELEMENT_ONLY
class LockType (pyxb.binding.basis.complexTypeDefinition):
    """
            This type defines the Lock element.  The Lock element
            defines a locking operation on feature instances of 
            a single type. An OGC Filter is used to constrain the
            scope of the operation.  Features to be locked can be
            identified individually by using their feature identifier
            or they can be locked by satisfying the spatial and 
            non-spatial constraints defined in the filter.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LockType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1143, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter'), 'Filter', '__httpwww_opengis_netwfs_LockType_httpwww_opengis_netogcFilter', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 39, 3), )

    
    Filter = property(__Filter.value, __Filter.set, None, None)

    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'handle'), 'handle', '__httpwww_opengis_netwfs_LockType_handle', pyxb.binding.datatypes.string)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1158, 6)
    __handle._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1158, 6)
    
    handle = property(__handle.value, __handle.set, None, '\n               The handle attribute allows a client application\n               to assign a client-generated request identifier\n               to a Lock action.  The handle is included to \n               facilitate error reporting.  If one of a set of\n               Lock actions failed while processing a LockFeature\n               request, a WFS may report the handle in an exception\n               report to localize the error.  If a handle is not\n               present then a WFS may employ some other means of \n               localizing the error (e.g. line number).\n            ')

    
    # Attribute typeName uses Python identifier typeName
    __typeName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typeName'), 'typeName', '__httpwww_opengis_netwfs_LockType_typeName', pyxb.binding.datatypes.QName, required=True)
    __typeName._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1173, 6)
    __typeName._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1173, 6)
    
    typeName = property(__typeName.value, __typeName.set, None, '\n              The value of the typeName attribute is the name \n              of the feature type to be updated. The name\n              specified must be a valid type that belongs to\n              the feature content as defined by the GML\n              Application Schema.\n           ')

    _ElementMap.update({
        __Filter.name() : __Filter
    })
    _AttributeMap.update({
        __handle.name() : __handle,
        __typeName.name() : __typeName
    })
_module_typeBindings.LockType = LockType
Namespace.addCategoryObject('typeBinding', 'LockType', LockType)


# Complex type {http://www.opengis.net/wfs}LockFeatureResponseType with content type ELEMENT_ONLY
class LockFeatureResponseType (pyxb.binding.basis.complexTypeDefinition):
    """
            The LockFeatureResponseType is used to define an
            element to contains the response to a LockFeature
            operation.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LockFeatureResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1195, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wfs}FeaturesLocked uses Python identifier FeaturesLocked
    __FeaturesLocked = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FeaturesLocked'), 'FeaturesLocked', '__httpwww_opengis_netwfs_LockFeatureResponseType_httpwww_opengis_netwfsFeaturesLocked', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1214, 9), )

    
    FeaturesLocked = property(__FeaturesLocked.value, __FeaturesLocked.set, None, '\n                  The LockFeature or GetFeatureWithLock operations\n                  identify and attempt to lock a set of feature \n                  instances that satisfy the constraints specified \n                  in the request.  In the event that the lockAction\n                  attribute (on the LockFeature or GetFeatureWithLock\n                  elements) is set to SOME, a Web Feature Service will\n                  attempt to lock as many of the feature instances from\n                  the result set as possible.\n\n                  The FeaturesLocked element contains list of ogc:FeatureId\n                  elements enumerating the feature instances that a WFS\n                  actually managed to lock.\n               ')

    
    # Element {http://www.opengis.net/wfs}FeaturesNotLocked uses Python identifier FeaturesNotLocked
    __FeaturesNotLocked = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FeaturesNotLocked'), 'FeaturesNotLocked', '__httpwww_opengis_netwfs_LockFeatureResponseType_httpwww_opengis_netwfsFeaturesNotLocked', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1233, 9), )

    
    FeaturesNotLocked = property(__FeaturesNotLocked.value, __FeaturesNotLocked.set, None, '\n                  In contrast to the FeaturesLocked element, the\n                  FeaturesNotLocked element contains a list of \n                  ogc:Filter elements identifying feature instances\n                  that a WFS did not manage to lock because they were\n                  already locked by another process.\n               ')

    
    # Element {http://www.opengis.net/wfs}LockId uses Python identifier LockId
    __LockId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LockId'), 'LockId', '__httpwww_opengis_netwfs_LockFeatureResponseType_httpwww_opengis_netwfsLockId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1344, 3), )

    
    LockId = property(__LockId.value, __LockId.set, None, '\n            The LockId element contains the value of the lock identifier\n            obtained by a client application from a previous GetFeatureWithLock\n            or LockFeature request.\n         ')

    _ElementMap.update({
        __FeaturesLocked.name() : __FeaturesLocked,
        __FeaturesNotLocked.name() : __FeaturesNotLocked,
        __LockId.name() : __LockId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LockFeatureResponseType = LockFeatureResponseType
Namespace.addCategoryObject('typeBinding', 'LockFeatureResponseType', LockFeatureResponseType)


# Complex type {http://www.opengis.net/wfs}FeaturesLockedType with content type ELEMENT_ONLY
class FeaturesLockedType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/wfs}FeaturesLockedType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FeaturesLockedType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1247, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}FeatureId uses Python identifier FeatureId
    __FeatureId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'FeatureId'), 'FeatureId', '__httpwww_opengis_netwfs_FeaturesLockedType_httpwww_opengis_netogcFeatureId', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 32, 3), )

    
    FeatureId = property(__FeatureId.value, __FeatureId.set, None, None)

    _ElementMap.update({
        __FeatureId.name() : __FeatureId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FeaturesLockedType = FeaturesLockedType
Namespace.addCategoryObject('typeBinding', 'FeaturesLockedType', FeaturesLockedType)


# Complex type {http://www.opengis.net/wfs}FeaturesNotLockedType with content type ELEMENT_ONLY
class FeaturesNotLockedType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/wfs}FeaturesNotLockedType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FeaturesNotLockedType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1252, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}FeatureId uses Python identifier FeatureId
    __FeatureId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'FeatureId'), 'FeatureId', '__httpwww_opengis_netwfs_FeaturesNotLockedType_httpwww_opengis_netogcFeatureId', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 32, 3), )

    
    FeatureId = property(__FeatureId.value, __FeatureId.set, None, None)

    _ElementMap.update({
        __FeatureId.name() : __FeatureId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FeaturesNotLockedType = FeaturesNotLockedType
Namespace.addCategoryObject('typeBinding', 'FeaturesNotLockedType', FeaturesNotLockedType)


# Complex type {http://www.opengis.net/wfs}UpdateElementType with content type ELEMENT_ONLY
class UpdateElementType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/wfs}UpdateElementType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UpdateElementType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1477, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter'), 'Filter', '__httpwww_opengis_netwfs_UpdateElementType_httpwww_opengis_netogcFilter', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 39, 3), )

    
    Filter = property(__Filter.value, __Filter.set, None, None)

    
    # Element {http://www.opengis.net/wfs}Property uses Python identifier Property
    __Property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Property'), 'Property', '__httpwww_opengis_netwfs_UpdateElementType_httpwww_opengis_netwfsProperty', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1558, 3), )

    
    Property = property(__Property.value, __Property.set, None, '\n            The Property element is used to specify the new\n            value of a feature property inside an Update\n            element.\n         ')

    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'handle'), 'handle', '__httpwww_opengis_netwfs_UpdateElementType_handle', pyxb.binding.datatypes.string)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1508, 6)
    __handle._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1508, 6)
    
    handle = property(__handle.value, __handle.set, None, '\n               The handle attribute allows a client application\n               to assign a client-generated request identifier\n               to an Insert action.  The handle is included to\n               facilitate error reporting.  If an Update action\n               in a Transaction request fails, then a WFS may\n               include the handle in an exception report to localize\n               the error.  If no handle is included of the offending\n               Insert element then a WFS may employee other means of\n               localizing the error (e.g. line number).\n            ')

    
    # Attribute typeName uses Python identifier typeName
    __typeName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typeName'), 'typeName', '__httpwww_opengis_netwfs_UpdateElementType_typeName', pyxb.binding.datatypes.QName, required=True)
    __typeName._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1523, 6)
    __typeName._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1523, 6)
    
    typeName = property(__typeName.value, __typeName.set, None, '\n              The value of the typeName attribute is the name \n              of the feature type to be updated. The name\n              specified must be a valid type that belongs to\n              the feature content as defined by the GML\n              Application Schema.\n           ')

    
    # Attribute inputFormat uses Python identifier inputFormat
    __inputFormat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'inputFormat'), 'inputFormat', '__httpwww_opengis_netwfs_UpdateElementType_inputFormat', pyxb.binding.datatypes.string, unicode_default='x-application/gml:3')
    __inputFormat._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1534, 6)
    __inputFormat._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1534, 6)
    
    inputFormat = property(__inputFormat.value, __inputFormat.set, None, "\n               This inputFormat attribute is used to indicate \n               the format used to encode a feature instance in\n               an Insert element.  The default value of\n               'text/xml; subtype=gml/3.1.1' is used to indicate\n               that feature encoding is GML3.  Another example\n               might be 'text/xml; subtype=gml/2.1.2' indicating\n               that the feature us encoded in GML2.  A WFS must\n               declare in the capabilities document, using a \n               Parameter element, which version of GML it supports.\n            ")

    
    # Attribute srsName uses Python identifier srsName
    __srsName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'srsName'), 'srsName', '__httpwww_opengis_netwfs_UpdateElementType_srsName', pyxb.binding.datatypes.anyURI)
    __srsName._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1550, 6)
    __srsName._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1550, 6)
    
    srsName = property(__srsName.value, __srsName.set, None, '\n               DO WE NEED THIS HERE?\n           ')

    _ElementMap.update({
        __Filter.name() : __Filter,
        __Property.name() : __Property
    })
    _AttributeMap.update({
        __handle.name() : __handle,
        __typeName.name() : __typeName,
        __inputFormat.name() : __inputFormat,
        __srsName.name() : __srsName
    })
_module_typeBindings.UpdateElementType = UpdateElementType
Namespace.addCategoryObject('typeBinding', 'UpdateElementType', UpdateElementType)


# Complex type {http://www.opengis.net/wfs}PropertyType with content type ELEMENT_ONLY
class PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/wfs}PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1567, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wfs}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httpwww_opengis_netwfs_PropertyType_httpwww_opengis_netwfsName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1569, 9), )

    
    Name = property(__Name.value, __Name.set, None, '\n                  The Name element contains the name of a feature property\n                  to be updated.\n               ')

    
    # Element {http://www.opengis.net/wfs}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Value'), 'Value', '__httpwww_opengis_netwfs_PropertyType_httpwww_opengis_netwfsValue', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1577, 9), )

    
    Value = property(__Value.value, __Value.set, None, '\n                  The Value element contains the replacement value for the\n                  named property.\n               ')

    _ElementMap.update({
        __Name.name() : __Name,
        __Value.name() : __Value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PropertyType = PropertyType
Namespace.addCategoryObject('typeBinding', 'PropertyType', PropertyType)


# Complex type {http://www.opengis.net/wfs}DeleteElementType with content type ELEMENT_ONLY
class DeleteElementType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/wfs}DeleteElementType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeleteElementType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1596, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter'), 'Filter', '__httpwww_opengis_netwfs_DeleteElementType_httpwww_opengis_netogcFilter', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 39, 3), )

    
    Filter = property(__Filter.value, __Filter.set, None, None)

    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'handle'), 'handle', '__httpwww_opengis_netwfs_DeleteElementType_handle', pyxb.binding.datatypes.string)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1615, 6)
    __handle._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1615, 6)
    
    handle = property(__handle.value, __handle.set, None, '\n               The handle attribute allows a client application\n               to assign a client-generated request identifier\n               to an Insert action.  The handle is included to\n               facilitate error reporting.  If a Delete action\n               in a Transaction request fails, then a WFS may\n               include the handle in an exception report to localize\n               the error.  If no handle is included of the offending\n               Insert element then a WFS may employee other means of\n               localizing the error (e.g. line number).\n            ')

    
    # Attribute typeName uses Python identifier typeName
    __typeName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typeName'), 'typeName', '__httpwww_opengis_netwfs_DeleteElementType_typeName', pyxb.binding.datatypes.QName, required=True)
    __typeName._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1630, 6)
    __typeName._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1630, 6)
    
    typeName = property(__typeName.value, __typeName.set, None, '\n              The value of the typeName attribute is the name \n              of the feature type to be updated. The name\n              specified must be a valid type that belongs to\n              the feature content as defined by the GML\n              Application Schema.\n           ')

    _ElementMap.update({
        __Filter.name() : __Filter
    })
    _AttributeMap.update({
        __handle.name() : __handle,
        __typeName.name() : __typeName
    })
_module_typeBindings.DeleteElementType = DeleteElementType
Namespace.addCategoryObject('typeBinding', 'DeleteElementType', DeleteElementType)


# Complex type {http://www.opengis.net/wfs}NativeType with content type EMPTY
class NativeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/wfs}NativeType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NativeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1652, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute vendorId uses Python identifier vendorId
    __vendorId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vendorId'), 'vendorId', '__httpwww_opengis_netwfs_NativeType_vendorId', pyxb.binding.datatypes.string, required=True)
    __vendorId._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1653, 6)
    __vendorId._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1653, 6)
    
    vendorId = property(__vendorId.value, __vendorId.set, None, "\n               The vendorId attribute is used to specify the name of\n               vendor who's vendor specific command the client\n               application wishes to execute.\n            ")

    
    # Attribute safeToIgnore uses Python identifier safeToIgnore
    __safeToIgnore = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'safeToIgnore'), 'safeToIgnore', '__httpwww_opengis_netwfs_NativeType_safeToIgnore', pyxb.binding.datatypes.boolean, required=True)
    __safeToIgnore._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1662, 6)
    __safeToIgnore._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1662, 6)
    
    safeToIgnore = property(__safeToIgnore.value, __safeToIgnore.set, None, '\n               In the event that a Web Feature Service does not recognize\n               the vendorId or does not recognize the vendor specific command,\n               the safeToIgnore attribute is used to indicate whether the \n               exception can be safely ignored.  A value of TRUE means that\n               the Web Feature Service may ignore the command.  A value of\n               FALSE means that a Web Feature Service cannot ignore the\n               command and an exception should be raised if a problem is \n               encountered.\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __vendorId.name() : __vendorId,
        __safeToIgnore.name() : __safeToIgnore
    })
_module_typeBindings.NativeType = NativeType
Namespace.addCategoryObject('typeBinding', 'NativeType', NativeType)


# Complex type {http://www.opengis.net/wfs}TransactionResponseType with content type ELEMENT_ONLY
class TransactionResponseType (pyxb.binding.basis.complexTypeDefinition):
    """
            The response for a transaction request that was successfully
            completed. If the transaction failed for any reason, an
            exception report is returned instead.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TransactionResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1687, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wfs}TransactionSummary uses Python identifier TransactionSummary
    __TransactionSummary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TransactionSummary'), 'TransactionSummary', '__httpwww_opengis_netwfs_TransactionResponseType_httpwww_opengis_netwfsTransactionSummary', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1696, 9), )

    
    TransactionSummary = property(__TransactionSummary.value, __TransactionSummary.set, None, '\n                  The TransactionSummary element is used to summarize\n                  the number of feature instances affected by the \n                  transaction.\n               ')

    
    # Element {http://www.opengis.net/wfs}TransactionResults uses Python identifier TransactionResults
    __TransactionResults = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TransactionResults'), 'TransactionResults', '__httpwww_opengis_netwfs_TransactionResponseType_httpwww_opengis_netwfsTransactionResults', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1706, 9), )

    
    TransactionResults = property(__TransactionResults.value, __TransactionResults.set, None, '\n                  For systems that do not support atomic transactions,\n                  the TransactionResults element may be used to report\n                  exception codes and messages for all actions of a\n                  transaction that failed to execute successfully.\n               ')

    
    # Element {http://www.opengis.net/wfs}InsertResults uses Python identifier InsertResults
    __InsertResults = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InsertResults'), 'InsertResults', '__httpwww_opengis_netwfs_TransactionResponseType_httpwww_opengis_netwfsInsertResults', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1718, 9), )

    
    InsertResults = property(__InsertResults.value, __InsertResults.set, None, '\n                  A transaction is a collection of Insert,Update and Delete\n                  actions.  The Update and Delete actions modify features\n                  that already exist.  The Insert action, however, creates\n                  new features.  The InsertResults element is used to\n                  report the identifiers of the newly created features.\n               ')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netwfs_TransactionResponseType_version', pyxb.binding.datatypes.string, fixed=True, unicode_default='1.1.0', required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1732, 6)
    __version._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1732, 6)
    
    version = property(__version.value, __version.set, None, '\n               The version attribute contains the version of the request\n               that generated this response.  So a V1.1.0 transaction\n               request generates a V1.1.0 transaction response.\n            ')

    _ElementMap.update({
        __TransactionSummary.name() : __TransactionSummary,
        __TransactionResults.name() : __TransactionResults,
        __InsertResults.name() : __InsertResults
    })
    _AttributeMap.update({
        __version.name() : __version
    })
_module_typeBindings.TransactionResponseType = TransactionResponseType
Namespace.addCategoryObject('typeBinding', 'TransactionResponseType', TransactionResponseType)


# Complex type {http://www.opengis.net/wfs}TransactionSummaryType with content type ELEMENT_ONLY
class TransactionSummaryType (pyxb.binding.basis.complexTypeDefinition):
    """
            Reports the total number of features affected by some kind 
            of write action (i.e, insert, update, delete).
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TransactionSummaryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1743, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wfs}totalInserted uses Python identifier totalInserted
    __totalInserted = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'totalInserted'), 'totalInserted', '__httpwww_opengis_netwfs_TransactionSummaryType_httpwww_opengis_netwfstotalInserted', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1751, 9), )

    
    totalInserted = property(__totalInserted.value, __totalInserted.set, None, None)

    
    # Element {http://www.opengis.net/wfs}totalUpdated uses Python identifier totalUpdated
    __totalUpdated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'totalUpdated'), 'totalUpdated', '__httpwww_opengis_netwfs_TransactionSummaryType_httpwww_opengis_netwfstotalUpdated', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1754, 9), )

    
    totalUpdated = property(__totalUpdated.value, __totalUpdated.set, None, None)

    
    # Element {http://www.opengis.net/wfs}totalDeleted uses Python identifier totalDeleted
    __totalDeleted = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'totalDeleted'), 'totalDeleted', '__httpwww_opengis_netwfs_TransactionSummaryType_httpwww_opengis_netwfstotalDeleted', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1757, 9), )

    
    totalDeleted = property(__totalDeleted.value, __totalDeleted.set, None, None)

    _ElementMap.update({
        __totalInserted.name() : __totalInserted,
        __totalUpdated.name() : __totalUpdated,
        __totalDeleted.name() : __totalDeleted
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TransactionSummaryType = TransactionSummaryType
Namespace.addCategoryObject('typeBinding', 'TransactionSummaryType', TransactionSummaryType)


# Complex type {http://www.opengis.net/wfs}TransactionResultsType with content type ELEMENT_ONLY
class TransactionResultsType (pyxb.binding.basis.complexTypeDefinition):
    """
            The TransactionResults element may be used to report exception
            codes and messages for all actions of a transaction that failed
            to complete successfully.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TransactionResultsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1762, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wfs}Action uses Python identifier Action
    __Action = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Action'), 'Action', '__httpwww_opengis_netwfs_TransactionResultsType_httpwww_opengis_netwfsAction', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1771, 9), )

    
    Action = property(__Action.value, __Action.set, None, '\n                  The Action element reports an exception code\n                  and exception message indicating why the\n                  corresponding action of a transaction request\n                  failed.\n               ')

    _ElementMap.update({
        __Action.name() : __Action
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TransactionResultsType = TransactionResultsType
Namespace.addCategoryObject('typeBinding', 'TransactionResultsType', TransactionResultsType)


# Complex type {http://www.opengis.net/wfs}ActionType with content type ELEMENT_ONLY
class ActionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/wfs}ActionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1784, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wfs}Message uses Python identifier Message
    __Message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Message'), 'Message', '__httpwww_opengis_netwfs_ActionType_httpwww_opengis_netwfsMessage', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1786, 9), )

    
    Message = property(__Message.value, __Message.set, None, '\n                  If an action fails, the message element may be used\n                  to supply an exception message.\n               ')

    
    # Attribute locator uses Python identifier locator
    __locator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'locator'), 'locator', '__httpwww_opengis_netwfs_ActionType_locator', pyxb.binding.datatypes.string, required=True)
    __locator._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1796, 6)
    __locator._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1796, 6)
    
    locator = property(__locator.value, __locator.set, None, '\n               The locator attribute is used to locate an action \n               within a <Transaction> element.  The value\n               of the locator attribute is either a string that\n               is equal to the value of the handle attribute\n               specified on an  <Insert>, <Update>\n               or <Delete> action.  If a value is not \n               specified for the handle attribute then a WFS \n               may employ some other means of locating the \n               action.  For example, the value of the locator\n               attribute may be an integer indicating the order\n               of the action (i.e. 1=First action, 2=Second action,\n               etc.).\n            ')

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__httpwww_opengis_netwfs_ActionType_code', pyxb.binding.datatypes.string)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1814, 6)
    __code._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1814, 6)
    
    code = property(__code.value, __code.set, None, '\n               The code attribute may be used to specify an \n               exception code indicating why an action failed.\n            ')

    _ElementMap.update({
        __Message.name() : __Message
    })
    _AttributeMap.update({
        __locator.name() : __locator,
        __code.name() : __code
    })
_module_typeBindings.ActionType = ActionType
Namespace.addCategoryObject('typeBinding', 'ActionType', ActionType)


# Complex type {http://www.opengis.net/wfs}InsertResultsType with content type ELEMENT_ONLY
class InsertResultsType (pyxb.binding.basis.complexTypeDefinition):
    """
            Reports the list of identifiers of all features created 
            by a transaction request.  New features are created using
            the Insert action and the list of idetifiers must be 
            presented in the same order as the Insert actions were
            encountered in the transaction request.  Features may
            optionally be correlated with identifiers using the 
            handle attribute (if it was specified on the Insert 
            element).
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InsertResultsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1823, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wfs}Feature uses Python identifier Feature
    __Feature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Feature'), 'Feature', '__httpwww_opengis_netwfs_InsertResultsType_httpwww_opengis_netwfsFeature', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1837, 9), )

    
    Feature = property(__Feature.value, __Feature.set, None, None)

    _ElementMap.update({
        __Feature.name() : __Feature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InsertResultsType = InsertResultsType
Namespace.addCategoryObject('typeBinding', 'InsertResultsType', InsertResultsType)


# Complex type {http://www.opengis.net/wfs}InsertedFeatureType with content type ELEMENT_ONLY
class InsertedFeatureType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/wfs}InsertedFeatureType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InsertedFeatureType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1842, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}FeatureId uses Python identifier FeatureId
    __FeatureId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'FeatureId'), 'FeatureId', '__httpwww_opengis_netwfs_InsertedFeatureType_httpwww_opengis_netogcFeatureId', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 32, 3), )

    
    FeatureId = property(__FeatureId.value, __FeatureId.set, None, None)

    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'handle'), 'handle', '__httpwww_opengis_netwfs_InsertedFeatureType_handle', pyxb.binding.datatypes.string)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1856, 6)
    __handle._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1856, 6)
    
    handle = property(__handle.value, __handle.set, None, '\n               If the insert element that generated this feature \n               had a value for the "handle" attribute then a WFS\n               may report it using this attribute to correlate\n               the feature created with the action that created it.\n            ')

    _ElementMap.update({
        __FeatureId.name() : __FeatureId
    })
    _AttributeMap.update({
        __handle.name() : __handle
    })
_module_typeBindings.InsertedFeatureType = InsertedFeatureType
Namespace.addCategoryObject('typeBinding', 'InsertedFeatureType', InsertedFeatureType)


# Complex type {http://www.opengis.net/wfs}MetadataURLType with content type SIMPLE
class MetadataURLType (pyxb.binding.basis.complexTypeDefinition):
    """
            A Web Feature Server MAY use zero or more MetadataURL
            elements to offer detailed, standardized metadata about
            the data underneath a particular feature type.  The type
            attribute indicates the standard to which the metadata
            complies; the format attribute indicates how the metadata is
            structured.  Two types are defined at present:
            'TC211' or 'ISO19115' = ISO TC211 19115; 
            'FGDC'                = FGDC CSDGM.
            'ISO19139'            = ISO 19139
         """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MetadataURLType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 345, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_opengis_netwfs_MetadataURLType_type', _module_typeBindings.STD_ANON, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 361, 12)
    __type._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 361, 12)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'format'), 'format', '__httpwww_opengis_netwfs_MetadataURLType_format', _module_typeBindings.STD_ANON_, required=True)
    __format._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 371, 12)
    __format._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 371, 12)
    
    format = property(__format.value, __format.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __format.name() : __format
    })
_module_typeBindings.MetadataURLType = MetadataURLType
Namespace.addCategoryObject('typeBinding', 'MetadataURLType', MetadataURLType)


# Complex type {http://www.opengis.net/wfs}DescribeFeatureTypeType with content type ELEMENT_ONLY
class DescribeFeatureTypeType (BaseRequestType):
    """
            The DescribeFeatureType operation allows a client application
            to request that a Web Feature Service describe one or more
            feature types.   A Web Feature Service must be able to generate
            feature descriptions as valid GML3 application schemas.

            The schemas generated by the DescribeFeatureType operation can
            be used by a client application to validate the output.

            Feature instances within the WFS interface must be specified
            using GML3.  The schema of feature instances specified within
            the WFS interface must validate against the feature schemas 
            generated by the DescribeFeatureType request.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DescribeFeatureTypeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 466, 3)
    _ElementMap = BaseRequestType._ElementMap.copy()
    _AttributeMap = BaseRequestType._AttributeMap.copy()
    # Base type is BaseRequestType
    
    # Element {http://www.opengis.net/wfs}TypeName uses Python identifier TypeName
    __TypeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TypeName'), 'TypeName', '__httpwww_opengis_netwfs_DescribeFeatureTypeType_httpwww_opengis_netwfsTypeName', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 486, 15), )

    
    TypeName = property(__TypeName.value, __TypeName.set, None, '\n                        The TypeName element is used to enumerate the\n                        feature types to be described.  If no TypeName\n                        elements are specified then all features should\n                        be described.  The name must be a valid type\n                        that belongs to the feature content as defined\n                        by the GML Application Schema.\n                     ')

    
    # Attribute service inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute version inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute handle inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute outputFormat uses Python identifier outputFormat
    __outputFormat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'outputFormat'), 'outputFormat', '__httpwww_opengis_netwfs_DescribeFeatureTypeType_outputFormat', pyxb.binding.datatypes.string, unicode_default='text/xml; subtype=gml/3.1.1')
    __outputFormat._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 500, 12)
    __outputFormat._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 500, 12)
    
    outputFormat = property(__outputFormat.value, __outputFormat.set, None, "\n                     The outputFormat attribute is used to specify what schema\n                     description language should be used to describe features.\n                     The default value of 'text/xml; subtype=3.1.1' means that\n                     the WFS must generate a GML3 application schema that can\n                     be used to validate the GML3 output of a GetFeature\n                     request or feature instances specified in Transaction\n                     operations.\n                     For the purposes of experimentation, vendor extension,\n                     or even extensions that serve a specific community of\n                     interest, other acceptable output format values may be\n                     advertised by a WFS service in the capabilities document.\n                     The meaning of such values in not defined in the WFS \n                     specification.  The only proviso is such cases is that\n                     clients may safely ignore outputFormat values that do\n                     not recognize.\n                  ")

    _ElementMap.update({
        __TypeName.name() : __TypeName
    })
    _AttributeMap.update({
        __outputFormat.name() : __outputFormat
    })
_module_typeBindings.DescribeFeatureTypeType = DescribeFeatureTypeType
Namespace.addCategoryObject('typeBinding', 'DescribeFeatureTypeType', DescribeFeatureTypeType)


# Complex type {http://www.opengis.net/wfs}GetFeatureType with content type ELEMENT_ONLY
class GetFeatureType (BaseRequestType):
    """
            A GetFeature element contains one or more Query elements
            that describe a query operation on one feature type.  In
            response to a GetFeature request, a Web Feature Service
            must be able to generate a GML3 response that validates
            using a schema generated by the DescribeFeatureType request.
            A Web Feature Service may support other possibly non-XML
            (and even binary) output formats as long as those formats
            are advertised in the capabilities document.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetFeatureType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 545, 3)
    _ElementMap = BaseRequestType._ElementMap.copy()
    _AttributeMap = BaseRequestType._AttributeMap.copy()
    # Base type is BaseRequestType
    
    # Element {http://www.opengis.net/wfs}Query uses Python identifier Query
    __Query = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Query'), 'Query', '__httpwww_opengis_netwfs_GetFeatureType_httpwww_opengis_netwfsQuery', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 680, 3), )

    
    Query = property(__Query.value, __Query.set, None, '\n            The Query element is used to describe a single query.\n            One or more Query elements can be specified inside a\n            GetFeature element so that multiple queries can be \n            executed in one request.  The output from the various\n            queries are combined in a wfs:FeatureCollection element\n            to form the response document.\n         ')

    
    # Attribute service inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute version inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute handle inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute resultType uses Python identifier resultType
    __resultType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'resultType'), 'resultType', '__httpwww_opengis_netwfs_GetFeatureType_resultType', _module_typeBindings.ResultTypeType, unicode_default='results')
    __resultType._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 563, 12)
    __resultType._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 563, 12)
    
    resultType = property(__resultType.value, __resultType.set, None, '\n                     The resultType attribute is used to indicate\n                     what response a WFS should return to user once\n                     a GetFeature request is processed.\n                     Possible values are:\n                        results - meaning that the full response set\n                                  (i.e. all the feature instances) \n                                  should be returned.\n                        hits    - meaning that an empty response set\n                                  should be returned (i.e. no feature\n                                  instances should be returned) but\n                                  the "numberOfFeatures" attribute\n                                  should be set to the number of feature\n                                  instances that would be returned.\n                  ')

    
    # Attribute outputFormat uses Python identifier outputFormat
    __outputFormat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'outputFormat'), 'outputFormat', '__httpwww_opengis_netwfs_GetFeatureType_outputFormat', pyxb.binding.datatypes.string, unicode_default='text/xml; subtype=gml/3.1.1')
    __outputFormat._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 584, 12)
    __outputFormat._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 584, 12)
    
    outputFormat = property(__outputFormat.value, __outputFormat.set, None, "\n                     The outputFormat attribute is used to specify the output\n                     format that the Web Feature Service should generate in\n                     response to a GetFeature or GetFeatureWithLock element.\n                     The default value of 'text/xml; subtype=gml/3.1.1'\n                     indicates that the output is an XML document that\n                     conforms to the Geography Markup Language (GML)\n                     Implementation Specification V3.1.1.\n                     For the purposes of experimentation, vendor extension,\n                     or even extensions that serve a specific community of\n                     interest, other acceptable output format values may be\n                     used to specify other formats as long as those values\n                     are advertised in the capabilities document.\n                     For example, the value WKB may be used to indicate that a \n                     Well Known Binary format be used to encode the output.\n                  ")

    
    # Attribute maxFeatures uses Python identifier maxFeatures
    __maxFeatures = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxFeatures'), 'maxFeatures', '__httpwww_opengis_netwfs_GetFeatureType_maxFeatures', pyxb.binding.datatypes.positiveInteger)
    __maxFeatures._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 606, 12)
    __maxFeatures._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 606, 12)
    
    maxFeatures = property(__maxFeatures.value, __maxFeatures.set, None, '\n                     The maxFeatures attribute is used to specify the maximum\n                     number of features that a GetFeature operation should\n                     generate (regardless of the actual number of query hits).\n                  ')

    
    # Attribute traverseXlinkDepth uses Python identifier traverseXlinkDepth
    __traverseXlinkDepth = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'traverseXlinkDepth'), 'traverseXlinkDepth', '__httpwww_opengis_netwfs_GetFeatureType_traverseXlinkDepth', pyxb.binding.datatypes.string)
    __traverseXlinkDepth._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 616, 12)
    __traverseXlinkDepth._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 616, 12)
    
    traverseXlinkDepth = property(__traverseXlinkDepth.value, __traverseXlinkDepth.set, None, '\n                     This attribute indicates the depth to which nested property\n                     XLink linking element locator attribute (href) XLinks are\n                     traversed and resolved if possible.  A value of "1"\n                     indicates that one linking element locator attribute\n                     (href) Xlink will be traversed and the referenced element\n                     returned if possible, but nested property XLink linking\n                     element locator attribute (href) XLinks in the returned\n                     element are not traversed.  A value of "*" indicates that\n                     all nested property XLink linking element locator attribute\n                     (href) XLinks will be traversed and the referenced elements\n                     returned if possible.  The range of valid values for this\n                     attribute consists of positive integers plus "*".\n                     If this attribute is not specified then no xlinks shall be \n                     resolved and the value of traverseXlinkExpiry attribute (if\n                     it specified) may be ignored.\n                  ')

    
    # Attribute traverseXlinkExpiry uses Python identifier traverseXlinkExpiry
    __traverseXlinkExpiry = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'traverseXlinkExpiry'), 'traverseXlinkExpiry', '__httpwww_opengis_netwfs_GetFeatureType_traverseXlinkExpiry', pyxb.binding.datatypes.positiveInteger)
    __traverseXlinkExpiry._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 638, 12)
    __traverseXlinkExpiry._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 638, 12)
    
    traverseXlinkExpiry = property(__traverseXlinkExpiry.value, __traverseXlinkExpiry.set, None, '\n                     The traverseXlinkExpiry attribute value is specified in\n                     minutes.  It indicates how long a Web Feature Service\n                     should wait to receive a response to a nested GetGmlObject\n                     request.\t\n                     This attribute is only relevant if a value is specified \n                     for the traverseXlinkDepth attribute.\n                  ')

    _ElementMap.update({
        __Query.name() : __Query
    })
    _AttributeMap.update({
        __resultType.name() : __resultType,
        __outputFormat.name() : __outputFormat,
        __maxFeatures.name() : __maxFeatures,
        __traverseXlinkDepth.name() : __traverseXlinkDepth,
        __traverseXlinkExpiry.name() : __traverseXlinkExpiry
    })
_module_typeBindings.GetFeatureType = GetFeatureType
Namespace.addCategoryObject('typeBinding', 'GetFeatureType', GetFeatureType)


# Complex type {http://www.opengis.net/wfs}GetGmlObjectType with content type ELEMENT_ONLY
class GetGmlObjectType (BaseRequestType):
    """
            A GetGmlObjectType element contains exactly one GmlObjectId.  
            The value of the gml:id attribute on that GmlObjectId is used 
            as a unique key to retrieve the complex element with a 
            gml:id attribute with the same value.  
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetGmlObjectType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 906, 3)
    _ElementMap = BaseRequestType._ElementMap.copy()
    _AttributeMap = BaseRequestType._AttributeMap.copy()
    # Base type is BaseRequestType
    
    # Element {http://www.opengis.net/ogc}GmlObjectId uses Python identifier GmlObjectId
    __GmlObjectId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'GmlObjectId'), 'GmlObjectId', '__httpwww_opengis_netwfs_GetGmlObjectType_httpwww_opengis_netogcGmlObjectId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 35, 3), )

    
    GmlObjectId = property(__GmlObjectId.value, __GmlObjectId.set, None, None)

    
    # Attribute service inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute version inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute handle inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute outputFormat uses Python identifier outputFormat
    __outputFormat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'outputFormat'), 'outputFormat', '__httpwww_opengis_netwfs_GetGmlObjectType_outputFormat', pyxb.binding.datatypes.string, unicode_default='GML3')
    __outputFormat._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 920, 12)
    __outputFormat._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 920, 12)
    
    outputFormat = property(__outputFormat.value, __outputFormat.set, None, None)

    
    # Attribute traverseXlinkDepth uses Python identifier traverseXlinkDepth
    __traverseXlinkDepth = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'traverseXlinkDepth'), 'traverseXlinkDepth', '__httpwww_opengis_netwfs_GetGmlObjectType_traverseXlinkDepth', pyxb.binding.datatypes.string, required=True)
    __traverseXlinkDepth._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 922, 12)
    __traverseXlinkDepth._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 922, 12)
    
    traverseXlinkDepth = property(__traverseXlinkDepth.value, __traverseXlinkDepth.set, None, '\n                     This attribute indicates the depth to which nested\n                     property XLink linking element locator attribute\n                     (href) XLinks are traversed and resolved if possible.\n                     A value of "1" indicates that one linking element\n                     locator attribute (href) XLink will be traversed\n                     and the referenced element returned if possible, but\n                     nested property XLink linking element locator attribute\n                     (href) XLinks in the returned element are not traversed.\n                     A value of "*" indicates that all nested property XLink\n                     linking element locator attribute (href) XLinks will be\n                     traversed and the referenced elements returned if\n                     possible.  The range of valid values for this attribute\n                     consists of positive integers plus "*".\n                  ')

    
    # Attribute traverseXlinkExpiry uses Python identifier traverseXlinkExpiry
    __traverseXlinkExpiry = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'traverseXlinkExpiry'), 'traverseXlinkExpiry', '__httpwww_opengis_netwfs_GetGmlObjectType_traverseXlinkExpiry', pyxb.binding.datatypes.positiveInteger)
    __traverseXlinkExpiry._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 942, 12)
    __traverseXlinkExpiry._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 942, 12)
    
    traverseXlinkExpiry = property(__traverseXlinkExpiry.value, __traverseXlinkExpiry.set, None, '\n                     The traverseXlinkExpiry attribute value is specified\n                     in minutes.  It indicates how long a Web Feature Service\n                     should wait to receive a response to a nested GetGmlObject\n                     request.\t\n                  ')

    _ElementMap.update({
        __GmlObjectId.name() : __GmlObjectId
    })
    _AttributeMap.update({
        __outputFormat.name() : __outputFormat,
        __traverseXlinkDepth.name() : __traverseXlinkDepth,
        __traverseXlinkExpiry.name() : __traverseXlinkExpiry
    })
_module_typeBindings.GetGmlObjectType = GetGmlObjectType
Namespace.addCategoryObject('typeBinding', 'GetGmlObjectType', GetGmlObjectType)


# Complex type {http://www.opengis.net/wfs}GetFeatureWithLockType with content type ELEMENT_ONLY
class GetFeatureWithLockType (BaseRequestType):
    """
            A GetFeatureWithLock request operates identically to a
            GetFeature request expect that it attempts to lock the
            feature instances in the result set and includes a lock
            identifier in its response to a client.  A lock identifier
            is an identifier generated by a Web Feature Service that 
            a client application can use, in subsequent operations,
            to reference the locked set of feature instances.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetFeatureWithLockType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 981, 3)
    _ElementMap = BaseRequestType._ElementMap.copy()
    _AttributeMap = BaseRequestType._AttributeMap.copy()
    # Base type is BaseRequestType
    
    # Element {http://www.opengis.net/wfs}Query uses Python identifier Query
    __Query = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Query'), 'Query', '__httpwww_opengis_netwfs_GetFeatureWithLockType_httpwww_opengis_netwfsQuery', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 680, 3), )

    
    Query = property(__Query.value, __Query.set, None, '\n            The Query element is used to describe a single query.\n            One or more Query elements can be specified inside a\n            GetFeature element so that multiple queries can be \n            executed in one request.  The output from the various\n            queries are combined in a wfs:FeatureCollection element\n            to form the response document.\n         ')

    
    # Attribute service inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute version inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute handle inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute expiry uses Python identifier expiry
    __expiry = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'expiry'), 'expiry', '__httpwww_opengis_netwfs_GetFeatureWithLockType_expiry', pyxb.binding.datatypes.positiveInteger, unicode_default='5')
    __expiry._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 998, 12)
    __expiry._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 998, 12)
    
    expiry = property(__expiry.value, __expiry.set, None, '\n                     The expiry attribute is used to set the length\n                     of time (expressed in minutes) that features will\n                     remain locked as a result of a GetFeatureWithLock\n                     request.  After the expiry period elapses, the\n                     locked resources must be released.  If the \n                     expiry attribute is not set, then the default\n                     value of 5 minutes will be enforced.\n                  ')

    
    # Attribute resultType uses Python identifier resultType
    __resultType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'resultType'), 'resultType', '__httpwww_opengis_netwfs_GetFeatureWithLockType_resultType', _module_typeBindings.ResultTypeType, unicode_default='results')
    __resultType._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1013, 12)
    __resultType._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1013, 12)
    
    resultType = property(__resultType.value, __resultType.set, None, '\n                     See definition of wfs:GetFeatureType.\n                  ')

    
    # Attribute outputFormat uses Python identifier outputFormat
    __outputFormat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'outputFormat'), 'outputFormat', '__httpwww_opengis_netwfs_GetFeatureWithLockType_outputFormat', pyxb.binding.datatypes.string, unicode_default='text/xml; subtype=gml/3.1.1')
    __outputFormat._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1022, 12)
    __outputFormat._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1022, 12)
    
    outputFormat = property(__outputFormat.value, __outputFormat.set, None, '\n                     See definition of wfs:GetFeatureType.\n                  ')

    
    # Attribute maxFeatures uses Python identifier maxFeatures
    __maxFeatures = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxFeatures'), 'maxFeatures', '__httpwww_opengis_netwfs_GetFeatureWithLockType_maxFeatures', pyxb.binding.datatypes.positiveInteger)
    __maxFeatures._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1031, 12)
    __maxFeatures._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1031, 12)
    
    maxFeatures = property(__maxFeatures.value, __maxFeatures.set, None, '\n                     See definition of wfs:GetFeatureType.\n                  ')

    
    # Attribute traverseXlinkDepth uses Python identifier traverseXlinkDepth
    __traverseXlinkDepth = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'traverseXlinkDepth'), 'traverseXlinkDepth', '__httpwww_opengis_netwfs_GetFeatureWithLockType_traverseXlinkDepth', pyxb.binding.datatypes.string)
    __traverseXlinkDepth._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1039, 12)
    __traverseXlinkDepth._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1039, 12)
    
    traverseXlinkDepth = property(__traverseXlinkDepth.value, __traverseXlinkDepth.set, None, '\n                     See definition of wfs:GetFeatureType.\n                  ')

    
    # Attribute traverseXlinkExpiry uses Python identifier traverseXlinkExpiry
    __traverseXlinkExpiry = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'traverseXlinkExpiry'), 'traverseXlinkExpiry', '__httpwww_opengis_netwfs_GetFeatureWithLockType_traverseXlinkExpiry', pyxb.binding.datatypes.positiveInteger)
    __traverseXlinkExpiry._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1047, 12)
    __traverseXlinkExpiry._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1047, 12)
    
    traverseXlinkExpiry = property(__traverseXlinkExpiry.value, __traverseXlinkExpiry.set, None, '\n                     See definition of wfs:GetFeatureType.\n                  ')

    _ElementMap.update({
        __Query.name() : __Query
    })
    _AttributeMap.update({
        __expiry.name() : __expiry,
        __resultType.name() : __resultType,
        __outputFormat.name() : __outputFormat,
        __maxFeatures.name() : __maxFeatures,
        __traverseXlinkDepth.name() : __traverseXlinkDepth,
        __traverseXlinkExpiry.name() : __traverseXlinkExpiry
    })
_module_typeBindings.GetFeatureWithLockType = GetFeatureWithLockType
Namespace.addCategoryObject('typeBinding', 'GetFeatureWithLockType', GetFeatureWithLockType)


# Complex type {http://www.opengis.net/wfs}LockFeatureType with content type ELEMENT_ONLY
class LockFeatureType (BaseRequestType):
    """
            This type defines the LockFeature operation.  The LockFeature
            element contains one or more Lock elements that define which
            features of a particular type should be locked.  A lock
            identifier (lockId) is returned to the client application which
            can be used by subsequent operations to reference the locked
            features.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LockFeatureType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1072, 3)
    _ElementMap = BaseRequestType._ElementMap.copy()
    _AttributeMap = BaseRequestType._AttributeMap.copy()
    # Base type is BaseRequestType
    
    # Element {http://www.opengis.net/wfs}Lock uses Python identifier Lock
    __Lock = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Lock'), 'Lock', '__httpwww_opengis_netwfs_LockFeatureType_httpwww_opengis_netwfsLock', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1086, 15), )

    
    Lock = property(__Lock.value, __Lock.set, None, '\n                        The lock element is used to indicate which feature \n                        instances of particular type are to be locked.\n                     ')

    
    # Attribute service inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute version inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute handle inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute expiry uses Python identifier expiry
    __expiry = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'expiry'), 'expiry', '__httpwww_opengis_netwfs_LockFeatureType_expiry', pyxb.binding.datatypes.positiveInteger, unicode_default='5')
    __expiry._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1096, 12)
    __expiry._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1096, 12)
    
    expiry = property(__expiry.value, __expiry.set, None, '\n                     The expiry attribute is used to set the length\n                     of time (expressed in minutes) that features will\n                     remain locked as a result of a LockFeature\n                     request.  After the expiry period elapses, the\n                     locked resources must be released.  If the \n                     expiry attribute is not set, then the default\n                     value of 5 minutes will be enforced.\n                  ')

    
    # Attribute lockAction uses Python identifier lockAction
    __lockAction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lockAction'), 'lockAction', '__httpwww_opengis_netwfs_LockFeatureType_lockAction', _module_typeBindings.AllSomeType, unicode_default='ALL')
    __lockAction._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1111, 12)
    __lockAction._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1111, 12)
    
    lockAction = property(__lockAction.value, __lockAction.set, None, '\n                     The lockAction attribute is used to indicate what\n                     a Web Feature Service should do when it encounters\n                     a feature instance that has already been locked by\n                     another client application.\n      \n                     Valid values are ALL or SOME.\n      \n                     ALL means that the Web Feature Service must acquire\n                     locks on all the requested feature instances.  If it\n                     cannot acquire those locks then the request should\n                     fail.  In this instance, all locks acquired by the\n                     operation should be released.\n       \n                     SOME means that the Web Feature Service should lock\n                     as many of the requested features as it can.\n                  ')

    _ElementMap.update({
        __Lock.name() : __Lock
    })
    _AttributeMap.update({
        __expiry.name() : __expiry,
        __lockAction.name() : __lockAction
    })
_module_typeBindings.LockFeatureType = LockFeatureType
Namespace.addCategoryObject('typeBinding', 'LockFeatureType', LockFeatureType)


# Complex type {http://www.opengis.net/wfs}TransactionType with content type ELEMENT_ONLY
class TransactionType (BaseRequestType):
    """
            The TransactionType defines the Transaction operation.  A
            Transaction element contains one or more Insert, Update
            Delete and Native elements that allow a client application
            to create, modify or remove feature instances from the 
            feature repository that a Web Feature Service controls.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TransactionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1272, 3)
    _ElementMap = BaseRequestType._ElementMap.copy()
    _AttributeMap = BaseRequestType._AttributeMap.copy()
    # Base type is BaseRequestType
    
    # Element {http://www.opengis.net/wfs}LockId uses Python identifier LockId
    __LockId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LockId'), 'LockId', '__httpwww_opengis_netwfs_TransactionType_httpwww_opengis_netwfsLockId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1344, 3), )

    
    LockId = property(__LockId.value, __LockId.set, None, '\n            The LockId element contains the value of the lock identifier\n            obtained by a client application from a previous GetFeatureWithLock\n            or LockFeature request.\n         ')

    
    # Element {http://www.opengis.net/wfs}Insert uses Python identifier Insert
    __Insert = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Insert'), 'Insert', '__httpwww_opengis_netwfs_TransactionType_httpwww_opengis_netwfsInsert', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1353, 3), )

    
    Insert = property(__Insert.value, __Insert.set, None, '\n            The Insert element is used to indicate that the Web Feature\n            Service should create a new instance of a feature type.  The\n            feature instance is specified using GML3 and one or more \n            feature instances to be created can be contained inside the\n            Insert element.\n         ')

    
    # Element {http://www.opengis.net/wfs}Update uses Python identifier Update
    __Update = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Update'), 'Update', '__httpwww_opengis_netwfs_TransactionType_httpwww_opengis_netwfsUpdate', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1469, 3), )

    
    Update = property(__Update.value, __Update.set, None, '\n            One or more existing feature instances can be changed by\n            using the Update element.\n         ')

    
    # Element {http://www.opengis.net/wfs}Delete uses Python identifier Delete
    __Delete = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Delete'), 'Delete', '__httpwww_opengis_netwfs_TransactionType_httpwww_opengis_netwfsDelete', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1587, 3), )

    
    Delete = property(__Delete.value, __Delete.set, None, '\n            The Delete element is used to indicate that one or more\n            feature instances should be removed from the feature\n            repository.\n         ')

    
    # Element {http://www.opengis.net/wfs}Native uses Python identifier Native
    __Native = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Native'), 'Native', '__httpwww_opengis_netwfs_TransactionType_httpwww_opengis_netwfsNative', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1642, 3), )

    
    Native = property(__Native.value, __Native.set, None, '\n            Many times, a Web Feature Service interacts with a repository\n            that may have special vendor specific capabilities.  The native\n            element allows vendor specific command to be passed to the\n            repository via the Web Feature Service.\n         ')

    
    # Attribute service inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute version inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute handle inherited from {http://www.opengis.net/wfs}BaseRequestType
    
    # Attribute releaseAction uses Python identifier releaseAction
    __releaseAction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'releaseAction'), 'releaseAction', '__httpwww_opengis_netwfs_TransactionType_releaseAction', _module_typeBindings.AllSomeType)
    __releaseAction._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1311, 12)
    __releaseAction._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1311, 12)
    
    releaseAction = property(__releaseAction.value, __releaseAction.set, None, '\n                     The releaseAction attribute is used to control how a Web\n                     Feature service releases locks on feature instances after\n                     a Transaction request has been processed.\n\n                     Valid values are ALL or SOME.\n\n                     A value of ALL means that the Web Feature Service should\n                     release the locks of all feature instances locked with the\n                     specified lockId regardless or whether or not the features\n                     were actually modified.\n\n                     A value of SOME means that the Web Feature Service will \n                     only release the locks held on feature instances that \n                     were actually operated upon by the transaction.  The\n                     lockId that the client application obtained shall remain\n                     valid and the other, unmodified, feature instances shall\n                     remain locked.\n                    \n                     If the expiry attribute was specified in the original\n                     operation that locked the feature instances, then the\n                     expiry counter will be reset to give the client\n                     application that same amount of time to post subsequent\n                     transactions against the locked features.\n                  ')

    _ElementMap.update({
        __LockId.name() : __LockId,
        __Insert.name() : __Insert,
        __Update.name() : __Update,
        __Delete.name() : __Delete,
        __Native.name() : __Native
    })
    _AttributeMap.update({
        __releaseAction.name() : __releaseAction
    })
_module_typeBindings.TransactionType = TransactionType
Namespace.addCategoryObject('typeBinding', 'TransactionType', TransactionType)


# Complex type {http://www.opengis.net/wfs}InsertElementType with content type ELEMENT_ONLY
class InsertElementType (pyxb.binding.basis.complexTypeDefinition):
    """
            An Insert element may contain a feature collection or one 
            or more feature instances to be inserted into the 
            repository.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InsertElementType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1364, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml}_Feature uses Python identifier Feature
    __Feature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, '_Feature'), 'Feature', '__httpwww_opengis_netwfs_InsertElementType_httpwww_opengis_netgml_Feature', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 19, 1), )

    
    Feature = property(__Feature.value, __Feature.set, None, None)

    
    # Attribute idgen uses Python identifier idgen
    __idgen = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'idgen'), 'idgen', '__httpwww_opengis_netwfs_InsertElementType_idgen', _module_typeBindings.IdentifierGenerationOptionType, unicode_default='GenerateNew')
    __idgen._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1375, 6)
    __idgen._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1375, 6)
    
    idgen = property(__idgen.value, __idgen.set, None, '\n               The idgen attribute control how a WFS generates identifiers\n               from newly created feature instances using the Insert action.\n               The default action is to have the WFS generate a new id for\n               the features.  This is also backward compatible with WFS 1.0\n               where the only action was for the WFS to generate an new id.\n            ')

    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'handle'), 'handle', '__httpwww_opengis_netwfs_InsertElementType_handle', pyxb.binding.datatypes.string)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1388, 6)
    __handle._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1388, 6)
    
    handle = property(__handle.value, __handle.set, None, '\n               The handle attribute allows a client application\n               to assign a client-generated request identifier\n               to an Insert action.  The handle is included to\n               facilitate error reporting.  If an Insert action\n               in a Transaction request fails, then a WFS may\n               include the handle in an exception report to localize\n               the error.  If no handle is included of the offending\n               Insert element then a WFS may employee other means of\n               localizing the error (e.g. line number).\n            ')

    
    # Attribute inputFormat uses Python identifier inputFormat
    __inputFormat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'inputFormat'), 'inputFormat', '__httpwww_opengis_netwfs_InsertElementType_inputFormat', pyxb.binding.datatypes.string, unicode_default='text/xml; subtype=gml/3.1.1')
    __inputFormat._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1403, 6)
    __inputFormat._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1403, 6)
    
    inputFormat = property(__inputFormat.value, __inputFormat.set, None, "\n               This inputFormat attribute is used to indicate \n               the format used to encode a feature instance in\n               an Insert element.  The default value of\n               'text/xml; subtype=gml/3.1.1' is used to indicate\n               that feature encoding is GML3.  Another example\n               might be 'text/xml; subtype=gml/2.1.2' indicating\n               that the feature us encoded in GML2.  A WFS must\n               declare in the capabilities document, using a \n               Parameter element, which version of GML it supports.\n            ")

    
    # Attribute srsName uses Python identifier srsName
    __srsName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'srsName'), 'srsName', '__httpwww_opengis_netwfs_InsertElementType_srsName', pyxb.binding.datatypes.anyURI)
    __srsName._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1419, 6)
    __srsName._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1419, 6)
    
    srsName = property(__srsName.value, __srsName.set, None, "\n              ===== PAV 12NOV2004 ====\n              WHY IS THIS HERE? WOULDN'T WE KNOW THE INCOMING SRS FROM THE \n              GML GEOMETRY ELEMENTS?   I ASSUME THAT IF THE INCOMING SRS\n              DOES NOT MATCH ONE OF THE STORAGE SRS(s) THEN THE WFS WOULD\n              EITHER PROJECT INTO THE STORAGE SRS OR RAISE AN EXCEPTION.\n           ")

    _ElementMap.update({
        __Feature.name() : __Feature
    })
    _AttributeMap.update({
        __idgen.name() : __idgen,
        __handle.name() : __handle,
        __inputFormat.name() : __inputFormat,
        __srsName.name() : __srsName
    })
_module_typeBindings.InsertElementType = InsertElementType
Namespace.addCategoryObject('typeBinding', 'InsertElementType', InsertElementType)


# Complex type {http://www.opengis.net/wfs}QueryType with content type ELEMENT_ONLY
class QueryType (pyxb.binding.basis.complexTypeDefinition):
    """
            The Query element is of type QueryType.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 692, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}Function uses Python identifier Function
    __Function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Function'), 'Function', '__httpwww_opengis_netwfs_QueryType_httpwww_opengis_netogcFunction', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 25, 3), )

    
    Function = property(__Function.value, __Function.set, None, None)

    
    # Element {http://www.opengis.net/ogc}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter'), 'Filter', '__httpwww_opengis_netwfs_QueryType_httpwww_opengis_netogcFilter', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 39, 3), )

    
    Filter = property(__Filter.value, __Filter.set, None, None)

    
    # Element {http://www.opengis.net/ogc}SortBy uses Python identifier SortBy
    __SortBy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'SortBy'), 'SortBy', '__httpwww_opengis_netwfs_QueryType_httpwww_opengis_netogcSortBy', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/sort.xsd', 21, 3), )

    
    SortBy = property(__SortBy.value, __SortBy.set, None, None)

    
    # Element {http://www.opengis.net/wfs}PropertyName uses Python identifier PropertyName
    __PropertyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), 'PropertyName', '__httpwww_opengis_netwfs_QueryType_httpwww_opengis_netwfsPropertyName', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 89, 3), )

    
    PropertyName = property(__PropertyName.value, __PropertyName.set, None, '\n            The Property element is used to specify one or more\n            properties of a feature whose values are to be retrieved\n            by a Web Feature Service.\n\n            While a Web Feature Service should endeavour to satisfy\n            the exact request specified, in some instance this may\n            not be possible.  Specifically, a Web Feature Service\n            must generate a valid GML3 response to a Query operation.\n            The schema used to generate the output may include\n            properties that are mandatory.  In order that the output\n            validates, these mandatory properties must be specified\n            in the request.  If they are not, a Web Feature Service\n            may add them automatically to the Query before processing\n            it.  Thus a client application should, in general, be\n            prepared to receive more properties than it requested.\n\n            Of course, using the DescribeFeatureType request, a client\n            application can determine which properties are mandatory\n            and request them in the first place.\n         ')

    
    # Element {http://www.opengis.net/wfs}XlinkPropertyName uses Python identifier XlinkPropertyName
    __XlinkPropertyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'XlinkPropertyName'), 'XlinkPropertyName', '__httpwww_opengis_netwfs_QueryType_httpwww_opengis_netwfsXlinkPropertyName', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 114, 3), )

    
    XlinkPropertyName = property(__XlinkPropertyName.value, __XlinkPropertyName.set, None, '\n            This element may be used in place of an wfs:PropertyName element\n            in a wfs:Query element in a wfs:GetFeature element to selectively\n            request the traversal of nested XLinks in the returned element for\n            the named property. This element may not be used in other requests\n            -- GetFeatureWithLock, LockFeature, Insert, Update, Delete -- in\n            this version of the WFS specification.\n         ')

    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'handle'), 'handle', '__httpwww_opengis_netwfs_QueryType_handle', pyxb.binding.datatypes.string)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 758, 5)
    __handle._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 758, 5)
    
    handle = property(__handle.value, __handle.set, None, '\n               The handle attribute allows a client application\n               to assign a client-generated identifier for the \n               Query.  The handle is included to facilitate error\n               reporting.  If one Query in a GetFeature request\n               causes an exception, a WFS may report the handle\n               to indicate which query element failed.  If the a\n               handle is not present, the WFS may use other means\n               to localize the error (e.g. line numbers).\n            ')

    
    # Attribute typeName uses Python identifier typeName
    __typeName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typeName'), 'typeName', '__httpwww_opengis_netwfs_QueryType_typeName', _module_typeBindings.TypeNameListType, required=True)
    __typeName._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 773, 5)
    __typeName._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 773, 5)
    
    typeName = property(__typeName.value, __typeName.set, None, "\n              The typeName attribute is a list of one or more\n              feature type names that indicate which types \n              of feature instances should be included in the\n              reponse set.  Specifying more than one typename\n              indicates that a join operation is being performed.\n              All the names in the typeName list must be valid\n              types that belong to this query's feature content\n              as defined by the GML Application Schema.\n           ")

    
    # Attribute featureVersion uses Python identifier featureVersion
    __featureVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'featureVersion'), 'featureVersion', '__httpwww_opengis_netwfs_QueryType_featureVersion', pyxb.binding.datatypes.string)
    __featureVersion._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 788, 5)
    __featureVersion._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 788, 5)
    
    featureVersion = property(__featureVersion.value, __featureVersion.set, None, "\n              For systems that implement versioning, the featureVersion\n              attribute is used to specify which version of a particular\n              feature instance is to be retrieved.  A value of ALL means\n              that all versions should be retrieved.  An integer value\n              'i', means that the ith version should be retrieve if it\n              exists or the most recent version otherwise.\n           ")

    
    # Attribute srsName uses Python identifier srsName
    __srsName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'srsName'), 'srsName', '__httpwww_opengis_netwfs_QueryType_srsName', pyxb.binding.datatypes.anyURI)
    __srsName._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 801, 5)
    __srsName._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 801, 5)
    
    srsName = property(__srsName.value, __srsName.set, None, '\n              This attribute is used to specify a specific WFS-supported SRS\n              that should be used for returned feature geometries.  The value\n              may be the WFS StorageSRS value, DefaultRetrievalSRS value, or\n              one of AdditionalSRS values.  If no srsName value is supplied,\n              then the features will be returned using either the\n              DefaultRetrievalSRS, if specified, and StorageSRS otherwise.\n              For feature types with no spatial properties, this attribute\n              must not be specified or ignored if it is specified.\n           ')

    _ElementMap.update({
        __Function.name() : __Function,
        __Filter.name() : __Filter,
        __SortBy.name() : __SortBy,
        __PropertyName.name() : __PropertyName,
        __XlinkPropertyName.name() : __XlinkPropertyName
    })
    _AttributeMap.update({
        __handle.name() : __handle,
        __typeName.name() : __typeName,
        __featureVersion.name() : __featureVersion,
        __srsName.name() : __srsName
    })
_module_typeBindings.QueryType = QueryType
Namespace.addCategoryObject('typeBinding', 'QueryType', QueryType)


PropertyName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), pyxb.binding.datatypes.string, documentation='\n            The Property element is used to specify one or more\n            properties of a feature whose values are to be retrieved\n            by a Web Feature Service.\n\n            While a Web Feature Service should endeavour to satisfy\n            the exact request specified, in some instance this may\n            not be possible.  Specifically, a Web Feature Service\n            must generate a valid GML3 response to a Query operation.\n            The schema used to generate the output may include\n            properties that are mandatory.  In order that the output\n            validates, these mandatory properties must be specified\n            in the request.  If they are not, a Web Feature Service\n            may add them automatically to the Query before processing\n            it.  Thus a client application should, in general, be\n            prepared to receive more properties than it requested.\n\n            Of course, using the DescribeFeatureType request, a client\n            application can determine which properties are mandatory\n            and request them in the first place.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 89, 3))
Namespace.addCategoryObject('elementBinding', PropertyName.name().localName(), PropertyName)

LockId = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LockId'), pyxb.binding.datatypes.string, documentation='\n            The LockId element contains the value of the lock identifier\n            obtained by a client application from a previous GetFeatureWithLock\n            or LockFeature request.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1344, 3))
Namespace.addCategoryObject('elementBinding', LockId.name().localName(), LockId)

XlinkPropertyName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'XlinkPropertyName'), CTD_ANON, documentation='\n            This element may be used in place of an wfs:PropertyName element\n            in a wfs:Query element in a wfs:GetFeature element to selectively\n            request the traversal of nested XLinks in the returned element for\n            the named property. This element may not be used in other requests\n            -- GetFeatureWithLock, LockFeature, Insert, Update, Delete -- in\n            this version of the WFS specification.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 114, 3))
Namespace.addCategoryObject('elementBinding', XlinkPropertyName.name().localName(), XlinkPropertyName)

GetCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetCapabilities'), GetCapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 167, 3))
Namespace.addCategoryObject('elementBinding', GetCapabilities.name().localName(), GetCapabilities)

WFS_Capabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WFS_Capabilities'), WFS_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 192, 3))
Namespace.addCategoryObject('elementBinding', WFS_Capabilities.name().localName(), WFS_Capabilities)

FeatureTypeList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FeatureTypeList'), FeatureTypeListType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 223, 3))
Namespace.addCategoryObject('elementBinding', FeatureTypeList.name().localName(), FeatureTypeList)

ServesGMLObjectTypeList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServesGMLObjectTypeList'), GMLObjectTypeListType, documentation='\n            List of GML Object types available for GetGmlObject requests\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 384, 3))
Namespace.addCategoryObject('elementBinding', ServesGMLObjectTypeList.name().localName(), ServesGMLObjectTypeList)

SupportsGMLObjectTypeList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SupportsGMLObjectTypeList'), GMLObjectTypeListType, documentation='\n            List of GML Object types that WFS is capable of serving, either\n            directly, or as validly derived types defined in a GML application\n            schema.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 392, 3))
Namespace.addCategoryObject('elementBinding', SupportsGMLObjectTypeList.name().localName(), SupportsGMLObjectTypeList)

FeatureCollection = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FeatureCollection'), FeatureCollectionType, documentation='\n            This element is a container for the response to a GetFeature\n            or GetFeatureWithLock (WFS-transaction.xsd) request.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 836, 3))
Namespace.addCategoryObject('elementBinding', FeatureCollection.name().localName(), FeatureCollection)

LockFeatureResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LockFeatureResponse'), LockFeatureResponseType, documentation='\n            The LockFeatureResponse element contains a report\n            about the completion status of a LockFeature request.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1186, 3))
Namespace.addCategoryObject('elementBinding', LockFeatureResponse.name().localName(), LockFeatureResponse)

Update = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Update'), UpdateElementType, documentation='\n            One or more existing feature instances can be changed by\n            using the Update element.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1469, 3))
Namespace.addCategoryObject('elementBinding', Update.name().localName(), Update)

Property = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Property'), PropertyType, documentation='\n            The Property element is used to specify the new\n            value of a feature property inside an Update\n            element.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1558, 3))
Namespace.addCategoryObject('elementBinding', Property.name().localName(), Property)

Delete = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Delete'), DeleteElementType, documentation='\n            The Delete element is used to indicate that one or more\n            feature instances should be removed from the feature\n            repository.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1587, 3))
Namespace.addCategoryObject('elementBinding', Delete.name().localName(), Delete)

Native = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Native'), NativeType, documentation='\n            Many times, a Web Feature Service interacts with a repository\n            that may have special vendor specific capabilities.  The native\n            element allows vendor specific command to be passed to the\n            repository via the Web Feature Service.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1642, 3))
Namespace.addCategoryObject('elementBinding', Native.name().localName(), Native)

TransactionResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TransactionResponse'), TransactionResponseType, documentation='\n            The TransactionResponse element contains a report\n            about the completion status of a Transaction operation.  \n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1678, 3))
Namespace.addCategoryObject('elementBinding', TransactionResponse.name().localName(), TransactionResponse)

DescribeFeatureType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescribeFeatureType'), DescribeFeatureTypeType, documentation='\n            The DescribeFeatureType element is used to request that a Web\n            Feature Service generate a document describing one or more \n            feature types.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 457, 3))
Namespace.addCategoryObject('elementBinding', DescribeFeatureType.name().localName(), DescribeFeatureType)

GetFeature = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetFeature'), GetFeatureType, documentation='\n            The GetFeature element is used to request that a Web Feature\n            Service return feature type instances of one or more feature\n            types.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 536, 3))
Namespace.addCategoryObject('elementBinding', GetFeature.name().localName(), GetFeature)

GetGmlObject = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetGmlObject'), GetGmlObjectType, documentation='\n            The GetGmlObject element is used to request that a Web Feature\n            Service return an element with a gml:id attribute value specified\n            by an ogc:GmlObjectId.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 897, 3))
Namespace.addCategoryObject('elementBinding', GetGmlObject.name().localName(), GetGmlObject)

GetFeatureWithLock = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetFeatureWithLock'), GetFeatureWithLockType, documentation='\n            This is the root element for the GetFeatureWithLock request.\n            The GetFeatureWithLock operation performs identically to a\n            GetFeature request except that the GetFeatureWithLock request\n            locks all the feature instances in the result set and returns\n            a lock identifier to a client application in the response.\n            The lock identifier is returned to the client application \n            using the lockId attribute define on the wfs:FeatureCollection\n            element.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 967, 3))
Namespace.addCategoryObject('elementBinding', GetFeatureWithLock.name().localName(), GetFeatureWithLock)

LockFeature = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LockFeature'), LockFeatureType, documentation='\n            This is the root element for a LockFeature request.\n            The LockFeature request can be used to lock one or\n            more feature instances.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1063, 3))
Namespace.addCategoryObject('elementBinding', LockFeature.name().localName(), LockFeature)

Transaction = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Transaction'), TransactionType, documentation='\n            This is the root element for a Transaction request.\n            A transaction request allows insert, update and \n            delete operations to be performed to create, change\n            or remove feature instances.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1262, 3))
Namespace.addCategoryObject('elementBinding', Transaction.name().localName(), Transaction)

Insert = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Insert'), InsertElementType, documentation='\n            The Insert element is used to indicate that the Web Feature\n            Service should create a new instance of a feature type.  The\n            feature instance is specified using GML3 and one or more \n            feature instances to be created can be contained inside the\n            Insert element.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1353, 3))
Namespace.addCategoryObject('elementBinding', Insert.name().localName(), Insert)

Query = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Query'), QueryType, documentation='\n            The Query element is used to describe a single query.\n            One or more Query elements can be specified inside a\n            GetFeature element so that multiple queries can be \n            executed in one request.  The output from the various\n            queries are combined in a wfs:FeatureCollection element\n            to form the response document.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 680, 3))
Namespace.addCategoryObject('elementBinding', Query.name().localName(), Query)



def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
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
    symbol = pyxb.binding.content.ElementUse(GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'AcceptVersions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 45, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Sections')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 50, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'AcceptFormats')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 55, 3))
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
GetCapabilitiesType._Automaton = _BuildAutomaton()




WFS_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter_Capabilities'), pyxb.bundles.opengis.filter.CTD_ANON, scope=WFS_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 20, 3)))

WFS_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FeatureTypeList'), FeatureTypeListType, scope=WFS_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 223, 3)))

WFS_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServesGMLObjectTypeList'), GMLObjectTypeListType, scope=WFS_CapabilitiesType, documentation='\n            List of GML Object types available for GetGmlObject requests\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 384, 3)))

WFS_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SupportsGMLObjectTypeList'), GMLObjectTypeListType, scope=WFS_CapabilitiesType, documentation='\n            List of GML Object types that WFS is capable of serving, either\n            directly, or as validly derived types defined in a GML application\n            schema.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 392, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 30, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 31, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 32, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 215, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 216, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 217, 15))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WFS_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'ServiceIdentification')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 30, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WFS_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'ServiceProvider')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WFS_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'OperationsMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 32, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WFS_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FeatureTypeList')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 215, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WFS_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServesGMLObjectTypeList')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 216, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WFS_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SupportsGMLObjectTypeList')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 217, 15))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(WFS_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter_Capabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 218, 15))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
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
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
WFS_CapabilitiesType._Automaton = _BuildAutomaton_()




FeatureTypeListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Operations'), OperationsType, scope=FeatureTypeListType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 231, 9)))

FeatureTypeListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FeatureType'), FeatureTypeType, scope=FeatureTypeListType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 234, 9)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 231, 9))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FeatureTypeListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Operations')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 231, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FeatureTypeListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FeatureType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 234, 9))
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
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FeatureTypeListType._Automaton = _BuildAutomaton_2()




FeatureTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Keywords'), pyxb.bundles.opengis.ows.KeywordsType, scope=FeatureTypeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 36, 1)))

FeatureTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'WGS84BoundingBox'), pyxb.bundles.opengis.ows.WGS84BoundingBoxType, scope=FeatureTypeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 111, 1)))

FeatureTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.QName, scope=FeatureTypeType, documentation='\n                  Name of this feature type, including any namespace prefix\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 248, 9)))

FeatureTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Title'), pyxb.binding.datatypes.string, scope=FeatureTypeType, documentation='\n                  Title of this feature type, normally used for display\n                  to a human.\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 255, 9)))

FeatureTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Abstract'), pyxb.binding.datatypes.string, scope=FeatureTypeType, documentation='\n                  Brief narrative description of this feature type, normally\n                  used for display to a human.\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 263, 9)))

FeatureTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DefaultSRS'), pyxb.binding.datatypes.anyURI, scope=FeatureTypeType, documentation='\n                        The DefaultSRS element indicated which spatial\n                        reference system shall be used by a WFS to\n                        express the state of a spatial feature if not\n                        otherwise explicitly identified within a query\n                        or transaction request.  The SRS may be indicated\n                        using either the EPSG form (EPSG:posc code) or\n                        the URL form defined in subclause 4.3.2 of\n                        refernce[2].\n                     ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 274, 15)))

FeatureTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OtherSRS'), pyxb.binding.datatypes.anyURI, scope=FeatureTypeType, documentation='\n                        The OtherSRS element is used to indicate other \n                        supported SRSs within query and transaction \n                        operations.  A supported SRS means that the \n                        WFS supports the transformation of spatial\n                        properties between the OtherSRS and the internal\n                        storage SRS.  The effects of such transformations \n                        must be considered when determining and declaring \n                        the guaranteed data accuracy.\n                     ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 289, 15)))

FeatureTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NoSRS'), CTD_ANON_, scope=FeatureTypeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 306, 12)))

FeatureTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Operations'), OperationsType, scope=FeatureTypeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 310, 9)))

FeatureTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutputFormats'), OutputFormatListType, scope=FeatureTypeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 313, 9)))

FeatureTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MetadataURL'), MetadataURLType, scope=FeatureTypeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 318, 9)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 263, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 271, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 289, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 310, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 313, 9))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 316, 9))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 318, 9))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FeatureTypeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 248, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FeatureTypeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 255, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FeatureTypeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 263, 9))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FeatureTypeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Keywords')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 271, 9))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FeatureTypeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DefaultSRS')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 274, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(FeatureTypeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OtherSRS')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 289, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FeatureTypeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NoSRS')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 306, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(FeatureTypeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Operations')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 310, 9))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(FeatureTypeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OutputFormats')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 313, 9))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(FeatureTypeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'WGS84BoundingBox')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 316, 9))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(FeatureTypeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MetadataURL')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 318, 9))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
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
    transitions.append(fac.Transition(st_6, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FeatureTypeType._Automaton = _BuildAutomaton_3()




OperationsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Operation'), OperationType, scope=OperationsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 325, 9)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OperationsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Operation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 325, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OperationsType._Automaton = _BuildAutomaton_4()




OutputFormatListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Format'), pyxb.binding.datatypes.string, scope=OutputFormatListType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 342, 9)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OutputFormatListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Format')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 342, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OutputFormatListType._Automaton = _BuildAutomaton_5()




GMLObjectTypeListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GMLObjectType'), GMLObjectTypeType, scope=GMLObjectTypeListType, documentation='\n                  Name of this GML object type, including any namespace prefix\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 404, 9)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GMLObjectTypeListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GMLObjectType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 404, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GMLObjectTypeListType._Automaton = _BuildAutomaton_6()




GMLObjectTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Keywords'), pyxb.bundles.opengis.ows.KeywordsType, scope=GMLObjectTypeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/ows19115subset.xsd', 36, 1)))

GMLObjectTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.QName, scope=GMLObjectTypeType, documentation='\n                  Name of this GML Object type, including any namespace prefix.\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 423, 9)))

GMLObjectTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Title'), pyxb.binding.datatypes.string, scope=GMLObjectTypeType, documentation='\n                  Title of this GML Object type, normally used for display\n                  to a human.\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 430, 9)))

GMLObjectTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Abstract'), pyxb.binding.datatypes.string, scope=GMLObjectTypeType, documentation='\n                  Brief narrative description of this GML Object type, normally\n                  used for display to a human.\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 438, 9)))

GMLObjectTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutputFormats'), OutputFormatListType, scope=GMLObjectTypeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 448, 9)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 430, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 438, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 446, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 448, 9))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GMLObjectTypeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 423, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GMLObjectTypeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 430, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GMLObjectTypeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 438, 9))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(GMLObjectTypeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Keywords')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 446, 9))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(GMLObjectTypeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OutputFormats')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 448, 9))
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
GMLObjectTypeType._Automaton = _BuildAutomaton_7()




def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 108, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 109, 5))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FeatureCollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(FeatureCollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(FeatureCollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(FeatureCollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(FeatureCollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(FeatureCollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'featureMember')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 108, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(FeatureCollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'featureMembers')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 109, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
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
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FeatureCollectionType._Automaton = _BuildAutomaton_8()




LockType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter'), pyxb.bundles.opengis.filter.FilterType, scope=LockType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 39, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1156, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LockType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1156, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LockType._Automaton = _BuildAutomaton_9()




LockFeatureResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FeaturesLocked'), FeaturesLockedType, scope=LockFeatureResponseType, documentation='\n                  The LockFeature or GetFeatureWithLock operations\n                  identify and attempt to lock a set of feature \n                  instances that satisfy the constraints specified \n                  in the request.  In the event that the lockAction\n                  attribute (on the LockFeature or GetFeatureWithLock\n                  elements) is set to SOME, a Web Feature Service will\n                  attempt to lock as many of the feature instances from\n                  the result set as possible.\n\n                  The FeaturesLocked element contains list of ogc:FeatureId\n                  elements enumerating the feature instances that a WFS\n                  actually managed to lock.\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1214, 9)))

LockFeatureResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FeaturesNotLocked'), FeaturesNotLockedType, scope=LockFeatureResponseType, documentation='\n                  In contrast to the FeaturesLocked element, the\n                  FeaturesNotLocked element contains a list of \n                  ogc:Filter elements identifying feature instances\n                  that a WFS did not manage to lock because they were\n                  already locked by another process.\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1233, 9)))

LockFeatureResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LockId'), pyxb.binding.datatypes.string, scope=LockFeatureResponseType, documentation='\n            The LockId element contains the value of the lock identifier\n            obtained by a client application from a previous GetFeatureWithLock\n            or LockFeature request.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1344, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1214, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1233, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LockFeatureResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LockId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1204, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LockFeatureResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FeaturesLocked')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1214, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(LockFeatureResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FeaturesNotLocked')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1233, 9))
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
LockFeatureResponseType._Automaton = _BuildAutomaton_10()




FeaturesLockedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'FeatureId'), pyxb.bundles.opengis.filter.FeatureIdType, scope=FeaturesLockedType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 32, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FeaturesLockedType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'FeatureId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1249, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FeaturesLockedType._Automaton = _BuildAutomaton_11()




FeaturesNotLockedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'FeatureId'), pyxb.bundles.opengis.filter.FeatureIdType, scope=FeaturesNotLockedType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 32, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FeaturesNotLockedType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'FeatureId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1254, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FeaturesNotLockedType._Automaton = _BuildAutomaton_12()




UpdateElementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter'), pyxb.bundles.opengis.filter.FilterType, scope=UpdateElementType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 39, 3)))

UpdateElementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Property'), PropertyType, scope=UpdateElementType, documentation='\n            The Property element is used to specify the new\n            value of a feature property inside an Update\n            element.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1558, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1492, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UpdateElementType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Property')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1479, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UpdateElementType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1492, 9))
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
UpdateElementType._Automaton = _BuildAutomaton_13()




PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.QName, scope=PropertyType, documentation='\n                  The Name element contains the name of a feature property\n                  to be updated.\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1569, 9)))

PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Value'), pyxb.binding.datatypes.anyType, scope=PropertyType, documentation='\n                  The Value element contains the replacement value for the\n                  named property.\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1577, 9)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1577, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1569, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Value')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1577, 9))
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
PropertyType._Automaton = _BuildAutomaton_14()




DeleteElementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter'), pyxb.bundles.opengis.filter.FilterType, scope=DeleteElementType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 39, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DeleteElementType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1598, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DeleteElementType._Automaton = _BuildAutomaton_15()




TransactionResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TransactionSummary'), TransactionSummaryType, scope=TransactionResponseType, documentation='\n                  The TransactionSummary element is used to summarize\n                  the number of feature instances affected by the \n                  transaction.\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1696, 9)))

TransactionResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TransactionResults'), TransactionResultsType, scope=TransactionResponseType, documentation='\n                  For systems that do not support atomic transactions,\n                  the TransactionResults element may be used to report\n                  exception codes and messages for all actions of a\n                  transaction that failed to execute successfully.\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1706, 9)))

TransactionResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InsertResults'), InsertResultsType, scope=TransactionResponseType, documentation='\n                  A transaction is a collection of Insert,Update and Delete\n                  actions.  The Update and Delete actions modify features\n                  that already exist.  The Insert action, however, creates\n                  new features.  The InsertResults element is used to\n                  report the identifiers of the newly created features.\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1718, 9)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1706, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1718, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TransactionResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TransactionSummary')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1696, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TransactionResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TransactionResults')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1706, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TransactionResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InsertResults')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1718, 9))
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
TransactionResponseType._Automaton = _BuildAutomaton_16()




TransactionSummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'totalInserted'), pyxb.binding.datatypes.nonNegativeInteger, scope=TransactionSummaryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1751, 9)))

TransactionSummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'totalUpdated'), pyxb.binding.datatypes.nonNegativeInteger, scope=TransactionSummaryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1754, 9)))

TransactionSummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'totalDeleted'), pyxb.binding.datatypes.nonNegativeInteger, scope=TransactionSummaryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1757, 9)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1751, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1754, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1757, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TransactionSummaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'totalInserted')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1751, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TransactionSummaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'totalUpdated')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1754, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TransactionSummaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'totalDeleted')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1757, 9))
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
TransactionSummaryType._Automaton = _BuildAutomaton_17()




TransactionResultsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Action'), ActionType, scope=TransactionResultsType, documentation='\n                  The Action element reports an exception code\n                  and exception message indicating why the\n                  corresponding action of a transaction request\n                  failed.\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1771, 9)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1771, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TransactionResultsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Action')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1771, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TransactionResultsType._Automaton = _BuildAutomaton_18()




ActionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Message'), pyxb.binding.datatypes.string, scope=ActionType, documentation='\n                  If an action fails, the message element may be used\n                  to supply an exception message.\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1786, 9)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1786, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ActionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Message')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1786, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ActionType._Automaton = _BuildAutomaton_19()




InsertResultsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Feature'), InsertedFeatureType, scope=InsertResultsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1837, 9)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InsertResultsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Feature')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1837, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InsertResultsType._Automaton = _BuildAutomaton_20()




InsertedFeatureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'FeatureId'), pyxb.bundles.opengis.filter.FeatureIdType, scope=InsertedFeatureType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 32, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InsertedFeatureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'FeatureId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1844, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InsertedFeatureType._Automaton = _BuildAutomaton_21()




DescribeFeatureTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TypeName'), pyxb.binding.datatypes.QName, scope=DescribeFeatureTypeType, documentation='\n                        The TypeName element is used to enumerate the\n                        feature types to be described.  If no TypeName\n                        elements are specified then all features should\n                        be described.  The name must be a valid type\n                        that belongs to the feature content as defined\n                        by the GML Application Schema.\n                     ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 486, 15)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 486, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DescribeFeatureTypeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TypeName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 486, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DescribeFeatureTypeType._Automaton = _BuildAutomaton_22()




GetFeatureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Query'), QueryType, scope=GetFeatureType, documentation='\n            The Query element is used to describe a single query.\n            One or more Query elements can be specified inside a\n            GetFeature element so that multiple queries can be \n            executed in one request.  The output from the various\n            queries are combined in a wfs:FeatureCollection element\n            to form the response document.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 680, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetFeatureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Query')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 561, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GetFeatureType._Automaton = _BuildAutomaton_23()




GetGmlObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'GmlObjectId'), pyxb.bundles.opengis.filter.GmlObjectIdType, scope=GetGmlObjectType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 35, 3)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetGmlObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'GmlObjectId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 918, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GetGmlObjectType._Automaton = _BuildAutomaton_24()




GetFeatureWithLockType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Query'), QueryType, scope=GetFeatureWithLockType, documentation='\n            The Query element is used to describe a single query.\n            One or more Query elements can be specified inside a\n            GetFeature element so that multiple queries can be \n            executed in one request.  The output from the various\n            queries are combined in a wfs:FeatureCollection element\n            to form the response document.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 680, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetFeatureWithLockType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Query')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 996, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GetFeatureWithLockType._Automaton = _BuildAutomaton_25()




LockFeatureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Lock'), LockType, scope=LockFeatureType, documentation='\n                        The lock element is used to indicate which feature \n                        instances of particular type are to be locked.\n                     ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1086, 15)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LockFeatureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Lock')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1086, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LockFeatureType._Automaton = _BuildAutomaton_26()




TransactionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LockId'), pyxb.binding.datatypes.string, scope=TransactionType, documentation='\n            The LockId element contains the value of the lock identifier\n            obtained by a client application from a previous GetFeatureWithLock\n            or LockFeature request.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1344, 3)))

TransactionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Insert'), InsertElementType, scope=TransactionType, documentation='\n            The Insert element is used to indicate that the Web Feature\n            Service should create a new instance of a feature type.  The\n            feature instance is specified using GML3 and one or more \n            feature instances to be created can be contained inside the\n            Insert element.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1353, 3)))

TransactionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Update'), UpdateElementType, scope=TransactionType, documentation='\n            One or more existing feature instances can be changed by\n            using the Update element.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1469, 3)))

TransactionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Delete'), DeleteElementType, scope=TransactionType, documentation='\n            The Delete element is used to indicate that one or more\n            feature instances should be removed from the feature\n            repository.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1587, 3)))

TransactionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Native'), NativeType, scope=TransactionType, documentation='\n            Many times, a Web Feature Service interacts with a repository\n            that may have special vendor specific capabilities.  The native\n            element allows vendor specific command to be passed to the\n            repository via the Web Feature Service.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1642, 3)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1285, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1304, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TransactionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LockId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1285, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TransactionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Insert')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1305, 18))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TransactionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Update')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1306, 18))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TransactionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Delete')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1307, 18))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TransactionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Native')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1308, 18))
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
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TransactionType._Automaton = _BuildAutomaton_27()




InsertElementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, '_Feature'), pyxb.bundles.opengis.gml.AbstractFeatureType, abstract=pyxb.binding.datatypes.boolean(1), scope=InsertElementType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 19, 1)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InsertElementType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, '_Feature')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 1373, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InsertElementType._Automaton = _BuildAutomaton_28()




QueryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Function'), pyxb.bundles.opengis.filter.FunctionType, scope=QueryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 25, 3)))

QueryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter'), pyxb.bundles.opengis.filter.FilterType, scope=QueryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 39, 3)))

QueryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'SortBy'), pyxb.bundles.opengis.filter.SortByType, scope=QueryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/sort.xsd', 21, 3)))

QueryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), pyxb.binding.datatypes.string, scope=QueryType, documentation='\n            The Property element is used to specify one or more\n            properties of a feature whose values are to be retrieved\n            by a Web Feature Service.\n\n            While a Web Feature Service should endeavour to satisfy\n            the exact request specified, in some instance this may\n            not be possible.  Specifically, a Web Feature Service\n            must generate a valid GML3 response to a Query operation.\n            The schema used to generate the output may include\n            properties that are mandatory.  In order that the output\n            validates, these mandatory properties must be specified\n            in the request.  If they are not, a Web Feature Service\n            may add them automatically to the Query before processing\n            it.  Thus a client application should, in general, be\n            prepared to receive more properties than it requested.\n\n            Of course, using the DescribeFeatureType request, a client\n            application can determine which properties are mandatory\n            and request them in the first place.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 89, 3)))

QueryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'XlinkPropertyName'), CTD_ANON, scope=QueryType, documentation='\n            This element may be used in place of an wfs:PropertyName element\n            in a wfs:Query element in a wfs:GetFeature element to selectively\n            request the traversal of nested XLinks in the returned element for\n            the named property. This element may not be used in other requests\n            -- GetFeatureWithLock, LockFeature, Insert, Update, Delete -- in\n            this version of the WFS specification.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 114, 3)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 699, 7))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 737, 7))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 748, 7))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PropertyName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 700, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'XlinkPropertyName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 725, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Function')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 726, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(QueryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 737, 7))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(QueryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'SortBy')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/wfs/1.1.0/wfs.xsd', 748, 7))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
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
    return fac.Automaton(states, counters, True, containing_state=None)
QueryType._Automaton = _BuildAutomaton_29()


FeatureCollection._setSubstitutionGroup(pyxb.bundles.opengis.gml.FeatureCollection)
