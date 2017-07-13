# ./pyxb/bundles/opengis/gml_3_3/raw/xbt.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:f3081acf489e348908aa0c477c9d001b7a6656f0
# Generated 2017-07-10 00:38:05.932904 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/gml/3.3/xbt

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
import pyxb.bundles.opengis.gml_3_2
import pyxb.binding.datatypes
import pyxb.binding.xml_

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/gml/3.3/xbt', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

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
class STD_ANON (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/extdBaseTypes.xsd', 27, 1)
    _Documentation = None
STD_ANON._InitializeFacetMap()
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {http://www.opengis.net/gml/3.3/xbt}OrdDate
class OrdDate (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrdDate')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/extdBaseTypes.xsd', 57, 1)
    _Documentation = None
OrdDate._CF_pattern = pyxb.binding.facets.CF_pattern()
OrdDate._CF_pattern.addPattern(pattern='-?[0-9]{4}-[0-9]{3}')
OrdDate._InitializeFacetMap(OrdDate._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'OrdDate', OrdDate)
_module_typeBindings.OrdDate = OrdDate

# Atomic simple type: {http://www.opengis.net/gml/3.3/xbt}WeekDate
class WeekDate (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WeekDate')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/extdBaseTypes.xsd', 62, 1)
    _Documentation = None
WeekDate._CF_pattern = pyxb.binding.facets.CF_pattern()
WeekDate._CF_pattern.addPattern(pattern='-?[0-9]{4}-W(0[1-9]|[1-4][0-9]|5[0-3])(-[1-7])?')
WeekDate._InitializeFacetMap(WeekDate._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'WeekDate', WeekDate)
_module_typeBindings.WeekDate = WeekDate

# Union simple type: {http://www.opengis.net/gml/3.3/xbt}TimePositionUnion
# superclasses pyxb.binding.datatypes.anySimpleType
class TimePositionUnion (pyxb.binding.basis.STD_union):

    """Simple type that is a union of pyxb.binding.datatypes.date, pyxb.binding.datatypes.gYearMonth, pyxb.binding.datatypes.gYear, OrdDate, WeekDate, pyxb.binding.datatypes.time, pyxb.binding.datatypes.dateTime, pyxb.binding.datatypes.anyURI, pyxb.binding.datatypes.decimal."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimePositionUnion')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/extdBaseTypes.xsd', 54, 1)
    _Documentation = None

    _MemberTypes = ( pyxb.binding.datatypes.date, pyxb.binding.datatypes.gYearMonth, pyxb.binding.datatypes.gYear, OrdDate, WeekDate, pyxb.binding.datatypes.time, pyxb.binding.datatypes.dateTime, pyxb.binding.datatypes.anyURI, pyxb.binding.datatypes.decimal, )
TimePositionUnion._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TimePositionUnion)
TimePositionUnion._CF_pattern = pyxb.binding.facets.CF_pattern()
TimePositionUnion._InitializeFacetMap(TimePositionUnion._CF_enumeration,
   TimePositionUnion._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TimePositionUnion', TimePositionUnion)
_module_typeBindings.TimePositionUnion = TimePositionUnion

# Complex type {http://www.opengis.net/gml/3.3/xbt}LanguageStringType with content type SIMPLE
class LanguageStringType (pyxb.binding.basis.complexTypeDefinition):
    """gmlxbt:LanguageStringType adds an optional xml:lang attribute to xs:string for the use within the GML schema and in GML application schemas."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LanguageStringType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/extdBaseTypes.xsd', 7, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_opengis_netgml3_3xbt_LanguageStringType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/extdBaseTypes.xsd', 13, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
_module_typeBindings.LanguageStringType = LanguageStringType
Namespace.addCategoryObject('typeBinding', 'LanguageStringType', LanguageStringType)


# Complex type {http://www.opengis.net/gml/3.3/xbt}LanguageStringAuxType with content type SIMPLE
class LanguageStringAuxType (pyxb.bundles.opengis.gml_3_2.StringOrRefType):
    """Complex type {http://www.opengis.net/gml/3.3/xbt}LanguageStringAuxType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LanguageStringAuxType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/extdBaseTypes.xsd', 37, 1)
    _ElementMap = pyxb.bundles.opengis.gml_3_2.StringOrRefType._ElementMap.copy()
    _AttributeMap = pyxb.bundles.opengis.gml_3_2.StringOrRefType._AttributeMap.copy()
    # Base type is pyxb.bundles.opengis.gml_3_2.StringOrRefType
    
    # Attribute remoteSchema inherited from {http://www.opengis.net/gml/3.2}StringOrRefType
    
    # Attribute nilReason inherited from {http://www.opengis.net/gml/3.2}StringOrRefType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_opengis_netgml3_3xbt_LanguageStringAuxType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/extdBaseTypes.xsd', 40, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute type inherited from {http://www.opengis.net/gml/3.2}StringOrRefType
    
    # Attribute href inherited from {http://www.opengis.net/gml/3.2}StringOrRefType
    
    # Attribute role inherited from {http://www.opengis.net/gml/3.2}StringOrRefType
    
    # Attribute arcrole inherited from {http://www.opengis.net/gml/3.2}StringOrRefType
    
    # Attribute title inherited from {http://www.opengis.net/gml/3.2}StringOrRefType
    
    # Attribute show inherited from {http://www.opengis.net/gml/3.2}StringOrRefType
    
    # Attribute actuate inherited from {http://www.opengis.net/gml/3.2}StringOrRefType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
_module_typeBindings.LanguageStringAuxType = LanguageStringAuxType
Namespace.addCategoryObject('typeBinding', 'LanguageStringAuxType', LanguageStringAuxType)


# Complex type {http://www.opengis.net/gml/3.3/xbt}CodeType with content type SIMPLE
class CodeType (LanguageStringType):
    """gmlxbt:CodeType is a generalized type to be used for a term, keyword or name. It adds a XML attribute codeSpace to a term, where the value of the codeSpace attribute (if present) shall indicate a dictionary, thesaurus, classification scheme, authority, or pattern for the term."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/extdBaseTypes.xsd', 17, 1)
    _ElementMap = LanguageStringType._ElementMap.copy()
    _AttributeMap = LanguageStringType._AttributeMap.copy()
    # Base type is LanguageStringType
    
    # Attribute lang inherited from {http://www.opengis.net/gml/3.3/xbt}LanguageStringType
    
    # Attribute codeSpace uses Python identifier codeSpace
    __codeSpace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'codeSpace'), 'codeSpace', '__httpwww_opengis_netgml3_3xbt_CodeType_codeSpace', pyxb.binding.datatypes.anyURI)
    __codeSpace._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/extdBaseTypes.xsd', 23, 4)
    __codeSpace._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/extdBaseTypes.xsd', 23, 4)
    
    codeSpace = property(__codeSpace.value, __codeSpace.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __codeSpace.name() : __codeSpace
    })
