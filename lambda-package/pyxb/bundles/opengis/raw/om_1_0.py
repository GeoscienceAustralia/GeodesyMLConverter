# ./pyxb/bundles/opengis/raw/om_1_0.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:c0f4d50579dd9a32da006ca53fd33f552201da56
# Generated 2017-07-10 00:37:06.501251 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/om/1.0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:e53002f6-6507-11e7-a14a-0a55f9edafa5')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.bundles.opengis.swe_1_0_1
import pyxb.bundles.opengis.sensorML_1_0_1
import pyxb.bundles.common.xlink
import pyxb.bundles.opengis.gml
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/om/1.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gml = pyxb.bundles.opengis.gml.Namespace
_Namespace_gml.configureCategories(['typeBinding', 'elementBinding'])
_Namespace = pyxb.bundles.common.xlink.Namespace
_Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_sml = pyxb.bundles.opengis.sensorML_1_0_1.Namespace
_Namespace_sml.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {http://www.opengis.net/om/1.0}ObservationType with content type ELEMENT_ONLY
class ObservationType (pyxb.bundles.opengis.gml.AbstractFeatureType):
    """Base type for Observations. 
            Observation is an act ("event"), whose result is an estimate of the value of a property of the feature of interest. 
            The observed property may be any property associated with the type of the feature of interest.

			    The following properties are inherited from AbstractFeatureType:
				
				"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ObservationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 27, 1)
    _ElementMap = pyxb.bundles.opengis.gml.AbstractFeatureType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml.AbstractFeatureType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml.AbstractFeatureType
    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element {http://www.opengis.net/om/1.0}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_opengis_netom1_0_ObservationType_httpwww_opengis_netom1_0metadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 44, 5), )

    
    metadata = property(__metadata.value, __metadata.set, None, 'Replace with reference to ISO Metadata entity when GML version 3.2.X has been formally adopted.')

    
    # Element {http://www.opengis.net/om/1.0}samplingTime uses Python identifier samplingTime
    __samplingTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'samplingTime'), 'samplingTime', '__httpwww_opengis_netom1_0_ObservationType_httpwww_opengis_netom1_0samplingTime', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 50, 5), )

    
    samplingTime = property(__samplingTime.value, __samplingTime.set, None, 'The samplingTime is the time that the result applies to the feature-of-interest. \n\t\t\t\t\tThis is the time usually required for geospatial analysis of the result.')

    
    # Element {http://www.opengis.net/om/1.0}resultTime uses Python identifier resultTime
    __resultTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'resultTime'), 'resultTime', '__httpwww_opengis_netom1_0_ObservationType_httpwww_opengis_netom1_0resultTime', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 56, 5), )

    
    resultTime = property(__resultTime.value, __resultTime.set, None, 'The resultTime is the time when the procedure associated with the observation act was applied. \n\t\t\t\t\tFor some observations this is identical to samplingTime, in which case the resultTime may be omitted. \n\t\t\t\t\t\n\t\t\t\t\tExample: \tWhere a measurement is made on a specimen in a laboratory, the samplingTime should record the time the specimen was retrieved from its host, while the resultTime should record the time the laboratory procedure was applied. \n\t\t\t\t\tExample: \tWhere sensor observation results are post-processed, the resultTime is the post-processing time, while the samplingTime preserves the time of initial interaction with the world. \n\t\t\t\t\tExample: \tSimulations are often used to estimate the values for phenomena in the future or past. The samplingTime is the real-world time that the result applies to, while the resultTime is the time that the simulation process was executed.')

    
    # Element {http://www.opengis.net/om/1.0}procedure uses Python identifier procedure
    __procedure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'procedure'), 'procedure', '__httpwww_opengis_netom1_0_ObservationType_httpwww_opengis_netom1_0procedure', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 66, 5), )

    
    procedure = property(__procedure.value, __procedure.set, None, 'The procedure is the description of a process used to generate the result. \n\t\t\t\t\t\t\tIt must be suitable for the observed property. \n\t\t\t\t\t\t\tNOTE: \tAt this level we do not distinguish between sensor-observations, \n\t\t\t\t\t\t\testimations made by an observer, or algorithms, simulations, computations and complex processing chains.')

    
    # Element {http://www.opengis.net/om/1.0}resultQuality uses Python identifier resultQuality
    __resultQuality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'resultQuality'), 'resultQuality', '__httpwww_opengis_netom1_0_ObservationType_httpwww_opengis_netom1_0resultQuality', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 74, 5), )

    
    resultQuality = property(__resultQuality.value, __resultQuality.set, None, 'Instance-specific quality assessment or measure. \n\t\t\t\t\t\t\tAllow multiple quality measures if required.\t\t\t\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\tReplace with reference to ISO Metadata entity when GML version 3.2.X has been formally adopted.')

    
    # Element {http://www.opengis.net/om/1.0}observedProperty uses Python identifier observedProperty
    __observedProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'observedProperty'), 'observedProperty', '__httpwww_opengis_netom1_0_ObservationType_httpwww_opengis_netom1_0observedProperty', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 83, 5), )

    
    observedProperty = property(__observedProperty.value, __observedProperty.set, None, 'Property-type or phenomenon for which the observation result provides an estimate of its value. \n\t\t\t\t\t\t\tfor example "wavelength", "grass-species", "power", "intensity in the waveband x-y", etc. \n\t\t\t\t\t\t\tIt must be a property associated with the type of the feature of interest. \n\t\t\t\t\t\t\tThis feature-property that provides the (semantic) type of the observation. \n\t\t\t\t\t\t\tThe description of the phenomenon may be quite specific and constrained. \n\n\t\t\t\t\t\t\tThe description of the property-type may be presented using various alternative encodings. \n\t\t\t\t\t\t\tIf shown inline, the swe:Phenomenon schema is required. \n\t\t\t\t\t\t\tIf provided using another encoding (e.g. OWL or SWEET) then the description must be in a remote repository and xlink reference used.')

    
    # Element {http://www.opengis.net/om/1.0}featureOfInterest uses Python identifier featureOfInterest
    __featureOfInterest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'featureOfInterest'), 'featureOfInterest', '__httpwww_opengis_netom1_0_ObservationType_httpwww_opengis_netom1_0featureOfInterest', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 96, 5), )

    
    featureOfInterest = property(__featureOfInterest.value, __featureOfInterest.set, None, 'The featureOfInterest is a feature of any type (ISO 19109, ISO 19101), which is a representation of the observation target, being the real-world object regarding which the observation is made. \n\t\t\t\t\t\t\tsuch as a specimen, station, tract, mountain, pixel, etc. \n\t\t\t\t\t\t\tThe spatial properties (location) of this feature of interest are typically of most interest for spatial analysis of the observation result.')

    
    # Element {http://www.opengis.net/om/1.0}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameter'), 'parameter', '__httpwww_opengis_netom1_0_ObservationType_httpwww_opengis_netom1_0parameter', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 103, 5), )

    
    parameter = property(__parameter.value, __parameter.set, None, 'An Observation parameter is a general event-specific parameter. \n\t\t\t\t\t\t\tThis will typically be used to record environmental parameters, or event-specific sampling parameters that are not tightly bound to either the feature-of-interest or the procedure. \n\t\t\t\t\t\t\tNOTE: \tParameters that are tightly bound to the procedure should be recorded as part of the procedure description. For example, the SensorML model associates parameters with specific process elements or stages. \n\t\t\t\t\t\t\tNOTE: \tThe semantics of the parameter must be provided as part of its value. \n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\tIn some applications it is convenient to use a generic or standard procedure, or feature-of-interest, rather than define an event-specific process or feature. \n\t\t\t\t\t\t\tIn this context, event-specific parameters are bound to the Observation act.')

    
    # Element {http://www.opengis.net/om/1.0}result uses Python identifier result
    __result = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'result'), 'result', '__httpwww_opengis_netom1_0_ObservationType_httpwww_opengis_netom1_0result', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 114, 5), )

    
    result = property(__result.value, __result.set, None, 'The result contains the value generated by the procedure. \n\t\t\t\t\t\t\tThe type of the observation result must be consistent with the observed property, and the scale or scope for the value must be consistent with the quantity or category type. \n\t\t\t\t\t\t\tApplication profiles may choose to constrain the type of the result.')

    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __metadata.name() : __metadata,
        __samplingTime.name() : __samplingTime,
        __resultTime.name() : __resultTime,
        __procedure.name() : __procedure,
        __resultQuality.name() : __resultQuality,
        __observedProperty.name() : __observedProperty,
        __featureOfInterest.name() : __featureOfInterest,
        __parameter.name() : __parameter,
        __result.name() : __result
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ObservationType = ObservationType
Namespace.addCategoryObject('typeBinding', 'ObservationType', ObservationType)


# Complex type {http://www.opengis.net/om/1.0}ObservationPropertyType with content type ELEMENT_ONLY
class ObservationPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/om/1.0}ObservationPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ObservationPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 133, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/om/1.0}Observation uses Python identifier Observation
    __Observation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Observation'), 'Observation', '__httpwww_opengis_netom1_0_ObservationPropertyType_httpwww_opengis_netom1_0Observation', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 126, 1), )

    
    Observation = property(__Observation.value, __Observation.set, None, 'Observation is an act ("event"), whose result is an estimate of the value of a property of the feature of interest. \n            The observed property may be any property associated with the type of the feature of interest.')

    
    # Attribute {http://www.opengis.net/gml}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netom1_0_ObservationPropertyType_httpwww_opengis_netgmlremoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 258, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 269, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, 'Reference to an XML Schema fragment that specifies the content model of the propertys value. This is in conformance with the XML Schema Section 4.14 Referencing Schemas from Elsewhere.')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netom1_0_ObservationPropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netom1_0_ObservationPropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netom1_0_ObservationPropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netom1_0_ObservationPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netom1_0_ObservationPropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netom1_0_ObservationPropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netom1_0_ObservationPropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __Observation.name() : __Observation
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
_module_typeBindings.ObservationPropertyType = ObservationPropertyType
Namespace.addCategoryObject('typeBinding', 'ObservationPropertyType', ObservationPropertyType)


# Complex type {http://www.opengis.net/om/1.0}ObservationCollectionType with content type ELEMENT_ONLY
class ObservationCollectionType (pyxb.bundles.opengis.gml.AbstractFeatureType):
    """Collection of arbitrary observations"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ObservationCollectionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 142, 1)
    _ElementMap = pyxb.bundles.opengis.gml.AbstractFeatureType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml.AbstractFeatureType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml.AbstractFeatureType
    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element {http://www.opengis.net/om/1.0}member uses Python identifier member
    __member = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'member'), 'member', '__httpwww_opengis_netom1_0_ObservationCollectionType_httpwww_opengis_netom1_0member', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 149, 5), )

    
    member = property(__member.value, __member.set, None, None)

    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __member.name() : __member
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ObservationCollectionType = ObservationCollectionType
Namespace.addCategoryObject('typeBinding', 'ObservationCollectionType', ObservationCollectionType)


