# ./pyxb/bundles/opengis/gml_3_3/raw/lro.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:49d05877d0d81a5486eede4046175d14852ac40d
# Generated 2017-07-10 00:38:05.931633 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/gml/3.3/lro [xmlns:gmllro]

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
import pyxb.bundles.opengis.gml_3_3.lr
import pyxb.binding.datatypes
import pyxb.bundles.common.xlink
import pyxb.bundles.opengis.gml_3_2

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/gml/3.3/lro', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gml = pyxb.bundles.opengis.gml_3_2.Namespace
_Namespace_gml.configureCategories(['typeBinding', 'elementBinding'])
_Namespace = pyxb.bundles.common.xlink.Namespace
_Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gmllr = pyxb.bundles.opengis.gml_3_3.lr.Namespace
_Namespace_gmllr.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://www.opengis.net/gml/3.3/lro}LateralOffsetDirectionType
class LateralOffsetDirectionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LateralOffsetDirectionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 67, 2)
    _Documentation = None
LateralOffsetDirectionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LateralOffsetDirectionType, enum_prefix=None)
LateralOffsetDirectionType.left = LateralOffsetDirectionType._CF_enumeration.addEnumeration(unicode_value='left', tag='left')
LateralOffsetDirectionType.right = LateralOffsetDirectionType._CF_enumeration.addEnumeration(unicode_value='right', tag='right')
LateralOffsetDirectionType._InitializeFacetMap(LateralOffsetDirectionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LateralOffsetDirectionType', LateralOffsetDirectionType)
_module_typeBindings.LateralOffsetDirectionType = LateralOffsetDirectionType

# Atomic simple type: {http://www.opengis.net/gml/3.3/lro}VerticalOffsetDirectionType
class VerticalOffsetDirectionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VerticalOffsetDirectionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 73, 2)
    _Documentation = None
VerticalOffsetDirectionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VerticalOffsetDirectionType, enum_prefix=None)
VerticalOffsetDirectionType.up = VerticalOffsetDirectionType._CF_enumeration.addEnumeration(unicode_value='up', tag='up')
VerticalOffsetDirectionType.down = VerticalOffsetDirectionType._CF_enumeration.addEnumeration(unicode_value='down', tag='down')
VerticalOffsetDirectionType._InitializeFacetMap(VerticalOffsetDirectionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VerticalOffsetDirectionType', VerticalOffsetDirectionType)
_module_typeBindings.VerticalOffsetDirectionType = VerticalOffsetDirectionType

# Complex type {http://www.opengis.net/gml/3.3/lro}LRMWithOffsetPropertyType with content type ELEMENT_ONLY
class LRMWithOffsetPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/gml/3.3/lro}LRMWithOffsetPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LRMWithOffsetPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 19, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.3/lro}LRMWithOffset uses Python identifier LRMWithOffset
    __LRMWithOffset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LRMWithOffset'), 'LRMWithOffset', '__httpwww_opengis_netgml3_3lro_LRMWithOffsetPropertyType_httpwww_opengis_netgml3_3lroLRMWithOffset', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 18, 2), )

    
    LRMWithOffset = property(__LRMWithOffset.value, __LRMWithOffset.set, None, None)

    
    # Attribute {http://www.opengis.net/gml/3.2}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netgml3_3lro_LRMWithOffsetPropertyType_httpwww_opengis_netgml3_2remoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/deprecatedTypes.xsd', 638, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 52, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, '')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_3lro_LRMWithOffsetPropertyType_nilReason', pyxb.bundles.opengis.gml_3_2.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netgml3_3lro_LRMWithOffsetPropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netgml3_3lro_LRMWithOffsetPropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netgml3_3lro_LRMWithOffsetPropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_3lro_LRMWithOffsetPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netgml3_3lro_LRMWithOffsetPropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netgml3_3lro_LRMWithOffsetPropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_3lro_LRMWithOffsetPropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __LRMWithOffset.name() : __LRMWithOffset
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
_module_typeBindings.LRMWithOffsetPropertyType = LRMWithOffsetPropertyType
Namespace.addCategoryObject('typeBinding', 'LRMWithOffsetPropertyType', LRMWithOffsetPropertyType)


