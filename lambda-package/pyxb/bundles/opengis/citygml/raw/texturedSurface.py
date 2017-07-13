# ./pyxb/bundles/opengis/citygml/raw/texturedSurface.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:d0c900ca512ca4d1024bf70ffaa5c66e996a6cdf
# Generated 2017-07-10 00:37:44.415265 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/citygml/texturedsurface/1.0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:fc472e06-6507-11e7-96af-0a55f9edafa5')

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
import pyxb.bundles.common.xlink
import pyxb.bundles.opengis.citygml.base
import pyxb.bundles.opengis.gml

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/citygml/texturedsurface/1.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gml = pyxb.bundles.opengis.gml.Namespace
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


# Atomic simple type: {http://www.opengis.net/citygml/texturedsurface/1.0}TextureTypeType
class TextureTypeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Deprecated since CityGML version 0.4.0. Use the concepts of the CityGML Appearance module instead.
                Textures can be qualified by the attribute textureType. The textureType differentiates between textures, which are
                specific for a certain object and are only used for that object (specific), and prototypic textures being typical
                for that kind of object and are used many times for all objects of that kind (typical). A typical texture may be
                replaced by a specific, if available. Textures may also be classified as unknown. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextureTypeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 124, 4)
    _Documentation = 'Deprecated since CityGML version 0.4.0. Use the concepts of the CityGML Appearance module instead.\n                Textures can be qualified by the attribute textureType. The textureType differentiates between textures, which are\n                specific for a certain object and are only used for that object (specific), and prototypic textures being typical\n                for that kind of object and are used many times for all objects of that kind (typical). A typical texture may be\n                replaced by a specific, if available. Textures may also be classified as unknown. '
TextureTypeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TextureTypeType, enum_prefix=None)
TextureTypeType.specific = TextureTypeType._CF_enumeration.addEnumeration(unicode_value='specific', tag='specific')
TextureTypeType.typical = TextureTypeType._CF_enumeration.addEnumeration(unicode_value='typical', tag='typical')
TextureTypeType.unknown = TextureTypeType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
TextureTypeType._InitializeFacetMap(TextureTypeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TextureTypeType', TextureTypeType)
_module_typeBindings.TextureTypeType = TextureTypeType

# List simple type: {http://www.opengis.net/citygml/texturedsurface/1.0}Color
# superclasses pyxb.bundles.opengis.citygml.base.doubleBetween0and1List
class Color (pyxb.binding.basis.STD_list):

    """Deprecated since CityGML version 0.4.0. Use the concepts of the CityGML Appearance module instead.
                List of three values (red, green, blue), separated by spaces. The values must be in the range between zero and
                one. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Color')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 140, 4)
    _Documentation = 'Deprecated since CityGML version 0.4.0. Use the concepts of the CityGML Appearance module instead.\n                List of three values (red, green, blue), separated by spaces. The values must be in the range between zero and\n                one. '

    _ItemType = pyxb.bundles.opengis.citygml.base.doubleBetween0and1
Color._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(3))
Color._InitializeFacetMap(Color._CF_length)
Namespace.addCategoryObject('typeBinding', 'Color', Color)
_module_typeBindings.Color = Color

# Complex type {http://www.opengis.net/citygml/texturedsurface/1.0}TexturedSurfaceType with content type ELEMENT_ONLY
class TexturedSurfaceType (pyxb.bundles.opengis.gml.OrientableSurfaceType):
    """Deprecated since CityGML version 0.4.0. Use the concepts of the CityGML Appearance module instead.
                The concept of positioning textures on surfaces complies with the standard X3D. Because there has been no
                appropriate texturing concept in GML3, CityGML adds the class TexturedSurface to the geometry model of GML 3. A
                texture is specified as a raster image referenced by an URI, and can be an arbitrary resource, even in the
                internet. Textures are positioned by employing the concept of texture coordinates, i.e. each texture coordinate
                matches with exactly one 3D coordinate of the TexturedSurface. The use of texture coordinates allows an exact
                positioning and trimming of the texture on the surface geometry. Each surface may be assigned one or more
                appearances, each refering to one side of the surface. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TexturedSurfaceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 23, 4)
    _ElementMap = pyxb.bundles.opengis.gml.OrientableSurfaceType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml.OrientableSurfaceType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml.OrientableSurfaceType
    
    # Element {http://www.opengis.net/citygml/texturedsurface/1.0}appearance uses Python identifier appearance
    __appearance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'appearance'), 'appearance', '__httpwww_opengis_netcitygmltexturedsurface1_0_TexturedSurfaceType_httpwww_opengis_netcitygmltexturedsurface1_0appearance', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 46, 4), )

    
    appearance = property(__appearance.value, __appearance.set, None, None)

    
    # Element baseSurface ({http://www.opengis.net/gml}baseSurface) inherited from {http://www.opengis.net/gml}OrientableSurfaceType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute gid inherited from {http://www.opengis.net/gml}AbstractGeometryType
    
    # Attribute srsName inherited from {http://www.opengis.net/gml}AbstractGeometryType
    
    # Attribute srsDimension inherited from {http://www.opengis.net/gml}AbstractGeometryType
    
    # Attribute axisLabels inherited from {http://www.opengis.net/gml}AbstractGeometryType
    
    # Attribute uomLabels inherited from {http://www.opengis.net/gml}AbstractGeometryType
    
    # Attribute orientation inherited from {http://www.opengis.net/gml}OrientableSurfaceType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __appearance.name() : __appearance
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TexturedSurfaceType = TexturedSurfaceType
Namespace.addCategoryObject('typeBinding', 'TexturedSurfaceType', TexturedSurfaceType)


