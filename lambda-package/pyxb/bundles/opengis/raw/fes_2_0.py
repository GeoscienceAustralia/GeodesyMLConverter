# ./pyxb/bundles/opengis/raw/fes_2_0.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:5ccf7e0a51e32f724a27302a5ff18a5d73e4062c
# Generated 2017-07-10 00:36:51.918115 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/fes/2.0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:ddad342c-6507-11e7-99ea-0a55f9edafa5')

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
import pyxb.bundles.opengis.ows_1_1

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/fes/2.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ows = pyxb.bundles.opengis.ows_1_1.Namespace
_Namespace_ows.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://www.opengis.net/fes/2.0}VersionActionTokens
class VersionActionTokens (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VersionActionTokens')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 227, 3)
    _Documentation = None
VersionActionTokens._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VersionActionTokens, enum_prefix=None)
VersionActionTokens.FIRST = VersionActionTokens._CF_enumeration.addEnumeration(unicode_value='FIRST', tag='FIRST')
VersionActionTokens.LAST = VersionActionTokens._CF_enumeration.addEnumeration(unicode_value='LAST', tag='LAST')
VersionActionTokens.PREVIOUS = VersionActionTokens._CF_enumeration.addEnumeration(unicode_value='PREVIOUS', tag='PREVIOUS')
VersionActionTokens.NEXT = VersionActionTokens._CF_enumeration.addEnumeration(unicode_value='NEXT', tag='NEXT')
VersionActionTokens.ALL = VersionActionTokens._CF_enumeration.addEnumeration(unicode_value='ALL', tag='ALL')
VersionActionTokens._InitializeFacetMap(VersionActionTokens._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VersionActionTokens', VersionActionTokens)
_module_typeBindings.VersionActionTokens = VersionActionTokens

# Atomic simple type: {http://www.opengis.net/fes/2.0}MatchActionType
class MatchActionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MatchActionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 253, 3)
    _Documentation = None
MatchActionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MatchActionType, enum_prefix=None)
MatchActionType.All = MatchActionType._CF_enumeration.addEnumeration(unicode_value='All', tag='All')
MatchActionType.Any = MatchActionType._CF_enumeration.addEnumeration(unicode_value='Any', tag='Any')
MatchActionType.One = MatchActionType._CF_enumeration.addEnumeration(unicode_value='One', tag='One')
MatchActionType._InitializeFacetMap(MatchActionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MatchActionType', MatchActionType)
_module_typeBindings.MatchActionType = MatchActionType

# Atomic simple type: {http://www.opengis.net/fes/2.0}UomSymbol
class UomSymbol (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UomSymbol')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 386, 3)
    _Documentation = None
UomSymbol._CF_pattern = pyxb.binding.facets.CF_pattern()
UomSymbol._CF_pattern.addPattern(pattern='[^: \\n\\r\\t]+')
UomSymbol._InitializeFacetMap(UomSymbol._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'UomSymbol', UomSymbol)
_module_typeBindings.UomSymbol = UomSymbol

# Atomic simple type: {http://www.opengis.net/fes/2.0}UomURI
class UomURI (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UomURI')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 391, 3)
    _Documentation = None
UomURI._CF_pattern = pyxb.binding.facets.CF_pattern()
UomURI._CF_pattern.addPattern(pattern='([a-zA-Z][a-zA-Z0-9\\-\\+\\.]*:|\\.\\./|\\./|#).*')
UomURI._InitializeFacetMap(UomURI._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'UomURI', UomURI)
_module_typeBindings.UomURI = UomURI

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 99, 9)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.PropertyIsEqualTo = STD_ANON._CF_enumeration.addEnumeration(unicode_value='PropertyIsEqualTo', tag='PropertyIsEqualTo')
STD_ANON.PropertyIsNotEqualTo = STD_ANON._CF_enumeration.addEnumeration(unicode_value='PropertyIsNotEqualTo', tag='PropertyIsNotEqualTo')
STD_ANON.PropertyIsLessThan = STD_ANON._CF_enumeration.addEnumeration(unicode_value='PropertyIsLessThan', tag='PropertyIsLessThan')
STD_ANON.PropertyIsGreaterThan = STD_ANON._CF_enumeration.addEnumeration(unicode_value='PropertyIsGreaterThan', tag='PropertyIsGreaterThan')
STD_ANON.PropertyIsLessThanOrEqualTo = STD_ANON._CF_enumeration.addEnumeration(unicode_value='PropertyIsLessThanOrEqualTo', tag='PropertyIsLessThanOrEqualTo')
STD_ANON.PropertyIsGreaterThanOrEqualTo = STD_ANON._CF_enumeration.addEnumeration(unicode_value='PropertyIsGreaterThanOrEqualTo', tag='PropertyIsGreaterThanOrEqualTo')
STD_ANON.PropertyIsLike = STD_ANON._CF_enumeration.addEnumeration(unicode_value='PropertyIsLike', tag='PropertyIsLike')
STD_ANON.PropertyIsNull = STD_ANON._CF_enumeration.addEnumeration(unicode_value='PropertyIsNull', tag='PropertyIsNull')
STD_ANON.PropertyIsNil = STD_ANON._CF_enumeration.addEnumeration(unicode_value='PropertyIsNil', tag='PropertyIsNil')
STD_ANON.PropertyIsBetween = STD_ANON._CF_enumeration.addEnumeration(unicode_value='PropertyIsBetween', tag='PropertyIsBetween')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 113, 9)
    _Documentation = None
STD_ANON_._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_._CF_pattern.addPattern(pattern='extension:\\w{2,}')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_pattern)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 184, 9)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.BBOX = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='BBOX', tag='BBOX')
STD_ANON_2.Equals = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Equals', tag='Equals')
STD_ANON_2.Disjoint = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Disjoint', tag='Disjoint')
STD_ANON_2.Intersects = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Intersects', tag='Intersects')
STD_ANON_2.Touches = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Touches', tag='Touches')
STD_ANON_2.Crosses = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Crosses', tag='Crosses')
STD_ANON_2.Within = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Within', tag='Within')
STD_ANON_2.Contains = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Contains', tag='Contains')
STD_ANON_2.Overlaps = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Overlaps', tag='Overlaps')
STD_ANON_2.Beyond = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Beyond', tag='Beyond')
STD_ANON_2.DWithin = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='DWithin', tag='DWithin')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 199, 9)
    _Documentation = None
STD_ANON_3._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_3._CF_pattern.addPattern(pattern='extension:\\w{2,}')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_pattern)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 243, 9)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.After = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='After', tag='After')
STD_ANON_4.Before = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Before', tag='Before')
STD_ANON_4.Begins = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Begins', tag='Begins')
STD_ANON_4.BegunBy = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='BegunBy', tag='BegunBy')
STD_ANON_4.TContains = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='TContains', tag='TContains')
STD_ANON_4.During = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='During', tag='During')
STD_ANON_4.TEquals = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='TEquals', tag='TEquals')
STD_ANON_4.TOverlaps = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='TOverlaps', tag='TOverlaps')
STD_ANON_4.Meets = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Meets', tag='Meets')
STD_ANON_4.OverlappedBy = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='OverlappedBy', tag='OverlappedBy')
STD_ANON_4.MetBy = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='MetBy', tag='MetBy')
STD_ANON_4.Ends = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Ends', tag='Ends')
STD_ANON_4.EndedBy = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='EndedBy', tag='EndedBy')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 260, 9)
    _Documentation = None
