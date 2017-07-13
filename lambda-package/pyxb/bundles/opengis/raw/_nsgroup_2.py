# ./pyxb/bundles/opengis/raw/_nsgroup_2.py
# -*- coding: utf-8 -*-
# PyXB bindings for NGM:74d7865bc281d02523b2e79f08defec82904da9c
# Generated 2017-07-10 00:38:03.298063 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Group contents:
# Namespace http://purl.org/dc/terms/ [xmlns:dct]
# Namespace http://www.opengis.net/cat/csw/2.0.2


from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.utils.utility
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:0787160a-6508-11e7-9767-0a55f9edafa5')

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
import pyxb.bundles.opengis.csw_dc
import pyxb.bundles.opengis.filter
import pyxb.bundles.opengis.ows

# NOTE: All namespace declarations are reserved within the binding
_Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/cat/csw/2.0.2', create_if_missing=True)
_Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ows = pyxb.bundles.opengis.ows.Namespace
_Namespace_ows.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ogc = pyxb.bundles.opengis.filter.Namespace
_Namespace_ogc.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_dc = pyxb.bundles.opengis.csw_dc.Namespace
_Namespace_dc.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_dct = pyxb.namespace.NamespaceForURI('http://purl.org/dc/terms/', create_if_missing=True)
_Namespace_dct.configureCategories(['typeBinding', 'elementBinding'])

# Atomic simple type: {http://www.opengis.net/cat/csw/2.0.2}ResultType
class ResultType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'ResultType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 180, 3)
    _Documentation = None
ResultType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ResultType, enum_prefix=None)
ResultType.results = ResultType._CF_enumeration.addEnumeration(unicode_value='results', tag='results')
ResultType.hits = ResultType._CF_enumeration.addEnumeration(unicode_value='hits', tag='hits')
ResultType.validate = ResultType._CF_enumeration.addEnumeration(unicode_value='validate', tag='validate')
ResultType._InitializeFacetMap(ResultType._CF_enumeration)
_Namespace.addCategoryObject('typeBinding', 'ResultType', ResultType)
_module_typeBindings.ResultType = ResultType

# List simple type: {http://www.opengis.net/cat/csw/2.0.2}TypeNameListType
# superclasses pyxb.binding.datatypes.anySimpleType
class TypeNameListType (pyxb.binding.basis.STD_list):

    """The exact syntax is defined in an application profile. If querying 
       against the common record properties, only a single type may be 
       specified (Record)."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'TypeNameListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 246, 3)
    _Documentation = 'The exact syntax is defined in an application profile. If querying \n       against the common record properties, only a single type may be \n       specified (Record).'

    _ItemType = pyxb.binding.datatypes.QName
TypeNameListType._InitializeFacetMap()
_Namespace.addCategoryObject('typeBinding', 'TypeNameListType', TypeNameListType)
_module_typeBindings.TypeNameListType = TypeNameListType

# Atomic simple type: {http://www.opengis.net/cat/csw/2.0.2}ElementSetType
class ElementSetType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Named subsets of catalogue object properties; these
         views are mapped to a specific information model and
         are defined in an application profile."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'ElementSetType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 281, 3)
    _Documentation = 'Named subsets of catalogue object properties; these\n         views are mapped to a specific information model and\n         are defined in an application profile.'
ElementSetType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ElementSetType, enum_prefix=None)
ElementSetType.brief = ElementSetType._CF_enumeration.addEnumeration(unicode_value='brief', tag='brief')
ElementSetType.summary = ElementSetType._CF_enumeration.addEnumeration(unicode_value='summary', tag='summary')
ElementSetType.full = ElementSetType._CF_enumeration.addEnumeration(unicode_value='full', tag='full')
ElementSetType._InitializeFacetMap(ElementSetType._CF_enumeration)
_Namespace.addCategoryObject('typeBinding', 'ElementSetType', ElementSetType)
_module_typeBindings.ElementSetType = ElementSetType

# Complex type {http://www.opengis.net/cat/csw/2.0.2}RequestBaseType with content type EMPTY
class RequestBaseType (pyxb.binding.basis.complexTypeDefinition):
    """
            Base type for all request messages except GetCapabilities. The 
            attributes identify the relevant service type and version.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'RequestBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 32, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__httpwww_opengis_netcatcsw2_0_2_RequestBaseType_service', pyxb.bundles.opengis.ows.ServiceType, fixed=True, unicode_default='CSW', required=True)
    __service._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 39, 6)
    __service._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 39, 6)
    
    service = property(__service.value, __service.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netcatcsw2_0_2_RequestBaseType_version', pyxb.bundles.opengis.ows.VersionType, fixed=True, unicode_default='2.0.2', required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 41, 6)
    __version._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 41, 6)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __service.name() : __service,
        __version.name() : __version
    })
_module_typeBindings.RequestBaseType = RequestBaseType
_Namespace.addCategoryObject('typeBinding', 'RequestBaseType', RequestBaseType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}GetCapabilitiesType with content type ELEMENT_ONLY
class GetCapabilitiesType (pyxb.bundles.opengis.ows.GetCapabilitiesType):
    """
            Request for a description of service capabilities. See OGC 05-008 
            for more information.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'GetCapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 47, 3)
    _ElementMap = pyxb.bundles.opengis.ows.GetCapabilitiesType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.ows.GetCapabilitiesType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.ows.GetCapabilitiesType
    
    # Element AcceptVersions ({http://www.opengis.net/ows}AcceptVersions) inherited from {http://www.opengis.net/ows}GetCapabilitiesType
    
    # Element Sections ({http://www.opengis.net/ows}Sections) inherited from {http://www.opengis.net/ows}GetCapabilitiesType
    
    # Element AcceptFormats ({http://www.opengis.net/ows}AcceptFormats) inherited from {http://www.opengis.net/ows}GetCapabilitiesType
    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__httpwww_opengis_netcatcsw2_0_2_GetCapabilitiesType_service', pyxb.bundles.opengis.ows.ServiceType, unicode_default='http://www.opengis.net/cat/csw')
    __service._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 56, 12)
    __service._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 56, 12)
    
    service = property(__service.value, __service.set, None, None)

    
    # Attribute updateSequence inherited from {http://www.opengis.net/ows}GetCapabilitiesType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __service.name() : __service
    })
_module_typeBindings.GetCapabilitiesType = GetCapabilitiesType
_Namespace.addCategoryObject('typeBinding', 'GetCapabilitiesType', GetCapabilitiesType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}CapabilitiesType with content type ELEMENT_ONLY
class CapabilitiesType (pyxb.bundles.opengis.ows.CapabilitiesBaseType):
    """This type extends ows:CapabilitiesBaseType defined in OGC-05-008 
         to include information about supported OGC filter components. A 
         profile may extend this type to describe additional capabilities."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'CapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 63, 3)
    _ElementMap = pyxb.bundles.opengis.ows.CapabilitiesBaseType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.ows.CapabilitiesBaseType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.ows.CapabilitiesBaseType
    
    # Element {http://www.opengis.net/ogc}Filter_Capabilities uses Python identifier Filter_Capabilities
    __Filter_Capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter_Capabilities'), 'Filter_Capabilities', '__httpwww_opengis_netcatcsw2_0_2_CapabilitiesType_httpwww_opengis_netogcFilter_Capabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 20, 3), )

    
    Filter_Capabilities = property(__Filter_Capabilities.value, __Filter_Capabilities.set, None, None)

    
    # Element OperationsMetadata ({http://www.opengis.net/ows}OperationsMetadata) inherited from {http://www.opengis.net/ows}CapabilitiesBaseType
    
    # Element ServiceIdentification ({http://www.opengis.net/ows}ServiceIdentification) inherited from {http://www.opengis.net/ows}CapabilitiesBaseType
    
    # Element ServiceProvider ({http://www.opengis.net/ows}ServiceProvider) inherited from {http://www.opengis.net/ows}CapabilitiesBaseType
    
    # Attribute version inherited from {http://www.opengis.net/ows}CapabilitiesBaseType
    
    # Attribute updateSequence inherited from {http://www.opengis.net/ows}CapabilitiesBaseType
    _ElementMap.update({
        __Filter_Capabilities.name() : __Filter_Capabilities
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CapabilitiesType = CapabilitiesType
_Namespace.addCategoryObject('typeBinding', 'CapabilitiesType', CapabilitiesType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}DescribeRecordResponseType with content type ELEMENT_ONLY
class DescribeRecordResponseType (pyxb.binding.basis.complexTypeDefinition):
    """The response contains a list of matching schema components
         in the requested schema language."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'DescribeRecordResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 105, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}SchemaComponent uses Python identifier SchemaComponent
    __SchemaComponent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'SchemaComponent'), 'SchemaComponent', '__httpwww_opengis_netcatcsw2_0_2_DescribeRecordResponseType_httpwww_opengis_netcatcsw2_0_2SchemaComponent', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 112, 9), )

    
    SchemaComponent = property(__SchemaComponent.value, __SchemaComponent.set, None, None)

    _ElementMap.update({
        __SchemaComponent.name() : __SchemaComponent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DescribeRecordResponseType = DescribeRecordResponseType
_Namespace.addCategoryObject('typeBinding', 'DescribeRecordResponseType', DescribeRecordResponseType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}SchemaComponentType with content type MIXED
class SchemaComponentType (pyxb.binding.basis.complexTypeDefinition):
    """A schema component includes a schema fragment (type
         definition) or an entire schema from some target namespace;
         the schema language is identified by URI. If the component
         is a schema fragment its parent MUST be referenced (parentSchema)."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'SchemaComponentType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 116, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute targetNamespace uses Python identifier targetNamespace
    __targetNamespace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'targetNamespace'), 'targetNamespace', '__httpwww_opengis_netcatcsw2_0_2_SchemaComponentType_targetNamespace', pyxb.binding.datatypes.anyURI, required=True)
    __targetNamespace._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 127, 6)
    __targetNamespace._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 127, 6)
    
    targetNamespace = property(__targetNamespace.value, __targetNamespace.set, None, None)

    
    # Attribute parentSchema uses Python identifier parentSchema
    __parentSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'parentSchema'), 'parentSchema', '__httpwww_opengis_netcatcsw2_0_2_SchemaComponentType_parentSchema', pyxb.binding.datatypes.anyURI)
    __parentSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 128, 6)
    __parentSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 128, 6)
    
    parentSchema = property(__parentSchema.value, __parentSchema.set, None, None)

    
    # Attribute schemaLanguage uses Python identifier schemaLanguage
    __schemaLanguage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schemaLanguage'), 'schemaLanguage', '__httpwww_opengis_netcatcsw2_0_2_SchemaComponentType_schemaLanguage', pyxb.binding.datatypes.anyURI, required=True)
    __schemaLanguage._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 129, 6)
    __schemaLanguage._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 129, 6)
    
    schemaLanguage = property(__schemaLanguage.value, __schemaLanguage.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __targetNamespace.name() : __targetNamespace,
        __parentSchema.name() : __parentSchema,
        __schemaLanguage.name() : __schemaLanguage
    })
_module_typeBindings.SchemaComponentType = SchemaComponentType
_Namespace.addCategoryObject('typeBinding', 'SchemaComponentType', SchemaComponentType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}DistributedSearchType with content type EMPTY
class DistributedSearchType (pyxb.binding.basis.complexTypeDefinition):
    """Governs the behaviour of a distributed search.
         hopCount     - the maximum number of message hops before
                        the search is terminated. Each catalogue node 
                        decrements this value when the request is received, 
                        and must not forward the request if hopCount=0."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'DistributedSearchType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 200, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute hopCount uses Python identifier hopCount
    __hopCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'hopCount'), 'hopCount', '__httpwww_opengis_netcatcsw2_0_2_DistributedSearchType_hopCount', pyxb.binding.datatypes.positiveInteger, unicode_default='2')
    __hopCount._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 208, 6)
    __hopCount._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 208, 6)
    
    hopCount = property(__hopCount.value, __hopCount.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __hopCount.name() : __hopCount
    })
_module_typeBindings.DistributedSearchType = DistributedSearchType
_Namespace.addCategoryObject('typeBinding', 'DistributedSearchType', DistributedSearchType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}AbstractQueryType with content type EMPTY
class AbstractQueryType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/cat/csw/2.0.2}AbstractQueryType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'AbstractQueryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 213, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractQueryType = AbstractQueryType
_Namespace.addCategoryObject('typeBinding', 'AbstractQueryType', AbstractQueryType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}QueryConstraintType with content type ELEMENT_ONLY
class QueryConstraintType (pyxb.binding.basis.complexTypeDefinition):
    """A search constraint that adheres to one of the following syntaxes:
         Filter   - OGC filter expression
         CqlText  - OGC CQL predicate"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'QueryConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 255, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}CqlText uses Python identifier CqlText
    __CqlText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'CqlText'), 'CqlText', '__httpwww_opengis_netcatcsw2_0_2_QueryConstraintType_httpwww_opengis_netcatcsw2_0_2CqlText', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 263, 9), )

    
    CqlText = property(__CqlText.value, __CqlText.set, None, None)

    
    # Element {http://www.opengis.net/ogc}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter'), 'Filter', '__httpwww_opengis_netcatcsw2_0_2_QueryConstraintType_httpwww_opengis_netogcFilter', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 39, 3), )

    
    Filter = property(__Filter.value, __Filter.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netcatcsw2_0_2_QueryConstraintType_version', pyxb.binding.datatypes.string, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 265, 6)
    __version._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 265, 6)
    
    version = property(__version.value, __version.set, None, 'Query language version')

    _ElementMap.update({
        __CqlText.name() : __CqlText,
        __Filter.name() : __Filter
    })
    _AttributeMap.update({
        __version.name() : __version
    })
