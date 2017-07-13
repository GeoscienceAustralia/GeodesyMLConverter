# ./pyxb/bundles/opengis/gml_3_3/raw/ce.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:675695c849daf6048aa7ed519f7cd30ab1b72135
# Generated 2017-07-10 00:38:05.933207 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/gml/3.3/ce

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
import pyxb.bundles.opengis.gml_3_2
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/gml/3.3/ce', create_if_missing=True)
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


# Complex type {http://www.opengis.net/gml/3.3/ce}SimplePolygonType with content type ELEMENT_ONLY
class SimplePolygonType (pyxb.bundles.opengis.gml_3_2.AbstractSurfaceType):
    """Complex type {http://www.opengis.net/gml/3.3/ce}SimplePolygonType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimplePolygonType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 16, 2)
    _ElementMap = pyxb.bundles.opengis.gml_3_2.AbstractSurfaceType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_2.AbstractSurfaceType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_2.AbstractSurfaceType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/gml/3.2}pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), 'pos', '__httpwww_opengis_netgml3_3ce_SimplePolygonType_httpwww_opengis_netgml3_2pos', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1), )

    
    pos = property(__pos.value, __pos.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}posList uses Python identifier posList
    __posList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), 'posList', '__httpwww_opengis_netgml3_3ce_SimplePolygonType_httpwww_opengis_netgml3_2posList', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1), )

    
    posList = property(__posList.value, __posList.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}pointProperty uses Python identifier pointProperty
    __pointProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), 'pointProperty', '__httpwww_opengis_netgml3_3ce_SimplePolygonType_httpwww_opengis_netgml3_2pointProperty', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1), )

    
    pointProperty = property(__pointProperty.value, __pointProperty.set, None, 'This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.')

    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Attribute srsName inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute srsDimension inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute axisLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute uomLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    _ElementMap.update({
        __pos.name() : __pos,
        __posList.name() : __posList,
        __pointProperty.name() : __pointProperty
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SimplePolygonType = SimplePolygonType
Namespace.addCategoryObject('typeBinding', 'SimplePolygonType', SimplePolygonType)


# Complex type {http://www.opengis.net/gml/3.3/ce}SimpleRectangleType with content type ELEMENT_ONLY
class SimpleRectangleType (pyxb.bundles.opengis.gml_3_2.AbstractSurfaceType):
    """Complex type {http://www.opengis.net/gml/3.3/ce}SimpleRectangleType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleRectangleType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 36, 2)
    _ElementMap = pyxb.bundles.opengis.gml_3_2.AbstractSurfaceType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_2.AbstractSurfaceType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_2.AbstractSurfaceType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/gml/3.2}pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), 'pos', '__httpwww_opengis_netgml3_3ce_SimpleRectangleType_httpwww_opengis_netgml3_2pos', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1), )

    
    pos = property(__pos.value, __pos.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}posList uses Python identifier posList
    __posList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), 'posList', '__httpwww_opengis_netgml3_3ce_SimpleRectangleType_httpwww_opengis_netgml3_2posList', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1), )

    
    posList = property(__posList.value, __posList.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}pointProperty uses Python identifier pointProperty
    __pointProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), 'pointProperty', '__httpwww_opengis_netgml3_3ce_SimpleRectangleType_httpwww_opengis_netgml3_2pointProperty', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1), )

    
    pointProperty = property(__pointProperty.value, __pointProperty.set, None, 'This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.')

    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Attribute srsName inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute srsDimension inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute axisLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute uomLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    _ElementMap.update({
        __pos.name() : __pos,
        __posList.name() : __posList,
        __pointProperty.name() : __pointProperty
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SimpleRectangleType = SimpleRectangleType
Namespace.addCategoryObject('typeBinding', 'SimpleRectangleType', SimpleRectangleType)


# Complex type {http://www.opengis.net/gml/3.3/ce}SimpleTriangleType with content type ELEMENT_ONLY
class SimpleTriangleType (pyxb.bundles.opengis.gml_3_2.AbstractSurfaceType):
    """Complex type {http://www.opengis.net/gml/3.3/ce}SimpleTriangleType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleTriangleType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 56, 2)
    _ElementMap = pyxb.bundles.opengis.gml_3_2.AbstractSurfaceType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_2.AbstractSurfaceType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_2.AbstractSurfaceType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/gml/3.2}pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), 'pos', '__httpwww_opengis_netgml3_3ce_SimpleTriangleType_httpwww_opengis_netgml3_2pos', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1), )

    
    pos = property(__pos.value, __pos.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}posList uses Python identifier posList
    __posList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), 'posList', '__httpwww_opengis_netgml3_3ce_SimpleTriangleType_httpwww_opengis_netgml3_2posList', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1), )

    
    posList = property(__posList.value, __posList.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}pointProperty uses Python identifier pointProperty
    __pointProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), 'pointProperty', '__httpwww_opengis_netgml3_3ce_SimpleTriangleType_httpwww_opengis_netgml3_2pointProperty', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1), )

    
    pointProperty = property(__pointProperty.value, __pointProperty.set, None, 'This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.')

    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Attribute srsName inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute srsDimension inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute axisLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute uomLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    _ElementMap.update({
        __pos.name() : __pos,
        __posList.name() : __posList,
        __pointProperty.name() : __pointProperty
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SimpleTriangleType = SimpleTriangleType
Namespace.addCategoryObject('typeBinding', 'SimpleTriangleType', SimpleTriangleType)


# Complex type {http://www.opengis.net/gml/3.3/ce}SimpleArcStringType with content type ELEMENT_ONLY
class SimpleArcStringType (pyxb.bundles.opengis.gml_3_2.AbstractCurveType):
    """Complex type {http://www.opengis.net/gml/3.3/ce}SimpleArcStringType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleArcStringType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 81, 2)
    _ElementMap = pyxb.bundles.opengis.gml_3_2.AbstractCurveType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_2.AbstractCurveType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_2.AbstractCurveType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/gml/3.2}pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), 'pos', '__httpwww_opengis_netgml3_3ce_SimpleArcStringType_httpwww_opengis_netgml3_2pos', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1), )

    
    pos = property(__pos.value, __pos.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}posList uses Python identifier posList
    __posList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), 'posList', '__httpwww_opengis_netgml3_3ce_SimpleArcStringType_httpwww_opengis_netgml3_2posList', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1), )

    
    posList = property(__posList.value, __posList.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}pointProperty uses Python identifier pointProperty
    __pointProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), 'pointProperty', '__httpwww_opengis_netgml3_3ce_SimpleArcStringType_httpwww_opengis_netgml3_2pointProperty', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1), )

    
    pointProperty = property(__pointProperty.value, __pointProperty.set, None, 'This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.')

    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Attribute srsName inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute srsDimension inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute axisLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute uomLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Attribute interpolation uses Python identifier interpolation
    __interpolation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'interpolation'), 'interpolation', '__httpwww_opengis_netgml3_3ce_SimpleArcStringType_interpolation', pyxb.bundles.opengis.gml_3_2.CurveInterpolationType, fixed=True, unicode_default='circularArc3Points')
    __interpolation._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 93, 8)
    __interpolation._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 93, 8)
    
    interpolation = property(__interpolation.value, __interpolation.set, None, None)

    
    # Attribute numArc uses Python identifier numArc
    __numArc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numArc'), 'numArc', '__httpwww_opengis_netgml3_3ce_SimpleArcStringType_numArc', pyxb.binding.datatypes.integer)
    __numArc._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 94, 8)
    __numArc._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 94, 8)
    
    numArc = property(__numArc.value, __numArc.set, None, None)

    _ElementMap.update({
        __pos.name() : __pos,
        __posList.name() : __posList,
        __pointProperty.name() : __pointProperty
    })
    _AttributeMap.update({
        __interpolation.name() : __interpolation,
        __numArc.name() : __numArc
    })