STD_ANON_5._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_5._CF_pattern.addPattern(pattern='extension:\\w{2,}')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_pattern)
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# Atomic simple type: {http://www.opengis.net/fes/2.0}SchemaElement
class SchemaElement (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SchemaElement')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 52, 3)
    _Documentation = None
SchemaElement._CF_pattern = pyxb.binding.facets.CF_pattern()
SchemaElement._CF_pattern.addPattern(pattern='schema\\-element\\(.+\\)')
SchemaElement._InitializeFacetMap(SchemaElement._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SchemaElement', SchemaElement)
_module_typeBindings.SchemaElement = SchemaElement

# List simple type: {http://www.opengis.net/fes/2.0}AliasesType
# superclasses pyxb.binding.datatypes.anySimpleType
class AliasesType (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.NCName."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AliasesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 57, 3)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.NCName
AliasesType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'AliasesType', AliasesType)
_module_typeBindings.AliasesType = AliasesType

# Atomic simple type: {http://www.opengis.net/fes/2.0}SortOrderType
class SortOrderType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SortOrderType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/sort.xsd', 43, 3)
    _Documentation = None
SortOrderType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SortOrderType, enum_prefix=None)
SortOrderType.DESC = SortOrderType._CF_enumeration.addEnumeration(unicode_value='DESC', tag='DESC')
SortOrderType.ASC = SortOrderType._CF_enumeration.addEnumeration(unicode_value='ASC', tag='ASC')
SortOrderType._InitializeFacetMap(SortOrderType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SortOrderType', SortOrderType)
_module_typeBindings.SortOrderType = SortOrderType

# Union simple type: {http://www.opengis.net/fes/2.0}VersionType
# superclasses pyxb.binding.datatypes.anySimpleType
class VersionType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of VersionActionTokens, pyxb.binding.datatypes.positiveInteger, pyxb.binding.datatypes.dateTime."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VersionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 221, 3)
    _Documentation = None

    _MemberTypes = ( VersionActionTokens, pyxb.binding.datatypes.positiveInteger, pyxb.binding.datatypes.dateTime, )
VersionType._CF_pattern = pyxb.binding.facets.CF_pattern()
VersionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VersionType)
VersionType.FIRST = 'FIRST'                       # originally VersionActionTokens.FIRST
VersionType.LAST = 'LAST'                         # originally VersionActionTokens.LAST
VersionType.PREVIOUS = 'PREVIOUS'                 # originally VersionActionTokens.PREVIOUS
VersionType.NEXT = 'NEXT'                         # originally VersionActionTokens.NEXT
VersionType.ALL = 'ALL'                           # originally VersionActionTokens.ALL
VersionType._InitializeFacetMap(VersionType._CF_pattern,
   VersionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VersionType', VersionType)
_module_typeBindings.VersionType = VersionType

# Union simple type: {http://www.opengis.net/fes/2.0}UomIdentifier
# superclasses pyxb.binding.datatypes.anySimpleType
class UomIdentifier (pyxb.binding.basis.STD_union):

    """Simple type that is a union of UomSymbol, UomURI."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UomIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 383, 3)
    _Documentation = None

    _MemberTypes = ( UomSymbol, UomURI, )
UomIdentifier._CF_pattern = pyxb.binding.facets.CF_pattern()
UomIdentifier._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UomIdentifier)
UomIdentifier._InitializeFacetMap(UomIdentifier._CF_pattern,
   UomIdentifier._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UomIdentifier', UomIdentifier)
_module_typeBindings.UomIdentifier = UomIdentifier

# Union simple type: {http://www.opengis.net/fes/2.0}ComparisonOperatorNameType
# superclasses pyxb.binding.datatypes.anySimpleType
class ComparisonOperatorNameType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of STD_ANON, STD_ANON_."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ComparisonOperatorNameType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 97, 3)
    _Documentation = None

    _MemberTypes = ( STD_ANON, STD_ANON_, )
ComparisonOperatorNameType._CF_pattern = pyxb.binding.facets.CF_pattern()
ComparisonOperatorNameType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ComparisonOperatorNameType)
ComparisonOperatorNameType.PropertyIsEqualTo = 'PropertyIsEqualTo'# originally STD_ANON.PropertyIsEqualTo
ComparisonOperatorNameType.PropertyIsNotEqualTo = 'PropertyIsNotEqualTo'# originally STD_ANON.PropertyIsNotEqualTo
ComparisonOperatorNameType.PropertyIsLessThan = 'PropertyIsLessThan'# originally STD_ANON.PropertyIsLessThan
ComparisonOperatorNameType.PropertyIsGreaterThan = 'PropertyIsGreaterThan'# originally STD_ANON.PropertyIsGreaterThan
ComparisonOperatorNameType.PropertyIsLessThanOrEqualTo = 'PropertyIsLessThanOrEqualTo'# originally STD_ANON.PropertyIsLessThanOrEqualTo
ComparisonOperatorNameType.PropertyIsGreaterThanOrEqualTo = 'PropertyIsGreaterThanOrEqualTo'# originally STD_ANON.PropertyIsGreaterThanOrEqualTo
ComparisonOperatorNameType.PropertyIsLike = 'PropertyIsLike'# originally STD_ANON.PropertyIsLike
ComparisonOperatorNameType.PropertyIsNull = 'PropertyIsNull'# originally STD_ANON.PropertyIsNull
ComparisonOperatorNameType.PropertyIsNil = 'PropertyIsNil'# originally STD_ANON.PropertyIsNil
ComparisonOperatorNameType.PropertyIsBetween = 'PropertyIsBetween'# originally STD_ANON.PropertyIsBetween
ComparisonOperatorNameType._InitializeFacetMap(ComparisonOperatorNameType._CF_pattern,
   ComparisonOperatorNameType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ComparisonOperatorNameType', ComparisonOperatorNameType)
_module_typeBindings.ComparisonOperatorNameType = ComparisonOperatorNameType

# Union simple type: {http://www.opengis.net/fes/2.0}SpatialOperatorNameType
# superclasses pyxb.binding.datatypes.anySimpleType
class SpatialOperatorNameType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of STD_ANON_2, STD_ANON_3."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpatialOperatorNameType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 182, 3)
    _Documentation = None

    _MemberTypes = ( STD_ANON_2, STD_ANON_3, )
SpatialOperatorNameType._CF_pattern = pyxb.binding.facets.CF_pattern()
SpatialOperatorNameType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SpatialOperatorNameType)
SpatialOperatorNameType.BBOX = 'BBOX'             # originally STD_ANON_2.BBOX
SpatialOperatorNameType.Equals = 'Equals'         # originally STD_ANON_2.Equals
SpatialOperatorNameType.Disjoint = 'Disjoint'     # originally STD_ANON_2.Disjoint
SpatialOperatorNameType.Intersects = 'Intersects' # originally STD_ANON_2.Intersects
SpatialOperatorNameType.Touches = 'Touches'       # originally STD_ANON_2.Touches
SpatialOperatorNameType.Crosses = 'Crosses'       # originally STD_ANON_2.Crosses
SpatialOperatorNameType.Within = 'Within'         # originally STD_ANON_2.Within
SpatialOperatorNameType.Contains = 'Contains'     # originally STD_ANON_2.Contains
SpatialOperatorNameType.Overlaps = 'Overlaps'     # originally STD_ANON_2.Overlaps
SpatialOperatorNameType.Beyond = 'Beyond'         # originally STD_ANON_2.Beyond
SpatialOperatorNameType.DWithin = 'DWithin'       # originally STD_ANON_2.DWithin
SpatialOperatorNameType._InitializeFacetMap(SpatialOperatorNameType._CF_pattern,
   SpatialOperatorNameType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SpatialOperatorNameType', SpatialOperatorNameType)
_module_typeBindings.SpatialOperatorNameType = SpatialOperatorNameType

# Union simple type: {http://www.opengis.net/fes/2.0}TemporalOperatorNameType
# superclasses pyxb.binding.datatypes.anySimpleType
class TemporalOperatorNameType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of STD_ANON_4, STD_ANON_5."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TemporalOperatorNameType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 241, 3)
    _Documentation = None

    _MemberTypes = ( STD_ANON_4, STD_ANON_5, )
TemporalOperatorNameType._CF_pattern = pyxb.binding.facets.CF_pattern()
TemporalOperatorNameType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TemporalOperatorNameType)
TemporalOperatorNameType.After = 'After'          # originally STD_ANON_4.After
TemporalOperatorNameType.Before = 'Before'        # originally STD_ANON_4.Before
TemporalOperatorNameType.Begins = 'Begins'        # originally STD_ANON_4.Begins
TemporalOperatorNameType.BegunBy = 'BegunBy'      # originally STD_ANON_4.BegunBy
TemporalOperatorNameType.TContains = 'TContains'  # originally STD_ANON_4.TContains
TemporalOperatorNameType.During = 'During'        # originally STD_ANON_4.During
TemporalOperatorNameType.TEquals = 'TEquals'      # originally STD_ANON_4.TEquals
TemporalOperatorNameType.TOverlaps = 'TOverlaps'  # originally STD_ANON_4.TOverlaps
TemporalOperatorNameType.Meets = 'Meets'          # originally STD_ANON_4.Meets
TemporalOperatorNameType.OverlappedBy = 'OverlappedBy'# originally STD_ANON_4.OverlappedBy
TemporalOperatorNameType.MetBy = 'MetBy'          # originally STD_ANON_4.MetBy
TemporalOperatorNameType.Ends = 'Ends'            # originally STD_ANON_4.Ends
TemporalOperatorNameType.EndedBy = 'EndedBy'      # originally STD_ANON_4.EndedBy
TemporalOperatorNameType._InitializeFacetMap(TemporalOperatorNameType._CF_pattern,
   TemporalOperatorNameType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TemporalOperatorNameType', TemporalOperatorNameType)
_module_typeBindings.TemporalOperatorNameType = TemporalOperatorNameType

# Union simple type: {http://www.opengis.net/fes/2.0}TypeNamesType
# superclasses pyxb.binding.datatypes.anySimpleType
class TypeNamesType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of SchemaElement, pyxb.binding.datatypes.QName."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TypeNamesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 49, 3)
    _Documentation = None

    _MemberTypes = ( SchemaElement, pyxb.binding.datatypes.QName, )
TypeNamesType._CF_pattern = pyxb.binding.facets.CF_pattern()
TypeNamesType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TypeNamesType)
TypeNamesType._InitializeFacetMap(TypeNamesType._CF_pattern,
   TypeNamesType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TypeNamesType', TypeNamesType)
_module_typeBindings.TypeNamesType = TypeNamesType

# List simple type: {http://www.opengis.net/fes/2.0}TypeNamesListType
# superclasses pyxb.binding.datatypes.anySimpleType
class TypeNamesListType (pyxb.binding.basis.STD_list):

    """Simple type that is a list of TypeNamesType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TypeNamesListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 46, 3)
    _Documentation = None

    _ItemType = TypeNamesType
TypeNamesListType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'TypeNamesListType', TypeNamesListType)
_module_typeBindings.TypeNamesListType = TypeNamesListType

# Complex type {http://www.opengis.net/fes/2.0}FunctionType with content type ELEMENT_ONLY
class FunctionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}FunctionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FunctionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 26, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netfes2_0_FunctionType_httpwww_opengis_netfes2_0expression', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netfes2_0_FunctionType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 31, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 31, 6)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __expression.name() : __expression
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.FunctionType = FunctionType
Namespace.addCategoryObject('typeBinding', 'FunctionType', FunctionType)


# Complex type {http://www.opengis.net/fes/2.0}LiteralType with content type MIXED
class LiteralType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}LiteralType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LiteralType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 36, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_opengis_netfes2_0_LiteralType_type', pyxb.binding.datatypes.QName)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 40, 6)
    __type._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 40, 6)
    
    type = property(__type.value, __type.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.LiteralType = LiteralType
Namespace.addCategoryObject('typeBinding', 'LiteralType', LiteralType)


# Complex type {http://www.opengis.net/fes/2.0}ComparisonOpsType with content type EMPTY
class ComparisonOpsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}ComparisonOpsType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ComparisonOpsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 56, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ComparisonOpsType = ComparisonOpsType
Namespace.addCategoryObject('typeBinding', 'ComparisonOpsType', ComparisonOpsType)


# Complex type {http://www.opengis.net/fes/2.0}SpatialOpsType with content type EMPTY
class SpatialOpsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}SpatialOpsType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpatialOpsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 92, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SpatialOpsType = SpatialOpsType
Namespace.addCategoryObject('typeBinding', 'SpatialOpsType', SpatialOpsType)


# Complex type {http://www.opengis.net/fes/2.0}TemporalOpsType with content type EMPTY
class TemporalOpsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}TemporalOpsType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TemporalOpsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 131, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TemporalOpsType = TemporalOpsType
Namespace.addCategoryObject('typeBinding', 'TemporalOpsType', TemporalOpsType)


# Complex type {http://www.opengis.net/fes/2.0}LogicOpsType with content type EMPTY
class LogicOpsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}LogicOpsType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogicOpsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 179, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LogicOpsType = LogicOpsType
Namespace.addCategoryObject('typeBinding', 'LogicOpsType', LogicOpsType)


# Complex type {http://www.opengis.net/fes/2.0}ExtensionOpsType with content type EMPTY
class ExtensionOpsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}ExtensionOpsType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExtensionOpsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 196, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ExtensionOpsType = ExtensionOpsType
Namespace.addCategoryObject('typeBinding', 'ExtensionOpsType', ExtensionOpsType)


# Complex type {http://www.opengis.net/fes/2.0}AbstractIdType with content type EMPTY
class AbstractIdType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}AbstractIdType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 202, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractIdType = AbstractIdType
Namespace.addCategoryObject('typeBinding', 'AbstractIdType', AbstractIdType)


# Complex type {http://www.opengis.net/fes/2.0}LowerBoundaryType with content type ELEMENT_ONLY
class LowerBoundaryType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}LowerBoundaryType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LowerBoundaryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 303, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netfes2_0_LowerBoundaryType_httpwww_opengis_netfes2_0expression', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    _ElementMap.update({
        __expression.name() : __expression
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LowerBoundaryType = LowerBoundaryType
Namespace.addCategoryObject('typeBinding', 'LowerBoundaryType', LowerBoundaryType)


