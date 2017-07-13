# ./pyxb/bundles/opengis/raw/csw_dc.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:fde543a00b9681daae05bbc5a17f3dce9cfacb0c
# Generated 2017-07-10 00:38:03.296911 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://purl.org/dc/elements/1.1/ [xmlns:dc]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:0787160a-6508-11e7-9767-0a55f9edafa5')

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
Namespace = pyxb.namespace.NamespaceForURI('http://purl.org/dc/elements/1.1/', create_if_missing=True)
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


# Complex type {http://purl.org/dc/elements/1.1/}SimpleLiteral with content type MIXED
class SimpleLiteral (pyxb.binding.basis.complexTypeDefinition):
    """This is the default type for all of the DC elements. It defines a 
      complexType SimpleLiteral which permits mixed content but disallows 
      child elements by use of minOcccurs/maxOccurs. However, this complexType 
      does permit the derivation of other types which would permit child 
      elements. The scheme attribute may be used as a qualifier to reference 
      an encoding scheme that describes the value domain for a given property."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleLiteral')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 11, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute scheme uses Python identifier scheme
    __scheme = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'scheme'), 'scheme', '__httppurl_orgdcelements1_1_SimpleLiteral_scheme', pyxb.binding.datatypes.anyURI)
    __scheme._DeclarationLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 25, 12)
    __scheme._UseLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 25, 12)
    
    scheme = property(__scheme.value, __scheme.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __scheme.name() : __scheme
    })
_module_typeBindings.SimpleLiteral = SimpleLiteral
Namespace.addCategoryObject('typeBinding', 'SimpleLiteral', SimpleLiteral)


# Complex type {http://purl.org/dc/elements/1.1/}elementContainer with content type ELEMENT_ONLY
class elementContainer (pyxb.binding.basis.complexTypeDefinition):
    """This type definition is included as a convenience for schema authors 
      who need a container element for all of the DC elements."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'elementContainer')
    _XSDLocation = pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 190, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://purl.org/dc/elements/1.1/}DC-element uses Python identifier DC_element
    __DC_element = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DC-element'), 'DC_element', '__httppurl_orgdcelements1_1_elementContainer_httppurl_orgdcelements1_1DC_element', True, pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 29, 3), )

    
    DC_element = property(__DC_element.value, __DC_element.set, None, None)

    _ElementMap.update({
        __DC_element.name() : __DC_element
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.elementContainer = elementContainer
Namespace.addCategoryObject('typeBinding', 'elementContainer', elementContainer)


DC_element = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC-element'), SimpleLiteral, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 29, 3))
Namespace.addCategoryObject('elementBinding', DC_element.name().localName(), DC_element)

title = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), SimpleLiteral, documentation='A name given to the resource. Typically, Title will be a name by \n      which the resource is formally known.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 30, 3))
Namespace.addCategoryObject('elementBinding', title.name().localName(), title)

creator = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'creator'), SimpleLiteral, documentation='An entity primarily responsible for making the content of the resource.\n      Examples of Creator include a person, an organization, or a service. \n      Typically, the name of a Creator should be used to indicate the entity.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 37, 3))
Namespace.addCategoryObject('elementBinding', creator.name().localName(), creator)

subject = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subject'), SimpleLiteral, documentation='A topic of the content of the resource. Typically, Subject will be \n      expressed as keywords, key phrases, or classification codes that \n      describe a topic of the resource. Recommended best practice is to \n      select a value from a controlled vocabulary or formal classification \n      scheme.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 45, 3))
Namespace.addCategoryObject('elementBinding', subject.name().localName(), subject)

description = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), SimpleLiteral, documentation='An account of the content of the resource. Examples of Description \n      include, but are not limited to, an abstract, table of contents, \n      reference to a graphical representation of content, or free-text \n      account of the content.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 55, 3))
Namespace.addCategoryObject('elementBinding', description.name().localName(), description)

publisher = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'publisher'), SimpleLiteral, documentation='An entity responsible for making the resource available. Examples of \n      Publisher include a person, an organization, or a service. Typically, \n      the name of a Publisher should be used to indicate the entity.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 64, 3))
Namespace.addCategoryObject('elementBinding', publisher.name().localName(), publisher)

contributor = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contributor'), SimpleLiteral, documentation='An entity responsible for making contributions to the content of \n      the resource. Examples of Contributor include a person, an organization, \n      or a service. Typically, the name of a Contributor should be used to \n      indicate the entity.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 72, 3))
Namespace.addCategoryObject('elementBinding', contributor.name().localName(), contributor)

date = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'date'), SimpleLiteral, documentation='A date of an event in the lifecycle of the resource. Typically, Date \n      will be associated with the creation or availability of the resource. \n      Recommended best practice for encoding the date value is defined in a \n      profile of ISO 8601 and includes (among others) dates of the \n      form YYYY-MM-DD.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 81, 3))
Namespace.addCategoryObject('elementBinding', date.name().localName(), date)