_module_typeBindings.QueryConstraintType = QueryConstraintType
_Namespace.addCategoryObject('typeBinding', 'QueryConstraintType', QueryConstraintType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}GetRecordsResponseType with content type ELEMENT_ONLY
class GetRecordsResponseType (pyxb.binding.basis.complexTypeDefinition):
    """
            The response message for a GetRecords request. Some or all of the 
            matching records may be included as children of the SearchResults 
            element. The RequestId is only included if the client specified it.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'GetRecordsResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 295, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}RequestId uses Python identifier RequestId
    __RequestId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'RequestId'), 'RequestId', '__httpwww_opengis_netcatcsw2_0_2_GetRecordsResponseType_httpwww_opengis_netcatcsw2_0_2RequestId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 304, 9), )

    
    RequestId = property(__RequestId.value, __RequestId.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}SearchStatus uses Python identifier SearchStatus
    __SearchStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'SearchStatus'), 'SearchStatus', '__httpwww_opengis_netcatcsw2_0_2_GetRecordsResponseType_httpwww_opengis_netcatcsw2_0_2SearchStatus', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 305, 9), )

    
    SearchStatus = property(__SearchStatus.value, __SearchStatus.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}SearchResults uses Python identifier SearchResults
    __SearchResults = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'SearchResults'), 'SearchResults', '__httpwww_opengis_netcatcsw2_0_2_GetRecordsResponseType_httpwww_opengis_netcatcsw2_0_2SearchResults', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 306, 9), )

    
    SearchResults = property(__SearchResults.value, __SearchResults.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netcatcsw2_0_2_GetRecordsResponseType_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 308, 6)
    __version._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 308, 6)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __RequestId.name() : __RequestId,
        __SearchStatus.name() : __SearchStatus,
        __SearchResults.name() : __SearchResults
    })
    _AttributeMap.update({
        __version.name() : __version
    })
_module_typeBindings.GetRecordsResponseType = GetRecordsResponseType
_Namespace.addCategoryObject('typeBinding', 'GetRecordsResponseType', GetRecordsResponseType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}RequestStatusType with content type EMPTY
class RequestStatusType (pyxb.binding.basis.complexTypeDefinition):
    """
            This element provides information about the status of the
            search request.

            status    - status of the search
            timestamp - the date and time when the result set was modified 
                        (ISO 8601 format: YYYY-MM-DDThh:mm:ss[+|-]hh:mm).
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'RequestStatusType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 311, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timestamp'), 'timestamp', '__httpwww_opengis_netcatcsw2_0_2_RequestStatusType_timestamp', pyxb.binding.datatypes.dateTime)
    __timestamp._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 322, 6)
    __timestamp._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 322, 6)
    
    timestamp = property(__timestamp.value, __timestamp.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __timestamp.name() : __timestamp
    })
_module_typeBindings.RequestStatusType = RequestStatusType
_Namespace.addCategoryObject('typeBinding', 'RequestStatusType', RequestStatusType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}GetRecordByIdResponseType with content type ELEMENT_ONLY
class GetRecordByIdResponseType (pyxb.binding.basis.complexTypeDefinition):
    """Returns a representation of the matching entry. If there is no 
         matching record, the response message must be empty."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'GetRecordByIdResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 392, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}AbstractRecord uses Python identifier AbstractRecord
    __AbstractRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'AbstractRecord'), 'AbstractRecord', '__httpwww_opengis_netcatcsw2_0_2_GetRecordByIdResponseType_httpwww_opengis_netcatcsw2_0_2AbstractRecord', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 29, 3), )

    
    AbstractRecord = property(__AbstractRecord.value, __AbstractRecord.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __AbstractRecord.name() : __AbstractRecord
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GetRecordByIdResponseType = GetRecordByIdResponseType
_Namespace.addCategoryObject('typeBinding', 'GetRecordByIdResponseType', GetRecordByIdResponseType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}GetDomainResponseType with content type ELEMENT_ONLY
class GetDomainResponseType (pyxb.binding.basis.complexTypeDefinition):
    """Returns the actual values for some property. In general this is a
         subset of the value domain (that is, set of permissible values),
         although in some cases these may be the same."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'GetDomainResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 426, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}DomainValues uses Python identifier DomainValues
    __DomainValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'DomainValues'), 'DomainValues', '__httpwww_opengis_netcatcsw2_0_2_GetDomainResponseType_httpwww_opengis_netcatcsw2_0_2DomainValues', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 433, 9), )

    
    DomainValues = property(__DomainValues.value, __DomainValues.set, None, None)

    _ElementMap.update({
        __DomainValues.name() : __DomainValues
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GetDomainResponseType = GetDomainResponseType
_Namespace.addCategoryObject('typeBinding', 'GetDomainResponseType', GetDomainResponseType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}DomainValuesType with content type ELEMENT_ONLY
class DomainValuesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/cat/csw/2.0.2}DomainValuesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'DomainValuesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 437, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}PropertyName uses Python identifier PropertyName
    __PropertyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'PropertyName'), 'PropertyName', '__httpwww_opengis_netcatcsw2_0_2_DomainValuesType_httpwww_opengis_netcatcsw2_0_2PropertyName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 440, 12), )

    
    PropertyName = property(__PropertyName.value, __PropertyName.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}ParameterName uses Python identifier ParameterName
    __ParameterName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'ParameterName'), 'ParameterName', '__httpwww_opengis_netcatcsw2_0_2_DomainValuesType_httpwww_opengis_netcatcsw2_0_2ParameterName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 441, 12), )

    
    ParameterName = property(__ParameterName.value, __ParameterName.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}ListOfValues uses Python identifier ListOfValues
    __ListOfValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'ListOfValues'), 'ListOfValues', '__httpwww_opengis_netcatcsw2_0_2_DomainValuesType_httpwww_opengis_netcatcsw2_0_2ListOfValues', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 444, 12), )

    
    ListOfValues = property(__ListOfValues.value, __ListOfValues.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}ConceptualScheme uses Python identifier ConceptualScheme
    __ConceptualScheme = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'ConceptualScheme'), 'ConceptualScheme', '__httpwww_opengis_netcatcsw2_0_2_DomainValuesType_httpwww_opengis_netcatcsw2_0_2ConceptualScheme', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 445, 12), )

    
    ConceptualScheme = property(__ConceptualScheme.value, __ConceptualScheme.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}RangeOfValues uses Python identifier RangeOfValues
    __RangeOfValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'RangeOfValues'), 'RangeOfValues', '__httpwww_opengis_netcatcsw2_0_2_DomainValuesType_httpwww_opengis_netcatcsw2_0_2RangeOfValues', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 446, 12), )

    
    RangeOfValues = property(__RangeOfValues.value, __RangeOfValues.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_opengis_netcatcsw2_0_2_DomainValuesType_type', pyxb.binding.datatypes.QName, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 449, 6)
    __type._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 449, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_opengis_netcatcsw2_0_2_DomainValuesType_uom', pyxb.binding.datatypes.anyURI)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 450, 6)
    __uom._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 450, 6)
    
    uom = property(__uom.value, __uom.set, None, None)

    _ElementMap.update({
        __PropertyName.name() : __PropertyName,
        __ParameterName.name() : __ParameterName,
        __ListOfValues.name() : __ListOfValues,
        __ConceptualScheme.name() : __ConceptualScheme,
        __RangeOfValues.name() : __RangeOfValues
    })
    _AttributeMap.update({
        __type.name() : __type,
        __uom.name() : __uom
    })
_module_typeBindings.DomainValuesType = DomainValuesType
_Namespace.addCategoryObject('typeBinding', 'DomainValuesType', DomainValuesType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}ListOfValuesType with content type ELEMENT_ONLY
class ListOfValuesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/cat/csw/2.0.2}ListOfValuesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'ListOfValuesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 452, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'Value'), 'Value', '__httpwww_opengis_netcatcsw2_0_2_ListOfValuesType_httpwww_opengis_netcatcsw2_0_2Value', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 454, 9), )

    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ListOfValuesType = ListOfValuesType
_Namespace.addCategoryObject('typeBinding', 'ListOfValuesType', ListOfValuesType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}ConceptualSchemeType with content type ELEMENT_ONLY
class ConceptualSchemeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/cat/csw/2.0.2}ConceptualSchemeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'ConceptualSchemeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 457, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'Name'), 'Name', '__httpwww_opengis_netcatcsw2_0_2_ConceptualSchemeType_httpwww_opengis_netcatcsw2_0_2Name', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 459, 9), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}Document uses Python identifier Document
    __Document = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'Document'), 'Document', '__httpwww_opengis_netcatcsw2_0_2_ConceptualSchemeType_httpwww_opengis_netcatcsw2_0_2Document', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 460, 9), )

    
    Document = property(__Document.value, __Document.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}Authority uses Python identifier Authority
    __Authority = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'Authority'), 'Authority', '__httpwww_opengis_netcatcsw2_0_2_ConceptualSchemeType_httpwww_opengis_netcatcsw2_0_2Authority', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 461, 9), )

    
    Authority = property(__Authority.value, __Authority.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __Document.name() : __Document,
        __Authority.name() : __Authority
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ConceptualSchemeType = ConceptualSchemeType
_Namespace.addCategoryObject('typeBinding', 'ConceptualSchemeType', ConceptualSchemeType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}RangeOfValuesType with content type ELEMENT_ONLY
class RangeOfValuesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/cat/csw/2.0.2}RangeOfValuesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'RangeOfValuesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 464, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}MinValue uses Python identifier MinValue
    __MinValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'MinValue'), 'MinValue', '__httpwww_opengis_netcatcsw2_0_2_RangeOfValuesType_httpwww_opengis_netcatcsw2_0_2MinValue', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 466, 9), )

    
    MinValue = property(__MinValue.value, __MinValue.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}MaxValue uses Python identifier MaxValue
    __MaxValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'MaxValue'), 'MaxValue', '__httpwww_opengis_netcatcsw2_0_2_RangeOfValuesType_httpwww_opengis_netcatcsw2_0_2MaxValue', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 467, 9), )

    
    MaxValue = property(__MaxValue.value, __MaxValue.set, None, None)

    _ElementMap.update({
        __MinValue.name() : __MinValue,
        __MaxValue.name() : __MaxValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RangeOfValuesType = RangeOfValuesType
_Namespace.addCategoryObject('typeBinding', 'RangeOfValuesType', RangeOfValuesType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}AcknowledgementType with content type ELEMENT_ONLY
class AcknowledgementType (pyxb.binding.basis.complexTypeDefinition):
    """This is a general acknowledgement response message for all requests 
         that may be processed in an asynchronous manner.
         EchoedRequest - Echoes the submitted request message
         RequestId     - identifier for polling purposes (if no response 
                         handler is available, or the URL scheme is
                         unsupported)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'AcknowledgementType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 472, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}EchoedRequest uses Python identifier EchoedRequest
    __EchoedRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'EchoedRequest'), 'EchoedRequest', '__httpwww_opengis_netcatcsw2_0_2_AcknowledgementType_httpwww_opengis_netcatcsw2_0_2EchoedRequest', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 482, 9), )

    
    EchoedRequest = property(__EchoedRequest.value, __EchoedRequest.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}RequestId uses Python identifier RequestId
    __RequestId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'RequestId'), 'RequestId', '__httpwww_opengis_netcatcsw2_0_2_AcknowledgementType_httpwww_opengis_netcatcsw2_0_2RequestId', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 483, 9), )

    
    RequestId = property(__RequestId.value, __RequestId.set, None, None)

    
    # Attribute timeStamp uses Python identifier timeStamp
    __timeStamp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timeStamp'), 'timeStamp', '__httpwww_opengis_netcatcsw2_0_2_AcknowledgementType_timeStamp', pyxb.binding.datatypes.dateTime, required=True)
    __timeStamp._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 485, 6)
    __timeStamp._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 485, 6)
    
    timeStamp = property(__timeStamp.value, __timeStamp.set, None, None)

    _ElementMap.update({
        __EchoedRequest.name() : __EchoedRequest,
        __RequestId.name() : __RequestId
    })
    _AttributeMap.update({
        __timeStamp.name() : __timeStamp
    })
_module_typeBindings.AcknowledgementType = AcknowledgementType
_Namespace.addCategoryObject('typeBinding', 'AcknowledgementType', AcknowledgementType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}EchoedRequestType with content type ELEMENT_ONLY
class EchoedRequestType (pyxb.binding.basis.complexTypeDefinition):
    """Includes a copy of the request message body."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'EchoedRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 487, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EchoedRequestType = EchoedRequestType
_Namespace.addCategoryObject('typeBinding', 'EchoedRequestType', EchoedRequestType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}InsertType with content type ELEMENT_ONLY
class InsertType (pyxb.binding.basis.complexTypeDefinition):
    """
            Submits one or more records to the catalogue. The representation
            is defined by the application profile. The handle attribute
            may be included to specify a local identifier for the action 
            (it must be unique within the context of the transaction).
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'InsertType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 49, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute typeName uses Python identifier typeName
    __typeName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typeName'), 'typeName', '__httpwww_opengis_netcatcsw2_0_2_InsertType_typeName', pyxb.binding.datatypes.anyURI)
    __typeName._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 62, 6)
    __typeName._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 62, 6)
    
    typeName = property(__typeName.value, __typeName.set, None, None)

    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'handle'), 'handle', '__httpwww_opengis_netcatcsw2_0_2_InsertType_handle', pyxb.binding.datatypes.ID)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 63, 6)
    __handle._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 63, 6)
    
    handle = property(__handle.value, __handle.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __typeName.name() : __typeName,
        __handle.name() : __handle
    })
_module_typeBindings.InsertType = InsertType
_Namespace.addCategoryObject('typeBinding', 'InsertType', InsertType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}UpdateType with content type ELEMENT_ONLY
class UpdateType (pyxb.binding.basis.complexTypeDefinition):
    """
            Update statements may replace an entire record or only update part 
            of a record:
            1) To replace an existing record, include a new instance of the 
               record;
            2) To update selected properties of an existing record, include
               a set of RecordProperty elements. The scope of the update
               statement  is determined by the Constraint element.
               The 'handle' is a local identifier for the action.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'UpdateType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 65, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}Constraint uses Python identifier Constraint
    __Constraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'Constraint'), 'Constraint', '__httpwww_opengis_netcatcsw2_0_2_UpdateType_httpwww_opengis_netcatcsw2_0_2Constraint', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 254, 3), )

    
    Constraint = property(__Constraint.value, __Constraint.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}RecordProperty uses Python identifier RecordProperty
    __RecordProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'RecordProperty'), 'RecordProperty', '__httpwww_opengis_netcatcsw2_0_2_UpdateType_httpwww_opengis_netcatcsw2_0_2RecordProperty', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 102, 3), )

    
    RecordProperty = property(__RecordProperty.value, __RecordProperty.set, None, '\n            The RecordProperty element is used to specify the new\n            value of a record property in an update statement.\n         ')

    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'handle'), 'handle', '__httpwww_opengis_netcatcsw2_0_2_UpdateType_handle', pyxb.binding.datatypes.ID)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 87, 6)
    __handle._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 87, 6)
    
    handle = property(__handle.value, __handle.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __Constraint.name() : __Constraint,
        __RecordProperty.name() : __RecordProperty
    })
    _AttributeMap.update({
        __handle.name() : __handle
    })