_module_typeBindings.CodeType = CodeType
Namespace.addCategoryObject('typeBinding', 'CodeType', CodeType)


# Complex type {http://www.opengis.net/gml/3.3/xbt}CodeWithAuthorityType with content type SIMPLE
class CodeWithAuthorityType (CodeType):
    """gmlxbt:CodeWithAuthorityType requires that the codeSpace attribute is provided in an instance."""
    _TypeDefinition = STD_ANON
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodeWithAuthorityType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/extdBaseTypes.xsd', 27, 1)
    _ElementMap = CodeType._ElementMap.copy()
    _AttributeMap = CodeType._AttributeMap.copy()
    # Base type is CodeType
    
    # Attribute lang inherited from {http://www.opengis.net/gml/3.3/xbt}LanguageStringType
    
    # Attribute codeSpace is restricted from parent
    
    # Attribute codeSpace uses Python identifier codeSpace
    __codeSpace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'codeSpace'), 'codeSpace', '__httpwww_opengis_netgml3_3xbt_CodeType_codeSpace', pyxb.binding.datatypes.anyURI, required=True)
    __codeSpace._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/extdBaseTypes.xsd', 33, 4)
    __codeSpace._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/extdBaseTypes.xsd', 33, 4)
    
    codeSpace = property(__codeSpace.value, __codeSpace.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __codeSpace.name() : __codeSpace
    })
_module_typeBindings.CodeWithAuthorityType = CodeWithAuthorityType
Namespace.addCategoryObject('typeBinding', 'CodeWithAuthorityType', CodeWithAuthorityType)


description = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), LanguageStringAuxType, documentation='The value of this property is a text description of the object with optional xml:lang attribute.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/extdBaseTypes.xsd', 44, 1))
Namespace.addCategoryObject('elementBinding', description.name().localName(), description)

remarks = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'remarks'), LanguageStringType, documentation='The value of this property is a text description of the object with optional xml:lang attribute.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/gml/3.3/extdBaseTypes.xsd', 49, 1))
Namespace.addCategoryObject('elementBinding', remarks.name().localName(), remarks)

description._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_2.description)

remarks._setSubstitutionGroup(pyxb.bundles.opengis.gml_3_2.remarks)