# Complex type {http://www.opengis.net/fes/2.0}UpperBoundaryType with content type ELEMENT_ONLY
class UpperBoundaryType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}UpperBoundaryType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UpperBoundaryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 308, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netfes2_0_UpperBoundaryType_httpwww_opengis_netfes2_0expression', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    _ElementMap.update({
        __expression.name() : __expression
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UpperBoundaryType = UpperBoundaryType
Namespace.addCategoryObject('typeBinding', 'UpperBoundaryType', UpperBoundaryType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 29, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}Conformance uses Python identifier Conformance
    __Conformance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Conformance'), 'Conformance', '__httpwww_opengis_netfes2_0_CTD_ANON_httpwww_opengis_netfes2_0Conformance', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 31, 12), )

    
    Conformance = property(__Conformance.value, __Conformance.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}Id_Capabilities uses Python identifier Id_Capabilities
    __Id_Capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id_Capabilities'), 'Id_Capabilities', '__httpwww_opengis_netfes2_0_CTD_ANON_httpwww_opengis_netfes2_0Id_Capabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 33, 12), )

    
    Id_Capabilities = property(__Id_Capabilities.value, __Id_Capabilities.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}Scalar_Capabilities uses Python identifier Scalar_Capabilities
    __Scalar_Capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Scalar_Capabilities'), 'Scalar_Capabilities', '__httpwww_opengis_netfes2_0_CTD_ANON_httpwww_opengis_netfes2_0Scalar_Capabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 36, 12), )

    
    Scalar_Capabilities = property(__Scalar_Capabilities.value, __Scalar_Capabilities.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}Spatial_Capabilities uses Python identifier Spatial_Capabilities
    __Spatial_Capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Spatial_Capabilities'), 'Spatial_Capabilities', '__httpwww_opengis_netfes2_0_CTD_ANON_httpwww_opengis_netfes2_0Spatial_Capabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 39, 12), )

    
    Spatial_Capabilities = property(__Spatial_Capabilities.value, __Spatial_Capabilities.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}Temporal_Capabilities uses Python identifier Temporal_Capabilities
    __Temporal_Capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Temporal_Capabilities'), 'Temporal_Capabilities', '__httpwww_opengis_netfes2_0_CTD_ANON_httpwww_opengis_netfes2_0Temporal_Capabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 42, 12), )

    
    Temporal_Capabilities = property(__Temporal_Capabilities.value, __Temporal_Capabilities.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}Functions uses Python identifier Functions
    __Functions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Functions'), 'Functions', '__httpwww_opengis_netfes2_0_CTD_ANON_httpwww_opengis_netfes2_0Functions', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 45, 12), )

    
    Functions = property(__Functions.value, __Functions.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}Extended_Capabilities uses Python identifier Extended_Capabilities
    __Extended_Capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extended_Capabilities'), 'Extended_Capabilities', '__httpwww_opengis_netfes2_0_CTD_ANON_httpwww_opengis_netfes2_0Extended_Capabilities', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 47, 12), )

    
    Extended_Capabilities = property(__Extended_Capabilities.value, __Extended_Capabilities.set, None, None)

    _ElementMap.update({
        __Conformance.name() : __Conformance,
        __Id_Capabilities.name() : __Id_Capabilities,
        __Scalar_Capabilities.name() : __Scalar_Capabilities,
        __Spatial_Capabilities.name() : __Spatial_Capabilities,
        __Temporal_Capabilities.name() : __Temporal_Capabilities,
        __Functions.name() : __Functions,
        __Extended_Capabilities.name() : __Extended_Capabilities
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://www.opengis.net/fes/2.0}ConformanceType with content type ELEMENT_ONLY
class ConformanceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}ConformanceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConformanceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 55, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}Constraint uses Python identifier Constraint
    __Constraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), 'Constraint', '__httpwww_opengis_netfes2_0_ConformanceType_httpwww_opengis_netfes2_0Constraint', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 57, 9), )

    
    Constraint = property(__Constraint.value, __Constraint.set, None, None)

    _ElementMap.update({
        __Constraint.name() : __Constraint
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ConformanceType = ConformanceType
Namespace.addCategoryObject('typeBinding', 'ConformanceType', ConformanceType)


# Complex type {http://www.opengis.net/fes/2.0}Id_CapabilitiesType with content type ELEMENT_ONLY
class Id_CapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}Id_CapabilitiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Id_CapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 63, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}ResourceIdentifier uses Python identifier ResourceIdentifier
    __ResourceIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResourceIdentifier'), 'ResourceIdentifier', '__httpwww_opengis_netfes2_0_Id_CapabilitiesType_httpwww_opengis_netfes2_0ResourceIdentifier', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 65, 9), )

    
    ResourceIdentifier = property(__ResourceIdentifier.value, __ResourceIdentifier.set, None, None)

    _ElementMap.update({
        __ResourceIdentifier.name() : __ResourceIdentifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Id_CapabilitiesType = Id_CapabilitiesType
Namespace.addCategoryObject('typeBinding', 'Id_CapabilitiesType', Id_CapabilitiesType)


# Complex type {http://www.opengis.net/fes/2.0}ResourceIdentifierType with content type ELEMENT_ONLY
class ResourceIdentifierType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}ResourceIdentifierType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceIdentifierType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 69, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata'), 'Metadata', '__httpwww_opengis_netfes2_0_ResourceIdentifierType_httpwww_opengis_netows1_1Metadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 42, 1), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netfes2_0_ResourceIdentifierType_name', pyxb.binding.datatypes.QName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 73, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 73, 6)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __Metadata.name() : __Metadata
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.ResourceIdentifierType = ResourceIdentifierType
Namespace.addCategoryObject('typeBinding', 'ResourceIdentifierType', ResourceIdentifierType)


# Complex type {http://www.opengis.net/fes/2.0}Scalar_CapabilitiesType with content type ELEMENT_ONLY
class Scalar_CapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}Scalar_CapabilitiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Scalar_CapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 77, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}ComparisonOperators uses Python identifier ComparisonOperators
    __ComparisonOperators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ComparisonOperators'), 'ComparisonOperators', '__httpwww_opengis_netfes2_0_Scalar_CapabilitiesType_httpwww_opengis_netfes2_0ComparisonOperators', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 80, 9), )

    
    ComparisonOperators = property(__ComparisonOperators.value, __ComparisonOperators.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}LogicalOperators uses Python identifier LogicalOperators
    __LogicalOperators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LogicalOperators'), 'LogicalOperators', '__httpwww_opengis_netfes2_0_Scalar_CapabilitiesType_httpwww_opengis_netfes2_0LogicalOperators', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 84, 3), )

    
    LogicalOperators = property(__LogicalOperators.value, __LogicalOperators.set, None, None)

    _ElementMap.update({
        __ComparisonOperators.name() : __ComparisonOperators,
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
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 85, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {http://www.opengis.net/fes/2.0}ComparisonOperatorsType with content type ELEMENT_ONLY
class ComparisonOperatorsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}ComparisonOperatorsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ComparisonOperatorsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 87, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}ComparisonOperator uses Python identifier ComparisonOperator
    __ComparisonOperator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ComparisonOperator'), 'ComparisonOperator', '__httpwww_opengis_netfes2_0_ComparisonOperatorsType_httpwww_opengis_netfes2_0ComparisonOperator', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 89, 9), )

    
    ComparisonOperator = property(__ComparisonOperator.value, __ComparisonOperator.set, None, None)

    _ElementMap.update({
        __ComparisonOperator.name() : __ComparisonOperator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ComparisonOperatorsType = ComparisonOperatorsType
Namespace.addCategoryObject('typeBinding', 'ComparisonOperatorsType', ComparisonOperatorsType)


# Complex type {http://www.opengis.net/fes/2.0}AvailableFunctionsType with content type ELEMENT_ONLY
class AvailableFunctionsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}AvailableFunctionsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AvailableFunctionsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 120, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}Function uses Python identifier Function
    __Function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Function'), 'Function', '__httpwww_opengis_netfes2_0_AvailableFunctionsType_httpwww_opengis_netfes2_0Function', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 122, 9), )

    
    Function = property(__Function.value, __Function.set, None, None)

    _ElementMap.update({
        __Function.name() : __Function
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AvailableFunctionsType = AvailableFunctionsType
Namespace.addCategoryObject('typeBinding', 'AvailableFunctionsType', AvailableFunctionsType)


# Complex type {http://www.opengis.net/fes/2.0}AvailableFunctionType with content type ELEMENT_ONLY
class AvailableFunctionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}AvailableFunctionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AvailableFunctionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 126, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}Returns uses Python identifier Returns
    __Returns = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Returns'), 'Returns', '__httpwww_opengis_netfes2_0_AvailableFunctionType_httpwww_opengis_netfes2_0Returns', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 129, 9), )

    
    Returns = property(__Returns.value, __Returns.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}Arguments uses Python identifier Arguments
    __Arguments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Arguments'), 'Arguments', '__httpwww_opengis_netfes2_0_AvailableFunctionType_httpwww_opengis_netfes2_0Arguments', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 130, 9), )

    
    Arguments = property(__Arguments.value, __Arguments.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata'), 'Metadata', '__httpwww_opengis_netfes2_0_AvailableFunctionType_httpwww_opengis_netows1_1Metadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 42, 1), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netfes2_0_AvailableFunctionType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 133, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 133, 6)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __Returns.name() : __Returns,
        __Arguments.name() : __Arguments,
        __Metadata.name() : __Metadata
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.AvailableFunctionType = AvailableFunctionType
Namespace.addCategoryObject('typeBinding', 'AvailableFunctionType', AvailableFunctionType)


# Complex type {http://www.opengis.net/fes/2.0}ArgumentsType with content type ELEMENT_ONLY
class ArgumentsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}ArgumentsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArgumentsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 135, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}Argument uses Python identifier Argument
    __Argument = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Argument'), 'Argument', '__httpwww_opengis_netfes2_0_ArgumentsType_httpwww_opengis_netfes2_0Argument', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 137, 9), )

    
    Argument = property(__Argument.value, __Argument.set, None, None)

    _ElementMap.update({
        __Argument.name() : __Argument
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ArgumentsType = ArgumentsType
Namespace.addCategoryObject('typeBinding', 'ArgumentsType', ArgumentsType)


# Complex type {http://www.opengis.net/fes/2.0}ArgumentType with content type ELEMENT_ONLY
class ArgumentType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}ArgumentType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArgumentType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 141, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Type'), 'Type', '__httpwww_opengis_netfes2_0_ArgumentType_httpwww_opengis_netfes2_0Type', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 144, 9), )

    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata'), 'Metadata', '__httpwww_opengis_netfes2_0_ArgumentType_httpwww_opengis_netows1_1Metadata', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 42, 1), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netfes2_0_ArgumentType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 146, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 146, 6)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __Type.name() : __Type,
        __Metadata.name() : __Metadata
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.ArgumentType = ArgumentType
Namespace.addCategoryObject('typeBinding', 'ArgumentType', ArgumentType)


# Complex type {http://www.opengis.net/fes/2.0}Spatial_CapabilitiesType with content type ELEMENT_ONLY
class Spatial_CapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}Spatial_CapabilitiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Spatial_CapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 150, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}GeometryOperands uses Python identifier GeometryOperands
    __GeometryOperands = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperands'), 'GeometryOperands', '__httpwww_opengis_netfes2_0_Spatial_CapabilitiesType_httpwww_opengis_netfes2_0GeometryOperands', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 152, 9), )

    
    GeometryOperands = property(__GeometryOperands.value, __GeometryOperands.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}SpatialOperators uses Python identifier SpatialOperators
    __SpatialOperators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SpatialOperators'), 'SpatialOperators', '__httpwww_opengis_netfes2_0_Spatial_CapabilitiesType_httpwww_opengis_netfes2_0SpatialOperators', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 154, 9), )

    
    SpatialOperators = property(__SpatialOperators.value, __SpatialOperators.set, None, None)

    _ElementMap.update({
        __GeometryOperands.name() : __GeometryOperands,
        __SpatialOperators.name() : __SpatialOperators
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Spatial_CapabilitiesType = Spatial_CapabilitiesType
Namespace.addCategoryObject('typeBinding', 'Spatial_CapabilitiesType', Spatial_CapabilitiesType)


# Complex type {http://www.opengis.net/fes/2.0}GeometryOperandsType with content type ELEMENT_ONLY
class GeometryOperandsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}GeometryOperandsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeometryOperandsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 158, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}GeometryOperand uses Python identifier GeometryOperand
    __GeometryOperand = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperand'), 'GeometryOperand', '__httpwww_opengis_netfes2_0_GeometryOperandsType_httpwww_opengis_netfes2_0GeometryOperand', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 160, 9), )

    
    GeometryOperand = property(__GeometryOperand.value, __GeometryOperand.set, None, None)

    _ElementMap.update({
        __GeometryOperand.name() : __GeometryOperand
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GeometryOperandsType = GeometryOperandsType
Namespace.addCategoryObject('typeBinding', 'GeometryOperandsType', GeometryOperandsType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 161, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netfes2_0_CTD_ANON_2_name', pyxb.binding.datatypes.QName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 162, 15)
    __name._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 162, 15)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type {http://www.opengis.net/fes/2.0}SpatialOperatorsType with content type ELEMENT_ONLY
class SpatialOperatorsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}SpatialOperatorsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpatialOperatorsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 167, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}SpatialOperator uses Python identifier SpatialOperator
    __SpatialOperator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SpatialOperator'), 'SpatialOperator', '__httpwww_opengis_netfes2_0_SpatialOperatorsType_httpwww_opengis_netfes2_0SpatialOperator', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 169, 9), )

    
    SpatialOperator = property(__SpatialOperator.value, __SpatialOperator.set, None, None)

    _ElementMap.update({
        __SpatialOperator.name() : __SpatialOperator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SpatialOperatorsType = SpatialOperatorsType
Namespace.addCategoryObject('typeBinding', 'SpatialOperatorsType', SpatialOperatorsType)


# Complex type {http://www.opengis.net/fes/2.0}Temporal_CapabilitiesType with content type ELEMENT_ONLY
class Temporal_CapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}Temporal_CapabilitiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Temporal_CapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 208, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}TemporalOperands uses Python identifier TemporalOperands
    __TemporalOperands = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperands'), 'TemporalOperands', '__httpwww_opengis_netfes2_0_Temporal_CapabilitiesType_httpwww_opengis_netfes2_0TemporalOperands', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 210, 9), )

    
    TemporalOperands = property(__TemporalOperands.value, __TemporalOperands.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}TemporalOperators uses Python identifier TemporalOperators
    __TemporalOperators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperators'), 'TemporalOperators', '__httpwww_opengis_netfes2_0_Temporal_CapabilitiesType_httpwww_opengis_netfes2_0TemporalOperators', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 212, 9), )

    
    TemporalOperators = property(__TemporalOperators.value, __TemporalOperators.set, None, None)

    _ElementMap.update({
        __TemporalOperands.name() : __TemporalOperands,
        __TemporalOperators.name() : __TemporalOperators
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Temporal_CapabilitiesType = Temporal_CapabilitiesType
Namespace.addCategoryObject('typeBinding', 'Temporal_CapabilitiesType', Temporal_CapabilitiesType)


# Complex type {http://www.opengis.net/fes/2.0}TemporalOperandsType with content type ELEMENT_ONLY
class TemporalOperandsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}TemporalOperandsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TemporalOperandsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 216, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}TemporalOperand uses Python identifier TemporalOperand
    __TemporalOperand = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperand'), 'TemporalOperand', '__httpwww_opengis_netfes2_0_TemporalOperandsType_httpwww_opengis_netfes2_0TemporalOperand', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 218, 9), )

    
    TemporalOperand = property(__TemporalOperand.value, __TemporalOperand.set, None, None)

    _ElementMap.update({
        __TemporalOperand.name() : __TemporalOperand
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TemporalOperandsType = TemporalOperandsType
Namespace.addCategoryObject('typeBinding', 'TemporalOperandsType', TemporalOperandsType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 219, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netfes2_0_CTD_ANON_3_name', pyxb.binding.datatypes.QName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 220, 15)
    __name._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 220, 15)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type {http://www.opengis.net/fes/2.0}TemporalOperatorsType with content type ELEMENT_ONLY
class TemporalOperatorsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}TemporalOperatorsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TemporalOperatorsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 225, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}TemporalOperator uses Python identifier TemporalOperator
    __TemporalOperator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperator'), 'TemporalOperator', '__httpwww_opengis_netfes2_0_TemporalOperatorsType_httpwww_opengis_netfes2_0TemporalOperator', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 227, 9), )

    
    TemporalOperator = property(__TemporalOperator.value, __TemporalOperator.set, None, None)

    _ElementMap.update({
        __TemporalOperator.name() : __TemporalOperator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TemporalOperatorsType = TemporalOperatorsType
Namespace.addCategoryObject('typeBinding', 'TemporalOperatorsType', TemporalOperatorsType)


# Complex type {http://www.opengis.net/fes/2.0}Extended_CapabilitiesType with content type ELEMENT_ONLY
class Extended_CapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}Extended_CapabilitiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Extended_CapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 269, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}AdditionalOperators uses Python identifier AdditionalOperators
    __AdditionalOperators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdditionalOperators'), 'AdditionalOperators', '__httpwww_opengis_netfes2_0_Extended_CapabilitiesType_httpwww_opengis_netfes2_0AdditionalOperators', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 271, 9), )

    
    AdditionalOperators = property(__AdditionalOperators.value, __AdditionalOperators.set, None, None)

    _ElementMap.update({
        __AdditionalOperators.name() : __AdditionalOperators
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Extended_CapabilitiesType = Extended_CapabilitiesType
Namespace.addCategoryObject('typeBinding', 'Extended_CapabilitiesType', Extended_CapabilitiesType)


# Complex type {http://www.opengis.net/fes/2.0}AdditionalOperatorsType with content type ELEMENT_ONLY
class AdditionalOperatorsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}AdditionalOperatorsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdditionalOperatorsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 275, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}Operator uses Python identifier Operator
    __Operator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Operator'), 'Operator', '__httpwww_opengis_netfes2_0_AdditionalOperatorsType_httpwww_opengis_netfes2_0Operator', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 277, 9), )

    
    Operator = property(__Operator.value, __Operator.set, None, None)

    _ElementMap.update({
        __Operator.name() : __Operator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AdditionalOperatorsType = AdditionalOperatorsType
Namespace.addCategoryObject('typeBinding', 'AdditionalOperatorsType', AdditionalOperatorsType)


# Complex type {http://www.opengis.net/fes/2.0}ExtensionOperatorType with content type EMPTY
class ExtensionOperatorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}ExtensionOperatorType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExtensionOperatorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 282, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netfes2_0_ExtensionOperatorType_name', pyxb.binding.datatypes.QName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 283, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 283, 6)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.ExtensionOperatorType = ExtensionOperatorType
Namespace.addCategoryObject('typeBinding', 'ExtensionOperatorType', ExtensionOperatorType)


# Complex type {http://www.opengis.net/fes/2.0}AbstractQueryExpressionType with content type EMPTY
class AbstractQueryExpressionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}AbstractQueryExpressionType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractQueryExpressionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 21, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute handle uses Python identifier handle
    __handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'handle'), 'handle', '__httpwww_opengis_netfes2_0_AbstractQueryExpressionType_handle', pyxb.binding.datatypes.string)
    __handle._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 22, 6)
    __handle._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 22, 6)
    
    handle = property(__handle.value, __handle.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __handle.name() : __handle
    })