# Complex type {http://www.opengis.net/gml/3.3/lro}LateralOffsetExpressionType with content type SIMPLE
class LateralOffsetExpressionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/gml/3.3/lro}LateralOffsetExpressionType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LateralOffsetExpressionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 36, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.double
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_opengis_netgml3_3lro_LateralOffsetExpressionType_uom', pyxb.bundles.opengis.gml_3_2.UomIdentifier)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 39, 8)
    __uom._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 39, 8)
    
    uom = property(__uom.value, __uom.set, None, None)

    
    # Attribute lateralOffsetReferent uses Python identifier lateralOffsetReferent
    __lateralOffsetReferent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lateralOffsetReferent'), 'lateralOffsetReferent', '__httpwww_opengis_netgml3_3lro_LateralOffsetExpressionType_lateralOffsetReferent', pyxb.binding.datatypes.string)
    __lateralOffsetReferent._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 40, 8)
    __lateralOffsetReferent._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 40, 8)
    
    lateralOffsetReferent = property(__lateralOffsetReferent.value, __lateralOffsetReferent.set, None, None)

    
    # Attribute featureGeometry uses Python identifier featureGeometry
    __featureGeometry = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'featureGeometry'), 'featureGeometry', '__httpwww_opengis_netgml3_3lro_LateralOffsetExpressionType_featureGeometry', pyxb.binding.datatypes.anyURI)
    __featureGeometry._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 41, 8)
    __featureGeometry._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 41, 8)
    
    featureGeometry = property(__featureGeometry.value, __featureGeometry.set, None, '')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom,
        __lateralOffsetReferent.name() : __lateralOffsetReferent,
        __featureGeometry.name() : __featureGeometry
    })
_module_typeBindings.LateralOffsetExpressionType = LateralOffsetExpressionType
Namespace.addCategoryObject('typeBinding', 'LateralOffsetExpressionType', LateralOffsetExpressionType)


# Complex type {http://www.opengis.net/gml/3.3/lro}VerticalOffsetExpressionType with content type SIMPLE
class VerticalOffsetExpressionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/gml/3.3/lro}VerticalOffsetExpressionType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VerticalOffsetExpressionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 51, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.double
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_opengis_netgml3_3lro_VerticalOffsetExpressionType_uom', pyxb.bundles.opengis.gml_3_2.UomIdentifier)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 54, 8)
    __uom._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 54, 8)
    
    uom = property(__uom.value, __uom.set, None, None)

    
    # Attribute verticalOffsetReferent uses Python identifier verticalOffsetReferent
    __verticalOffsetReferent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'verticalOffsetReferent'), 'verticalOffsetReferent', '__httpwww_opengis_netgml3_3lro_VerticalOffsetExpressionType_verticalOffsetReferent', pyxb.binding.datatypes.string)
    __verticalOffsetReferent._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 55, 8)
    __verticalOffsetReferent._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 55, 8)
    
    verticalOffsetReferent = property(__verticalOffsetReferent.value, __verticalOffsetReferent.set, None, None)

    
    # Attribute featureGeometry uses Python identifier featureGeometry
    __featureGeometry = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'featureGeometry'), 'featureGeometry', '__httpwww_opengis_netgml3_3lro_VerticalOffsetExpressionType_featureGeometry', pyxb.binding.datatypes.anyURI)
    __featureGeometry._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 56, 8)
    __featureGeometry._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 56, 8)
    
    featureGeometry = property(__featureGeometry.value, __featureGeometry.set, None, 'The featureGeometry attribute value should reference a Geometry object')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom,
        __verticalOffsetReferent.name() : __verticalOffsetReferent,
        __featureGeometry.name() : __featureGeometry
    })
