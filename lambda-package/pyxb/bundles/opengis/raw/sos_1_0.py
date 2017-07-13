# ./pyxb/bundles/opengis/raw/sos_1_0.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:174f2064d4c9c2f52a72ce02f36f6f8f371fe8e0
# Generated 2017-07-10 00:37:15.514625 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/sos/1.0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:ea30544a-6507-11e7-bab2-0a55f9edafa5')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.bundles.opengis._ogc
import pyxb.bundles.opengis.ows_1_1
import pyxb.bundles.opengis.filter
import pyxb.bundles.opengis.om_1_0
import pyxb.bundles.opengis.swe_1_0_1
import pyxb.binding.datatypes
import pyxb.bundles.opengis.gml

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/sos/1.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gml = pyxb.bundles.opengis.gml.Namespace
_Namespace_gml.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ows = pyxb.bundles.opengis.ows_1_1.Namespace
_Namespace_ows.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ogc = pyxb.bundles.opengis.filter.Namespace
_Namespace_ogc.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_om = pyxb.bundles.opengis.om_1_0.Namespace
_Namespace_om.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://www.opengis.net/sos/1.0}responseModeType
class responseModeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'responseModeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosCommon.xsd', 37, 1)
    _Documentation = None
responseModeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=responseModeType, enum_prefix=None)
responseModeType.inline = responseModeType._CF_enumeration.addEnumeration(unicode_value='inline', tag='inline')
responseModeType.attached = responseModeType._CF_enumeration.addEnumeration(unicode_value='attached', tag='attached')
responseModeType.out_of_band = responseModeType._CF_enumeration.addEnumeration(unicode_value='out-of-band', tag='out_of_band')
responseModeType.resultTemplate = responseModeType._CF_enumeration.addEnumeration(unicode_value='resultTemplate', tag='resultTemplate')
responseModeType._InitializeFacetMap(responseModeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'responseModeType', responseModeType)
_module_typeBindings.responseModeType = responseModeType

# Complex type {http://www.opengis.net/sos/1.0}RequestBaseType with content type EMPTY
class RequestBaseType (pyxb.binding.basis.complexTypeDefinition):
    """XML encoded SOS operation request base, for all operations except Get Capabilities. In this XML encoding, no "request" parameter is included, since the element name specifies the specific operation. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosCommon.xsd', 22, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__httpwww_opengis_netsos1_0_RequestBaseType_service', pyxb.binding.datatypes.string, fixed=True, unicode_default='SOS', required=True)
    __service._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosCommon.xsd', 26, 2)
    __service._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosCommon.xsd', 26, 2)
    
    service = property(__service.value, __service.set, None, 'Service type identifier. ')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netsos1_0_RequestBaseType_version', pyxb.binding.datatypes.string, fixed=True, unicode_default='1.0.0', required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosCommon.xsd', 31, 2)
    __version._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosCommon.xsd', 31, 2)
    
    version = property(__version.value, __version.set, None, 'Specification version for SOS version and operation.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __service.name() : __service,
        __version.name() : __version
    })
_module_typeBindings.RequestBaseType = RequestBaseType
Namespace.addCategoryObject('typeBinding', 'RequestBaseType', RequestBaseType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Contents section of SOS service metadata (or Capabilites) XML document. For the SOS, these contents are data and functions that the SOS server provides."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 30, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/sos/1.0}ObservationOfferingList uses Python identifier ObservationOfferingList
    __ObservationOfferingList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ObservationOfferingList'), 'ObservationOfferingList', '__httpwww_opengis_netsos1_0_CTD_ANON_httpwww_opengis_netsos1_0ObservationOfferingList', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 32, 4), )

    
    ObservationOfferingList = property(__ObservationOfferingList.value, __ObservationOfferingList.set, None, None)

    _ElementMap.update({
        __ObservationOfferingList.name() : __ObservationOfferingList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 33, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/sos/1.0}ObservationOffering uses Python identifier ObservationOffering
    __ObservationOffering = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ObservationOffering'), 'ObservationOffering', '__httpwww_opengis_netsos1_0_CTD_ANON__httpwww_opengis_netsos1_0ObservationOffering', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 35, 7), )

    
    ObservationOffering = property(__ObservationOffering.value, __ObservationOffering.set, None, None)

    _ElementMap.update({
        __ObservationOffering.name() : __ObservationOffering
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {http://www.opengis.net/sos/1.0}ObservationOfferingBaseType with content type ELEMENT_ONLY
class ObservationOfferingBaseType (pyxb.bundles.opengis.gml.AbstractFeatureType):
    """Makes boundedBy mandatory"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ObservationOfferingBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 43, 1)
    _ElementMap = pyxb.bundles.opengis.gml.AbstractFeatureType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml.AbstractFeatureType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml.AbstractFeatureType
    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ObservationOfferingBaseType = ObservationOfferingBaseType