_module_typeBindings.SimpleArcStringType = SimpleArcStringType
Namespace.addCategoryObject('typeBinding', 'SimpleArcStringType', SimpleArcStringType)


# Complex type {http://www.opengis.net/gml/3.3/ce}SimpleArcType with content type ELEMENT_ONLY
class SimpleArcType (pyxb.bundles.opengis.gml_3_2.AbstractCurveType):
    """Complex type {http://www.opengis.net/gml/3.3/ce}SimpleArcType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleArcType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 103, 2)
    _ElementMap = pyxb.bundles.opengis.gml_3_2.AbstractCurveType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_2.AbstractCurveType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_2.AbstractCurveType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/gml/3.2}pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), 'pos', '__httpwww_opengis_netgml3_3ce_SimpleArcType_httpwww_opengis_netgml3_2pos', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1), )

    
    pos = property(__pos.value, __pos.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}posList uses Python identifier posList
    __posList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), 'posList', '__httpwww_opengis_netgml3_3ce_SimpleArcType_httpwww_opengis_netgml3_2posList', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1), )

    
    posList = property(__posList.value, __posList.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}pointProperty uses Python identifier pointProperty
    __pointProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), 'pointProperty', '__httpwww_opengis_netgml3_3ce_SimpleArcType_httpwww_opengis_netgml3_2pointProperty', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1), )

    
    pointProperty = property(__pointProperty.value, __pointProperty.set, None, 'This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.')

    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Attribute srsName inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute srsDimension inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute axisLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute uomLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Attribute interpolation uses Python identifier interpolation
    __interpolation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'interpolation'), 'interpolation', '__httpwww_opengis_netgml3_3ce_SimpleArcType_interpolation', pyxb.bundles.opengis.gml_3_2.CurveInterpolationType, fixed=True, unicode_default='circularArc3Points')
    __interpolation._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 115, 8)
    __interpolation._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 115, 8)
    
    interpolation = property(__interpolation.value, __interpolation.set, None, None)

    
    # Attribute numArc uses Python identifier numArc
    __numArc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numArc'), 'numArc', '__httpwww_opengis_netgml3_3ce_SimpleArcType_numArc', pyxb.binding.datatypes.integer, fixed=True, unicode_default='1')
    __numArc._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 116, 8)
    __numArc._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 116, 8)
    
    numArc = property(__numArc.value, __numArc.set, None, None)

    _ElementMap.update({
        __pos.name() : __pos,
        __posList.name() : __posList,
        __pointProperty.name() : __pointProperty
    })
    _AttributeMap.update({
        __interpolation.name() : __interpolation,
        __numArc.name() : __numArc
    })
_module_typeBindings.SimpleArcType = SimpleArcType
Namespace.addCategoryObject('typeBinding', 'SimpleArcType', SimpleArcType)


# Complex type {http://www.opengis.net/gml/3.3/ce}SimpleArcByCenterPointType with content type ELEMENT_ONLY
class SimpleArcByCenterPointType (pyxb.bundles.opengis.gml_3_2.AbstractCurveType):
    """Complex type {http://www.opengis.net/gml/3.3/ce}SimpleArcByCenterPointType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleArcByCenterPointType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 125, 2)
    _ElementMap = pyxb.bundles.opengis.gml_3_2.AbstractCurveType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_2.AbstractCurveType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_2.AbstractCurveType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/gml/3.2}pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), 'pos', '__httpwww_opengis_netgml3_3ce_SimpleArcByCenterPointType_httpwww_opengis_netgml3_2pos', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1), )

    
    pos = property(__pos.value, __pos.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}posList uses Python identifier posList
    __posList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), 'posList', '__httpwww_opengis_netgml3_3ce_SimpleArcByCenterPointType_httpwww_opengis_netgml3_2posList', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1), )

    
    posList = property(__posList.value, __posList.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}pointProperty uses Python identifier pointProperty
    __pointProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), 'pointProperty', '__httpwww_opengis_netgml3_3ce_SimpleArcByCenterPointType_httpwww_opengis_netgml3_2pointProperty', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1), )

    
    pointProperty = property(__pointProperty.value, __pointProperty.set, None, 'This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.')

    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/gml/3.3/ce}radius uses Python identifier radius
    __radius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'radius'), 'radius', '__httpwww_opengis_netgml3_3ce_SimpleArcByCenterPointType_httpwww_opengis_netgml3_3ceradius', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 136, 10), )

    
    radius = property(__radius.value, __radius.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.3/ce}startAngle uses Python identifier startAngle
    __startAngle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startAngle'), 'startAngle', '__httpwww_opengis_netgml3_3ce_SimpleArcByCenterPointType_httpwww_opengis_netgml3_3cestartAngle', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 138, 10), )

    
    startAngle = property(__startAngle.value, __startAngle.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.3/ce}endAngle uses Python identifier endAngle
    __endAngle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endAngle'), 'endAngle', '__httpwww_opengis_netgml3_3ce_SimpleArcByCenterPointType_httpwww_opengis_netgml3_3ceendAngle', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 139, 10), )

    
    endAngle = property(__endAngle.value, __endAngle.set, None, None)

    
    # Attribute srsName inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute srsDimension inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute axisLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute uomLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Attribute interpolation uses Python identifier interpolation
    __interpolation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'interpolation'), 'interpolation', '__httpwww_opengis_netgml3_3ce_SimpleArcByCenterPointType_interpolation', pyxb.bundles.opengis.gml_3_2.CurveInterpolationType, fixed=True, unicode_default='circularArcCenterPointWithRadius')
    __interpolation._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 141, 8)
    __interpolation._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 141, 8)
    
    interpolation = property(__interpolation.value, __interpolation.set, None, None)

    
    # Attribute numArc uses Python identifier numArc
    __numArc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numArc'), 'numArc', '__httpwww_opengis_netgml3_3ce_SimpleArcByCenterPointType_numArc', pyxb.binding.datatypes.integer, fixed=True, unicode_default='1', required=True)
    __numArc._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 142, 8)
    __numArc._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 142, 8)
    
    numArc = property(__numArc.value, __numArc.set, None, None)

    _ElementMap.update({
        __pos.name() : __pos,
        __posList.name() : __posList,
        __pointProperty.name() : __pointProperty,
        __radius.name() : __radius,
        __startAngle.name() : __startAngle,
        __endAngle.name() : __endAngle
    })
    _AttributeMap.update({
        __interpolation.name() : __interpolation,
        __numArc.name() : __numArc
    })
