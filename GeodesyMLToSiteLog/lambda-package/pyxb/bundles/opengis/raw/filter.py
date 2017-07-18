# ./pyxb/bundles/opengis/raw/filter.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:5b31a14669a98cd6cc4f3673117954e87b7d869b
# Generated 2017-07-10 00:36:51.218833 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/ogc

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:dcc7cee6-6507-11e7-93b9-0a55f9edafa5')

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


# Atomic simple type: {http://www.opengis.net/ogc}GeometryOperandType
class GeometryOperandType (pyxb.binding.datatypes.QName, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeometryOperandType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 46, 3)
    _Documentation = None
GeometryOperandType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=GeometryOperandType, enum_prefix=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'Envelope'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'Point'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'LineString'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'Polygon'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'ArcByCenterPoint'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'CircleByCenterPoint'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'Arc'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'Circle'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'ArcByBulge'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'Bezier'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'Clothoid'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'CubicSpline'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'Geodesic'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'OffsetCurve'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'Triangle'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'PolyhedralSurface'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'TriangulatedSurface'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'Tin'), tag=None)
GeometryOperandType._CF_enumeration.addEnumeration(value=pyxb.namespace.ExpandedName(_Namespace_gml, 'Solid'), tag=None)
GeometryOperandType._InitializeFacetMap(GeometryOperandType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'GeometryOperandType', GeometryOperandType)
_module_typeBindings.GeometryOperandType = GeometryOperandType

# Atomic simple type: {http://www.opengis.net/ogc}SpatialOperatorNameType
class SpatialOperatorNameType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpatialOperatorNameType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 84, 3)
    _Documentation = None
SpatialOperatorNameType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SpatialOperatorNameType, enum_prefix=None)
SpatialOperatorNameType.BBOX = SpatialOperatorNameType._CF_enumeration.addEnumeration(unicode_value='BBOX', tag='BBOX')
SpatialOperatorNameType.Equals = SpatialOperatorNameType._CF_enumeration.addEnumeration(unicode_value='Equals', tag='Equals')
SpatialOperatorNameType.Disjoint = SpatialOperatorNameType._CF_enumeration.addEnumeration(unicode_value='Disjoint', tag='Disjoint')
SpatialOperatorNameType.Intersects = SpatialOperatorNameType._CF_enumeration.addEnumeration(unicode_value='Intersects', tag='Intersects')
SpatialOperatorNameType.Touches = SpatialOperatorNameType._CF_enumeration.addEnumeration(unicode_value='Touches', tag='Touches')
SpatialOperatorNameType.Crosses = SpatialOperatorNameType._CF_enumeration.addEnumeration(unicode_value='Crosses', tag='Crosses')
SpatialOperatorNameType.Within = SpatialOperatorNameType._CF_enumeration.addEnumeration(unicode_value='Within', tag='Within')
SpatialOperatorNameType.Contains = SpatialOperatorNameType._CF_enumeration.addEnumeration(unicode_value='Contains', tag='Contains')
SpatialOperatorNameType.Overlaps = SpatialOperatorNameType._CF_enumeration.addEnumeration(unicode_value='Overlaps', tag='Overlaps')
SpatialOperatorNameType.Beyond = SpatialOperatorNameType._CF_enumeration.addEnumeration(unicode_value='Beyond', tag='Beyond')
SpatialOperatorNameType.DWithin = SpatialOperatorNameType._CF_enumeration.addEnumeration(unicode_value='DWithin', tag='DWithin')
SpatialOperatorNameType._InitializeFacetMap(SpatialOperatorNameType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SpatialOperatorNameType', SpatialOperatorNameType)
_module_typeBindings.SpatialOperatorNameType = SpatialOperatorNameType

# Atomic simple type: {http://www.opengis.net/ogc}ComparisonOperatorType
class ComparisonOperatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ComparisonOperatorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 120, 3)
    _Documentation = None
ComparisonOperatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ComparisonOperatorType, enum_prefix=None)
ComparisonOperatorType.LessThan = ComparisonOperatorType._CF_enumeration.addEnumeration(unicode_value='LessThan', tag='LessThan')
ComparisonOperatorType.GreaterThan = ComparisonOperatorType._CF_enumeration.addEnumeration(unicode_value='GreaterThan', tag='GreaterThan')
ComparisonOperatorType.LessThanEqualTo = ComparisonOperatorType._CF_enumeration.addEnumeration(unicode_value='LessThanEqualTo', tag='LessThanEqualTo')
ComparisonOperatorType.GreaterThanEqualTo = ComparisonOperatorType._CF_enumeration.addEnumeration(unicode_value='GreaterThanEqualTo', tag='GreaterThanEqualTo')
ComparisonOperatorType.EqualTo = ComparisonOperatorType._CF_enumeration.addEnumeration(unicode_value='EqualTo', tag='EqualTo')
ComparisonOperatorType.NotEqualTo = ComparisonOperatorType._CF_enumeration.addEnumeration(unicode_value='NotEqualTo', tag='NotEqualTo')
ComparisonOperatorType.Like = ComparisonOperatorType._CF_enumeration.addEnumeration(unicode_value='Like', tag='Like')
ComparisonOperatorType.Between = ComparisonOperatorType._CF_enumeration.addEnumeration(unicode_value='Between', tag='Between')
ComparisonOperatorType.NullCheck = ComparisonOperatorType._CF_enumeration.addEnumeration(unicode_value='NullCheck', tag='NullCheck')
ComparisonOperatorType._InitializeFacetMap(ComparisonOperatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ComparisonOperatorType', ComparisonOperatorType)
_module_typeBindings.ComparisonOperatorType = ComparisonOperatorType

# Atomic simple type: {http://www.opengis.net/ogc}SortOrderType
class SortOrderType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SortOrderType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/sort.xsd', 41, 3)
    _Documentation = None
SortOrderType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SortOrderType, enum_prefix=None)
SortOrderType.DESC = SortOrderType._CF_enumeration.addEnumeration(unicode_value='DESC', tag='DESC')
SortOrderType.ASC = SortOrderType._CF_enumeration.addEnumeration(unicode_value='ASC', tag='ASC')
SortOrderType._InitializeFacetMap(SortOrderType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SortOrderType', SortOrderType)
_module_typeBindings.SortOrderType = SortOrderType

# Complex type {http://www.opengis.net/ogc}ExpressionType with content type EMPTY
class ExpressionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}ExpressionType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExpressionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 32, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ExpressionType = ExpressionType
Namespace.addCategoryObject('typeBinding', 'ExpressionType', ExpressionType)


# Complex type {http://www.opengis.net/ogc}FilterType with content type ELEMENT_ONLY
class FilterType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}FilterType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FilterType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 40, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}_Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_Id'), 'Id', '__httpwww_opengis_netogc_FilterType_httpwww_opengis_netogc_Id', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 31, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://www.opengis.net/ogc}comparisonOps uses Python identifier comparisonOps
    __comparisonOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps'), 'comparisonOps', '__httpwww_opengis_netogc_FilterType_httpwww_opengis_netogccomparisonOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 49, 3), )

    
    comparisonOps = property(__comparisonOps.value, __comparisonOps.set, None, None)

    
    # Element {http://www.opengis.net/ogc}spatialOps uses Python identifier spatialOps
    __spatialOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'spatialOps'), 'spatialOps', '__httpwww_opengis_netogc_FilterType_httpwww_opengis_netogcspatialOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 80, 3), )

    
    spatialOps = property(__spatialOps.value, __spatialOps.set, None, None)

    
    # Element {http://www.opengis.net/ogc}logicOps uses Python identifier logicOps
    __logicOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'logicOps'), 'logicOps', '__httpwww_opengis_netogc_FilterType_httpwww_opengis_netogclogicOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 115, 3), )

    
    logicOps = property(__logicOps.value, __logicOps.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __comparisonOps.name() : __comparisonOps,
        __spatialOps.name() : __spatialOps,
        __logicOps.name() : __logicOps
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FilterType = FilterType
Namespace.addCategoryObject('typeBinding', 'FilterType', FilterType)


# Complex type {http://www.opengis.net/ogc}ComparisonOpsType with content type EMPTY
class ComparisonOpsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}ComparisonOpsType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ComparisonOpsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 79, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ComparisonOpsType = ComparisonOpsType
Namespace.addCategoryObject('typeBinding', 'ComparisonOpsType', ComparisonOpsType)