_module_typeBindings.AbstractQueryExpressionType = AbstractQueryExpressionType
Namespace.addCategoryObject('typeBinding', 'AbstractQueryExpressionType', AbstractQueryExpressionType)


# Complex type {http://www.opengis.net/fes/2.0}AbstractProjectionClauseType with content type EMPTY
class AbstractProjectionClauseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}AbstractProjectionClauseType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractProjectionClauseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 62, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractProjectionClauseType = AbstractProjectionClauseType
Namespace.addCategoryObject('typeBinding', 'AbstractProjectionClauseType', AbstractProjectionClauseType)


# Complex type {http://www.opengis.net/fes/2.0}AbstractSelectionClauseType with content type EMPTY
class AbstractSelectionClauseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}AbstractSelectionClauseType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractSelectionClauseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 65, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractSelectionClauseType = AbstractSelectionClauseType
Namespace.addCategoryObject('typeBinding', 'AbstractSelectionClauseType', AbstractSelectionClauseType)


# Complex type {http://www.opengis.net/fes/2.0}AbstractSortingClauseType with content type EMPTY
class AbstractSortingClauseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}AbstractSortingClauseType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractSortingClauseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 68, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractSortingClauseType = AbstractSortingClauseType
Namespace.addCategoryObject('typeBinding', 'AbstractSortingClauseType', AbstractSortingClauseType)


# Complex type {http://www.opengis.net/fes/2.0}SortByType with content type ELEMENT_ONLY
class SortByType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}SortByType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SortByType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/sort.xsd', 31, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}SortProperty uses Python identifier SortProperty
    __SortProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SortProperty'), 'SortProperty', '__httpwww_opengis_netfes2_0_SortByType_httpwww_opengis_netfes2_0SortProperty', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/sort.xsd', 33, 9), )

    
    SortProperty = property(__SortProperty.value, __SortProperty.set, None, None)

    _ElementMap.update({
        __SortProperty.name() : __SortProperty
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SortByType = SortByType
Namespace.addCategoryObject('typeBinding', 'SortByType', SortByType)


# Complex type {http://www.opengis.net/fes/2.0}SortPropertyType with content type ELEMENT_ONLY
class SortPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}SortPropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SortPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/sort.xsd', 37, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}ValueReference uses Python identifier ValueReference
    __ValueReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValueReference'), 'ValueReference', '__httpwww_opengis_netfes2_0_SortPropertyType_httpwww_opengis_netfes2_0ValueReference', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 21, 3), )

    
    ValueReference = property(__ValueReference.value, __ValueReference.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}SortOrder uses Python identifier SortOrder
    __SortOrder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SortOrder'), 'SortOrder', '__httpwww_opengis_netfes2_0_SortPropertyType_httpwww_opengis_netfes2_0SortOrder', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/sort.xsd', 40, 9), )

    
    SortOrder = property(__SortOrder.value, __SortOrder.set, None, None)

    _ElementMap.update({
        __ValueReference.name() : __ValueReference,
        __SortOrder.name() : __SortOrder
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SortPropertyType = SortPropertyType
Namespace.addCategoryObject('typeBinding', 'SortPropertyType', SortPropertyType)


# Complex type {http://www.opengis.net/fes/2.0}FilterType with content type ELEMENT_ONLY
class FilterType (AbstractSelectionClauseType):
    """Complex type {http://www.opengis.net/fes/2.0}FilterType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FilterType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 25, 3)
    _ElementMap = AbstractSelectionClauseType._ElementMap.copy()
    _AttributeMap = AbstractSelectionClauseType._AttributeMap.copy()
    # Base type is AbstractSelectionClauseType
    
    # Element {http://www.opengis.net/fes/2.0}Function uses Python identifier Function
    __Function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Function'), 'Function', '__httpwww_opengis_netfes2_0_FilterType_httpwww_opengis_netfes2_0Function', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 24, 3), )

    
    Function = property(__Function.value, __Function.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}comparisonOps uses Python identifier comparisonOps
    __comparisonOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps'), 'comparisonOps', '__httpwww_opengis_netfes2_0_FilterType_httpwww_opengis_netfes2_0comparisonOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 53, 3), )

    
    comparisonOps = property(__comparisonOps.value, __comparisonOps.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}spatialOps uses Python identifier spatialOps
    __spatialOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'spatialOps'), 'spatialOps', '__httpwww_opengis_netfes2_0_FilterType_httpwww_opengis_netfes2_0spatialOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 91, 3), )

    
    spatialOps = property(__spatialOps.value, __spatialOps.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}temporalOps uses Python identifier temporalOps
    __temporalOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'temporalOps'), 'temporalOps', '__httpwww_opengis_netfes2_0_FilterType_httpwww_opengis_netfes2_0temporalOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 130, 3), )

    
    temporalOps = property(__temporalOps.value, __temporalOps.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}logicOps uses Python identifier logicOps
    __logicOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'logicOps'), 'logicOps', '__httpwww_opengis_netfes2_0_FilterType_httpwww_opengis_netfes2_0logicOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 178, 3), )

    
    logicOps = property(__logicOps.value, __logicOps.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}extensionOps uses Python identifier extensionOps
    __extensionOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensionOps'), 'extensionOps', '__httpwww_opengis_netfes2_0_FilterType_httpwww_opengis_netfes2_0extensionOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 193, 3), )

    
    extensionOps = property(__extensionOps.value, __extensionOps.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}_Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_Id'), 'Id', '__httpwww_opengis_netfes2_0_FilterType_httpwww_opengis_netfes2_0_Id', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 201, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __Function.name() : __Function,
        __comparisonOps.name() : __comparisonOps,
        __spatialOps.name() : __spatialOps,
        __temporalOps.name() : __temporalOps,
        __logicOps.name() : __logicOps,
        __extensionOps.name() : __extensionOps,
        __Id.name() : __Id
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FilterType = FilterType
Namespace.addCategoryObject('typeBinding', 'FilterType', FilterType)


# Complex type {http://www.opengis.net/fes/2.0}BinaryComparisonOpType with content type ELEMENT_ONLY
class BinaryComparisonOpType (ComparisonOpsType):
    """Complex type {http://www.opengis.net/fes/2.0}BinaryComparisonOpType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BinaryComparisonOpType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 240, 3)
    _ElementMap = ComparisonOpsType._ElementMap.copy()
    _AttributeMap = ComparisonOpsType._AttributeMap.copy()
    # Base type is ComparisonOpsType
    
    # Element {http://www.opengis.net/fes/2.0}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netfes2_0_BinaryComparisonOpType_httpwww_opengis_netfes2_0expression', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    
    # Attribute matchCase uses Python identifier matchCase
    __matchCase = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'matchCase'), 'matchCase', '__httpwww_opengis_netfes2_0_BinaryComparisonOpType_matchCase', pyxb.binding.datatypes.boolean, unicode_default='true')
    __matchCase._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 246, 12)
    __matchCase._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 246, 12)
    
    matchCase = property(__matchCase.value, __matchCase.set, None, None)

    
    # Attribute matchAction uses Python identifier matchAction
    __matchAction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'matchAction'), 'matchAction', '__httpwww_opengis_netfes2_0_BinaryComparisonOpType_matchAction', _module_typeBindings.MatchActionType, unicode_default='Any')
    __matchAction._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 248, 12)
    __matchAction._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 248, 12)
    
    matchAction = property(__matchAction.value, __matchAction.set, None, None)

    _ElementMap.update({
        __expression.name() : __expression
    })
    _AttributeMap.update({
        __matchCase.name() : __matchCase,
        __matchAction.name() : __matchAction
    })