_module_typeBindings.SimpleArcByCenterPointType = SimpleArcByCenterPointType
Namespace.addCategoryObject('typeBinding', 'SimpleArcByCenterPointType', SimpleArcByCenterPointType)


# Complex type {http://www.opengis.net/gml/3.3/ce}SimpleArcStringByBulgeType with content type ELEMENT_ONLY
class SimpleArcStringByBulgeType (pyxb.bundles.opengis.gml_3_2.AbstractCurveType):
    """Complex type {http://www.opengis.net/gml/3.3/ce}SimpleArcStringByBulgeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleArcStringByBulgeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 151, 2)
    _ElementMap = pyxb.bundles.opengis.gml_3_2.AbstractCurveType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_2.AbstractCurveType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_2.AbstractCurveType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/gml/3.2}pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), 'pos', '__httpwww_opengis_netgml3_3ce_SimpleArcStringByBulgeType_httpwww_opengis_netgml3_2pos', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1), )

    
    pos = property(__pos.value, __pos.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}posList uses Python identifier posList
    __posList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), 'posList', '__httpwww_opengis_netgml3_3ce_SimpleArcStringByBulgeType_httpwww_opengis_netgml3_2posList', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1), )

    
    posList = property(__posList.value, __posList.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}pointProperty uses Python identifier pointProperty
    __pointProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), 'pointProperty', '__httpwww_opengis_netgml3_3ce_SimpleArcStringByBulgeType_httpwww_opengis_netgml3_2pointProperty', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1), )

    
    pointProperty = property(__pointProperty.value, __pointProperty.set, None, 'This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.')

    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/gml/3.3/ce}bulge uses Python identifier bulge
    __bulge = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bulge'), 'bulge', '__httpwww_opengis_netgml3_3ce_SimpleArcStringByBulgeType_httpwww_opengis_netgml3_3cebulge', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 162, 10), )

    
    bulge = property(__bulge.value, __bulge.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.3/ce}normal uses Python identifier normal
    __normal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'normal'), 'normal', '__httpwww_opengis_netgml3_3ce_SimpleArcStringByBulgeType_httpwww_opengis_netgml3_3cenormal', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 163, 10), )

    
    normal = property(__normal.value, __normal.set, None, None)

    
    # Attribute srsName inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute srsDimension inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute axisLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute uomLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Attribute interpolation uses Python identifier interpolation
    __interpolation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'interpolation'), 'interpolation', '__httpwww_opengis_netgml3_3ce_SimpleArcStringByBulgeType_interpolation', pyxb.bundles.opengis.gml_3_2.CurveInterpolationType, fixed=True, unicode_default='circularArc2PointWithBulge')
    __interpolation._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 165, 8)
    __interpolation._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 165, 8)
    
    interpolation = property(__interpolation.value, __interpolation.set, None, None)

    
    # Attribute numArc uses Python identifier numArc
    __numArc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numArc'), 'numArc', '__httpwww_opengis_netgml3_3ce_SimpleArcStringByBulgeType_numArc', pyxb.binding.datatypes.integer)
    __numArc._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 166, 8)
    __numArc._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 166, 8)
    
    numArc = property(__numArc.value, __numArc.set, None, None)

    _ElementMap.update({
        __pos.name() : __pos,
        __posList.name() : __posList,
        __pointProperty.name() : __pointProperty,
        __bulge.name() : __bulge,
        __normal.name() : __normal
    })
    _AttributeMap.update({
        __interpolation.name() : __interpolation,
        __numArc.name() : __numArc
    })
_module_typeBindings.SimpleArcStringByBulgeType = SimpleArcStringByBulgeType
Namespace.addCategoryObject('typeBinding', 'SimpleArcStringByBulgeType', SimpleArcStringByBulgeType)


# Complex type {http://www.opengis.net/gml/3.3/ce}SimpleArcByBulgeType with content type ELEMENT_ONLY
class SimpleArcByBulgeType (pyxb.bundles.opengis.gml_3_2.AbstractCurveType):
    """Complex type {http://www.opengis.net/gml/3.3/ce}SimpleArcByBulgeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleArcByBulgeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 175, 2)
    _ElementMap = pyxb.bundles.opengis.gml_3_2.AbstractCurveType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_2.AbstractCurveType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_2.AbstractCurveType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/gml/3.2}pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), 'pos', '__httpwww_opengis_netgml3_3ce_SimpleArcByBulgeType_httpwww_opengis_netgml3_2pos', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1), )

    
    pos = property(__pos.value, __pos.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}posList uses Python identifier posList
    __posList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), 'posList', '__httpwww_opengis_netgml3_3ce_SimpleArcByBulgeType_httpwww_opengis_netgml3_2posList', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1), )

    
    posList = property(__posList.value, __posList.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.2}pointProperty uses Python identifier pointProperty
    __pointProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), 'pointProperty', '__httpwww_opengis_netgml3_3ce_SimpleArcByBulgeType_httpwww_opengis_netgml3_2pointProperty', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1), )

    
    pointProperty = property(__pointProperty.value, __pointProperty.set, None, 'This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.')

    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/gml/3.3/ce}bulge uses Python identifier bulge
    __bulge = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bulge'), 'bulge', '__httpwww_opengis_netgml3_3ce_SimpleArcByBulgeType_httpwww_opengis_netgml3_3cebulge', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 186, 10), )

    
    bulge = property(__bulge.value, __bulge.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.3/ce}normal uses Python identifier normal
    __normal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'normal'), 'normal', '__httpwww_opengis_netgml3_3ce_SimpleArcByBulgeType_httpwww_opengis_netgml3_3cenormal', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 187, 10), )

    
    normal = property(__normal.value, __normal.set, None, None)

    
    # Attribute srsName inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute srsDimension inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute axisLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute uomLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Attribute interpolation uses Python identifier interpolation
    __interpolation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'interpolation'), 'interpolation', '__httpwww_opengis_netgml3_3ce_SimpleArcByBulgeType_interpolation', pyxb.bundles.opengis.gml_3_2.CurveInterpolationType, fixed=True, unicode_default='circularArc2PointWithBulge')
    __interpolation._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 189, 8)
    __interpolation._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 189, 8)
    
    interpolation = property(__interpolation.value, __interpolation.set, None, None)

    
    # Attribute numArc uses Python identifier numArc
    __numArc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numArc'), 'numArc', '__httpwww_opengis_netgml3_3ce_SimpleArcByBulgeType_numArc', pyxb.binding.datatypes.integer, fixed=True, unicode_default='1')
    __numArc._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 190, 8)
    __numArc._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 190, 8)
    
    numArc = property(__numArc.value, __numArc.set, None, None)

    _ElementMap.update({
        __pos.name() : __pos,
        __posList.name() : __posList,
        __pointProperty.name() : __pointProperty,
        __bulge.name() : __bulge,
        __normal.name() : __normal
    })
    _AttributeMap.update({
        __interpolation.name() : __interpolation,
        __numArc.name() : __numArc
    })
