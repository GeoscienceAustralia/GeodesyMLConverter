# ./pyxb/bundles/opengis/gml_3_3/raw/tin.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:fe87b9fed1198ebfac663950c06d9b9dd8690d3e
# Generated 2017-07-10 00:38:05.932589 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/gml/3.3/tin

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:08b5e8b2-6508-11e7-ae71-0a55f9edafa5')

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
import pyxb.binding.datatypes
import pyxb.bundles.opengis.gml_3_2

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/gml/3.3/tin', create_if_missing=True)
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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 56, 6)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.randomPoints = STD_ANON._CF_enumeration.addEnumeration(unicode_value='randomPoints', tag='randomPoints')
STD_ANON.groupSpot = STD_ANON._CF_enumeration.addEnumeration(unicode_value='groupSpot', tag='groupSpot')
STD_ANON.boundary = STD_ANON._CF_enumeration.addEnumeration(unicode_value='boundary', tag='boundary')
STD_ANON.breakline = STD_ANON._CF_enumeration.addEnumeration(unicode_value='breakline', tag='breakline')
STD_ANON.softBreak = STD_ANON._CF_enumeration.addEnumeration(unicode_value='softBreak', tag='softBreak')
STD_ANON.controlContour = STD_ANON._CF_enumeration.addEnumeration(unicode_value='controlContour', tag='controlContour')
STD_ANON.breakVoid = STD_ANON._CF_enumeration.addEnumeration(unicode_value='breakVoid', tag='breakVoid')
STD_ANON.drapeVoid = STD_ANON._CF_enumeration.addEnumeration(unicode_value='drapeVoid', tag='drapeVoid')
STD_ANON.void = STD_ANON._CF_enumeration.addEnumeration(unicode_value='void', tag='void')
STD_ANON.hole = STD_ANON._CF_enumeration.addEnumeration(unicode_value='hole', tag='hole')
STD_ANON.stopLine = STD_ANON._CF_enumeration.addEnumeration(unicode_value='stopLine', tag='stopLine')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 71, 6)
    _Documentation = None