# Complex type {http://www.opengis.net/ogc}SpatialOpsType with content type EMPTY
class SpatialOpsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}SpatialOpsType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpatialOpsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 114, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SpatialOpsType = SpatialOpsType
Namespace.addCategoryObject('typeBinding', 'SpatialOpsType', SpatialOpsType)


# Complex type {http://www.opengis.net/ogc}LogicOpsType with content type EMPTY
class LogicOpsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}LogicOpsType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogicOpsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 125, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LogicOpsType = LogicOpsType
Namespace.addCategoryObject('typeBinding', 'LogicOpsType', LogicOpsType)


# Complex type {http://www.opengis.net/ogc}AbstractIdType with content type EMPTY
class AbstractIdType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}AbstractIdType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 126, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractIdType = AbstractIdType
Namespace.addCategoryObject('typeBinding', 'AbstractIdType', AbstractIdType)


# Complex type {http://www.opengis.net/ogc}LowerBoundaryType with content type ELEMENT_ONLY
class LowerBoundaryType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}LowerBoundaryType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LowerBoundaryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 187, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netogc_LowerBoundaryType_httpwww_opengis_netogcexpression', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 29, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    _ElementMap.update({
        __expression.name() : __expression
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LowerBoundaryType = LowerBoundaryType
Namespace.addCategoryObject('typeBinding', 'LowerBoundaryType', LowerBoundaryType)


# Complex type {http://www.opengis.net/ogc}UpperBoundaryType with content type ELEMENT_ONLY
class UpperBoundaryType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}UpperBoundaryType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UpperBoundaryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 192, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netogc_UpperBoundaryType_httpwww_opengis_netogcexpression', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 29, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    _ElementMap.update({
        __expression.name() : __expression
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UpperBoundaryType = UpperBoundaryType
Namespace.addCategoryObject('typeBinding', 'UpperBoundaryType', UpperBoundaryType)