_module_typeBindings.SimpleArcByBulgeType = SimpleArcByBulgeType
Namespace.addCategoryObject('typeBinding', 'SimpleArcByBulgeType', SimpleArcByBulgeType)


# Complex type {http://www.opengis.net/gml/3.3/ce}SimpleMultiPointType with content type ELEMENT_ONLY
class SimpleMultiPointType (pyxb.bundles.opengis.gml_3_2.AbstractGeometricAggregateType):
    """Complex type {http://www.opengis.net/gml/3.3/ce}SimpleMultiPointType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleMultiPointType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 200, 2)
    _ElementMap = pyxb.bundles.opengis.gml_3_2.AbstractGeometricAggregateType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_2.AbstractGeometricAggregateType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_2.AbstractGeometricAggregateType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/gml/3.2}posList uses Python identifier posList
    __posList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), 'posList', '__httpwww_opengis_netgml3_3ce_SimpleMultiPointType_httpwww_opengis_netgml3_2posList', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1), )

    
    posList = property(__posList.value, __posList.set, None, None)

    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Attribute srsName inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute srsDimension inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute axisLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute uomLabels inherited from {http://www.opengis.net/gml/3.2}AbstractGeometryType
    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Attribute aggregationType inherited from {http://www.opengis.net/gml/3.2}AbstractGeometricAggregateType
    _ElementMap.update({
        __posList.name() : __posList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SimpleMultiPointType = SimpleMultiPointType
Namespace.addCategoryObject('typeBinding', 'SimpleMultiPointType', SimpleMultiPointType)


# Complex type {http://www.opengis.net/gml/3.3/ce}MultiPointPropertyType with content type ELEMENT_ONLY
class MultiPointPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/gml/3.3/ce}MultiPointPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MultiPointPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 210, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.2}MultiPoint uses Python identifier MultiPoint
    __MultiPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'MultiPoint'), 'MultiPoint', '__httpwww_opengis_netgml3_3ce_MultiPointPropertyType_httpwww_opengis_netgml3_2MultiPoint', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryAggregates.xsd', 73, 1), )

    
    MultiPoint = property(__MultiPoint.value, __MultiPoint.set, None, 'A gml:MultiPoint consists of one or more gml:Points.\nThe members of the geometric aggregate may be specified either using the "standard" property (gml:pointMember) or the array property (gml:pointMembers). It is also valid to use both the "standard" and the array properties in the same collection.')

    
    # Element {http://www.opengis.net/gml/3.3/ce}SimpleMultiPoint uses Python identifier SimpleMultiPoint
    __SimpleMultiPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SimpleMultiPoint'), 'SimpleMultiPoint', '__httpwww_opengis_netgml3_3ce_MultiPointPropertyType_httpwww_opengis_netgml3_3ceSimpleMultiPoint', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 209, 2), )

    
    SimpleMultiPoint = property(__SimpleMultiPoint.value, __SimpleMultiPoint.set, None, None)

    
    # Attribute {http://www.opengis.net/gml/3.2}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netgml3_3ce_MultiPointPropertyType_httpwww_opengis_netgml3_2remoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/deprecatedTypes.xsd', 638, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 52, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, '')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_3ce_MultiPointPropertyType_nilReason', pyxb.bundles.opengis.gml_3_2.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute owns uses Python identifier owns
    __owns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owns'), 'owns', '__httpwww_opengis_netgml3_3ce_MultiPointPropertyType_owns', pyxb.binding.datatypes.boolean, unicode_default='false')
    __owns._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    __owns._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 79, 2)
    
    owns = property(__owns.value, __owns.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netgml3_3ce_MultiPointPropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netgml3_3ce_MultiPointPropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netgml3_3ce_MultiPointPropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_3ce_MultiPointPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netgml3_3ce_MultiPointPropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netgml3_3ce_MultiPointPropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_3ce_MultiPointPropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __MultiPoint.name() : __MultiPoint,
        __SimpleMultiPoint.name() : __SimpleMultiPoint
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
_module_typeBindings.MultiPointPropertyType = MultiPointPropertyType
Namespace.addCategoryObject('typeBinding', 'MultiPointPropertyType', MultiPointPropertyType)


AbstractSimplePolygon = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractSimplePolygon'), pyxb.bundles.opengis.gml_3_2.AbstractSurfaceType, documentation='Abstract element representative of a substitution affiliation', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 11, 2))
Namespace.addCategoryObject('elementBinding', AbstractSimplePolygon.name().localName(), AbstractSimplePolygon)

AbstractSimpleArcString = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractSimpleArcString'), pyxb.bundles.opengis.gml_3_2.AbstractCurveType, documentation='Abstract element representative of a substitution affiliation', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 76, 2))
Namespace.addCategoryObject('elementBinding', AbstractSimpleArcString.name().localName(), AbstractSimpleArcString)

SimplePolygon = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimplePolygon'), SimplePolygonType, documentation="A SimplePolygon is a specialized polygon that has a simplified encoding of the logically equivalent GML 3.2 Surface with a single GML 3.2 PolygonPatch as its surface patch consisting of a single LinearRing as its exterior boundary and does not have any interior boundary. Thus the usage of the term 'simple' here refers to a specialized polygon with a _simplified_ encoding, which is _simply_ connected (no interior rings) and uses a _simple_ closed curve (no self-crossings) to represent its single boundary ring.", location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 6, 2))
Namespace.addCategoryObject('elementBinding', SimplePolygon.name().localName(), SimplePolygon)

SimpleRectangle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleRectangle'), SimpleRectangleType, documentation='A SimpleRectangle is the special case of a simple polygon, which has exactly 4 control points in its boundary encoding representing the 4 corners of the rectangle.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 31, 2))
Namespace.addCategoryObject('elementBinding', SimpleRectangle.name().localName(), SimpleRectangle)

SimpleTriangle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleTriangle'), SimpleTriangleType, documentation='A SimpleTriangle is the special case of a simple polygon, which has exactly 3 control points in its boundary encoding representing the 3 corners of the triangle.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 51, 2))
Namespace.addCategoryObject('elementBinding', SimpleTriangle.name().localName(), SimpleTriangle)

SimpleArcString = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleArcString'), SimpleArcStringType, documentation='A SimpleArcString is a specialized curve that has a simplified encoding of the logically equivalent GML 3.2 Curve with one or more GML 3.2 Arc segments', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 71, 2))
Namespace.addCategoryObject('elementBinding', SimpleArcString.name().localName(), SimpleArcString)

SimpleArc = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleArc'), SimpleArcType, documentation='A SimpleArc is a specialized curve that has a simplified encoding of the logically equivalent GML 3.2 Curve with a single GML 3.2 ArcString segment .', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 98, 2))
Namespace.addCategoryObject('elementBinding', SimpleArc.name().localName(), SimpleArc)

SimpleArcByCenterPoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleArcByCenterPoint'), SimpleArcByCenterPointType, documentation='A SimpleArcByCenterPoint is a specialized curve that has a simplified encoding of the logically equivalent GML 3.2 Curve with a single GML 3.2 SimpleArcByCenterPoint segment.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 120, 2))
Namespace.addCategoryObject('elementBinding', SimpleArcByCenterPoint.name().localName(), SimpleArcByCenterPoint)

SimpleArcStringByBulge = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleArcStringByBulge'), SimpleArcStringByBulgeType, documentation='A SimpleArcStringByBulge is a specialized curve that has a simplified encoding of the logically equivalent GML 3.2 Curve with one or more GML 3.2 ArcByBulge segments.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 146, 2))
Namespace.addCategoryObject('elementBinding', SimpleArcStringByBulge.name().localName(), SimpleArcStringByBulge)

SimpleArcByBulge = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleArcByBulge'), SimpleArcByBulgeType, documentation='A SimpleArcStringByBulge is a specialized curve that has a simplified encoding of the logically equivalent GML 3.2 Curve with one GML 3.2 ArcByBulge segment.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 170, 2))
Namespace.addCategoryObject('elementBinding', SimpleArcByBulge.name().localName(), SimpleArcByBulge)

SimpleCircle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleCircle'), SimpleArcType, documentation='A SimpleCircle is a specialized curve that has a simplified encoding of the logically equivalent GML 3.2 Curve with a single GML 3.2 Circle segment.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 194, 2))
Namespace.addCategoryObject('elementBinding', SimpleCircle.name().localName(), SimpleCircle)

SimpleCircleByCenterPoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleCircleByCenterPoint'), SimpleArcByCenterPointType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 199, 2))
Namespace.addCategoryObject('elementBinding', SimpleCircleByCenterPoint.name().localName(), SimpleCircleByCenterPoint)

SimpleMultiPoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleMultiPoint'), SimpleMultiPointType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 209, 2))
Namespace.addCategoryObject('elementBinding', SimpleMultiPoint.name().localName(), SimpleMultiPoint)



SimplePolygonType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), pyxb.bundles.opengis.gml_3_2.DirectPositionType, scope=SimplePolygonType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1)))

SimplePolygonType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), pyxb.bundles.opengis.gml_3_2.DirectPositionListType, scope=SimplePolygonType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1)))

SimplePolygonType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), pyxb.bundles.opengis.gml_3_2.PointPropertyType, scope=SimplePolygonType, documentation='This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1)))

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
    cc_5 = fac.CounterCondition(min=3, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 21, 12))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimplePolygonType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimplePolygonType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimplePolygonType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimplePolygonType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimplePolygonType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SimplePolygonType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 22, 14))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SimplePolygonType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 23, 14))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimplePolygonType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 25, 12))
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
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SimplePolygonType._Automaton = _BuildAutomaton()




SimpleRectangleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), pyxb.bundles.opengis.gml_3_2.DirectPositionType, scope=SimpleRectangleType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1)))

SimpleRectangleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), pyxb.bundles.opengis.gml_3_2.DirectPositionListType, scope=SimpleRectangleType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1)))

SimpleRectangleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), pyxb.bundles.opengis.gml_3_2.PointPropertyType, scope=SimpleRectangleType, documentation='This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1)))

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
    cc_5 = fac.CounterCondition(min=4, max=4, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 41, 12))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleRectangleType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleRectangleType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleRectangleType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleRectangleType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleRectangleType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SimpleRectangleType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 42, 14))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SimpleRectangleType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 43, 14))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleRectangleType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 45, 12))
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
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SimpleRectangleType._Automaton = _BuildAutomaton_()




SimpleTriangleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), pyxb.bundles.opengis.gml_3_2.DirectPositionType, scope=SimpleTriangleType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1)))

SimpleTriangleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), pyxb.bundles.opengis.gml_3_2.DirectPositionListType, scope=SimpleTriangleType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1)))

SimpleTriangleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), pyxb.bundles.opengis.gml_3_2.PointPropertyType, scope=SimpleTriangleType, documentation='This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1)))

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
    cc_5 = fac.CounterCondition(min=3, max=3, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 61, 12))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleTriangleType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleTriangleType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleTriangleType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleTriangleType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleTriangleType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SimpleTriangleType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 62, 14))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SimpleTriangleType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 63, 14))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleTriangleType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 65, 12))
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
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SimpleTriangleType._Automaton = _BuildAutomaton_2()




SimpleArcStringType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), pyxb.bundles.opengis.gml_3_2.DirectPositionType, scope=SimpleArcStringType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1)))

SimpleArcStringType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), pyxb.bundles.opengis.gml_3_2.DirectPositionListType, scope=SimpleArcStringType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1)))

SimpleArcStringType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), pyxb.bundles.opengis.gml_3_2.PointPropertyType, scope=SimpleArcStringType, documentation='This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
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
    cc_5 = fac.CounterCondition(min=3, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 86, 12))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 87, 14))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 88, 14))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 90, 12))
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
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SimpleArcStringType._Automaton = _BuildAutomaton_3()




SimpleArcType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), pyxb.bundles.opengis.gml_3_2.DirectPositionType, scope=SimpleArcType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1)))

SimpleArcType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), pyxb.bundles.opengis.gml_3_2.DirectPositionListType, scope=SimpleArcType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1)))

SimpleArcType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), pyxb.bundles.opengis.gml_3_2.PointPropertyType, scope=SimpleArcType, documentation='This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
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
    cc_5 = fac.CounterCondition(min=3, max=3, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 108, 12))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SimpleArcType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 109, 14))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SimpleArcType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 110, 14))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleArcType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 112, 12))
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
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SimpleArcType._Automaton = _BuildAutomaton_4()




SimpleArcByCenterPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), pyxb.bundles.opengis.gml_3_2.DirectPositionType, scope=SimpleArcByCenterPointType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1)))

SimpleArcByCenterPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), pyxb.bundles.opengis.gml_3_2.DirectPositionListType, scope=SimpleArcByCenterPointType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1)))

SimpleArcByCenterPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), pyxb.bundles.opengis.gml_3_2.PointPropertyType, scope=SimpleArcByCenterPointType, documentation='This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1)))

SimpleArcByCenterPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'radius'), pyxb.bundles.opengis.gml_3_2.LengthType, scope=SimpleArcByCenterPointType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 136, 10)))

SimpleArcByCenterPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startAngle'), pyxb.bundles.opengis.gml_3_2.AngleType, scope=SimpleArcByCenterPointType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 138, 10)))

SimpleArcByCenterPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endAngle'), pyxb.bundles.opengis.gml_3_2.AngleType, scope=SimpleArcByCenterPointType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 139, 10)))

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
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByCenterPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByCenterPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByCenterPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByCenterPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByCenterPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByCenterPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 131, 14))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByCenterPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 132, 14))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByCenterPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 134, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByCenterPointType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'radius')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 136, 10))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByCenterPointType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startAngle')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 138, 10))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleArcByCenterPointType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endAngle')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 139, 10))
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
    transitions.append(fac.Transition(st_8, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SimpleArcByCenterPointType._Automaton = _BuildAutomaton_5()




SimpleArcStringByBulgeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), pyxb.bundles.opengis.gml_3_2.DirectPositionType, scope=SimpleArcStringByBulgeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1)))

SimpleArcStringByBulgeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), pyxb.bundles.opengis.gml_3_2.DirectPositionListType, scope=SimpleArcStringByBulgeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1)))

SimpleArcStringByBulgeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), pyxb.bundles.opengis.gml_3_2.PointPropertyType, scope=SimpleArcStringByBulgeType, documentation='This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1)))

SimpleArcStringByBulgeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bulge'), pyxb.binding.datatypes.double, scope=SimpleArcStringByBulgeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 162, 10)))

SimpleArcStringByBulgeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'normal'), pyxb.bundles.opengis.gml_3_2.VectorType, scope=SimpleArcStringByBulgeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 163, 10)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
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
    cc_5 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 156, 12))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringByBulgeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringByBulgeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringByBulgeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringByBulgeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringByBulgeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringByBulgeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 157, 14))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringByBulgeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 158, 14))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringByBulgeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 160, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringByBulgeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bulge')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 162, 10))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleArcStringByBulgeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'normal')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 163, 10))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
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
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
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
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SimpleArcStringByBulgeType._Automaton = _BuildAutomaton_6()




SimpleArcByBulgeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos'), pyxb.bundles.opengis.gml_3_2.DirectPositionType, scope=SimpleArcByBulgeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 87, 1)))

SimpleArcByBulgeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), pyxb.bundles.opengis.gml_3_2.DirectPositionListType, scope=SimpleArcByBulgeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1)))

SimpleArcByBulgeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty'), pyxb.bundles.opengis.gml_3_2.PointPropertyType, scope=SimpleArcByBulgeType, documentation='This property element either references a point via the XLink-attributes or contains the point element. pointProperty is the predefined property which may be used by GML Application Schemas whenever a GML feature has a property with a value that is substitutable for Point.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 204, 1)))

SimpleArcByBulgeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bulge'), pyxb.binding.datatypes.double, scope=SimpleArcByBulgeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 186, 10)))

SimpleArcByBulgeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'normal'), pyxb.bundles.opengis.gml_3_2.VectorType, scope=SimpleArcByBulgeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 187, 10)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
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
    cc_5 = fac.CounterCondition(min=2, max=2, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 180, 12))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByBulgeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByBulgeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByBulgeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByBulgeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByBulgeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByBulgeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pos')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 181, 14))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByBulgeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'pointProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 182, 14))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByBulgeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 184, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleArcByBulgeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bulge')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 186, 10))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleArcByBulgeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'normal')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 187, 10))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
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
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
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
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SimpleArcByBulgeType._Automaton = _BuildAutomaton_7()




SimpleMultiPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList'), pyxb.bundles.opengis.gml_3_2.DirectPositionListType, scope=SimpleMultiPointType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryBasic0d1d.xsd', 102, 1)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
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
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMultiPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMultiPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMultiPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMultiPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMultiPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleMultiPointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'posList')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 204, 10))
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
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SimpleMultiPointType._Automaton = _BuildAutomaton_8()




MultiPointPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'MultiPoint'), pyxb.bundles.opengis.gml_3_2.MultiPointType, scope=MultiPointPropertyType, documentation='A gml:MultiPoint consists of one or more gml:Points.\nThe members of the geometric aggregate may be specified either using the "standard" property (gml:pointMember) or the array property (gml:pointMembers). It is also valid to use both the "standard" and the array properties in the same collection.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/geometryAggregates.xsd', 73, 1)))

MultiPointPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleMultiPoint'), SimpleMultiPointType, scope=MultiPointPropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 209, 2)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 211, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MultiPointPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'MultiPoint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 212, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MultiPointPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SimpleMultiPoint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/geometryCompact.xsd', 213, 6))
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
MultiPointPropertyType._Automaton = _BuildAutomaton_9()


AbstractSimplePolygon._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_2.AbstractSurface)

AbstractSimpleArcString._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_2.AbstractCurve)

SimplePolygon._setSubstitutionGroup(AbstractSimplePolygon)

SimpleRectangle._setSubstitutionGroup(AbstractSimplePolygon)

SimpleTriangle._setSubstitutionGroup(AbstractSimplePolygon)

SimpleArcString._setSubstitutionGroup(AbstractSimpleArcString)

SimpleArc._setSubstitutionGroup(AbstractSimpleArcString)

SimpleArcByCenterPoint._setSubstitutionGroup(AbstractSimpleArcString)

SimpleArcStringByBulge._setSubstitutionGroup(AbstractSimpleArcString)

SimpleArcByBulge._setSubstitutionGroup(AbstractSimpleArcString)

SimpleCircle._setSubstitutionGroup(AbstractSimpleArcString)

SimpleCircleByCenterPoint._setSubstitutionGroup(AbstractSimpleArcString)

SimpleMultiPoint._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_2.AbstractGeometricAggregate)