STD_ANON_._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_._CF_pattern.addPattern(pattern='other:\\w{2,}')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_pattern)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Union simple type: {http://www.opengis.net/gml/3.3/tin}TINElementTypeType
# superclasses pyxb.binding.datatypes.anySimpleType
class TINElementTypeType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of STD_ANON, STD_ANON_."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TINElementTypeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 54, 2)
    _Documentation = None

    _MemberTypes = ( STD_ANON, STD_ANON_, )
TINElementTypeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TINElementTypeType)
TINElementTypeType._CF_pattern = pyxb.binding.facets.CF_pattern()
TINElementTypeType.randomPoints = 'randomPoints'  # originally STD_ANON.randomPoints
TINElementTypeType.groupSpot = 'groupSpot'        # originally STD_ANON.groupSpot
TINElementTypeType.boundary = 'boundary'          # originally STD_ANON.boundary
TINElementTypeType.breakline = 'breakline'        # originally STD_ANON.breakline
TINElementTypeType.softBreak = 'softBreak'        # originally STD_ANON.softBreak
TINElementTypeType.controlContour = 'controlContour'# originally STD_ANON.controlContour
TINElementTypeType.breakVoid = 'breakVoid'        # originally STD_ANON.breakVoid
TINElementTypeType.drapeVoid = 'drapeVoid'        # originally STD_ANON.drapeVoid
TINElementTypeType.void = 'void'                  # originally STD_ANON.void
TINElementTypeType.hole = 'hole'                  # originally STD_ANON.hole
TINElementTypeType.stopLine = 'stopLine'          # originally STD_ANON.stopLine
TINElementTypeType._InitializeFacetMap(TINElementTypeType._CF_enumeration,
   TINElementTypeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TINElementTypeType', TINElementTypeType)
_module_typeBindings.TINElementTypeType = TINElementTypeType

# Complex type {http://www.opengis.net/gml/3.3/tin}SimpleTrianglePatchType with content type ELEMENT_ONLY
class SimpleTrianglePatchType (pyxb.bundles.opengis.gml_3_2.AbstractSurfacePatchType):
    """Complex type {http://www.opengis.net/gml/3.3/tin}SimpleTrianglePatchType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleTrianglePatchType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 7, 2)
    _ElementMap = pyxb.bundles.opengis.gml_3_2.AbstractSurfacePatchType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_2.AbstractSurfacePatchType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_2.AbstractSurfacePatchType
    
    # Element {http://www.opengis.net/gml/3.2}pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), 'pos', '__httpwww_opengis_netgml3_3tin_SimpleTrianglePatchType_httpwww_opengis_netgml3_2pos', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1), )

    
    pos = property(__pos.value, __pos.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}posList uses Python identifier posList
    __posList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), 'posList', '__httpwww_opengis_netgml3_3tin_SimpleTrianglePatchType_httpwww_opengis_netgml3_2posList', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1), )

    
    posList = property(__posList.value, __posList.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}pointProperty uses Python identifier pointProperty
    __pointProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), 'pointProperty', '__httpwww_opengis_netgml3_3tin_SimpleTrianglePatchType_httpwww_opengis_netgml3_2pointProperty', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1), )

    
    pointProperty = property(__pointProperty.value, __pointProperty.set, None, 'This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.')

    
    # Attribute interpolation uses Python identifier interpolation
    __interpolation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'interpolation'), 'interpolation', '__httpwww_opengis_netgml3_3tin_SimpleTrianglePatchType_interpolation', pyxb.bundles.opengis.gml_3_2.SurfaceInterpolationType, fixed=True, unicode_default='planar')
    __interpolation._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 19, 8)
    __interpolation._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 19, 8)
    
    interpolation = property(__interpolation.value, __interpolation.set, None, None)

    _ElementMap.update({
        __pos.name() : __pos,
        __posList.name() : __posList,
        __pointProperty.name() : __pointProperty
    })
    _AttributeMap.update({
        __interpolation.name() : __interpolation
    })
_module_typeBindings.SimpleTrianglePatchType = SimpleTrianglePatchType
Namespace.addCategoryObject('typeBinding', 'SimpleTrianglePatchType', SimpleTrianglePatchType)


# Complex type {http://www.opengis.net/gml/3.3/tin}TINType with content type ELEMENT_ONLY
class TINType (pyxb.bundles.opengis.gml_3_2.SurfaceType):
    """Complex type {http://www.opengis.net/gml/3.3/tin}TINType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TINType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 24, 2)
    _ElementMap = pyxb.bundles.opengis.gml_3_2.SurfaceType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_2.SurfaceType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_2.SurfaceType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element patches ({http://www.opengis.net/gml/3.2}patches) inherited from {http://www.opengis.net/gml/3.2}SurfaceType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/gml/3.3/tin}tinElement uses Python identifier tinElement
    __tinElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tinElement'), 'tinElement', '__httpwww_opengis_netgml3_3tin_TINType_httpwww_opengis_netgml3_3tintinElement', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 28, 10), )

    
    tinElement = property(__tinElement.value, __tinElement.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.3/tin}maxLength uses Python identifier maxLength
    __maxLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maxLength'), 'maxLength', '__httpwww_opengis_netgml3_3tin_TINType_httpwww_opengis_netgml3_3tinmaxLength', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 29, 10), )

    
    maxLength = property(__maxLength.value, __maxLength.set, None, None)

    
    # Attribute srsName inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute srsDimension inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute axisLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute uomLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    _ElementMap.update({
        __tinElement.name() : __tinElement,
        __maxLength.name() : __maxLength
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TINType = TINType
Namespace.addCategoryObject('typeBinding', 'TINType', TINType)


# Complex type {http://www.opengis.net/gml/3.3/tin}TINElementType with content type ELEMENT_ONLY
class TINElementType (pyxb.bundles.opengis.gml_3_2.AbstractFeatureType):
    """Complex type {http://www.opengis.net/gml/3.3/tin}TINElementType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TINElementType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 35, 2)
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
    
    # Element {http://www.opengis.net/gml/3.3/tin}elementType uses Python identifier elementType
    __elementType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'elementType'), 'elementType', '__httpwww_opengis_netgml3_3tin_TINElementType_httpwww_opengis_netgml3_3tinelementType', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 39, 10), )

    
    elementType = property(__elementType.value, __elementType.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.3/tin}elementID uses Python identifier elementID
    __elementID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'elementID'), 'elementID', '__httpwww_opengis_netgml3_3tin_TINElementType_httpwww_opengis_netgml3_3tinelementID', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 40, 10), )

    
    elementID = property(__elementID.value, __elementID.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.3/tin}elementTag uses Python identifier elementTag
    __elementTag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'elementTag'), 'elementTag', '__httpwww_opengis_netgml3_3tin_TINElementType_httpwww_opengis_netgml3_3tinelementTag', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 41, 10), )

    
    elementTag = property(__elementTag.value, __elementTag.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.3/tin}elementGeometry uses Python identifier elementGeometry
    __elementGeometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'elementGeometry'), 'elementGeometry', '__httpwww_opengis_netgml3_3tin_TINElementType_httpwww_opengis_netgml3_3tinelementGeometry', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 42, 10), )

    
    elementGeometry = property(__elementGeometry.value, __elementGeometry.set, None, None)

    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    _ElementMap.update({
        __elementType.name() : __elementType,
        __elementID.name() : __elementID,
        __elementTag.name() : __elementTag,
        __elementGeometry.name() : __elementGeometry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TINElementType = TINElementType
Namespace.addCategoryObject('typeBinding', 'TINElementType', TINElementType)


# Complex type {http://www.opengis.net/gml/3.3/tin}TINElementPropertyType with content type ELEMENT_ONLY
class TINElementPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/gml/3.3/tin}TINElementPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TINElementPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 48, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.3/tin}TINElement uses Python identifier TINElement
    __TINElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TINElement'), 'TINElement', '__httpwww_opengis_netgml3_3tin_TINElementPropertyType_httpwww_opengis_netgml3_3tinTINElement', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 47, 2), )

    
    TINElement = property(__TINElement.value, __TINElement.set, None, None)

    
    # Attribute {http://www.opengis.net/gml/3.2}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netgml3_3tin_TINElementPropertyType_httpwww_opengis_netgml3_2remoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/deprecatedTypes.xsd', 638, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 52, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, '')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_3tin_TINElementPropertyType_nilReason', pyxb.bundles.opengis.gml_3_2.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netgml3_3tin_TINElementPropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netgml3_3tin_TINElementPropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netgml3_3tin_TINElementPropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_3tin_TINElementPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netgml3_3tin_TINElementPropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netgml3_3tin_TINElementPropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_3tin_TINElementPropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __TINElement.name() : __TINElement
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
_module_typeBindings.TINElementPropertyType = TINElementPropertyType
Namespace.addCategoryObject('typeBinding', 'TINElementPropertyType', TINElementPropertyType)


TriangulatedSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TriangulatedSurface'), pyxb.bundles.opengis.gml_3_2.SurfaceType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 6, 2))
Namespace.addCategoryObject('elementBinding', TriangulatedSurface.name().localName(), TriangulatedSurface)

SimpleTrianglePatch = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleTrianglePatch'), SimpleTrianglePatchType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 23, 2))
Namespace.addCategoryObject('elementBinding', SimpleTrianglePatch.name().localName(), SimpleTrianglePatch)

TIN = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TIN'), TINType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 34, 2))
Namespace.addCategoryObject('elementBinding', TIN.name().localName(), TIN)

TINElement = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TINElement'), TINElementType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 47, 2))
Namespace.addCategoryObject('elementBinding', TINElement.name().localName(), TINElement)



SimpleTrianglePatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), pyxb.bundles.opengis.gml_3_2.DirectPositionType, scope=SimpleTrianglePatchType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1)))

SimpleTrianglePatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), pyxb.bundles.opengis.gml_3_2.DirectPositionListType, scope=SimpleTrianglePatchType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1)))

SimpleTrianglePatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), pyxb.bundles.opengis.gml_3_2.PointPropertyType, scope=SimpleTrianglePatchType, documentation='This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=3, max=3, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 12, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SimpleTrianglePatchType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 13, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SimpleTrianglePatchType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 14, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleTrianglePatchType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 16, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
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
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SimpleTrianglePatchType._Automaton = _BuildAutomaton()




TINType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tinElement'), TINElementPropertyType, scope=TINType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 28, 10)))

TINType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maxLength'), pyxb.bundles.opengis.gml_3_2.LengthType, scope=TINType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 29, 10)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
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
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 28, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 29, 10))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TINType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'patches')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryPrimitives.xsd', 502, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TINType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tinElement')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 28, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TINType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maxLength')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 29, 10))
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
TINType._Automaton = _BuildAutomaton_()




TINElementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'elementType'), TINElementTypeType, scope=TINElementType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 39, 10)))

TINElementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'elementID'), pyxb.binding.datatypes.integer, scope=TINElementType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 40, 10)))

TINElementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'elementTag'), pyxb.binding.datatypes.string, scope=TINElementType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 41, 10)))

TINElementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'elementGeometry'), pyxb.bundles.opengis.gml_3_2.GeometryPropertyType, scope=TINElementType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 42, 10)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
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
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 40, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 41, 10))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINElementType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINElementType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINElementType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINElementType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINElementType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINElementType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 26, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINElementType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/feature.xsd', 27, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINElementType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'elementType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 39, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINElementType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'elementID')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 40, 10))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINElementType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'elementTag')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 41, 10))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TINElementType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'elementGeometry')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 42, 10))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
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
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TINElementType._Automaton = _BuildAutomaton_2()




TINElementPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TINElement'), TINElementType, scope=TINElementPropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 47, 2)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 49, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TINElementPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TINElement')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/tin.xsd', 50, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TINElementPropertyType._Automaton = _BuildAutomaton_3()


TriangulatedSurface._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_2.Surface)

SimpleTrianglePatch._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_2.AbstractSurfacePatch)

TIN._setSubstitutionGroup(TriangulatedSurface)

TINElement._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_2.AbstractObject)
