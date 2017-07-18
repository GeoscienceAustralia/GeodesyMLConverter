# ./pyxb/bundles/opengis/raw/csw_dct.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:62e52a6e1b0d23522982e9c2905e5cb67ad01951
# Generated 2017-07-10 00:38:03.297559 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://purl.org/dc/terms/ [xmlns:dct]

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
import pyxb.bundles.opengis.raw._nsgroup_2

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://purl.org/dc/terms/', create_if_missing=True)
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

from pyxb.bundles.opengis.raw._nsgroup_2 import abstract # {http://purl.org/dc/terms/}abstract
from pyxb.bundles.opengis.raw._nsgroup_2 import accessRights # {http://purl.org/dc/terms/}accessRights
from pyxb.bundles.opengis.raw._nsgroup_2 import alternative # {http://purl.org/dc/terms/}alternative
from pyxb.bundles.opengis.raw._nsgroup_2 import audience # {http://purl.org/dc/terms/}audience
from pyxb.bundles.opengis.raw._nsgroup_2 import available # {http://purl.org/dc/terms/}available
from pyxb.bundles.opengis.raw._nsgroup_2 import bibliographicCitation # {http://purl.org/dc/terms/}bibliographicCitation
from pyxb.bundles.opengis.raw._nsgroup_2 import conformsTo # {http://purl.org/dc/terms/}conformsTo
from pyxb.bundles.opengis.raw._nsgroup_2 import created # {http://purl.org/dc/terms/}created
from pyxb.bundles.opengis.raw._nsgroup_2 import dateAccepted # {http://purl.org/dc/terms/}dateAccepted
from pyxb.bundles.opengis.raw._nsgroup_2 import dateCopyrighted # {http://purl.org/dc/terms/}dateCopyrighted
from pyxb.bundles.opengis.raw._nsgroup_2 import dateSubmitted # {http://purl.org/dc/terms/}dateSubmitted
from pyxb.bundles.opengis.raw._nsgroup_2 import educationLevel # {http://purl.org/dc/terms/}educationLevel
from pyxb.bundles.opengis.raw._nsgroup_2 import extent # {http://purl.org/dc/terms/}extent
from pyxb.bundles.opengis.raw._nsgroup_2 import hasFormat # {http://purl.org/dc/terms/}hasFormat
from pyxb.bundles.opengis.raw._nsgroup_2 import hasPart # {http://purl.org/dc/terms/}hasPart
from pyxb.bundles.opengis.raw._nsgroup_2 import hasVersion # {http://purl.org/dc/terms/}hasVersion
from pyxb.bundles.opengis.raw._nsgroup_2 import isFormatOf # {http://purl.org/dc/terms/}isFormatOf
from pyxb.bundles.opengis.raw._nsgroup_2 import isPartOf # {http://purl.org/dc/terms/}isPartOf
from pyxb.bundles.opengis.raw._nsgroup_2 import isReferencedBy # {http://purl.org/dc/terms/}isReferencedBy
from pyxb.bundles.opengis.raw._nsgroup_2 import isReplacedBy # {http://purl.org/dc/terms/}isReplacedBy
from pyxb.bundles.opengis.raw._nsgroup_2 import isRequiredBy # {http://purl.org/dc/terms/}isRequiredBy
from pyxb.bundles.opengis.raw._nsgroup_2 import issued # {http://purl.org/dc/terms/}issued
from pyxb.bundles.opengis.raw._nsgroup_2 import isVersionOf # {http://purl.org/dc/terms/}isVersionOf
from pyxb.bundles.opengis.raw._nsgroup_2 import license # {http://purl.org/dc/terms/}license
from pyxb.bundles.opengis.raw._nsgroup_2 import mediator # {http://purl.org/dc/terms/}mediator
from pyxb.bundles.opengis.raw._nsgroup_2 import medium # {http://purl.org/dc/terms/}medium
from pyxb.bundles.opengis.raw._nsgroup_2 import modified # {http://purl.org/dc/terms/}modified
from pyxb.bundles.opengis.raw._nsgroup_2 import provenance # {http://purl.org/dc/terms/}provenance
from pyxb.bundles.opengis.raw._nsgroup_2 import references # {http://purl.org/dc/terms/}references
from pyxb.bundles.opengis.raw._nsgroup_2 import replaces # {http://purl.org/dc/terms/}replaces
from pyxb.bundles.opengis.raw._nsgroup_2 import requires # {http://purl.org/dc/terms/}requires
from pyxb.bundles.opengis.raw._nsgroup_2 import rightsHolder # {http://purl.org/dc/terms/}rightsHolder
from pyxb.bundles.opengis.raw._nsgroup_2 import spatial # {http://purl.org/dc/terms/}spatial
from pyxb.bundles.opengis.raw._nsgroup_2 import tableOfContents # {http://purl.org/dc/terms/}tableOfContents
from pyxb.bundles.opengis.raw._nsgroup_2 import temporal # {http://purl.org/dc/terms/}temporal
from pyxb.bundles.opengis.raw._nsgroup_2 import valid # {http://purl.org/dc/terms/}valid