type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), SimpleLiteral, documentation='The nature or genre of the content of the resource. Type includes \n      terms describing general categories, functions, genres, or aggregation \n      levels for content. Recommended best practice is to select a value \n      from a controlled vocabulary (for example, the DCMI Type Vocabulary). \n      To describe the physical or digital manifestation of the resource, \n      use the Format element.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 91, 3))
Namespace.addCategoryObject('elementBinding', type.name().localName(), type)

format = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'format'), SimpleLiteral, documentation='The physical or digital manifestation of the resource. Typically, \n      Format will include the media-type or dimensions of the resource. \n      Format may be used to identify the software, hardware, or other \n      equipment needed to display or operate the resource. Examples of \n      dimensions include size and duration. Recommended best practice is to \n      select a value from a controlled vocabulary (for example, the list \n      of Internet Media Types defining computer media formats).', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 102, 3))
Namespace.addCategoryObject('elementBinding', format.name().localName(), format)

identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'identifier'), SimpleLiteral, documentation='An unambiguous reference to the resource within a given context. \n      Recommended best practice is to identify the resource by means of a \n      string or number conforming to a formal identification system. Formal \n      identification systems include but are not limited to the Uniform \n      Resource Identifier (URI) (including the Uniform Resource Locator \n      (URL)), the Digital Object Identifier (DOI), and the International \n      Standard Book Number (ISBN).', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 114, 3))
Namespace.addCategoryObject('elementBinding', identifier.name().localName(), identifier)

source = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'source'), SimpleLiteral, documentation='A Reference to a resource from which the present resource is derived.\n      The present resource may be derived from the Source resource in whole \n      or in part. Recommended best practice is to identify the referenced \n      resource by means of a string or number conforming to a formal \n      identification system.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 126, 3))
Namespace.addCategoryObject('elementBinding', source.name().localName(), source)

language = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'language'), SimpleLiteral, documentation='A language of the intellectual content of the resource. Recommended \n      best practice is to use RFC 3066, which, in conjunction with ISO 639, \n      defines two- and three-letter primary language tags with optional \n      subtags. Examples include "en" or "eng" for English, "akk" for\n      Akkadian, and "en-GB" for English used in the United Kingdom.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 136, 3))
Namespace.addCategoryObject('elementBinding', language.name().localName(), language)

relation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relation'), SimpleLiteral, documentation='A reference to a related resource. Recommended best practice is to \n      identify the referenced resource by means of a string or number \n      conforming to a formal identification system.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 146, 3))
Namespace.addCategoryObject('elementBinding', relation.name().localName(), relation)

coverage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coverage'), SimpleLiteral, documentation='The extent or scope of the content of the resource. Typically, \n      Coverage will include spatial location (a place name or geographic \n      coordinates), temporal period (a period label, date, or date range), \n      or jurisdiction (such as a named administrative entity). Recommended \n      best practice is to select a value from a controlled vocabulary \n      (for example, the Thesaurus of Geographic Names [TGN]) and to use, \n      where appropriate, named places or time periods in preference to \n      numeric identifiers such as sets of coordinates or date ranges.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 154, 3))
Namespace.addCategoryObject('elementBinding', coverage.name().localName(), coverage)

rights = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rights'), SimpleLiteral, documentation='Information about rights held in and over the resource. Typically, \n      Rights will contain a rights management statement for the resource, \n      or reference a service providing such information. Rights information \n      often encompasses Intellectual Property Rights (IPR), Copyright, and \n      various Property Rights. If the Rights element is absent, no \n      assumptions may be made about any rights held in or over the resource.', location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 167, 3))
Namespace.addCategoryObject('elementBinding', rights.name().localName(), rights)



def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=0, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 23, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 23, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SimpleLiteral._Automaton = _BuildAutomaton()




elementContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC-element'), SimpleLiteral, abstract=pyxb.binding.datatypes.boolean(1), scope=elementContainer, location=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 29, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 185, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(elementContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DC-element')), pyxb.utils.utility.Location('/home/ec2-user/proj/GeodesyML/tools/converter/pyxb-test/PyXB-1.2.5/pyxb/bundles/opengis/schemas/csw/2.0.2/rec-dcmes.xsd', 186, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
elementContainer._Automaton = _BuildAutomaton_()


title._setSubstitutionGroup(DC_element)

creator._setSubstitutionGroup(DC_element)

subject._setSubstitutionGroup(DC_element)

description._setSubstitutionGroup(DC_element)

publisher._setSubstitutionGroup(DC_element)

contributor._setSubstitutionGroup(DC_element)

date._setSubstitutionGroup(DC_element)

type._setSubstitutionGroup(DC_element)

format._setSubstitutionGroup(DC_element)

identifier._setSubstitutionGroup(DC_element)

source._setSubstitutionGroup(DC_element)

language._setSubstitutionGroup(DC_element)

relation._setSubstitutionGroup(DC_element)

coverage._setSubstitutionGroup(DC_element)

rights._setSubstitutionGroup(DC_element)
