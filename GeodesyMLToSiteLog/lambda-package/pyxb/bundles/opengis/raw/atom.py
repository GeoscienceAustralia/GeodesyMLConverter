# ./pyxb/bundles/opengis/raw/atom.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:741a4e51acfa398449878d8690bb692b0b09b93a
# Generated 2017-07-10 00:38:00.342474 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.w3.org/2005/Atom [xmlns:atom]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:064905e6-6508-11e7-aa9b-0a55f9edafa5')

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

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.w3.org/2005/Atom', create_if_missing=True)
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


# Atomic simple type: {http://www.w3.org/2005/Atom}atomMediaType
class atomMediaType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'atomMediaType')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 46, 2)
    _Documentation = None
atomMediaType._CF_pattern = pyxb.binding.facets.CF_pattern()
atomMediaType._CF_pattern.addPattern(pattern='.+/.+')
atomMediaType._InitializeFacetMap(atomMediaType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'atomMediaType', atomMediaType)
_module_typeBindings.atomMediaType = atomMediaType

# Atomic simple type: {http://www.w3.org/2005/Atom}atomLanguageTag
class atomLanguageTag (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'atomLanguageTag')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 53, 2)
    _Documentation = None
atomLanguageTag._CF_pattern = pyxb.binding.facets.CF_pattern()
atomLanguageTag._CF_pattern.addPattern(pattern='[A-Za-z]{1,8}(-[A-Za-z0-9]{1,8})*')
atomLanguageTag._InitializeFacetMap(atomLanguageTag._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'atomLanguageTag', atomLanguageTag)
_module_typeBindings.atomLanguageTag = atomLanguageTag

# Atomic simple type: {http://www.w3.org/2005/Atom}atomEmailAddress
class atomEmailAddress (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'atomEmailAddress')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 60, 2)
    _Documentation = None
atomEmailAddress._CF_pattern = pyxb.binding.facets.CF_pattern()
atomEmailAddress._CF_pattern.addPattern(pattern='.+@.+')
atomEmailAddress._InitializeFacetMap(atomEmailAddress._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'atomEmailAddress', atomEmailAddress)
_module_typeBindings.atomEmailAddress = atomEmailAddress

# Complex type {http://www.w3.org/2005/Atom}atomPersonConstruct with content type ELEMENT_ONLY
class atomPersonConstruct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2005/Atom}atomPersonConstruct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'atomPersonConstruct')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 15, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/Atom}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpwww_w3_org2005Atom_atomPersonConstruct_httpwww_w3_org2005Atomname', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 23, 2), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}uri uses Python identifier uri
    __uri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uri'), 'uri', '__httpwww_w3_org2005Atom_atomPersonConstruct_httpwww_w3_org2005Atomuri', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 24, 2), )

    
    uri = property(__uri.value, __uri.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'email'), 'email', '__httpwww_w3_org2005Atom_atomPersonConstruct_httpwww_w3_org2005Atomemail', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 25, 2), )

    
    email = property(__email.value, __email.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __uri.name() : __uri,
        __email.name() : __email
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.atomPersonConstruct = atomPersonConstruct
Namespace.addCategoryObject('typeBinding', 'atomPersonConstruct', atomPersonConstruct)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 32, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'href'), 'href', '__httpwww_w3_org2005Atom_CTD_ANON_href', pyxb.binding.datatypes.anySimpleType, required=True)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 34, 6)
    __href._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 34, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute rel uses Python identifier rel
    __rel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rel'), 'rel', '__httpwww_w3_org2005Atom_CTD_ANON_rel', pyxb.binding.datatypes.anySimpleType)
    __rel._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 35, 6)
    __rel._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 35, 6)
    
    rel = property(__rel.value, __rel.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_w3_org2005Atom_CTD_ANON_type', _module_typeBindings.atomMediaType)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 36, 6)
    __type._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 36, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute hreflang uses Python identifier hreflang
    __hreflang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'hreflang'), 'hreflang', '__httpwww_w3_org2005Atom_CTD_ANON_hreflang', _module_typeBindings.atomLanguageTag)
    __hreflang._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 37, 6)
    __hreflang._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 37, 6)
    
    hreflang = property(__hreflang.value, __hreflang.set, None, None)

    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__httpwww_w3_org2005Atom_CTD_ANON_title', pyxb.binding.datatypes.anySimpleType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 38, 6)
    __title._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 38, 6)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute length uses Python identifier length
    __length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'length'), 'length', '__httpwww_w3_org2005Atom_CTD_ANON_length', pyxb.binding.datatypes.anySimpleType)
    __length._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 39, 6)
    __length._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 39, 6)
    
    length = property(__length.value, __length.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __href.name() : __href,
        __rel.name() : __rel,
        __type.name() : __type,
        __hreflang.name() : __hreflang,
        __title.name() : __title,
        __length.name() : __length
    })
_module_typeBindings.CTD_ANON = CTD_ANON


name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 23, 2))
Namespace.addCategoryObject('elementBinding', name.name().localName(), name)

uri = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uri'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 24, 2))
Namespace.addCategoryObject('elementBinding', uri.name().localName(), uri)

email = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'email'), atomEmailAddress, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 25, 2))
Namespace.addCategoryObject('elementBinding', email.name().localName(), email)

author = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'author'), atomPersonConstruct, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 28, 2))
Namespace.addCategoryObject('elementBinding', author.name().localName(), author)

link = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'link'), CTD_ANON, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 31, 2))
Namespace.addCategoryObject('elementBinding', link.name().localName(), link)



atomPersonConstruct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=atomPersonConstruct, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 23, 2)))

atomPersonConstruct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uri'), pyxb.binding.datatypes.string, scope=atomPersonConstruct, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 24, 2)))

atomPersonConstruct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'email'), atomEmailAddress, scope=atomPersonConstruct, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 25, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 16, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(atomPersonConstruct._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 17, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(atomPersonConstruct._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uri')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 18, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(atomPersonConstruct._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'email')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/kml/2.2.0/atom-author-link.xsd', 19, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
atomPersonConstruct._Automaton = _BuildAutomaton()