_module_typeBindings.UpdateType = UpdateType
_Namespace.addCategoryObject('typeBinding', 'UpdateType', UpdateType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}DeleteType with content type ELEMENT_ONLY
class DeleteType (pyxb.binding.basis.complexTypeDefinition):
    """
            Deletes one or more catalogue items that satisfy some set of 
            conditions.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'DeleteType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 89, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}Constraint uses Python identifier Constraint
    __Constraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'Constraint'), 'Constraint', '__httpwww_opengis_netcatcsw2_0_2_DeleteType_httpwww_opengis_netcatcsw2_0_2Constraint', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 254, 3), )

    
    Constraint = property(__Constraint.value, __Constraint.set, None, None)

    
    # Attribute typeName uses Python identifier typeName
    __typeName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typeName'), 'typeName', '__httpwww_opengis_netcatcsw2_0_2_DeleteType_typeName', pyxb.binding.datatypes.anyURI)
    __typeName._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 99, 6)
    __typeName._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 99, 6)
    
    typeName = property(__typeName.value, __typeName.set, None, None)

    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'handle'), 'handle', '__httpwww_opengis_netcatcsw2_0_2_DeleteType_handle', pyxb.binding.datatypes.ID)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 100, 6)
    __handle._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 100, 6)
    
    handle = property(__handle.value, __handle.set, None, None)

    _ElementMap.update({
        __Constraint.name() : __Constraint
    })
    _AttributeMap.update({
        __typeName.name() : __typeName,
        __handle.name() : __handle
    })
_module_typeBindings.DeleteType = DeleteType
_Namespace.addCategoryObject('typeBinding', 'DeleteType', DeleteType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}RecordPropertyType with content type ELEMENT_ONLY
class RecordPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/cat/csw/2.0.2}RecordPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'RecordPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 110, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'Name'), 'Name', '__httpwww_opengis_netcatcsw2_0_2_RecordPropertyType_httpwww_opengis_netcatcsw2_0_2Name', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 112, 9), )

    
    Name = property(__Name.value, __Name.set, None, '\n                  The Name element contains the name of a property\n                  to be updated.  The name may be a path expression.\n               ')

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'Value'), 'Value', '__httpwww_opengis_netcatcsw2_0_2_RecordPropertyType_httpwww_opengis_netcatcsw2_0_2Value', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 120, 9), )

    
    Value = property(__Value.value, __Value.set, None, '\n                  The Value element contains the replacement value for the\n                  named property.\n               ')

    _ElementMap.update({
        __Name.name() : __Name,
        __Value.name() : __Value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RecordPropertyType = RecordPropertyType
_Namespace.addCategoryObject('typeBinding', 'RecordPropertyType', RecordPropertyType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}TransactionResponseType with content type ELEMENT_ONLY
class TransactionResponseType (pyxb.binding.basis.complexTypeDefinition):
    """
            The response for a transaction request that was successfully
            completed. If the transaction failed for any reason, a service 
            exception report indicating a TransactionFailure is returned
            instead.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'TransactionResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 132, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}TransactionSummary uses Python identifier TransactionSummary
    __TransactionSummary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'TransactionSummary'), 'TransactionSummary', '__httpwww_opengis_netcatcsw2_0_2_TransactionResponseType_httpwww_opengis_netcatcsw2_0_2TransactionSummary', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 142, 9), )

    
    TransactionSummary = property(__TransactionSummary.value, __TransactionSummary.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}InsertResult uses Python identifier InsertResult
    __InsertResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'InsertResult'), 'InsertResult', '__httpwww_opengis_netcatcsw2_0_2_TransactionResponseType_httpwww_opengis_netcatcsw2_0_2InsertResult', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 144, 9), )

    
    InsertResult = property(__InsertResult.value, __InsertResult.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netcatcsw2_0_2_TransactionResponseType_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 147, 6)
    __version._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 147, 6)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __TransactionSummary.name() : __TransactionSummary,
        __InsertResult.name() : __InsertResult
    })
    _AttributeMap.update({
        __version.name() : __version
    })
_module_typeBindings.TransactionResponseType = TransactionResponseType
_Namespace.addCategoryObject('typeBinding', 'TransactionResponseType', TransactionResponseType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}TransactionSummaryType with content type ELEMENT_ONLY
class TransactionSummaryType (pyxb.binding.basis.complexTypeDefinition):
    """
         Reports the total number of catalogue items modified by a transaction 
         request (i.e, inserted, updated, deleted). If the client did not 
         specify a requestId, the server may assign one (a URI value).
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'TransactionSummaryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 149, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}totalInserted uses Python identifier totalInserted
    __totalInserted = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'totalInserted'), 'totalInserted', '__httpwww_opengis_netcatcsw2_0_2_TransactionSummaryType_httpwww_opengis_netcatcsw2_0_2totalInserted', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 158, 9), )

    
    totalInserted = property(__totalInserted.value, __totalInserted.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}totalUpdated uses Python identifier totalUpdated
    __totalUpdated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'totalUpdated'), 'totalUpdated', '__httpwww_opengis_netcatcsw2_0_2_TransactionSummaryType_httpwww_opengis_netcatcsw2_0_2totalUpdated', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 160, 9), )

    
    totalUpdated = property(__totalUpdated.value, __totalUpdated.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}totalDeleted uses Python identifier totalDeleted
    __totalDeleted = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'totalDeleted'), 'totalDeleted', '__httpwww_opengis_netcatcsw2_0_2_TransactionSummaryType_httpwww_opengis_netcatcsw2_0_2totalDeleted', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 162, 9), )

    
    totalDeleted = property(__totalDeleted.value, __totalDeleted.set, None, None)

    
    # Attribute requestId uses Python identifier requestId
    __requestId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'requestId'), 'requestId', '__httpwww_opengis_netcatcsw2_0_2_TransactionSummaryType_requestId', pyxb.binding.datatypes.anyURI)
    __requestId._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 165, 6)
    __requestId._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 165, 6)
    
    requestId = property(__requestId.value, __requestId.set, None, None)

    _ElementMap.update({
        __totalInserted.name() : __totalInserted,
        __totalUpdated.name() : __totalUpdated,
        __totalDeleted.name() : __totalDeleted
    })
    _AttributeMap.update({
        __requestId.name() : __requestId
    })
_module_typeBindings.TransactionSummaryType = TransactionSummaryType
_Namespace.addCategoryObject('typeBinding', 'TransactionSummaryType', TransactionSummaryType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}InsertResultType with content type ELEMENT_ONLY
class InsertResultType (pyxb.binding.basis.complexTypeDefinition):
    """
            Returns a "brief" view of any newly created catalogue records.
            The handle attribute may reference a particular statement in
            the corresponding transaction request.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'InsertResultType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 167, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}BriefRecord uses Python identifier BriefRecord
    __BriefRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'BriefRecord'), 'BriefRecord', '__httpwww_opengis_netcatcsw2_0_2_InsertResultType_httpwww_opengis_netcatcsw2_0_2BriefRecord', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 53, 3), )

    
    BriefRecord = property(__BriefRecord.value, __BriefRecord.set, None, None)

    
    # Attribute handleRef uses Python identifier handleRef
    __handleRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'handleRef'), 'handleRef', '__httpwww_opengis_netcatcsw2_0_2_InsertResultType_handleRef', pyxb.binding.datatypes.anyURI)
    __handleRef._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 178, 6)
    __handleRef._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 178, 6)
    
    handleRef = property(__handleRef.value, __handleRef.set, None, None)

    _ElementMap.update({
        __BriefRecord.name() : __BriefRecord
    })
    _AttributeMap.update({
        __handleRef.name() : __handleRef
    })
