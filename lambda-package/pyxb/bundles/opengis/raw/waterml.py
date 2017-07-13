# ./pyxb/bundles/opengis/raw/waterml.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e8093cd1c1d4e7011de9f171b6c8138239a66dfa
# Generated 2017-07-10 00:37:53.667706 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/waterml/2.0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:01214740-6508-11e7-94a8-0a55f9edafa5')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.bundles.common.xlink
import pyxb.bundles.opengis.gml_3_2
import pyxb.bundles.opengis._sams
import pyxb.bundles.opengis.iso19139.v20070417.gmd
import pyxb.bundles.opengis.swe_2_0
import pyxb.bundles.opengis.om_2_0
import pyxb.binding.datatypes
import pyxb.bundles.opengis._sam

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/waterml/2.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gml = pyxb.bundles.opengis.gml_3_2.Namespace
_Namespace_gml.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gmd = pyxb.bundles.opengis.iso19139.v20070417.gmd.Namespace
_Namespace_gmd.configureCategories(['typeBinding', 'elementBinding'])
_Namespace = pyxb.bundles.common.xlink.Namespace
_Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_sam = pyxb.bundles.opengis._sam.Namespace
_Namespace_sam.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_sams = pyxb.bundles.opengis._sams.Namespace
_Namespace_sams.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://www.opengis.net/waterml/2.0}SamplingFeatureMemberUnionSemantics
class SamplingFeatureMemberUnionSemantics (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SamplingFeatureMemberUnionSemantics')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 176, 1)
    _Documentation = None
SamplingFeatureMemberUnionSemantics._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SamplingFeatureMemberUnionSemantics, enum_prefix=None)
SamplingFeatureMemberUnionSemantics.byFeature = SamplingFeatureMemberUnionSemantics._CF_enumeration.addEnumeration(unicode_value='byFeature', tag='byFeature')
SamplingFeatureMemberUnionSemantics.byGroup = SamplingFeatureMemberUnionSemantics._CF_enumeration.addEnumeration(unicode_value='byGroup', tag='byGroup')
SamplingFeatureMemberUnionSemantics._InitializeFacetMap(SamplingFeatureMemberUnionSemantics._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SamplingFeatureMemberUnionSemantics', SamplingFeatureMemberUnionSemantics)
_module_typeBindings.SamplingFeatureMemberUnionSemantics = SamplingFeatureMemberUnionSemantics

# Complex type {http://www.opengis.net/waterml/2.0}CollectionType with content type ELEMENT_ONLY
class CollectionType (pyxb.bundles.opengis.gml_3_2.AbstractFeatureType):
    """Complex type {http://www.opengis.net/waterml/2.0}CollectionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CollectionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 36, 1)
    _ElementMap = pyxb.bundles.opengis.gml_3_2.AbstractFeatureType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_2.AbstractFeatureType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_2.AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element location ({http://www.opengis.net/gml/3.2}location) inherited from {http://www.opengis.net/gml/3.2}AbstractFeatureType
    
    # Element boundedBy ({http://www.opengis.net/gml/3.2}boundedBy) inherited from {http://www.opengis.net/gml/3.2}AbstractFeatureType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/waterml/2.0}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_opengis_netwaterml2_0_CollectionType_httpwww_opengis_netwaterml2_0metadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 40, 5), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element {http://www.opengis.net/waterml/2.0}temporalExtent uses Python identifier temporalExtent
    __temporalExtent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'temporalExtent'), 'temporalExtent', '__httpwww_opengis_netwaterml2_0_CollectionType_httpwww_opengis_netwaterml2_0temporalExtent', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 41, 5), )

    
    temporalExtent = property(__temporalExtent.value, __temporalExtent.set, None, 'Describes the temporal extent of the all the time series\n\t\t\t\t\t\t\t  contained within the collection (if they exist).')

    
    # Element {http://www.opengis.net/waterml/2.0}sourceDefinition uses Python identifier sourceDefinition
    __sourceDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sourceDefinition'), 'sourceDefinition', '__httpwww_opengis_netwaterml2_0_CollectionType_httpwww_opengis_netwaterml2_0sourceDefinition', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 53, 6), )

    
    sourceDefinition = property(__sourceDefinition.value, __sourceDefinition.set, None, 'Provides a context for identification of particular data elements through use of MD_DataIdentification. \n\t\t\t\t      These can be referenced from individual timeseries values. ')

    
    # Element {http://www.opengis.net/waterml/2.0}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameter'), 'parameter', '__httpwww_opengis_netwaterml2_0_CollectionType_httpwww_opengis_netwaterml2_0parameter', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 65, 6), )

    
    parameter = property(__parameter.value, __parameter.set, None, 'A soft-typed parameter for extra metadata properties.')

    
    # Element {http://www.opengis.net/waterml/2.0}localDictionary uses Python identifier localDictionary
    __localDictionary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'localDictionary'), 'localDictionary', '__httpwww_opengis_netwaterml2_0_CollectionType_httpwww_opengis_netwaterml2_0localDictionary', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 71, 5), )

    
    localDictionary = property(__localDictionary.value, __localDictionary.set, None, 'Contains inline defintions of observed phenomenon.')

    
    # Element {http://www.opengis.net/waterml/2.0}samplingFeatureMember uses Python identifier samplingFeatureMember
    __samplingFeatureMember = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'samplingFeatureMember'), 'samplingFeatureMember', '__httpwww_opengis_netwaterml2_0_CollectionType_httpwww_opengis_netwaterml2_0samplingFeatureMember', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 82, 5), )

    
    samplingFeatureMember = property(__samplingFeatureMember.value, __samplingFeatureMember.set, None, 'Contains sampling feature member items. This allows\n                                features of interest to be encoded at the header of a document and\n                                referenced later or collections of features to be encoded.\n                            ')

    
    # Element {http://www.opengis.net/waterml/2.0}observationMember uses Python identifier observationMember
    __observationMember = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'observationMember'), 'observationMember', '__httpwww_opengis_netwaterml2_0_CollectionType_httpwww_opengis_netwaterml2_0observationMember', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 90, 5), )

    
    observationMember = property(__observationMember.value, __observationMember.set, None, 'Contains members of Timeseries Observations. The type\n                                shown here is only OM_Observation as the restrictions of this occur\n                                using schematron. ')

    
    # Element {http://www.opengis.net/waterml/2.0}communityExtension uses Python identifier communityExtension
    __communityExtension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'communityExtension'), 'communityExtension', '__httpwww_opengis_netwaterml2_0_CollectionType_httpwww_opengis_netwaterml2_0communityExtension', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 97, 5), )

    
    communityExtension = property(__communityExtension.value, __communityExtension.set, None, 'Use this extention point for community-agreed extensions to the schema.')

    
    # Element {http://www.opengis.net/waterml/2.0}internalExtension uses Python identifier internalExtension
    __internalExtension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'internalExtension'), 'internalExtension', '__httpwww_opengis_netwaterml2_0_CollectionType_httpwww_opengis_netwaterml2_0internalExtension', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 102, 6), )

    
    internalExtension = property(__internalExtension.value, __internalExtension.set, None, 'Use this extention point for internal extensions that have not been defined for external use.')

    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    _ElementMap.update({
        __metadata.name() : __metadata,
        __temporalExtent.name() : __temporalExtent,
        __sourceDefinition.name() : __sourceDefinition,
        __parameter.name() : __parameter,
        __localDictionary.name() : __localDictionary,
        __samplingFeatureMember.name() : __samplingFeatureMember,
        __observationMember.name() : __observationMember,
        __communityExtension.name() : __communityExtension,
        __internalExtension.name() : __internalExtension
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CollectionType = CollectionType
Namespace.addCategoryObject('typeBinding', 'CollectionType', CollectionType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Describes the temporal extent of the all the time series
							  contained within the collection (if they exist)."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 46, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}TimePeriod uses Python identifier TimePeriod
    __TimePeriod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'TimePeriod'), 'TimePeriod', '__httpwww_opengis_netwaterml2_0_CTD_ANON_httpwww_opengis_netgml3_2TimePeriod', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/temporal.xsd', 133, 1), )

    
    TimePeriod = property(__TimePeriod.value, __TimePeriod.set, None, 'gml:TimePeriod acts as a one-dimensional geometric primitive that represents an identifiable extent in time.\nThe location in of a gml:TimePeriod is described by the temporal positions of the instants at which it begins and ends. The length of the period is equal to the temporal distance between the two bounding temporal positions. \nBoth beginning and end may be described in terms of their direct position using gml:TimePositionType which is an XML Schema simple content type, or by reference to an indentifiable time instant using gml:TimeInstantPropertyType.\nAlternatively a limit of a gml:TimePeriod may use the conventional GML property model to make a reference to a time instant described elsewhere, or a limit may be indicated as a direct position.')

    _ElementMap.update({
        __TimePeriod.name() : __TimePeriod
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Provides a context for identification of particular data elements through use of MD_DataIdentification. 
				      These can be referenced from individual timeseries values. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 58, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.isotc211.org/2005/gmd}MD_DataIdentification uses Python identifier MD_DataIdentification
    __MD_DataIdentification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gmd, 'MD_DataIdentification'), 'MD_DataIdentification', '__httpwww_opengis_netwaterml2_0_CTD_ANON__httpwww_isotc211_org2005gmdMD_DataIdentification', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/identification.xsd', 93, 1), )

    
    MD_DataIdentification = property(__MD_DataIdentification.value, __MD_DataIdentification.set, None, None)

    _ElementMap.update({
        __MD_DataIdentification.name() : __MD_DataIdentification
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Contains inline defintions of observed phenomenon."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 75, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}Dictionary uses Python identifier Dictionary
    __Dictionary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'Dictionary'), 'Dictionary', '__httpwww_opengis_netwaterml2_0_CTD_ANON_2_httpwww_opengis_netgml3_2Dictionary', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/dictionary.xsd', 55, 1), )

    
    Dictionary = property(__Dictionary.value, __Dictionary.set, None, 'Sets of definitions may be collected into dictionaries or collections.\nA gml:Dictionary is a non-abstract collection of definitions.\nThe gml:Dictionary content model adds a list of gml:dictionaryEntry properties that contain or reference gml:Definition objects.  A database handle (gml:id attribute) is required, in order that this collection may be referred to. The standard gml:identifier, gml:description, gml:descriptionReference and gml:name properties are available to reference or contain more information about this dictionary. The gml:description and gml:descriptionReference property elements may be used for a description of this dictionary. The derived gml:name element may be used for the name(s) of this dictionary. for remote definiton references gml:dictionaryEntry shall be used. If a Definition object contained within a Dictionary uses the descriptionReference property to refer to a remote definition, then this enables the inclusion of a remote definition in a local dictionary, giving a handle and identifier in the context of the local dictionary.')

    _ElementMap.update({
        __Dictionary.name() : __Dictionary
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type {http://www.opengis.net/waterml/2.0}CollectionPropertyType with content type ELEMENT_ONLY
class CollectionPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}CollectionPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CollectionPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 111, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}Collection uses Python identifier Collection
    __Collection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Collection'), 'Collection', '__httpwww_opengis_netwaterml2_0_CollectionPropertyType_httpwww_opengis_netwaterml2_0Collection', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 27, 1), )

    
    Collection = property(__Collection.value, __Collection.set, None, 'OGC WaterML2.0 defines a generic collection feature type to\n                allow the grouping of observations and/or sampling features with metadata to\n                describe the nature of the collection. Such collections are required in a number of\n                data exchange scenarios; whether the underlying transport technology is web\n                services, FTP or other technologies.')

    
    # Attribute {http://www.opengis.net/gml/3.2}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netwaterml2_0_CollectionPropertyType_httpwww_opengis_netgml3_2remoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/deprecatedTypes.xsd', 638, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 52, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, '')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netwaterml2_0_CollectionPropertyType_nilReason', pyxb.bundles.opengis.gml_3_2.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netwaterml2_0_CollectionPropertyType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    __owns._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    
    owns = property(__owns.value, __owns.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netwaterml2_0_CollectionPropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netwaterml2_0_CollectionPropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netwaterml2_0_CollectionPropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netwaterml2_0_CollectionPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netwaterml2_0_CollectionPropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netwaterml2_0_CollectionPropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netwaterml2_0_CollectionPropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __Collection.name() : __Collection
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __nilReason.name() : __nilReason,
        __owns.name() : __owns,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.CollectionPropertyType = CollectionPropertyType
Namespace.addCategoryObject('typeBinding', 'CollectionPropertyType', CollectionPropertyType)


# Complex type {http://www.opengis.net/waterml/2.0}DocumentMetadataType with content type ELEMENT_ONLY
class DocumentMetadataType (pyxb.bundles.opengis.gml_3_2.AbstractGMLType):
    """Metadata relating to the document, when it was created, by what etc.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DocumentMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 127, 1)
    _ElementMap = pyxb.bundles.opengis.gml_3_2.AbstractGMLType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_2.AbstractGMLType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_2.AbstractGMLType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/waterml/2.0}generationDate uses Python identifier generationDate
    __generationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'generationDate'), 'generationDate', '__httpwww_opengis_netwaterml2_0_DocumentMetadataType_httpwww_opengis_netwaterml2_0generationDate', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 135, 5), )

    
    generationDate = property(__generationDate.value, __generationDate.set, None, None)

    
    # Element {http://www.opengis.net/waterml/2.0}version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'version'), 'version', '__httpwww_opengis_netwaterml2_0_DocumentMetadataType_httpwww_opengis_netwaterml2_0version', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 136, 5), )

    
    version = property(__version.value, __version.set, None, None)

    
    # Element {http://www.opengis.net/waterml/2.0}generationSystem uses Python identifier generationSystem
    __generationSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'generationSystem'), 'generationSystem', '__httpwww_opengis_netwaterml2_0_DocumentMetadataType_httpwww_opengis_netwaterml2_0generationSystem', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 137, 5), )

    
    generationSystem = property(__generationSystem.value, __generationSystem.set, None, None)

    
    # Element {http://www.opengis.net/waterml/2.0}profile uses Python identifier profile
    __profile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'profile'), 'profile', '__httpwww_opengis_netwaterml2_0_DocumentMetadataType_httpwww_opengis_netwaterml2_0profile', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 138, 6), )

    
    profile = property(__profile.value, __profile.set, None, 'Used to specify the conformance classes that are in use within the collection document. The conformance classes are identified by the URL')

    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    _ElementMap.update({
        __generationDate.name() : __generationDate,
        __version.name() : __version,
        __generationSystem.name() : __generationSystem,
        __profile.name() : __profile
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DocumentMetadataType = DocumentMetadataType
Namespace.addCategoryObject('typeBinding', 'DocumentMetadataType', DocumentMetadataType)


# Complex type {http://www.opengis.net/waterml/2.0}DocumentMetadataPropertyType with content type ELEMENT_ONLY
class DocumentMetadataPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}DocumentMetadataPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DocumentMetadataPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 147, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}DocumentMetadata uses Python identifier DocumentMetadata
    __DocumentMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DocumentMetadata'), 'DocumentMetadata', '__httpwww_opengis_netwaterml2_0_DocumentMetadataPropertyType_httpwww_opengis_netwaterml2_0DocumentMetadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 122, 1), )

    
    DocumentMetadata = property(__DocumentMetadata.value, __DocumentMetadata.set, None, 'Metadata about the document')

    
    # Attribute {http://www.opengis.net/gml/3.2}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netwaterml2_0_DocumentMetadataPropertyType_httpwww_opengis_netgml3_2remoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/deprecatedTypes.xsd', 638, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 52, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, '')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netwaterml2_0_DocumentMetadataPropertyType_nilReason', pyxb.bundles.opengis.gml_3_2.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netwaterml2_0_DocumentMetadataPropertyType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    __owns._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    
    owns = property(__owns.value, __owns.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netwaterml2_0_DocumentMetadataPropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netwaterml2_0_DocumentMetadataPropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netwaterml2_0_DocumentMetadataPropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netwaterml2_0_DocumentMetadataPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netwaterml2_0_DocumentMetadataPropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netwaterml2_0_DocumentMetadataPropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netwaterml2_0_DocumentMetadataPropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __DocumentMetadata.name() : __DocumentMetadata
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __nilReason.name() : __nilReason,
        __owns.name() : __owns,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.DocumentMetadataPropertyType = DocumentMetadataPropertyType
Namespace.addCategoryObject('typeBinding', 'DocumentMetadataPropertyType', DocumentMetadataPropertyType)


# Complex type {http://www.opengis.net/waterml/2.0}MonitoringPointPropertyType with content type ELEMENT_ONLY
class MonitoringPointPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}MonitoringPointPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MonitoringPointPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 80, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}MonitoringPoint uses Python identifier MonitoringPoint
    __MonitoringPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MonitoringPoint'), 'MonitoringPoint', '__httpwww_opengis_netwaterml2_0_MonitoringPointPropertyType_httpwww_opengis_netwaterml2_0MonitoringPoint', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 25, 4), )

    
    MonitoringPoint = property(__MonitoringPoint.value, __MonitoringPoint.set, None, 'A (point) location where water flow or properties are reported, such as a stream gauge, rainfall gauge, or water quality monitoring site.')

    
    # Attribute {http://www.opengis.net/gml/3.2}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netwaterml2_0_MonitoringPointPropertyType_httpwww_opengis_netgml3_2remoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/deprecatedTypes.xsd', 638, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 52, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, '')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netwaterml2_0_MonitoringPointPropertyType_nilReason', pyxb.bundles.opengis.gml_3_2.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netwaterml2_0_MonitoringPointPropertyType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    __owns._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    
    owns = property(__owns.value, __owns.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netwaterml2_0_MonitoringPointPropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netwaterml2_0_MonitoringPointPropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netwaterml2_0_MonitoringPointPropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netwaterml2_0_MonitoringPointPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netwaterml2_0_MonitoringPointPropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netwaterml2_0_MonitoringPointPropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netwaterml2_0_MonitoringPointPropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __MonitoringPoint.name() : __MonitoringPoint
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __nilReason.name() : __nilReason,
        __owns.name() : __owns,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.MonitoringPointPropertyType = MonitoringPointPropertyType
Namespace.addCategoryObject('typeBinding', 'MonitoringPointPropertyType', MonitoringPointPropertyType)


# Complex type {http://www.opengis.net/waterml/2.0}TimeZoneType with content type ELEMENT_ONLY
class TimeZoneType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}TimeZoneType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeZoneType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 89, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}zoneOffset uses Python identifier zoneOffset
    __zoneOffset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'zoneOffset'), 'zoneOffset', '__httpwww_opengis_netwaterml2_0_TimeZoneType_httpwww_opengis_netwaterml2_0zoneOffset', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 91, 12), )

    
    zoneOffset = property(__zoneOffset.value, __zoneOffset.set, None, None)

    
    # Element {http://www.opengis.net/waterml/2.0}zoneAbbreviation uses Python identifier zoneAbbreviation
    __zoneAbbreviation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'zoneAbbreviation'), 'zoneAbbreviation', '__httpwww_opengis_netwaterml2_0_TimeZoneType_httpwww_opengis_netwaterml2_0zoneAbbreviation', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 92, 12), )

    
    zoneAbbreviation = property(__zoneAbbreviation.value, __zoneAbbreviation.set, None, None)

    _ElementMap.update({
        __zoneOffset.name() : __zoneOffset,
        __zoneAbbreviation.name() : __zoneAbbreviation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TimeZoneType = TimeZoneType
Namespace.addCategoryObject('typeBinding', 'TimeZoneType', TimeZoneType)


# Complex type {http://www.opengis.net/waterml/2.0}TimeZonePropertyType with content type ELEMENT_ONLY
class TimeZonePropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}TimeZonePropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeZonePropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 96, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}TimeZone uses Python identifier TimeZone
    __TimeZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TimeZone'), 'TimeZone', '__httpwww_opengis_netwaterml2_0_TimeZonePropertyType_httpwww_opengis_netwaterml2_0TimeZone', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 88, 4), )

    
    TimeZone = property(__TimeZone.value, __TimeZone.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netwaterml2_0_TimeZonePropertyType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    __owns._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    
    owns = property(__owns.value, __owns.set, None, None)

    _ElementMap.update({
        __TimeZone.name() : __TimeZone
    })
    _AttributeMap.update({
        __owns.name() : __owns
    })
_module_typeBindings.TimeZonePropertyType = TimeZonePropertyType
Namespace.addCategoryObject('typeBinding', 'TimeZonePropertyType', TimeZonePropertyType)


# Complex type {http://www.opengis.net/waterml/2.0}ObservationProcessType with content type ELEMENT_ONLY
class ObservationProcessType (pyxb.bundles.opengis.gml_3_2.AbstractFeatureType):
    """Complex type {http://www.opengis.net/waterml/2.0}ObservationProcessType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ObservationProcessType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 30, 2)
    _ElementMap = pyxb.bundles.opengis.gml_3_2.AbstractFeatureType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_2.AbstractFeatureType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_2.AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element location ({http://www.opengis.net/gml/3.2}location) inherited from {http://www.opengis.net/gml/3.2}AbstractFeatureType
    
    # Element boundedBy ({http://www.opengis.net/gml/3.2}boundedBy) inherited from {http://www.opengis.net/gml/3.2}AbstractFeatureType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/waterml/2.0}processType uses Python identifier processType
    __processType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'processType'), 'processType', '__httpwww_opengis_netwaterml2_0_ObservationProcessType_httpwww_opengis_netwaterml2_0processType', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 34, 10), )

    
    processType = property(__processType.value, __processType.set, None, 'A defintion of the type of process used in the observation. This may be a Sensor, ManualMethod, Algorithm or Simulation\n                (including models).')

    
    # Element {http://www.opengis.net/waterml/2.0}originatingProcess uses Python identifier originatingProcess
    __originatingProcess = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'originatingProcess'), 'originatingProcess', '__httpwww_opengis_netwaterml2_0_ObservationProcessType_httpwww_opengis_netwaterml2_0originatingProcess', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 40, 10), )

    
    originatingProcess = property(__originatingProcess.value, __originatingProcess.set, None, 'A reference to the original source of the data. For example, if this is a post-processed time series (and processType is\n                algorithm), this link would specify the original process that generated the data, e.g. the sensor. This allows the origin of the data\n                to be maintained regardless of the processing that has occured to it.')

    
    # Element {http://www.opengis.net/waterml/2.0}aggregationDuration uses Python identifier aggregationDuration
    __aggregationDuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aggregationDuration'), 'aggregationDuration', '__httpwww_opengis_netwaterml2_0_ObservationProcessType_httpwww_opengis_netwaterml2_0aggregationDuration', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 47, 10), )

    
    aggregationDuration = property(__aggregationDuration.value, __aggregationDuration.set, None, 'If the process involves temporal aggregation of a result set, the time duration over which data has been aggregated should be expressed here. E.g. hourly, daily aggregates.')

    
    # Element {http://www.opengis.net/waterml/2.0}verticalDatum uses Python identifier verticalDatum
    __verticalDatum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'verticalDatum'), 'verticalDatum', '__httpwww_opengis_netwaterml2_0_ObservationProcessType_httpwww_opengis_netwaterml2_0verticalDatum', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 52, 10), )

    
    verticalDatum = property(__verticalDatum.value, __verticalDatum.set, None, 'Specifies the datum that is used as the zero point for level measurements. This can be process-specific as opposed to the\n                gauge at the actual monitoring point.')

    
    # Element {http://www.opengis.net/waterml/2.0}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comment'), 'comment', '__httpwww_opengis_netwaterml2_0_ObservationProcessType_httpwww_opengis_netwaterml2_0comment', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 58, 10), )

    
    comment = property(__comment.value, __comment.set, None, 'Comments specific to the process from the operator or system performing the process.')

    
    # Element {http://www.opengis.net/waterml/2.0}processReference uses Python identifier processReference
    __processReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'processReference'), 'processReference', '__httpwww_opengis_netwaterml2_0_ObservationProcessType_httpwww_opengis_netwaterml2_0processReference', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 63, 10), )

    
    processReference = property(__processReference.value, __processReference.set, None, 'Reference to an external process definition.')

    
    # Element {http://www.opengis.net/waterml/2.0}input uses Python identifier input
    __input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'input'), 'input', '__httpwww_opengis_netwaterml2_0_ObservationProcessType_httpwww_opengis_netwaterml2_0input', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 68, 10), )

    
    input = property(__input.value, __input.set, None, 'A list of the inputs used in the process. This may be a list of references to the data sets used (e.g. model input\n                series) or an input array to an algorithm.')

    
    # Element {http://www.opengis.net/waterml/2.0}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameter'), 'parameter', '__httpwww_opengis_netwaterml2_0_ObservationProcessType_httpwww_opengis_netwaterml2_0parameter', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 74, 10), )

    
    parameter = property(__parameter.value, __parameter.set, None, 'A soft-typed parameter to allow arbitrary properties to be added to the description. This property uses the name-value type from ISO19156.')

    
    # Element {http://www.opengis.net/waterml/2.0}operator uses Python identifier operator
    __operator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'operator'), 'operator', '__httpwww_opengis_netwaterml2_0_ObservationProcessType_httpwww_opengis_netwaterml2_0operator', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 79, 10), )

    
    operator = property(__operator.value, __operator.set, None, 'Describes the party responsible for performing the process. E.g. the person performing the method or operating the sensor.')

    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    _ElementMap.update({
        __processType.name() : __processType,
        __originatingProcess.name() : __originatingProcess,
        __aggregationDuration.name() : __aggregationDuration,
        __verticalDatum.name() : __verticalDatum,
        __comment.name() : __comment,
        __processReference.name() : __processReference,
        __input.name() : __input,
        __parameter.name() : __parameter,
        __operator.name() : __operator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ObservationProcessType = ObservationProcessType
Namespace.addCategoryObject('typeBinding', 'ObservationProcessType', ObservationProcessType)


# Complex type {http://www.opengis.net/waterml/2.0}ObservationProcessPropertyType with content type ELEMENT_ONLY
class ObservationProcessPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}ObservationProcessPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ObservationProcessPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 88, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}ObservationProcess uses Python identifier ObservationProcess
    __ObservationProcess = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ObservationProcess'), 'ObservationProcess', '__httpwww_opengis_netwaterml2_0_ObservationProcessPropertyType_httpwww_opengis_netwaterml2_0ObservationProcess', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 18, 2), )

    
    ObservationProcess = property(__ObservationProcess.value, __ObservationProcess.set, None, 'A large number of direct in-situ hydrological observations are performed by a sensor or sensor system. Common types of sensors\n        include rain gauges, level gauges, quality sensors such as temperature, turbidity etc. Manual procedures may be also used to make measurements\n        at a particular sampling point. These may be ad-hoc visits to particular point that may be of interest, or continued visits to a well\n        identified sampling point. Procedures that generate derived or synthetic results also exist, such as those produced by algorithms or\n        simulations. Algorithms are commonly implemented in hydrological software to process data sets for reporting or other purposes. Examples\n        include: - Temporal interpolation or aggregation; - Spatial interpolation; - Quality assurance related tasks such as automatic spike removal\n        or gap filling; - Derivation of new observed phenomena such as calculation of volume from stage, discharge (flow) from stage\n        etc.')

    
    # Attribute {http://www.opengis.net/gml/3.2}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netwaterml2_0_ObservationProcessPropertyType_httpwww_opengis_netgml3_2remoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/deprecatedTypes.xsd', 638, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 52, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, '')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netwaterml2_0_ObservationProcessPropertyType_nilReason', pyxb.bundles.opengis.gml_3_2.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netwaterml2_0_ObservationProcessPropertyType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    __owns._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    
    owns = property(__owns.value, __owns.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netwaterml2_0_ObservationProcessPropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netwaterml2_0_ObservationProcessPropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netwaterml2_0_ObservationProcessPropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netwaterml2_0_ObservationProcessPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netwaterml2_0_ObservationProcessPropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netwaterml2_0_ObservationProcessPropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netwaterml2_0_ObservationProcessPropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __ObservationProcess.name() : __ObservationProcess
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __nilReason.name() : __nilReason,
        __owns.name() : __owns,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.ObservationProcessPropertyType = ObservationProcessPropertyType
Namespace.addCategoryObject('typeBinding', 'ObservationProcessPropertyType', ObservationProcessPropertyType)


# Complex type {http://www.opengis.net/waterml/2.0}TVPMetadataType with content type ELEMENT_ONLY
class TVPMetadataType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}TVPMetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TVPMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 30, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}quality uses Python identifier quality
    __quality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'quality'), 'quality', '__httpwww_opengis_netwaterml2_0_TVPMetadataType_httpwww_opengis_netwaterml2_0quality', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 32, 6), )

    
    quality = property(__quality.value, __quality.set, None, 'Defines the quality of the point (or the default if it is the defaultTimeValuePair) using an OGC WaterML2.0 quality code. The\n            qualifier element should be used for other assertions (e.g. using internal codes). ')

    
    # Element {http://www.opengis.net/waterml/2.0}nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nilReason'), 'nilReason', '__httpwww_opengis_netwaterml2_0_TVPMetadataType_httpwww_opengis_netwaterml2_0nilReason', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 38, 6), )

    
    nilReason = property(__nilReason.value, __nilReason.set, None, "Specifies the reason for a null point (xsi:nil='true'). Must be present if the value is null. ")

    
    # Element {http://www.opengis.net/waterml/2.0}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comment'), 'comment', '__httpwww_opengis_netwaterml2_0_TVPMetadataType_httpwww_opengis_netwaterml2_0comment', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 43, 6), )

    
    comment = property(__comment.value, __comment.set, None, 'Free text comment associated with the data point.')

    
    # Element {http://www.opengis.net/waterml/2.0}relatedObservation uses Python identifier relatedObservation
    __relatedObservation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relatedObservation'), 'relatedObservation', '__httpwww_opengis_netwaterml2_0_TVPMetadataType_httpwww_opengis_netwaterml2_0relatedObservation', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 48, 6), )

    
    relatedObservation = property(__relatedObservation.value, __relatedObservation.set, None, 'Defines a reference to an observation that is related to this point. E.g. derived from a sample.')

    
    # Element {http://www.opengis.net/waterml/2.0}qualifier uses Python identifier qualifier
    __qualifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'qualifier'), 'qualifier', '__httpwww_opengis_netwaterml2_0_TVPMetadataType_httpwww_opengis_netwaterml2_0qualifier', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 54, 6), )

    
    qualifier = property(__qualifier.value, __qualifier.set, None, 'A general qualifier for the point to define influencing conditions, or other qualifying information. A broader, more\n            flexible location for qualifiers.')

    
    # Element {http://www.opengis.net/waterml/2.0}processing uses Python identifier processing
    __processing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'processing'), 'processing', '__httpwww_opengis_netwaterml2_0_TVPMetadataType_httpwww_opengis_netwaterml2_0processing', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 60, 6), )

    
    processing = property(__processing.value, __processing.set, None, 'Defines what processing has occured on the data point using a reference to a code item.')

    
    # Element {http://www.opengis.net/waterml/2.0}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'source'), 'source', '__httpwww_opengis_netwaterml2_0_TVPMetadataType_httpwww_opengis_netwaterml2_0source', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 65, 6), )

    
    source = property(__source.value, __source.set, None, 'Defines the source of the value using a reference to an appropriate resource. This is used where the timeseries may be aggregated from multiple sources.his can be an internal link to om:OM_Observation/om:metadata/wml2:ObservationMetadata/gmd:identificationInfo/gmd:MD_DataIdentification')

    _ElementMap.update({
        __quality.name() : __quality,
        __nilReason.name() : __nilReason,
        __comment.name() : __comment,
        __relatedObservation.name() : __relatedObservation,
        __qualifier.name() : __qualifier,
        __processing.name() : __processing,
        __source.name() : __source
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TVPMetadataType = TVPMetadataType
Namespace.addCategoryObject('typeBinding', 'TVPMetadataType', TVPMetadataType)


# Complex type {http://www.opengis.net/waterml/2.0}TVPMetadataPropertyType with content type ELEMENT_ONLY
class TVPMetadataPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}TVPMetadataPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TVPMetadataPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 111, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}TVPMetadata uses Python identifier TVPMetadata
    __TVPMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TVPMetadata'), 'TVPMetadata', '__httpwww_opengis_netwaterml2_0_TVPMetadataPropertyType_httpwww_opengis_netwaterml2_0TVPMetadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 29, 2), )

    
    TVPMetadata = property(__TVPMetadata.value, __TVPMetadata.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netwaterml2_0_TVPMetadataPropertyType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    __owns._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    
    owns = property(__owns.value, __owns.set, None, None)

    _ElementMap.update({
        __TVPMetadata.name() : __TVPMetadata
    })
    _AttributeMap.update({
        __owns.name() : __owns
    })
_module_typeBindings.TVPMetadataPropertyType = TVPMetadataPropertyType
Namespace.addCategoryObject('typeBinding', 'TVPMetadataPropertyType', TVPMetadataPropertyType)


# Complex type {http://www.opengis.net/waterml/2.0}TVPMeasurementMetadataPropertyType with content type ELEMENT_ONLY
class TVPMeasurementMetadataPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}TVPMeasurementMetadataPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TVPMeasurementMetadataPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 118, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}TVPMeasurementMetadata uses Python identifier TVPMeasurementMetadata
    __TVPMeasurementMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TVPMeasurementMetadata'), 'TVPMeasurementMetadata', '__httpwww_opengis_netwaterml2_0_TVPMeasurementMetadataPropertyType_httpwww_opengis_netwaterml2_0TVPMeasurementMetadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 74, 2), )

    
    TVPMeasurementMetadata = property(__TVPMeasurementMetadata.value, __TVPMeasurementMetadata.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netwaterml2_0_TVPMeasurementMetadataPropertyType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    __owns._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    
    owns = property(__owns.value, __owns.set, None, None)

    _ElementMap.update({
        __TVPMeasurementMetadata.name() : __TVPMeasurementMetadata
    })
    _AttributeMap.update({
        __owns.name() : __owns
    })
_module_typeBindings.TVPMeasurementMetadataPropertyType = TVPMeasurementMetadataPropertyType
Namespace.addCategoryObject('typeBinding', 'TVPMeasurementMetadataPropertyType', TVPMeasurementMetadataPropertyType)


# Complex type {http://www.opengis.net/waterml/2.0}TVPDefaultMetadataPropertyType with content type ELEMENT_ONLY
class TVPDefaultMetadataPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}TVPDefaultMetadataPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TVPDefaultMetadataPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 125, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}DefaultTVPMetadata uses Python identifier DefaultTVPMetadata
    __DefaultTVPMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DefaultTVPMetadata'), 'DefaultTVPMetadata', '__httpwww_opengis_netwaterml2_0_TVPDefaultMetadataPropertyType_httpwww_opengis_netwaterml2_0DefaultTVPMetadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 309, 2), )

    
    DefaultTVPMetadata = property(__DefaultTVPMetadata.value, __DefaultTVPMetadata.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netwaterml2_0_TVPDefaultMetadataPropertyType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    __owns._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    
    owns = property(__owns.value, __owns.set, None, None)

    _ElementMap.update({
        __DefaultTVPMetadata.name() : __DefaultTVPMetadata
    })
    _AttributeMap.update({
        __owns.name() : __owns
    })
_module_typeBindings.TVPDefaultMetadataPropertyType = TVPDefaultMetadataPropertyType
Namespace.addCategoryObject('typeBinding', 'TVPDefaultMetadataPropertyType', TVPDefaultMetadataPropertyType)


# Complex type {http://www.opengis.net/waterml/2.0}TimeseriesType with content type ELEMENT_ONLY
class TimeseriesType (pyxb.bundles.opengis.gml_3_2.AbstractFeatureType):
    """Complex type {http://www.opengis.net/waterml/2.0}TimeseriesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeseriesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 141, 2)
    _ElementMap = pyxb.bundles.opengis.gml_3_2.AbstractFeatureType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_2.AbstractFeatureType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_2.AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element location ({http://www.opengis.net/gml/3.2}location) inherited from {http://www.opengis.net/gml/3.2}AbstractFeatureType
    
    # Element boundedBy ({http://www.opengis.net/gml/3.2}boundedBy) inherited from {http://www.opengis.net/gml/3.2}AbstractFeatureType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/waterml/2.0}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_opengis_netwaterml2_0_TimeseriesType_httpwww_opengis_netwaterml2_0metadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 145, 10), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element {http://www.opengis.net/waterml/2.0}defaultPointMetadata uses Python identifier defaultPointMetadata
    __defaultPointMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'defaultPointMetadata'), 'defaultPointMetadata', '__httpwww_opengis_netwaterml2_0_TimeseriesType_httpwww_opengis_netwaterml2_0defaultPointMetadata', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 147, 10), )

    
    defaultPointMetadata = property(__defaultPointMetadata.value, __defaultPointMetadata.set, None, None)

    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    _ElementMap.update({
        __metadata.name() : __metadata,
        __defaultPointMetadata.name() : __defaultPointMetadata
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TimeseriesType = TimeseriesType
Namespace.addCategoryObject('typeBinding', 'TimeseriesType', TimeseriesType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 170, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}MeasurementTVP uses Python identifier MeasurementTVP
    __MeasurementTVP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MeasurementTVP'), 'MeasurementTVP', '__httpwww_opengis_netwaterml2_0_CTD_ANON_3_httpwww_opengis_netwaterml2_0MeasurementTVP', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 353, 2), )

    
    MeasurementTVP = property(__MeasurementTVP.value, __MeasurementTVP.set, None, None)

    _ElementMap.update({
        __MeasurementTVP.name() : __MeasurementTVP
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
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 193, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}CategoricalTVP uses Python identifier CategoricalTVP
    __CategoricalTVP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CategoricalTVP'), 'CategoricalTVP', '__httpwww_opengis_netwaterml2_0_CTD_ANON_4_httpwww_opengis_netwaterml2_0CategoricalTVP', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 370, 2), )

    
    CategoricalTVP = property(__CategoricalTVP.value, __CategoricalTVP.set, None, None)

    _ElementMap.update({
        __CategoricalTVP.name() : __CategoricalTVP
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type {http://www.opengis.net/waterml/2.0}TimeseriesPropertyType with content type ELEMENT_ONLY
class TimeseriesPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}TimeseriesPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeseriesPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 204, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}Timeseries uses Python identifier Timeseries
    __Timeseries = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Timeseries'), 'Timeseries', '__httpwww_opengis_netwaterml2_0_TimeseriesPropertyType_httpwww_opengis_netwaterml2_0Timeseries', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 135, 2), )

    
    Timeseries = property(__Timeseries.value, __Timeseries.set, None, 'Describes a time series as a collection of time-value pairs (implements TimeseriesTVP model type). A time series is a also a realisation of a discrete time coverage as\n        defined by ISO19123 - Coverages.')

    
    # Attribute {http://www.opengis.net/gml/3.2}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netwaterml2_0_TimeseriesPropertyType_httpwww_opengis_netgml3_2remoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/deprecatedTypes.xsd', 638, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 52, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, '')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netwaterml2_0_TimeseriesPropertyType_nilReason', pyxb.bundles.opengis.gml_3_2.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netwaterml2_0_TimeseriesPropertyType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    __owns._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    
    owns = property(__owns.value, __owns.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netwaterml2_0_TimeseriesPropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netwaterml2_0_TimeseriesPropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netwaterml2_0_TimeseriesPropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netwaterml2_0_TimeseriesPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netwaterml2_0_TimeseriesPropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netwaterml2_0_TimeseriesPropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netwaterml2_0_TimeseriesPropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __Timeseries.name() : __Timeseries
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __nilReason.name() : __nilReason,
        __owns.name() : __owns,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.TimeseriesPropertyType = TimeseriesPropertyType
Namespace.addCategoryObject('typeBinding', 'TimeseriesPropertyType', TimeseriesPropertyType)


# Complex type {http://www.opengis.net/waterml/2.0}TimeseriesMetadataType with content type ELEMENT_ONLY
class TimeseriesMetadataType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}TimeseriesMetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeseriesMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 214, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}temporalExtent uses Python identifier temporalExtent
    __temporalExtent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'temporalExtent'), 'temporalExtent', '__httpwww_opengis_netwaterml2_0_TimeseriesMetadataType_httpwww_opengis_netwaterml2_0temporalExtent', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 216, 6), )

    
    temporalExtent = property(__temporalExtent.value, __temporalExtent.set, None, 'Defines the start and end times of the represented time series.')

    
    # Element {http://www.opengis.net/waterml/2.0}baseTime uses Python identifier baseTime
    __baseTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'baseTime'), 'baseTime', '__httpwww_opengis_netwaterml2_0_TimeseriesMetadataType_httpwww_opengis_netwaterml2_0baseTime', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 221, 6), )

    
    baseTime = property(__baseTime.value, __baseTime.set, None, 'Defines the start time for isochronous (equidistant) time series. Each point occurs at regular steps (defined by the spacing\n            property). If baseTime is specified you must supply a spacing element. ')

    
    # Element {http://www.opengis.net/waterml/2.0}spacing uses Python identifier spacing
    __spacing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'spacing'), 'spacing', '__httpwww_opengis_netwaterml2_0_TimeseriesMetadataType_httpwww_opengis_netwaterml2_0spacing', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 227, 6), )

    
    spacing = property(__spacing.value, __spacing.set, None, 'The spacing between points for isochronous or equidistant (equally space) points. This is used with the baseTime element to allow calculation of time instants.')

    
    # Element {http://www.opengis.net/waterml/2.0}commentBlock uses Python identifier commentBlock
    __commentBlock = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'commentBlock'), 'commentBlock', '__httpwww_opengis_netwaterml2_0_TimeseriesMetadataType_httpwww_opengis_netwaterml2_0commentBlock', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 232, 6), )

    
    commentBlock = property(__commentBlock.value, __commentBlock.set, None, 'A comment that applies over a period of time for the time series.')

    
    # Element {http://www.opengis.net/waterml/2.0}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameter'), 'parameter', '__httpwww_opengis_netwaterml2_0_TimeseriesMetadataType_httpwww_opengis_netwaterml2_0parameter', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 238, 6), )

    
    parameter = property(__parameter.value, __parameter.set, None, 'A named-value extension point, allowing extra metadata to be associated with a timeseries. ')

    _ElementMap.update({
        __temporalExtent.name() : __temporalExtent,
        __baseTime.name() : __baseTime,
        __spacing.name() : __spacing,
        __commentBlock.name() : __commentBlock,
        __parameter.name() : __parameter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TimeseriesMetadataType = TimeseriesMetadataType
Namespace.addCategoryObject('typeBinding', 'TimeseriesMetadataType', TimeseriesMetadataType)


# Complex type {http://www.opengis.net/waterml/2.0}TimeseriesMetadataPropertyType with content type ELEMENT_ONLY
class TimeseriesMetadataPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}TimeseriesMetadataPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeseriesMetadataPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 246, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}TimeseriesMetadata uses Python identifier TimeseriesMetadata
    __TimeseriesMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TimeseriesMetadata'), 'TimeseriesMetadata', '__httpwww_opengis_netwaterml2_0_TimeseriesMetadataPropertyType_httpwww_opengis_netwaterml2_0TimeseriesMetadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 213, 2), )

    
    TimeseriesMetadata = property(__TimeseriesMetadata.value, __TimeseriesMetadata.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netwaterml2_0_TimeseriesMetadataPropertyType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    __owns._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    
    owns = property(__owns.value, __owns.set, None, None)

    _ElementMap.update({
        __TimeseriesMetadata.name() : __TimeseriesMetadata
    })
    _AttributeMap.update({
        __owns.name() : __owns
    })
_module_typeBindings.TimeseriesMetadataPropertyType = TimeseriesMetadataPropertyType
Namespace.addCategoryObject('typeBinding', 'TimeseriesMetadataPropertyType', TimeseriesMetadataPropertyType)


# Complex type {http://www.opengis.net/waterml/2.0}MeasurementTSMetadataPropertyType with content type ELEMENT_ONLY
class MeasurementTSMetadataPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}MeasurementTSMetadataPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasurementTSMetadataPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 297, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}MeasurementTimeseriesMetadata uses Python identifier MeasurementTimeseriesMetadata
    __MeasurementTimeseriesMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MeasurementTimeseriesMetadata'), 'MeasurementTimeseriesMetadata', '__httpwww_opengis_netwaterml2_0_MeasurementTSMetadataPropertyType_httpwww_opengis_netwaterml2_0MeasurementTimeseriesMetadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 254, 2), )

    
    MeasurementTimeseriesMetadata = property(__MeasurementTimeseriesMetadata.value, __MeasurementTimeseriesMetadata.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netwaterml2_0_MeasurementTSMetadataPropertyType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    __owns._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    
    owns = property(__owns.value, __owns.set, None, None)

    _ElementMap.update({
        __MeasurementTimeseriesMetadata.name() : __MeasurementTimeseriesMetadata
    })
    _AttributeMap.update({
        __owns.name() : __owns
    })
_module_typeBindings.MeasurementTSMetadataPropertyType = MeasurementTSMetadataPropertyType
Namespace.addCategoryObject('typeBinding', 'MeasurementTSMetadataPropertyType', MeasurementTSMetadataPropertyType)


# Complex type {http://www.opengis.net/waterml/2.0}DefaultTVPMetadataPropertyType with content type ELEMENT_ONLY
class DefaultTVPMetadataPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}DefaultTVPMetadataPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DefaultTVPMetadataPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 329, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}DefaultTVPMetadata uses Python identifier DefaultTVPMetadata
    __DefaultTVPMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DefaultTVPMetadata'), 'DefaultTVPMetadata', '__httpwww_opengis_netwaterml2_0_DefaultTVPMetadataPropertyType_httpwww_opengis_netwaterml2_0DefaultTVPMetadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 309, 2), )

    
    DefaultTVPMetadata = property(__DefaultTVPMetadata.value, __DefaultTVPMetadata.set, None, None)

    
    # Attribute {http://www.opengis.net/gml/3.2}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netwaterml2_0_DefaultTVPMetadataPropertyType_httpwww_opengis_netgml3_2remoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/deprecatedTypes.xsd', 638, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 52, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, '')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netwaterml2_0_DefaultTVPMetadataPropertyType_nilReason', pyxb.bundles.opengis.gml_3_2.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netwaterml2_0_DefaultTVPMetadataPropertyType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    __owns._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    
    owns = property(__owns.value, __owns.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netwaterml2_0_DefaultTVPMetadataPropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netwaterml2_0_DefaultTVPMetadataPropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netwaterml2_0_DefaultTVPMetadataPropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netwaterml2_0_DefaultTVPMetadataPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netwaterml2_0_DefaultTVPMetadataPropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netwaterml2_0_DefaultTVPMetadataPropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netwaterml2_0_DefaultTVPMetadataPropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __DefaultTVPMetadata.name() : __DefaultTVPMetadata
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __nilReason.name() : __nilReason,
        __owns.name() : __owns,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.DefaultTVPMetadataPropertyType = DefaultTVPMetadataPropertyType
Namespace.addCategoryObject('typeBinding', 'DefaultTVPMetadataPropertyType', DefaultTVPMetadataPropertyType)


# Complex type {http://www.opengis.net/waterml/2.0}TimeValuePairType with content type ELEMENT_ONLY
class TimeValuePairType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}TimeValuePairType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeValuePairType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 343, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}time uses Python identifier time
    __time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'time'), 'time', '__httpwww_opengis_netwaterml2_0_TimeValuePairType_httpwww_opengis_netwaterml2_0time', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 345, 6), )

    
    time = property(__time.value, __time.set, None, 'The time instant for the data point.')

    _ElementMap.update({
        __time.name() : __time
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TimeValuePairType = TimeValuePairType
Namespace.addCategoryObject('typeBinding', 'TimeValuePairType', TimeValuePairType)


# Complex type {http://www.opengis.net/waterml/2.0}CommentBlockType with content type ELEMENT_ONLY
class CommentBlockType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}CommentBlockType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommentBlockType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 390, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}applicablePeriod uses Python identifier applicablePeriod
    __applicablePeriod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'applicablePeriod'), 'applicablePeriod', '__httpwww_opengis_netwaterml2_0_CommentBlockType_httpwww_opengis_netwaterml2_0applicablePeriod', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 392, 6), )

    
    applicablePeriod = property(__applicablePeriod.value, __applicablePeriod.set, None, 'The period over which the comment applies.')

    
    # Element {http://www.opengis.net/waterml/2.0}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comment'), 'comment', '__httpwww_opengis_netwaterml2_0_CommentBlockType_httpwww_opengis_netwaterml2_0comment', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 397, 6), )

    
    comment = property(__comment.value, __comment.set, None, 'The comment that applies for the period.')

    _ElementMap.update({
        __applicablePeriod.name() : __applicablePeriod,
        __comment.name() : __comment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CommentBlockType = CommentBlockType
Namespace.addCategoryObject('typeBinding', 'CommentBlockType', CommentBlockType)


# Complex type {http://www.opengis.net/waterml/2.0}CommentBlockPropertyType with content type ELEMENT_ONLY
class CommentBlockPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}CommentBlockPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommentBlockPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 404, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}CommentBlock uses Python identifier CommentBlock
    __CommentBlock = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CommentBlock'), 'CommentBlock', '__httpwww_opengis_netwaterml2_0_CommentBlockPropertyType_httpwww_opengis_netwaterml2_0CommentBlock', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 389, 2), )

    
    CommentBlock = property(__CommentBlock.value, __CommentBlock.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netwaterml2_0_CommentBlockPropertyType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    __owns._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    
    owns = property(__owns.value, __owns.set, None, None)

    _ElementMap.update({
        __CommentBlock.name() : __CommentBlock
    })
    _AttributeMap.update({
        __owns.name() : __owns
    })
_module_typeBindings.CommentBlockPropertyType = CommentBlockPropertyType
Namespace.addCategoryObject('typeBinding', 'CommentBlockPropertyType', CommentBlockPropertyType)


# Complex type {http://www.opengis.net/waterml/2.0}MeasureType with content type SIMPLE
class MeasureType (pyxb.binding.basis.complexTypeDefinition):
    """gml:MeasureType supports recording an amount encoded as a value of XML Schema double, together with a units of measure indicated
        by an attribute uom, short for "units Of measure". The value of the uom attribute identifies a reference system for the amount, usually a
        ratio or interval scale. OGC WaterML2.0 alters this definition to make uom optional as this value is defaulted for a series."""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasureType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 415, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.double
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_opengis_netwaterml2_0_MeasureType_uom', pyxb.bundles.opengis.swe_2_0.UomSymbol)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 423, 8)
    __uom._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 423, 8)
    
    uom = property(__uom.value, __uom.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom
    })