_module_typeBindings.BinaryComparisonOpType = BinaryComparisonOpType
Namespace.addCategoryObject('typeBinding', 'BinaryComparisonOpType', BinaryComparisonOpType)


# Complex type {http://www.opengis.net/fes/2.0}PropertyIsLikeType with content type ELEMENT_ONLY
class PropertyIsLikeType (ComparisonOpsType):
    """Complex type {http://www.opengis.net/fes/2.0}PropertyIsLikeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PropertyIsLikeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 260, 3)
    _ElementMap = ComparisonOpsType._ElementMap.copy()
    _AttributeMap = ComparisonOpsType._AttributeMap.copy()
    # Base type is ComparisonOpsType
    
    # Element {http://www.opengis.net/fes/2.0}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netfes2_0_PropertyIsLikeType_httpwww_opengis_netfes2_0expression', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    
    # Attribute wildCard uses Python identifier wildCard
    __wildCard = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wildCard'), 'wildCard', '__httpwww_opengis_netfes2_0_PropertyIsLikeType_wildCard', pyxb.binding.datatypes.string, required=True)
    __wildCard._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 266, 12)
    __wildCard._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 266, 12)
    
    wildCard = property(__wildCard.value, __wildCard.set, None, None)

    
    # Attribute singleChar uses Python identifier singleChar
    __singleChar = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'singleChar'), 'singleChar', '__httpwww_opengis_netfes2_0_PropertyIsLikeType_singleChar', pyxb.binding.datatypes.string, required=True)
    __singleChar._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 267, 12)
    __singleChar._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 267, 12)
    
    singleChar = property(__singleChar.value, __singleChar.set, None, None)

    
    # Attribute escapeChar uses Python identifier escapeChar
    __escapeChar = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'escapeChar'), 'escapeChar', '__httpwww_opengis_netfes2_0_PropertyIsLikeType_escapeChar', pyxb.binding.datatypes.string, required=True)
    __escapeChar._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 268, 12)
    __escapeChar._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 268, 12)
    
    escapeChar = property(__escapeChar.value, __escapeChar.set, None, None)

    
    # Attribute matchCase uses Python identifier matchCase
    __matchCase = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'matchCase'), 'matchCase', '__httpwww_opengis_netfes2_0_PropertyIsLikeType_matchCase', pyxb.binding.datatypes.boolean, unicode_default='true')
    __matchCase._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 269, 12)
    __matchCase._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 269, 12)
    
    matchCase = property(__matchCase.value, __matchCase.set, None, None)

    _ElementMap.update({
        __expression.name() : __expression
    })
    _AttributeMap.update({
        __wildCard.name() : __wildCard,
        __singleChar.name() : __singleChar,
        __escapeChar.name() : __escapeChar,
        __matchCase.name() : __matchCase
    })
_module_typeBindings.PropertyIsLikeType = PropertyIsLikeType
Namespace.addCategoryObject('typeBinding', 'PropertyIsLikeType', PropertyIsLikeType)


# Complex type {http://www.opengis.net/fes/2.0}PropertyIsNullType with content type ELEMENT_ONLY
class PropertyIsNullType (ComparisonOpsType):
    """Complex type {http://www.opengis.net/fes/2.0}PropertyIsNullType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PropertyIsNullType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 273, 3)
    _ElementMap = ComparisonOpsType._ElementMap.copy()
    _AttributeMap = ComparisonOpsType._AttributeMap.copy()
    # Base type is ComparisonOpsType
    
    # Element {http://www.opengis.net/fes/2.0}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netfes2_0_PropertyIsNullType_httpwww_opengis_netfes2_0expression', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    _ElementMap.update({
        __expression.name() : __expression
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PropertyIsNullType = PropertyIsNullType
Namespace.addCategoryObject('typeBinding', 'PropertyIsNullType', PropertyIsNullType)


# Complex type {http://www.opengis.net/fes/2.0}PropertyIsNilType with content type ELEMENT_ONLY
class PropertyIsNilType (ComparisonOpsType):
    """Complex type {http://www.opengis.net/fes/2.0}PropertyIsNilType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PropertyIsNilType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 282, 3)
    _ElementMap = ComparisonOpsType._ElementMap.copy()
    _AttributeMap = ComparisonOpsType._AttributeMap.copy()
    # Base type is ComparisonOpsType
    
    # Element {http://www.opengis.net/fes/2.0}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netfes2_0_PropertyIsNilType_httpwww_opengis_netfes2_0expression', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    
    # Attribute nilReason uses Python identifier nilReason
    __nilReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nilReason'), 'nilReason', '__httpwww_opengis_netfes2_0_PropertyIsNilType_nilReason', pyxb.binding.datatypes.string)
    __nilReason._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 288, 12)
    __nilReason._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 288, 12)
    
    nilReason = property(__nilReason.value, __nilReason.set, None, None)

    _ElementMap.update({
        __expression.name() : __expression
    })
    _AttributeMap.update({
        __nilReason.name() : __nilReason
    })
_module_typeBindings.PropertyIsNilType = PropertyIsNilType
Namespace.addCategoryObject('typeBinding', 'PropertyIsNilType', PropertyIsNilType)


# Complex type {http://www.opengis.net/fes/2.0}PropertyIsBetweenType with content type ELEMENT_ONLY
class PropertyIsBetweenType (ComparisonOpsType):
    """Complex type {http://www.opengis.net/fes/2.0}PropertyIsBetweenType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PropertyIsBetweenType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 292, 3)
    _ElementMap = ComparisonOpsType._ElementMap.copy()
    _AttributeMap = ComparisonOpsType._AttributeMap.copy()
    # Base type is ComparisonOpsType
    
    # Element {http://www.opengis.net/fes/2.0}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netfes2_0_PropertyIsBetweenType_httpwww_opengis_netfes2_0expression', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}LowerBoundary uses Python identifier LowerBoundary
    __LowerBoundary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LowerBoundary'), 'LowerBoundary', '__httpwww_opengis_netfes2_0_PropertyIsBetweenType_httpwww_opengis_netfes2_0LowerBoundary', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 297, 15), )

    
    LowerBoundary = property(__LowerBoundary.value, __LowerBoundary.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}UpperBoundary uses Python identifier UpperBoundary
    __UpperBoundary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UpperBoundary'), 'UpperBoundary', '__httpwww_opengis_netfes2_0_PropertyIsBetweenType_httpwww_opengis_netfes2_0UpperBoundary', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 298, 15), )

    
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


# Complex type {http://www.opengis.net/fes/2.0}BinarySpatialOpType with content type ELEMENT_ONLY
class BinarySpatialOpType (SpatialOpsType):
    """Complex type {http://www.opengis.net/fes/2.0}BinarySpatialOpType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BinarySpatialOpType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 313, 3)
    _ElementMap = SpatialOpsType._ElementMap.copy()
    _AttributeMap = SpatialOpsType._AttributeMap.copy()
    # Base type is SpatialOpsType
    
    # Element {http://www.opengis.net/fes/2.0}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netfes2_0_BinarySpatialOpType_httpwww_opengis_netfes2_0expression', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __expression.name() : __expression
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BinarySpatialOpType = BinarySpatialOpType
Namespace.addCategoryObject('typeBinding', 'BinarySpatialOpType', BinarySpatialOpType)


# Complex type {http://www.opengis.net/fes/2.0}BinaryTemporalOpType with content type ELEMENT_ONLY
class BinaryTemporalOpType (TemporalOpsType):
    """Complex type {http://www.opengis.net/fes/2.0}BinaryTemporalOpType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BinaryTemporalOpType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 323, 3)
    _ElementMap = TemporalOpsType._ElementMap.copy()
    _AttributeMap = TemporalOpsType._AttributeMap.copy()
    # Base type is TemporalOpsType
    
    # Element {http://www.opengis.net/fes/2.0}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netfes2_0_BinaryTemporalOpType_httpwww_opengis_netfes2_0expression', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __expression.name() : __expression
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BinaryTemporalOpType = BinaryTemporalOpType
Namespace.addCategoryObject('typeBinding', 'BinaryTemporalOpType', BinaryTemporalOpType)


# Complex type {http://www.opengis.net/fes/2.0}BBOXType with content type ELEMENT_ONLY
class BBOXType (SpatialOpsType):
    """Complex type {http://www.opengis.net/fes/2.0}BBOXType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BBOXType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 333, 3)
    _ElementMap = SpatialOpsType._ElementMap.copy()
    _AttributeMap = SpatialOpsType._AttributeMap.copy()
    # Base type is SpatialOpsType
    
    # Element {http://www.opengis.net/fes/2.0}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netfes2_0_BBOXType_httpwww_opengis_netfes2_0expression', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __expression.name() : __expression
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BBOXType = BBOXType
Namespace.addCategoryObject('typeBinding', 'BBOXType', BBOXType)


# Complex type {http://www.opengis.net/fes/2.0}DistanceBufferType with content type ELEMENT_ONLY
class DistanceBufferType (SpatialOpsType):
    """Complex type {http://www.opengis.net/fes/2.0}DistanceBufferType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DistanceBufferType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 343, 3)
    _ElementMap = SpatialOpsType._ElementMap.copy()
    _AttributeMap = SpatialOpsType._AttributeMap.copy()
    # Base type is SpatialOpsType
    
    # Element {http://www.opengis.net/fes/2.0}expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expression'), 'expression', '__httpwww_opengis_netfes2_0_DistanceBufferType_httpwww_opengis_netfes2_0expression', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3), )

    
    expression = property(__expression.value, __expression.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}Distance uses Python identifier Distance
    __Distance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Distance'), 'Distance', '__httpwww_opengis_netfes2_0_DistanceBufferType_httpwww_opengis_netfes2_0Distance', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 351, 15), )

    
    Distance = property(__Distance.value, __Distance.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __expression.name() : __expression,
        __Distance.name() : __Distance
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DistanceBufferType = DistanceBufferType
Namespace.addCategoryObject('typeBinding', 'DistanceBufferType', DistanceBufferType)


# Complex type {http://www.opengis.net/fes/2.0}BinaryLogicOpType with content type ELEMENT_ONLY
class BinaryLogicOpType (LogicOpsType):
    """Complex type {http://www.opengis.net/fes/2.0}BinaryLogicOpType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BinaryLogicOpType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 356, 3)
    _ElementMap = LogicOpsType._ElementMap.copy()
    _AttributeMap = LogicOpsType._AttributeMap.copy()
    # Base type is LogicOpsType
    
    # Element {http://www.opengis.net/fes/2.0}Function uses Python identifier Function
    __Function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Function'), 'Function', '__httpwww_opengis_netfes2_0_BinaryLogicOpType_httpwww_opengis_netfes2_0Function', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 24, 3), )

    
    Function = property(__Function.value, __Function.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}comparisonOps uses Python identifier comparisonOps
    __comparisonOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps'), 'comparisonOps', '__httpwww_opengis_netfes2_0_BinaryLogicOpType_httpwww_opengis_netfes2_0comparisonOps', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 53, 3), )

    
    comparisonOps = property(__comparisonOps.value, __comparisonOps.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}spatialOps uses Python identifier spatialOps
    __spatialOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'spatialOps'), 'spatialOps', '__httpwww_opengis_netfes2_0_BinaryLogicOpType_httpwww_opengis_netfes2_0spatialOps', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 91, 3), )

    
    spatialOps = property(__spatialOps.value, __spatialOps.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}temporalOps uses Python identifier temporalOps
    __temporalOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'temporalOps'), 'temporalOps', '__httpwww_opengis_netfes2_0_BinaryLogicOpType_httpwww_opengis_netfes2_0temporalOps', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 130, 3), )

    
    temporalOps = property(__temporalOps.value, __temporalOps.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}logicOps uses Python identifier logicOps
    __logicOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'logicOps'), 'logicOps', '__httpwww_opengis_netfes2_0_BinaryLogicOpType_httpwww_opengis_netfes2_0logicOps', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 178, 3), )

    
    logicOps = property(__logicOps.value, __logicOps.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}extensionOps uses Python identifier extensionOps
    __extensionOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensionOps'), 'extensionOps', '__httpwww_opengis_netfes2_0_BinaryLogicOpType_httpwww_opengis_netfes2_0extensionOps', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 193, 3), )

    
    extensionOps = property(__extensionOps.value, __extensionOps.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}_Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_Id'), 'Id', '__httpwww_opengis_netfes2_0_BinaryLogicOpType_httpwww_opengis_netfes2_0_Id', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 201, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __Function.name() : __Function,
        __comparisonOps.name() : __comparisonOps,
        __spatialOps.name() : __spatialOps,
        __temporalOps.name() : __temporalOps,
        __logicOps.name() : __logicOps,
        __extensionOps.name() : __extensionOps,
        __Id.name() : __Id
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BinaryLogicOpType = BinaryLogicOpType
Namespace.addCategoryObject('typeBinding', 'BinaryLogicOpType', BinaryLogicOpType)


# Complex type {http://www.opengis.net/fes/2.0}UnaryLogicOpType with content type ELEMENT_ONLY
class UnaryLogicOpType (LogicOpsType):
    """Complex type {http://www.opengis.net/fes/2.0}UnaryLogicOpType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnaryLogicOpType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 365, 3)
    _ElementMap = LogicOpsType._ElementMap.copy()
    _AttributeMap = LogicOpsType._AttributeMap.copy()
    # Base type is LogicOpsType
    
    # Element {http://www.opengis.net/fes/2.0}Function uses Python identifier Function
    __Function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Function'), 'Function', '__httpwww_opengis_netfes2_0_UnaryLogicOpType_httpwww_opengis_netfes2_0Function', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 24, 3), )

    
    Function = property(__Function.value, __Function.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}comparisonOps uses Python identifier comparisonOps
    __comparisonOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps'), 'comparisonOps', '__httpwww_opengis_netfes2_0_UnaryLogicOpType_httpwww_opengis_netfes2_0comparisonOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 53, 3), )

    
    comparisonOps = property(__comparisonOps.value, __comparisonOps.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}spatialOps uses Python identifier spatialOps
    __spatialOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'spatialOps'), 'spatialOps', '__httpwww_opengis_netfes2_0_UnaryLogicOpType_httpwww_opengis_netfes2_0spatialOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 91, 3), )

    
    spatialOps = property(__spatialOps.value, __spatialOps.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}temporalOps uses Python identifier temporalOps
    __temporalOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'temporalOps'), 'temporalOps', '__httpwww_opengis_netfes2_0_UnaryLogicOpType_httpwww_opengis_netfes2_0temporalOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 130, 3), )

    
    temporalOps = property(__temporalOps.value, __temporalOps.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}logicOps uses Python identifier logicOps
    __logicOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'logicOps'), 'logicOps', '__httpwww_opengis_netfes2_0_UnaryLogicOpType_httpwww_opengis_netfes2_0logicOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 178, 3), )

    
    logicOps = property(__logicOps.value, __logicOps.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}extensionOps uses Python identifier extensionOps
    __extensionOps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensionOps'), 'extensionOps', '__httpwww_opengis_netfes2_0_UnaryLogicOpType_httpwww_opengis_netfes2_0extensionOps', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 193, 3), )

    
    extensionOps = property(__extensionOps.value, __extensionOps.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}_Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_Id'), 'Id', '__httpwww_opengis_netfes2_0_UnaryLogicOpType_httpwww_opengis_netfes2_0_Id', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 201, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __Function.name() : __Function,
        __comparisonOps.name() : __comparisonOps,
        __spatialOps.name() : __spatialOps,
        __temporalOps.name() : __temporalOps,
        __logicOps.name() : __logicOps,
        __extensionOps.name() : __extensionOps,
        __Id.name() : __Id
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UnaryLogicOpType = UnaryLogicOpType
Namespace.addCategoryObject('typeBinding', 'UnaryLogicOpType', UnaryLogicOpType)


# Complex type {http://www.opengis.net/fes/2.0}ResourceIdType with content type EMPTY
class ResourceIdType (AbstractIdType):
    """Complex type {http://www.opengis.net/fes/2.0}ResourceIdType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 210, 3)
    _ElementMap = AbstractIdType._ElementMap.copy()
    _AttributeMap = AbstractIdType._AttributeMap.copy()
    # Base type is AbstractIdType
    
    # Attribute rid uses Python identifier rid
    __rid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rid'), 'rid', '__httpwww_opengis_netfes2_0_ResourceIdType_rid', pyxb.binding.datatypes.string, required=True)
    __rid._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 213, 12)
    __rid._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 213, 12)
    
    rid = property(__rid.value, __rid.set, None, None)

    
    # Attribute previousRid uses Python identifier previousRid
    __previousRid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'previousRid'), 'previousRid', '__httpwww_opengis_netfes2_0_ResourceIdType_previousRid', pyxb.binding.datatypes.string)
    __previousRid._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 214, 12)
    __previousRid._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 214, 12)
    
    previousRid = property(__previousRid.value, __previousRid.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netfes2_0_ResourceIdType_version', _module_typeBindings.VersionType)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 215, 12)
    __version._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 215, 12)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute startDate uses Python identifier startDate
    __startDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'startDate'), 'startDate', '__httpwww_opengis_netfes2_0_ResourceIdType_startDate', pyxb.binding.datatypes.dateTime)
    __startDate._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 216, 12)
    __startDate._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 216, 12)
    
    startDate = property(__startDate.value, __startDate.set, None, None)

    
    # Attribute endDate uses Python identifier endDate
    __endDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'endDate'), 'endDate', '__httpwww_opengis_netfes2_0_ResourceIdType_endDate', pyxb.binding.datatypes.dateTime)
    __endDate._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 217, 12)
    __endDate._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 217, 12)
    
    endDate = property(__endDate.value, __endDate.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rid.name() : __rid,
        __previousRid.name() : __previousRid,
        __version.name() : __version,
        __startDate.name() : __startDate,
        __endDate.name() : __endDate
    })
_module_typeBindings.ResourceIdType = ResourceIdType
Namespace.addCategoryObject('typeBinding', 'ResourceIdType', ResourceIdType)


# Complex type {http://www.opengis.net/fes/2.0}MeasureType with content type SIMPLE
class MeasureType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}MeasureType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasureType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 376, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.double
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_opengis_netfes2_0_MeasureType_uom', _module_typeBindings.UomIdentifier, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 379, 12)
    __uom._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 379, 12)
    
    uom = property(__uom.value, __uom.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom
    })
_module_typeBindings.MeasureType = MeasureType
Namespace.addCategoryObject('typeBinding', 'MeasureType', MeasureType)


# Complex type {http://www.opengis.net/fes/2.0}ComparisonOperatorType with content type EMPTY
class ComparisonOperatorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}ComparisonOperatorType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ComparisonOperatorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 93, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netfes2_0_ComparisonOperatorType_name', _module_typeBindings.ComparisonOperatorNameType, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 94, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 94, 6)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.ComparisonOperatorType = ComparisonOperatorType
Namespace.addCategoryObject('typeBinding', 'ComparisonOperatorType', ComparisonOperatorType)


# Complex type {http://www.opengis.net/fes/2.0}SpatialOperatorType with content type ELEMENT_ONLY
class SpatialOperatorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}SpatialOperatorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpatialOperatorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 174, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}GeometryOperands uses Python identifier GeometryOperands
    __GeometryOperands = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperands'), 'GeometryOperands', '__httpwww_opengis_netfes2_0_SpatialOperatorType_httpwww_opengis_netfes2_0GeometryOperands', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 176, 9), )

    
    GeometryOperands = property(__GeometryOperands.value, __GeometryOperands.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netfes2_0_SpatialOperatorType_name', _module_typeBindings.SpatialOperatorNameType)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 180, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 180, 6)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __GeometryOperands.name() : __GeometryOperands
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.SpatialOperatorType = SpatialOperatorType
Namespace.addCategoryObject('typeBinding', 'SpatialOperatorType', SpatialOperatorType)


# Complex type {http://www.opengis.net/fes/2.0}TemporalOperatorType with content type ELEMENT_ONLY
class TemporalOperatorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/fes/2.0}TemporalOperatorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TemporalOperatorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 232, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/fes/2.0}TemporalOperands uses Python identifier TemporalOperands
    __TemporalOperands = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperands'), 'TemporalOperands', '__httpwww_opengis_netfes2_0_TemporalOperatorType_httpwww_opengis_netfes2_0TemporalOperands', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 234, 9), )

    
    TemporalOperands = property(__TemporalOperands.value, __TemporalOperands.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netfes2_0_TemporalOperatorType_name', _module_typeBindings.TemporalOperatorNameType, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 238, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 238, 6)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __TemporalOperands.name() : __TemporalOperands
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.TemporalOperatorType = TemporalOperatorType
Namespace.addCategoryObject('typeBinding', 'TemporalOperatorType', TemporalOperatorType)


# Complex type {http://www.opengis.net/fes/2.0}AbstractAdhocQueryExpressionType with content type ELEMENT_ONLY
class AbstractAdhocQueryExpressionType (AbstractQueryExpressionType):
    """Complex type {http://www.opengis.net/fes/2.0}AbstractAdhocQueryExpressionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractAdhocQueryExpressionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 29, 3)
    _ElementMap = AbstractQueryExpressionType._ElementMap.copy()
    _AttributeMap = AbstractQueryExpressionType._AttributeMap.copy()
    # Base type is AbstractQueryExpressionType
    
    # Element {http://www.opengis.net/fes/2.0}AbstractProjectionClause uses Python identifier AbstractProjectionClause
    __AbstractProjectionClause = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AbstractProjectionClause'), 'AbstractProjectionClause', '__httpwww_opengis_netfes2_0_AbstractAdhocQueryExpressionType_httpwww_opengis_netfes2_0AbstractProjectionClause', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 61, 3), )

    
    AbstractProjectionClause = property(__AbstractProjectionClause.value, __AbstractProjectionClause.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}AbstractSelectionClause uses Python identifier AbstractSelectionClause
    __AbstractSelectionClause = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AbstractSelectionClause'), 'AbstractSelectionClause', '__httpwww_opengis_netfes2_0_AbstractAdhocQueryExpressionType_httpwww_opengis_netfes2_0AbstractSelectionClause', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 64, 3), )

    
    AbstractSelectionClause = property(__AbstractSelectionClause.value, __AbstractSelectionClause.set, None, None)

    
    # Element {http://www.opengis.net/fes/2.0}AbstractSortingClause uses Python identifier AbstractSortingClause
    __AbstractSortingClause = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AbstractSortingClause'), 'AbstractSortingClause', '__httpwww_opengis_netfes2_0_AbstractAdhocQueryExpressionType_httpwww_opengis_netfes2_0AbstractSortingClause', False, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 67, 3), )

    
    AbstractSortingClause = property(__AbstractSortingClause.value, __AbstractSortingClause.set, None, None)

    
    # Attribute handle inherited from {http://www.opengis.net/fes/2.0}AbstractQueryExpressionType
    
    # Attribute typeNames uses Python identifier typeNames
    __typeNames = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typeNames'), 'typeNames', '__httpwww_opengis_netfes2_0_AbstractAdhocQueryExpressionType_typeNames', _module_typeBindings.TypeNamesListType, required=True)
    __typeNames._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 38, 12)
    __typeNames._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 38, 12)
    
    typeNames = property(__typeNames.value, __typeNames.set, None, None)

    
    # Attribute aliases uses Python identifier aliases
    __aliases = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'aliases'), 'aliases', '__httpwww_opengis_netfes2_0_AbstractAdhocQueryExpressionType_aliases', _module_typeBindings.AliasesType)
    __aliases._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 40, 12)
    __aliases._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 40, 12)
    
    aliases = property(__aliases.value, __aliases.set, None, None)

    _ElementMap.update({
        __AbstractProjectionClause.name() : __AbstractProjectionClause,
        __AbstractSelectionClause.name() : __AbstractSelectionClause,
        __AbstractSortingClause.name() : __AbstractSortingClause
    })
    _AttributeMap.update({
        __typeNames.name() : __typeNames,
        __aliases.name() : __aliases
    })