_module_typeBindings.InsertResultType = InsertResultType
_Namespace.addCategoryObject('typeBinding', 'InsertResultType', InsertResultType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}HarvestResponseType with content type ELEMENT_ONLY
class HarvestResponseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/cat/csw/2.0.2}HarvestResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'HarvestResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 239, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}Acknowledgement uses Python identifier Acknowledgement
    __Acknowledgement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'Acknowledgement'), 'Acknowledgement', '__httpwww_opengis_netcatcsw2_0_2_HarvestResponseType_httpwww_opengis_netcatcsw2_0_2Acknowledgement', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 470, 3), )

    
    Acknowledgement = property(__Acknowledgement.value, __Acknowledgement.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}TransactionResponse uses Python identifier TransactionResponse
    __TransactionResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'TransactionResponse'), 'TransactionResponse', '__httpwww_opengis_netcatcsw2_0_2_HarvestResponseType_httpwww_opengis_netcatcsw2_0_2TransactionResponse', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 130, 3), )

    
    TransactionResponse = property(__TransactionResponse.value, __TransactionResponse.set, None, None)

    _ElementMap.update({
        __Acknowledgement.name() : __Acknowledgement,
        __TransactionResponse.name() : __TransactionResponse
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.HarvestResponseType = HarvestResponseType
_Namespace.addCategoryObject('typeBinding', 'HarvestResponseType', HarvestResponseType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}AbstractRecordType with content type EMPTY
class AbstractRecordType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/cat/csw/2.0.2}AbstractRecordType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'AbstractRecordType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 31, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractRecordType = AbstractRecordType
_Namespace.addCategoryObject('typeBinding', 'AbstractRecordType', AbstractRecordType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}EmptyType with content type EMPTY
class EmptyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/cat/csw/2.0.2}EmptyType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'EmptyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 138, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EmptyType = EmptyType
_Namespace.addCategoryObject('typeBinding', 'EmptyType', EmptyType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}DescribeRecordType with content type ELEMENT_ONLY
class DescribeRecordType (RequestBaseType):
    """This request allows a user to discover elements of the
         information model supported by the catalogue. If no TypeName 
         elements are included, then all of the schemas for the 
         information model must be returned.
      
         schemaLanguage - preferred schema language
                          (W3C XML Schema by default)
         outputFormat - preferred output format (application/xml by default)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'DescribeRecordType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 79, 3)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}TypeName uses Python identifier TypeName
    __TypeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'TypeName'), 'TypeName', '__httpwww_opengis_netcatcsw2_0_2_DescribeRecordType_httpwww_opengis_netcatcsw2_0_2TypeName', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 93, 15), )

    
    TypeName = property(__TypeName.value, __TypeName.set, None, None)

    
    # Attribute service inherited from {http://www.opengis.net/cat/csw/2.0.2}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/cat/csw/2.0.2}RequestBaseType
    
    # Attribute outputFormat uses Python identifier outputFormat
    __outputFormat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'outputFormat'), 'outputFormat', '__httpwww_opengis_netcatcsw2_0_2_DescribeRecordType_outputFormat', pyxb.binding.datatypes.string, unicode_default='application/xml')
    __outputFormat._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 96, 12)
    __outputFormat._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 96, 12)
    
    outputFormat = property(__outputFormat.value, __outputFormat.set, None, None)

    
    # Attribute schemaLanguage uses Python identifier schemaLanguage
    __schemaLanguage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schemaLanguage'), 'schemaLanguage', '__httpwww_opengis_netcatcsw2_0_2_DescribeRecordType_schemaLanguage', pyxb.binding.datatypes.anyURI, unicode_default='http://www.w3.org/XML/Schema')
    __schemaLanguage._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 98, 12)
    __schemaLanguage._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 98, 12)
    
    schemaLanguage = property(__schemaLanguage.value, __schemaLanguage.set, None, None)

    _ElementMap.update({
        __TypeName.name() : __TypeName
    })
    _AttributeMap.update({
        __outputFormat.name() : __outputFormat,
        __schemaLanguage.name() : __schemaLanguage
    })
_module_typeBindings.DescribeRecordType = DescribeRecordType
_Namespace.addCategoryObject('typeBinding', 'DescribeRecordType', DescribeRecordType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}GetRecordsType with content type ELEMENT_ONLY
class GetRecordsType (RequestBaseType):
    """
         The principal means of searching the catalogue. The matching 
         catalogue entries may be included with the response. The client 
         may assign a requestId (absolute URI). A distributed search is 
         performed if the DistributedSearch element is present and the 
         catalogue is a member of a federation. Profiles may allow 
         alternative query expressions."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'GetRecordsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 132, 3)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}DistributedSearch uses Python identifier DistributedSearch
    __DistributedSearch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'DistributedSearch'), 'DistributedSearch', '__httpwww_opengis_netcatcsw2_0_2_GetRecordsType_httpwww_opengis_netcatcsw2_0_2DistributedSearch', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 145, 15), )

    
    DistributedSearch = property(__DistributedSearch.value, __DistributedSearch.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}ResponseHandler uses Python identifier ResponseHandler
    __ResponseHandler = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'ResponseHandler'), 'ResponseHandler', '__httpwww_opengis_netcatcsw2_0_2_GetRecordsType_httpwww_opengis_netcatcsw2_0_2ResponseHandler', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 147, 15), )

    
    ResponseHandler = property(__ResponseHandler.value, __ResponseHandler.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}AbstractQuery uses Python identifier AbstractQuery
    __AbstractQuery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'AbstractQuery'), 'AbstractQuery', '__httpwww_opengis_netcatcsw2_0_2_GetRecordsType_httpwww_opengis_netcatcsw2_0_2AbstractQuery', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 211, 3), )

    
    AbstractQuery = property(__AbstractQuery.value, __AbstractQuery.set, None, None)

    
    # Attribute service inherited from {http://www.opengis.net/cat/csw/2.0.2}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/cat/csw/2.0.2}RequestBaseType
    
    # Attribute requestId uses Python identifier requestId
    __requestId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'requestId'), 'requestId', '__httpwww_opengis_netcatcsw2_0_2_GetRecordsType_requestId', pyxb.binding.datatypes.anyURI)
    __requestId._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 154, 12)
    __requestId._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 154, 12)
    
    requestId = property(__requestId.value, __requestId.set, None, None)

    
    # Attribute resultType uses Python identifier resultType
    __resultType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'resultType'), 'resultType', '__httpwww_opengis_netcatcsw2_0_2_GetRecordsType_resultType', _module_typeBindings.ResultType, unicode_default='hits')
    __resultType._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 155, 12)
    __resultType._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 155, 12)
    
    resultType = property(__resultType.value, __resultType.set, None, None)

    
    # Attribute outputFormat uses Python identifier outputFormat
    __outputFormat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'outputFormat'), 'outputFormat', '__httpwww_opengis_netcatcsw2_0_2_GetRecordsType_outputFormat', pyxb.binding.datatypes.string, unicode_default='application/xml')
    __outputFormat._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 172, 6)
    __outputFormat._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 172, 6)
    
    outputFormat = property(__outputFormat.value, __outputFormat.set, None, None)

    
    # Attribute outputSchema uses Python identifier outputSchema
    __outputSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'outputSchema'), 'outputSchema', '__httpwww_opengis_netcatcsw2_0_2_GetRecordsType_outputSchema', pyxb.binding.datatypes.anyURI)
    __outputSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 174, 6)
    __outputSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 174, 6)
    
    outputSchema = property(__outputSchema.value, __outputSchema.set, None, None)

    
    # Attribute startPosition uses Python identifier startPosition
    __startPosition = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'startPosition'), 'startPosition', '__httpwww_opengis_netcatcsw2_0_2_GetRecordsType_startPosition', pyxb.binding.datatypes.positiveInteger, unicode_default='1')
    __startPosition._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 175, 6)
    __startPosition._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 175, 6)
    
    startPosition = property(__startPosition.value, __startPosition.set, None, None)

    
    # Attribute maxRecords uses Python identifier maxRecords
    __maxRecords = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxRecords'), 'maxRecords', '__httpwww_opengis_netcatcsw2_0_2_GetRecordsType_maxRecords', pyxb.binding.datatypes.nonNegativeInteger, unicode_default='10')
    __maxRecords._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 177, 6)
    __maxRecords._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 177, 6)
    
    maxRecords = property(__maxRecords.value, __maxRecords.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __DistributedSearch.name() : __DistributedSearch,
        __ResponseHandler.name() : __ResponseHandler,
        __AbstractQuery.name() : __AbstractQuery
    })
    _AttributeMap.update({
        __requestId.name() : __requestId,
        __resultType.name() : __resultType,
        __outputFormat.name() : __outputFormat,
        __outputSchema.name() : __outputSchema,
        __startPosition.name() : __startPosition,
        __maxRecords.name() : __maxRecords
    })
_module_typeBindings.GetRecordsType = GetRecordsType
_Namespace.addCategoryObject('typeBinding', 'GetRecordsType', GetRecordsType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}QueryType with content type ELEMENT_ONLY
class QueryType (AbstractQueryType):
    """Specifies a query to execute against instances of one or
         more object types. A set of ElementName elements may be included 
         to specify an adhoc view of the csw:Record instances in the result 
         set. Otherwise, use ElementSetName to specify a predefined view. 
         The Constraint element contains a query filter expressed in a 
         supported query language. A sorting criterion that specifies a 
         property to sort by may be included.

         typeNames - a list of object types to query."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'QueryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 217, 3)
    _ElementMap = AbstractQueryType._ElementMap.copy()
    _AttributeMap = AbstractQueryType._AttributeMap.copy()
    # Base type is AbstractQueryType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}ElementName uses Python identifier ElementName
    __ElementName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'ElementName'), 'ElementName', '__httpwww_opengis_netcatcsw2_0_2_QueryType_httpwww_opengis_netcatcsw2_0_2ElementName', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 234, 18), )

    
    ElementName = property(__ElementName.value, __ElementName.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}Constraint uses Python identifier Constraint
    __Constraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'Constraint'), 'Constraint', '__httpwww_opengis_netcatcsw2_0_2_QueryType_httpwww_opengis_netcatcsw2_0_2Constraint', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 254, 3), )

    
    Constraint = property(__Constraint.value, __Constraint.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}ElementSetName uses Python identifier ElementSetName
    __ElementSetName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'ElementSetName'), 'ElementSetName', '__httpwww_opengis_netcatcsw2_0_2_QueryType_httpwww_opengis_netcatcsw2_0_2ElementSetName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 271, 3), )

    
    ElementSetName = property(__ElementSetName.value, __ElementSetName.set, None, None)

    
    # Element {http://www.opengis.net/ogc}SortBy uses Python identifier SortBy
    __SortBy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ogc, 'SortBy'), 'SortBy', '__httpwww_opengis_netcatcsw2_0_2_QueryType_httpwww_opengis_netogcSortBy', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/sort.xsd', 21, 3), )

    
    SortBy = property(__SortBy.value, __SortBy.set, None, None)

    
    # Attribute typeNames uses Python identifier typeNames
    __typeNames = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typeNames'), 'typeNames', '__httpwww_opengis_netcatcsw2_0_2_QueryType_typeNames', _module_typeBindings.TypeNameListType, required=True)
    __typeNames._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 241, 12)
    __typeNames._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 241, 12)
    
    typeNames = property(__typeNames.value, __typeNames.set, None, None)

    _ElementMap.update({
        __ElementName.name() : __ElementName,
        __Constraint.name() : __Constraint,
        __ElementSetName.name() : __ElementSetName,
        __SortBy.name() : __SortBy
    })
    _AttributeMap.update({
        __typeNames.name() : __typeNames
    })
_module_typeBindings.QueryType = QueryType
_Namespace.addCategoryObject('typeBinding', 'QueryType', QueryType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}ElementSetNameType with content type SIMPLE
class ElementSetNameType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/cat/csw/2.0.2}ElementSetNameType with content type SIMPLE"""
    _TypeDefinition = ElementSetType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'ElementSetNameType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 273, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is ElementSetType
    
    # Attribute typeNames uses Python identifier typeNames
    __typeNames = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typeNames'), 'typeNames', '__httpwww_opengis_netcatcsw2_0_2_ElementSetNameType_typeNames', _module_typeBindings.TypeNameListType)
    __typeNames._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 276, 12)
    __typeNames._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 276, 12)
    
    typeNames = property(__typeNames.value, __typeNames.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __typeNames.name() : __typeNames
    })