Namespace.addCategoryObject('typeBinding', 'ObservationOfferingBaseType', ObservationOfferingBaseType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.bundles.opengis.ows_1_1.GetCapabilitiesType):
    """Request to a SOS to perform the GetCapabilities operation. This operation allows a client to retrieve service metadata (capabilities XML) providing metadata for the specific SOS server. In this XML encoding, no "request" parameter is included, since the element name specifies the specific operation. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 29, 2)
    _ElementMap = pyxb.bundles.opengis.ows_1_1.GetCapabilitiesType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.ows_1_1.GetCapabilitiesType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.ows_1_1.GetCapabilitiesType
    
    # Element AcceptVersions ({http://www.opengis.net/ows/1.1}AcceptVersions) inherited from {http://www.opengis.net/ows/1.1}GetCapabilitiesType
    
    # Element Sections ({http://www.opengis.net/ows/1.1}Sections) inherited from {http://www.opengis.net/ows/1.1}GetCapabilitiesType
    
    # Element AcceptFormats ({http://www.opengis.net/ows/1.1}AcceptFormats) inherited from {http://www.opengis.net/ows/1.1}GetCapabilitiesType
    
    # Attribute updateSequence inherited from {http://www.opengis.net/ows/1.1}GetCapabilitiesType
    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__httpwww_opengis_netsos1_0_CTD_ANON_2_service', pyxb.bundles.opengis.ows_1_1.ServiceType, fixed=True, unicode_default='SOS', required=True)
    __service._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 33, 5)
    __service._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 33, 5)
    
    service = property(__service.value, __service.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __service.name() : __service
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.bundles.opengis.ows_1_1.CapabilitiesBaseType):
    """XML encoded SOS GetCapabilities operation response. This document provides clients with service metadata about a specific service instance, including metadata about the tightly-coupled data served. If the server does not implement the updateSequence parameter, the server shall always return the complete Capabilities document, without the updateSequence parameter. When the server implements the updateSequence parameter and the GetCapabilities operation request included the updateSequence parameter with the current value, the server shall return this element with only the "version" and "updateSequence" attributes. Otherwise, all optional elements shall be included or not depending on the actual value of the Sections parameter in the GetCapabilities operation request. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 43, 2)
    _ElementMap = pyxb.bundles.opengis.ows_1_1.CapabilitiesBaseType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.ows_1_1.CapabilitiesBaseType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.ows_1_1.CapabilitiesBaseType
    
    # Element OperationsMetadata ({http://www.opengis.net/ows/1.1}OperationsMetadata) inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Element ServiceIdentification ({http://www.opengis.net/ows/1.1}ServiceIdentification) inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Element ServiceProvider ({http://www.opengis.net/ows/1.1}ServiceProvider) inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Element {http://www.opengis.net/sos/1.0}Contents uses Python identifier Contents
    __Contents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Contents'), 'Contents', '__httpwww_opengis_netsos1_0_CTD_ANON_3_httpwww_opengis_netsos1_0Contents', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 26, 1), )

    
    Contents = property(__Contents.value, __Contents.set, None, 'Contents section of SOS service metadata (or Capabilites) XML document. For the SOS, these contents are data and functions that the SOS server provides.')

    
    # Element {http://www.opengis.net/sos/1.0}Filter_Capabilities uses Python identifier Filter_Capabilities
    __Filter_Capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Filter_Capabilities'), 'Filter_Capabilities', '__httpwww_opengis_netsos1_0_CTD_ANON_3_httpwww_opengis_netsos1_0Filter_Capabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 56, 1), )

    
    Filter_Capabilities = property(__Filter_Capabilities.value, __Filter_Capabilities.set, None, None)

    
    # Attribute version inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Attribute updateSequence inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    _ElementMap.update({
        __Contents.name() : __Contents,
        __Filter_Capabilities.name() : __Filter_Capabilities
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 57, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}Spatial_Capabilities uses Python identifier Spatial_Capabilities
    __Spatial_Capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Spatial_Capabilities'), 'Spatial_Capabilities', '__httpwww_opengis_netsos1_0_CTD_ANON_4_httpwww_opengis_netogcSpatial_Capabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 99, 2), )

    
    Spatial_Capabilities = property(__Spatial_Capabilities.value, __Spatial_Capabilities.set, None, None)

    
    # Element {http://www.opengis.net/ogc}Scalar_Capabilities uses Python identifier Scalar_Capabilities
    __Scalar_Capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Scalar_Capabilities'), 'Scalar_Capabilities', '__httpwww_opengis_netsos1_0_CTD_ANON_4_httpwww_opengis_netogcScalar_Capabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 100, 2), )

    
    Scalar_Capabilities = property(__Scalar_Capabilities.value, __Scalar_Capabilities.set, None, None)

    
    # Element {http://www.opengis.net/ogc}Id_Capabilities uses Python identifier Id_Capabilities
    __Id_Capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Id_Capabilities'), 'Id_Capabilities', '__httpwww_opengis_netsos1_0_CTD_ANON_4_httpwww_opengis_netogcId_Capabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 101, 2), )

    
    Id_Capabilities = property(__Id_Capabilities.value, __Id_Capabilities.set, None, None)

    
    # Element {http://www.opengis.net/ogc}Temporal_Capabilities uses Python identifier Temporal_Capabilities
    __Temporal_Capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Temporal_Capabilities'), 'Temporal_Capabilities', '__httpwww_opengis_netsos1_0_CTD_ANON_4_httpwww_opengis_netogcTemporal_Capabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 102, 2), )

    
    Temporal_Capabilities = property(__Temporal_Capabilities.value, __Temporal_Capabilities.set, None, None)

    _ElementMap.update({
        __Spatial_Capabilities.name() : __Spatial_Capabilities,
        __Scalar_Capabilities.name() : __Scalar_Capabilities,
        __Id_Capabilities.name() : __Id_Capabilities,
        __Temporal_Capabilities.name() : __Temporal_Capabilities
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Uses modified version of filter.xsd"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterest.xsd', 42, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}spatialOps uses Python identifier spatialOps
    __spatialOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'spatialOps'), 'spatialOps', '__httpwww_opengis_netsos1_0_CTD_ANON_5_httpwww_opengis_netogcspatialOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 80, 3), )

    
    spatialOps = property(__spatialOps.value, __spatialOps.set, None, None)

    _ElementMap.update({
        __spatialOps.name() : __spatialOps
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Uses modified version of filter.xsd 
								
								Allows a client to request targets from a specific instant, multiple instances or periods of time in the past, present and future. 
								This is useful for dynamic sensors for which the properties of the target are time-dependent. 
								Multiple time paramters may be indicated so that the client may request details of the observation target at multiple times. 
								The supported range is listed in the contents section of the service metadata."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterest.xsd', 58, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}temporalOps uses Python identifier temporalOps
    __temporalOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'temporalOps'), 'temporalOps', '__httpwww_opengis_netsos1_0_CTD_ANON_6_httpwww_opengis_netogctemporalOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 21, 2), )

    
    temporalOps = property(__temporalOps.value, __temporalOps.set, None, None)

    _ElementMap.update({
        __temporalOps.name() : __temporalOps
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Allows a client to request observations from a specific instant, multiple instances or periods of time in the past, present and future. The supported range is listed in the selected offering capabilities.
								"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 46, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}temporalOps uses Python identifier temporalOps
    __temporalOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'temporalOps'), 'temporalOps', '__httpwww_opengis_netsos1_0_CTD_ANON_7_httpwww_opengis_netogctemporalOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 21, 2), )

    
    temporalOps = property(__temporalOps.value, __temporalOps.set, None, None)

    _ElementMap.update({
        __temporalOps.name() : __temporalOps
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Specifies target feature for which observations are requested. Mostly a hepler for in-situ sensors, since geo-location has to be done on the server side. The supported area should be listed in the selected offering capabilities.
								"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 69, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}spatialOps uses Python identifier spatialOps
    __spatialOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'spatialOps'), 'spatialOps', '__httpwww_opengis_netsos1_0_CTD_ANON_8_httpwww_opengis_netogcspatialOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 80, 3), )

    
    spatialOps = property(__spatialOps.value, __spatialOps.set, None, None)

    
    # Element {http://www.opengis.net/sos/1.0}ObjectID uses Python identifier ObjectID
    __ObjectID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ObjectID'), 'ObjectID', '__httpwww_opengis_netsos1_0_CTD_ANON_8_httpwww_opengis_netsos1_0ObjectID', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 72, 9), )

    
    ObjectID = property(__ObjectID.value, __ObjectID.set, None, 'Unordered list of zero or more object identifiers. These identifiers are usually listed in the Contents section of the service metadata (Capabilities) document. If no ObjectID value is included, and if only one category of objects is allowed for this operation, the server shall return all objects of that category. NOTE: Although retention of this ability is allowed by a specific OWS that uses this operation, such retention is discouraged due to possible problems. Making this ability optional implementation by servers reduces interoperability. Requiring implementation of this ability can require a server to return a huge response, when there are a large number of items in that category. ')

    _ElementMap.update({
        __spatialOps.name() : __spatialOps,
        __ObjectID.name() : __ObjectID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Only report observations where the result matches this expression.
								"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 85, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}comparisonOps uses Python identifier comparisonOps
    __comparisonOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'comparisonOps'), 'comparisonOps', '__httpwww_opengis_netsos1_0_CTD_ANON_9_httpwww_opengis_netogccomparisonOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 49, 3), )

    
    comparisonOps = property(__comparisonOps.value, __comparisonOps.set, None, None)

    _ElementMap.update({
        __comparisonOps.name() : __comparisonOps
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Allows a client to request observations from a specific instant, multiple instances or periods of time in the past, present and future. The supported range is listed in the selected offering capabilities.
								"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 43, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}temporalOps uses Python identifier temporalOps
    __temporalOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'temporalOps'), 'temporalOps', '__httpwww_opengis_netsos1_0_CTD_ANON_10_httpwww_opengis_netogctemporalOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 21, 2), )

    
    temporalOps = property(__temporalOps.value, __temporalOps.set, None, None)

    _ElementMap.update({
        __temporalOps.name() : __temporalOps
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """the response of a GetResult operation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 61, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/sos/1.0}result uses Python identifier result
    __result = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'result'), 'result', '__httpwww_opengis_netsos1_0_CTD_ANON_11_httpwww_opengis_netsos1_0result', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 63, 4), )

    
    result = property(__result.value, __result.set, None, 'RS attribute points to the description of the reference system of the result. The description will contain all information necessary to understand what is provided within the result response. The most simple case would be a single value.')

    _ElementMap.update({
        __result.name() : __result
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """RS attribute points to the description of the reference system of the result. The description will contain all information necessary to understand what is provided within the result response. The most simple case would be a single value."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 67, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute RS uses Python identifier RS
    __RS = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'RS'), 'RS', '__httpwww_opengis_netsos1_0_CTD_ANON_12_RS', pyxb.binding.datatypes.anyURI, required=True)
    __RS._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 70, 8)
    __RS._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 70, 8)
    
    RS = property(__RS.value, __RS.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __RS.name() : __RS
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """returns the Id of the Observation assigend by the SOS"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosInsert.xsd', 56, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/sos/1.0}AssignedObservationId uses Python identifier AssignedObservationId
    __AssignedObservationId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AssignedObservationId'), 'AssignedObservationId', '__httpwww_opengis_netsos1_0_CTD_ANON_13_httpwww_opengis_netsos1_0AssignedObservationId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosInsert.xsd', 58, 4), )

    
    AssignedObservationId = property(__AssignedObservationId.value, __AssignedObservationId.set, None, None)

    _ElementMap.update({
        __AssignedObservationId.name() : __AssignedObservationId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 34, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """A template of the observations that will be inserted into the SOS."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 50, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/om/1.0}Observation uses Python identifier Observation
    __Observation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_om, 'Observation'), 'Observation', '__httpwww_opengis_netsos1_0_CTD_ANON_15_httpwww_opengis_netom1_0Observation', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 126, 1), )

    
    Observation = property(__Observation.value, __Observation.set, None, 'Observation is an act ("event"), whose result is an estimate of the value of a property of the feature of interest. \n            The observed property may be any property associated with the type of the feature of interest.')

    _ElementMap.update({
        __Observation.name() : __Observation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """returns the Id that is used in the insert operation to link the sensor to an Observation"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 63, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/sos/1.0}AssignedSensorId uses Python identifier AssignedSensorId
    __AssignedSensorId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AssignedSensorId'), 'AssignedSensorId', '__httpwww_opengis_netsos1_0_CTD_ANON_16_httpwww_opengis_netsos1_0AssignedSensorId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 65, 8), )

    
    AssignedSensorId = property(__AssignedSensorId.value, __AssignedSensorId.set, None, None)

    _ElementMap.update({
        __AssignedSensorId.name() : __AssignedSensorId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_16 = CTD_ANON_16


# Complex type {http://www.opengis.net/sos/1.0}ObservationOfferingType with content type ELEMENT_ONLY
class ObservationOfferingType (ObservationOfferingBaseType):
    """Complex type {http://www.opengis.net/sos/1.0}ObservationOfferingType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ObservationOfferingType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 57, 1)
    _ElementMap = ObservationOfferingBaseType._ElementMap.copy()
    _AttributeMap = ObservationOfferingBaseType._AttributeMap.copy()
    # Base type is ObservationOfferingBaseType
    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element {http://www.opengis.net/sos/1.0}intendedApplication uses Python identifier intendedApplication
    __intendedApplication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'intendedApplication'), 'intendedApplication', '__httpwww_opengis_netsos1_0_ObservationOfferingType_httpwww_opengis_netsos1_0intendedApplication', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 61, 5), )

    
    intendedApplication = property(__intendedApplication.value, __intendedApplication.set, None, None)

    
    # Element {http://www.opengis.net/sos/1.0}time uses Python identifier time
    __time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'time'), 'time', '__httpwww_opengis_netsos1_0_ObservationOfferingType_httpwww_opengis_netsos1_0time', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 62, 5), )

    
    time = property(__time.value, __time.set, None, None)

    
    # Element {http://www.opengis.net/sos/1.0}procedure uses Python identifier procedure
    __procedure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'procedure'), 'procedure', '__httpwww_opengis_netsos1_0_ObservationOfferingType_httpwww_opengis_netsos1_0procedure', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 63, 5), )

    
    procedure = property(__procedure.value, __procedure.set, None, None)

    
    # Element {http://www.opengis.net/sos/1.0}observedProperty uses Python identifier observedProperty
    __observedProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'observedProperty'), 'observedProperty', '__httpwww_opengis_netsos1_0_ObservationOfferingType_httpwww_opengis_netsos1_0observedProperty', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 64, 5), )

    
    observedProperty = property(__observedProperty.value, __observedProperty.set, None, None)

    
    # Element {http://www.opengis.net/sos/1.0}featureOfInterest uses Python identifier featureOfInterest
    __featureOfInterest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'featureOfInterest'), 'featureOfInterest', '__httpwww_opengis_netsos1_0_ObservationOfferingType_httpwww_opengis_netsos1_0featureOfInterest', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 65, 5), )

    
    featureOfInterest = property(__featureOfInterest.value, __featureOfInterest.set, None, None)

    
    # Element {http://www.opengis.net/sos/1.0}responseFormat uses Python identifier responseFormat
    __responseFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseFormat'), 'responseFormat', '__httpwww_opengis_netsos1_0_ObservationOfferingType_httpwww_opengis_netsos1_0responseFormat', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 66, 5), )

    
    responseFormat = property(__responseFormat.value, __responseFormat.set, None, None)

    
    # Element {http://www.opengis.net/sos/1.0}resultModel uses Python identifier resultModel
    __resultModel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'resultModel'), 'resultModel', '__httpwww_opengis_netsos1_0_ObservationOfferingType_httpwww_opengis_netsos1_0resultModel', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 67, 5), )

    
    resultModel = property(__resultModel.value, __resultModel.set, None, '\n\t\t\t\t\t\t\tIndicates the qualified name of the observation element that will be returned from a call to GetObservation for this offering.  \n\t\t\t\t\t\t\tThis element must be in the om:AbstractObservation substitution group and is typically the om:Observation or a specialized extension.\n\t\t\t\t\t\t\t')

    
    # Element {http://www.opengis.net/sos/1.0}responseMode uses Python identifier responseMode
    __responseMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseMode'), 'responseMode', '__httpwww_opengis_netsos1_0_ObservationOfferingType_httpwww_opengis_netsos1_0responseMode', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 75, 5), )

    
    responseMode = property(__responseMode.value, __responseMode.set, None, 'This element allows the client to request the form of the response.  The value of resultTemplate is used to retrieve an observation template \n\t\t\t\t\t\t\tthat will later be used in calls to GetResult.  The other options allow results to appear inline in a resultTag (inline), external to the observation element (out-of-band)\n\t\t\t\t\t\t\tor as a MIME attachment (attached)')

    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __intendedApplication.name() : __intendedApplication,
        __time.name() : __time,
        __procedure.name() : __procedure,
        __observedProperty.name() : __observedProperty,
        __featureOfInterest.name() : __featureOfInterest,
        __responseFormat.name() : __responseFormat,
        __resultModel.name() : __resultModel,
        __responseMode.name() : __responseMode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ObservationOfferingType = ObservationOfferingType