_module_typeBindings.AbstractAdhocQueryExpressionType = AbstractAdhocQueryExpressionType
Namespace.addCategoryObject('typeBinding', 'AbstractAdhocQueryExpressionType', AbstractAdhocQueryExpressionType)


expression = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3))
Namespace.addCategoryObject('elementBinding', expression.name().localName(), expression)

ValueReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValueReference'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 21, 3))
Namespace.addCategoryObject('elementBinding', ValueReference.name().localName(), ValueReference)

AbstractProjectionClause = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractProjectionClause'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 61, 3))
Namespace.addCategoryObject('elementBinding', AbstractProjectionClause.name().localName(), AbstractProjectionClause)

AbstractSelectionClause = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractSelectionClause'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 64, 3))
Namespace.addCategoryObject('elementBinding', AbstractSelectionClause.name().localName(), AbstractSelectionClause)

AbstractSortingClause = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractSortingClause'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 67, 3))
Namespace.addCategoryObject('elementBinding', AbstractSortingClause.name().localName(), AbstractSortingClause)

Function = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Function'), FunctionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 24, 3))
Namespace.addCategoryObject('elementBinding', Function.name().localName(), Function)

Literal = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Literal'), LiteralType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 34, 3))
Namespace.addCategoryObject('elementBinding', Literal.name().localName(), Literal)