# Complex type {http://www.opengis.net/citygml/texturedsurface/1.0}AppearancePropertyType with content type ELEMENT_ONLY
class AppearancePropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Deprecated since CityGML version 0.4.0. Use the concepts of the CityGML Appearance module instead. A
                property that has an _Appearance as its value domain, which can either be a Material (Color,...) or a Texture. The
                _Appearance Element can either be encapsulated in an element of this type or an XLink reference to a remote
                _Appearance element (where remote geometry elements are located in another document or elsewhere in the same
                document). Either the reference or the contained element must be given, but neither both nor none. The side of the
                surface the _Appearance refers to is given by the orientation attribute, which refers to the corresponding sign
                attribute of the orientable surface: + means the side with positive orientation, and - the side with negative
                orientation. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AppearancePropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 48, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/citygml/texturedsurface/1.0}_Appearance uses Python identifier Appearance
    __Appearance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_Appearance'), 'Appearance', '__httpwww_opengis_netcitygmltexturedsurface1_0_AppearancePropertyType_httpwww_opengis_netcitygmltexturedsurface1_0_Appearance', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 80, 4), )

    
    Appearance = property(__Appearance.value, __Appearance.set, None, None)

    
    # Attribute orientation uses Python identifier orientation
    __orientation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'orientation'), 'orientation', '__httpwww_opengis_netcitygmltexturedsurface1_0_AppearancePropertyType_orientation', pyxb.bundles.opengis.gml.SignType, unicode_default='+')
    __orientation._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 63, 8)
    __orientation._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 63, 8)
    
    orientation = property(__orientation.value, __orientation.set, None, None)

    
    # Attribute {http://www.opengis.net/gml}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netcitygmltexturedsurface1_0_AppearancePropertyType_httpwww_opengis_netgmlremoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 258, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 269, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, 'Reference to an XML Schema fragment that specifies the content model of the propertys value. This is in conformance with the XML Schema Section 4.14 Referencing Schemas from Elsewhere.')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netcitygmltexturedsurface1_0_AppearancePropertyType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netcitygmltexturedsurface1_0_AppearancePropertyType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netcitygmltexturedsurface1_0_AppearancePropertyType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netcitygmltexturedsurface1_0_AppearancePropertyType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netcitygmltexturedsurface1_0_AppearancePropertyType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netcitygmltexturedsurface1_0_AppearancePropertyType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netcitygmltexturedsurface1_0_AppearancePropertyType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mjW1MNk/PyXB-1.2.5/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __Appearance.name() : __Appearance
    })
    _AttributeMap.update({
        __orientation.name() : __orientation,
        __remoteSchema.name() : __remoteSchema,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.AppearancePropertyType = AppearancePropertyType
Namespace.addCategoryObject('typeBinding', 'AppearancePropertyType', AppearancePropertyType)


# Complex type {http://www.opengis.net/citygml/texturedsurface/1.0}AbstractAppearanceType with content type ELEMENT_ONLY
class AbstractAppearanceType (pyxb.bundles.opengis.gml.AbstractGMLType):
    """Deprecated since CityGML version 0.4.0. Use the concepts of the CityGML Appearance module instead.
                This abstract type is the parent type of MaterialType and SimpleTextureType. It is derived from
                gml:AbstractGMLType, thus it inherits the attribute gml:id and may be referenced by an appearanceProperty,
                although it is defined elsewhere in another appearanceProperty. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractAppearanceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 67, 4)
    _ElementMap = pyxb.bundles.opengis.gml.AbstractGMLType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml.AbstractGMLType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml.AbstractGMLType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractAppearanceType = AbstractAppearanceType
Namespace.addCategoryObject('typeBinding', 'AbstractAppearanceType', AbstractAppearanceType)


# Complex type {http://www.opengis.net/citygml/texturedsurface/1.0}MaterialType with content type ELEMENT_ONLY
class MaterialType (AbstractAppearanceType):
    """Deprecated since CityGML version 0.4.0. Use the concepts of the CityGML Appearance module instead.
                Adopted from X3D standard (http://www.web3d.org/x3d/) """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MaterialType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 82, 4)
    _ElementMap = AbstractAppearanceType._ElementMap.copy()
    _AttributeMap = AbstractAppearanceType._AttributeMap.copy()
    # Base type is AbstractAppearanceType
    
    # Element {http://www.opengis.net/citygml/texturedsurface/1.0}shininess uses Python identifier shininess
    __shininess = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shininess'), 'shininess', '__httpwww_opengis_netcitygmltexturedsurface1_0_MaterialType_httpwww_opengis_netcitygmltexturedsurface1_0shininess', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 91, 20), )

    
    shininess = property(__shininess.value, __shininess.set, None, None)

    
    # Element {http://www.opengis.net/citygml/texturedsurface/1.0}transparency uses Python identifier transparency
    __transparency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transparency'), 'transparency', '__httpwww_opengis_netcitygmltexturedsurface1_0_MaterialType_httpwww_opengis_netcitygmltexturedsurface1_0transparency', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 92, 20), )

    
    transparency = property(__transparency.value, __transparency.set, None, None)

    
    # Element {http://www.opengis.net/citygml/texturedsurface/1.0}ambientIntensity uses Python identifier ambientIntensity
    __ambientIntensity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ambientIntensity'), 'ambientIntensity', '__httpwww_opengis_netcitygmltexturedsurface1_0_MaterialType_httpwww_opengis_netcitygmltexturedsurface1_0ambientIntensity', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 93, 20), )

    
    ambientIntensity = property(__ambientIntensity.value, __ambientIntensity.set, None, None)

    
    # Element {http://www.opengis.net/citygml/texturedsurface/1.0}specularColor uses Python identifier specularColor
    __specularColor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'specularColor'), 'specularColor', '__httpwww_opengis_netcitygmltexturedsurface1_0_MaterialType_httpwww_opengis_netcitygmltexturedsurface1_0specularColor', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 94, 20), )

    
    specularColor = property(__specularColor.value, __specularColor.set, None, None)

    
    # Element {http://www.opengis.net/citygml/texturedsurface/1.0}diffuseColor uses Python identifier diffuseColor
    __diffuseColor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'diffuseColor'), 'diffuseColor', '__httpwww_opengis_netcitygmltexturedsurface1_0_MaterialType_httpwww_opengis_netcitygmltexturedsurface1_0diffuseColor', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 95, 20), )

    
    diffuseColor = property(__diffuseColor.value, __diffuseColor.set, None, None)

    
    # Element {http://www.opengis.net/citygml/texturedsurface/1.0}emissiveColor uses Python identifier emissiveColor
    __emissiveColor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'emissiveColor'), 'emissiveColor', '__httpwww_opengis_netcitygmltexturedsurface1_0_MaterialType_httpwww_opengis_netcitygmltexturedsurface1_0emissiveColor', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 96, 20), )

    
    emissiveColor = property(__emissiveColor.value, __emissiveColor.set, None, None)

    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __shininess.name() : __shininess,
        __transparency.name() : __transparency,
        __ambientIntensity.name() : __ambientIntensity,
        __specularColor.name() : __specularColor,
        __diffuseColor.name() : __diffuseColor,
        __emissiveColor.name() : __emissiveColor
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MaterialType = MaterialType
Namespace.addCategoryObject('typeBinding', 'MaterialType', MaterialType)


