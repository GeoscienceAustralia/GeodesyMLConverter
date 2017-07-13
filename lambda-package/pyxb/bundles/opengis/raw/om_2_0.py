# ./pyxb/bundles/opengis/raw/om_2_0.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:fd8991d47a42db9b29acdbb43f7d40be2e37f986
# Generated 2017-07-10 00:37:08.886199 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/om/2.0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:e6d32c3c-6507-11e7-b8b8-0a55f9edafa5')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.bundles.opengis.iso19139.v20070417.gmd
import pyxb.bundles.opengis.gml_3_2
import pyxb.bundles.common.xlink
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/om/2.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gml = pyxb.bundles.opengis.gml_3_2.Namespace
_Namespace_gml.configureCategories(['typeBinding', 'elementBinding'])
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


# Complex type {http://www.opengis.net/om/2.0}OM_ObservationType with content type ELEMENT_ONLY
class OM_ObservationType (pyxb.bundles.opengis.gml_3_2.AbstractFeatureType):
    """ Generic observation, whose result is anyType The following properties
				are inherited from AbstractFeatureType: 
				
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OM_ObservationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 217, 1)
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
    
    # Element {http://www.opengis.net/om/2.0}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__httpwww_opengis_netom2_0_OM_ObservationType_httpwww_opengis_netom2_0type', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 42, 3), )

    
    type = property(__type.value, __type.set, None, "If present, the sub-element 'type' shall indicate the class of\n\t\t\t\t\t\tobservation. A register of type identifiers corresponding with the\n\t\t\t\t\t\tobservation types in ISO 19156, which distinguishes types on the basis of\n\t\t\t\t\t\tthe type of the result, is provided by OGC at\n\t\t\t\t\t\thttp://www.opengis.net/def/observationType/OGC-OM/2.0/ ")

    
    # Element {http://www.opengis.net/om/2.0}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_opengis_netom2_0_OM_ObservationType_httpwww_opengis_netom2_0metadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 54, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, ' If present, the association Metadata shall link the\n\t\t\t\t\t\tOM_Observation to descriptive metadata. ')

    
    # Element {http://www.opengis.net/om/2.0}relatedObservation uses Python identifier relatedObservation
    __relatedObservation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relatedObservation'), 'relatedObservation', '__httpwww_opengis_netom2_0_OM_ObservationType_httpwww_opengis_netom2_0relatedObservation', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 63, 3), )

    
    relatedObservation = property(__relatedObservation.value, __relatedObservation.set, None, ' Some observations depend on other observations to provide\n\t\t\t\t\t\tcontext which is important, sometimes essential, in understanding the\n\t\t\t\t\t\tresult. These dependencies are stronger than mere spatiotemporal\n\t\t\t\t\t\tcoincidences, requiring explicit representation. If present, the association\n\t\t\t\t\t\tclass ObservationContext (Figure 2) shall link a OM_Observation to another\n\t\t\t\t\t\tOM_Observation, with the role name relatedObservation for the target.\n\t\t\t\t\t')

    
    # Element {http://www.opengis.net/om/2.0}phenomenonTime uses Python identifier phenomenonTime
    __phenomenonTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'phenomenonTime'), 'phenomenonTime', '__httpwww_opengis_netom2_0_OM_ObservationType_httpwww_opengis_netom2_0phenomenonTime', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 78, 3), )

    
    phenomenonTime = property(__phenomenonTime.value, __phenomenonTime.set, None, ' The attribute phenomenonTime:TM_Object shall describe the time\n\t\t\t\t\t\tthat the result (6.2.2.9) applies to the property of the feature-of-interest\n\t\t\t\t\t\t(6.2.2.7). This is often the time of interaction by a sampling procedure\n\t\t\t\t\t\t(8.1.3) or observation procedure (6.2.2.10) with a real-world feature.\n\t\t\t\t\t')

    
    # Element {http://www.opengis.net/om/2.0}resultTime uses Python identifier resultTime
    __resultTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'resultTime'), 'resultTime', '__httpwww_opengis_netom2_0_OM_ObservationType_httpwww_opengis_netom2_0resultTime', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 89, 3), )

    
    resultTime = property(__resultTime.value, __resultTime.set, None, ' The attribute resultTime:TM_Instant shall describe the time when\n\t\t\t\t\t\tthe result became available, typically when the procedure (6.2.2.10)\n\t\t\t\t\t\tassociated with the observation was completed For some observations this is\n\t\t\t\t\t\tidentical to the samplingTime. However, there are important cases where they\n\t\t\t\t\t\tdiffer. ')

    
    # Element {http://www.opengis.net/om/2.0}validTime uses Python identifier validTime
    __validTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'validTime'), 'validTime', '__httpwww_opengis_netom2_0_OM_ObservationType_httpwww_opengis_netom2_0validTime', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 102, 3), )

    
    validTime = property(__validTime.value, __validTime.set, None, ' If present, the attribute validTime:TM_Period shall describe the\n\t\t\t\t\t\ttime period during which the result is intended to be used. ')

    
    # Element {http://www.opengis.net/om/2.0}procedure uses Python identifier procedure
    __procedure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'procedure'), 'procedure', '__httpwww_opengis_netom2_0_OM_ObservationType_httpwww_opengis_netom2_0procedure', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 111, 3), )

    
    procedure = property(__procedure.value, __procedure.set, None, ' The association ProcessUsed shall link the OM_Observation to the\n\t\t\t\t\t\tOM_Process (6.2.3) used to generate the result. The process has the role\n\t\t\t\t\t\tprocedure with respect to the observation. A process might be responsible\n\t\t\t\t\t\tfor more than one generatedObservation. ')

    
    # Element {http://www.opengis.net/om/2.0}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameter'), 'parameter', '__httpwww_opengis_netom2_0_OM_ObservationType_httpwww_opengis_netom2_0parameter', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 122, 3), )

    
    parameter = property(__parameter.value, __parameter.set, None, ' If present, the attributes parameter:NamedValue shall describe\n\t\t\t\t\t\tan arbitrary event-specific parameter. This might be an environmental\n\t\t\t\t\t\tparameter, an instrument setting or input, or an event-specific sampling\n\t\t\t\t\t\tparameter that is not tightly bound to either the feature-of-interest\n\t\t\t\t\t\t(6.2.2.7) or to the observation procedure (6.2.2.10). To avoid ambiguity,\n\t\t\t\t\t\tthere shall be no more than one parameter with the same name. NOTE\n\t\t\t\t\t\tParameters that are tightly bound to the procedure may be recorded as part\n\t\t\t\t\t\tof the procedure description. In some contexts the Observation::procedure\n\t\t\t\t\t\t(6.2.2.10) is a generic or standard procedure, rather than an event-specific\n\t\t\t\t\t\tprocess. In this context, parameters bound to the observation act, such as\n\t\t\t\t\t\tinstrument settings, calibrations or inputs, local position, detection\n\t\t\t\t\t\tlimits, asset identifier, operator, may augment the description of a\n\t\t\t\t\t\tstandard procedure. ')

    
    # Element {http://www.opengis.net/om/2.0}observedProperty uses Python identifier observedProperty
    __observedProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'observedProperty'), 'observedProperty', '__httpwww_opengis_netom2_0_OM_ObservationType_httpwww_opengis_netom2_0observedProperty', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 143, 3), )

    
    observedProperty = property(__observedProperty.value, __observedProperty.set, None, ' The association Phenomenon shall link the OM_Observation to the\n\t\t\t\t\t\tGFI_PropertyType (C.2.2) for which the OM_Observation:result (6.2.2.9)\n\t\t\t\t\t\tprovides an estimate of its value. The property type has the role\n\t\t\t\t\t\tobservedProperty with respect to the observation. The observed property\n\t\t\t\t\t\tshall be a phenomenon associated with the type of the featureOfInterest.\n\t\t\t\t\t\tNOTE An observed property may, but need not be modelled as a property (in\n\t\t\t\t\t\tthe sense of the General Feature Model) in a formal application schema that\n\t\t\t\t\t\tdefines the type of the feature of interest The observed property supports\n\t\t\t\t\t\tsemantic or thematic classification of observations, which is useful for\n\t\t\t\t\t\tdiscovery and data fusion. ')

    
    # Element {http://www.opengis.net/om/2.0}featureOfInterest uses Python identifier featureOfInterest
    __featureOfInterest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'featureOfInterest'), 'featureOfInterest', '__httpwww_opengis_netom2_0_OM_ObservationType_httpwww_opengis_netom2_0featureOfInterest', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 163, 3), )

    
    featureOfInterest = property(__featureOfInterest.value, __featureOfInterest.set, None, ' The association Domain shall link the OM_Observation to the\n\t\t\t\t\t\tGFI_Feature (C.2.1) that is the subject of the observation and carries the\n\t\t\t\t\t\tobserved property. This feature has the role featureOfInterest with respect\n\t\t\t\t\t\tto the observation. This feature is the real-world object whose properties\n\t\t\t\t\t\tare under observation, or is a feature intended to sample the real-world\n\t\t\t\t\t\tobject, as described in Clause 8 of this International Standard. An\n\t\t\t\t\t\tobservation instance serves as a propertyValueProvider for its feature of\n\t\t\t\t\t\tinterest. ')

    
    # Element {http://www.opengis.net/om/2.0}resultQuality uses Python identifier resultQuality
    __resultQuality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'resultQuality'), 'resultQuality', '__httpwww_opengis_netom2_0_OM_ObservationType_httpwww_opengis_netom2_0resultQuality', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 178, 3), )

    
    resultQuality = property(__resultQuality.value, __resultQuality.set, None, ' If present, the attributes resultQuality:DQ_Element shall\n\t\t\t\t\t\tdescribe the quality of the result (6.2.2.9). This instance-specific\n\t\t\t\t\t\tdescription complements the description of the observation procedure\n\t\t\t\t\t\t(6.2.2.10), which provides information concerning the quality of all\n\t\t\t\t\t\tobservations using this procedure. Quality of a result may be assessed\n\t\t\t\t\t\tfollowing the procedures in ISO 19114:2003. Multiple measures may be\n\t\t\t\t\t\tprovided (ISO/TS 19138:2006). ')

    
    # Element {http://www.opengis.net/om/2.0}result uses Python identifier result
    __result = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'result'), 'result', '__httpwww_opengis_netom2_0_OM_ObservationType_httpwww_opengis_netom2_0result', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 199, 1), )

    
    result = property(__result.value, __result.set, None, ' The association Range shall link the OM_Observation to the value\n\t\t\t\tgenerated by the procedure. The value has the role result with respect to the\n\t\t\t\tobservation. The type of the result is shown as Any, since it may represent the\n\t\t\t\tvalue of any feature property. NOTE 1 OGC SWE Common provides a model suitable for\n\t\t\t\tdescribing many kinds of observation results. The type of the observation result\n\t\t\t\tshall be consistent with the observed property, and the scale or scope for the value\n\t\t\t\tshall be consistent with the quantity or category type. If the observed property\n\t\t\t\t(6.2.2.8) is a spatial operation or function, the type of the result may be a\n\t\t\t\tcoverage, NOTE 2 In some contexts, particularly in earth and environmental sciences,\n\t\t\t\tthe term \u201cobservation\u201d is used to refer to the result itself. ')

    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    _ElementMap.update({
        __type.name() : __type,
        __metadata.name() : __metadata,
        __relatedObservation.name() : __relatedObservation,
        __phenomenonTime.name() : __phenomenonTime,
        __resultTime.name() : __resultTime,
        __validTime.name() : __validTime,
        __procedure.name() : __procedure,
        __parameter.name() : __parameter,
        __observedProperty.name() : __observedProperty,
        __featureOfInterest.name() : __featureOfInterest,
        __resultQuality.name() : __resultQuality,
        __result.name() : __result
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OM_ObservationType = OM_ObservationType
Namespace.addCategoryObject('typeBinding', 'OM_ObservationType', OM_ObservationType)


# Complex type {http://www.opengis.net/om/2.0}OM_ObservationPropertyType with content type ELEMENT_ONLY
class OM_ObservationPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/om/2.0}OM_ObservationPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OM_ObservationPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 253, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/om/2.0}OM_Observation uses Python identifier OM_Observation
    __OM_Observation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OM_Observation'), 'OM_Observation', '__httpwww_opengis_netom2_0_OM_ObservationPropertyType_httpwww_opengis_netom2_0OM_Observation', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 242, 1), )

    
    OM_Observation = property(__OM_Observation.value, __OM_Observation.set, None, 'Observation is an act ("event"), whose result is an estimate of the value\n\t\t\t\tof a property of the feature of interest. The observed property may be any property\n\t\t\t\tassociated with the type of the feature of interest.')

    
    # Attribute {http://www.opengis.net/gml/3.2}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netom2_0_OM_ObservationPropertyType_httpwww_opengis_netgml3_2remoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/deprecatedTypes.xsd', 638, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 52, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, '')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netom2_0_OM_ObservationPropertyType_nilReason', pyxb.bundles.opengis.gml_3_2.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netom2_0_OM_ObservationPropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netom2_0_OM_ObservationPropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netom2_0_OM_ObservationPropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netom2_0_OM_ObservationPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netom2_0_OM_ObservationPropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netom2_0_OM_ObservationPropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netom2_0_OM_ObservationPropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __OM_Observation.name() : __OM_Observation
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.OM_ObservationPropertyType = OM_ObservationPropertyType
Namespace.addCategoryObject('typeBinding', 'OM_ObservationPropertyType', OM_ObservationPropertyType)


# Complex type {http://www.opengis.net/om/2.0}ObservationContextType with content type ELEMENT_ONLY
class ObservationContextType (pyxb.binding.basis.complexTypeDefinition):
    """ Some observations depend on other observations to provide context which
				is important, sometimes essential, in understanding the result. These dependencies
				are stronger than mere spatiotemporal coincidences, requiring explicit
				representation. If present, the association class ObservationContext (Figure 2)
				shall link a OM_Observation to another OM_Observation, with the role name
				relatedObservation for the target. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ObservationContextType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 266, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/om/2.0}role uses Python identifier role
    __role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'role'), 'role', '__httpwww_opengis_netom2_0_ObservationContextType_httpwww_opengis_netom2_0role', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 277, 3), )

    
    role = property(__role.value, __role.set, None, "The attribute 'role' shall describe the relationship of the\n\t\t\t\t\t\ttarget OM_Observation to the source OM_Observation. ")

    
    # Element {http://www.opengis.net/om/2.0}relatedObservation uses Python identifier relatedObservation
    __relatedObservation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relatedObservation'), 'relatedObservation', '__httpwww_opengis_netom2_0_ObservationContextType_httpwww_opengis_netom2_0relatedObservation', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 285, 3), )

    
    relatedObservation = property(__relatedObservation.value, __relatedObservation.set, None, ' Some observations depend on other observations to provide\n\t\t\t\t\t\tcontext which is important, sometimes essential, in understanding the\n\t\t\t\t\t\tresult. These dependencies are stronger than mere spatiotemporal\n\t\t\t\t\t\tcoincidences, requiring explicit representation. If present, the association\n\t\t\t\t\t\tclass ObservationContext (Figure 2) shall link a OM_Observation to another\n\t\t\t\t\t\tOM_Observation, with the role name relatedObservation for the target.\n\t\t\t\t\t')

    _ElementMap.update({
        __role.name() : __role,
        __relatedObservation.name() : __relatedObservation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ObservationContextType = ObservationContextType
Namespace.addCategoryObject('typeBinding', 'ObservationContextType', ObservationContextType)


# Complex type {http://www.opengis.net/om/2.0}ObservationContextPropertyType with content type ELEMENT_ONLY
class ObservationContextPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """ObservationContext is a dataType, without identity, so may only be used
				inline"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ObservationContextPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 317, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/om/2.0}ObservationContext uses Python identifier ObservationContext
    __ObservationContext = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ObservationContext'), 'ObservationContext', '__httpwww_opengis_netom2_0_ObservationContextPropertyType_httpwww_opengis_netom2_0ObservationContext', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 304, 1), )

    
    ObservationContext = property(__ObservationContext.value, __ObservationContext.set, None, ' Some observations depend on other observations to provide context which\n\t\t\t\tis important, sometimes essential, in understanding the result. These dependencies\n\t\t\t\tare stronger than mere spatiotemporal coincidences, requiring explicit\n\t\t\t\trepresentation. If present, the association class ObservationContext (Figure 2)\n\t\t\t\tshall link a OM_Observation to another OM_Observation, with the role name\n\t\t\t\trelatedObservation for the target. ')

    _ElementMap.update({
        __ObservationContext.name() : __ObservationContext
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ObservationContextPropertyType = ObservationContextPropertyType
Namespace.addCategoryObject('typeBinding', 'ObservationContextPropertyType', ObservationContextPropertyType)


# Complex type {http://www.opengis.net/om/2.0}OM_ProcessPropertyType with content type ELEMENT_ONLY
class OM_ProcessPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """ The purpose of an observation process is to generate an observation
				result. An instance is often an instrument or sensor, but may be a human observer, a
				simulator, or a process or algorithm applied to more primitive results used as
				inputs. The model for OM_Process is abstract, and has no attributes, operations, or
				associations. NOTE ISO 19115-2:2008 provides MI_Instrument, LE_Processing and
				LE_Algorithm, which could all be modelled as specializations of OM_Process. Any
				suitable XML may be used to describe the observation process in line, provided that
				it is contained in a single XML element. If reference to a schema is provided it
				must also be valid. OGC SensorML provides a model which is suitable for many
				observation procedures. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OM_ProcessPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 331, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.opengis.net/gml/3.2}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netom2_0_OM_ProcessPropertyType_httpwww_opengis_netgml3_2remoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/deprecatedTypes.xsd', 638, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 52, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, '')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netom2_0_OM_ProcessPropertyType_nilReason', pyxb.bundles.opengis.gml_3_2.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netom2_0_OM_ProcessPropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netom2_0_OM_ProcessPropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netom2_0_OM_ProcessPropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netom2_0_OM_ProcessPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netom2_0_OM_ProcessPropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netom2_0_OM_ProcessPropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netom2_0_OM_ProcessPropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.OM_ProcessPropertyType = OM_ProcessPropertyType
Namespace.addCategoryObject('typeBinding', 'OM_ProcessPropertyType', OM_ProcessPropertyType)


# Complex type {http://www.opengis.net/om/2.0}NamedValueType with content type ELEMENT_ONLY
class NamedValueType (pyxb.binding.basis.complexTypeDefinition):
    """ The class 'NamedValue' provides for a generic soft-typed parameter
				value. NamedValue shall support two attributes. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NamedValueType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 363, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/om/2.0}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpwww_opengis_netom2_0_NamedValueType_httpwww_opengis_netom2_0name', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 370, 3), )

    
    name = property(__name.value, __name.set, None, " The attribute 'name' shall indicate the meaning of the named\n\t\t\t\t\t\tvalue. Its value should be taken from a well-governed source if possible.\n\t\t\t\t\t")

    
    # Element {http://www.opengis.net/om/2.0}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__httpwww_opengis_netom2_0_NamedValueType_httpwww_opengis_netom2_0value', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 379, 3), )

    
    value_ = property(__value.value, __value.set, None, " The attribute 'value' shall provide the value. The type Any\n\t\t\t\t\t\tshould be substituted by a suitable concrete type, such as\n\t\t\t\t\t\tCI_ResponsibleParty or Measure. ")

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NamedValueType = NamedValueType
Namespace.addCategoryObject('typeBinding', 'NamedValueType', NamedValueType)


# Complex type {http://www.opengis.net/om/2.0}NamedValuePropertyType with content type ELEMENT_ONLY
class NamedValuePropertyType (pyxb.binding.basis.complexTypeDefinition):
    """ The class 'NamedValue' provides for a generic soft-typed parameter
				value. NamedValue shall support two attributes. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NamedValuePropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 399, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/om/2.0}NamedValue uses Python identifier NamedValue
    __NamedValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NamedValue'), 'NamedValue', '__httpwww_opengis_netom2_0_NamedValuePropertyType_httpwww_opengis_netom2_0NamedValue', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 390, 1), )

    
    NamedValue = property(__NamedValue.value, __NamedValue.set, None, " The class 'NamedValue' provides for a generic soft-typed parameter\n\t\t\t\tvalue. NamedValue shall support two attributes. ")

    
    # Attribute {http://www.opengis.net/gml/3.2}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netom2_0_NamedValuePropertyType_httpwww_opengis_netgml3_2remoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/deprecatedTypes.xsd', 638, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 52, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, '')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netom2_0_NamedValuePropertyType_nilReason', pyxb.bundles.opengis.gml_3_2.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netom2_0_NamedValuePropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netom2_0_NamedValuePropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netom2_0_NamedValuePropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netom2_0_NamedValuePropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netom2_0_NamedValuePropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netom2_0_NamedValuePropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netom2_0_NamedValuePropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __NamedValue.name() : __NamedValue
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.NamedValuePropertyType = NamedValuePropertyType
Namespace.addCategoryObject('typeBinding', 'NamedValuePropertyType', NamedValuePropertyType)