_module_typeBindings.VerticalOffsetExpressionType = VerticalOffsetExpressionType
Namespace.addCategoryObject('typeBinding', 'VerticalOffsetExpressionType', VerticalOffsetExpressionType)


# Complex type {http://www.opengis.net/gml/3.3/lro}LateralOffsetLinearSRSType with content type ELEMENT_ONLY
class LateralOffsetLinearSRSType (pyxb.bundles.opengis.gml_3_2.IdentifiedObjectType):
    """Complex type {http://www.opengis.net/gml/3.3/lro}LateralOffsetLinearSRSType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LateralOffsetLinearSRSType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 79, 2)
    _ElementMap = pyxb.bundles.opengis.gml_3_2.IdentifiedObjectType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_2.IdentifiedObjectType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_2.IdentifiedObjectType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element remarks ({http://www.opengis.net/gml/3.2}remarks) inherited from {http://www.opengis.net/gml/3.2}DefinitionType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element {http://www.opengis.net/gml/3.3/lro}linearElement uses Python identifier linearElement
    __linearElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'linearElement'), 'linearElement', '__httpwww_opengis_netgml3_3lro_LateralOffsetLinearSRSType_httpwww_opengis_netgml3_3lrolinearElement', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 83, 10), )

    
    linearElement = property(__linearElement.value, __linearElement.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.3/lro}lrm uses Python identifier lrm
    __lrm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lrm'), 'lrm', '__httpwww_opengis_netgml3_3lro_LateralOffsetLinearSRSType_httpwww_opengis_netgml3_3lrolrm', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 84, 10), )

    
    lrm = property(__lrm.value, __lrm.set, None, None)

    
    # Attribute id_ inherited from {http://www.opengis.net/gml/3.2}DefinitionBaseType
    _ElementMap.update({
        __linearElement.name() : __linearElement,
        __lrm.name() : __lrm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LateralOffsetLinearSRSType = LateralOffsetLinearSRSType
Namespace.addCategoryObject('typeBinding', 'LateralOffsetLinearSRSType', LateralOffsetLinearSRSType)


# Complex type {http://www.opengis.net/gml/3.3/lro}LateralOffsetLinearSRSPropertyType with content type ELEMENT_ONLY
class LateralOffsetLinearSRSPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/gml/3.3/lro}LateralOffsetLinearSRSPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LateralOffsetLinearSRSPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 90, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml/3.3/lro}LateralOffsetLinearSRS uses Python identifier LateralOffsetLinearSRS
    __LateralOffsetLinearSRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LateralOffsetLinearSRS'), 'LateralOffsetLinearSRS', '__httpwww_opengis_netgml3_3lro_LateralOffsetLinearSRSPropertyType_httpwww_opengis_netgml3_3lroLateralOffsetLinearSRS', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 89, 2), )

    
    LateralOffsetLinearSRS = property(__LateralOffsetLinearSRS.value, __LateralOffsetLinearSRS.set, None, None)

    
    # Attribute {http://www.opengis.net/gml/3.2}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netgml3_3lro_LateralOffsetLinearSRSPropertyType_httpwww_opengis_netgml3_2remoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/deprecatedTypes.xsd', 638, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 52, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, '')

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netgml3_3lro_LateralOffsetLinearSRSPropertyType_nilReason', pyxb.bundles.opengis.gml_3_2.NilReasonType)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 51, 2)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netgml3_3lro_LateralOffsetLinearSRSPropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netgml3_3lro_LateralOffsetLinearSRSPropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netgml3_3lro_LateralOffsetLinearSRSPropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netgml3_3lro_LateralOffsetLinearSRSPropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netgml3_3lro_LateralOffsetLinearSRSPropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netgml3_3lro_LateralOffsetLinearSRSPropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netgml3_3lro_LateralOffsetLinearSRSPropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __LateralOffsetLinearSRS.name() : __LateralOffsetLinearSRS
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
_module_typeBindings.LateralOffsetLinearSRSPropertyType = LateralOffsetLinearSRSPropertyType
Namespace.addCategoryObject('typeBinding', 'LateralOffsetLinearSRSPropertyType', LateralOffsetLinearSRSPropertyType)


# Complex type {http://www.opengis.net/gml/3.3/lro}LRMWithOffsetType with content type ELEMENT_ONLY
class LRMWithOffsetType (pyxb.bundles.opengis.gml_3_3.lr.LinearReferencingMethodType):
    """Complex type {http://www.opengis.net/gml/3.3/lro}LRMWithOffsetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LRMWithOffsetType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 7, 2)
    _ElementMap = pyxb.bundles.opengis.gml_3_3.lr.LinearReferencingMethodType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_3.lr.LinearReferencingMethodType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_3.lr.LinearReferencingMethodType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name_ ({http://www.opengis.net/gml/3.3/lr}name) inherited from {http://www.opengis.net/gml/3.3/lr}LinearReferencingMethodType
    
    # Element type ({http://www.opengis.net/gml/3.3/lr}type) inherited from {http://www.opengis.net/gml/3.3/lr}LinearReferencingMethodType
    
    # Element units ({http://www.opengis.net/gml/3.3/lr}units) inherited from {http://www.opengis.net/gml/3.3/lr}LinearReferencingMethodType
    
    # Element constraint ({http://www.opengis.net/gml/3.3/lr}constraint) inherited from {http://www.opengis.net/gml/3.3/lr}LinearReferencingMethodType
    
    # Element {http://www.opengis.net/gml/3.3/lro}offsetUnits uses Python identifier offsetUnits
    __offsetUnits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'offsetUnits'), 'offsetUnits', '__httpwww_opengis_netgml3_3lro_LRMWithOffsetType_httpwww_opengis_netgml3_3lrooffsetUnits', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 11, 10), )

    
    offsetUnits = property(__offsetUnits.value, __offsetUnits.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.3/lro}positiveLateralOffsetDirection uses Python identifier positiveLateralOffsetDirection
    __positiveLateralOffsetDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'positiveLateralOffsetDirection'), 'positiveLateralOffsetDirection', '__httpwww_opengis_netgml3_3lro_LRMWithOffsetType_httpwww_opengis_netgml3_3lropositiveLateralOffsetDirection', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 12, 10), )

    
    positiveLateralOffsetDirection = property(__positiveLateralOffsetDirection.value, __positiveLateralOffsetDirection.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.3/lro}positiveVerticalOffsetDirection uses Python identifier positiveVerticalOffsetDirection
    __positiveVerticalOffsetDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'positiveVerticalOffsetDirection'), 'positiveVerticalOffsetDirection', '__httpwww_opengis_netgml3_3lro_LRMWithOffsetType_httpwww_opengis_netgml3_3lropositiveVerticalOffsetDirection', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 13, 10), )

    
    positiveVerticalOffsetDirection = property(__positiveVerticalOffsetDirection.value, __positiveVerticalOffsetDirection.set, None, None)

    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    _ElementMap.update({
        __offsetUnits.name() : __offsetUnits,
        __positiveLateralOffsetDirection.name() : __positiveLateralOffsetDirection,
        __positiveVerticalOffsetDirection.name() : __positiveVerticalOffsetDirection
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LRMWithOffsetType = LRMWithOffsetType
Namespace.addCategoryObject('typeBinding', 'LRMWithOffsetType', LRMWithOffsetType)


# Complex type {http://www.opengis.net/gml/3.3/lro}LateralOffsetDistanceExpressionType with content type ELEMENT_ONLY
class LateralOffsetDistanceExpressionType (pyxb.bundles.opengis.gml_3_3.lr.DistanceExpressionType):
    """Complex type {http://www.opengis.net/gml/3.3/lro}LateralOffsetDistanceExpressionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LateralOffsetDistanceExpressionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 25, 2)
    _ElementMap = pyxb.bundles.opengis.gml_3_3.lr.DistanceExpressionType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_3.lr.DistanceExpressionType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_3.lr.DistanceExpressionType
    
    # Element metaDataProperty ({http://www.opengis.net/gml/3.2}metaDataProperty) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml/3.2}description) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element descriptionReference ({http://www.opengis.net/gml/3.2}descriptionReference) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml/3.2}name) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element identifier ({http://www.opengis.net/gml/3.2}identifier) inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    
    # Element distanceAlong ({http://www.opengis.net/gml/3.3/lr}distanceAlong) inherited from {http://www.opengis.net/gml/3.3/lr}DistanceExpressionType
    
    # Element referent ({http://www.opengis.net/gml/3.3/lr}referent) inherited from {http://www.opengis.net/gml/3.3/lr}DistanceExpressionType
    
    # Element {http://www.opengis.net/gml/3.3/lro}lateralOffsetExpression uses Python identifier lateralOffsetExpression
    __lateralOffsetExpression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lateralOffsetExpression'), 'lateralOffsetExpression', '__httpwww_opengis_netgml3_3lro_LateralOffsetDistanceExpressionType_httpwww_opengis_netgml3_3lrolateralOffsetExpression', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 29, 10), )

    
    lateralOffsetExpression = property(__lateralOffsetExpression.value, __lateralOffsetExpression.set, None, None)

    
    # Element {http://www.opengis.net/gml/3.3/lro}verticalOffsetExpression uses Python identifier verticalOffsetExpression
    __verticalOffsetExpression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'verticalOffsetExpression'), 'verticalOffsetExpression', '__httpwww_opengis_netgml3_3lro_LateralOffsetDistanceExpressionType_httpwww_opengis_netgml3_3lroverticalOffsetExpression', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 30, 10), )

    
    verticalOffsetExpression = property(__verticalOffsetExpression.value, __verticalOffsetExpression.set, None, None)

    
    # Attribute id inherited from {http://www.opengis.net/gml/3.2}AbstractGMLType
    _ElementMap.update({
        __lateralOffsetExpression.name() : __lateralOffsetExpression,
        __verticalOffsetExpression.name() : __verticalOffsetExpression
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LateralOffsetDistanceExpressionType = LateralOffsetDistanceExpressionType
Namespace.addCategoryObject('typeBinding', 'LateralOffsetDistanceExpressionType', LateralOffsetDistanceExpressionType)


LateralOffsetLinearSRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LateralOffsetLinearSRS'), LateralOffsetLinearSRSType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 89, 2))
Namespace.addCategoryObject('elementBinding', LateralOffsetLinearSRS.name().localName(), LateralOffsetLinearSRS)

LRMWithOffset = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LRMWithOffset'), LRMWithOffsetType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 18, 2))
Namespace.addCategoryObject('elementBinding', LRMWithOffset.name().localName(), LRMWithOffset)

LateralOffsetDistanceExpression = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LateralOffsetDistanceExpression'), LateralOffsetDistanceExpressionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 35, 2))
Namespace.addCategoryObject('elementBinding', LateralOffsetDistanceExpression.name().localName(), LateralOffsetDistanceExpression)



LRMWithOffsetPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LRMWithOffset'), LRMWithOffsetType, scope=LRMWithOffsetPropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 18, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 20, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LRMWithOffsetPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LRMWithOffset')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 21, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LRMWithOffsetPropertyType._Automaton = _BuildAutomaton()




LateralOffsetLinearSRSType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'linearElement'), pyxb.bundles.opengis.gml_3_3.lr.LinearElementPropertyType, scope=LateralOffsetLinearSRSType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 83, 10)))

LateralOffsetLinearSRSType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lrm'), LRMWithOffsetPropertyType, scope=LateralOffsetLinearSRSType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 84, 10)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/dictionary.xsd', 35, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/dictionary.xsd', 36, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/dictionary.xsd', 37, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/dictionary.xsd', 39, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/dictionary.xsd', 49, 5))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LateralOffsetLinearSRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/dictionary.xsd', 35, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LateralOffsetLinearSRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/dictionary.xsd', 36, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LateralOffsetLinearSRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/dictionary.xsd', 37, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LateralOffsetLinearSRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/dictionary.xsd', 38, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LateralOffsetLinearSRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/dictionary.xsd', 39, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LateralOffsetLinearSRSType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'remarks')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/dictionary.xsd', 49, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LateralOffsetLinearSRSType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'linearElement')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 83, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LateralOffsetLinearSRSType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lrm')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 84, 10))
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
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LateralOffsetLinearSRSType._Automaton = _BuildAutomaton_()




LateralOffsetLinearSRSPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LateralOffsetLinearSRS'), LateralOffsetLinearSRSType, scope=LateralOffsetLinearSRSPropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 89, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 91, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LateralOffsetLinearSRSPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LateralOffsetLinearSRS')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 92, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LateralOffsetLinearSRSPropertyType._Automaton = _BuildAutomaton_2()




LRMWithOffsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'offsetUnits'), pyxb.bundles.opengis.gml_3_2.UomIdentifier, scope=LRMWithOffsetType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 11, 10)))

LRMWithOffsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'positiveLateralOffsetDirection'), LateralOffsetDirectionType, scope=LRMWithOffsetType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 12, 10), unicode_default='right'))

LRMWithOffsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'positiveVerticalOffsetDirection'), VerticalOffsetDirectionType, scope=LRMWithOffsetType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 13, 10), unicode_default='up'))

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
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRef.xsd', 68, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 12, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 13, 10))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LRMWithOffsetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LRMWithOffsetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LRMWithOffsetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LRMWithOffsetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LRMWithOffsetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LRMWithOffsetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmllr, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRef.xsd', 65, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LRMWithOffsetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmllr, 'type')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRef.xsd', 66, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LRMWithOffsetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmllr, 'units')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRef.xsd', 67, 10))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LRMWithOffsetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmllr, 'constraint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRef.xsd', 68, 10))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LRMWithOffsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'offsetUnits')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 11, 10))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(LRMWithOffsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'positiveLateralOffsetDirection')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 12, 10))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(LRMWithOffsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'positiveVerticalOffsetDirection')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 13, 10))
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LRMWithOffsetType._Automaton = _BuildAutomaton_3()




LateralOffsetDistanceExpressionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lateralOffsetExpression'), LateralOffsetExpressionType, scope=LateralOffsetDistanceExpressionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 29, 10)))

LateralOffsetDistanceExpressionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'verticalOffsetExpression'), VerticalOffsetExpressionType, scope=LateralOffsetDistanceExpressionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 30, 10)))

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
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRef.xsd', 85, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 29, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 30, 10))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LateralOffsetDistanceExpressionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LateralOffsetDistanceExpressionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LateralOffsetDistanceExpressionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'descriptionReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LateralOffsetDistanceExpressionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'identifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LateralOffsetDistanceExpressionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.2.1/gmlBase.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LateralOffsetDistanceExpressionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmllr, 'distanceAlong')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRef.xsd', 84, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(LateralOffsetDistanceExpressionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gmllr, 'referent')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRef.xsd', 85, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(LateralOffsetDistanceExpressionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lateralOffsetExpression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 29, 10))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(LateralOffsetDistanceExpressionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'verticalOffsetExpression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/linearRefOffset.xsd', 30, 10))
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
LateralOffsetDistanceExpressionType._Automaton = _BuildAutomaton_4()


LateralOffsetLinearSRS._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_2.Definition)

LRMWithOffset._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_3.lr.LinearReferencingMethod)

LateralOffsetDistanceExpression._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_3.lr.DistanceExpression)