# Complex type {http://www.opengis.net/ogc}DistanceType with content type SIMPLE
class DistanceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}DistanceType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DistanceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 232, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.double
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_opengis_netogc_DistanceType_units', pyxb.binding.datatypes.anyURI, required=True)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 235, 12)
    __units._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 235, 12)
    
    units = property(__units.value, __units.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
_module_typeBindings.DistanceType = DistanceType
Namespace.addCategoryObject('typeBinding', 'DistanceType', DistanceType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 21, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}Spatial_Capabilities uses Python identifier Spatial_Capabilities
    __Spatial_Capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Spatial_Capabilities'), 'Spatial_Capabilities', '__httpwww_opengis_netogc_CTD_ANON_httpwww_opengis_netogcSpatial_Capabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 23, 12), )

    
    Spatial_Capabilities = property(__Spatial_Capabilities.value, __Spatial_Capabilities.set, None, None)

    
    # Element {http://www.opengis.net/ogc}Scalar_Capabilities uses Python identifier Scalar_Capabilities
    __Scalar_Capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Scalar_Capabilities'), 'Scalar_Capabilities', '__httpwww_opengis_netogc_CTD_ANON_httpwww_opengis_netogcScalar_Capabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 25, 12), )

    
    Scalar_Capabilities = property(__Scalar_Capabilities.value, __Scalar_Capabilities.set, None, None)

    
    # Element {http://www.opengis.net/ogc}Id_Capabilities uses Python identifier Id_Capabilities
    __Id_Capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id_Capabilities'), 'Id_Capabilities', '__httpwww_opengis_netogc_CTD_ANON_httpwww_opengis_netogcId_Capabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 27, 12), )

    
    Id_Capabilities = property(__Id_Capabilities.value, __Id_Capabilities.set, None, None)

    _ElementMap.update({
        __Spatial_Capabilities.name() : __Spatial_Capabilities,
        __Scalar_Capabilities.name() : __Scalar_Capabilities,
        __Id_Capabilities.name() : __Id_Capabilities
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://www.opengis.net/ogc}Spatial_CapabilitiesType with content type ELEMENT_ONLY
class Spatial_CapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}Spatial_CapabilitiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Spatial_CapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 32, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}GeometryOperands uses Python identifier GeometryOperands
    __GeometryOperands = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperands'), 'GeometryOperands', '__httpwww_opengis_netogc_Spatial_CapabilitiesType_httpwww_opengis_netogcGeometryOperands', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 34, 9), )

    
    GeometryOperands = property(__GeometryOperands.value, __GeometryOperands.set, None, None)

    
    # Element {http://www.opengis.net/ogc}SpatialOperators uses Python identifier SpatialOperators
    __SpatialOperators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SpatialOperators'), 'SpatialOperators', '__httpwww_opengis_netogc_Spatial_CapabilitiesType_httpwww_opengis_netogcSpatialOperators', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 36, 9), )

    
    SpatialOperators = property(__SpatialOperators.value, __SpatialOperators.set, None, None)

    _ElementMap.update({
        __GeometryOperands.name() : __GeometryOperands,
        __SpatialOperators.name() : __SpatialOperators
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Spatial_CapabilitiesType = Spatial_CapabilitiesType
Namespace.addCategoryObject('typeBinding', 'Spatial_CapabilitiesType', Spatial_CapabilitiesType)


# Complex type {http://www.opengis.net/ogc}GeometryOperandsType with content type ELEMENT_ONLY
class GeometryOperandsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}GeometryOperandsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeometryOperandsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 40, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}GeometryOperand uses Python identifier GeometryOperand
    __GeometryOperand = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperand'), 'GeometryOperand', '__httpwww_opengis_netogc_GeometryOperandsType_httpwww_opengis_netogcGeometryOperand', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 42, 9), )

    
    GeometryOperand = property(__GeometryOperand.value, __GeometryOperand.set, None, None)

    _ElementMap.update({
        __GeometryOperand.name() : __GeometryOperand
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GeometryOperandsType = GeometryOperandsType
Namespace.addCategoryObject('typeBinding', 'GeometryOperandsType', GeometryOperandsType)


# Complex type {http://www.opengis.net/ogc}SpatialOperatorsType with content type ELEMENT_ONLY
class SpatialOperatorsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}SpatialOperatorsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpatialOperatorsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 69, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}SpatialOperator uses Python identifier SpatialOperator
    __SpatialOperator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SpatialOperator'), 'SpatialOperator', '__httpwww_opengis_netogc_SpatialOperatorsType_httpwww_opengis_netogcSpatialOperator', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 71, 9), )

    
    SpatialOperator = property(__SpatialOperator.value, __SpatialOperator.set, None, None)

    _ElementMap.update({
        __SpatialOperator.name() : __SpatialOperator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SpatialOperatorsType = SpatialOperatorsType
Namespace.addCategoryObject('typeBinding', 'SpatialOperatorsType', SpatialOperatorsType)


# Complex type {http://www.opengis.net/ogc}Scalar_CapabilitiesType with content type ELEMENT_ONLY
class Scalar_CapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}Scalar_CapabilitiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Scalar_CapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 99, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}ComparisonOperators uses Python identifier ComparisonOperators
    __ComparisonOperators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ComparisonOperators'), 'ComparisonOperators', '__httpwww_opengis_netogc_Scalar_CapabilitiesType_httpwww_opengis_netogcComparisonOperators', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 103, 9), )

    
    ComparisonOperators = property(__ComparisonOperators.value, __ComparisonOperators.set, None, None)

    
    # Element {http://www.opengis.net/ogc}ArithmeticOperators uses Python identifier ArithmeticOperators
    __ArithmeticOperators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ArithmeticOperators'), 'ArithmeticOperators', '__httpwww_opengis_netogc_Scalar_CapabilitiesType_httpwww_opengis_netogcArithmeticOperators', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 106, 9), )

    
    ArithmeticOperators = property(__ArithmeticOperators.value, __ArithmeticOperators.set, None, None)

    
    # Element {http://www.opengis.net/ogc}LogicalOperators uses Python identifier LogicalOperators
    __LogicalOperators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LogicalOperators'), 'LogicalOperators', '__httpwww_opengis_netogc_Scalar_CapabilitiesType_httpwww_opengis_netogcLogicalOperators', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 111, 3), )

    
    LogicalOperators = property(__LogicalOperators.value, __LogicalOperators.set, None, None)

    _ElementMap.update({
        __ComparisonOperators.name() : __ComparisonOperators,
        __ArithmeticOperators.name() : __ArithmeticOperators,
        __LogicalOperators.name() : __LogicalOperators
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Scalar_CapabilitiesType = Scalar_CapabilitiesType
Namespace.addCategoryObject('typeBinding', 'Scalar_CapabilitiesType', Scalar_CapabilitiesType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 112, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {http://www.opengis.net/ogc}ComparisonOperatorsType with content type ELEMENT_ONLY
class ComparisonOperatorsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}ComparisonOperatorsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ComparisonOperatorsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 114, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}ComparisonOperator uses Python identifier ComparisonOperator
    __ComparisonOperator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ComparisonOperator'), 'ComparisonOperator', '__httpwww_opengis_netogc_ComparisonOperatorsType_httpwww_opengis_netogcComparisonOperator', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 116, 9), )

    
    ComparisonOperator = property(__ComparisonOperator.value, __ComparisonOperator.set, None, None)

    _ElementMap.update({
        __ComparisonOperator.name() : __ComparisonOperator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ComparisonOperatorsType = ComparisonOperatorsType
Namespace.addCategoryObject('typeBinding', 'ComparisonOperatorsType', ComparisonOperatorsType)


# Complex type {http://www.opengis.net/ogc}ArithmeticOperatorsType with content type ELEMENT_ONLY
class ArithmeticOperatorsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}ArithmeticOperatorsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArithmeticOperatorsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 133, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}Functions uses Python identifier Functions
    __Functions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Functions'), 'Functions', '__httpwww_opengis_netogc_ArithmeticOperatorsType_httpwww_opengis_netogcFunctions', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 136, 9), )

    
    Functions = property(__Functions.value, __Functions.set, None, None)

    
    # Element {http://www.opengis.net/ogc}SimpleArithmetic uses Python identifier SimpleArithmetic
    __SimpleArithmetic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SimpleArithmetic'), 'SimpleArithmetic', '__httpwww_opengis_netogc_ArithmeticOperatorsType_httpwww_opengis_netogcSimpleArithmetic', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 139, 3), )

    
    SimpleArithmetic = property(__SimpleArithmetic.value, __SimpleArithmetic.set, None, None)

    _ElementMap.update({
        __Functions.name() : __Functions,
        __SimpleArithmetic.name() : __SimpleArithmetic
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ArithmeticOperatorsType = ArithmeticOperatorsType
Namespace.addCategoryObject('typeBinding', 'ArithmeticOperatorsType', ArithmeticOperatorsType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 140, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type {http://www.opengis.net/ogc}FunctionsType with content type ELEMENT_ONLY
class FunctionsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}FunctionsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FunctionsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 142, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}FunctionNames uses Python identifier FunctionNames
    __FunctionNames = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FunctionNames'), 'FunctionNames', '__httpwww_opengis_netogc_FunctionsType_httpwww_opengis_netogcFunctionNames', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 144, 9), )

    
    FunctionNames = property(__FunctionNames.value, __FunctionNames.set, None, None)

    _ElementMap.update({
        __FunctionNames.name() : __FunctionNames
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FunctionsType = FunctionsType
Namespace.addCategoryObject('typeBinding', 'FunctionsType', FunctionsType)


# Complex type {http://www.opengis.net/ogc}FunctionNamesType with content type ELEMENT_ONLY
class FunctionNamesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}FunctionNamesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FunctionNamesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 147, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}FunctionName uses Python identifier FunctionName
    __FunctionName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FunctionName'), 'FunctionName', '__httpwww_opengis_netogc_FunctionNamesType_httpwww_opengis_netogcFunctionName', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 149, 9), )

    
    FunctionName = property(__FunctionName.value, __FunctionName.set, None, None)

    _ElementMap.update({
        __FunctionName.name() : __FunctionName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FunctionNamesType = FunctionNamesType
Namespace.addCategoryObject('typeBinding', 'FunctionNamesType', FunctionNamesType)


# Complex type {http://www.opengis.net/ogc}FunctionNameType with content type SIMPLE
class FunctionNameType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}FunctionNameType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FunctionNameType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 152, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute nArgs uses Python identifier nArgs
    __nArgs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nArgs'), 'nArgs', '__httpwww_opengis_netogc_FunctionNameType_nArgs', pyxb.binding.datatypes.string, required=True)
    __nArgs._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 155, 12)
    __nArgs._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 155, 12)
    
    nArgs = property(__nArgs.value, __nArgs.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __nArgs.name() : __nArgs
    })
_module_typeBindings.FunctionNameType = FunctionNameType
Namespace.addCategoryObject('typeBinding', 'FunctionNameType', FunctionNameType)


# Complex type {http://www.opengis.net/ogc}Id_CapabilitiesType with content type ELEMENT_ONLY
class Id_CapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}Id_CapabilitiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Id_CapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 159, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}EID uses Python identifier EID
    __EID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EID'), 'EID', '__httpwww_opengis_netogc_Id_CapabilitiesType_httpwww_opengis_netogcEID', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 165, 3), )

    
    EID = property(__EID.value, __EID.set, None, None)

    
    # Element {http://www.opengis.net/ogc}FID uses Python identifier FID
    __FID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FID'), 'FID', '__httpwww_opengis_netogc_Id_CapabilitiesType_httpwww_opengis_netogcFID', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 168, 3), )

    
    FID = property(__FID.value, __FID.set, None, None)

    _ElementMap.update({
        __EID.name() : __EID,
        __FID.name() : __FID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Id_CapabilitiesType = Id_CapabilitiesType
Namespace.addCategoryObject('typeBinding', 'Id_CapabilitiesType', Id_CapabilitiesType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 166, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 169, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type {http://www.opengis.net/ogc}SortByType with content type ELEMENT_ONLY
class SortByType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}SortByType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SortByType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/sort.xsd', 26, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}SortProperty uses Python identifier SortProperty
    __SortProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SortProperty'), 'SortProperty', '__httpwww_opengis_netogc_SortByType_httpwww_opengis_netogcSortProperty', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/sort.xsd', 28, 9), )

    
    SortProperty = property(__SortProperty.value, __SortProperty.set, None, None)

    _ElementMap.update({
        __SortProperty.name() : __SortProperty
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SortByType = SortByType
Namespace.addCategoryObject('typeBinding', 'SortByType', SortByType)


# Complex type {http://www.opengis.net/ogc}SortPropertyType with content type ELEMENT_ONLY
class SortPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}SortPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SortPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/sort.xsd', 33, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}PropertyName uses Python identifier PropertyName
    __PropertyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), 'PropertyName', '__httpwww_opengis_netogc_SortPropertyType_httpwww_opengis_netogcPropertyName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 23, 3), )

    
    PropertyName = property(__PropertyName.value, __PropertyName.set, None, None)

    
    # Element {http://www.opengis.net/ogc}SortOrder uses Python identifier SortOrder
    __SortOrder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SortOrder'), 'SortOrder', '__httpwww_opengis_netogc_SortPropertyType_httpwww_opengis_netogcSortOrder', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/sort.xsd', 36, 9), )

    
    SortOrder = property(__SortOrder.value, __SortOrder.set, None, None)

    _ElementMap.update({
        __PropertyName.name() : __PropertyName,
        __SortOrder.name() : __SortOrder
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SortPropertyType = SortPropertyType
Namespace.addCategoryObject('typeBinding', 'SortPropertyType', SortPropertyType)


# Complex type {http://www.opengis.net/ogc}BinaryOperatorType with content type ELEMENT_ONLY
class BinaryOperatorType (ExpressionType):
    """Complex type {http://www.opengis.net/ogc}BinaryOperatorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BinaryOperatorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 33, 3)
    _ElementMap = ExpressionType._ElementMap.copy()
    _AttributeMap = ExpressionType._AttributeMap.copy()
    # Base type is ExpressionType
    
    # Element {http://www.opengis.net/ogc}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netogc_BinaryOperatorType_httpwww_opengis_netogcexpression', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 29, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    _ElementMap.update({
        __expression.name() : __expression
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BinaryOperatorType = BinaryOperatorType
Namespace.addCategoryObject('typeBinding', 'BinaryOperatorType', BinaryOperatorType)


# Complex type {http://www.opengis.net/ogc}FunctionType with content type ELEMENT_ONLY
class FunctionType (ExpressionType):
    """Complex type {http://www.opengis.net/ogc}FunctionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FunctionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 42, 3)
    _ElementMap = ExpressionType._ElementMap.copy()
    _AttributeMap = ExpressionType._AttributeMap.copy()
    # Base type is ExpressionType
    
    # Element {http://www.opengis.net/ogc}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netogc_FunctionType_httpwww_opengis_netogcexpression', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 29, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netogc_FunctionType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 49, 12)
    __name._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 49, 12)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __expression.name() : __expression
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.FunctionType = FunctionType
Namespace.addCategoryObject('typeBinding', 'FunctionType', FunctionType)


# Complex type {http://www.opengis.net/ogc}LiteralType with content type MIXED
class LiteralType (ExpressionType):
    """Complex type {http://www.opengis.net/ogc}LiteralType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LiteralType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 53, 3)
    _ElementMap = ExpressionType._ElementMap.copy()
    _AttributeMap = ExpressionType._AttributeMap.copy()
    # Base type is ExpressionType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LiteralType = LiteralType
Namespace.addCategoryObject('typeBinding', 'LiteralType', LiteralType)


# Complex type {http://www.opengis.net/ogc}PropertyNameType with content type MIXED
class PropertyNameType (ExpressionType):
    """Complex type {http://www.opengis.net/ogc}PropertyNameType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PropertyNameType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 62, 3)
    _ElementMap = ExpressionType._ElementMap.copy()
    _AttributeMap = ExpressionType._AttributeMap.copy()
    # Base type is ExpressionType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PropertyNameType = PropertyNameType
Namespace.addCategoryObject('typeBinding', 'PropertyNameType', PropertyNameType)


# Complex type {http://www.opengis.net/ogc}FeatureIdType with content type EMPTY
class FeatureIdType (AbstractIdType):
    """Complex type {http://www.opengis.net/ogc}FeatureIdType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FeatureIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 127, 3)
    _ElementMap = AbstractIdType._ElementMap.copy()
    _AttributeMap = AbstractIdType._AttributeMap.copy()
    # Base type is AbstractIdType
    
    # Attribute fid uses Python identifier fid
    __fid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fid'), 'fid', '__httpwww_opengis_netogc_FeatureIdType_fid', pyxb.binding.datatypes.ID, required=True)
    __fid._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 130, 12)
    __fid._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 130, 12)
    
    fid = property(__fid.value, __fid.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __fid.name() : __fid
    })
_module_typeBindings.FeatureIdType = FeatureIdType
Namespace.addCategoryObject('typeBinding', 'FeatureIdType', FeatureIdType)


# Complex type {http://www.opengis.net/ogc}GmlObjectIdType with content type EMPTY
class GmlObjectIdType (AbstractIdType):
    """Complex type {http://www.opengis.net/ogc}GmlObjectIdType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GmlObjectIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 134, 3)
    _ElementMap = AbstractIdType._ElementMap.copy()
    _AttributeMap = AbstractIdType._AttributeMap.copy()
    # Base type is AbstractIdType
    
    # Attribute {http://www.opengis.net/gml}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'id'), 'id', '__httpwww_opengis_netogc_GmlObjectIdType_httpwww_opengis_netgmlid', pyxb.binding.datatypes.ID, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 252, 1)
    __id._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 137, 12)
    
    id = property(__id.value, __id.set, None, 'Database handle for the object.  It is of XML type ID, so is constrained to be unique in the XML document within which it occurs.  An external identifier for the object in the form of a URI may be constructed using standard XML and XPointer methods.  This is done by concatenating the URI for the document, a fragment separator, and the value of the id attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.GmlObjectIdType = GmlObjectIdType
Namespace.addCategoryObject('typeBinding', 'GmlObjectIdType', GmlObjectIdType)


# Complex type {http://www.opengis.net/ogc}BinaryComparisonOpType with content type ELEMENT_ONLY
class BinaryComparisonOpType (ComparisonOpsType):
    """Complex type {http://www.opengis.net/ogc}BinaryComparisonOpType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BinaryComparisonOpType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 141, 3)
    _ElementMap = ComparisonOpsType._ElementMap.copy()
    _AttributeMap = ComparisonOpsType._AttributeMap.copy()
    # Base type is ComparisonOpsType
    
    # Element {http://www.opengis.net/ogc}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netogc_BinaryComparisonOpType_httpwww_opengis_netogcexpression', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 29, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    
    # Attribute matchCase uses Python identifier matchCase
    __matchCase = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'matchCase'), 'matchCase', '__httpwww_opengis_netogc_BinaryComparisonOpType_matchCase', pyxb.binding.datatypes.boolean, unicode_default='true')
    __matchCase._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 147, 12)
    __matchCase._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 147, 12)
    
    matchCase = property(__matchCase.value, __matchCase.set, None, None)

    _ElementMap.update({
        __expression.name() : __expression
    })
    _AttributeMap.update({
        __matchCase.name() : __matchCase
    })
_module_typeBindings.BinaryComparisonOpType = BinaryComparisonOpType
Namespace.addCategoryObject('typeBinding', 'BinaryComparisonOpType', BinaryComparisonOpType)


# Complex type {http://www.opengis.net/ogc}PropertyIsLikeType with content type ELEMENT_ONLY
class PropertyIsLikeType (ComparisonOpsType):
    """Complex type {http://www.opengis.net/ogc}PropertyIsLikeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PropertyIsLikeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 152, 3)
    _ElementMap = ComparisonOpsType._ElementMap.copy()
    _AttributeMap = ComparisonOpsType._AttributeMap.copy()
    # Base type is ComparisonOpsType
    
    # Element {http://www.opengis.net/ogc}PropertyName uses Python identifier PropertyName
    __PropertyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), 'PropertyName', '__httpwww_opengis_netogc_PropertyIsLikeType_httpwww_opengis_netogcPropertyName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 23, 3), )

    
    PropertyName = property(__PropertyName.value, __PropertyName.set, None, None)

    
    # Element {http://www.opengis.net/ogc}Literal uses Python identifier Literal
    __Literal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Literal'), 'Literal', '__httpwww_opengis_netogc_PropertyIsLikeType_httpwww_opengis_netogcLiteral', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 27, 3), )

    
    Literal = property(__Literal.value, __Literal.set, None, None)

    
    # Attribute wildCard uses Python identifier wildCard
    __wildCard = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wildCard'), 'wildCard', '__httpwww_opengis_netogc_PropertyIsLikeType_wildCard', pyxb.binding.datatypes.string, required=True)
    __wildCard._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 159, 12)
    __wildCard._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 159, 12)
    
    wildCard = property(__wildCard.value, __wildCard.set, None, None)

    
    # Attribute singleChar uses Python identifier singleChar
    __singleChar = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'singleChar'), 'singleChar', '__httpwww_opengis_netogc_PropertyIsLikeType_singleChar', pyxb.binding.datatypes.string, required=True)
    __singleChar._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 160, 12)
    __singleChar._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 160, 12)
    
    singleChar = property(__singleChar.value, __singleChar.set, None, None)

    
    # Attribute escapeChar uses Python identifier escapeChar
    __escapeChar = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'escapeChar'), 'escapeChar', '__httpwww_opengis_netogc_PropertyIsLikeType_escapeChar', pyxb.binding.datatypes.string, required=True)
    __escapeChar._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 161, 12)
    __escapeChar._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 161, 12)
    
    escapeChar = property(__escapeChar.value, __escapeChar.set, None, None)

    
    # Attribute matchCase uses Python identifier matchCase
    __matchCase = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'matchCase'), 'matchCase', '__httpwww_opengis_netogc_PropertyIsLikeType_matchCase', pyxb.binding.datatypes.boolean, unicode_default='true')
    __matchCase._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 162, 12)
    __matchCase._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 162, 12)
    
    matchCase = property(__matchCase.value, __matchCase.set, None, None)

    _ElementMap.update({
        __PropertyName.name() : __PropertyName,
        __Literal.name() : __Literal
    })
    _AttributeMap.update({
        __wildCard.name() : __wildCard,
        __singleChar.name() : __singleChar,
        __escapeChar.name() : __escapeChar,
        __matchCase.name() : __matchCase
    })
