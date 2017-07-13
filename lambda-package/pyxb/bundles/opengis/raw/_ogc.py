# ./pyxb/bundles/opengis/raw/_ogc.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:5b31a14669a98cd6cc4f3673117954e87b7d869b
# Generated 2017-07-10 00:37:15.514279 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/ogc [xmlns:ogc]

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
import pyxb.binding.datatypes
import pyxb.bundles.opengis.gml
import pyxb.bundles.opengis.filter

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/ogc', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gml = pyxb.namespace.NamespaceForURI('http://www.opengis.net/gml', create_if_missing=True)
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


# Atomic simple type: {http://www.opengis.net/ogc}TemporalOperandType
class TemporalOperandType (pyxb.binding.datatypes.QName, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TemporalOperandType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 60, 2)
    _Documentation = None
TemporalOperandType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TemporalOperandType, enum_prefix=None)
TemporalOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'validTime'), tag=None)
TemporalOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'TimeInstant'), tag=None)
TemporalOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'TimePeriod'), tag=None)
TemporalOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'timePosition'), tag=None)
TemporalOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'timeInterval'), tag=None)
TemporalOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'duration'), tag=None)
TemporalOperandType._InitializeFacetMap(TemporalOperandType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TemporalOperandType', TemporalOperandType)
_module_typeBindings.TemporalOperandType = TemporalOperandType

# Atomic simple type: {http://www.opengis.net/ogc}TemporalOperatorNameType
class TemporalOperatorNameType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TemporalOperatorNameType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 81, 2)
    _Documentation = None
TemporalOperatorNameType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TemporalOperatorNameType, enum_prefix=None)
TemporalOperatorNameType.TM_After = TemporalOperatorNameType._CF_enumeration.addEnumeration(unicode_value='TM_After', tag='TM_After')
TemporalOperatorNameType.TM_Before = TemporalOperatorNameType._CF_enumeration.addEnumeration(unicode_value='TM_Before', tag='TM_Before')
TemporalOperatorNameType.TM_Begins = TemporalOperatorNameType._CF_enumeration.addEnumeration(unicode_value='TM_Begins', tag='TM_Begins')
TemporalOperatorNameType.TM_BegunBy = TemporalOperatorNameType._CF_enumeration.addEnumeration(unicode_value='TM_BegunBy', tag='TM_BegunBy')
TemporalOperatorNameType.TM_Contains = TemporalOperatorNameType._CF_enumeration.addEnumeration(unicode_value='TM_Contains', tag='TM_Contains')
TemporalOperatorNameType.TM_During = TemporalOperatorNameType._CF_enumeration.addEnumeration(unicode_value='TM_During', tag='TM_During')
TemporalOperatorNameType.TM_Equals = TemporalOperatorNameType._CF_enumeration.addEnumeration(unicode_value='TM_Equals', tag='TM_Equals')
TemporalOperatorNameType.TM_Overlaps = TemporalOperatorNameType._CF_enumeration.addEnumeration(unicode_value='TM_Overlaps', tag='TM_Overlaps')
TemporalOperatorNameType.TM_Meets = TemporalOperatorNameType._CF_enumeration.addEnumeration(unicode_value='TM_Meets', tag='TM_Meets')
TemporalOperatorNameType.TM_OverlappedBy = TemporalOperatorNameType._CF_enumeration.addEnumeration(unicode_value='TM_OverlappedBy', tag='TM_OverlappedBy')
TemporalOperatorNameType.TM_MetBy = TemporalOperatorNameType._CF_enumeration.addEnumeration(unicode_value='TM_MetBy', tag='TM_MetBy')
TemporalOperatorNameType.TM_EndedBy = TemporalOperatorNameType._CF_enumeration.addEnumeration(unicode_value='TM_EndedBy', tag='TM_EndedBy')
TemporalOperatorNameType.TM_Ends = TemporalOperatorNameType._CF_enumeration.addEnumeration(unicode_value='TM_Ends', tag='TM_Ends')
TemporalOperatorNameType._InitializeFacetMap(TemporalOperatorNameType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TemporalOperatorNameType', TemporalOperatorNameType)
_module_typeBindings.TemporalOperatorNameType = TemporalOperatorNameType

# Complex type {http://www.opengis.net/ogc}TemporalOpsType with content type EMPTY
class TemporalOpsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}TemporalOpsType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TemporalOpsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 22, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TemporalOpsType = TemporalOpsType
Namespace.addCategoryObject('typeBinding', 'TemporalOpsType', TemporalOpsType)