_module_typeBindings.ElementSetNameType = ElementSetNameType
_Namespace.addCategoryObject('typeBinding', 'ElementSetNameType', ElementSetNameType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}SearchResultsType with content type ELEMENT_ONLY
class SearchResultsType (pyxb.binding.basis.complexTypeDefinition):
    """Includes representations of result set members if maxRecords > 0.
         The items must conform to one of the csw:Record views or a 
         profile-specific representation. 
         
         resultSetId  - id of the result set (a URI).
         elementSet  - The element set that has been returned
                       (i.e., "brief", "summary", "full")
         recordSchema  - schema reference for included records(URI)
         numberOfRecordsMatched  - number of records matched by the query
         numberOfRecordsReturned - number of records returned to client
         nextRecord - position of next record in the result set
                      (0 if no records remain).
         expires - the time instant when the result set expires and 
                   is discarded (ISO 8601 format)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'SearchResultsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 325, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}AbstractRecord uses Python identifier AbstractRecord
    __AbstractRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'AbstractRecord'), 'AbstractRecord', '__httpwww_opengis_netcatcsw2_0_2_SearchResultsType_httpwww_opengis_netcatcsw2_0_2AbstractRecord', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 29, 3), )

    
    AbstractRecord = property(__AbstractRecord.value, __AbstractRecord.set, None, None)

    
    # Attribute resultSetId uses Python identifier resultSetId
    __resultSetId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'resultSetId'), 'resultSetId', '__httpwww_opengis_netcatcsw2_0_2_SearchResultsType_resultSetId', pyxb.binding.datatypes.anyURI)
    __resultSetId._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 350, 6)
    __resultSetId._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 350, 6)
    
    resultSetId = property(__resultSetId.value, __resultSetId.set, None, None)

    
    # Attribute elementSet uses Python identifier elementSet
    __elementSet = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'elementSet'), 'elementSet', '__httpwww_opengis_netcatcsw2_0_2_SearchResultsType_elementSet', _module_typeBindings.ElementSetType)
    __elementSet._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 352, 6)
    __elementSet._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 352, 6)
    
    elementSet = property(__elementSet.value, __elementSet.set, None, None)

    
    # Attribute recordSchema uses Python identifier recordSchema
    __recordSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'recordSchema'), 'recordSchema', '__httpwww_opengis_netcatcsw2_0_2_SearchResultsType_recordSchema', pyxb.binding.datatypes.anyURI)
    __recordSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 354, 6)
    __recordSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 354, 6)
    
    recordSchema = property(__recordSchema.value, __recordSchema.set, None, None)

    
    # Attribute numberOfRecordsMatched uses Python identifier numberOfRecordsMatched
    __numberOfRecordsMatched = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numberOfRecordsMatched'), 'numberOfRecordsMatched', '__httpwww_opengis_netcatcsw2_0_2_SearchResultsType_numberOfRecordsMatched', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    __numberOfRecordsMatched._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 356, 6)
    __numberOfRecordsMatched._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 356, 6)
    
    numberOfRecordsMatched = property(__numberOfRecordsMatched.value, __numberOfRecordsMatched.set, None, None)

    
    # Attribute numberOfRecordsReturned uses Python identifier numberOfRecordsReturned
    __numberOfRecordsReturned = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numberOfRecordsReturned'), 'numberOfRecordsReturned', '__httpwww_opengis_netcatcsw2_0_2_SearchResultsType_numberOfRecordsReturned', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    __numberOfRecordsReturned._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 358, 6)
    __numberOfRecordsReturned._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 358, 6)
    
    numberOfRecordsReturned = property(__numberOfRecordsReturned.value, __numberOfRecordsReturned.set, None, None)

    
    # Attribute nextRecord uses Python identifier nextRecord
    __nextRecord = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nextRecord'), 'nextRecord', '__httpwww_opengis_netcatcsw2_0_2_SearchResultsType_nextRecord', pyxb.binding.datatypes.nonNegativeInteger)
    __nextRecord._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 360, 6)
    __nextRecord._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 360, 6)
    
    nextRecord = property(__nextRecord.value, __nextRecord.set, None, None)

    
    # Attribute expires uses Python identifier expires
    __expires = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'expires'), 'expires', '__httpwww_opengis_netcatcsw2_0_2_SearchResultsType_expires', pyxb.binding.datatypes.dateTime)
    __expires._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 362, 6)
    __expires._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 362, 6)
    
    expires = property(__expires.value, __expires.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __AbstractRecord.name() : __AbstractRecord
    })
    _AttributeMap.update({
        __resultSetId.name() : __resultSetId,
        __elementSet.name() : __elementSet,
        __recordSchema.name() : __recordSchema,
        __numberOfRecordsMatched.name() : __numberOfRecordsMatched,
        __numberOfRecordsReturned.name() : __numberOfRecordsReturned,
        __nextRecord.name() : __nextRecord,
        __expires.name() : __expires
    })
_module_typeBindings.SearchResultsType = SearchResultsType
_Namespace.addCategoryObject('typeBinding', 'SearchResultsType', SearchResultsType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}GetRecordByIdType with content type ELEMENT_ONLY
class GetRecordByIdType (RequestBaseType):
    """
            Convenience operation to retrieve default record representations 
            by identifier.
            Id - object identifier (a URI) that provides a reference to a 
                 catalogue item (or a result set if the catalogue supports 
                 persistent result sets).
            ElementSetName - one of "brief, "summary", or "full"
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'GetRecordByIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 366, 3)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}ElementSetName uses Python identifier ElementSetName
    __ElementSetName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'ElementSetName'), 'ElementSetName', '__httpwww_opengis_netcatcsw2_0_2_GetRecordByIdType_httpwww_opengis_netcatcsw2_0_2ElementSetName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 271, 3), )

    
    ElementSetName = property(__ElementSetName.value, __ElementSetName.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'Id'), 'Id', '__httpwww_opengis_netcatcsw2_0_2_GetRecordByIdType_httpwww_opengis_netcatcsw2_0_2Id', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 380, 15), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Attribute service inherited from {http://www.opengis.net/cat/csw/2.0.2}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/cat/csw/2.0.2}RequestBaseType
    
    # Attribute outputFormat uses Python identifier outputFormat
    __outputFormat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'outputFormat'), 'outputFormat', '__httpwww_opengis_netcatcsw2_0_2_GetRecordByIdType_outputFormat', pyxb.binding.datatypes.string, unicode_default='application/xml')
    __outputFormat._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 383, 12)
    __outputFormat._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 383, 12)
    
    outputFormat = property(__outputFormat.value, __outputFormat.set, None, None)

    
    # Attribute outputSchema uses Python identifier outputSchema
    __outputSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'outputSchema'), 'outputSchema', '__httpwww_opengis_netcatcsw2_0_2_GetRecordByIdType_outputSchema', pyxb.binding.datatypes.anyURI)
    __outputSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 385, 12)
    __outputSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 385, 12)
    
    outputSchema = property(__outputSchema.value, __outputSchema.set, None, None)

    _ElementMap.update({
        __ElementSetName.name() : __ElementSetName,
        __Id.name() : __Id
    })
    _AttributeMap.update({
        __outputFormat.name() : __outputFormat,
        __outputSchema.name() : __outputSchema
    })
_module_typeBindings.GetRecordByIdType = GetRecordByIdType
_Namespace.addCategoryObject('typeBinding', 'GetRecordByIdType', GetRecordByIdType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}GetDomainType with content type ELEMENT_ONLY
class GetDomainType (RequestBaseType):
    """Requests the actual values of some specified request parameter 
        or other data element."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'GetDomainType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 408, 3)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}PropertyName uses Python identifier PropertyName
    __PropertyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'PropertyName'), 'PropertyName', '__httpwww_opengis_netcatcsw2_0_2_GetDomainType_httpwww_opengis_netcatcsw2_0_2PropertyName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 417, 18), )

    
    PropertyName = property(__PropertyName.value, __PropertyName.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}ParameterName uses Python identifier ParameterName
    __ParameterName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'ParameterName'), 'ParameterName', '__httpwww_opengis_netcatcsw2_0_2_GetDomainType_httpwww_opengis_netcatcsw2_0_2ParameterName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 418, 18), )

    
    ParameterName = property(__ParameterName.value, __ParameterName.set, None, None)

    
    # Attribute service inherited from {http://www.opengis.net/cat/csw/2.0.2}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/cat/csw/2.0.2}RequestBaseType
    _ElementMap.update({
        __PropertyName.name() : __PropertyName,
        __ParameterName.name() : __ParameterName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GetDomainType = GetDomainType
_Namespace.addCategoryObject('typeBinding', 'GetDomainType', GetDomainType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}TransactionType with content type ELEMENT_ONLY
class TransactionType (RequestBaseType):
    """
            Users may insert, update, or delete catalogue entries. If the 
            verboseResponse attribute has the value "true", then one or more 
            csw:InsertResult elements must be included in the response.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'TransactionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 26, 3)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}Insert uses Python identifier Insert
    __Insert = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'Insert'), 'Insert', '__httpwww_opengis_netcatcsw2_0_2_TransactionType_httpwww_opengis_netcatcsw2_0_2Insert', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 38, 18), )

    
    Insert = property(__Insert.value, __Insert.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}Update uses Python identifier Update
    __Update = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'Update'), 'Update', '__httpwww_opengis_netcatcsw2_0_2_TransactionType_httpwww_opengis_netcatcsw2_0_2Update', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 39, 18), )

    
    Update = property(__Update.value, __Update.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}Delete uses Python identifier Delete
    __Delete = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'Delete'), 'Delete', '__httpwww_opengis_netcatcsw2_0_2_TransactionType_httpwww_opengis_netcatcsw2_0_2Delete', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 40, 18), )

    
    Delete = property(__Delete.value, __Delete.set, None, None)

    
    # Attribute service inherited from {http://www.opengis.net/cat/csw/2.0.2}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/cat/csw/2.0.2}RequestBaseType
    
    # Attribute verboseResponse uses Python identifier verboseResponse
    __verboseResponse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'verboseResponse'), 'verboseResponse', '__httpwww_opengis_netcatcsw2_0_2_TransactionType_verboseResponse', pyxb.binding.datatypes.boolean, unicode_default='false')
    __verboseResponse._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 43, 12)
    __verboseResponse._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 43, 12)
    
    verboseResponse = property(__verboseResponse.value, __verboseResponse.set, None, None)

    
    # Attribute requestId uses Python identifier requestId
    __requestId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'requestId'), 'requestId', '__httpwww_opengis_netcatcsw2_0_2_TransactionType_requestId', pyxb.binding.datatypes.anyURI)
    __requestId._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 45, 12)
    __requestId._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 45, 12)
    
    requestId = property(__requestId.value, __requestId.set, None, None)

    _ElementMap.update({
        __Insert.name() : __Insert,
        __Update.name() : __Update,
        __Delete.name() : __Delete
    })
    _AttributeMap.update({
        __verboseResponse.name() : __verboseResponse,
        __requestId.name() : __requestId
    })