Namespace.addCategoryObject('typeBinding', 'ObservationOfferingType', ObservationOfferingType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (RequestBaseType):
    """Request to a SOS to perform the DescribeFeatureType operation. This operation is designed to request detailed information concerning the observation's target"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeFeatureType.xsd', 27, 2)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/sos/1.0}FeatureId uses Python identifier FeatureId
    __FeatureId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FeatureId'), 'FeatureId', '__httpwww_opengis_netsos1_0_CTD_ANON_17_httpwww_opengis_netsos1_0FeatureId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeFeatureType.xsd', 31, 6), )

    
    FeatureId = property(__FeatureId.value, __FeatureId.set, None, 'Identifier of the feature for which detailed information is requested. These identifiers are usually listed in the Contents section of the service metadata (Capabilities) document. ')

    
    # Attribute service inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    _ElementMap.update({
        __FeatureId.name() : __FeatureId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_17 = CTD_ANON_17


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (RequestBaseType):
    """Request to a SOS to perform the DescribeObservationTypeoperation. This operation is designed to request detailed information concerning hard typed observation schemas"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeObservationType.xsd', 27, 2)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/sos/1.0}observedProperty uses Python identifier observedProperty
    __observedProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'observedProperty'), 'observedProperty', '__httpwww_opengis_netsos1_0_CTD_ANON_18_httpwww_opengis_netsos1_0observedProperty', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeObservationType.xsd', 31, 6), )

    
    observedProperty = property(__observedProperty.value, __observedProperty.set, None, 'The phenomenon for which the observationType (OM application schema) is requested.')

    
    # Attribute service inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    _ElementMap.update({
        __observedProperty.name() : __observedProperty
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_18 = CTD_ANON_18


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (RequestBaseType):
    """Request to a SOS to perform the DescribeResultModel operation. 
			This operation is designed to request detailed information concerning the format of the observation's result"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeResultModel.xsd', 28, 2)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/sos/1.0}ResultName uses Python identifier ResultName
    __ResultName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResultName'), 'ResultName', '__httpwww_opengis_netsos1_0_CTD_ANON_19_httpwww_opengis_netsos1_0ResultName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeResultModel.xsd', 32, 6), )

    
    ResultName = property(__ResultName.value, __ResultName.set, None, 'Identifier of the type of the result, for which detailed information is requested.')

    
    # Attribute service inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    _ElementMap.update({
        __ResultName.name() : __ResultName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_19 = CTD_ANON_19


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (RequestBaseType):
    """Request to a SOS to perform the DescribeSensor operation. This operation is designed to request detailed sensor metadata.	"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeSensor.xsd', 28, 2)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/sos/1.0}procedure uses Python identifier procedure
    __procedure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'procedure'), 'procedure', '__httpwww_opengis_netsos1_0_CTD_ANON_20_httpwww_opengis_netsos1_0procedure', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeSensor.xsd', 32, 6), )

    
    procedure = property(__procedure.value, __procedure.set, None, 'Identifier of the sensor, for which detailed metadata is requested.')

    
    # Attribute service inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    
    # Attribute outputFormat uses Python identifier outputFormat
    __outputFormat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'outputFormat'), 'outputFormat', '__httpwww_opengis_netsos1_0_CTD_ANON_20_outputFormat', pyxb.bundles.opengis.ows_1_1.MimeType, required=True)
    __outputFormat._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeSensor.xsd', 38, 5)
    __outputFormat._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeSensor.xsd', 38, 5)
    
    outputFormat = property(__outputFormat.value, __outputFormat.set, None, 'Identifier of the output format to be used for the requested data. The outputFormats supported by a SOS server are listed in the operations metadata section of the service metadata (capabilities XML). If this attribute is omitted, the outputFormat should be tex/xml;subtype="sensorML/1.0.0". If the requested outputFormat is not supported by the SOS server, an exception message shall be returned.\n\t\t\t\t')

    _ElementMap.update({
        __procedure.name() : __procedure
    })
    _AttributeMap.update({
        __outputFormat.name() : __outputFormat
    })