# Complex type {http://www.opengis.net/citygml/texturedsurface/1.0}SimpleTextureType with content type ELEMENT_ONLY
class SimpleTextureType (AbstractAppearanceType):
    """Deprecated since CityGML version 0.4.0. Use the concepts of the CityGML Appearance module instead.
                Adopted from X3D standard (http://www.web3d.org/x3d/). ToDo: repeat """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleTextureType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 104, 4)
    _ElementMap = AbstractAppearanceType._ElementMap.copy()
    _AttributeMap = AbstractAppearanceType._AttributeMap.copy()
    # Base type is AbstractAppearanceType
    
    # Element {http://www.opengis.net/citygml/texturedsurface/1.0}textureMap uses Python identifier textureMap
    __textureMap = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'textureMap'), 'textureMap', '__httpwww_opengis_netcitygmltexturedsurface1_0_SimpleTextureType_httpwww_opengis_netcitygmltexturedsurface1_0textureMap', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 113, 20), )

    
    textureMap = property(__textureMap.value, __textureMap.set, None, None)

    
    # Element {http://www.opengis.net/citygml/texturedsurface/1.0}textureCoordinates uses Python identifier textureCoordinates
    __textureCoordinates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'textureCoordinates'), 'textureCoordinates', '__httpwww_opengis_netcitygmltexturedsurface1_0_SimpleTextureType_httpwww_opengis_netcitygmltexturedsurface1_0textureCoordinates', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 114, 20), )

    
    textureCoordinates = property(__textureCoordinates.value, __textureCoordinates.set, None, None)

    
    # Element {http://www.opengis.net/citygml/texturedsurface/1.0}textureType uses Python identifier textureType
    __textureType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'textureType'), 'textureType', '__httpwww_opengis_netcitygmltexturedsurface1_0_SimpleTextureType_httpwww_opengis_netcitygmltexturedsurface1_0textureType', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 115, 20), )

    
    textureType = property(__textureType.value, __textureType.set, None, None)

    
    # Element {http://www.opengis.net/citygml/texturedsurface/1.0}repeat uses Python identifier repeat
    __repeat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'repeat'), 'repeat', '__httpwww_opengis_netcitygmltexturedsurface1_0_SimpleTextureType_httpwww_opengis_netcitygmltexturedsurface1_0repeat', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 116, 20), )

    
    repeat = property(__repeat.value, __repeat.set, None, None)

    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __textureMap.name() : __textureMap,
        __textureCoordinates.name() : __textureCoordinates,
        __textureType.name() : __textureType,
        __repeat.name() : __repeat
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SimpleTextureType = SimpleTextureType
Namespace.addCategoryObject('typeBinding', 'SimpleTextureType', SimpleTextureType)


TexturedSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TexturedSurface'), TexturedSurfaceType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 44, 4))
Namespace.addCategoryObject('elementBinding', TexturedSurface.name().localName(), TexturedSurface)

appearance = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'appearance'), AppearancePropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 46, 4))
Namespace.addCategoryObject('elementBinding', appearance.name().localName(), appearance)

Appearance = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_Appearance'), AbstractAppearanceType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 80, 4))
Namespace.addCategoryObject('elementBinding', Appearance.name().localName(), Appearance)

Material = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Material'), MaterialType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 102, 4))
Namespace.addCategoryObject('elementBinding', Material.name().localName(), Material)

SimpleTexture = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleTexture'), SimpleTextureType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 122, 4))
Namespace.addCategoryObject('elementBinding', SimpleTexture.name().localName(), SimpleTexture)



TexturedSurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'appearance'), AppearancePropertyType, scope=TexturedSurfaceType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 46, 4)))

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
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TexturedSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TexturedSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TexturedSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TexturedSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'baseSurface')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/geometryPrimitives.xsd', 967, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TexturedSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'appearance')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 38, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TexturedSurfaceType._Automaton = _BuildAutomaton()




AppearancePropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_Appearance'), AbstractAppearanceType, abstract=pyxb.binding.datatypes.boolean(1), scope=AppearancePropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 80, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 60, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AppearancePropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_Appearance')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 61, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AppearancePropertyType._Automaton = _BuildAutomaton_()




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
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AbstractAppearanceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AbstractAppearanceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AbstractAppearanceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
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
AbstractAppearanceType._Automaton = _BuildAutomaton_2()




MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shininess'), pyxb.bundles.opengis.citygml.base.doubleBetween0and1, scope=MaterialType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 91, 20)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transparency'), pyxb.bundles.opengis.citygml.base.doubleBetween0and1, scope=MaterialType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 92, 20)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ambientIntensity'), pyxb.bundles.opengis.citygml.base.doubleBetween0and1, scope=MaterialType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 93, 20)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'specularColor'), Color, scope=MaterialType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 94, 20)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'diffuseColor'), Color, scope=MaterialType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 95, 20)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'emissiveColor'), Color, scope=MaterialType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 96, 20)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 91, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 92, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 93, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 94, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 95, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 96, 20))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shininess')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 91, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transparency')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 92, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ambientIntensity')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 93, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'specularColor')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 94, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'diffuseColor')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 95, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'emissiveColor')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 96, 20))
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
MaterialType._Automaton = _BuildAutomaton_3()




SimpleTextureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'textureMap'), pyxb.binding.datatypes.anyURI, scope=SimpleTextureType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 113, 20)))

SimpleTextureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'textureCoordinates'), pyxb.bundles.opengis.gml.doubleList, scope=SimpleTextureType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 114, 20)))

SimpleTextureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'textureType'), TextureTypeType, scope=SimpleTextureType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 115, 20)))

SimpleTextureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'repeat'), pyxb.binding.datatypes.boolean, scope=SimpleTextureType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 116, 20)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 115, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 116, 20))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleTextureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleTextureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleTextureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleTextureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'textureMap')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 113, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleTextureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'textureCoordinates')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 114, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SimpleTextureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'textureType')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 115, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SimpleTextureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'repeat')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/citygml/texturedsurface/1.0/texturedSurface.xsd', 116, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SimpleTextureType._Automaton = _BuildAutomaton_4()


TexturedSurface._setSubstitutionGroup(pyxb.bundles.opengis.gml.OrientableSurface)

Appearance._setSubstitutionGroup(pyxb.bundles.opengis.gml.GML)

Material._setSubstitutionGroup(Appearance)

SimpleTexture._setSubstitutionGroup(Appearance)