_module_typeBindings.TransactionType = TransactionType
_Namespace.addCategoryObject('typeBinding', 'TransactionType', TransactionType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}HarvestType with content type ELEMENT_ONLY
class HarvestType (RequestBaseType):
    """
         Requests that the catalogue attempt to harvest a resource from some 
         network location identified by the source URL.

         Source          - a URL from which the resource is retrieved
         ResourceType    - normally a URI that specifies the type of the resource
                           (DCMES v1.1) being harvested if it is known.
         ResourceFormat  - a media type indicating the format of the 
                           resource being harvested.  The default is 
                           "application/xml".
         ResponseHandler - a reference to some endpoint to which the 
                           response shall be forwarded when the
                           harvest operation has been completed
         HarvestInterval - an interval expressed using the ISO 8601 syntax; 
                           it specifies the interval between harvest 
                           attempts (e.g., P6M indicates an interval of 
                           six months).
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'HarvestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 181, 3)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'Source'), 'Source', '__httpwww_opengis_netcatcsw2_0_2_HarvestType_httpwww_opengis_netcatcsw2_0_2Source', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 205, 15), )

    
    Source = property(__Source.value, __Source.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}ResourceType uses Python identifier ResourceType
    __ResourceType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'ResourceType'), 'ResourceType', '__httpwww_opengis_netcatcsw2_0_2_HarvestType_httpwww_opengis_netcatcsw2_0_2ResourceType', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 206, 15), )

    
    ResourceType = property(__ResourceType.value, __ResourceType.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}ResourceFormat uses Python identifier ResourceFormat
    __ResourceFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'ResourceFormat'), 'ResourceFormat', '__httpwww_opengis_netcatcsw2_0_2_HarvestType_httpwww_opengis_netcatcsw2_0_2ResourceFormat', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 207, 15), )

    
    ResourceFormat = property(__ResourceFormat.value, __ResourceFormat.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}HarvestInterval uses Python identifier HarvestInterval
    __HarvestInterval = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'HarvestInterval'), 'HarvestInterval', '__httpwww_opengis_netcatcsw2_0_2_HarvestType_httpwww_opengis_netcatcsw2_0_2HarvestInterval', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 209, 15), )

    
    HarvestInterval = property(__HarvestInterval.value, __HarvestInterval.set, None, None)

    
    # Element {http://www.opengis.net/cat/csw/2.0.2}ResponseHandler uses Python identifier ResponseHandler
    __ResponseHandler = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'ResponseHandler'), 'ResponseHandler', '__httpwww_opengis_netcatcsw2_0_2_HarvestType_httpwww_opengis_netcatcsw2_0_2ResponseHandler', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 211, 15), )

    
    ResponseHandler = property(__ResponseHandler.value, __ResponseHandler.set, None, None)

    
    # Attribute service inherited from {http://www.opengis.net/cat/csw/2.0.2}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/cat/csw/2.0.2}RequestBaseType
    _ElementMap.update({
        __Source.name() : __Source,
        __ResourceType.name() : __ResourceType,
        __ResourceFormat.name() : __ResourceFormat,
        __HarvestInterval.name() : __HarvestInterval,
        __ResponseHandler.name() : __ResponseHandler
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.HarvestType = HarvestType
_Namespace.addCategoryObject('typeBinding', 'HarvestType', HarvestType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}DCMIRecordType with content type ELEMENT_ONLY
class DCMIRecordType (AbstractRecordType):
    """
            This type encapsulates all of the standard DCMI metadata terms,
            including the Dublin Core refinements; these terms may be mapped
            to the profile-specific information model.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'DCMIRecordType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 36, 3)
    _ElementMap = AbstractRecordType._ElementMap.copy()
    _AttributeMap = AbstractRecordType._AttributeMap.copy()
    # Base type is AbstractRecordType
    
    # Element {http://purl.org/dc/elements/1.1/}DC-element uses Python identifier DC_element
    __DC_element = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, 'DC-element'), 'DC_element', '__httpwww_opengis_netcatcsw2_0_2_DCMIRecordType_httppurl_orgdcelements1_1DC_element', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 29, 3), )

    
    DC_element = property(__DC_element.value, __DC_element.set, None, None)

    _ElementMap.update({
        __DC_element.name() : __DC_element
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DCMIRecordType = DCMIRecordType
_Namespace.addCategoryObject('typeBinding', 'DCMIRecordType', DCMIRecordType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}BriefRecordType with content type ELEMENT_ONLY
class BriefRecordType (AbstractRecordType):
    """
            This type defines a brief representation of the common record
            format.  It extends AbstractRecordType to include only the
             dc:identifier and dc:type properties.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'BriefRecordType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 55, 3)
    _ElementMap = AbstractRecordType._ElementMap.copy()
    _AttributeMap = AbstractRecordType._AttributeMap.copy()
    # Base type is AbstractRecordType
    
    # Element {http://purl.org/dc/elements/1.1/}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, 'title'), 'title', '__httpwww_opengis_netcatcsw2_0_2_BriefRecordType_httppurl_orgdcelements1_1title', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 30, 3), )

    
    title = property(__title.value, __title.set, None, 'A name given to the resource. Typically, Title will be a name by \n      which the resource is formally known.')

    
    # Element {http://purl.org/dc/elements/1.1/}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, 'type'), 'type', '__httpwww_opengis_netcatcsw2_0_2_BriefRecordType_httppurl_orgdcelements1_1type', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 91, 3), )

    
    type = property(__type.value, __type.set, None, 'The nature or genre of the content of the resource. Type includes \n      terms describing general categories, functions, genres, or aggregation \n      levels for content. Recommended best practice is to select a value \n      from a controlled vocabulary (for example, the DCMI Type Vocabulary). \n      To describe the physical or digital manifestation of the resource, \n      use the Format element.')

    
    # Element {http://purl.org/dc/elements/1.1/}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, 'identifier'), 'identifier', '__httpwww_opengis_netcatcsw2_0_2_BriefRecordType_httppurl_orgdcelements1_1identifier', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 114, 3), )

    
    identifier = property(__identifier.value, __identifier.set, None, 'An unambiguous reference to the resource within a given context. \n      Recommended best practice is to identify the resource by means of a \n      string or number conforming to a formal identification system. Formal \n      identification systems include but are not limited to the Uniform \n      Resource Identifier (URI) (including the Uniform Resource Locator \n      (URL)), the Digital Object Identifier (DOI), and the International \n      Standard Book Number (ISBN).')

    
    # Element {http://www.opengis.net/ows}BoundingBox uses Python identifier BoundingBox
    __BoundingBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'BoundingBox'), 'BoundingBox', '__httpwww_opengis_netcatcsw2_0_2_BriefRecordType_httpwww_opengis_netowsBoundingBox', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 68, 1), )

    
    BoundingBox = property(__BoundingBox.value, __BoundingBox.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __type.name() : __type,
        __identifier.name() : __identifier,
        __BoundingBox.name() : __BoundingBox
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BriefRecordType = BriefRecordType
_Namespace.addCategoryObject('typeBinding', 'BriefRecordType', BriefRecordType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}SummaryRecordType with content type ELEMENT_ONLY
class SummaryRecordType (AbstractRecordType):
    """
            This type defines a summary representation of the common record
            format.  It extends AbstractRecordType to include the core
            properties.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'SummaryRecordType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 81, 3)
    _ElementMap = AbstractRecordType._ElementMap.copy()
    _AttributeMap = AbstractRecordType._AttributeMap.copy()
    # Base type is AbstractRecordType
    
    # Element {http://purl.org/dc/elements/1.1/}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, 'title'), 'title', '__httpwww_opengis_netcatcsw2_0_2_SummaryRecordType_httppurl_orgdcelements1_1title', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 30, 3), )

    
    title = property(__title.value, __title.set, None, 'A name given to the resource. Typically, Title will be a name by \n      which the resource is formally known.')

    
    # Element {http://purl.org/dc/elements/1.1/}subject uses Python identifier subject
    __subject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, 'subject'), 'subject', '__httpwww_opengis_netcatcsw2_0_2_SummaryRecordType_httppurl_orgdcelements1_1subject', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 45, 3), )

    
    subject = property(__subject.value, __subject.set, None, 'A topic of the content of the resource. Typically, Subject will be \n      expressed as keywords, key phrases, or classification codes that \n      describe a topic of the resource. Recommended best practice is to \n      select a value from a controlled vocabulary or formal classification \n      scheme.')

    
    # Element {http://purl.org/dc/elements/1.1/}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, 'type'), 'type', '__httpwww_opengis_netcatcsw2_0_2_SummaryRecordType_httppurl_orgdcelements1_1type', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 91, 3), )

    
    type = property(__type.value, __type.set, None, 'The nature or genre of the content of the resource. Type includes \n      terms describing general categories, functions, genres, or aggregation \n      levels for content. Recommended best practice is to select a value \n      from a controlled vocabulary (for example, the DCMI Type Vocabulary). \n      To describe the physical or digital manifestation of the resource, \n      use the Format element.')

    
    # Element {http://purl.org/dc/elements/1.1/}format uses Python identifier format
    __format = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, 'format'), 'format', '__httpwww_opengis_netcatcsw2_0_2_SummaryRecordType_httppurl_orgdcelements1_1format', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 102, 3), )

    
    format = property(__format.value, __format.set, None, 'The physical or digital manifestation of the resource. Typically, \n      Format will include the media-type or dimensions of the resource. \n      Format may be used to identify the software, hardware, or other \n      equipment needed to display or operate the resource. Examples of \n      dimensions include size and duration. Recommended best practice is to \n      select a value from a controlled vocabulary (for example, the list \n      of Internet Media Types defining computer media formats).')

    
    # Element {http://purl.org/dc/elements/1.1/}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, 'identifier'), 'identifier', '__httpwww_opengis_netcatcsw2_0_2_SummaryRecordType_httppurl_orgdcelements1_1identifier', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 114, 3), )

    
    identifier = property(__identifier.value, __identifier.set, None, 'An unambiguous reference to the resource within a given context. \n      Recommended best practice is to identify the resource by means of a \n      string or number conforming to a formal identification system. Formal \n      identification systems include but are not limited to the Uniform \n      Resource Identifier (URI) (including the Uniform Resource Locator \n      (URL)), the Digital Object Identifier (DOI), and the International \n      Standard Book Number (ISBN).')

    
    # Element {http://purl.org/dc/elements/1.1/}relation uses Python identifier relation
    __relation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, 'relation'), 'relation', '__httpwww_opengis_netcatcsw2_0_2_SummaryRecordType_httppurl_orgdcelements1_1relation', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 146, 3), )

    
    relation = property(__relation.value, __relation.set, None, 'A reference to a related resource. Recommended best practice is to \n      identify the referenced resource by means of a string or number \n      conforming to a formal identification system.')

    
    # Element {http://purl.org/dc/terms/}abstract uses Python identifier abstract
    __abstract = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'abstract'), 'abstract', '__httpwww_opengis_netcatcsw2_0_2_SummaryRecordType_httppurl_orgdctermsabstract', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 13, 3), )

    
    abstract = property(__abstract.value, __abstract.set, None, None)

    
    # Element {http://purl.org/dc/terms/}modified uses Python identifier modified
    __modified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), 'modified', '__httpwww_opengis_netcatcsw2_0_2_SummaryRecordType_httppurl_orgdctermsmodified', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 64, 3), )

    
    modified = property(__modified.value, __modified.set, None, None)

    
    # Element {http://purl.org/dc/terms/}spatial uses Python identifier spatial
    __spatial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial'), 'spatial', '__httpwww_opengis_netcatcsw2_0_2_SummaryRecordType_httppurl_orgdctermsspatial', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 76, 3), )

    
    spatial = property(__spatial.value, __spatial.set, None, None)

    
    # Element {http://www.opengis.net/ows}BoundingBox uses Python identifier BoundingBox
    __BoundingBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'BoundingBox'), 'BoundingBox', '__httpwww_opengis_netcatcsw2_0_2_SummaryRecordType_httpwww_opengis_netowsBoundingBox', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 68, 1), )

    
    BoundingBox = property(__BoundingBox.value, __BoundingBox.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __subject.name() : __subject,
        __type.name() : __type,
        __format.name() : __format,
        __identifier.name() : __identifier,
        __relation.name() : __relation,
        __abstract.name() : __abstract,
        __modified.name() : __modified,
        __spatial.name() : __spatial,
        __BoundingBox.name() : __BoundingBox
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SummaryRecordType = SummaryRecordType
_Namespace.addCategoryObject('typeBinding', 'SummaryRecordType', SummaryRecordType)


# Complex type {http://www.opengis.net/cat/csw/2.0.2}RecordType with content type ELEMENT_ONLY
class RecordType (DCMIRecordType):
    """
            This type extends DCMIRecordType to add ows:BoundingBox;
            it may be used to specify a spatial envelope for the
            catalogued resource.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, 'RecordType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 119, 3)
    _ElementMap = DCMIRecordType._ElementMap.copy()
    _AttributeMap = DCMIRecordType._AttributeMap.copy()
    # Base type is DCMIRecordType
    
    # Element DC_element ({http://purl.org/dc/elements/1.1/}DC-element) inherited from {http://www.opengis.net/cat/csw/2.0.2}DCMIRecordType
    
    # Element {http://www.opengis.net/cat/csw/2.0.2}AnyText uses Python identifier AnyText
    __AnyText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace, 'AnyText'), 'AnyText', '__httpwww_opengis_netcatcsw2_0_2_RecordType_httpwww_opengis_netcatcsw2_0_2AnyText', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 130, 15), )

    
    AnyText = property(__AnyText.value, __AnyText.set, None, None)

    
    # Element {http://www.opengis.net/ows}BoundingBox uses Python identifier BoundingBox
    __BoundingBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'BoundingBox'), 'BoundingBox', '__httpwww_opengis_netcatcsw2_0_2_RecordType_httpwww_opengis_netowsBoundingBox', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 68, 1), )

    
    BoundingBox = property(__BoundingBox.value, __BoundingBox.set, None, None)

    _ElementMap.update({
        __AnyText.name() : __AnyText,
        __BoundingBox.name() : __BoundingBox
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RecordType = RecordType
_Namespace.addCategoryObject('typeBinding', 'RecordType', RecordType)


abstract = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'abstract'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 13, 3))
_Namespace_dct.addCategoryObject('elementBinding', abstract.name().localName(), abstract)

accessRights = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'accessRights'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 15, 3))
_Namespace_dct.addCategoryObject('elementBinding', accessRights.name().localName(), accessRights)

alternative = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'alternative'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 17, 3))
_Namespace_dct.addCategoryObject('elementBinding', alternative.name().localName(), alternative)

audience = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'audience'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 19, 3))
_Namespace_dct.addCategoryObject('elementBinding', audience.name().localName(), audience)

available = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'available'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 21, 3))
_Namespace_dct.addCategoryObject('elementBinding', available.name().localName(), available)

bibliographicCitation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'bibliographicCitation'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 23, 3))
_Namespace_dct.addCategoryObject('elementBinding', bibliographicCitation.name().localName(), bibliographicCitation)

conformsTo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'conformsTo'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 25, 3))
_Namespace_dct.addCategoryObject('elementBinding', conformsTo.name().localName(), conformsTo)

created = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'created'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 27, 3))
_Namespace_dct.addCategoryObject('elementBinding', created.name().localName(), created)

dateAccepted = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'dateAccepted'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 29, 3))
_Namespace_dct.addCategoryObject('elementBinding', dateAccepted.name().localName(), dateAccepted)

dateCopyrighted = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'dateCopyrighted'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 31, 3))
_Namespace_dct.addCategoryObject('elementBinding', dateCopyrighted.name().localName(), dateCopyrighted)

dateSubmitted = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'dateSubmitted'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 33, 3))
_Namespace_dct.addCategoryObject('elementBinding', dateSubmitted.name().localName(), dateSubmitted)

educationLevel = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'educationLevel'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 35, 3))
_Namespace_dct.addCategoryObject('elementBinding', educationLevel.name().localName(), educationLevel)

extent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'extent'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 37, 3))
_Namespace_dct.addCategoryObject('elementBinding', extent.name().localName(), extent)

hasFormat = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'hasFormat'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 39, 3))
_Namespace_dct.addCategoryObject('elementBinding', hasFormat.name().localName(), hasFormat)

hasPart = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'hasPart'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 41, 3))
_Namespace_dct.addCategoryObject('elementBinding', hasPart.name().localName(), hasPart)

hasVersion = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'hasVersion'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 43, 3))
_Namespace_dct.addCategoryObject('elementBinding', hasVersion.name().localName(), hasVersion)

isFormatOf = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'isFormatOf'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 45, 3))
_Namespace_dct.addCategoryObject('elementBinding', isFormatOf.name().localName(), isFormatOf)

isPartOf = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'isPartOf'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 47, 3))
_Namespace_dct.addCategoryObject('elementBinding', isPartOf.name().localName(), isPartOf)

isReferencedBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'isReferencedBy'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 49, 3))
_Namespace_dct.addCategoryObject('elementBinding', isReferencedBy.name().localName(), isReferencedBy)

isReplacedBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'isReplacedBy'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 51, 3))
_Namespace_dct.addCategoryObject('elementBinding', isReplacedBy.name().localName(), isReplacedBy)

isRequiredBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'isRequiredBy'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 53, 3))
_Namespace_dct.addCategoryObject('elementBinding', isRequiredBy.name().localName(), isRequiredBy)

issued = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 55, 3))
_Namespace_dct.addCategoryObject('elementBinding', issued.name().localName(), issued)

isVersionOf = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'isVersionOf'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 56, 3))
_Namespace_dct.addCategoryObject('elementBinding', isVersionOf.name().localName(), isVersionOf)

license = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'license'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 58, 3))
_Namespace_dct.addCategoryObject('elementBinding', license.name().localName(), license)

mediator = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'mediator'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 60, 3))
_Namespace_dct.addCategoryObject('elementBinding', mediator.name().localName(), mediator)

medium = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'medium'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 62, 3))
_Namespace_dct.addCategoryObject('elementBinding', medium.name().localName(), medium)

modified = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 64, 3))
_Namespace_dct.addCategoryObject('elementBinding', modified.name().localName(), modified)

provenance = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'provenance'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 66, 3))
_Namespace_dct.addCategoryObject('elementBinding', provenance.name().localName(), provenance)

references = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'references'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 68, 3))
_Namespace_dct.addCategoryObject('elementBinding', references.name().localName(), references)

replaces = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'replaces'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 70, 3))
_Namespace_dct.addCategoryObject('elementBinding', replaces.name().localName(), replaces)

requires = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'requires'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 72, 3))
_Namespace_dct.addCategoryObject('elementBinding', requires.name().localName(), requires)

rightsHolder = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'rightsHolder'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 74, 3))
_Namespace_dct.addCategoryObject('elementBinding', rightsHolder.name().localName(), rightsHolder)

spatial = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 76, 3))
_Namespace_dct.addCategoryObject('elementBinding', spatial.name().localName(), spatial)

tableOfContents = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'tableOfContents'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 78, 3))
_Namespace_dct.addCategoryObject('elementBinding', tableOfContents.name().localName(), tableOfContents)

temporal = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'temporal'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 80, 3))
_Namespace_dct.addCategoryObject('elementBinding', temporal.name().localName(), temporal)

valid = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'valid'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 82, 3))
_Namespace_dct.addCategoryObject('elementBinding', valid.name().localName(), valid)

GetCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'GetCapabilities'), GetCapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 45, 3))
_Namespace.addCategoryObject('elementBinding', GetCapabilities.name().localName(), GetCapabilities)

Capabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Capabilities'), CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 61, 3))
_Namespace.addCategoryObject('elementBinding', Capabilities.name().localName(), Capabilities)

DescribeRecordResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'DescribeRecordResponse'), DescribeRecordResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 103, 3))
_Namespace.addCategoryObject('elementBinding', DescribeRecordResponse.name().localName(), DescribeRecordResponse)

AbstractQuery = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'AbstractQuery'), AbstractQueryType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 211, 3))
_Namespace.addCategoryObject('elementBinding', AbstractQuery.name().localName(), AbstractQuery)

Constraint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Constraint'), QueryConstraintType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 254, 3))
_Namespace.addCategoryObject('elementBinding', Constraint.name().localName(), Constraint)

GetRecordsResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'GetRecordsResponse'), GetRecordsResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 293, 3))
_Namespace.addCategoryObject('elementBinding', GetRecordsResponse.name().localName(), GetRecordsResponse)

GetRecordByIdResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'GetRecordByIdResponse'), GetRecordByIdResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 390, 3))
_Namespace.addCategoryObject('elementBinding', GetRecordByIdResponse.name().localName(), GetRecordByIdResponse)

GetDomainResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'GetDomainResponse'), GetDomainResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 424, 3))
_Namespace.addCategoryObject('elementBinding', GetDomainResponse.name().localName(), GetDomainResponse)

Acknowledgement = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Acknowledgement'), AcknowledgementType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 470, 3))
_Namespace.addCategoryObject('elementBinding', Acknowledgement.name().localName(), Acknowledgement)

RecordProperty = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'RecordProperty'), RecordPropertyType, documentation='\n            The RecordProperty element is used to specify the new\n            value of a record property in an update statement.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 102, 3))
_Namespace.addCategoryObject('elementBinding', RecordProperty.name().localName(), RecordProperty)

TransactionResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'TransactionResponse'), TransactionResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 130, 3))
_Namespace.addCategoryObject('elementBinding', TransactionResponse.name().localName(), TransactionResponse)

HarvestResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'HarvestResponse'), HarvestResponseType, documentation='\n         The content of the response varies depending on the presence of the \n         ResponseHandler element. If present, then the catalogue should \n         verify the request and respond immediately with an csw:Acknowledgement \n         element in the response. The catalogue must then attempt to harvest \n         the resource at some later time and send the response message to the \n         location specified by the value of the ResponseHandler element using \n         the indicated protocol (e.g. ftp, mailto, http).\n         \n         If the ResponseHandler element is absent, then the catalogue \n         must attempt to harvest the resource immediately and include a \n         TransactionResponse element in the response.\n        \n         In any case, if the harvest attempt is successful the response \n         shall include summary representations of the newly created \n         catalogue item(s).\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 217, 3))
_Namespace.addCategoryObject('elementBinding', HarvestResponse.name().localName(), HarvestResponse)

AbstractRecord = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'AbstractRecord'), AbstractRecordType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 29, 3))
_Namespace.addCategoryObject('elementBinding', AbstractRecord.name().localName(), AbstractRecord)

DescribeRecord = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'DescribeRecord'), DescribeRecordType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 77, 3))
_Namespace.addCategoryObject('elementBinding', DescribeRecord.name().localName(), DescribeRecord)

GetRecords = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'GetRecords'), GetRecordsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 131, 3))
_Namespace.addCategoryObject('elementBinding', GetRecords.name().localName(), GetRecords)

Query = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Query'), QueryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 215, 3))
_Namespace.addCategoryObject('elementBinding', Query.name().localName(), Query)

ElementSetName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'ElementSetName'), ElementSetNameType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 271, 3), unicode_default='summary')
_Namespace.addCategoryObject('elementBinding', ElementSetName.name().localName(), ElementSetName)

GetRecordById = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'GetRecordById'), GetRecordByIdType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 364, 3))
_Namespace.addCategoryObject('elementBinding', GetRecordById.name().localName(), GetRecordById)

GetDomain = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'GetDomain'), GetDomainType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 407, 3))
_Namespace.addCategoryObject('elementBinding', GetDomain.name().localName(), GetDomain)

Transaction = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Transaction'), TransactionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 25, 3))
_Namespace.addCategoryObject('elementBinding', Transaction.name().localName(), Transaction)

Harvest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Harvest'), HarvestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 180, 3))
_Namespace.addCategoryObject('elementBinding', Harvest.name().localName(), Harvest)

DCMIRecord = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'DCMIRecord'), DCMIRecordType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 34, 3))
_Namespace.addCategoryObject('elementBinding', DCMIRecord.name().localName(), DCMIRecord)

BriefRecord = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'BriefRecord'), BriefRecordType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 53, 3))
_Namespace.addCategoryObject('elementBinding', BriefRecord.name().localName(), BriefRecord)

SummaryRecord = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'SummaryRecord'), SummaryRecordType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 79, 3))
_Namespace.addCategoryObject('elementBinding', SummaryRecord.name().localName(), SummaryRecord)

Record = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Record'), RecordType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 117, 3))
_Namespace.addCategoryObject('elementBinding', Record.name().localName(), Record)



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




CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter_Capabilities'), pyxb.bundles.opengis.filter.CTD_ANON, scope=CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 20, 3)))

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
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'ServiceIdentification')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 30, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'ServiceProvider')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'OperationsMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsGetCapabilities.xsd', 32, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter_Capabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 72, 15))
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
CapabilitiesType._Automaton = _BuildAutomaton_()




DescribeRecordResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'SchemaComponent'), SchemaComponentType, scope=DescribeRecordResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 112, 9)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 112, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DescribeRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'SchemaComponent')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 112, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DescribeRecordResponseType._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 125, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SchemaComponentType._Automaton = _BuildAutomaton_3()




QueryConstraintType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'CqlText'), pyxb.binding.datatypes.string, scope=QueryConstraintType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 263, 9)))

QueryConstraintType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter'), pyxb.bundles.opengis.filter.FilterType, scope=QueryConstraintType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 39, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryConstraintType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'Filter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 262, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryConstraintType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'CqlText')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 263, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryConstraintType._Automaton = _BuildAutomaton_4()




GetRecordsResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'RequestId'), pyxb.binding.datatypes.anyURI, scope=GetRecordsResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 304, 9)))

GetRecordsResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'SearchStatus'), RequestStatusType, scope=GetRecordsResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 305, 9)))

GetRecordsResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'SearchResults'), SearchResultsType, scope=GetRecordsResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 306, 9)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 304, 9))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GetRecordsResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'RequestId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 304, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GetRecordsResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'SearchStatus')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 305, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetRecordsResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'SearchResults')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 306, 9))
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
GetRecordsResponseType._Automaton = _BuildAutomaton_5()




GetRecordByIdResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'AbstractRecord'), AbstractRecordType, abstract=pyxb.binding.datatypes.boolean(1), scope=GetRecordByIdResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 29, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 400, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 402, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GetRecordByIdResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'AbstractRecord')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 400, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.opengis.net/cat/csw/2.0.2')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 402, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GetRecordByIdResponseType._Automaton = _BuildAutomaton_6()




GetDomainResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'DomainValues'), DomainValuesType, scope=GetDomainResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 433, 9)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetDomainResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'DomainValues')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 433, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GetDomainResponseType._Automaton = _BuildAutomaton_7()




DomainValuesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'PropertyName'), pyxb.binding.datatypes.anyURI, scope=DomainValuesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 440, 12)))

DomainValuesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'ParameterName'), pyxb.binding.datatypes.anyURI, scope=DomainValuesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 441, 12)))

DomainValuesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'ListOfValues'), ListOfValuesType, scope=DomainValuesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 444, 12)))

DomainValuesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'ConceptualScheme'), ConceptualSchemeType, scope=DomainValuesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 445, 12)))

DomainValuesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'RangeOfValues'), RangeOfValuesType, scope=DomainValuesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 446, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 443, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DomainValuesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'PropertyName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 440, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DomainValuesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'ParameterName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 441, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DomainValuesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'ListOfValues')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 444, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DomainValuesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'ConceptualScheme')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 445, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DomainValuesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'RangeOfValues')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 446, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
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
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DomainValuesType._Automaton = _BuildAutomaton_8()




ListOfValuesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Value'), pyxb.binding.datatypes.anyType, scope=ListOfValuesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 454, 9)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ListOfValuesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'Value')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 454, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ListOfValuesType._Automaton = _BuildAutomaton_9()




ConceptualSchemeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Name'), pyxb.binding.datatypes.string, scope=ConceptualSchemeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 459, 9)))

ConceptualSchemeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Document'), pyxb.binding.datatypes.anyURI, scope=ConceptualSchemeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 460, 9)))

ConceptualSchemeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Authority'), pyxb.binding.datatypes.anyURI, scope=ConceptualSchemeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 461, 9)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConceptualSchemeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'Name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 459, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConceptualSchemeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'Document')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 460, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConceptualSchemeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'Authority')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 461, 9))
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
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ConceptualSchemeType._Automaton = _BuildAutomaton_10()




RangeOfValuesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'MinValue'), pyxb.binding.datatypes.anyType, scope=RangeOfValuesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 466, 9)))

RangeOfValuesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'MaxValue'), pyxb.binding.datatypes.anyType, scope=RangeOfValuesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 467, 9)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RangeOfValuesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'MinValue')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 466, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RangeOfValuesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'MaxValue')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 467, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RangeOfValuesType._Automaton = _BuildAutomaton_11()




AcknowledgementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'EchoedRequest'), EchoedRequestType, scope=AcknowledgementType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 482, 9)))

AcknowledgementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'RequestId'), pyxb.binding.datatypes.anyURI, scope=AcknowledgementType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 483, 9)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 483, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AcknowledgementType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'EchoedRequest')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 482, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AcknowledgementType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'RequestId')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 483, 9))
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
AcknowledgementType._Automaton = _BuildAutomaton_12()




def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 492, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EchoedRequestType._Automaton = _BuildAutomaton_13()




def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.opengis.net/cat/csw/2.0.2')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 59, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InsertType._Automaton = _BuildAutomaton_14()




UpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Constraint'), QueryConstraintType, scope=UpdateType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 254, 3)))

UpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'RecordProperty'), RecordPropertyType, scope=UpdateType, documentation='\n            The RecordProperty element is used to specify the new\n            value of a record property in an update statement.\n         ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 102, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.opengis.net/cat/csw/2.0.2')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 80, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UpdateType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'RecordProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 82, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UpdateType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'Constraint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 83, 15))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UpdateType._Automaton = _BuildAutomaton_15()




DeleteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Constraint'), QueryConstraintType, scope=DeleteType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 254, 3)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DeleteType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'Constraint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 97, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DeleteType._Automaton = _BuildAutomaton_16()




RecordPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Name'), pyxb.binding.datatypes.string, scope=RecordPropertyType, documentation='\n                  The Name element contains the name of a property\n                  to be updated.  The name may be a path expression.\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 112, 9)))

RecordPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Value'), pyxb.binding.datatypes.anyType, scope=RecordPropertyType, documentation='\n                  The Value element contains the replacement value for the\n                  named property.\n               ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 120, 9)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 120, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RecordPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'Name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 112, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RecordPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'Value')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 120, 9))
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
RecordPropertyType._Automaton = _BuildAutomaton_17()




TransactionResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'TransactionSummary'), TransactionSummaryType, scope=TransactionResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 142, 9)))

TransactionResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'InsertResult'), InsertResultType, scope=TransactionResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 144, 9)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 144, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TransactionResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'TransactionSummary')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 142, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TransactionResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'InsertResult')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 144, 9))
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
TransactionResponseType._Automaton = _BuildAutomaton_18()




TransactionSummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'totalInserted'), pyxb.binding.datatypes.nonNegativeInteger, scope=TransactionSummaryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 158, 9)))

TransactionSummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'totalUpdated'), pyxb.binding.datatypes.nonNegativeInteger, scope=TransactionSummaryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 160, 9)))

TransactionSummaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'totalDeleted'), pyxb.binding.datatypes.nonNegativeInteger, scope=TransactionSummaryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 162, 9)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 158, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 160, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 162, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TransactionSummaryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'totalInserted')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 158, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TransactionSummaryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'totalUpdated')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 160, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TransactionSummaryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'totalDeleted')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 162, 9))
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
TransactionSummaryType._Automaton = _BuildAutomaton_19()




InsertResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'BriefRecord'), BriefRecordType, scope=InsertResultType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 53, 3)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InsertResultType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'BriefRecord')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 176, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InsertResultType._Automaton = _BuildAutomaton_20()




HarvestResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Acknowledgement'), AcknowledgementType, scope=HarvestResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 470, 3)))

HarvestResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'TransactionResponse'), TransactionResponseType, scope=HarvestResponseType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 130, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(HarvestResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'Acknowledgement')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 241, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(HarvestResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'TransactionResponse')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 242, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
HarvestResponseType._Automaton = _BuildAutomaton_21()




DescribeRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'TypeName'), pyxb.binding.datatypes.QName, scope=DescribeRecordType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 93, 15)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 93, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DescribeRecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'TypeName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 93, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DescribeRecordType._Automaton = _BuildAutomaton_22()




GetRecordsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'DistributedSearch'), DistributedSearchType, scope=GetRecordsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 145, 15)))

GetRecordsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'ResponseHandler'), pyxb.binding.datatypes.anyURI, scope=GetRecordsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 147, 15)))

GetRecordsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'AbstractQuery'), AbstractQueryType, abstract=pyxb.binding.datatypes.boolean(1), scope=GetRecordsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 211, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 145, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 147, 15))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GetRecordsType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'DistributedSearch')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 145, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GetRecordsType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'ResponseHandler')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 147, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetRecordsType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'AbstractQuery')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 150, 18))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.opengis.net/cat/csw/2.0.2')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 151, 18))
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
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GetRecordsType._Automaton = _BuildAutomaton_23()




QueryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'ElementName'), pyxb.binding.datatypes.QName, scope=QueryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 234, 18)))

QueryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Constraint'), QueryConstraintType, scope=QueryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 254, 3)))

QueryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'ElementSetName'), ElementSetNameType, scope=QueryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 271, 3), unicode_default='summary'))

QueryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ogc, 'SortBy'), pyxb.bundles.opengis.filter.SortByType, scope=QueryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/sort.xsd', 21, 3)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 238, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 239, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'ElementSetName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 233, 18))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'ElementName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 234, 18))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'Constraint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 238, 15))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(QueryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ogc, 'SortBy')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 239, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
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
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryType._Automaton = _BuildAutomaton_24()




SearchResultsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'AbstractRecord'), AbstractRecordType, abstract=pyxb.binding.datatypes.boolean(1), scope=SearchResultsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 29, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 344, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 346, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SearchResultsType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'AbstractRecord')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 344, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.opengis.net/cat/csw/2.0.2')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 346, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SearchResultsType._Automaton = _BuildAutomaton_25()




GetRecordByIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'ElementSetName'), ElementSetNameType, scope=GetRecordByIdType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 271, 3), unicode_default='summary'))

GetRecordByIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Id'), pyxb.binding.datatypes.anyURI, scope=GetRecordByIdType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 380, 15)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 381, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetRecordByIdType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'Id')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 380, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GetRecordByIdType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'ElementSetName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 381, 15))
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
GetRecordByIdType._Automaton = _BuildAutomaton_26()




GetDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'PropertyName'), pyxb.binding.datatypes.anyURI, scope=GetDomainType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 417, 18)))

GetDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'ParameterName'), pyxb.binding.datatypes.anyURI, scope=GetDomainType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 418, 18)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetDomainType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'PropertyName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 417, 18))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetDomainType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'ParameterName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-discovery.xsd', 418, 18))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GetDomainType._Automaton = _BuildAutomaton_27()




TransactionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Insert'), InsertType, scope=TransactionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 38, 18)))

TransactionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Update'), UpdateType, scope=TransactionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 39, 18)))

TransactionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Delete'), DeleteType, scope=TransactionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 40, 18)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TransactionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'Insert')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 38, 18))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TransactionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'Update')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 39, 18))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TransactionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'Delete')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 40, 18))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TransactionType._Automaton = _BuildAutomaton_28()




HarvestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'Source'), pyxb.binding.datatypes.anyURI, scope=HarvestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 205, 15)))

HarvestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'ResourceType'), pyxb.binding.datatypes.string, scope=HarvestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 206, 15)))

HarvestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'ResourceFormat'), pyxb.binding.datatypes.string, scope=HarvestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 207, 15), unicode_default='application/xml'))

HarvestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'HarvestInterval'), pyxb.binding.datatypes.duration, scope=HarvestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 209, 15)))

HarvestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'ResponseHandler'), pyxb.binding.datatypes.anyURI, scope=HarvestType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 211, 15)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 207, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 209, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 211, 15))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(HarvestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'Source')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 205, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(HarvestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'ResourceType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 206, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(HarvestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'ResourceFormat')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 207, 15))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(HarvestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'HarvestInterval')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 209, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(HarvestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'ResponseHandler')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/CSW-publication.xsd', 211, 15))
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
HarvestType._Automaton = _BuildAutomaton_29()




DCMIRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, 'DC-element'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, abstract=pyxb.binding.datatypes.boolean(1), scope=DCMIRecordType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 29, 3)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 89, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DCMIRecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, 'DC-element')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 90, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DCMIRecordType._Automaton = _BuildAutomaton_30()




BriefRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, 'title'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, scope=BriefRecordType, documentation='A name given to the resource. Typically, Title will be a name by \n      which the resource is formally known.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 30, 3)))

BriefRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, 'type'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, scope=BriefRecordType, documentation='The nature or genre of the content of the resource. Type includes \n      terms describing general categories, functions, genres, or aggregation \n      levels for content. Recommended best practice is to select a value \n      from a controlled vocabulary (for example, the DCMI Type Vocabulary). \n      To describe the physical or digital manifestation of the resource, \n      use the Format element.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 91, 3)))

BriefRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, 'identifier'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, scope=BriefRecordType, documentation='An unambiguous reference to the resource within a given context. \n      Recommended best practice is to identify the resource by means of a \n      string or number conforming to a formal identification system. Formal \n      identification systems include but are not limited to the Uniform \n      Resource Identifier (URI) (including the Uniform Resource Locator \n      (URL)), the Digital Object Identifier (DOI), and the International \n      Standard Book Number (ISBN).', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 114, 3)))

BriefRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'BoundingBox'), pyxb.bundles.opengis.ows.BoundingBoxType, scope=BriefRecordType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 68, 1)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 70, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 72, 15))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BriefRecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 66, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BriefRecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, 'title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 68, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BriefRecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, 'type')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 70, 15))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BriefRecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'BoundingBox')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 72, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
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
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BriefRecordType._Automaton = _BuildAutomaton_31()




SummaryRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, 'title'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, scope=SummaryRecordType, documentation='A name given to the resource. Typically, Title will be a name by \n      which the resource is formally known.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 30, 3)))

SummaryRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, 'subject'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, scope=SummaryRecordType, documentation='A topic of the content of the resource. Typically, Subject will be \n      expressed as keywords, key phrases, or classification codes that \n      describe a topic of the resource. Recommended best practice is to \n      select a value from a controlled vocabulary or formal classification \n      scheme.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 45, 3)))

SummaryRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, 'type'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, scope=SummaryRecordType, documentation='The nature or genre of the content of the resource. Type includes \n      terms describing general categories, functions, genres, or aggregation \n      levels for content. Recommended best practice is to select a value \n      from a controlled vocabulary (for example, the DCMI Type Vocabulary). \n      To describe the physical or digital manifestation of the resource, \n      use the Format element.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 91, 3)))

SummaryRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, 'format'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, scope=SummaryRecordType, documentation='The physical or digital manifestation of the resource. Typically, \n      Format will include the media-type or dimensions of the resource. \n      Format may be used to identify the software, hardware, or other \n      equipment needed to display or operate the resource. Examples of \n      dimensions include size and duration. Recommended best practice is to \n      select a value from a controlled vocabulary (for example, the list \n      of Internet Media Types defining computer media formats).', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 102, 3)))

SummaryRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, 'identifier'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, scope=SummaryRecordType, documentation='An unambiguous reference to the resource within a given context. \n      Recommended best practice is to identify the resource by means of a \n      string or number conforming to a formal identification system. Formal \n      identification systems include but are not limited to the Uniform \n      Resource Identifier (URI) (including the Uniform Resource Locator \n      (URL)), the Digital Object Identifier (DOI), and the International \n      Standard Book Number (ISBN).', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 114, 3)))

SummaryRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, 'relation'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, scope=SummaryRecordType, documentation='A reference to a related resource. Recommended best practice is to \n      identify the referenced resource by means of a string or number \n      conforming to a formal identification system.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 146, 3)))

SummaryRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'abstract'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, scope=SummaryRecordType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 13, 3)))

SummaryRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, scope=SummaryRecordType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 64, 3)))

SummaryRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial'), pyxb.bundles.opengis.csw_dc.SimpleLiteral, scope=SummaryRecordType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 76, 3)))

SummaryRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'BoundingBox'), pyxb.bundles.opengis.ows.BoundingBoxType, scope=SummaryRecordType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 68, 1)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 96, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 98, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 100, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 102, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 104, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 106, 15))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 108, 15))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 110, 15))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SummaryRecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 92, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SummaryRecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, 'title')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 94, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SummaryRecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, 'type')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 96, 15))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SummaryRecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, 'subject')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 98, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SummaryRecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, 'format')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 100, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SummaryRecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, 'relation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 102, 15))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SummaryRecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 104, 15))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SummaryRecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'abstract')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 106, 15))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(SummaryRecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 108, 15))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(SummaryRecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'BoundingBox')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 110, 15))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SummaryRecordType._Automaton = _BuildAutomaton_32()




RecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, 'AnyText'), EmptyType, scope=RecordType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 130, 15)))

RecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'BoundingBox'), pyxb.bundles.opengis.ows.BoundingBoxType, scope=RecordType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.0.0/owsCommon.xsd', 68, 1)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 89, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 130, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 132, 15))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, 'DC-element')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcterms.xsd', 90, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace, 'AnyText')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 130, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RecordType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'BoundingBox')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/record.xsd', 132, 15))
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
RecordType._Automaton = _BuildAutomaton_33()


abstract._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.description)

accessRights._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.rights)

alternative._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.title)

audience._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.DC_element)

available._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.date)

bibliographicCitation._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.identifier)

conformsTo._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.relation)

created._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.date)

dateAccepted._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.date)

dateCopyrighted._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.date)

dateSubmitted._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.date)

educationLevel._setSubstitutionGroup(audience)

extent._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.format)

hasFormat._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.relation)

hasPart._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.relation)

hasVersion._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.relation)

isFormatOf._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.relation)

isPartOf._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.relation)

isReferencedBy._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.relation)

isReplacedBy._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.relation)

isRequiredBy._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.relation)

issued._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.date)

isVersionOf._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.relation)

license._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.rights)

mediator._setSubstitutionGroup(audience)

medium._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.format)

modified._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.date)

provenance._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.DC_element)

references._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.relation)

replaces._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.relation)

requires._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.relation)

rightsHolder._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.DC_element)

spatial._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.coverage)

tableOfContents._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.description)

temporal._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.coverage)

valid._setSubstitutionGroup(pyxb.bundles.opengis.csw_dc.date)

Query._setSubstitutionGroup(AbstractQuery)

DCMIRecord._setSubstitutionGroup(AbstractRecord)

BriefRecord._setSubstitutionGroup(AbstractRecord)

SummaryRecord._setSubstitutionGroup(AbstractRecord)

Record._setSubstitutionGroup(AbstractRecord)