_module_typeBindings.PropertyIsLikeType = PropertyIsLikeType
Namespace.addCategoryObject('typeBinding', 'PropertyIsLikeType', PropertyIsLikeType)


# Complex type {http://www.opengis.net/ogc}PropertyIsNullType with content type ELEMENT_ONLY
class PropertyIsNullType (ComparisonOpsType):
    """Complex type {http://www.opengis.net/ogc}PropertyIsNullType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PropertyIsNullType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 167, 3)
    _ElementMap = ComparisonOpsType._ElementMap.copy()
    _AttributeMap = ComparisonOpsType._AttributeMap.copy()
    # Base type is ComparisonOpsType
    
    # Element {http://www.opengis.net/ogc}PropertyName uses Python identifier PropertyName
    __PropertyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), 'PropertyName', '__httpwww_opengis_netogc_PropertyIsNullType_httpwww_opengis_netogcPropertyName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 23, 3), )

    
    PropertyName = property(__PropertyName.value, __PropertyName.set, None, None)

    _ElementMap.update({
        __PropertyName.name() : __PropertyName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PropertyIsNullType = PropertyIsNullType
Namespace.addCategoryObject('typeBinding', 'PropertyIsNullType', PropertyIsNullType)


# Complex type {http://www.opengis.net/ogc}PropertyIsBetweenType with content type ELEMENT_ONLY
class PropertyIsBetweenType (ComparisonOpsType):
    """Complex type {http://www.opengis.net/ogc}PropertyIsBetweenType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PropertyIsBetweenType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 176, 3)
    _ElementMap = ComparisonOpsType._ElementMap.copy()
    _AttributeMap = ComparisonOpsType._AttributeMap.copy()
    # Base type is ComparisonOpsType
    
    # Element {http://www.opengis.net/ogc}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netogc_PropertyIsBetweenType_httpwww_opengis_netogcexpression', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 29, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    
    # Element {http://www.opengis.net/ogc}LowerBoundary uses Python identifier LowerBoundary
    __LowerBoundary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LowerBoundary'), 'LowerBoundary', '__httpwww_opengis_netogc_PropertyIsBetweenType_httpwww_opengis_netogcLowerBoundary', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 181, 15), )

    
    LowerBoundary = property(__LowerBoundary.value, __LowerBoundary.set, None, None)

    
    # Element {http://www.opengis.net/ogc}UpperBoundary uses Python identifier UpperBoundary
    __UpperBoundary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UpperBoundary'), 'UpperBoundary', '__httpwww_opengis_netogc_PropertyIsBetweenType_httpwww_opengis_netogcUpperBoundary', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 182, 15), )

    
    UpperBoundary = property(__UpperBoundary.value, __UpperBoundary.set, None, None)

    _ElementMap.update({
        __expression.name() : __expression,
        __LowerBoundary.name() : __LowerBoundary,
        __UpperBoundary.name() : __UpperBoundary
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PropertyIsBetweenType = PropertyIsBetweenType
Namespace.addCategoryObject('typeBinding', 'PropertyIsBetweenType', PropertyIsBetweenType)


# Complex type {http://www.opengis.net/ogc}BinarySpatialOpType with content type ELEMENT_ONLY
class BinarySpatialOpType (SpatialOpsType):
    """Complex type {http://www.opengis.net/ogc}BinarySpatialOpType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BinarySpatialOpType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 197, 3)
    _ElementMap = SpatialOpsType._ElementMap.copy()
    _AttributeMap = SpatialOpsType._AttributeMap.copy()
    # Base type is SpatialOpsType
    
    # Element {http://www.opengis.net/gml}_Geometry uses Python identifier Geometry
    __Geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, '_Geometry'), 'Geometry', '__httpwww_opengis_netogc_BinarySpatialOpType_httpwww_opengis_netgml_Geometry', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/geometryBasic0d1d.xsd', 39, 1), )

    
    Geometry = property(__Geometry.value, __Geometry.set, None, 'The "_Geometry" element is the abstract head of the substituition group for all geometry elements of GML 3. This \n\t\t\tincludes pre-defined and user-defined geometry elements. Any geometry element must be a direct or indirect extension/restriction \n\t\t\tof AbstractGeometryType and must be directly or indirectly in the substitution group of "_Geometry".')

    
    # Element {http://www.opengis.net/gml}Envelope uses Python identifier Envelope
    __Envelope = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'Envelope'), 'Envelope', '__httpwww_opengis_netogc_BinarySpatialOpType_httpwww_opengis_netgmlEnvelope', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/geometryBasic0d1d.xsd', 519, 1), )

    
    Envelope = property(__Envelope.value, __Envelope.set, None, None)

    
    # Element {http://www.opengis.net/ogc}PropertyName uses Python identifier PropertyName
    __PropertyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), 'PropertyName', '__httpwww_opengis_netogc_BinarySpatialOpType_httpwww_opengis_netogcPropertyName', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 23, 3), )

    
    PropertyName = property(__PropertyName.value, __PropertyName.set, None, None)

    _ElementMap.update({
        __Geometry.name() : __Geometry,
        __Envelope.name() : __Envelope,
        __PropertyName.name() : __PropertyName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BinarySpatialOpType = BinarySpatialOpType
Namespace.addCategoryObject('typeBinding', 'BinarySpatialOpType', BinarySpatialOpType)


# Complex type {http://www.opengis.net/ogc}BBOXType with content type ELEMENT_ONLY
class BBOXType (SpatialOpsType):
    """Complex type {http://www.opengis.net/ogc}BBOXType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BBOXType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 211, 3)
    _ElementMap = SpatialOpsType._ElementMap.copy()
    _AttributeMap = SpatialOpsType._AttributeMap.copy()
    # Base type is SpatialOpsType
    
    # Element {http://www.opengis.net/gml}Envelope uses Python identifier Envelope
    __Envelope = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'Envelope'), 'Envelope', '__httpwww_opengis_netogc_BBOXType_httpwww_opengis_netgmlEnvelope', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/geometryBasic0d1d.xsd', 519, 1), )

    
    Envelope = property(__Envelope.value, __Envelope.set, None, None)

    
    # Element {http://www.opengis.net/ogc}PropertyName uses Python identifier PropertyName
    __PropertyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), 'PropertyName', '__httpwww_opengis_netogc_BBOXType_httpwww_opengis_netogcPropertyName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 23, 3), )

    
    PropertyName = property(__PropertyName.value, __PropertyName.set, None, None)

    _ElementMap.update({
        __Envelope.name() : __Envelope,
        __PropertyName.name() : __PropertyName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BBOXType = BBOXType
Namespace.addCategoryObject('typeBinding', 'BBOXType', BBOXType)


# Complex type {http://www.opengis.net/ogc}DistanceBufferType with content type ELEMENT_ONLY
class DistanceBufferType (SpatialOpsType):
    """Complex type {http://www.opengis.net/ogc}DistanceBufferType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DistanceBufferType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 221, 3)
    _ElementMap = SpatialOpsType._ElementMap.copy()
    _AttributeMap = SpatialOpsType._AttributeMap.copy()
    # Base type is SpatialOpsType
    
    # Element {http://www.opengis.net/gml}_Geometry uses Python identifier Geometry
    __Geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, '_Geometry'), 'Geometry', '__httpwww_opengis_netogc_DistanceBufferType_httpwww_opengis_netgml_Geometry', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/geometryBasic0d1d.xsd', 39, 1), )

    
    Geometry = property(__Geometry.value, __Geometry.set, None, 'The "_Geometry" element is the abstract head of the substituition group for all geometry elements of GML 3. This \n\t\t\tincludes pre-defined and user-defined geometry elements. Any geometry element must be a direct or indirect extension/restriction \n\t\t\tof AbstractGeometryType and must be directly or indirectly in the substitution group of "_Geometry".')

    
    # Element {http://www.opengis.net/ogc}PropertyName uses Python identifier PropertyName
    __PropertyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), 'PropertyName', '__httpwww_opengis_netogc_DistanceBufferType_httpwww_opengis_netogcPropertyName', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 23, 3), )

    
    PropertyName = property(__PropertyName.value, __PropertyName.set, None, None)

    
    # Element {http://www.opengis.net/ogc}Distance uses Python identifier Distance
    __Distance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Distance'), 'Distance', '__httpwww_opengis_netogc_DistanceBufferType_httpwww_opengis_netogcDistance', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 227, 15), )

    
    Distance = property(__Distance.value, __Distance.set, None, None)

    _ElementMap.update({
        __Geometry.name() : __Geometry,
        __PropertyName.name() : __PropertyName,
        __Distance.name() : __Distance
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DistanceBufferType = DistanceBufferType
Namespace.addCategoryObject('typeBinding', 'DistanceBufferType', DistanceBufferType)


# Complex type {http://www.opengis.net/ogc}BinaryLogicOpType with content type ELEMENT_ONLY
class BinaryLogicOpType (LogicOpsType):
    """Complex type {http://www.opengis.net/ogc}BinaryLogicOpType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BinaryLogicOpType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 239, 3)
    _ElementMap = LogicOpsType._ElementMap.copy()
    _AttributeMap = LogicOpsType._AttributeMap.copy()
    # Base type is LogicOpsType
    
    # Element {http://www.opengis.net/ogc}Function uses Python identifier Function
    __Function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Function'), 'Function', '__httpwww_opengis_netogc_BinaryLogicOpType_httpwww_opengis_netogcFunction', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 25, 3), )

    
    Function = property(__Function.value, __Function.set, None, None)

    
    # Element {http://www.opengis.net/ogc}comparisonOps uses Python identifier comparisonOps
    __comparisonOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps'), 'comparisonOps', '__httpwww_opengis_netogc_BinaryLogicOpType_httpwww_opengis_netogccomparisonOps', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 49, 3), )

    
    comparisonOps = property(__comparisonOps.value, __comparisonOps.set, None, None)

    
    # Element {http://www.opengis.net/ogc}spatialOps uses Python identifier spatialOps
    __spatialOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'spatialOps'), 'spatialOps', '__httpwww_opengis_netogc_BinaryLogicOpType_httpwww_opengis_netogcspatialOps', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 80, 3), )

    
    spatialOps = property(__spatialOps.value, __spatialOps.set, None, None)

    
    # Element {http://www.opengis.net/ogc}logicOps uses Python identifier logicOps
    __logicOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'logicOps'), 'logicOps', '__httpwww_opengis_netogc_BinaryLogicOpType_httpwww_opengis_netogclogicOps', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 115, 3), )

    
    logicOps = property(__logicOps.value, __logicOps.set, None, None)

    _ElementMap.update({
        __Function.name() : __Function,
        __comparisonOps.name() : __comparisonOps,
        __spatialOps.name() : __spatialOps,
        __logicOps.name() : __logicOps
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BinaryLogicOpType = BinaryLogicOpType
Namespace.addCategoryObject('typeBinding', 'BinaryLogicOpType', BinaryLogicOpType)


# Complex type {http://www.opengis.net/ogc}UnaryLogicOpType with content type ELEMENT_ONLY
class UnaryLogicOpType (LogicOpsType):
    """Complex type {http://www.opengis.net/ogc}UnaryLogicOpType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnaryLogicOpType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 251, 3)
    _ElementMap = LogicOpsType._ElementMap.copy()
    _AttributeMap = LogicOpsType._AttributeMap.copy()
    # Base type is LogicOpsType
    
    # Element {http://www.opengis.net/ogc}Function uses Python identifier Function
    __Function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Function'), 'Function', '__httpwww_opengis_netogc_UnaryLogicOpType_httpwww_opengis_netogcFunction', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 25, 3), )

    
    Function = property(__Function.value, __Function.set, None, None)

    
    # Element {http://www.opengis.net/ogc}comparisonOps uses Python identifier comparisonOps
    __comparisonOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps'), 'comparisonOps', '__httpwww_opengis_netogc_UnaryLogicOpType_httpwww_opengis_netogccomparisonOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 49, 3), )

    
    comparisonOps = property(__comparisonOps.value, __comparisonOps.set, None, None)

    
    # Element {http://www.opengis.net/ogc}spatialOps uses Python identifier spatialOps
    __spatialOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'spatialOps'), 'spatialOps', '__httpwww_opengis_netogc_UnaryLogicOpType_httpwww_opengis_netogcspatialOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 80, 3), )

    
    spatialOps = property(__spatialOps.value, __spatialOps.set, None, None)

    
    # Element {http://www.opengis.net/ogc}logicOps uses Python identifier logicOps
    __logicOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'logicOps'), 'logicOps', '__httpwww_opengis_netogc_UnaryLogicOpType_httpwww_opengis_netogclogicOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 115, 3), )

    
    logicOps = property(__logicOps.value, __logicOps.set, None, None)

    _ElementMap.update({
        __Function.name() : __Function,
        __comparisonOps.name() : __comparisonOps,
        __spatialOps.name() : __spatialOps,
        __logicOps.name() : __logicOps
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UnaryLogicOpType = UnaryLogicOpType
Namespace.addCategoryObject('typeBinding', 'UnaryLogicOpType', UnaryLogicOpType)


# Complex type {http://www.opengis.net/ogc}SpatialOperatorType with content type ELEMENT_ONLY
class SpatialOperatorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/ogc}SpatialOperatorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpatialOperatorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 76, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ogc}GeometryOperands uses Python identifier GeometryOperands
    __GeometryOperands = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperands'), 'GeometryOperands', '__httpwww_opengis_netogc_SpatialOperatorType_httpwww_opengis_netogcGeometryOperands', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 78, 9), )

    
    GeometryOperands = property(__GeometryOperands.value, __GeometryOperands.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netogc_SpatialOperatorType_name', _module_typeBindings.SpatialOperatorNameType)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 82, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 82, 6)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __GeometryOperands.name() : __GeometryOperands
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.SpatialOperatorType = SpatialOperatorType
Namespace.addCategoryObject('typeBinding', 'SpatialOperatorType', SpatialOperatorType)


expression = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), ExpressionType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 29, 3))
Namespace.addCategoryObject('elementBinding', expression.name().localName(), expression)

Id = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_Id'), AbstractIdType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 31, 3))
Namespace.addCategoryObject('elementBinding', Id.name().localName(), Id)

Filter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Filter'), FilterType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 39, 3))
Namespace.addCategoryObject('elementBinding', Filter.name().localName(), Filter)

comparisonOps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps'), ComparisonOpsType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 49, 3))
Namespace.addCategoryObject('elementBinding', comparisonOps.name().localName(), comparisonOps)

spatialOps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'spatialOps'), SpatialOpsType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 80, 3))
Namespace.addCategoryObject('elementBinding', spatialOps.name().localName(), spatialOps)

logicOps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'logicOps'), LogicOpsType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 115, 3))
Namespace.addCategoryObject('elementBinding', logicOps.name().localName(), logicOps)

Filter_Capabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Filter_Capabilities'), CTD_ANON, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 20, 3))
Namespace.addCategoryObject('elementBinding', Filter_Capabilities.name().localName(), Filter_Capabilities)

LogicalOperators = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LogicalOperators'), CTD_ANON_, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 111, 3))
Namespace.addCategoryObject('elementBinding', LogicalOperators.name().localName(), LogicalOperators)

SimpleArithmetic = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleArithmetic'), CTD_ANON_2, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 139, 3))
Namespace.addCategoryObject('elementBinding', SimpleArithmetic.name().localName(), SimpleArithmetic)

EID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EID'), CTD_ANON_3, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 165, 3))
Namespace.addCategoryObject('elementBinding', EID.name().localName(), EID)

FID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FID'), CTD_ANON_4, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 168, 3))
Namespace.addCategoryObject('elementBinding', FID.name().localName(), FID)

SortBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SortBy'), SortByType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/sort.xsd', 21, 3))
Namespace.addCategoryObject('elementBinding', SortBy.name().localName(), SortBy)

Add = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Add'), BinaryOperatorType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 15, 3))
Namespace.addCategoryObject('elementBinding', Add.name().localName(), Add)

Sub = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Sub'), BinaryOperatorType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 17, 3))
Namespace.addCategoryObject('elementBinding', Sub.name().localName(), Sub)

Mul = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Mul'), BinaryOperatorType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 19, 3))
Namespace.addCategoryObject('elementBinding', Mul.name().localName(), Mul)

Div = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Div'), BinaryOperatorType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 21, 3))
Namespace.addCategoryObject('elementBinding', Div.name().localName(), Div)

PropertyName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), PropertyNameType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 23, 3))
Namespace.addCategoryObject('elementBinding', PropertyName.name().localName(), PropertyName)

Function = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Function'), FunctionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 25, 3))
Namespace.addCategoryObject('elementBinding', Function.name().localName(), Function)

Literal = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Literal'), LiteralType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 27, 3))
Namespace.addCategoryObject('elementBinding', Literal.name().localName(), Literal)

FeatureId = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FeatureId'), FeatureIdType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 32, 3))
Namespace.addCategoryObject('elementBinding', FeatureId.name().localName(), FeatureId)

GmlObjectId = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GmlObjectId'), GmlObjectIdType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 35, 3))
Namespace.addCategoryObject('elementBinding', GmlObjectId.name().localName(), GmlObjectId)

PropertyIsEqualTo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsEqualTo'), BinaryComparisonOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 52, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsEqualTo.name().localName(), PropertyIsEqualTo)

PropertyIsNotEqualTo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsNotEqualTo'), BinaryComparisonOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 55, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsNotEqualTo.name().localName(), PropertyIsNotEqualTo)

PropertyIsLessThan = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsLessThan'), BinaryComparisonOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 58, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsLessThan.name().localName(), PropertyIsLessThan)

PropertyIsGreaterThan = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsGreaterThan'), BinaryComparisonOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 61, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsGreaterThan.name().localName(), PropertyIsGreaterThan)

PropertyIsLessThanOrEqualTo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsLessThanOrEqualTo'), BinaryComparisonOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 64, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsLessThanOrEqualTo.name().localName(), PropertyIsLessThanOrEqualTo)

PropertyIsGreaterThanOrEqualTo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsGreaterThanOrEqualTo'), BinaryComparisonOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 67, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsGreaterThanOrEqualTo.name().localName(), PropertyIsGreaterThanOrEqualTo)

PropertyIsLike = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsLike'), PropertyIsLikeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 70, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsLike.name().localName(), PropertyIsLike)

PropertyIsNull = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsNull'), PropertyIsNullType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 73, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsNull.name().localName(), PropertyIsNull)

PropertyIsBetween = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsBetween'), PropertyIsBetweenType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 76, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsBetween.name().localName(), PropertyIsBetween)

Equals = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Equals'), BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 81, 3))
Namespace.addCategoryObject('elementBinding', Equals.name().localName(), Equals)

Disjoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Disjoint'), BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 84, 3))
Namespace.addCategoryObject('elementBinding', Disjoint.name().localName(), Disjoint)

Touches = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Touches'), BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 87, 3))
Namespace.addCategoryObject('elementBinding', Touches.name().localName(), Touches)

Within = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Within'), BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 90, 3))
Namespace.addCategoryObject('elementBinding', Within.name().localName(), Within)

Overlaps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Overlaps'), BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 93, 3))
Namespace.addCategoryObject('elementBinding', Overlaps.name().localName(), Overlaps)

Crosses = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Crosses'), BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 96, 3))
Namespace.addCategoryObject('elementBinding', Crosses.name().localName(), Crosses)

Intersects = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Intersects'), BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 99, 3))
Namespace.addCategoryObject('elementBinding', Intersects.name().localName(), Intersects)

Contains = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contains'), BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 102, 3))
Namespace.addCategoryObject('elementBinding', Contains.name().localName(), Contains)

DWithin = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DWithin'), DistanceBufferType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 105, 3))
Namespace.addCategoryObject('elementBinding', DWithin.name().localName(), DWithin)

Beyond = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Beyond'), DistanceBufferType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 108, 3))
Namespace.addCategoryObject('elementBinding', Beyond.name().localName(), Beyond)

BBOX = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BBOX'), BBOXType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 111, 3))
Namespace.addCategoryObject('elementBinding', BBOX.name().localName(), BBOX)

And = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'And'), BinaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 116, 3))
Namespace.addCategoryObject('elementBinding', And.name().localName(), And)

Or = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Or'), BinaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 119, 3))
Namespace.addCategoryObject('elementBinding', Or.name().localName(), Or)

Not = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Not'), UnaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 122, 3))
Namespace.addCategoryObject('elementBinding', Not.name().localName(), Not)



FilterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_Id'), AbstractIdType, abstract=pyxb.binding.datatypes.boolean(1), scope=FilterType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 31, 3)))

FilterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps'), ComparisonOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=FilterType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 49, 3)))

FilterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'spatialOps'), SpatialOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=FilterType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 80, 3)))

FilterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'logicOps'), LogicOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=FilterType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 115, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FilterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'spatialOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 42, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FilterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 43, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FilterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'logicOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 44, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FilterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_Id')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 45, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FilterType._Automaton = _BuildAutomaton()




LowerBoundaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), ExpressionType, abstract=pyxb.binding.datatypes.boolean(1), scope=LowerBoundaryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 29, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LowerBoundaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 189, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LowerBoundaryType._Automaton = _BuildAutomaton_()




UpperBoundaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), ExpressionType, abstract=pyxb.binding.datatypes.boolean(1), scope=UpperBoundaryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 29, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UpperBoundaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 194, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UpperBoundaryType._Automaton = _BuildAutomaton_2()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Spatial_Capabilities'), Spatial_CapabilitiesType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 23, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Scalar_Capabilities'), Scalar_CapabilitiesType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 25, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id_Capabilities'), Id_CapabilitiesType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 27, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Spatial_Capabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 23, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Scalar_Capabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 25, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id_Capabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 27, 12))
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
CTD_ANON._Automaton = _BuildAutomaton_3()




Spatial_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperands'), GeometryOperandsType, scope=Spatial_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 34, 9)))

Spatial_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SpatialOperators'), SpatialOperatorsType, scope=Spatial_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 36, 9)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Spatial_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperands')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 34, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Spatial_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SpatialOperators')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 36, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Spatial_CapabilitiesType._Automaton = _BuildAutomaton_4()




GeometryOperandsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperand'), GeometryOperandType, scope=GeometryOperandsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 42, 9)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeometryOperandsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperand')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 42, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GeometryOperandsType._Automaton = _BuildAutomaton_5()




SpatialOperatorsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SpatialOperator'), SpatialOperatorType, scope=SpatialOperatorsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 71, 9)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SpatialOperatorsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SpatialOperator')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 71, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SpatialOperatorsType._Automaton = _BuildAutomaton_6()




Scalar_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ComparisonOperators'), ComparisonOperatorsType, scope=Scalar_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 103, 9)))

Scalar_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ArithmeticOperators'), ArithmeticOperatorsType, scope=Scalar_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 106, 9)))

Scalar_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LogicalOperators'), CTD_ANON_, scope=Scalar_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 111, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 101, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 103, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 106, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Scalar_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LogicalOperators')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 101, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Scalar_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ComparisonOperators')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 103, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Scalar_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ArithmeticOperators')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 106, 9))
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
Scalar_CapabilitiesType._Automaton = _BuildAutomaton_7()




ComparisonOperatorsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ComparisonOperator'), ComparisonOperatorType, scope=ComparisonOperatorsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 116, 9)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ComparisonOperatorsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ComparisonOperator')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 116, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ComparisonOperatorsType._Automaton = _BuildAutomaton_8()




ArithmeticOperatorsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Functions'), FunctionsType, scope=ArithmeticOperatorsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 136, 9)))

ArithmeticOperatorsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleArithmetic'), CTD_ANON_2, scope=ArithmeticOperatorsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 139, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ArithmeticOperatorsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SimpleArithmetic')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 135, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ArithmeticOperatorsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Functions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 136, 9))
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
ArithmeticOperatorsType._Automaton = _BuildAutomaton_9()




FunctionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FunctionNames'), FunctionNamesType, scope=FunctionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 144, 9)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FunctionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FunctionNames')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 144, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FunctionsType._Automaton = _BuildAutomaton_10()




FunctionNamesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FunctionName'), FunctionNameType, scope=FunctionNamesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 149, 9)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FunctionNamesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FunctionName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 149, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FunctionNamesType._Automaton = _BuildAutomaton_11()




Id_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EID'), CTD_ANON_3, scope=Id_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 165, 3)))

Id_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FID'), CTD_ANON_4, scope=Id_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 168, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Id_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EID')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 161, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Id_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FID')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 162, 9))
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
Id_CapabilitiesType._Automaton = _BuildAutomaton_12()




SortByType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SortProperty'), SortPropertyType, scope=SortByType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/sort.xsd', 28, 9)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SortByType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SortProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/sort.xsd', 28, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SortByType._Automaton = _BuildAutomaton_13()




SortPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), PropertyNameType, scope=SortPropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 23, 3)))

SortPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SortOrder'), SortOrderType, scope=SortPropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/sort.xsd', 36, 9)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/sort.xsd', 36, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SortPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PropertyName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/sort.xsd', 35, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SortPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SortOrder')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/sort.xsd', 36, 9))
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
SortPropertyType._Automaton = _BuildAutomaton_14()




BinaryOperatorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), ExpressionType, abstract=pyxb.binding.datatypes.boolean(1), scope=BinaryOperatorType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 29, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=2, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 37, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BinaryOperatorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 37, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BinaryOperatorType._Automaton = _BuildAutomaton_15()




FunctionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), ExpressionType, abstract=pyxb.binding.datatypes.boolean(1), scope=FunctionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 29, 3)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 46, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FunctionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 46, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FunctionType._Automaton = _BuildAutomaton_16()




def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 57, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 57, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LiteralType._Automaton = _BuildAutomaton_17()




def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
PropertyNameType._Automaton = _BuildAutomaton_18()




BinaryComparisonOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), ExpressionType, abstract=pyxb.binding.datatypes.boolean(1), scope=BinaryComparisonOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 29, 3)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=2, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 145, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BinaryComparisonOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 145, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BinaryComparisonOpType._Automaton = _BuildAutomaton_19()




PropertyIsLikeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), PropertyNameType, scope=PropertyIsLikeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 23, 3)))

PropertyIsLikeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Literal'), LiteralType, scope=PropertyIsLikeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 27, 3)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PropertyIsLikeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PropertyName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 156, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PropertyIsLikeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Literal')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 157, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PropertyIsLikeType._Automaton = _BuildAutomaton_20()




PropertyIsNullType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), PropertyNameType, scope=PropertyIsNullType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 23, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PropertyIsNullType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PropertyName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 171, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PropertyIsNullType._Automaton = _BuildAutomaton_21()




PropertyIsBetweenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), ExpressionType, abstract=pyxb.binding.datatypes.boolean(1), scope=PropertyIsBetweenType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 29, 3)))

PropertyIsBetweenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LowerBoundary'), LowerBoundaryType, scope=PropertyIsBetweenType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 181, 15)))

PropertyIsBetweenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UpperBoundary'), UpperBoundaryType, scope=PropertyIsBetweenType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 182, 15)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PropertyIsBetweenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 180, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PropertyIsBetweenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LowerBoundary')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 181, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PropertyIsBetweenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UpperBoundary')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 182, 15))
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
PropertyIsBetweenType._Automaton = _BuildAutomaton_22()




BinarySpatialOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, '_Geometry'), pyxb.bundles.opengis.gml.AbstractGeometryType, abstract=pyxb.binding.datatypes.boolean(1), scope=BinarySpatialOpType, documentation='The "_Geometry" element is the abstract head of the substituition group for all geometry elements of GML 3. This \n\t\t\tincludes pre-defined and user-defined geometry elements. Any geometry element must be a direct or indirect extension/restriction \n\t\t\tof AbstractGeometryType and must be directly or indirectly in the substitution group of "_Geometry".', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/geometryBasic0d1d.xsd', 39, 1)))

BinarySpatialOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'Envelope'), pyxb.bundles.opengis.gml.EnvelopeType, scope=BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/geometryBasic0d1d.xsd', 519, 1)))

BinarySpatialOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), PropertyNameType, scope=BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 23, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BinarySpatialOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PropertyName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 201, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BinarySpatialOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PropertyName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 203, 18))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BinarySpatialOpType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, '_Geometry')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 204, 18))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BinarySpatialOpType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'Envelope')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 205, 18))
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
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BinarySpatialOpType._Automaton = _BuildAutomaton_23()




BBOXType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'Envelope'), pyxb.bundles.opengis.gml.EnvelopeType, scope=BBOXType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/geometryBasic0d1d.xsd', 519, 1)))

BBOXType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), PropertyNameType, scope=BBOXType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 23, 3)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 215, 15))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BBOXType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PropertyName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 215, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BBOXType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'Envelope')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 216, 15))
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
BBOXType._Automaton = _BuildAutomaton_24()




DistanceBufferType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, '_Geometry'), pyxb.bundles.opengis.gml.AbstractGeometryType, abstract=pyxb.binding.datatypes.boolean(1), scope=DistanceBufferType, documentation='The "_Geometry" element is the abstract head of the substituition group for all geometry elements of GML 3. This \n\t\t\tincludes pre-defined and user-defined geometry elements. Any geometry element must be a direct or indirect extension/restriction \n\t\t\tof AbstractGeometryType and must be directly or indirectly in the substitution group of "_Geometry".', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/geometryBasic0d1d.xsd', 39, 1)))

DistanceBufferType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyName'), PropertyNameType, scope=DistanceBufferType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 23, 3)))

DistanceBufferType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Distance'), DistanceType, scope=DistanceBufferType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 227, 15)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DistanceBufferType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PropertyName')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 225, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DistanceBufferType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, '_Geometry')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 226, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DistanceBufferType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Distance')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 227, 15))
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
DistanceBufferType._Automaton = _BuildAutomaton_25()




BinaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Function'), FunctionType, scope=BinaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 25, 3)))

BinaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps'), ComparisonOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=BinaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 49, 3)))

BinaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'spatialOps'), SpatialOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=BinaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 80, 3)))

BinaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'logicOps'), LogicOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=BinaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 115, 3)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 242, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BinaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 243, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BinaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'spatialOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 244, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BinaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'logicOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 245, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BinaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Function')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 246, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BinaryLogicOpType._Automaton = _BuildAutomaton_26()




UnaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Function'), FunctionType, scope=UnaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/expr.xsd', 25, 3)))

UnaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps'), ComparisonOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=UnaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 49, 3)))

UnaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'spatialOps'), SpatialOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=UnaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 80, 3)))

UnaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'logicOps'), LogicOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=UnaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 115, 3)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 256, 18))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'spatialOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 257, 18))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'logicOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 258, 18))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Function')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filter.xsd', 259, 18))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UnaryLogicOpType._Automaton = _BuildAutomaton_27()




SpatialOperatorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperands'), GeometryOperandsType, scope=SpatialOperatorType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 78, 9)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 78, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SpatialOperatorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperands')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/1.1.0/filterCapabilities.xsd', 78, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SpatialOperatorType._Automaton = _BuildAutomaton_28()


Add._setSubstitutionGroup(expression)

Sub._setSubstitutionGroup(expression)

Mul._setSubstitutionGroup(expression)

Div._setSubstitutionGroup(expression)

PropertyName._setSubstitutionGroup(expression)

Function._setSubstitutionGroup(expression)

Literal._setSubstitutionGroup(expression)

FeatureId._setSubstitutionGroup(Id)

GmlObjectId._setSubstitutionGroup(Id)

PropertyIsEqualTo._setSubstitutionGroup(comparisonOps)

PropertyIsNotEqualTo._setSubstitutionGroup(comparisonOps)

PropertyIsLessThan._setSubstitutionGroup(comparisonOps)

PropertyIsGreaterThan._setSubstitutionGroup(comparisonOps)

PropertyIsLessThanOrEqualTo._setSubstitutionGroup(comparisonOps)

PropertyIsGreaterThanOrEqualTo._setSubstitutionGroup(comparisonOps)

PropertyIsLike._setSubstitutionGroup(comparisonOps)

PropertyIsNull._setSubstitutionGroup(comparisonOps)

PropertyIsBetween._setSubstitutionGroup(comparisonOps)

Equals._setSubstitutionGroup(spatialOps)

Disjoint._setSubstitutionGroup(spatialOps)

Touches._setSubstitutionGroup(spatialOps)

Within._setSubstitutionGroup(spatialOps)

Overlaps._setSubstitutionGroup(spatialOps)

Crosses._setSubstitutionGroup(spatialOps)

Intersects._setSubstitutionGroup(spatialOps)

Contains._setSubstitutionGroup(spatialOps)

DWithin._setSubstitutionGroup(spatialOps)

Beyond._setSubstitutionGroup(spatialOps)

BBOX._setSubstitutionGroup(spatialOps)

And._setSubstitutionGroup(logicOps)

Or._setSubstitutionGroup(logicOps)

Not._setSubstitutionGroup(logicOps)