_module_typeBindings.CTD_ANON_20 = CTD_ANON_20


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (RequestBaseType):
    """Request to a SOS to perform the GetFeatureOfInterest operation. This operation is designed to request target feaure instances"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterest.xsd', 28, 2)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/sos/1.0}FeatureOfInterestId uses Python identifier FeatureOfInterestId
    __FeatureOfInterestId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FeatureOfInterestId'), 'FeatureOfInterestId', '__httpwww_opengis_netsos1_0_CTD_ANON_21_httpwww_opengis_netsos1_0FeatureOfInterestId', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterest.xsd', 33, 7), )

    
    FeatureOfInterestId = property(__FeatureOfInterestId.value, __FeatureOfInterestId.set, None, 'Identifier of the feature of interest, for which detailed information is requested. These identifiers are usually listed in the Contents section of the service metadata (Capabilities) document. ')

    
    # Element {http://www.opengis.net/sos/1.0}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'location'), 'location', '__httpwww_opengis_netsos1_0_CTD_ANON_21_httpwww_opengis_netsos1_0location', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterest.xsd', 38, 7), )

    
    location = property(__location.value, __location.set, None, 'Uses modified version of filter.xsd')

    
    # Element {http://www.opengis.net/sos/1.0}eventTime uses Python identifier eventTime
    __eventTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eventTime'), 'eventTime', '__httpwww_opengis_netsos1_0_CTD_ANON_21_httpwww_opengis_netsos1_0eventTime', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterest.xsd', 49, 6), )

    
    eventTime = property(__eventTime.value, __eventTime.set, None, 'Uses modified version of filter.xsd \n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\tAllows a client to request targets from a specific instant, multiple instances or periods of time in the past, present and future. \n\t\t\t\t\t\t\t\tThis is useful for dynamic sensors for which the properties of the target are time-dependent. \n\t\t\t\t\t\t\t\tMultiple time paramters may be indicated so that the client may request details of the observation target at multiple times. \n\t\t\t\t\t\t\t\tThe supported range is listed in the contents section of the service metadata.')

    
    # Attribute service inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    _ElementMap.update({
        __FeatureOfInterestId.name() : __FeatureOfInterestId,
        __location.name() : __location,
        __eventTime.name() : __eventTime
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_21 = CTD_ANON_21


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22 (RequestBaseType):
    """Request to a SOS to perform the GetTargetTime operation. 
			This operation is designed to request the time that specified target feature instances or target locations are available"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterestTime.xsd', 30, 2)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/sos/1.0}FeatureOfInterestId uses Python identifier FeatureOfInterestId
    __FeatureOfInterestId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FeatureOfInterestId'), 'FeatureOfInterestId', '__httpwww_opengis_netsos1_0_CTD_ANON_22_httpwww_opengis_netsos1_0FeatureOfInterestId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterestTime.xsd', 34, 6), )

    
    FeatureOfInterestId = property(__FeatureOfInterestId.value, __FeatureOfInterestId.set, None, 'Identifier of the feature of interest, for which detailed information is requested. These identifiers are usually listed in the Contents section of the service metadata (Capabilities) document. ')

    
    # Attribute service inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    _ElementMap.update({
        __FeatureOfInterestId.name() : __FeatureOfInterestId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_22 = CTD_ANON_22


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_23 (RequestBaseType):
    """Request to a SOS to perform the GetObservation operation. This operation is designed to request sensor data from live sensors as well as sensor data archives."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 30, 2)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/sos/1.0}offering uses Python identifier offering
    __offering = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'offering'), 'offering', '__httpwww_opengis_netsos1_0_CTD_ANON_23_httpwww_opengis_netsos1_0offering', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 34, 6), )

    
    offering = property(__offering.value, __offering.set, None, 'ID of an offering advertised in the capabilities.\n\t\t\t\t\t\t\t\t\tAll following parameters are depending on the selected offering.\n\t\t\t\t\t\t\t\t')

    
    # Element {http://www.opengis.net/sos/1.0}eventTime uses Python identifier eventTime
    __eventTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eventTime'), 'eventTime', '__httpwww_opengis_netsos1_0_CTD_ANON_23_httpwww_opengis_netsos1_0eventTime', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 41, 6), )

    
    eventTime = property(__eventTime.value, __eventTime.set, None, 'Allows a client to request observations from a specific instant, multiple instances or periods of time in the past, present and future. The supported range is listed in the selected offering capabilities.\n\t\t\t\t\t\t\t\t')

    
    # Element {http://www.opengis.net/sos/1.0}procedure uses Python identifier procedure
    __procedure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'procedure'), 'procedure', '__httpwww_opengis_netsos1_0_CTD_ANON_23_httpwww_opengis_netsos1_0procedure', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 52, 6), )

    
    procedure = property(__procedure.value, __procedure.set, None, "Index of a particular sensor if offering procedure is a Sensor Array. Allows client to request data from one or more sensors in the array. The size of the array should be specified in the selected offering capabilities. This is to support scenarios with sensor grids (we don't want to have one offering for each sensor in that case). Note that sensorML can describe Sensor Arrays too. \t\t\t\t\t\t\t\t\t\t")

    
    # Element {http://www.opengis.net/sos/1.0}observedProperty uses Python identifier observedProperty
    __observedProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'observedProperty'), 'observedProperty', '__httpwww_opengis_netsos1_0_CTD_ANON_23_httpwww_opengis_netsos1_0observedProperty', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 57, 6), )

    
    observedProperty = property(__observedProperty.value, __observedProperty.set, None, 'ID of a phenomenon advertised in capabilities document.\n\t\t\t\t\t\t\t\t\tAll possible phenomena are listed in the selected offering capabilities.\n\t\t\t\t\t\t\t\t')

    
    # Element {http://www.opengis.net/sos/1.0}featureOfInterest uses Python identifier featureOfInterest
    __featureOfInterest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'featureOfInterest'), 'featureOfInterest', '__httpwww_opengis_netsos1_0_CTD_ANON_23_httpwww_opengis_netsos1_0featureOfInterest', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 64, 6), )

    
    featureOfInterest = property(__featureOfInterest.value, __featureOfInterest.set, None, 'Specifies target feature for which observations are requested. Mostly a hepler for in-situ sensors, since geo-location has to be done on the server side. The supported area should be listed in the selected offering capabilities.\n\t\t\t\t\t\t\t\t')

    
    # Element {http://www.opengis.net/sos/1.0}result uses Python identifier result
    __result = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'result'), 'result', '__httpwww_opengis_netsos1_0_CTD_ANON_23_httpwww_opengis_netsos1_0result', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 80, 6), )

    
    result = property(__result.value, __result.set, None, 'Only report observations where the result matches this expression.\n\t\t\t\t\t\t\t\t')

    
    # Element {http://www.opengis.net/sos/1.0}responseFormat uses Python identifier responseFormat
    __responseFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseFormat'), 'responseFormat', '__httpwww_opengis_netsos1_0_CTD_ANON_23_httpwww_opengis_netsos1_0responseFormat', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 91, 6), )

    
    responseFormat = property(__responseFormat.value, __responseFormat.set, None, 'ID of the output format to be used for the requested data. The supported output formats are listed in the selected offering capabilities.\n\t\t\t\t\t\t\t\t')

    
    # Element {http://www.opengis.net/sos/1.0}resultModel uses Python identifier resultModel
    __resultModel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'resultModel'), 'resultModel', '__httpwww_opengis_netsos1_0_CTD_ANON_23_httpwww_opengis_netsos1_0resultModel', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 97, 6), )

    
    resultModel = property(__resultModel.value, __resultModel.set, None, 'Identifier of the result model to be used for the requested data. The resultModel values supported by a SOS server are listed in the contents section of the service metadata, identified as QName values.  If the requested resultModel is not supported by the SOS server, an exception message shall be returned.\n\t\t\t\t\t\t\t')

    
    # Element {http://www.opengis.net/sos/1.0}responseMode uses Python identifier responseMode
    __responseMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseMode'), 'responseMode', '__httpwww_opengis_netsos1_0_CTD_ANON_23_httpwww_opengis_netsos1_0responseMode', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 103, 6), )

    
    responseMode = property(__responseMode.value, __responseMode.set, None, 'This element allows the client to request the form of the response.  The value of resultTemplate is used to retrieve an observation template \n\t\t\t\t\t\t\tthat will later be used in calls to GetResult.  The other options allow results to appear inline in a resultTag (inline), external to the observation element (out-of-band)\n\t\t\t\t\t\t\tor as a MIME attachment (attached)')

    
    # Attribute service inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    
    # Attribute srsName uses Python identifier srsName
    __srsName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'srsName'), 'srsName', '__httpwww_opengis_netsos1_0_CTD_ANON_23_srsName', pyxb.binding.datatypes.anyURI)
    __srsName._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 111, 5)
    __srsName._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 111, 5)
    
    srsName = property(__srsName.value, __srsName.set, None, None)

    _ElementMap.update({
        __offering.name() : __offering,
        __eventTime.name() : __eventTime,
        __procedure.name() : __procedure,
        __observedProperty.name() : __observedProperty,
        __featureOfInterest.name() : __featureOfInterest,
        __result.name() : __result,
        __responseFormat.name() : __responseFormat,
        __resultModel.name() : __resultModel,
        __responseMode.name() : __responseMode
    })
    _AttributeMap.update({
        __srsName.name() : __srsName
    })
_module_typeBindings.CTD_ANON_23 = CTD_ANON_23


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_24 (RequestBaseType):
    """Request to a SOS to perform the GetObservation operation using an Observation ID."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 29, 2)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/sos/1.0}ObservationId uses Python identifier ObservationId
    __ObservationId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ObservationId'), 'ObservationId', '__httpwww_opengis_netsos1_0_CTD_ANON_24_httpwww_opengis_netsos1_0ObservationId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 33, 6), )

    
    ObservationId = property(__ObservationId.value, __ObservationId.set, None, 'ID of the observation to obtain.  This could have been obtained by the client via a URL in a feed, alert, or some other notification\n\t\t\t\t\t\t\t\t')

    
    # Element {http://www.opengis.net/sos/1.0}responseFormat uses Python identifier responseFormat
    __responseFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseFormat'), 'responseFormat', '__httpwww_opengis_netsos1_0_CTD_ANON_24_httpwww_opengis_netsos1_0responseFormat', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 39, 6), )

    
    responseFormat = property(__responseFormat.value, __responseFormat.set, None, 'ID of the output format to be used for the requested data. The supported output formats are listed in the selected offering capabilities.\n\t\t\t\t\t\t\t\t')

    
    # Element {http://www.opengis.net/sos/1.0}resultModel uses Python identifier resultModel
    __resultModel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'resultModel'), 'resultModel', '__httpwww_opengis_netsos1_0_CTD_ANON_24_httpwww_opengis_netsos1_0resultModel', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 45, 6), )

    
    resultModel = property(__resultModel.value, __resultModel.set, None, None)

    
    # Element {http://www.opengis.net/sos/1.0}responseMode uses Python identifier responseMode
    __responseMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseMode'), 'responseMode', '__httpwww_opengis_netsos1_0_CTD_ANON_24_httpwww_opengis_netsos1_0responseMode', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 46, 6), )

    
    responseMode = property(__responseMode.value, __responseMode.set, None, 'This element allows the client to request the form of the response.  The value of resultTemplate is used to retrieve an observation template \n\t\t\t\t\t\t\tthat will later be used in calls to GetResult.  The other options allow results to appear inline in a resultTag (inline), external to the observation element (out-of-band)\n\t\t\t\t\t\t\tor as a MIME attachment (attached)')

    
    # Attribute service inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    
    # Attribute srsName uses Python identifier srsName
    __srsName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'srsName'), 'srsName', '__httpwww_opengis_netsos1_0_CTD_ANON_24_srsName', pyxb.binding.datatypes.anyURI)
    __srsName._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 54, 5)
    __srsName._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 54, 5)
    
    srsName = property(__srsName.value, __srsName.set, None, None)

    _ElementMap.update({
        __ObservationId.name() : __ObservationId,
        __responseFormat.name() : __responseFormat,
        __resultModel.name() : __resultModel,
        __responseMode.name() : __responseMode
    })
    _AttributeMap.update({
        __srsName.name() : __srsName
    })