# Complex type {http://www.opengis.net/ogc}Temporal_CapabilitiesType with content type ELEMENT_ONLY
class Temporal_CapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}Temporal_CapabilitiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Temporal_CapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 49, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}TemporalOperands uses Python identifier TemporalOperands
    __TemporalOperands = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperands'), 'TemporalOperands', '__httpwww_opengis_netogc_Temporal_CapabilitiesType_httpwww_opengis_netogcTemporalOperands', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 51, 6), )

    
    TemporalOperands = property(__TemporalOperands.value, __TemporalOperands.set, None, None)

    
    # Element {http://www.opengis.net/ogc}TemporalOperators uses Python identifier TemporalOperators
    __TemporalOperators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperators'), 'TemporalOperators', '__httpwww_opengis_netogc_Temporal_CapabilitiesType_httpwww_opengis_netogcTemporalOperators', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 52, 6), )

    
    TemporalOperators = property(__TemporalOperators.value, __TemporalOperators.set, None, None)

    _ElementMap.update({
        __TemporalOperands.name() : __TemporalOperands,
        __TemporalOperators.name() : __TemporalOperators
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Temporal_CapabilitiesType = Temporal_CapabilitiesType
Namespace.addCategoryObject('typeBinding', 'Temporal_CapabilitiesType', Temporal_CapabilitiesType)


# Complex type {http://www.opengis.net/ogc}TemporalOperandsType with content type ELEMENT_ONLY
class TemporalOperandsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}TemporalOperandsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TemporalOperandsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 55, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}TemporalOperand uses Python identifier TemporalOperand
    __TemporalOperand = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperand'), 'TemporalOperand', '__httpwww_opengis_netogc_TemporalOperandsType_httpwww_opengis_netogcTemporalOperand', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 57, 6), )

    
    TemporalOperand = property(__TemporalOperand.value, __TemporalOperand.set, None, None)

    _ElementMap.update({
        __TemporalOperand.name() : __TemporalOperand
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TemporalOperandsType = TemporalOperandsType
Namespace.addCategoryObject('typeBinding', 'TemporalOperandsType', TemporalOperandsType)


# Complex type {http://www.opengis.net/ogc}TemporalOperatorsType with content type ELEMENT_ONLY
class TemporalOperatorsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}TemporalOperatorsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TemporalOperatorsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 70, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}TemporalOperator uses Python identifier TemporalOperator
    __TemporalOperator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperator'), 'TemporalOperator', '__httpwww_opengis_netogc_TemporalOperatorsType_httpwww_opengis_netogcTemporalOperator', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 72, 6), )

    
    TemporalOperator = property(__TemporalOperator.value, __TemporalOperator.set, None, None)

    _ElementMap.update({
        __TemporalOperator.name() : __TemporalOperator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TemporalOperatorsType = TemporalOperatorsType
Namespace.addCategoryObject('typeBinding', 'TemporalOperatorsType', TemporalOperatorsType)


# Complex type {http://www.opengis.net/ogc}BinaryTemporalOpType with content type ELEMENT_ONLY
class BinaryTemporalOpType (TemporalOpsType):
    """Complex type {http://www.opengis.net/ogc}BinaryTemporalOpType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BinaryTemporalOpType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 36, 2)
    _ElementMap = TemporalOpsType._ElementMap.copy()
    _AttributeMap = TemporalOpsType._AttributeMap.copy()
    # Base type is TemporalOpsType
    
    # Element {http://www.opengis.net/gml}_TimeObject uses Python identifier TimeObject
    __TimeObject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, '_TimeObject'), 'TimeObject', '__httpwww_opengis_netogc_BinaryTemporalOpType_httpwww_opengis_netgml_TimeObject', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/temporal.xsd', 19, 1), )

    
    TimeObject = property(__TimeObject.value, __TimeObject.set, None, 'This abstract element acts as the head of the substitution group for temporal primitives and complexes.')

    
    # Element {http://www.opengis.net/ogc}PropertyName uses Python identifier PropertyName
    __PropertyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), 'PropertyName', '__httpwww_opengis_netogc_BinaryTemporalOpType_httpwww_opengis_netogcPropertyName', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 23, 3), )

    
    PropertyName = property(__PropertyName.value, __PropertyName.set, None, None)

    _ElementMap.update({
        __TimeObject.name() : __TimeObject,
        __PropertyName.name() : __PropertyName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BinaryTemporalOpType = BinaryTemporalOpType
Namespace.addCategoryObject('typeBinding', 'BinaryTemporalOpType', BinaryTemporalOpType)


# Complex type {http://www.opengis.net/ogc}TemporalOperatorType with content type ELEMENT_ONLY
class TemporalOperatorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}TemporalOperatorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TemporalOperatorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 75, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}TemporalOperands uses Python identifier TemporalOperands
    __TemporalOperands = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperands'), 'TemporalOperands', '__httpwww_opengis_netogc_TemporalOperatorType_httpwww_opengis_netogcTemporalOperands', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 77, 6), )

    
    TemporalOperands = property(__TemporalOperands.value, __TemporalOperands.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netogc_TemporalOperatorType_name', _module_typeBindings.TemporalOperatorNameType)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 79, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 79, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __TemporalOperands.name() : __TemporalOperands
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.TemporalOperatorType = TemporalOperatorType
Namespace.addCategoryObject('typeBinding', 'TemporalOperatorType', TemporalOperatorType)


Spatial_Capabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Spatial_Capabilities'), pyxb.bundles.opengis.filter.Spatial_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 99, 2))
Namespace.addCategoryObject('elementBinding', Spatial_Capabilities.name().localName(), Spatial_Capabilities)

Scalar_Capabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Scalar_Capabilities'), pyxb.bundles.opengis.filter.Scalar_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 100, 2))
Namespace.addCategoryObject('elementBinding', Scalar_Capabilities.name().localName(), Scalar_Capabilities)

Id_Capabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id_Capabilities'), pyxb.bundles.opengis.filter.Id_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 101, 2))
Namespace.addCategoryObject('elementBinding', Id_Capabilities.name().localName(), Id_Capabilities)

temporalOps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'temporalOps'), TemporalOpsType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 21, 2))
Namespace.addCategoryObject('elementBinding', temporalOps.name().localName(), temporalOps)

Temporal_Capabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Temporal_Capabilities'), Temporal_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 102, 2))
Namespace.addCategoryObject('elementBinding', Temporal_Capabilities.name().localName(), Temporal_Capabilities)

TM_After = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TM_After'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 23, 2))
Namespace.addCategoryObject('elementBinding', TM_After.name().localName(), TM_After)

TM_Before = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TM_Before'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 24, 2))
Namespace.addCategoryObject('elementBinding', TM_Before.name().localName(), TM_Before)

TM_Begins = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TM_Begins'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 25, 2))
Namespace.addCategoryObject('elementBinding', TM_Begins.name().localName(), TM_Begins)

TM_BegunBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TM_BegunBy'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 26, 2))
Namespace.addCategoryObject('elementBinding', TM_BegunBy.name().localName(), TM_BegunBy)

TM_Contains = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TM_Contains'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 27, 2))
Namespace.addCategoryObject('elementBinding', TM_Contains.name().localName(), TM_Contains)

TM_During = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TM_During'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 28, 2))
Namespace.addCategoryObject('elementBinding', TM_During.name().localName(), TM_During)

TM_EndedBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TM_EndedBy'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 29, 2))
Namespace.addCategoryObject('elementBinding', TM_EndedBy.name().localName(), TM_EndedBy)

TM_Ends = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TM_Ends'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 30, 2))
Namespace.addCategoryObject('elementBinding', TM_Ends.name().localName(), TM_Ends)

TM_Equals = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TM_Equals'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 31, 2))
Namespace.addCategoryObject('elementBinding', TM_Equals.name().localName(), TM_Equals)

TM_Meets = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TM_Meets'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 32, 2))
Namespace.addCategoryObject('elementBinding', TM_Meets.name().localName(), TM_Meets)

TM_MetBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TM_MetBy'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 33, 2))
Namespace.addCategoryObject('elementBinding', TM_MetBy.name().localName(), TM_MetBy)

TM_Overalps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TM_Overalps'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 34, 2))
Namespace.addCategoryObject('elementBinding', TM_Overalps.name().localName(), TM_Overalps)

TM_OverlappedBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TM_OverlappedBy'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 35, 2))
Namespace.addCategoryObject('elementBinding', TM_OverlappedBy.name().localName(), TM_OverlappedBy)



Temporal_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperands'), TemporalOperandsType, scope=Temporal_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 51, 6)))

Temporal_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperators'), TemporalOperatorsType, scope=Temporal_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 52, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Temporal_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperands')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 51, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Temporal_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperators')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 52, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Temporal_CapabilitiesType._Automaton = _BuildAutomaton()




TemporalOperandsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperand'), TemporalOperandType, scope=TemporalOperandsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 57, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TemporalOperandsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperand')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 57, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TemporalOperandsType._Automaton = _BuildAutomaton_()




TemporalOperatorsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperator'), TemporalOperatorType, scope=TemporalOperatorsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 72, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TemporalOperatorsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperator')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 72, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TemporalOperatorsType._Automaton = _BuildAutomaton_2()




BinaryTemporalOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, '_TimeObject'), pyxb.bundles.opengis.gml.AbstractTimeObjectType, abstract=pyxb.binding.datatypes.boolean(1), scope=BinaryTemporalOpType, documentation='This abstract element acts as the head of the substitution group for temporal primitives and complexes.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/temporal.xsd', 19, 1)))

BinaryTemporalOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), pyxb.bundles.opengis.filter.PropertyNameType, scope=BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 23, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BinaryTemporalOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PropertyName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 40, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BinaryTemporalOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PropertyName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 42, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BinaryTemporalOpType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, '_TimeObject')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 43, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BinaryTemporalOpType._Automaton = _BuildAutomaton_3()




TemporalOperatorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperands'), TemporalOperandsType, scope=TemporalOperatorType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 77, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 77, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TemporalOperatorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperands')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/sos/1.0.0/ogc4sos.xsd', 77, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TemporalOperatorType._Automaton = _BuildAutomaton_4()


TM_After._setSubstitutionGroup(temporalOps)

TM_Before._setSubstitutionGroup(temporalOps)

TM_Begins._setSubstitutionGroup(temporalOps)

TM_BegunBy._setSubstitutionGroup(temporalOps)

TM_Contains._setSubstitutionGroup(temporalOps)

TM_During._setSubstitutionGroup(temporalOps)

TM_EndedBy._setSubstitutionGroup(temporalOps)

TM_Ends._setSubstitutionGroup(temporalOps)

TM_Equals._setSubstitutionGroup(temporalOps)

TM_Meets._setSubstitutionGroup(temporalOps)

TM_MetBy._setSubstitutionGroup(temporalOps)

TM_Overalps._setSubstitutionGroup(temporalOps)

TM_OverlappedBy._setSubstitutionGroup(temporalOps)