# Complex type {http://www.opengis.net/om/2.0}TimeObjectPropertyType with content type ELEMENT_ONLY
class TimeObjectPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """This property type is not provided directly by GML"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeObjectPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 416, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}AbstractTimeObject uses Python identifier AbstractTimeObject
    __AbstractTimeObject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractTimeObject'), 'AbstractTimeObject', '__httpwww_opengis_netom2_0_TimeObjectPropertyType_httpwww_opengis_netgml3_2AbstractTimeObject', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/temporal.xsd', 18, 1), )

    
    AbstractTimeObject = property(__AbstractTimeObject.value, __AbstractTimeObject.set, None, 'gml:AbstractTimeObject acts as the head of a substitution group for all temporal primitives and complexes.')

    
    # Attribute {http://www.opengis.net/gml/3.2}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netom2_0_TimeObjectPropertyType_httpwww_opengis_netgml3_2remoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/deprecatedTypes.xsd', 638, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 52, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, '')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netom2_0_TimeObjectPropertyType_nilReason', pyxb.bundles.opengis.gml_3_2.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netom2_0_TimeObjectPropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netom2_0_TimeObjectPropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netom2_0_TimeObjectPropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netom2_0_TimeObjectPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netom2_0_TimeObjectPropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netom2_0_TimeObjectPropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netom2_0_TimeObjectPropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __AbstractTimeObject.name() : __AbstractTimeObject
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __nilReason.name() : __nilReason,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.TimeObjectPropertyType = TimeObjectPropertyType
Namespace.addCategoryObject('typeBinding', 'TimeObjectPropertyType', TimeObjectPropertyType)


result = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'result'), pyxb.binding.datatypes.anyType, documentation=' The association Range shall link the OM_Observation to the value\n\t\t\t\tgenerated by the procedure. The value has the role result with respect to the\n\t\t\t\tobservation. The type of the result is shown as Any, since it may represent the\n\t\t\t\tvalue of any feature property. NOTE 1 OGC SWE Common provides a model suitable for\n\t\t\t\tdescribing many kinds of observation results. The type of the observation result\n\t\t\t\tshall be consistent with the observed property, and the scale or scope for the value\n\t\t\t\tshall be consistent with the quantity or category type. If the observed property\n\t\t\t\t(6.2.2.8) is a spatial operation or function, the type of the result may be a\n\t\t\t\tcoverage, NOTE 2 In some contexts, particularly in earth and environmental sciences,\n\t\t\t\tthe term \u201cobservation\u201d is used to refer to the result itself. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 199, 1))
Namespace.addCategoryObject('elementBinding', result.name().localName(), result)

OM_Observation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OM_Observation'), OM_ObservationType, documentation='Observation is an act ("event"), whose result is an estimate of the value\n\t\t\t\tof a property of the feature of interest. The observed property may be any property\n\t\t\t\tassociated with the type of the feature of interest.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 242, 1))
Namespace.addCategoryObject('elementBinding', OM_Observation.name().localName(), OM_Observation)

ObservationContext = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObservationContext'), ObservationContextType, documentation=' Some observations depend on other observations to provide context which\n\t\t\t\tis important, sometimes essential, in understanding the result. These dependencies\n\t\t\t\tare stronger than mere spatiotemporal coincidences, requiring explicit\n\t\t\t\trepresentation. If present, the association class ObservationContext (Figure 2)\n\t\t\t\tshall link a OM_Observation to another OM_Observation, with the role name\n\t\t\t\trelatedObservation for the target. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 304, 1))
Namespace.addCategoryObject('elementBinding', ObservationContext.name().localName(), ObservationContext)

NamedValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NamedValue'), NamedValueType, documentation=" The class 'NamedValue' provides for a generic soft-typed parameter\n\t\t\t\tvalue. NamedValue shall support two attributes. ", location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 390, 1))
Namespace.addCategoryObject('elementBinding', NamedValue.name().localName(), NamedValue)



OM_ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=OM_ObservationType, documentation="If present, the sub-element 'type' shall indicate the class of\n\t\t\t\t\t\tobservation. A register of type identifiers corresponding with the\n\t\t\t\t\t\tobservation types in ISO 19156, which distinguishes types on the basis of\n\t\t\t\t\t\tthe type of the result, is provided by OGC at\n\t\t\t\t\t\thttp://www.opengis.net/def/observationType/OGC-OM/2.0/ ", location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 42, 3)))

OM_ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), pyxb.bundles.opengis.iso19139.v20070417.gmd.MD_Metadata_PropertyType, scope=OM_ObservationType, documentation=' If present, the association Metadata shall link the\n\t\t\t\t\t\tOM_Observation to descriptive metadata. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 54, 3)))

OM_ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relatedObservation'), ObservationContextPropertyType, scope=OM_ObservationType, documentation=' Some observations depend on other observations to provide\n\t\t\t\t\t\tcontext which is important, sometimes essential, in understanding the\n\t\t\t\t\t\tresult. These dependencies are stronger than mere spatiotemporal\n\t\t\t\t\t\tcoincidences, requiring explicit representation. If present, the association\n\t\t\t\t\t\tclass ObservationContext (Figure 2) shall link a OM_Observation to another\n\t\t\t\t\t\tOM_Observation, with the role name relatedObservation for the target.\n\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 63, 3)))

OM_ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'phenomenonTime'), TimeObjectPropertyType, scope=OM_ObservationType, documentation=' The attribute phenomenonTime:TM_Object shall describe the time\n\t\t\t\t\t\tthat the result (6.2.2.9) applies to the property of the feature-of-interest\n\t\t\t\t\t\t(6.2.2.7). This is often the time of interaction by a sampling procedure\n\t\t\t\t\t\t(8.1.3) or observation procedure (6.2.2.10) with a real-world feature.\n\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 78, 3)))

OM_ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'resultTime'), pyxb.bundles.opengis.gml_3_2.TimeInstantPropertyType, scope=OM_ObservationType, documentation=' The attribute resultTime:TM_Instant shall describe the time when\n\t\t\t\t\t\tthe result became available, typically when the procedure (6.2.2.10)\n\t\t\t\t\t\tassociated with the observation was completed For some observations this is\n\t\t\t\t\t\tidentical to the samplingTime. However, there are important cases where they\n\t\t\t\t\t\tdiffer. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 89, 3)))

OM_ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'validTime'), pyxb.bundles.opengis.gml_3_2.TimePeriodPropertyType, scope=OM_ObservationType, documentation=' If present, the attribute validTime:TM_Period shall describe the\n\t\t\t\t\t\ttime period during which the result is intended to be used. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 102, 3)))

OM_ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'procedure'), OM_ProcessPropertyType, nillable=pyxb.binding.datatypes.boolean(1), scope=OM_ObservationType, documentation=' The association ProcessUsed shall link the OM_Observation to the\n\t\t\t\t\t\tOM_Process (6.2.3) used to generate the result. The process has the role\n\t\t\t\t\t\tprocedure with respect to the observation. A process might be responsible\n\t\t\t\t\t\tfor more than one generatedObservation. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 111, 3)))

OM_ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameter'), NamedValuePropertyType, scope=OM_ObservationType, documentation=' If present, the attributes parameter:NamedValue shall describe\n\t\t\t\t\t\tan arbitrary event-specific parameter. This might be an environmental\n\t\t\t\t\t\tparameter, an instrument setting or input, or an event-specific sampling\n\t\t\t\t\t\tparameter that is not tightly bound to either the feature-of-interest\n\t\t\t\t\t\t(6.2.2.7) or to the observation procedure (6.2.2.10). To avoid ambiguity,\n\t\t\t\t\t\tthere shall be no more than one parameter with the same name. NOTE\n\t\t\t\t\t\tParameters that are tightly bound to the procedure may be recorded as part\n\t\t\t\t\t\tof the procedure description. In some contexts the Observation::procedure\n\t\t\t\t\t\t(6.2.2.10) is a generic or standard procedure, rather than an event-specific\n\t\t\t\t\t\tprocess. In this context, parameters bound to the observation act, such as\n\t\t\t\t\t\tinstrument settings, calibrations or inputs, local position, detection\n\t\t\t\t\t\tlimits, asset identifier, operator, may augment the description of a\n\t\t\t\t\t\tstandard procedure. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 122, 3)))

OM_ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'observedProperty'), pyxb.bundles.opengis.gml_3_2.ReferenceType, nillable=pyxb.binding.datatypes.boolean(1), scope=OM_ObservationType, documentation=' The association Phenomenon shall link the OM_Observation to the\n\t\t\t\t\t\tGFI_PropertyType (C.2.2) for which the OM_Observation:result (6.2.2.9)\n\t\t\t\t\t\tprovides an estimate of its value. The property type has the role\n\t\t\t\t\t\tobservedProperty with respect to the observation. The observed property\n\t\t\t\t\t\tshall be a phenomenon associated with the type of the featureOfInterest.\n\t\t\t\t\t\tNOTE An observed property may, but need not be modelled as a property (in\n\t\t\t\t\t\tthe sense of the General Feature Model) in a formal application schema that\n\t\t\t\t\t\tdefines the type of the feature of interest The observed property supports\n\t\t\t\t\t\tsemantic or thematic classification of observations, which is useful for\n\t\t\t\t\t\tdiscovery and data fusion. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 143, 3)))

OM_ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'featureOfInterest'), pyxb.bundles.opengis.gml_3_2.FeaturePropertyType, nillable=pyxb.binding.datatypes.boolean(1), scope=OM_ObservationType, documentation=' The association Domain shall link the OM_Observation to the\n\t\t\t\t\t\tGFI_Feature (C.2.1) that is the subject of the observation and carries the\n\t\t\t\t\t\tobserved property. This feature has the role featureOfInterest with respect\n\t\t\t\t\t\tto the observation. This feature is the real-world object whose properties\n\t\t\t\t\t\tare under observation, or is a feature intended to sample the real-world\n\t\t\t\t\t\tobject, as described in Clause 8 of this International Standard. An\n\t\t\t\t\t\tobservation instance serves as a propertyValueProvider for its feature of\n\t\t\t\t\t\tinterest. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 163, 3)))

OM_ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'resultQuality'), pyxb.bundles.opengis.iso19139.v20070417.gmd.DQ_Element_PropertyType, scope=OM_ObservationType, documentation=' If present, the attributes resultQuality:DQ_Element shall\n\t\t\t\t\t\tdescribe the quality of the result (6.2.2.9). This instance-specific\n\t\t\t\t\t\tdescription complements the description of the observation procedure\n\t\t\t\t\t\t(6.2.2.10), which provides information concerning the quality of all\n\t\t\t\t\t\tobservations using this procedure. Quality of a result may be assessed\n\t\t\t\t\t\tfollowing the procedures in ISO 19114:2003. Multiple measures may be\n\t\t\t\t\t\tprovided (ISO/TS 19138:2006). ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 178, 3)))

OM_ObservationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'result'), pyxb.binding.datatypes.anyType, scope=OM_ObservationType, documentation=' The association Range shall link the OM_Observation to the value\n\t\t\t\tgenerated by the procedure. The value has the role result with respect to the\n\t\t\t\tobservation. The type of the result is shown as Any, since it may represent the\n\t\t\t\tvalue of any feature property. NOTE 1 OGC SWE Common provides a model suitable for\n\t\t\t\tdescribing many kinds of observation results. The type of the observation result\n\t\t\t\tshall be consistent with the observed property, and the scale or scope for the value\n\t\t\t\tshall be consistent with the quantity or category type. If the observed property\n\t\t\t\t(6.2.2.8) is a spatial operation or function, the type of the result may be a\n\t\t\t\tcoverage, NOTE 2 In some contexts, particularly in earth and environmental sciences,\n\t\t\t\tthe term \u201cobservation\u201d is used to refer to the result itself. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 199, 1)))

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
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 42, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 54, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 63, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 102, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 122, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 178, 3))
    counters.add(cc_12)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 26, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 27, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 42, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 54, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relatedObservation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 63, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'phenomenonTime')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 78, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'resultTime')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 89, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validTime')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 102, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'procedure')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 111, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameter')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 122, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'observedProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 143, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'featureOfInterest')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 163, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'resultQuality')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 178, 3))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OM_ObservationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'result')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 235, 5))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
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
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    st_18._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OM_ObservationType._Automaton = _BuildAutomaton()




OM_ObservationPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OM_Observation'), OM_ObservationType, scope=OM_ObservationPropertyType, documentation='Observation is an act ("event"), whose result is an estimate of the value\n\t\t\t\tof a property of the feature of interest. The observed property may be any property\n\t\t\t\tassociated with the type of the feature of interest.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 242, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 255, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OM_ObservationPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OM_Observation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 257, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
OM_ObservationPropertyType._Automaton = _BuildAutomaton_()




ObservationContextType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'role'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=ObservationContextType, documentation="The attribute 'role' shall describe the relationship of the\n\t\t\t\t\t\ttarget OM_Observation to the source OM_Observation. ", location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 277, 3)))

ObservationContextType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relatedObservation'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=ObservationContextType, documentation=' Some observations depend on other observations to provide\n\t\t\t\t\t\tcontext which is important, sometimes essential, in understanding the\n\t\t\t\t\t\tresult. These dependencies are stronger than mere spatiotemporal\n\t\t\t\t\t\tcoincidences, requiring explicit representation. If present, the association\n\t\t\t\t\t\tclass ObservationContext (Figure 2) shall link a OM_Observation to another\n\t\t\t\t\t\tOM_Observation, with the role name relatedObservation for the target.\n\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 285, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationContextType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'role')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 277, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ObservationContextType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relatedObservation')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 285, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ObservationContextType._Automaton = _BuildAutomaton_2()




ObservationContextPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObservationContext'), ObservationContextType, scope=ObservationContextPropertyType, documentation=' Some observations depend on other observations to provide context which\n\t\t\t\tis important, sometimes essential, in understanding the result. These dependencies\n\t\t\t\tare stronger than mere spatiotemporal coincidences, requiring explicit\n\t\t\t\trepresentation. If present, the association class ObservationContext (Figure 2)\n\t\t\t\tshall link a OM_Observation to another OM_Observation, with the role name\n\t\t\t\trelatedObservation for the target. ', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 304, 1)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ObservationContextPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ObservationContext')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 324, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ObservationContextPropertyType._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 345, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 347, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
OM_ProcessPropertyType._Automaton = _BuildAutomaton_4()




NamedValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.bundles.opengis.gml_3_2.ReferenceType, scope=NamedValueType, documentation=" The attribute 'name' shall indicate the meaning of the named\n\t\t\t\t\t\tvalue. Its value should be taken from a well-governed source if possible.\n\t\t\t\t\t", location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 370, 3)))

NamedValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), pyxb.binding.datatypes.anyType, scope=NamedValueType, documentation=" The attribute 'value' shall provide the value. The type Any\n\t\t\t\t\t\tshould be substituted by a suitable concrete type, such as\n\t\t\t\t\t\tCI_ResponsibleParty or Measure. ", location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 379, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(NamedValueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 370, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NamedValueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 379, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
NamedValueType._Automaton = _BuildAutomaton_5()




NamedValuePropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NamedValue'), NamedValueType, scope=NamedValuePropertyType, documentation=" The class 'NamedValue' provides for a generic soft-typed parameter\n\t\t\t\tvalue. NamedValue shall support two attributes. ", location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 390, 1)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 405, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NamedValuePropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NamedValue')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 407, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NamedValuePropertyType._Automaton = _BuildAutomaton_6()




TimeObjectPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractTimeObject'), pyxb.bundles.opengis.gml_3_2.AbstractTimeObjectType, abstract=pyxb.binding.datatypes.boolean(1), scope=TimeObjectPropertyType, documentation='gml:AbstractTimeObject acts as the head of a substitution group for all temporal primitives and complexes.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/temporal.xsd', 18, 1)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 421, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TimeObjectPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'AbstractTimeObject')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/om/2.0/observation.xsd', 423, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TimeObjectPropertyType._Automaton = _BuildAutomaton_7()


OM_Observation._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_2.AbstractFeature)