# Complex type {http://www.opengis.net/om/1.0}ProcessPropertyType with content type ELEMENT_ONLY
class ProcessPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """This property type allows the Observation/procedure property to  either 
		* contain a SensorML Process, 
		* contain a description of a process described using another model, wrapped inside a om:Process element
		* point to a Process either elsewhere in the document or identified by a URI"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProcessPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 162, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/om/1.0}Process uses Python identifier Process
    __Process = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Process'), 'Process', '__httpwww_opengis_netom1_0_ProcessPropertyType_httpwww_opengis_netom1_0Process', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 176, 4), )

    
    Process = property(__Process.value, __Process.set, None, 'This element is xs:anyType so may contain a description of a process provided in any well-formed XML. \n\t\t\t\tIf the process description is namespace qualified, then the namespace must be identified in the instance document.')

    
    # Element {http://www.opengis.net/sensorML/1.0.1}_Process uses Python identifier Process_
    __Process_ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_sml, '_Process'), 'Process_', '__httpwww_opengis_netom1_0_ProcessPropertyType_httpwww_opengis_netsensorML1_0_1_Process', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sensorML/1.0.1/process.xsd', 17, 1), )

    
    Process_ = property(__Process_.value, __Process_.set, None, 'base substitution group for all processes')

    
    # Attribute {http://www.opengis.net/gml}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netom1_0_ProcessPropertyType_httpwww_opengis_netgmlremoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 258, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 269, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, 'Reference to an XML Schema fragment that specifies the content model of the propertys value. This is in conformance with the XML Schema Section 4.14 Referencing Schemas from Elsewhere.')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netom1_0_ProcessPropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netom1_0_ProcessPropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netom1_0_ProcessPropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netom1_0_ProcessPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netom1_0_ProcessPropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netom1_0_ProcessPropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netom1_0_ProcessPropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __Process.name() : __Process,
        __Process_.name() : __Process_
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
_module_typeBindings.ProcessPropertyType = ProcessPropertyType
Namespace.addCategoryObject('typeBinding', 'ProcessPropertyType', ProcessPropertyType)


# Complex type {http://www.opengis.net/om/1.0}AnyOrReferenceType with content type ELEMENT_ONLY
class AnyOrReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """Placeholder type
			Used in a few places where ISO 19139 metadata classes are used, which will become available with GML 3.2"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnyOrReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 188, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.opengis.net/gml}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netom1_0_AnyOrReferenceType_httpwww_opengis_netgmlremoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 258, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 269, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, 'Reference to an XML Schema fragment that specifies the content model of the propertys value. This is in conformance with the XML Schema Section 4.14 Referencing Schemas from Elsewhere.')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netom1_0_AnyOrReferenceType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netom1_0_AnyOrReferenceType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netom1_0_AnyOrReferenceType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netom1_0_AnyOrReferenceType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netom1_0_AnyOrReferenceType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netom1_0_AnyOrReferenceType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netom1_0_AnyOrReferenceType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
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
_module_typeBindings.AnyOrReferenceType = AnyOrReferenceType
Namespace.addCategoryObject('typeBinding', 'AnyOrReferenceType', AnyOrReferenceType)