comparisonOps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps'), ComparisonOpsType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 53, 3))
Namespace.addCategoryObject('elementBinding', comparisonOps.name().localName(), comparisonOps)

spatialOps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'spatialOps'), SpatialOpsType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 91, 3))
Namespace.addCategoryObject('elementBinding', spatialOps.name().localName(), spatialOps)

temporalOps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'temporalOps'), TemporalOpsType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 130, 3))
Namespace.addCategoryObject('elementBinding', temporalOps.name().localName(), temporalOps)

logicOps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'logicOps'), LogicOpsType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 178, 3))
Namespace.addCategoryObject('elementBinding', logicOps.name().localName(), logicOps)

extensionOps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensionOps'), ExtensionOpsType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 193, 3))
Namespace.addCategoryObject('elementBinding', extensionOps.name().localName(), extensionOps)

Id = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_Id'), AbstractIdType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 201, 3))
Namespace.addCategoryObject('elementBinding', Id.name().localName(), Id)

Filter_Capabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Filter_Capabilities'), CTD_ANON, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 28, 3))
Namespace.addCategoryObject('elementBinding', Filter_Capabilities.name().localName(), Filter_Capabilities)

LogicalOperators = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LogicalOperators'), CTD_ANON_, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 84, 3))
Namespace.addCategoryObject('elementBinding', LogicalOperators.name().localName(), LogicalOperators)

AbstractQueryExpression = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractQueryExpression'), AbstractQueryExpressionType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 19, 3))
Namespace.addCategoryObject('elementBinding', AbstractQueryExpression.name().localName(), AbstractQueryExpression)

SortBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SortBy'), SortByType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/sort.xsd', 24, 3))
Namespace.addCategoryObject('elementBinding', SortBy.name().localName(), SortBy)

Filter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Filter'), FilterType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 22, 3))
Namespace.addCategoryObject('elementBinding', Filter.name().localName(), Filter)

PropertyIsEqualTo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsEqualTo'), BinaryComparisonOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 57, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsEqualTo.name().localName(), PropertyIsEqualTo)

PropertyIsNotEqualTo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsNotEqualTo'), BinaryComparisonOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 60, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsNotEqualTo.name().localName(), PropertyIsNotEqualTo)

PropertyIsLessThan = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsLessThan'), BinaryComparisonOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 63, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsLessThan.name().localName(), PropertyIsLessThan)

PropertyIsGreaterThan = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsGreaterThan'), BinaryComparisonOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 66, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsGreaterThan.name().localName(), PropertyIsGreaterThan)

PropertyIsLessThanOrEqualTo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsLessThanOrEqualTo'), BinaryComparisonOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 69, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsLessThanOrEqualTo.name().localName(), PropertyIsLessThanOrEqualTo)

PropertyIsGreaterThanOrEqualTo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsGreaterThanOrEqualTo'), BinaryComparisonOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 72, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsGreaterThanOrEqualTo.name().localName(), PropertyIsGreaterThanOrEqualTo)

PropertyIsLike = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsLike'), PropertyIsLikeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 75, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsLike.name().localName(), PropertyIsLike)

PropertyIsNull = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsNull'), PropertyIsNullType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 78, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsNull.name().localName(), PropertyIsNull)

PropertyIsNil = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsNil'), PropertyIsNilType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 81, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsNil.name().localName(), PropertyIsNil)

PropertyIsBetween = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyIsBetween'), PropertyIsBetweenType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 84, 3))
Namespace.addCategoryObject('elementBinding', PropertyIsBetween.name().localName(), PropertyIsBetween)

Equals = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Equals'), BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 93, 3))
Namespace.addCategoryObject('elementBinding', Equals.name().localName(), Equals)

Disjoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Disjoint'), BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 96, 3))
Namespace.addCategoryObject('elementBinding', Disjoint.name().localName(), Disjoint)

Touches = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Touches'), BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 99, 3))
Namespace.addCategoryObject('elementBinding', Touches.name().localName(), Touches)

Within = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Within'), BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 102, 3))
Namespace.addCategoryObject('elementBinding', Within.name().localName(), Within)

Overlaps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Overlaps'), BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 105, 3))
Namespace.addCategoryObject('elementBinding', Overlaps.name().localName(), Overlaps)

Crosses = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Crosses'), BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 108, 3))
Namespace.addCategoryObject('elementBinding', Crosses.name().localName(), Crosses)

Intersects = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Intersects'), BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 111, 3))
Namespace.addCategoryObject('elementBinding', Intersects.name().localName(), Intersects)

Contains = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contains'), BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 114, 3))
Namespace.addCategoryObject('elementBinding', Contains.name().localName(), Contains)

DWithin = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DWithin'), DistanceBufferType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 117, 3))
Namespace.addCategoryObject('elementBinding', DWithin.name().localName(), DWithin)

Beyond = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Beyond'), DistanceBufferType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 120, 3))
Namespace.addCategoryObject('elementBinding', Beyond.name().localName(), Beyond)

BBOX = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BBOX'), BBOXType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 123, 3))
Namespace.addCategoryObject('elementBinding', BBOX.name().localName(), BBOX)

After = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'After'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 132, 3))
Namespace.addCategoryObject('elementBinding', After.name().localName(), After)

Before = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Before'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 135, 3))
Namespace.addCategoryObject('elementBinding', Before.name().localName(), Before)

Begins = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Begins'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 138, 3))
Namespace.addCategoryObject('elementBinding', Begins.name().localName(), Begins)

BegunBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BegunBy'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 141, 3))
Namespace.addCategoryObject('elementBinding', BegunBy.name().localName(), BegunBy)

TContains = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TContains'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 144, 3))
Namespace.addCategoryObject('elementBinding', TContains.name().localName(), TContains)

During = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'During'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 147, 3))
Namespace.addCategoryObject('elementBinding', During.name().localName(), During)

EndedBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndedBy'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 150, 3))
Namespace.addCategoryObject('elementBinding', EndedBy.name().localName(), EndedBy)

Ends = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ends'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 153, 3))
Namespace.addCategoryObject('elementBinding', Ends.name().localName(), Ends)

TEquals = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TEquals'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 156, 3))
Namespace.addCategoryObject('elementBinding', TEquals.name().localName(), TEquals)

Meets = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Meets'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 159, 3))
Namespace.addCategoryObject('elementBinding', Meets.name().localName(), Meets)

MetBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MetBy'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 162, 3))
Namespace.addCategoryObject('elementBinding', MetBy.name().localName(), MetBy)

TOverlaps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TOverlaps'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 165, 3))
Namespace.addCategoryObject('elementBinding', TOverlaps.name().localName(), TOverlaps)

OverlappedBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OverlappedBy'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 168, 3))
Namespace.addCategoryObject('elementBinding', OverlappedBy.name().localName(), OverlappedBy)

AnyInteracts = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AnyInteracts'), BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 171, 3))
Namespace.addCategoryObject('elementBinding', AnyInteracts.name().localName(), AnyInteracts)

And = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'And'), BinaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 180, 3))
Namespace.addCategoryObject('elementBinding', And.name().localName(), And)

Or = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Or'), BinaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 183, 3))
Namespace.addCategoryObject('elementBinding', Or.name().localName(), Or)

Not = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Not'), UnaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 186, 3))
Namespace.addCategoryObject('elementBinding', Not.name().localName(), Not)

ResourceId = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResourceId'), ResourceIdType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 207, 3))
Namespace.addCategoryObject('elementBinding', ResourceId.name().localName(), ResourceId)

AbstractAdhocQueryExpression = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractAdhocQueryExpression'), AbstractAdhocQueryExpressionType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 25, 3))
Namespace.addCategoryObject('elementBinding', AbstractAdhocQueryExpression.name().localName(), AbstractAdhocQueryExpression)



FunctionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=FunctionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 28, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FunctionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 28, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FunctionType._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 38, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 38, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LiteralType._Automaton = _BuildAutomaton_()




LowerBoundaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=LowerBoundaryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LowerBoundaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 305, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LowerBoundaryType._Automaton = _BuildAutomaton_2()




UpperBoundaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=UpperBoundaryType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UpperBoundaryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 310, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UpperBoundaryType._Automaton = _BuildAutomaton_3()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Conformance'), ConformanceType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 31, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id_Capabilities'), Id_CapabilitiesType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 33, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Scalar_Capabilities'), Scalar_CapabilitiesType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 36, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Spatial_Capabilities'), Spatial_CapabilitiesType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 39, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Temporal_Capabilities'), Temporal_CapabilitiesType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 42, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Functions'), AvailableFunctionsType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 45, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extended_Capabilities'), Extended_CapabilitiesType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 47, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 33, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 36, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 39, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 42, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 45, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 47, 12))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Conformance')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 31, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id_Capabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 33, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Scalar_Capabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 36, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Spatial_Capabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 39, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Temporal_Capabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 42, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Functions')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 45, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extended_Capabilities')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 47, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_4()




ConformanceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), pyxb.bundles.opengis.ows_1_1.DomainType, scope=ConformanceType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 57, 9)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConformanceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Constraint')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 57, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ConformanceType._Automaton = _BuildAutomaton_5()




Id_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResourceIdentifier'), ResourceIdentifierType, scope=Id_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 65, 9)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Id_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResourceIdentifier')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 65, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Id_CapabilitiesType._Automaton = _BuildAutomaton_6()




ResourceIdentifierType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata'), pyxb.bundles.opengis.ows_1_1.MetadataType, scope=ResourceIdentifierType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 42, 1)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 71, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ResourceIdentifierType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 71, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ResourceIdentifierType._Automaton = _BuildAutomaton_7()




Scalar_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ComparisonOperators'), ComparisonOperatorsType, scope=Scalar_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 80, 9)))

Scalar_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LogicalOperators'), CTD_ANON_, scope=Scalar_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 84, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 79, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 80, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Scalar_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LogicalOperators')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 79, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Scalar_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ComparisonOperators')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 80, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Scalar_CapabilitiesType._Automaton = _BuildAutomaton_8()




ComparisonOperatorsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ComparisonOperator'), ComparisonOperatorType, scope=ComparisonOperatorsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 89, 9)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ComparisonOperatorsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ComparisonOperator')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 89, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ComparisonOperatorsType._Automaton = _BuildAutomaton_9()




AvailableFunctionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Function'), AvailableFunctionType, scope=AvailableFunctionsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 122, 9)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AvailableFunctionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Function')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 122, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AvailableFunctionsType._Automaton = _BuildAutomaton_10()




AvailableFunctionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Returns'), pyxb.binding.datatypes.QName, scope=AvailableFunctionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 129, 9)))

AvailableFunctionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Arguments'), ArgumentsType, scope=AvailableFunctionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 130, 9)))

AvailableFunctionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata'), pyxb.bundles.opengis.ows_1_1.MetadataType, scope=AvailableFunctionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 42, 1)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 128, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 130, 9))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AvailableFunctionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 128, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AvailableFunctionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Returns')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 129, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AvailableFunctionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Arguments')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 130, 9))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AvailableFunctionType._Automaton = _BuildAutomaton_11()




ArgumentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Argument'), ArgumentType, scope=ArgumentsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 137, 9)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ArgumentsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Argument')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 137, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ArgumentsType._Automaton = _BuildAutomaton_12()




ArgumentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Type'), pyxb.binding.datatypes.QName, scope=ArgumentType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 144, 9)))

ArgumentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata'), pyxb.bundles.opengis.ows_1_1.MetadataType, scope=ArgumentType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/ows/1.1.0/owsCommon.xsd', 42, 1)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 143, 9))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ArgumentType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 143, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ArgumentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Type')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 144, 9))
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
ArgumentType._Automaton = _BuildAutomaton_13()




Spatial_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperands'), GeometryOperandsType, scope=Spatial_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 152, 9)))

Spatial_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SpatialOperators'), SpatialOperatorsType, scope=Spatial_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 154, 9)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Spatial_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperands')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 152, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Spatial_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SpatialOperators')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 154, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Spatial_CapabilitiesType._Automaton = _BuildAutomaton_14()




GeometryOperandsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperand'), CTD_ANON_2, scope=GeometryOperandsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 160, 9)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeometryOperandsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperand')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 160, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GeometryOperandsType._Automaton = _BuildAutomaton_15()




SpatialOperatorsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SpatialOperator'), SpatialOperatorType, scope=SpatialOperatorsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 169, 9)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SpatialOperatorsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SpatialOperator')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 169, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SpatialOperatorsType._Automaton = _BuildAutomaton_16()




Temporal_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperands'), TemporalOperandsType, scope=Temporal_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 210, 9)))

Temporal_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperators'), TemporalOperatorsType, scope=Temporal_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 212, 9)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Temporal_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperands')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 210, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Temporal_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperators')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 212, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Temporal_CapabilitiesType._Automaton = _BuildAutomaton_17()




TemporalOperandsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperand'), CTD_ANON_3, scope=TemporalOperandsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 218, 9)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TemporalOperandsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperand')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 218, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TemporalOperandsType._Automaton = _BuildAutomaton_18()




TemporalOperatorsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperator'), TemporalOperatorType, scope=TemporalOperatorsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 227, 9)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TemporalOperatorsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperator')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 227, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TemporalOperatorsType._Automaton = _BuildAutomaton_19()




Extended_CapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdditionalOperators'), AdditionalOperatorsType, scope=Extended_CapabilitiesType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 271, 9)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 271, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Extended_CapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdditionalOperators')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 271, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Extended_CapabilitiesType._Automaton = _BuildAutomaton_20()




AdditionalOperatorsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Operator'), ExtensionOperatorType, scope=AdditionalOperatorsType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 277, 9)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 277, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AdditionalOperatorsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Operator')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 277, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AdditionalOperatorsType._Automaton = _BuildAutomaton_21()




SortByType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SortProperty'), SortPropertyType, scope=SortByType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/sort.xsd', 33, 9)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SortByType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SortProperty')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/sort.xsd', 33, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SortByType._Automaton = _BuildAutomaton_22()




SortPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValueReference'), pyxb.binding.datatypes.string, scope=SortPropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 21, 3)))

SortPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SortOrder'), SortOrderType, scope=SortPropertyType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/sort.xsd', 40, 9)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/sort.xsd', 40, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SortPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValueReference')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/sort.xsd', 39, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SortPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SortOrder')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/sort.xsd', 40, 9))
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
SortPropertyType._Automaton = _BuildAutomaton_23()




FilterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Function'), FunctionType, scope=FilterType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 24, 3)))

FilterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps'), ComparisonOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=FilterType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 53, 3)))

FilterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'spatialOps'), SpatialOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=FilterType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 91, 3)))

FilterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'temporalOps'), TemporalOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=FilterType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 130, 3)))

FilterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'logicOps'), LogicOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=FilterType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 178, 3)))

FilterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensionOps'), ExtensionOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=FilterType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 193, 3)))

FilterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_Id'), AbstractIdType, abstract=pyxb.binding.datatypes.boolean(1), scope=FilterType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 201, 3)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FilterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 40, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FilterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'spatialOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 41, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FilterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'temporalOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 42, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FilterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'logicOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 43, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FilterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 44, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FilterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Function')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 45, 9))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FilterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_Id')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 46, 9))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FilterType._Automaton = _BuildAutomaton_24()




BinaryComparisonOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=BinaryComparisonOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=2, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 244, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BinaryComparisonOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 244, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BinaryComparisonOpType._Automaton = _BuildAutomaton_25()




PropertyIsLikeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=PropertyIsLikeType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=2, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 264, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PropertyIsLikeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 264, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PropertyIsLikeType._Automaton = _BuildAutomaton_26()




PropertyIsNullType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=PropertyIsNullType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PropertyIsNullType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 277, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PropertyIsNullType._Automaton = _BuildAutomaton_27()




PropertyIsNilType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=PropertyIsNilType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PropertyIsNilType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 286, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PropertyIsNilType._Automaton = _BuildAutomaton_28()




PropertyIsBetweenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=PropertyIsBetweenType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3)))

PropertyIsBetweenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LowerBoundary'), LowerBoundaryType, scope=PropertyIsBetweenType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 297, 15)))

PropertyIsBetweenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UpperBoundary'), UpperBoundaryType, scope=PropertyIsBetweenType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 298, 15)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PropertyIsBetweenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 296, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PropertyIsBetweenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LowerBoundary')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 297, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PropertyIsBetweenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UpperBoundary')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 298, 15))
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
PropertyIsBetweenType._Automaton = _BuildAutomaton_29()




BinarySpatialOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=BinarySpatialOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=2, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 316, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BinarySpatialOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 317, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.opengis.net/fes/2.0')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 318, 15))
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
    return fac.Automaton(states, counters, False, containing_state=None)
BinarySpatialOpType._Automaton = _BuildAutomaton_30()




BinaryTemporalOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=BinaryTemporalOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=2, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 326, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BinaryTemporalOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 327, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.opengis.net/fes/2.0')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 328, 15))
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
    return fac.Automaton(states, counters, False, containing_state=None)
BinaryTemporalOpType._Automaton = _BuildAutomaton_31()




BBOXType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=BBOXType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=2, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 336, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BBOXType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 337, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.opengis.net/fes/2.0')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 338, 15))
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
    return fac.Automaton(states, counters, False, containing_state=None)
BBOXType._Automaton = _BuildAutomaton_32()




DistanceBufferType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expression'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=DistanceBufferType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 19, 3)))

DistanceBufferType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Distance'), MeasureType, scope=DistanceBufferType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 351, 15)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=2, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 347, 15))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DistanceBufferType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expression')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 348, 18))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.opengis.net/fes/2.0')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 349, 18))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DistanceBufferType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Distance')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 351, 15))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DistanceBufferType._Automaton = _BuildAutomaton_33()




BinaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Function'), FunctionType, scope=BinaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 24, 3)))

BinaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps'), ComparisonOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=BinaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 53, 3)))

BinaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'spatialOps'), SpatialOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=BinaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 91, 3)))

BinaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'temporalOps'), TemporalOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=BinaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 130, 3)))

BinaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'logicOps'), LogicOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=BinaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 178, 3)))

BinaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensionOps'), ExtensionOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=BinaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 193, 3)))

BinaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_Id'), AbstractIdType, abstract=pyxb.binding.datatypes.boolean(1), scope=BinaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 201, 3)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 359, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BinaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 40, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BinaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'spatialOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 41, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BinaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'temporalOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 42, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BinaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'logicOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 43, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BinaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 44, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BinaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Function')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 45, 9))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BinaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_Id')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 46, 9))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
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
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
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
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
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
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BinaryLogicOpType._Automaton = _BuildAutomaton_34()




UnaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Function'), FunctionType, scope=UnaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/expr.xsd', 24, 3)))

UnaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps'), ComparisonOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=UnaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 53, 3)))

UnaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'spatialOps'), SpatialOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=UnaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 91, 3)))

UnaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'temporalOps'), TemporalOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=UnaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 130, 3)))

UnaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'logicOps'), LogicOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=UnaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 178, 3)))

UnaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensionOps'), ExtensionOpsType, abstract=pyxb.binding.datatypes.boolean(1), scope=UnaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 193, 3)))

UnaryLogicOpType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_Id'), AbstractIdType, abstract=pyxb.binding.datatypes.boolean(1), scope=UnaryLogicOpType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 201, 3)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comparisonOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 40, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'spatialOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 41, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'temporalOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 42, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'logicOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 43, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionOps')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 44, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Function')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 45, 9))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnaryLogicOpType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_Id')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filter.xsd', 46, 9))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UnaryLogicOpType._Automaton = _BuildAutomaton_35()




SpatialOperatorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperands'), GeometryOperandsType, scope=SpatialOperatorType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 176, 9)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 176, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SpatialOperatorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeometryOperands')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 176, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SpatialOperatorType._Automaton = _BuildAutomaton_36()




TemporalOperatorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperands'), TemporalOperandsType, scope=TemporalOperatorType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 234, 9)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 234, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TemporalOperatorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemporalOperands')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/filterCapabilities.xsd', 234, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TemporalOperatorType._Automaton = _BuildAutomaton_37()




AbstractAdhocQueryExpressionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractProjectionClause'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=AbstractAdhocQueryExpressionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 61, 3)))

AbstractAdhocQueryExpressionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractSelectionClause'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=AbstractAdhocQueryExpressionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 64, 3)))

AbstractAdhocQueryExpressionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractSortingClause'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=AbstractAdhocQueryExpressionType, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 67, 3)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 33, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 35, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 36, 15))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AbstractAdhocQueryExpressionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AbstractProjectionClause')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 33, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AbstractAdhocQueryExpressionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AbstractSelectionClause')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 35, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AbstractAdhocQueryExpressionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AbstractSortingClause')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/filter/2.0/query.xsd', 36, 15))
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
AbstractAdhocQueryExpressionType._Automaton = _BuildAutomaton_38()


ValueReference._setSubstitutionGroup(expression)

Function._setSubstitutionGroup(expression)

Literal._setSubstitutionGroup(expression)

SortBy._setSubstitutionGroup(AbstractSortingClause)

Filter._setSubstitutionGroup(AbstractSelectionClause)

PropertyIsEqualTo._setSubstitutionGroup(comparisonOps)

PropertyIsNotEqualTo._setSubstitutionGroup(comparisonOps)

PropertyIsLessThan._setSubstitutionGroup(comparisonOps)

PropertyIsGreaterThan._setSubstitutionGroup(comparisonOps)

PropertyIsLessThanOrEqualTo._setSubstitutionGroup(comparisonOps)

PropertyIsGreaterThanOrEqualTo._setSubstitutionGroup(comparisonOps)

PropertyIsLike._setSubstitutionGroup(comparisonOps)

PropertyIsNull._setSubstitutionGroup(comparisonOps)

PropertyIsNil._setSubstitutionGroup(comparisonOps)

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

After._setSubstitutionGroup(temporalOps)

Before._setSubstitutionGroup(temporalOps)

Begins._setSubstitutionGroup(temporalOps)

BegunBy._setSubstitutionGroup(temporalOps)

TContains._setSubstitutionGroup(temporalOps)

During._setSubstitutionGroup(temporalOps)

EndedBy._setSubstitutionGroup(temporalOps)

Ends._setSubstitutionGroup(temporalOps)

TEquals._setSubstitutionGroup(temporalOps)

Meets._setSubstitutionGroup(temporalOps)

MetBy._setSubstitutionGroup(temporalOps)

TOverlaps._setSubstitutionGroup(temporalOps)

OverlappedBy._setSubstitutionGroup(temporalOps)

AnyInteracts._setSubstitutionGroup(temporalOps)

And._setSubstitutionGroup(logicOps)

Or._setSubstitutionGroup(logicOps)

Not._setSubstitutionGroup(logicOps)

ResourceId._setSubstitutionGroup(Id)

AbstractAdhocQueryExpression._setSubstitutionGroup(AbstractQueryExpression)