_module_typeBindings.MeasureType = MeasureType
Namespace.addCategoryObject('typeBinding', 'MeasureType', MeasureType)


# Complex type {http://www.opengis.net/waterml/2.0}ObservationMetadataType with content type ELEMENT_ONLY
class ObservationMetadataType (pyxb.bundles.opengis.iso19139.v20070417.gmd.MD_Metadata_Type):
    """Complex type {http://www.opengis.net/waterml/2.0}ObservationMetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ObservationMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 25, 2)
    _ElementMap = pyxb.bundles.opengis.iso19139.v20070417.gmd.MD_Metadata_Type._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.iso19139.v20070417.gmd.MD_Metadata_Type._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.iso19139.v20070417.gmd.MD_Metadata_Type
    
    # Element fileIdentifier ({http://www.isotc211.org/2005/gmd}fileIdentifier) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element language ({http://www.isotc211.org/2005/gmd}language) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element characterSet ({http://www.isotc211.org/2005/gmd}characterSet) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element parentIdentifier ({http://www.isotc211.org/2005/gmd}parentIdentifier) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element hierarchyLevel ({http://www.isotc211.org/2005/gmd}hierarchyLevel) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element hierarchyLevelName ({http://www.isotc211.org/2005/gmd}hierarchyLevelName) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element contact ({http://www.isotc211.org/2005/gmd}contact) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element dateStamp ({http://www.isotc211.org/2005/gmd}dateStamp) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element metadataStandardName ({http://www.isotc211.org/2005/gmd}metadataStandardName) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element metadataStandardVersion ({http://www.isotc211.org/2005/gmd}metadataStandardVersion) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element dataSetURI ({http://www.isotc211.org/2005/gmd}dataSetURI) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element locale ({http://www.isotc211.org/2005/gmd}locale) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element spatialRepresentationInfo ({http://www.isotc211.org/2005/gmd}spatialRepresentationInfo) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element referenceSystemInfo ({http://www.isotc211.org/2005/gmd}referenceSystemInfo) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element metadataExtensionInfo ({http://www.isotc211.org/2005/gmd}metadataExtensionInfo) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element identificationInfo ({http://www.isotc211.org/2005/gmd}identificationInfo) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element contentInfo ({http://www.isotc211.org/2005/gmd}contentInfo) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element distributionInfo ({http://www.isotc211.org/2005/gmd}distributionInfo) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element dataQualityInfo ({http://www.isotc211.org/2005/gmd}dataQualityInfo) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element portrayalCatalogueInfo ({http://www.isotc211.org/2005/gmd}portrayalCatalogueInfo) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element metadataConstraints ({http://www.isotc211.org/2005/gmd}metadataConstraints) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element applicationSchemaInfo ({http://www.isotc211.org/2005/gmd}applicationSchemaInfo) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element metadataMaintenance ({http://www.isotc211.org/2005/gmd}metadataMaintenance) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element series ({http://www.isotc211.org/2005/gmd}series) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element describes ({http://www.isotc211.org/2005/gmd}describes) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element propertyType ({http://www.isotc211.org/2005/gmd}propertyType) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element featureType ({http://www.isotc211.org/2005/gmd}featureType) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element featureAttribute ({http://www.isotc211.org/2005/gmd}featureAttribute) inherited from {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
    
    # Element {http://www.opengis.net/waterml/2.0}intendedObservationSpacing uses Python identifier intendedObservationSpacing
    __intendedObservationSpacing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'intendedObservationSpacing'), 'intendedObservationSpacing', '__httpwww_opengis_netwaterml2_0_ObservationMetadataType_httpwww_opengis_netwaterml2_0intendedObservationSpacing', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 29, 10), )

    
    intendedObservationSpacing = property(__intendedObservationSpacing.value, __intendedObservationSpacing.set, None, 'Defines the expected interval in which observations can be expected. e.g. daily.')

    
    # Element {http://www.opengis.net/waterml/2.0}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__httpwww_opengis_netwaterml2_0_ObservationMetadataType_httpwww_opengis_netwaterml2_0status', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 34, 10), )

    
    status = property(__status.value, __status.set, None, 'Indicates the statues of the observation. E.g. unreleased, verified etc.')

    
    # Element {http://www.opengis.net/waterml/2.0}sampledMedium uses Python identifier sampledMedium
    __sampledMedium = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sampledMedium'), 'sampledMedium', '__httpwww_opengis_netwaterml2_0_ObservationMetadataType_httpwww_opengis_netwaterml2_0sampledMedium', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 39, 10), )

    
    sampledMedium = property(__sampledMedium.value, __sampledMedium.set, None, 'Indicates the medium that was sampled. E.g. water, air, etc.')

    
    # Element {http://www.opengis.net/waterml/2.0}maximumGap uses Python identifier maximumGap
    __maximumGap = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maximumGap'), 'maximumGap', '__httpwww_opengis_netwaterml2_0_ObservationMetadataType_httpwww_opengis_netwaterml2_0maximumGap', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 44, 10), )

    
    maximumGap = property(__maximumGap.value, __maximumGap.set, None, '\n                Defines the allowed gap between series when joining this time series with another. \n              ')

    
    # Element {http://www.opengis.net/waterml/2.0}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameter'), 'parameter', '__httpwww_opengis_netwaterml2_0_ObservationMetadataType_httpwww_opengis_netwaterml2_0parameter', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 51, 10), )

    
    parameter = property(__parameter.value, __parameter.set, None, 'A soft-typed parameter to allow extension through name-value pairs.')

    
    # Attribute id inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    
    # Attribute uuid inherited from {http://www.isotc211.org/2005/gco}AbstractObject_Type
    _ElementMap.update({
        __intendedObservationSpacing.name() : __intendedObservationSpacing,
        __status.name() : __status,
        __sampledMedium.name() : __sampledMedium,
        __maximumGap.name() : __maximumGap,
        __parameter.name() : __parameter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ObservationMetadataType = ObservationMetadataType
Namespace.addCategoryObject('typeBinding', 'ObservationMetadataType', ObservationMetadataType)


# Complex type {http://www.opengis.net/waterml/2.0}ObservationMetadataPropertyType with content type ELEMENT_ONLY
class ObservationMetadataPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}ObservationMetadataPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ObservationMetadataPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 61, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/waterml/2.0}ObservationMetadata uses Python identifier ObservationMetadata
    __ObservationMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ObservationMetadata'), 'ObservationMetadata', '__httpwww_opengis_netwaterml2_0_ObservationMetadataPropertyType_httpwww_opengis_netwaterml2_0ObservationMetadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 20, 2), )

    
    ObservationMetadata = property(__ObservationMetadata.value, __ObservationMetadata.set, None, 'Metadata relating to water observation. Specialisation of the ISO19115 MD_Metadata type. ')

    
    # Attribute {http://www.opengis.net/gml/3.2}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netwaterml2_0_ObservationMetadataPropertyType_httpwww_opengis_netgml3_2remoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/deprecatedTypes.xsd', 638, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 52, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, '')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netwaterml2_0_ObservationMetadataPropertyType_nilReason', pyxb.bundles.opengis.gml_3_2.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netwaterml2_0_ObservationMetadataPropertyType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    __owns._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    
    owns = property(__owns.value, __owns.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netwaterml2_0_ObservationMetadataPropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netwaterml2_0_ObservationMetadataPropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netwaterml2_0_ObservationMetadataPropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netwaterml2_0_ObservationMetadataPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netwaterml2_0_ObservationMetadataPropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netwaterml2_0_ObservationMetadataPropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netwaterml2_0_ObservationMetadataPropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __ObservationMetadata.name() : __ObservationMetadata
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __nilReason.name() : __nilReason,
        __owns.name() : __owns,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.ObservationMetadataPropertyType = ObservationMetadataPropertyType
Namespace.addCategoryObject('typeBinding', 'ObservationMetadataPropertyType', ObservationMetadataPropertyType)


# Complex type {http://www.opengis.net/waterml/2.0}SamplingFeatureMemberPropertyType with content type ELEMENT_ONLY
class SamplingFeatureMemberPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/waterml/2.0}SamplingFeatureMemberPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SamplingFeatureMemberPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 168, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/sampling/2.0}SF_SamplingFeatureCollection uses Python identifier SF_SamplingFeatureCollection
    __SF_SamplingFeatureCollection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_sam, 'SF_SamplingFeatureCollection'), 'SF_SamplingFeatureCollection', '__httpwww_opengis_netwaterml2_0_SamplingFeatureMemberPropertyType_httpwww_opengis_netsampling2_0SF_SamplingFeatureCollection', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sampling/2.0/samplingFeature.xsd', 216, 1), )

    
    SF_SamplingFeatureCollection = property(__SF_SamplingFeatureCollection.value, __SF_SamplingFeatureCollection.set, None, None)

    
    # Element {http://www.opengis.net/samplingSpatial/2.0}SF_SpatialSamplingFeature uses Python identifier SF_SpatialSamplingFeature
    __SF_SpatialSamplingFeature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_sams, 'SF_SpatialSamplingFeature'), 'SF_SpatialSamplingFeature', '__httpwww_opengis_netwaterml2_0_SamplingFeatureMemberPropertyType_httpwww_opengis_netsamplingSpatial2_0SF_SpatialSamplingFeature', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/samplingSpatial/2.0/spatialSamplingFeature.xsd', 140, 1), )

    
    SF_SpatialSamplingFeature = property(__SF_SpatialSamplingFeature.value, __SF_SpatialSamplingFeature.set, None, None)

    
    # Attribute {http://www.opengis.net/gml/3.2}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netwaterml2_0_SamplingFeatureMemberPropertyType_httpwww_opengis_netgml3_2remoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/deprecatedTypes.xsd', 638, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 52, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, '')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netwaterml2_0_SamplingFeatureMemberPropertyType_nilReason', pyxb.bundles.opengis.gml_3_2.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netwaterml2_0_SamplingFeatureMemberPropertyType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    __owns._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    
    owns = property(__owns.value, __owns.set, None, None)

    
    # Attribute unionSemantics uses Python identifier unionSemantics
    __unionSemantics = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unionSemantics'), 'unionSemantics', '__httpwww_opengis_netwaterml2_0_SamplingFeatureMemberPropertyType_unionSemantics', _module_typeBindings.SamplingFeatureMemberUnionSemantics)
    __unionSemantics._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 173, 2)
    __unionSemantics._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 173, 2)
    
    unionSemantics = property(__unionSemantics.value, __unionSemantics.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netwaterml2_0_SamplingFeatureMemberPropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netwaterml2_0_SamplingFeatureMemberPropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netwaterml2_0_SamplingFeatureMemberPropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netwaterml2_0_SamplingFeatureMemberPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netwaterml2_0_SamplingFeatureMemberPropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netwaterml2_0_SamplingFeatureMemberPropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netwaterml2_0_SamplingFeatureMemberPropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __SF_SamplingFeatureCollection.name() : __SF_SamplingFeatureCollection,
        __SF_SpatialSamplingFeature.name() : __SF_SpatialSamplingFeature
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __nilReason.name() : __nilReason,
        __owns.name() : __owns,
        __unionSemantics.name() : __unionSemantics,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.SamplingFeatureMemberPropertyType = SamplingFeatureMemberPropertyType
Namespace.addCategoryObject('typeBinding', 'SamplingFeatureMemberPropertyType', SamplingFeatureMemberPropertyType)


# Complex type {http://www.opengis.net/waterml/2.0}TVPMeasurementMetadataType with content type ELEMENT_ONLY
class TVPMeasurementMetadataType (TVPMetadataType):
    """Complex type {http://www.opengis.net/waterml/2.0}TVPMeasurementMetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TVPMeasurementMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 76, 2)
    _ElementMap = TVPMetadataType._ElementMap.copy()
    _AttributeMap = TVPMetadataType._AttributeMap.copy()
    # Base type is TVPMetadataType
    
    # Element quality ({http://www.opengis.net/waterml/2.0}quality) inherited from {http://www.opengis.net/waterml/2.0}TVPMetadataType
    
    # Element nilReason ({http://www.opengis.net/waterml/2.0}nilReason) inherited from {http://www.opengis.net/waterml/2.0}TVPMetadataType
    
    # Element comment ({http://www.opengis.net/waterml/2.0}comment) inherited from {http://www.opengis.net/waterml/2.0}TVPMetadataType
    
    # Element relatedObservation ({http://www.opengis.net/waterml/2.0}relatedObservation) inherited from {http://www.opengis.net/waterml/2.0}TVPMetadataType
    
    # Element qualifier ({http://www.opengis.net/waterml/2.0}qualifier) inherited from {http://www.opengis.net/waterml/2.0}TVPMetadataType
    
    # Element processing ({http://www.opengis.net/waterml/2.0}processing) inherited from {http://www.opengis.net/waterml/2.0}TVPMetadataType
    
    # Element source ({http://www.opengis.net/waterml/2.0}source) inherited from {http://www.opengis.net/waterml/2.0}TVPMetadataType
    
    # Element {http://www.opengis.net/waterml/2.0}uom uses Python identifier uom
    __uom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uom'), 'uom', '__httpwww_opengis_netwaterml2_0_TVPMeasurementMetadataType_httpwww_opengis_netwaterml2_0uom', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 80, 10), )

    
    uom = property(__uom.value, __uom.set, None, 'Defines the default unit of measure across the series. The uom code is specified using the UCUM code. ')

    
    # Element {http://www.opengis.net/waterml/2.0}interpolationType uses Python identifier interpolationType
    __interpolationType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'interpolationType'), 'interpolationType', '__httpwww_opengis_netwaterml2_0_TVPMeasurementMetadataType_httpwww_opengis_netwaterml2_0interpolationType', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 85, 10), )

    
    interpolationType = property(__interpolationType.value, __interpolationType.set, None, 'The interpolation type of the time series point. This describes the nature of the value to the time with which it is\n                associated. E.g. average in the preceeding interval. The URL codes are available at http://www.opengis.net/def/waterml/2.0/interpolationType/')

    
    # Element {http://www.opengis.net/waterml/2.0}censoredReason uses Python identifier censoredReason
    __censoredReason = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'censoredReason'), 'censoredReason', '__httpwww_opengis_netwaterml2_0_TVPMeasurementMetadataType_httpwww_opengis_netwaterml2_0censoredReason', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 91, 10), )

    
    censoredReason = property(__censoredReason.value, __censoredReason.set, None, 'Specifies the reason the value has been censored. e.g. left/right censoring, ')

    
    # Element {http://www.opengis.net/waterml/2.0}accuracy uses Python identifier accuracy
    __accuracy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'accuracy'), 'accuracy', '__httpwww_opengis_netwaterml2_0_TVPMeasurementMetadataType_httpwww_opengis_netwaterml2_0accuracy', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 96, 10), )

    
    accuracy = property(__accuracy.value, __accuracy.set, None, 'Used to specify the accuracy of a single value. ')

    
    # Element {http://www.opengis.net/waterml/2.0}aggregationDuration uses Python identifier aggregationDuration
    __aggregationDuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aggregationDuration'), 'aggregationDuration', '__httpwww_opengis_netwaterml2_0_TVPMeasurementMetadataType_httpwww_opengis_netwaterml2_0aggregationDuration', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 101, 10), )

    
    aggregationDuration = property(__aggregationDuration.value, __aggregationDuration.set, None, 'Describes the temporal aggregation that has occured to the value. ')

    _ElementMap.update({
        __uom.name() : __uom,
        __interpolationType.name() : __interpolationType,
        __censoredReason.name() : __censoredReason,
        __accuracy.name() : __accuracy,
        __aggregationDuration.name() : __aggregationDuration
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TVPMeasurementMetadataType = TVPMeasurementMetadataType
Namespace.addCategoryObject('typeBinding', 'TVPMeasurementMetadataType', TVPMeasurementMetadataType)


# Complex type {http://www.opengis.net/waterml/2.0}MeasurementTimeseriesType with content type ELEMENT_ONLY
class MeasurementTimeseriesType (TimeseriesType):
    """Complex type {http://www.opengis.net/waterml/2.0}MeasurementTimeseriesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasurementTimeseriesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 165, 2)
    _ElementMap = TimeseriesType._ElementMap.copy()
    _AttributeMap = TimeseriesType._AttributeMap.copy()
    # Base type is TimeseriesType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element location ({http://www.opengis.net/gml/3.2}location) inherited from {http://www.opengis.net/gml/3.2}AbstractFeatureType
    
    # Element boundedBy ({http://www.opengis.net/gml/3.2}boundedBy) inherited from {http://www.opengis.net/gml/3.2}AbstractFeatureType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element metadata ({http://www.opengis.net/waterml/2.0}metadata) inherited from {http://www.opengis.net/waterml/2.0}TimeseriesType
    
    # Element defaultPointMetadata ({http://www.opengis.net/waterml/2.0}defaultPointMetadata) inherited from {http://www.opengis.net/waterml/2.0}TimeseriesType
    
    # Element {http://www.opengis.net/waterml/2.0}point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'point'), 'point', '__httpwww_opengis_netwaterml2_0_MeasurementTimeseriesType_httpwww_opengis_netwaterml2_0point', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 169, 10), )

    
    point = property(__point.value, __point.set, None, None)

    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    _ElementMap.update({
        __point.name() : __point
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MeasurementTimeseriesType = MeasurementTimeseriesType
Namespace.addCategoryObject('typeBinding', 'MeasurementTimeseriesType', MeasurementTimeseriesType)


# Complex type {http://www.opengis.net/waterml/2.0}CategoricalTimeseriesType with content type ELEMENT_ONLY
class CategoricalTimeseriesType (TimeseriesType):
    """Complex type {http://www.opengis.net/waterml/2.0}CategoricalTimeseriesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CategoricalTimeseriesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 188, 2)
    _ElementMap = TimeseriesType._ElementMap.copy()
    _AttributeMap = TimeseriesType._AttributeMap.copy()
    # Base type is TimeseriesType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element location ({http://www.opengis.net/gml/3.2}location) inherited from {http://www.opengis.net/gml/3.2}AbstractFeatureType
    
    # Element boundedBy ({http://www.opengis.net/gml/3.2}boundedBy) inherited from {http://www.opengis.net/gml/3.2}AbstractFeatureType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element metadata ({http://www.opengis.net/waterml/2.0}metadata) inherited from {http://www.opengis.net/waterml/2.0}TimeseriesType
    
    # Element defaultPointMetadata ({http://www.opengis.net/waterml/2.0}defaultPointMetadata) inherited from {http://www.opengis.net/waterml/2.0}TimeseriesType
    
    # Element {http://www.opengis.net/waterml/2.0}point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'point'), 'point', '__httpwww_opengis_netwaterml2_0_CategoricalTimeseriesType_httpwww_opengis_netwaterml2_0point', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 192, 10), )

    
    point = property(__point.value, __point.set, None, None)

    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    _ElementMap.update({
        __point.name() : __point
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CategoricalTimeseriesType = CategoricalTimeseriesType
Namespace.addCategoryObject('typeBinding', 'CategoricalTimeseriesType', CategoricalTimeseriesType)


# Complex type {http://www.opengis.net/waterml/2.0}MeasurementTimeseriesMetadataType with content type ELEMENT_ONLY
class MeasurementTimeseriesMetadataType (TimeseriesMetadataType):
    """Complex type {http://www.opengis.net/waterml/2.0}MeasurementTimeseriesMetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasurementTimeseriesMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 256, 2)
    _ElementMap = TimeseriesMetadataType._ElementMap.copy()
    _AttributeMap = TimeseriesMetadataType._AttributeMap.copy()
    # Base type is TimeseriesMetadataType
    
    # Element temporalExtent ({http://www.opengis.net/waterml/2.0}temporalExtent) inherited from {http://www.opengis.net/waterml/2.0}TimeseriesMetadataType
    
    # Element baseTime ({http://www.opengis.net/waterml/2.0}baseTime) inherited from {http://www.opengis.net/waterml/2.0}TimeseriesMetadataType
    
    # Element spacing ({http://www.opengis.net/waterml/2.0}spacing) inherited from {http://www.opengis.net/waterml/2.0}TimeseriesMetadataType
    
    # Element commentBlock ({http://www.opengis.net/waterml/2.0}commentBlock) inherited from {http://www.opengis.net/waterml/2.0}TimeseriesMetadataType
    
    # Element parameter ({http://www.opengis.net/waterml/2.0}parameter) inherited from {http://www.opengis.net/waterml/2.0}TimeseriesMetadataType
    
    # Element {http://www.opengis.net/waterml/2.0}startAnchorPoint uses Python identifier startAnchorPoint
    __startAnchorPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startAnchorPoint'), 'startAnchorPoint', '__httpwww_opengis_netwaterml2_0_MeasurementTimeseriesMetadataType_httpwww_opengis_netwaterml2_0startAnchorPoint', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 260, 10), )

    
    startAnchorPoint = property(__startAnchorPoint.value, __startAnchorPoint.set, None, 'The anchor point for the beginning of the series.')

    
    # Element {http://www.opengis.net/waterml/2.0}endAnchorPoint uses Python identifier endAnchorPoint
    __endAnchorPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endAnchorPoint'), 'endAnchorPoint', '__httpwww_opengis_netwaterml2_0_MeasurementTimeseriesMetadataType_httpwww_opengis_netwaterml2_0endAnchorPoint', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 265, 10), )

    
    endAnchorPoint = property(__endAnchorPoint.value, __endAnchorPoint.set, None, 'The anchor point for the end of the series.')

    
    # Element {http://www.opengis.net/waterml/2.0}cumulative uses Python identifier cumulative
    __cumulative = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cumulative'), 'cumulative', '__httpwww_opengis_netwaterml2_0_MeasurementTimeseriesMetadataType_httpwww_opengis_netwaterml2_0cumulative', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 270, 10), )

    
    cumulative = property(__cumulative.value, __cumulative.set, None, 'Sets the time series to be a cumulative series.')

    
    # Element {http://www.opengis.net/waterml/2.0}accumulationAnchorTime uses Python identifier accumulationAnchorTime
    __accumulationAnchorTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'accumulationAnchorTime'), 'accumulationAnchorTime', '__httpwww_opengis_netwaterml2_0_MeasurementTimeseriesMetadataType_httpwww_opengis_netwaterml2_0accumulationAnchorTime', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 275, 10), )

    
    accumulationAnchorTime = property(__accumulationAnchorTime.value, __accumulationAnchorTime.set, None, 'Defines the time at which accumulation begins.')

    
    # Element {http://www.opengis.net/waterml/2.0}accumulationIntervalLength uses Python identifier accumulationIntervalLength
    __accumulationIntervalLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'accumulationIntervalLength'), 'accumulationIntervalLength', '__httpwww_opengis_netwaterml2_0_MeasurementTimeseriesMetadataType_httpwww_opengis_netwaterml2_0accumulationIntervalLength', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 281, 10), )

    
    accumulationIntervalLength = property(__accumulationIntervalLength.value, __accumulationIntervalLength.set, None, 'Defines the period over which accumulation occurs.')

    
    # Element {http://www.opengis.net/waterml/2.0}maxGapPeriod uses Python identifier maxGapPeriod
    __maxGapPeriod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maxGapPeriod'), 'maxGapPeriod', '__httpwww_opengis_netwaterml2_0_MeasurementTimeseriesMetadataType_httpwww_opengis_netwaterml2_0maxGapPeriod', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 286, 10), )

    
    maxGapPeriod = property(__maxGapPeriod.value, __maxGapPeriod.set, None, 'Indicates the maxiumum period allowed between two series before interpolation is not possible. \n              ')

    _ElementMap.update({
        __startAnchorPoint.name() : __startAnchorPoint,
        __endAnchorPoint.name() : __endAnchorPoint,
        __cumulative.name() : __cumulative,
        __accumulationAnchorTime.name() : __accumulationAnchorTime,
        __accumulationIntervalLength.name() : __accumulationIntervalLength,
        __maxGapPeriod.name() : __maxGapPeriod
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MeasurementTimeseriesMetadataType = MeasurementTimeseriesMetadataType
Namespace.addCategoryObject('typeBinding', 'MeasurementTimeseriesMetadataType', MeasurementTimeseriesMetadataType)


# Complex type {http://www.opengis.net/waterml/2.0}DefaultCategoricalTVPMetadataType with content type ELEMENT_ONLY
class DefaultCategoricalTVPMetadataType (TVPMetadataType):
    """Complex type {http://www.opengis.net/waterml/2.0}DefaultCategoricalTVPMetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DefaultCategoricalTVPMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 315, 2)
    _ElementMap = TVPMetadataType._ElementMap.copy()
    _AttributeMap = TVPMetadataType._AttributeMap.copy()
    # Base type is TVPMetadataType
    
    # Element quality ({http://www.opengis.net/waterml/2.0}quality) inherited from {http://www.opengis.net/waterml/2.0}TVPMetadataType
    
    # Element nilReason ({http://www.opengis.net/waterml/2.0}nilReason) inherited from {http://www.opengis.net/waterml/2.0}TVPMetadataType
    
    # Element comment ({http://www.opengis.net/waterml/2.0}comment) inherited from {http://www.opengis.net/waterml/2.0}TVPMetadataType
    
    # Element relatedObservation ({http://www.opengis.net/waterml/2.0}relatedObservation) inherited from {http://www.opengis.net/waterml/2.0}TVPMetadataType
    
    # Element qualifier ({http://www.opengis.net/waterml/2.0}qualifier) inherited from {http://www.opengis.net/waterml/2.0}TVPMetadataType
    
    # Element processing ({http://www.opengis.net/waterml/2.0}processing) inherited from {http://www.opengis.net/waterml/2.0}TVPMetadataType
    
    # Element source ({http://www.opengis.net/waterml/2.0}source) inherited from {http://www.opengis.net/waterml/2.0}TVPMetadataType
    
    # Element {http://www.opengis.net/waterml/2.0}codeSpace uses Python identifier codeSpace
    __codeSpace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'codeSpace'), 'codeSpace', '__httpwww_opengis_netwaterml2_0_DefaultCategoricalTVPMetadataType_httpwww_opengis_netwaterml2_0codeSpace', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 319, 10), )

    
    codeSpace = property(__codeSpace.value, __codeSpace.set, None, 'Defines the default codeSpace for the category timeseries')

    _ElementMap.update({
        __codeSpace.name() : __codeSpace
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DefaultCategoricalTVPMetadataType = DefaultCategoricalTVPMetadataType
Namespace.addCategoryObject('typeBinding', 'DefaultCategoricalTVPMetadataType', DefaultCategoricalTVPMetadataType)


# Complex type {http://www.opengis.net/waterml/2.0}MeasureTVPType with content type ELEMENT_ONLY
class MeasureTVPType (TimeValuePairType):
    """Complex type {http://www.opengis.net/waterml/2.0}MeasureTVPType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasureTVPType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 354, 2)
    _ElementMap = TimeValuePairType._ElementMap.copy()
    _AttributeMap = TimeValuePairType._AttributeMap.copy()
    # Base type is TimeValuePairType
    
    # Element time ({http://www.opengis.net/waterml/2.0}time) inherited from {http://www.opengis.net/waterml/2.0}TimeValuePairType
    
    # Element {http://www.opengis.net/waterml/2.0}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__httpwww_opengis_netwaterml2_0_MeasureTVPType_httpwww_opengis_netwaterml2_0value', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 358, 10), )

    
    value_ = property(__value.value, __value.set, None, 'The value of a measurement timeseries is a measure')

    
    # Element {http://www.opengis.net/waterml/2.0}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_opengis_netwaterml2_0_MeasureTVPType_httpwww_opengis_netwaterml2_0metadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 363, 10), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    _ElementMap.update({
        __value.name() : __value,
        __metadata.name() : __metadata
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MeasureTVPType = MeasureTVPType
Namespace.addCategoryObject('typeBinding', 'MeasureTVPType', MeasureTVPType)


# Complex type {http://www.opengis.net/waterml/2.0}CategoricalTVPType with content type ELEMENT_ONLY
class CategoricalTVPType (TimeValuePairType):
    """Complex type {http://www.opengis.net/waterml/2.0}CategoricalTVPType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CategoricalTVPType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 372, 2)
    _ElementMap = TimeValuePairType._ElementMap.copy()
    _AttributeMap = TimeValuePairType._AttributeMap.copy()
    # Base type is TimeValuePairType
    
    # Element time ({http://www.opengis.net/waterml/2.0}time) inherited from {http://www.opengis.net/waterml/2.0}TimeValuePairType
    
    # Element {http://www.opengis.net/waterml/2.0}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__httpwww_opengis_netwaterml2_0_CategoricalTVPType_httpwww_opengis_netwaterml2_0value', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 376, 10), )

    
    value_ = property(__value.value, __value.set, None, 'The value type is a category')

    
    # Element {http://www.opengis.net/waterml/2.0}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_opengis_netwaterml2_0_CategoricalTVPType_httpwww_opengis_netwaterml2_0metadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 382, 10), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    _ElementMap.update({
        __value.name() : __value,
        __metadata.name() : __metadata
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CategoricalTVPType = CategoricalTVPType
Namespace.addCategoryObject('typeBinding', 'CategoricalTVPType', CategoricalTVPType)


# Complex type {http://www.opengis.net/waterml/2.0}MonitoringPointType with content type ELEMENT_ONLY
class MonitoringPointType (pyxb.bundles.opengis._sams.SF_SpatialSamplingFeatureType):
    """Complex type {http://www.opengis.net/waterml/2.0}MonitoringPointType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MonitoringPointType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 31, 4)
    _ElementMap = pyxb.bundles.opengis._sams.SF_SpatialSamplingFeatureType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis._sams.SF_SpatialSamplingFeatureType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis._sams.SF_SpatialSamplingFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element location ({http://www.opengis.net/gml/3.2}location) inherited from {http://www.opengis.net/gml/3.2}AbstractFeatureType
    
    # Element boundedBy ({http://www.opengis.net/gml/3.2}boundedBy) inherited from {http://www.opengis.net/gml/3.2}AbstractFeatureType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element type ({http://www.opengis.net/sampling/2.0}type) inherited from {http://www.opengis.net/sampling/2.0}SF_SamplingFeatureType
    
    # Element sampledFeature ({http://www.opengis.net/sampling/2.0}sampledFeature) inherited from {http://www.opengis.net/sampling/2.0}SF_SamplingFeatureType
    
    # Element lineage ({http://www.opengis.net/sampling/2.0}lineage) inherited from {http://www.opengis.net/sampling/2.0}SF_SamplingFeatureType
    
    # Element relatedObservation ({http://www.opengis.net/sampling/2.0}relatedObservation) inherited from {http://www.opengis.net/sampling/2.0}SF_SamplingFeatureType
    
    # Element relatedSamplingFeature ({http://www.opengis.net/sampling/2.0}relatedSamplingFeature) inherited from {http://www.opengis.net/sampling/2.0}SF_SamplingFeatureType
    
    # Element parameter ({http://www.opengis.net/sampling/2.0}parameter) inherited from {http://www.opengis.net/sampling/2.0}SF_SamplingFeatureType
    
    # Element hostedProcedure ({http://www.opengis.net/samplingSpatial/2.0}hostedProcedure) inherited from {http://www.opengis.net/samplingSpatial/2.0}SF_SpatialSamplingFeatureType
    
    # Element positionalAccuracy ({http://www.opengis.net/samplingSpatial/2.0}positionalAccuracy) inherited from {http://www.opengis.net/samplingSpatial/2.0}SF_SpatialSamplingFeatureType
    
    # Element shape ({http://www.opengis.net/samplingSpatial/2.0}shape) inherited from {http://www.opengis.net/samplingSpatial/2.0}SF_SpatialSamplingFeatureType
    
    # Element {http://www.opengis.net/waterml/2.0}relatedParty uses Python identifier relatedParty
    __relatedParty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relatedParty'), 'relatedParty', '__httpwww_opengis_netwaterml2_0_MonitoringPointType_httpwww_opengis_netwaterml2_0relatedParty', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 36, 20), )

    
    relatedParty = property(__relatedParty.value, __relatedParty.set, None, 'Describes parties - individuals or organisations - that are related to the monitoring point. Multiple related parties may be described using the role code list (from ISO 19115). The most common relationships are likely to be: owner, originator, pointOfContact, principalInvestigator and distributor.')

    
    # Element {http://www.opengis.net/waterml/2.0}monitoringType uses Python identifier monitoringType
    __monitoringType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'monitoringType'), 'monitoringType', '__httpwww_opengis_netwaterml2_0_MonitoringPointType_httpwww_opengis_netwaterml2_0monitoringType', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 43, 20), )

    
    monitoringType = property(__monitoringType.value, __monitoringType.set, None, 'A characterisation of the type of station. E.g. meteorological, surface water, groundwater, water quality etc.')

    
    # Element {http://www.opengis.net/waterml/2.0}descriptionReference uses Python identifier descriptionReference_
    __descriptionReference_ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'descriptionReference'), 'descriptionReference_', '__httpwww_opengis_netwaterml2_0_MonitoringPointType_httpwww_opengis_netwaterml2_0descriptionReference', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 50, 20), )

    
    descriptionReference_ = property(__descriptionReference_.value, __descriptionReference_.set, None, 'Provide extra description about a monitoring point. This could be a link to an HTML page describing the location, photos of a monitoring point, history records etc.')

    
    # Element {http://www.opengis.net/waterml/2.0}verticalDatum uses Python identifier verticalDatum
    __verticalDatum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'verticalDatum'), 'verticalDatum', '__httpwww_opengis_netwaterml2_0_MonitoringPointType_httpwww_opengis_netwaterml2_0verticalDatum', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 57, 20), )

    
    verticalDatum = property(__verticalDatum.value, __verticalDatum.set, None, 'Specifies the elevation that is used as the zero point, or datum, for vertical measurements (e.g stage/level).  \n                          The gml:VerticalDatumPropertyType type allows specification of the local gauge zero as a height above a reference datum. E.g. local gauge zero is 23m above the AHD using the anchorDefinition. \n                        ')

    
    # Element {http://www.opengis.net/waterml/2.0}timeZone uses Python identifier timeZone
    __timeZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timeZone'), 'timeZone', '__httpwww_opengis_netwaterml2_0_MonitoringPointType_httpwww_opengis_netwaterml2_0timeZone', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 66, 20), )

    
    timeZone = property(__timeZone.value, __timeZone.set, None, 'Specifies the time zone that the sampling point is located in. The zone offset must be specified (e.g. +10:00 GMT), with an optional zone abbreviation (e.g. AEST)')

    
    # Element {http://www.opengis.net/waterml/2.0}daylightSavingTimeZone uses Python identifier daylightSavingTimeZone
    __daylightSavingTimeZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'daylightSavingTimeZone'), 'daylightSavingTimeZone', '__httpwww_opengis_netwaterml2_0_MonitoringPointType_httpwww_opengis_netwaterml2_0daylightSavingTimeZone', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 73, 20), )

    
    daylightSavingTimeZone = property(__daylightSavingTimeZone.value, __daylightSavingTimeZone.set, None, None)

    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    _ElementMap.update({
        __relatedParty.name() : __relatedParty,
        __monitoringType.name() : __monitoringType,
        __descriptionReference_.name() : __descriptionReference_,
        __verticalDatum.name() : __verticalDatum,
        __timeZone.name() : __timeZone,
        __daylightSavingTimeZone.name() : __daylightSavingTimeZone
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MonitoringPointType = MonitoringPointType
Namespace.addCategoryObject('typeBinding', 'MonitoringPointType', MonitoringPointType)


Collection = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Collection'), CollectionType, documentation='OGC WaterML2.0 defines a generic collection feature type to\n                allow the grouping of observations and/or sampling features with metadata to\n                describe the nature of the collection. Such collections are required in a number of\n                data exchange scenarios; whether the underlying transport technology is web\n                services, FTP or other technologies.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 27, 1))
Namespace.addCategoryObject('elementBinding', Collection.name().localName(), Collection)

DocumentMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DocumentMetadata'), DocumentMetadataType, documentation='Metadata about the document', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 122, 1))
Namespace.addCategoryObject('elementBinding', DocumentMetadata.name().localName(), DocumentMetadata)

TimeZone = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeZone'), TimeZoneType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 88, 4))
Namespace.addCategoryObject('elementBinding', TimeZone.name().localName(), TimeZone)

ObservationProcess = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObservationProcess'), ObservationProcessType, documentation='A large number of direct in-situ hydrological observations are performed by a sensor or sensor system. Common types of sensors\n        include rain gauges, level gauges, quality sensors such as temperature, turbidity etc. Manual procedures may be also used to make measurements\n        at a particular sampling point. These may be ad-hoc visits to particular point that may be of interest, or continued visits to a well\n        identified sampling point. Procedures that generate derived or synthetic results also exist, such as those produced by algorithms or\n        simulations. Algorithms are commonly implemented in hydrological software to process data sets for reporting or other purposes. Examples\n        include: - Temporal interpolation or aggregation; - Spatial interpolation; - Quality assurance related tasks such as automatic spike removal\n        or gap filling; - Derivation of new observed phenomena such as calculation of volume from stage, discharge (flow) from stage\n        etc.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 18, 2))
Namespace.addCategoryObject('elementBinding', ObservationProcess.name().localName(), ObservationProcess)

TVPMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TVPMetadata'), TVPMetadataType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 29, 2))
Namespace.addCategoryObject('elementBinding', TVPMetadata.name().localName(), TVPMetadata)

Timeseries = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Timeseries'), TimeseriesType, documentation='Describes a time series as a collection of time-value pairs (implements TimeseriesTVP model type). A time series is a also a realisation of a discrete time coverage as\n        defined by ISO19123 - Coverages.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 135, 2))
Namespace.addCategoryObject('elementBinding', Timeseries.name().localName(), Timeseries)

TimeseriesMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeseriesMetadata'), TimeseriesMetadataType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 213, 2))
Namespace.addCategoryObject('elementBinding', TimeseriesMetadata.name().localName(), TimeseriesMetadata)

DefaultTVPMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DefaultTVPMetadata'), TVPMetadataType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 309, 2))
Namespace.addCategoryObject('elementBinding', DefaultTVPMetadata.name().localName(), DefaultTVPMetadata)

TimeValuePair = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeValuePair'), TimeValuePairType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 342, 2))
Namespace.addCategoryObject('elementBinding', TimeValuePair.name().localName(), TimeValuePair)

CommentBlock = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CommentBlock'), CommentBlockType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 389, 2))
Namespace.addCategoryObject('elementBinding', CommentBlock.name().localName(), CommentBlock)

value = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), MeasureType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 414, 2))
Namespace.addCategoryObject('elementBinding', value.name().localName(), value)

ObservationMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObservationMetadata'), ObservationMetadataType, documentation='Metadata relating to water observation. Specialisation of the ISO19115 MD_Metadata type. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 20, 2))
Namespace.addCategoryObject('elementBinding', ObservationMetadata.name().localName(), ObservationMetadata)

TVPMeasurementMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TVPMeasurementMetadata'), TVPMeasurementMetadataType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 74, 2))
Namespace.addCategoryObject('elementBinding', TVPMeasurementMetadata.name().localName(), TVPMeasurementMetadata)

MeasurementTimeseries = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeasurementTimeseries'), MeasurementTimeseriesType, documentation='Describes a time series as a collection of time-value pairs where the value-type is a measurement\n        and associated metadata is specific to measurement types. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 158, 2))
Namespace.addCategoryObject('elementBinding', MeasurementTimeseries.name().localName(), MeasurementTimeseries)

CategoricalTimeseries = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CategoricalTimeseries'), CategoricalTimeseriesType, documentation='Describes a time series as a collection of time-value pairs where the value-type is a category\n        and associated metadata is specific to categorical types. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 181, 2))
Namespace.addCategoryObject('elementBinding', CategoricalTimeseries.name().localName(), CategoricalTimeseries)

MeasurementTimeseriesMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeasurementTimeseriesMetadata'), MeasurementTimeseriesMetadataType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 254, 2))
Namespace.addCategoryObject('elementBinding', MeasurementTimeseriesMetadata.name().localName(), MeasurementTimeseriesMetadata)

DefaultTVPMeasurementMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DefaultTVPMeasurementMetadata'), TVPMeasurementMetadataType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 310, 2))
Namespace.addCategoryObject('elementBinding', DefaultTVPMeasurementMetadata.name().localName(), DefaultTVPMeasurementMetadata)

DefaultTVPCategoricalMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DefaultTVPCategoricalMetadata'), DefaultCategoricalTVPMetadataType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 312, 2))
Namespace.addCategoryObject('elementBinding', DefaultTVPCategoricalMetadata.name().localName(), DefaultTVPCategoricalMetadata)

MeasurementTVP = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeasurementTVP'), MeasureTVPType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 353, 2))
Namespace.addCategoryObject('elementBinding', MeasurementTVP.name().localName(), MeasurementTVP)

CategoricalTVP = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CategoricalTVP'), CategoricalTVPType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 370, 2))
Namespace.addCategoryObject('elementBinding', CategoricalTVP.name().localName(), CategoricalTVP)

MonitoringPoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MonitoringPoint'), MonitoringPointType, documentation='A (point) location where water flow or properties are reported, such as a stream gauge, rainfall gauge, or water quality monitoring site.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 25, 4))
Namespace.addCategoryObject('elementBinding', MonitoringPoint.name().localName(), MonitoringPoint)



CollectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), DocumentMetadataPropertyType, scope=CollectionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 40, 5)))

CollectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'temporalExtent'), CTD_ANON, scope=CollectionType, documentation='Describes the temporal extent of the all the time series\n\t\t\t\t\t\t\t  contained within the collection (if they exist).', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 41, 5)))

CollectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sourceDefinition'), CTD_ANON_, scope=CollectionType, documentation='Provides a context for identification of particular data elements through use of MD_DataIdentification. \n\t\t\t\t      These can be referenced from individual timeseries values. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 53, 6)))

CollectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameter'), pyxb.bundles.opengis.om_2_0.NamedValuePropertyType, scope=CollectionType, documentation='A soft-typed parameter for extra metadata properties.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 65, 6)))

CollectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'localDictionary'), CTD_ANON_2, scope=CollectionType, documentation='Contains inline defintions of observed phenomenon.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 71, 5)))

CollectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'samplingFeatureMember'), SamplingFeatureMemberPropertyType, scope=CollectionType, documentation='Contains sampling feature member items. This allows\n                                features of interest to be encoded at the header of a document and\n                                referenced later or collections of features to be encoded.\n                            ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 82, 5)))

CollectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'observationMember'), pyxb.bundles.opengis.om_2_0.OM_ObservationPropertyType, scope=CollectionType, documentation='Contains members of Timeseries Observations. The type\n                                shown here is only OM_Observation as the restrictions of this occur\n                                using schematron. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 90, 5)))

CollectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'communityExtension'), pyxb.binding.datatypes.anyType, scope=CollectionType, documentation='Use this extention point for community-agreed extensions to the schema.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 97, 5)))

CollectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'internalExtension'), pyxb.binding.datatypes.anyType, scope=CollectionType, documentation='Use this extention point for internal extensions that have not been defined for external use.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 102, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 26, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 27, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 41, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 53, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 65, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 71, 5))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 82, 5))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 90, 5))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 97, 5))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 102, 6))
    counters.add(cc_14)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 26, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 27, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CollectionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 40, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CollectionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'temporalExtent')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 41, 5))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CollectionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sourceDefinition')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 53, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CollectionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 65, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CollectionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'localDictionary')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 71, 5))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CollectionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'samplingFeatureMember')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 82, 5))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CollectionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'observationMember')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 90, 5))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CollectionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'communityExtension')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 97, 5))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CollectionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'internalExtension')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 102, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
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
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CollectionType._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'TimePeriod'), pyxb.bundles.opengis.gml_3_2.TimePeriodType, scope=CTD_ANON, documentation='gml:TimePeriod acts as a one-dimensional geometric primitive that represents an identifiable extent in time.\nThe location in of a gml:TimePeriod is described by the temporal positions of the instants at which it begins and ends. The length of the period is equal to the temporal distance between the two bounding temporal positions. \nBoth beginning and end may be described in terms of their direct position using gml:TimePositionType which is an XML Schema simple content type, or by reference to an indentifiable time instant using gml:TimeInstantPropertyType.\nAlternatively a limit of a gml:TimePeriod may use the conventional GML property model to make a reference to a time instant described elsewhere, or a limit may be indicated as a direct position.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/temporal.xsd', 133, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'TimePeriod')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 48, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gmd, 'MD_DataIdentification'), pyxb.bundles.opengis.iso19139.v20070417.gmd.MD_DataIdentification_Type, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/identification.xsd', 93, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'MD_DataIdentification')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 60, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'Dictionary'), pyxb.bundles.opengis.gml_3_2.DictionaryType, scope=CTD_ANON_2, documentation='Sets of definitions may be collected into dictionaries or collections.\nA gml:Dictionary is a non-abstract collection of definitions.\nThe gml:Dictionary content model adds a list of gml:dictionaryEntry properties that contain or reference gml:Definition objects.  A database handle (gml:id attribute) is required, in order that this collection may be referred to. The standard gml:identifier, gml:description, gml:descriptionReference and gml:name properties are available to reference or contain more information about this dictionary. The gml:description and gml:descriptionReference property elements may be used for a description of this dictionary. The derived gml:name element may be used for the name(s) of this dictionary. for remote definiton references gml:dictionaryEntry shall be used. If a Definition object contained within a Dictionary uses the descriptionReference property to refer to a remote definition, then this enables the inclusion of a remote definition in a local dictionary, giving a handle and identifier in the context of the local dictionary.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/dictionary.xsd', 55, 1)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'Dictionary')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 77, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_3()




CollectionPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Collection'), CollectionType, scope=CollectionPropertyType, documentation='OGC WaterML2.0 defines a generic collection feature type to\n                allow the grouping of observations and/or sampling features with metadata to\n                describe the nature of the collection. Such collections are required in a number of\n                data exchange scenarios; whether the underlying transport technology is web\n                services, FTP or other technologies.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 27, 1)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 112, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CollectionPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Collection')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 113, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CollectionPropertyType._Automaton = _BuildAutomaton_4()




DocumentMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'generationDate'), pyxb.binding.datatypes.dateTime, scope=DocumentMetadataType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 135, 5)))

DocumentMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'version'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=DocumentMetadataType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 136, 5)))

DocumentMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'generationSystem'), pyxb.binding.datatypes.string, scope=DocumentMetadataType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 137, 5)))

DocumentMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'profile'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=DocumentMetadataType, documentation='Used to specify the conformance classes that are in use within the collection document. The conformance classes are identified by the URL', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 138, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 136, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 137, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 138, 6))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DocumentMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DocumentMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DocumentMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DocumentMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DocumentMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DocumentMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'generationDate')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 135, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(DocumentMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'version')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 136, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(DocumentMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'generationSystem')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 137, 5))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(DocumentMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'profile')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 138, 6))
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
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DocumentMetadataType._Automaton = _BuildAutomaton_5()




DocumentMetadataPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DocumentMetadata'), DocumentMetadataType, scope=DocumentMetadataPropertyType, documentation='Metadata about the document', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 122, 1)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 148, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DocumentMetadataPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DocumentMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 149, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DocumentMetadataPropertyType._Automaton = _BuildAutomaton_6()




MonitoringPointPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MonitoringPoint'), MonitoringPointType, scope=MonitoringPointPropertyType, documentation='A (point) location where water flow or properties are reported, such as a stream gauge, rainfall gauge, or water quality monitoring site.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 25, 4)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 81, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MonitoringPointPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MonitoringPoint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 82, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MonitoringPointPropertyType._Automaton = _BuildAutomaton_7()




TimeZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'zoneOffset'), pyxb.binding.datatypes.string, scope=TimeZoneType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 91, 12)))

TimeZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'zoneAbbreviation'), pyxb.binding.datatypes.string, scope=TimeZoneType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 92, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 92, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TimeZoneType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'zoneOffset')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 91, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TimeZoneType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'zoneAbbreviation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 92, 12))
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
TimeZoneType._Automaton = _BuildAutomaton_8()




TimeZonePropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeZone'), TimeZoneType, scope=TimeZonePropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 88, 4)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TimeZonePropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimeZone')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 98, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TimeZonePropertyType._Automaton = _BuildAutomaton_9()




ObservationProcessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'processType'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=ObservationProcessType, documentation='A defintion of the type of process used in the observation. This may be a Sensor, ManualMethod, Algorithm or Simulation\n                (including models).', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 34, 10)))

ObservationProcessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'originatingProcess'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=ObservationProcessType, documentation='A reference to the original source of the data. For example, if this is a post-processed time series (and processType is\n                algorithm), this link would specify the original process that generated the data, e.g. the sensor. This allows the origin of the data\n                to be maintained regardless of the processing that has occured to it.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 40, 10)))

ObservationProcessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aggregationDuration'), pyxb.binding.datatypes.duration, scope=ObservationProcessType, documentation='If the process involves temporal aggregation of a result set, the time duration over which data has been aggregated should be expressed here. E.g. hourly, daily aggregates.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 47, 10)))

ObservationProcessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'verticalDatum'), pyxb.bundles.opengis.gml_3_2.VerticalDatumPropertyType, scope=ObservationProcessType, documentation='Specifies the datum that is used as the zero point for level measurements. This can be process-specific as opposed to the\n                gauge at the actual monitoring point.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 52, 10)))

ObservationProcessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comment'), pyxb.binding.datatypes.string, scope=ObservationProcessType, documentation='Comments specific to the process from the operator or system performing the process.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 58, 10)))

ObservationProcessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'processReference'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=ObservationProcessType, documentation='Reference to an external process definition.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 63, 10)))

ObservationProcessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'input'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=ObservationProcessType, documentation='A list of the inputs used in the process. This may be a list of references to the data sets used (e.g. model input\n                series) or an input array to an algorithm.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 68, 10)))

ObservationProcessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameter'), pyxb.bundles.opengis.om_2_0.NamedValuePropertyType, scope=ObservationProcessType, documentation='A soft-typed parameter to allow arbitrary properties to be added to the description. This property uses the name-value type from ISO19156.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 74, 10)))

ObservationProcessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'operator'), pyxb.bundles.opengis.iso19139.v20070417.gmd.CI_ResponsibleParty_PropertyType, scope=ObservationProcessType, documentation='Describes the party responsible for performing the process. E.g. the person performing the method or operating the sensor.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 79, 10)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 26, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 27, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 40, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 47, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 52, 10))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 58, 10))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 63, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 68, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 74, 10))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 79, 10))
    counters.add(cc_14)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationProcessType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationProcessType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationProcessType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationProcessType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationProcessType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationProcessType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 26, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationProcessType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 27, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ObservationProcessType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'processType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 34, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(ObservationProcessType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originatingProcess')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 40, 10))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(ObservationProcessType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aggregationDuration')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 47, 10))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(ObservationProcessType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'verticalDatum')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 52, 10))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(ObservationProcessType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comment')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 58, 10))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(ObservationProcessType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'processReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 63, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(ObservationProcessType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'input')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 68, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(ObservationProcessType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 74, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(ObservationProcessType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'operator')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 79, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
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
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ObservationProcessType._Automaton = _BuildAutomaton_10()




ObservationProcessPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObservationProcess'), ObservationProcessType, scope=ObservationProcessPropertyType, documentation='A large number of direct in-situ hydrological observations are performed by a sensor or sensor system. Common types of sensors\n        include rain gauges, level gauges, quality sensors such as temperature, turbidity etc. Manual procedures may be also used to make measurements\n        at a particular sampling point. These may be ad-hoc visits to particular point that may be of interest, or continued visits to a well\n        identified sampling point. Procedures that generate derived or synthetic results also exist, such as those produced by algorithms or\n        simulations. Algorithms are commonly implemented in hydrological software to process data sets for reporting or other purposes. Examples\n        include: - Temporal interpolation or aggregation; - Spatial interpolation; - Quality assurance related tasks such as automatic spike removal\n        or gap filling; - Derivation of new observed phenomena such as calculation of volume from stage, discharge (flow) from stage\n        etc.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 18, 2)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 89, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ObservationProcessPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ObservationProcess')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/observationProcess.xsd', 90, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ObservationProcessPropertyType._Automaton = _BuildAutomaton_11()




TVPMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'quality'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=TVPMetadataType, documentation='Defines the quality of the point (or the default if it is the defaultTimeValuePair) using an OGC WaterML2.0 quality code. The\n            qualifier element should be used for other assertions (e.g. using internal codes). ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 32, 6)))

TVPMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nilReason'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=TVPMetadataType, documentation="Specifies the reason for a null point (xsi:nil='true'). Must be present if the value is null. ", location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 38, 6)))

TVPMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comment'), pyxb.binding.datatypes.string, scope=TVPMetadataType, documentation='Free text comment associated with the data point.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 43, 6)))

TVPMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relatedObservation'), pyxb.bundles.opengis.om_2_0.ObservationContextPropertyType, scope=TVPMetadataType, documentation='Defines a reference to an observation that is related to this point. E.g. derived from a sample.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 48, 6)))

TVPMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'qualifier'), pyxb.bundles.opengis.swe_2_0.QualityPropertyType, scope=TVPMetadataType, documentation='A general qualifier for the point to define influencing conditions, or other qualifying information. A broader, more\n            flexible location for qualifiers.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 54, 6)))

TVPMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'processing'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=TVPMetadataType, documentation='Defines what processing has occured on the data point using a reference to a code item.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 60, 6)))

TVPMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'source'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=TVPMetadataType, documentation='Defines the source of the value using a reference to an appropriate resource. This is used where the timeseries may be aggregated from multiple sources.his can be an internal link to om:OM_Observation/om:metadata/wml2:ObservationMetadata/gmd:identificationInfo/gmd:MD_DataIdentification', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 65, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 32, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 38, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 43, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 48, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 54, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 60, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 65, 6))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TVPMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'quality')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 32, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TVPMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nilReason')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 38, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TVPMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comment')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 43, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TVPMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relatedObservation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 48, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TVPMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'qualifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 54, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TVPMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'processing')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 60, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TVPMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 65, 6))
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
TVPMetadataType._Automaton = _BuildAutomaton_12()




TVPMetadataPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TVPMetadata'), TVPMetadataType, scope=TVPMetadataPropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 29, 2)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TVPMetadataPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TVPMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 113, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TVPMetadataPropertyType._Automaton = _BuildAutomaton_13()




TVPMeasurementMetadataPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TVPMeasurementMetadata'), TVPMeasurementMetadataType, scope=TVPMeasurementMetadataPropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 74, 2)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TVPMeasurementMetadataPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TVPMeasurementMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 120, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TVPMeasurementMetadataPropertyType._Automaton = _BuildAutomaton_14()




TVPDefaultMetadataPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DefaultTVPMetadata'), TVPMetadataType, scope=TVPDefaultMetadataPropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 309, 2)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TVPDefaultMetadataPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DefaultTVPMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 127, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TVPDefaultMetadataPropertyType._Automaton = _BuildAutomaton_15()




TimeseriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), TimeseriesMetadataPropertyType, scope=TimeseriesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 145, 10)))

TimeseriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'defaultPointMetadata'), TVPDefaultMetadataPropertyType, scope=TimeseriesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 147, 10)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 26, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 27, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 145, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 147, 10))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 26, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 27, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(TimeseriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 145, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(TimeseriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'defaultPointMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 147, 10))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TimeseriesType._Automaton = _BuildAutomaton_16()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeasurementTVP'), MeasureTVPType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 353, 2)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MeasurementTVP')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 172, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_17()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CategoricalTVP'), CategoricalTVPType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 370, 2)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CategoricalTVP')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 195, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_18()




TimeseriesPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Timeseries'), TimeseriesType, scope=TimeseriesPropertyType, documentation='Describes a time series as a collection of time-value pairs (implements TimeseriesTVP model type). A time series is a also a realisation of a discrete time coverage as\n        defined by ISO19123 - Coverages.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 135, 2)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 205, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TimeseriesPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Timeseries')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 206, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TimeseriesPropertyType._Automaton = _BuildAutomaton_19()




TimeseriesMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'temporalExtent'), pyxb.bundles.opengis.gml_3_2.TimePeriodPropertyType, scope=TimeseriesMetadataType, documentation='Defines the start and end times of the represented time series.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 216, 6)))

TimeseriesMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'baseTime'), pyxb.bundles.opengis.gml_3_2.TimePositionType, scope=TimeseriesMetadataType, documentation='Defines the start time for isochronous (equidistant) time series. Each point occurs at regular steps (defined by the spacing\n            property). If baseTime is specified you must supply a spacing element. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 221, 6)))

TimeseriesMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'spacing'), pyxb.binding.datatypes.duration, scope=TimeseriesMetadataType, documentation='The spacing between points for isochronous or equidistant (equally space) points. This is used with the baseTime element to allow calculation of time instants.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 227, 6)))

TimeseriesMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'commentBlock'), CommentBlockPropertyType, scope=TimeseriesMetadataType, documentation='A comment that applies over a period of time for the time series.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 232, 6)))

TimeseriesMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameter'), pyxb.bundles.opengis.om_2_0.NamedValuePropertyType, scope=TimeseriesMetadataType, documentation='A named-value extension point, allowing extra metadata to be associated with a timeseries. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 238, 6)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 221, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 227, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 232, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 238, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TimeseriesMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'temporalExtent')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 216, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TimeseriesMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'baseTime')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 221, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TimeseriesMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'spacing')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 227, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TimeseriesMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'commentBlock')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 232, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TimeseriesMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 238, 6))
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
TimeseriesMetadataType._Automaton = _BuildAutomaton_20()




TimeseriesMetadataPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeseriesMetadata'), TimeseriesMetadataType, scope=TimeseriesMetadataPropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 213, 2)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TimeseriesMetadataPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimeseriesMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 248, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TimeseriesMetadataPropertyType._Automaton = _BuildAutomaton_21()




MeasurementTSMetadataPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeasurementTimeseriesMetadata'), MeasurementTimeseriesMetadataType, scope=MeasurementTSMetadataPropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 254, 2)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MeasurementTSMetadataPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MeasurementTimeseriesMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 299, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MeasurementTSMetadataPropertyType._Automaton = _BuildAutomaton_22()




DefaultTVPMetadataPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DefaultTVPMetadata'), TVPMetadataType, scope=DefaultTVPMetadataPropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 309, 2)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 330, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DefaultTVPMetadataPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DefaultTVPMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 331, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DefaultTVPMetadataPropertyType._Automaton = _BuildAutomaton_23()




TimeValuePairType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'time'), pyxb.bundles.opengis.gml_3_2.TimePositionType, scope=TimeValuePairType, documentation='The time instant for the data point.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 345, 6)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 345, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TimeValuePairType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'time')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 345, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TimeValuePairType._Automaton = _BuildAutomaton_24()




CommentBlockType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'applicablePeriod'), pyxb.bundles.opengis.gml_3_2.TimePeriodPropertyType, scope=CommentBlockType, documentation='The period over which the comment applies.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 392, 6)))

CommentBlockType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comment'), pyxb.binding.datatypes.string, scope=CommentBlockType, documentation='The comment that applies for the period.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 397, 6)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommentBlockType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'applicablePeriod')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 392, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CommentBlockType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comment')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 397, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CommentBlockType._Automaton = _BuildAutomaton_25()




CommentBlockPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CommentBlock'), CommentBlockType, scope=CommentBlockPropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 389, 2)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CommentBlockPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CommentBlock')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 406, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CommentBlockPropertyType._Automaton = _BuildAutomaton_26()




ObservationMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'intendedObservationSpacing'), pyxb.binding.datatypes.duration, scope=ObservationMetadataType, documentation='Defines the expected interval in which observations can be expected. e.g. daily.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 29, 10)))

ObservationMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'status'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=ObservationMetadataType, documentation='Indicates the statues of the observation. E.g. unreleased, verified etc.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 34, 10)))

ObservationMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sampledMedium'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=ObservationMetadataType, documentation='Indicates the medium that was sampled. E.g. water, air, etc.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 39, 10)))

ObservationMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maximumGap'), pyxb.binding.datatypes.duration, scope=ObservationMetadataType, documentation='\n                Defines the allowed gap between series when joining this time series with another. \n              ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 44, 10)))

ObservationMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameter'), pyxb.bundles.opengis.om_2_0.NamedValuePropertyType, scope=ObservationMetadataType, documentation='A soft-typed parameter to allow extension through name-value pairs.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 51, 10)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 28, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 29, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 30, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 31, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 32, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 33, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 36, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 37, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 38, 5))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 39, 5))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 40, 5))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 41, 5))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 42, 5))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 44, 5))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 45, 5))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 46, 5))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 47, 5))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 48, 5))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 49, 5))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 50, 5))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 51, 5))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 52, 5))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 53, 5))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 54, 5))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 55, 5))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 29, 10))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 34, 10))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 39, 10))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 44, 10))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 51, 10))
    counters.add(cc_29)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'fileIdentifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 28, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'language')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 29, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'characterSet')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 30, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'parentIdentifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 31, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'hierarchyLevel')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 32, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'hierarchyLevelName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 33, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'contact')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 34, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'dateStamp')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 35, 5))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'metadataStandardName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 36, 5))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'metadataStandardVersion')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 37, 5))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'dataSetURI')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 38, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'locale')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 39, 5))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'spatialRepresentationInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 40, 5))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'referenceSystemInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 41, 5))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'metadataExtensionInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 42, 5))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'identificationInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 43, 5))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'contentInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 44, 5))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'distributionInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 45, 5))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'dataQualityInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 46, 5))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'portrayalCatalogueInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 47, 5))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'metadataConstraints')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 48, 5))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'applicationSchemaInfo')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 49, 5))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'metadataMaintenance')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 50, 5))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'series')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 51, 5))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'describes')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 52, 5))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'propertyType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 53, 5))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'featureType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 54, 5))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmd, 'featureAttribute')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/iso/19139/20070417/gmd/metadataEntity.xsd', 55, 5))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'intendedObservationSpacing')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 29, 10))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 34, 10))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sampledMedium')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 39, 10))
    st_30 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maximumGap')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 44, 10))
    st_31 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_29, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 51, 10))
    st_32 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
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
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_29, True) ]))
    st_32._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ObservationMetadataType._Automaton = _BuildAutomaton_27()




ObservationMetadataPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObservationMetadata'), ObservationMetadataType, scope=ObservationMetadataPropertyType, documentation='Metadata relating to water observation. Specialisation of the ISO19115 MD_Metadata type. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 20, 2)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 62, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ObservationMetadataPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ObservationMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseriesObservationMetadata.xsd', 63, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ObservationMetadataPropertyType._Automaton = _BuildAutomaton_28()




SamplingFeatureMemberPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_sam, 'SF_SamplingFeatureCollection'), pyxb.bundles.opengis._sam.SF_SamplingFeatureCollectionType, scope=SamplingFeatureMemberPropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sampling/2.0/samplingFeature.xsd', 216, 1)))

SamplingFeatureMemberPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_sams, 'SF_SpatialSamplingFeature'), pyxb.bundles.opengis._sams.SF_SpatialSamplingFeatureType, scope=SamplingFeatureMemberPropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/samplingSpatial/2.0/spatialSamplingFeature.xsd', 140, 1)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 169, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SamplingFeatureMemberPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_sams, 'SF_SpatialSamplingFeature')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 164, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SamplingFeatureMemberPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_sam, 'SF_SamplingFeatureCollection')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/collection.xsd', 165, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SamplingFeatureMemberPropertyType._Automaton = _BuildAutomaton_29()




TVPMeasurementMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uom'), pyxb.bundles.opengis.swe_2_0.UnitReference, scope=TVPMeasurementMetadataType, documentation='Defines the default unit of measure across the series. The uom code is specified using the UCUM code. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 80, 10)))

TVPMeasurementMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'interpolationType'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=TVPMeasurementMetadataType, documentation='The interpolation type of the time series point. This describes the nature of the value to the time with which it is\n                associated. E.g. average in the preceeding interval. The URL codes are available at http://www.opengis.net/def/waterml/2.0/interpolationType/', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 85, 10)))

TVPMeasurementMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'censoredReason'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=TVPMeasurementMetadataType, documentation='Specifies the reason the value has been censored. e.g. left/right censoring, ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 91, 10)))

TVPMeasurementMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accuracy'), pyxb.bundles.opengis.swe_2_0.QuantityPropertyType, scope=TVPMeasurementMetadataType, documentation='Used to specify the accuracy of a single value. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 96, 10)))

TVPMeasurementMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aggregationDuration'), pyxb.binding.datatypes.duration, scope=TVPMeasurementMetadataType, documentation='Describes the temporal aggregation that has occured to the value. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 101, 10)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 32, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 38, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 43, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 48, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 54, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 60, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 65, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 80, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 85, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 91, 10))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 96, 10))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 101, 10))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TVPMeasurementMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'quality')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 32, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TVPMeasurementMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nilReason')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 38, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TVPMeasurementMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comment')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 43, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TVPMeasurementMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relatedObservation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 48, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TVPMeasurementMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'qualifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 54, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TVPMeasurementMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'processing')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 60, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TVPMeasurementMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 65, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(TVPMeasurementMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uom')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 80, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(TVPMeasurementMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'interpolationType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 85, 10))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(TVPMeasurementMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'censoredReason')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 91, 10))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(TVPMeasurementMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accuracy')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 96, 10))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(TVPMeasurementMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aggregationDuration')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 101, 10))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
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
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TVPMeasurementMetadataType._Automaton = _BuildAutomaton_30()




MeasurementTimeseriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'point'), CTD_ANON_3, scope=MeasurementTimeseriesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 169, 10)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 26, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 27, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 145, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 147, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 169, 10))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 26, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 27, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 145, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'defaultPointMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 147, 10))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'point')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 169, 10))
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
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MeasurementTimeseriesType._Automaton = _BuildAutomaton_31()




CategoricalTimeseriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'point'), CTD_ANON_4, scope=CategoricalTimeseriesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 192, 10)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 26, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 27, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 145, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 147, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 191, 8))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 192, 10))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CategoricalTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CategoricalTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CategoricalTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CategoricalTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CategoricalTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CategoricalTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 26, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CategoricalTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 27, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CategoricalTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 145, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CategoricalTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'defaultPointMetadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 147, 10))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CategoricalTimeseriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'point')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 192, 10))
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
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CategoricalTimeseriesType._Automaton = _BuildAutomaton_32()




MeasurementTimeseriesMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startAnchorPoint'), pyxb.bundles.opengis.gml_3_2.TimePositionType, scope=MeasurementTimeseriesMetadataType, documentation='The anchor point for the beginning of the series.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 260, 10)))

MeasurementTimeseriesMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endAnchorPoint'), pyxb.bundles.opengis.gml_3_2.TimePositionType, scope=MeasurementTimeseriesMetadataType, documentation='The anchor point for the end of the series.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 265, 10)))

MeasurementTimeseriesMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cumulative'), pyxb.binding.datatypes.boolean, scope=MeasurementTimeseriesMetadataType, documentation='Sets the time series to be a cumulative series.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 270, 10)))

MeasurementTimeseriesMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accumulationAnchorTime'), pyxb.bundles.opengis.gml_3_2.TimePositionType, scope=MeasurementTimeseriesMetadataType, documentation='Defines the time at which accumulation begins.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 275, 10)))

MeasurementTimeseriesMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accumulationIntervalLength'), pyxb.binding.datatypes.duration, scope=MeasurementTimeseriesMetadataType, documentation='Defines the period over which accumulation occurs.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 281, 10)))

MeasurementTimeseriesMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maxGapPeriod'), pyxb.binding.datatypes.duration, scope=MeasurementTimeseriesMetadataType, documentation='Indicates the maxiumum period allowed between two series before interpolation is not possible. \n              ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 286, 10)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 221, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 227, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 232, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 238, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 260, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 265, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 270, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 275, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 281, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 286, 10))
    counters.add(cc_9)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'temporalExtent')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 216, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'baseTime')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 221, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'spacing')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 227, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'commentBlock')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 232, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 238, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startAnchorPoint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 260, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endAnchorPoint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 265, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cumulative')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 270, 10))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accumulationAnchorTime')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 275, 10))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accumulationIntervalLength')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 281, 10))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(MeasurementTimeseriesMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maxGapPeriod')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 286, 10))
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MeasurementTimeseriesMetadataType._Automaton = _BuildAutomaton_33()




DefaultCategoricalTVPMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'codeSpace'), pyxb.binding.datatypes.anyURI, scope=DefaultCategoricalTVPMetadataType, documentation='Defines the default codeSpace for the category timeseries', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 319, 10)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 32, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 38, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 43, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 48, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 54, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 60, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 65, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 319, 10))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DefaultCategoricalTVPMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'quality')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 32, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DefaultCategoricalTVPMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nilReason')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 38, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DefaultCategoricalTVPMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comment')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 43, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DefaultCategoricalTVPMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relatedObservation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 48, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DefaultCategoricalTVPMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'qualifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 54, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(DefaultCategoricalTVPMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'processing')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 60, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(DefaultCategoricalTVPMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 65, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(DefaultCategoricalTVPMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'codeSpace')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 319, 10))
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
DefaultCategoricalTVPMetadataType._Automaton = _BuildAutomaton_34()




MeasureTVPType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), MeasureType, nillable=pyxb.binding.datatypes.boolean(1), scope=MeasureTVPType, documentation='The value of a measurement timeseries is a measure', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 358, 10)))

MeasureTVPType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), TVPMeasurementMetadataPropertyType, scope=MeasureTVPType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 363, 10)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 345, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 358, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 363, 10))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MeasureTVPType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'time')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 345, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MeasureTVPType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 358, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MeasureTVPType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 363, 10))
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
MeasureTVPType._Automaton = _BuildAutomaton_35()




CategoricalTVPType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), pyxb.bundles.opengis.swe_2_0.CategoryPropertyType, nillable=pyxb.binding.datatypes.boolean(1), scope=CategoricalTVPType, documentation='The value type is a category', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 376, 10)))

CategoricalTVPType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), TVPMetadataPropertyType, scope=CategoricalTVPType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 382, 10)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 345, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 376, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 382, 10))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CategoricalTVPType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'time')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 345, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CategoricalTVPType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 376, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CategoricalTVPType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/timeseries.xsd', 382, 10))
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
CategoricalTVPType._Automaton = _BuildAutomaton_36()




MonitoringPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relatedParty'), pyxb.bundles.opengis.iso19139.v20070417.gmd.CI_ResponsibleParty_PropertyType, scope=MonitoringPointType, documentation='Describes parties - individuals or organisations - that are related to the monitoring point. Multiple related parties may be described using the role code list (from ISO 19115). The most common relationships are likely to be: owner, originator, pointOfContact, principalInvestigator and distributor.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 36, 20)))

MonitoringPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'monitoringType'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=MonitoringPointType, documentation='A characterisation of the type of station. E.g. meteorological, surface water, groundwater, water quality etc.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 43, 20)))

MonitoringPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'descriptionReference'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=MonitoringPointType, documentation='Provide extra description about a monitoring point. This could be a link to an HTML page describing the location, photos of a monitoring point, history records etc.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 50, 20)))

MonitoringPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'verticalDatum'), pyxb.bundles.opengis.gml_3_2.VerticalDatumPropertyType, scope=MonitoringPointType, documentation='Specifies the elevation that is used as the zero point, or datum, for vertical measurements (e.g stage/level).  \n                          The gml:VerticalDatumPropertyType type allows specification of the local gauge zero as a height above a reference datum. E.g. local gauge zero is 23m above the AHD using the anchorDefinition. \n                        ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 57, 20)))

MonitoringPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timeZone'), TimeZonePropertyType, scope=MonitoringPointType, documentation='Specifies the time zone that the sampling point is located in. The zone offset must be specified (e.g. +10:00 GMT), with an optional zone abbreviation (e.g. AEST)', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 66, 20)))

MonitoringPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'daylightSavingTimeZone'), TimeZonePropertyType, scope=MonitoringPointType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 73, 20)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 26, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 27, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sampling/2.0/samplingFeature.xsd', 39, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sampling/2.0/samplingFeature.xsd', 66, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sampling/2.0/samplingFeature.xsd', 77, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sampling/2.0/samplingFeature.xsd', 95, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sampling/2.0/samplingFeature.xsd', 107, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/samplingSpatial/2.0/spatialSamplingFeature.xsd', 56, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/samplingSpatial/2.0/spatialSamplingFeature.xsd', 69, 3))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 36, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 43, 20))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 50, 20))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 57, 20))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 66, 20))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 73, 20))
    counters.add(cc_19)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 26, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 27, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_sam, 'type')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sampling/2.0/samplingFeature.xsd', 39, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_sam, 'sampledFeature')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sampling/2.0/samplingFeature.xsd', 50, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_sam, 'lineage')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sampling/2.0/samplingFeature.xsd', 66, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_sam, 'relatedObservation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sampling/2.0/samplingFeature.xsd', 77, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_sam, 'relatedSamplingFeature')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sampling/2.0/samplingFeature.xsd', 95, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_sam, 'parameter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sampling/2.0/samplingFeature.xsd', 107, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_sams, 'hostedProcedure')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/samplingSpatial/2.0/spatialSamplingFeature.xsd', 56, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_sams, 'positionalAccuracy')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/samplingSpatial/2.0/spatialSamplingFeature.xsd', 69, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_sams, 'shape')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/samplingSpatial/2.0/spatialSamplingFeature.xsd', 127, 5))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relatedParty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 36, 20))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'monitoringType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 43, 20))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 50, 20))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'verticalDatum')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 57, 20))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timeZone')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 66, 20))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(MonitoringPointType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'daylightSavingTimeZone')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/waterml/2.0/monitoringPoint.xsd', 73, 20))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
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
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, True) ]))
    st_21._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MonitoringPointType._Automaton = _BuildAutomaton_37()


Collection._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_2.AbstractFeature)

DocumentMetadata._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_2.AbstractGML)

TimeZone._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_2.AbstractObject)

ObservationProcess._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_2.AbstractFeature)

Timeseries._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_2.AbstractFeature)

CommentBlock._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_2.AbstractObject)

ObservationMetadata._setSubstitutionGroup(pyxb.bundles.opengis.iso19139.v20070417.gmd.MD_Metadata)

TVPMeasurementMetadata._setSubstitutionGroup(TVPMetadata)

MeasurementTimeseries._setSubstitutionGroup(Timeseries)

CategoricalTimeseries._setSubstitutionGroup(Timeseries)

MeasurementTimeseriesMetadata._setSubstitutionGroup(TimeseriesMetadata)

DefaultTVPMeasurementMetadata._setSubstitutionGroup(DefaultTVPMetadata)

DefaultTVPCategoricalMetadata._setSubstitutionGroup(DefaultTVPMetadata)

MeasurementTVP._setSubstitutionGroup(TimeValuePair)

CategoricalTVP._setSubstitutionGroup(TimeValuePair)

MonitoringPoint._setSubstitutionGroup(pyxb.bundles.opengis._sams.SF_SpatialSamplingFeature)