Observation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Observation'), ObservationType, documentation='Observation is an act ("event"), whose result is an estimate of the value of a property of the feature of interest. \n            The observed property may be any property associated with the type of the feature of interest.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 126, 1))
Namespace.addCategoryObject('elementBinding', Observation.name().localName(), Observation)

ObservationCollection = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObservationCollection'), ObservationCollectionType, documentation='Collection of arbitrary observations', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 155, 1))
Namespace.addCategoryObject('elementBinding', ObservationCollection.name().localName(), ObservationCollection)



ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), AnyOrReferenceType, scope=ObservationType, documentation='Replace with reference to ISO Metadata entity when GML version 3.2.X has been formally adopted.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 44, 5)))

ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'samplingTime'), pyxb.bundles.opengis.swe_1_0_1.TimeObjectPropertyType, scope=ObservationType, documentation='The samplingTime is the time that the result applies to the feature-of-interest. \n\t\t\t\t\tThis is the time usually required for geospatial analysis of the result.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 50, 5)))

ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'resultTime'), pyxb.bundles.opengis.swe_1_0_1.TimeObjectPropertyType, scope=ObservationType, documentation='The resultTime is the time when the procedure associated with the observation act was applied. \n\t\t\t\t\tFor some observations this is identical to samplingTime, in which case the resultTime may be omitted. \n\t\t\t\t\t\n\t\t\t\t\tExample: \tWhere a measurement is made on a specimen in a laboratory, the samplingTime should record the time the specimen was retrieved from its host, while the resultTime should record the time the laboratory procedure was applied. \n\t\t\t\t\tExample: \tWhere sensor observation results are post-processed, the resultTime is the post-processing time, while the samplingTime preserves the time of initial interaction with the world. \n\t\t\t\t\tExample: \tSimulations are often used to estimate the values for phenomena in the future or past. The samplingTime is the real-world time that the result applies to, while the resultTime is the time that the simulation process was executed.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 56, 5)))

ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'procedure'), ProcessPropertyType, scope=ObservationType, documentation='The procedure is the description of a process used to generate the result. \n\t\t\t\t\t\t\tIt must be suitable for the observed property. \n\t\t\t\t\t\t\tNOTE: \tAt this level we do not distinguish between sensor-observations, \n\t\t\t\t\t\t\testimations made by an observer, or algorithms, simulations, computations and complex processing chains.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 66, 5)))

ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'resultQuality'), AnyOrReferenceType, scope=ObservationType, documentation='Instance-specific quality assessment or measure. \n\t\t\t\t\t\t\tAllow multiple quality measures if required.\t\t\t\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\tReplace with reference to ISO Metadata entity when GML version 3.2.X has been formally adopted.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 74, 5)))

ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'observedProperty'), pyxb.bundles.opengis.swe_1_0_1.PhenomenonPropertyType, scope=ObservationType, documentation='Property-type or phenomenon for which the observation result provides an estimate of its value. \n\t\t\t\t\t\t\tfor example "wavelength", "grass-species", "power", "intensity in the waveband x-y", etc. \n\t\t\t\t\t\t\tIt must be a property associated with the type of the feature of interest. \n\t\t\t\t\t\t\tThis feature-property that provides the (semantic) type of the observation. \n\t\t\t\t\t\t\tThe description of the phenomenon may be quite specific and constrained. \n\n\t\t\t\t\t\t\tThe description of the property-type may be presented using various alternative encodings. \n\t\t\t\t\t\t\tIf shown inline, the swe:Phenomenon schema is required. \n\t\t\t\t\t\t\tIf provided using another encoding (e.g. OWL or SWEET) then the description must be in a remote repository and xlink reference used.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 83, 5)))

ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'featureOfInterest'), pyxb.bundles.opengis.gml.FeaturePropertyType, scope=ObservationType, documentation='The featureOfInterest is a feature of any type (ISO 19109, ISO 19101), which is a representation of the observation target, being the real-world object regarding which the observation is made. \n\t\t\t\t\t\t\tsuch as a specimen, station, tract, mountain, pixel, etc. \n\t\t\t\t\t\t\tThe spatial properties (location) of this feature of interest are typically of most interest for spatial analysis of the observation result.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 96, 5)))

ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameter'), pyxb.bundles.opengis.swe_1_0_1.AnyDataPropertyType, scope=ObservationType, documentation='An Observation parameter is a general event-specific parameter. \n\t\t\t\t\t\t\tThis will typically be used to record environmental parameters, or event-specific sampling parameters that are not tightly bound to either the feature-of-interest or the procedure. \n\t\t\t\t\t\t\tNOTE: \tParameters that are tightly bound to the procedure should be recorded as part of the procedure description. For example, the SensorML model associates parameters with specific process elements or stages. \n\t\t\t\t\t\t\tNOTE: \tThe semantics of the parameter must be provided as part of its value. \n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\tIn some applications it is convenient to use a generic or standard procedure, or feature-of-interest, rather than define an event-specific process or feature. \n\t\t\t\t\t\t\tIn this context, event-specific parameters are bound to the Observation act.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 103, 5)))

ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'result'), pyxb.binding.datatypes.anyType, scope=ObservationType, documentation='The result contains the value generated by the procedure. \n\t\t\t\t\t\t\tThe type of the observation result must be consistent with the observed property, and the scale or scope for the value must be consistent with the quantity or category type. \n\t\t\t\t\t\t\tApplication profiles may choose to constrain the type of the result.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 114, 5)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
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
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 44, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 56, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 74, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 103, 5))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 44, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'samplingTime')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 50, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'resultTime')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 56, 5))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'procedure')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 66, 5))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'resultQuality')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 74, 5))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'observedProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 83, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'featureOfInterest')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 96, 5))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 103, 5))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'result')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 114, 5))
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
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
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
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ObservationType._Automaton = _BuildAutomaton()




ObservationPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Observation'), ObservationType, scope=ObservationPropertyType, documentation='Observation is an act ("event"), whose result is an estimate of the value of a property of the feature of interest. \n            The observed property may be any property associated with the type of the feature of interest.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 126, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 134, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ObservationPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Observation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 135, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ObservationPropertyType._Automaton = _BuildAutomaton_()




ObservationCollectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'member'), ObservationPropertyType, scope=ObservationCollectionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 149, 5)))

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
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationCollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationCollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationCollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationCollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationCollectionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ObservationCollectionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'member')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 149, 5))
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
ObservationCollectionType._Automaton = _BuildAutomaton_2()




ProcessPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Process'), pyxb.binding.datatypes.anyType, scope=ProcessPropertyType, documentation='This element is xs:anyType so may contain a description of a process provided in any well-formed XML. \n\t\t\t\tIf the process description is namespace qualified, then the namespace must be identified in the instance document.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 176, 4)))

ProcessPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_sml, '_Process'), pyxb.bundles.opengis.sensorML_1_0_1.AbstractProcessType, abstract=pyxb.binding.datatypes.boolean(1), scope=ProcessPropertyType, documentation='base substitution group for all processes', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sensorML/1.0.1/process.xsd', 17, 1)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 169, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProcessPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_sml, '_Process')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 171, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProcessPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Process')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 176, 4))
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
ProcessPropertyType._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 193, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/1.0.0/observation.xsd', 194, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AnyOrReferenceType._Automaton = _BuildAutomaton_4()


Observation._setSubstitutionGroup(pyxb.bundles.opengis.gml.Feature)

ObservationCollection._setSubstitutionGroup(pyxb.bundles.opengis.gml.Feature)