_module_typeBindings.CTD_ANON_24 = CTD_ANON_24


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25 (RequestBaseType):
    """request to a SOS to perform a GetResult operation. this operation is designed to request sensor data from live sensors. Instead of retriveing the observations as a full OM document, you will get an simple value and a link to the reference system"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 28, 2)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/sos/1.0}ObservationTemplateId uses Python identifier ObservationTemplateId
    __ObservationTemplateId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ObservationTemplateId'), 'ObservationTemplateId', '__httpwww_opengis_netsos1_0_CTD_ANON_25_httpwww_opengis_netsos1_0ObservationTemplateId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 32, 6), )

    
    ObservationTemplateId = property(__ObservationTemplateId.value, __ObservationTemplateId.set, None, 'The gml:id of an previous GetObservation request response indicating observations from a certain sensor for a certain target.\n\t\t\t\t\t\t\t\t')

    
    # Element {http://www.opengis.net/sos/1.0}eventTime uses Python identifier eventTime
    __eventTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eventTime'), 'eventTime', '__httpwww_opengis_netsos1_0_CTD_ANON_25_httpwww_opengis_netsos1_0eventTime', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 38, 6), )

    
    eventTime = property(__eventTime.value, __eventTime.set, None, 'Allows a client to request observations from a specific instant, multiple instances or periods of time in the past, present and future. The supported range is listed in the selected offering capabilities.\n\t\t\t\t\t\t\t\t')

    
    # Attribute service inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    _ElementMap.update({
        __ObservationTemplateId.name() : __ObservationTemplateId,
        __eventTime.name() : __eventTime
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_25 = CTD_ANON_25


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_26 (RequestBaseType):
    """Request to a SOS to perform the Insert operation. This operation is designed to insert new observations. The request is constraint by the following parameters: ID obtained by the registerSensor operation (identifying the sensor and the observyationType, and the observation encoded as OM"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosInsert.xsd', 30, 2)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/om/1.0}Observation uses Python identifier Observation
    __Observation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_om, 'Observation'), 'Observation', '__httpwww_opengis_netsos1_0_CTD_ANON_26_httpwww_opengis_netom1_0Observation', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 126, 1), )

    
    Observation = property(__Observation.value, __Observation.set, None, 'Observation is an act ("event"), whose result is an estimate of the value of a property of the feature of interest. \n            The observed property may be any property associated with the type of the feature of interest.')

    
    # Element {http://www.opengis.net/sos/1.0}AssignedSensorId uses Python identifier AssignedSensorId
    __AssignedSensorId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AssignedSensorId'), 'AssignedSensorId', '__httpwww_opengis_netsos1_0_CTD_ANON_26_httpwww_opengis_netsos1_0AssignedSensorId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosInsert.xsd', 34, 6), )

    
    AssignedSensorId = property(__AssignedSensorId.value, __AssignedSensorId.set, None, 'The id obtained by the registerSensor operation.')

    
    # Attribute service inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    _ElementMap.update({
        __Observation.name() : __Observation,
        __AssignedSensorId.name() : __AssignedSensorId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_26 = CTD_ANON_26


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_27 (RequestBaseType):
    """Request to a SOS to perform the registerSensor operation. This operation is designed to register new sensors at the SOS."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 29, 4)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/sos/1.0}SensorDescription uses Python identifier SensorDescription
    __SensorDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SensorDescription'), 'SensorDescription', '__httpwww_opengis_netsos1_0_CTD_ANON_27_httpwww_opengis_netsos1_0SensorDescription', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 33, 12), )

    
    SensorDescription = property(__SensorDescription.value, __SensorDescription.set, None, None)

    
    # Element {http://www.opengis.net/sos/1.0}ObservationTemplate uses Python identifier ObservationTemplate
    __ObservationTemplate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ObservationTemplate'), 'ObservationTemplate', '__httpwww_opengis_netsos1_0_CTD_ANON_27_httpwww_opengis_netsos1_0ObservationTemplate', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 46, 2), )

    
    ObservationTemplate = property(__ObservationTemplate.value, __ObservationTemplate.set, None, 'A template of the observations that will be inserted into the SOS.')

    
    # Attribute service inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/sos/1.0}RequestBaseType
    _ElementMap.update({
        __SensorDescription.name() : __SensorDescription,
        __ObservationTemplate.name() : __ObservationTemplate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_27 = CTD_ANON_27


srsName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'srsName'), pyxb.bundles.opengis.gml.CodeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 87, 1))
Namespace.addCategoryObject('elementBinding', srsName.name().localName(), srsName)

supportedSensorDescription = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supportedSensorDescription'), pyxb.binding.datatypes.QName, documentation='The QName of the root of a sensor desription that is supported by this service.  Examples are "sml:_Process" and "tml:system"', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 88, 1))
Namespace.addCategoryObject('elementBinding', supportedSensorDescription.name().localName(), supportedSensorDescription)

supportedSRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supportedSRS'), pyxb.bundles.opengis.gml.CodeType, documentation='The name by which this reference system is identified.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 93, 1))
Namespace.addCategoryObject('elementBinding', supportedSRS.name().localName(), supportedSRS)

Contents = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contents'), CTD_ANON, documentation='Contents section of SOS service metadata (or Capabilites) XML document. For the SOS, these contents are data and functions that the SOS server provides.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 26, 1))
Namespace.addCategoryObject('elementBinding', Contents.name().localName(), Contents)

GetCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetCapabilities'), CTD_ANON_2, documentation='Request to a SOS to perform the GetCapabilities operation. This operation allows a client to retrieve service metadata (capabilities XML) providing metadata for the specific SOS server. In this XML encoding, no "request" parameter is included, since the element name specifies the specific operation. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 25, 1))
Namespace.addCategoryObject('elementBinding', GetCapabilities.name().localName(), GetCapabilities)

Capabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Capabilities'), CTD_ANON_3, documentation='XML encoded SOS GetCapabilities operation response. This document provides clients with service metadata about a specific service instance, including metadata about the tightly-coupled data served. If the server does not implement the updateSequence parameter, the server shall always return the complete Capabilities document, without the updateSequence parameter. When the server implements the updateSequence parameter and the GetCapabilities operation request included the updateSequence parameter with the current value, the server shall return this element with only the "version" and "updateSequence" attributes. Otherwise, all optional elements shall be included or not depending on the actual value of the Sections parameter in the GetCapabilities operation request. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 39, 1))
Namespace.addCategoryObject('elementBinding', Capabilities.name().localName(), Capabilities)

Filter_Capabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Filter_Capabilities'), CTD_ANON_4, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 56, 1))
Namespace.addCategoryObject('elementBinding', Filter_Capabilities.name().localName(), Filter_Capabilities)

GetResultResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetResultResponse'), CTD_ANON_11, documentation='the response of a GetResult operation', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 57, 1))
Namespace.addCategoryObject('elementBinding', GetResultResponse.name().localName(), GetResultResponse)

InsertObservationResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InsertObservationResponse'), CTD_ANON_13, documentation='returns the Id of the Observation assigend by the SOS', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosInsert.xsd', 52, 1))
Namespace.addCategoryObject('elementBinding', InsertObservationResponse.name().localName(), InsertObservationResponse)

ObservationTemplate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObservationTemplate'), CTD_ANON_15, documentation='A template of the observations that will be inserted into the SOS.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 46, 2))
Namespace.addCategoryObject('elementBinding', ObservationTemplate.name().localName(), ObservationTemplate)

RegisterSensorResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RegisterSensorResponse'), CTD_ANON_16, documentation='returns the Id that is used in the insert operation to link the sensor to an Observation', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 59, 2))
Namespace.addCategoryObject('elementBinding', RegisterSensorResponse.name().localName(), RegisterSensorResponse)

DescribeFeatureType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescribeFeatureType'), CTD_ANON_17, documentation="Request to a SOS to perform the DescribeFeatureType operation. This operation is designed to request detailed information concerning the observation's target", location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeFeatureType.xsd', 23, 1))
Namespace.addCategoryObject('elementBinding', DescribeFeatureType.name().localName(), DescribeFeatureType)

DescribeObservationType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescribeObservationType'), CTD_ANON_18, documentation='Request to a SOS to perform the DescribeObservationTypeoperation. This operation is designed to request detailed information concerning hard typed observation schemas', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeObservationType.xsd', 23, 1))
Namespace.addCategoryObject('elementBinding', DescribeObservationType.name().localName(), DescribeObservationType)

DescribeResultModel = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescribeResultModel'), CTD_ANON_19, documentation="Request to a SOS to perform the DescribeResultModel operation. \n\t\t\tThis operation is designed to request detailed information concerning the format of the observation's result", location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeResultModel.xsd', 23, 1))
Namespace.addCategoryObject('elementBinding', DescribeResultModel.name().localName(), DescribeResultModel)

DescribeSensor = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescribeSensor'), CTD_ANON_20, documentation='Request to a SOS to perform the DescribeSensor operation. This operation is designed to request detailed sensor metadata.\t', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeSensor.xsd', 24, 1))
Namespace.addCategoryObject('elementBinding', DescribeSensor.name().localName(), DescribeSensor)

GetFeatureOfInterest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetFeatureOfInterest'), CTD_ANON_21, documentation='Request to a SOS to perform the GetFeatureOfInterest operation. This operation is designed to request target feaure instances', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterest.xsd', 24, 1))
Namespace.addCategoryObject('elementBinding', GetFeatureOfInterest.name().localName(), GetFeatureOfInterest)

GetFeatureOfInterestTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetFeatureOfInterestTime'), CTD_ANON_22, documentation='Request to a SOS to perform the GetTargetTime operation. \n\t\t\tThis operation is designed to request the time that specified target feature instances or target locations are available', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterestTime.xsd', 25, 1))
Namespace.addCategoryObject('elementBinding', GetFeatureOfInterestTime.name().localName(), GetFeatureOfInterestTime)

GetObservation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetObservation'), CTD_ANON_23, documentation='Request to a SOS to perform the GetObservation operation. This operation is designed to request sensor data from live sensors as well as sensor data archives.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 26, 1))
Namespace.addCategoryObject('elementBinding', GetObservation.name().localName(), GetObservation)

GetObservationById = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetObservationById'), CTD_ANON_24, documentation='Request to a SOS to perform the GetObservation operation using an Observation ID.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 25, 1))
Namespace.addCategoryObject('elementBinding', GetObservationById.name().localName(), GetObservationById)

GetResult = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetResult'), CTD_ANON_25, documentation='request to a SOS to perform a GetResult operation. this operation is designed to request sensor data from live sensors. Instead of retriveing the observations as a full OM document, you will get an simple value and a link to the reference system', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 24, 1))
Namespace.addCategoryObject('elementBinding', GetResult.name().localName(), GetResult)

InsertObservation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InsertObservation'), CTD_ANON_26, documentation='Request to a SOS to perform the Insert operation. This operation is designed to insert new observations. The request is constraint by the following parameters: ID obtained by the registerSensor operation (identifying the sensor and the observyationType, and the observation encoded as OM', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosInsert.xsd', 26, 1))
Namespace.addCategoryObject('elementBinding', InsertObservation.name().localName(), InsertObservation)

RegisterSensor = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RegisterSensor'), CTD_ANON_27, documentation='Request to a SOS to perform the registerSensor operation. This operation is designed to register new sensors at the SOS.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 25, 2))
Namespace.addCategoryObject('elementBinding', RegisterSensor.name().localName(), RegisterSensor)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObservationOfferingList'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 32, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ObservationOfferingList')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 32, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObservationOffering'), ObservationOfferingType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 35, 7)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ObservationOffering')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 35, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationOfferingBaseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationOfferingBaseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationOfferingBaseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ObservationOfferingBaseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 51, 5))
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
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ObservationOfferingBaseType._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
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
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'AcceptVersions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 49, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Sections')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 54, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'AcceptFormats')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 59, 3))
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
CTD_ANON_2._Automaton = _BuildAutomaton_3()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contents'), CTD_ANON, scope=CTD_ANON_3, documentation='Contents section of SOS service metadata (or Capabilites) XML document. For the SOS, these contents are data and functions that the SOS server provides.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 26, 1)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Filter_Capabilities'), CTD_ANON_4, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 56, 1)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 30, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 31, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 32, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 47, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 48, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'ServiceIdentification')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 30, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'ServiceProvider')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'OperationsMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsGetCapabilities.xsd', 32, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filter_Capabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 47, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contents')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 48, 6))
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
CTD_ANON_3._Automaton = _BuildAutomaton_4()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Spatial_Capabilities'), pyxb.bundles.opengis.filter.Spatial_CapabilitiesType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 99, 2)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Scalar_Capabilities'), pyxb.bundles.opengis.filter.Scalar_CapabilitiesType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 100, 2)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Id_Capabilities'), pyxb.bundles.opengis.filter.Id_CapabilitiesType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 101, 2)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Temporal_Capabilities'), pyxb.bundles.opengis._ogc.Temporal_CapabilitiesType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 102, 2)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Spatial_Capabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 59, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Temporal_Capabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 60, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Scalar_Capabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 61, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Id_Capabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetCapabilities.xsd', 62, 4))
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
CTD_ANON_4._Automaton = _BuildAutomaton_5()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'spatialOps'), pyxb.bundles.opengis.filter.SpatialOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 80, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'spatialOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterest.xsd', 44, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_6()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'temporalOps'), pyxb.bundles.opengis._ogc.TemporalOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 21, 2)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'temporalOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterest.xsd', 60, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_7()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'temporalOps'), pyxb.bundles.opengis._ogc.TemporalOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 21, 2)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'temporalOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 48, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_8()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'spatialOps'), pyxb.bundles.opengis.filter.SpatialOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 80, 3)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObjectID'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_8, documentation='Unordered list of zero or more object identifiers. These identifiers are usually listed in the Contents section of the service metadata (Capabilities) document. If no ObjectID value is included, and if only one category of objects is allowed for this operation, the server shall return all objects of that category. NOTE: Although retention of this ability is allowed by a specific OWS that uses this operation, such retention is discouraged due to possible problems. Making this ability optional implementation by servers reduces interoperability. Requiring implementation of this ability can require a server to return a huge response, when there are a large number of items in that category. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 72, 9)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'spatialOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 71, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ObjectID')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 72, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_9()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'comparisonOps'), pyxb.bundles.opengis.filter.ComparisonOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 49, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'comparisonOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 87, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_10()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'temporalOps'), pyxb.bundles.opengis._ogc.TemporalOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 21, 2)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'temporalOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 45, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_11()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'result'), CTD_ANON_12, scope=CTD_ANON_11, documentation='RS attribute points to the description of the reference system of the result. The description will contain all information necessary to understand what is provided within the result response. The most simple case would be a single value.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 63, 4)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'result')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 63, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_12()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AssignedObservationId'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosInsert.xsd', 58, 4)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AssignedObservationId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosInsert.xsd', 58, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_13()




def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.opengis.net/sos/1.0')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 36, 18))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_14()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_om, 'Observation'), pyxb.bundles.opengis.om_1_0.ObservationType, scope=CTD_ANON_15, documentation='Observation is an act ("event"), whose result is an estimate of the value of a property of the feature of interest. \n            The observed property may be any property associated with the type of the feature of interest.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 126, 1)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(_Namespace_om, 'Observation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 52, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_15()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AssignedSensorId'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 65, 8)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AssignedSensorId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 65, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_16()




ObservationOfferingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'intendedApplication'), pyxb.binding.datatypes.token, scope=ObservationOfferingType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 61, 5)))

ObservationOfferingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'time'), pyxb.bundles.opengis.swe_1_0_1.TimeGeometricPrimitivePropertyType, scope=ObservationOfferingType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 62, 5)))

ObservationOfferingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'procedure'), pyxb.bundles.opengis.gml.ReferenceType, scope=ObservationOfferingType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 63, 5)))

ObservationOfferingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'observedProperty'), pyxb.bundles.opengis.swe_1_0_1.PhenomenonPropertyType, scope=ObservationOfferingType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 64, 5)))

ObservationOfferingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'featureOfInterest'), pyxb.bundles.opengis.gml.ReferenceType, scope=ObservationOfferingType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 65, 5)))

ObservationOfferingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseFormat'), pyxb.bundles.opengis.ows_1_1.MimeType, scope=ObservationOfferingType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 66, 5)))

ObservationOfferingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'resultModel'), pyxb.binding.datatypes.QName, scope=ObservationOfferingType, documentation='\n\t\t\t\t\t\t\tIndicates the qualified name of the observation element that will be returned from a call to GetObservation for this offering.  \n\t\t\t\t\t\t\tThis element must be in the om:AbstractObservation substitution group and is typically the om:Observation or a specialized extension.\n\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 67, 5)))

ObservationOfferingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseMode'), responseModeType, scope=ObservationOfferingType, documentation='This element allows the client to request the form of the response.  The value of resultTemplate is used to retrieve an observation template \n\t\t\t\t\t\t\tthat will later be used in calls to GetResult.  The other options allow results to appear inline in a resultTag (inline), external to the observation element (out-of-band)\n\t\t\t\t\t\t\tor as a MIME attachment (attached)', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 75, 5)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 61, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 67, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 75, 5))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationOfferingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationOfferingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationOfferingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationOfferingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 51, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationOfferingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'intendedApplication')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 61, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationOfferingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'time')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 62, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationOfferingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'procedure')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 63, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationOfferingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'observedProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 64, 5))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationOfferingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'featureOfInterest')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 65, 5))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ObservationOfferingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseFormat')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 66, 5))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ObservationOfferingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'resultModel')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 67, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ObservationOfferingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseMode')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosContents.xsd', 75, 5))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
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
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ObservationOfferingType._Automaton = _BuildAutomaton_17()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FeatureId'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_17, documentation='Identifier of the feature for which detailed information is requested. These identifiers are usually listed in the Contents section of the service metadata (Capabilities) document. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeFeatureType.xsd', 31, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FeatureId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeFeatureType.xsd', 31, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_18()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'observedProperty'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_18, documentation='The phenomenon for which the observationType (OM application schema) is requested.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeObservationType.xsd', 31, 6)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'observedProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeObservationType.xsd', 31, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_19()




CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResultName'), pyxb.binding.datatypes.QName, scope=CTD_ANON_19, documentation='Identifier of the type of the result, for which detailed information is requested.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeResultModel.xsd', 32, 6)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResultName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeResultModel.xsd', 32, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_20()




CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'procedure'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_20, documentation='Identifier of the sensor, for which detailed metadata is requested.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeSensor.xsd', 32, 6)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'procedure')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosDescribeSensor.xsd', 32, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_21()




CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FeatureOfInterestId'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_21, documentation='Identifier of the feature of interest, for which detailed information is requested. These identifiers are usually listed in the Contents section of the service metadata (Capabilities) document. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterest.xsd', 33, 7)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'location'), CTD_ANON_5, scope=CTD_ANON_21, documentation='Uses modified version of filter.xsd', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterest.xsd', 38, 7)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eventTime'), CTD_ANON_6, scope=CTD_ANON_21, documentation='Uses modified version of filter.xsd \n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\tAllows a client to request targets from a specific instant, multiple instances or periods of time in the past, present and future. \n\t\t\t\t\t\t\t\tThis is useful for dynamic sensors for which the properties of the target are time-dependent. \n\t\t\t\t\t\t\t\tMultiple time paramters may be indicated so that the client may request details of the observation target at multiple times. \n\t\t\t\t\t\t\t\tThe supported range is listed in the contents section of the service metadata.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterest.xsd', 49, 6)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterest.xsd', 49, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FeatureOfInterestId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterest.xsd', 33, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'location')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterest.xsd', 38, 7))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eventTime')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterest.xsd', 49, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_2, [
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
CTD_ANON_21._Automaton = _BuildAutomaton_22()




CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FeatureOfInterestId'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_22, documentation='Identifier of the feature of interest, for which detailed information is requested. These identifiers are usually listed in the Contents section of the service metadata (Capabilities) document. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterestTime.xsd', 34, 6)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FeatureOfInterestId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetFeatureOfInterestTime.xsd', 34, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_23()




CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'offering'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_23, documentation='ID of an offering advertised in the capabilities.\n\t\t\t\t\t\t\t\t\tAll following parameters are depending on the selected offering.\n\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 34, 6)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eventTime'), CTD_ANON_7, scope=CTD_ANON_23, documentation='Allows a client to request observations from a specific instant, multiple instances or periods of time in the past, present and future. The supported range is listed in the selected offering capabilities.\n\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 41, 6)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'procedure'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_23, documentation="Index of a particular sensor if offering procedure is a Sensor Array. Allows client to request data from one or more sensors in the array. The size of the array should be specified in the selected offering capabilities. This is to support scenarios with sensor grids (we don't want to have one offering for each sensor in that case). Note that sensorML can describe Sensor Arrays too. \t\t\t\t\t\t\t\t\t\t", location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 52, 6)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'observedProperty'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_23, documentation='ID of a phenomenon advertised in capabilities document.\n\t\t\t\t\t\t\t\t\tAll possible phenomena are listed in the selected offering capabilities.\n\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 57, 6)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'featureOfInterest'), CTD_ANON_8, scope=CTD_ANON_23, documentation='Specifies target feature for which observations are requested. Mostly a hepler for in-situ sensors, since geo-location has to be done on the server side. The supported area should be listed in the selected offering capabilities.\n\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 64, 6)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'result'), CTD_ANON_9, scope=CTD_ANON_23, documentation='Only report observations where the result matches this expression.\n\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 80, 6)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseFormat'), pyxb.bundles.opengis.ows_1_1.MimeType, scope=CTD_ANON_23, documentation='ID of the output format to be used for the requested data. The supported output formats are listed in the selected offering capabilities.\n\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 91, 6)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'resultModel'), pyxb.binding.datatypes.QName, scope=CTD_ANON_23, documentation='Identifier of the result model to be used for the requested data. The resultModel values supported by a SOS server are listed in the contents section of the service metadata, identified as QName values.  If the requested resultModel is not supported by the SOS server, an exception message shall be returned.\n\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 97, 6)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseMode'), responseModeType, scope=CTD_ANON_23, documentation='This element allows the client to request the form of the response.  The value of resultTemplate is used to retrieve an observation template \n\t\t\t\t\t\t\tthat will later be used in calls to GetResult.  The other options allow results to appear inline in a resultTag (inline), external to the observation element (out-of-band)\n\t\t\t\t\t\t\tor as a MIME attachment (attached)', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 103, 6)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 33, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 41, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 52, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 64, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 80, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 97, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 103, 6))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'offering')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 34, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eventTime')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 41, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'procedure')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 52, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'observedProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 57, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'featureOfInterest')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 64, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'result')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 80, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseFormat')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 91, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'resultModel')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 97, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseMode')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservation.xsd', 103, 6))
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
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_23._Automaton = _BuildAutomaton_24()




CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObservationId'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_24, documentation='ID of the observation to obtain.  This could have been obtained by the client via a URL in a feed, alert, or some other notification\n\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 33, 6)))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseFormat'), pyxb.bundles.opengis.ows_1_1.MimeType, scope=CTD_ANON_24, documentation='ID of the output format to be used for the requested data. The supported output formats are listed in the selected offering capabilities.\n\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 39, 6)))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'resultModel'), pyxb.binding.datatypes.QName, scope=CTD_ANON_24, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 45, 6)))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseMode'), responseModeType, scope=CTD_ANON_24, documentation='This element allows the client to request the form of the response.  The value of resultTemplate is used to retrieve an observation template \n\t\t\t\t\t\t\tthat will later be used in calls to GetResult.  The other options allow results to appear inline in a resultTag (inline), external to the observation element (out-of-band)\n\t\t\t\t\t\t\tor as a MIME attachment (attached)', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 46, 6)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 39, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 45, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 46, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ObservationId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 33, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseFormat')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 39, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'resultModel')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 45, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseMode')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetObservationById.xsd', 46, 6))
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
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_24._Automaton = _BuildAutomaton_25()




CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObservationTemplateId'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_25, documentation='The gml:id of an previous GetObservation request response indicating observations from a certain sensor for a certain target.\n\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 32, 6)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eventTime'), CTD_ANON_10, scope=CTD_ANON_25, documentation='Allows a client to request observations from a specific instant, multiple instances or periods of time in the past, present and future. The supported range is listed in the selected offering capabilities.\n\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 38, 6)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 38, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ObservationTemplateId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 32, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eventTime')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosGetResult.xsd', 38, 6))
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
CTD_ANON_25._Automaton = _BuildAutomaton_26()




CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_om, 'Observation'), pyxb.bundles.opengis.om_1_0.ObservationType, scope=CTD_ANON_26, documentation='Observation is an act ("event"), whose result is an estimate of the value of a property of the feature of interest. \n            The observed property may be any property associated with the type of the feature of interest.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 126, 1)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AssignedSensorId'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_26, documentation='The id obtained by the registerSensor operation.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosInsert.xsd', 34, 6)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AssignedSensorId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosInsert.xsd', 34, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(_Namespace_om, 'Observation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosInsert.xsd', 39, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_26._Automaton = _BuildAutomaton_27()




CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SensorDescription'), CTD_ANON_14, scope=CTD_ANON_27, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 33, 12)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObservationTemplate'), CTD_ANON_15, scope=CTD_ANON_27, documentation='A template of the observations that will be inserted into the SOS.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 46, 2)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SensorDescription')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 33, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ObservationTemplate')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/sosRegisterSensor.xsd', 40, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_27._Automaton = _BuildAutomaton_28()


srsName._setSubstitutionGroup(pyxb.bundles.opengis.ows_1_1.AbstractMetaData)

supportedSensorDescription._setSubstitutionGroup(pyxb.bundles.opengis.ows_1_1.AbstractMetaData)

supportedSRS._setSubstitutionGroup(pyxb.bundles.opengis.gml.name)
