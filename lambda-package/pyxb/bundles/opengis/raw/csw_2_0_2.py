# ./pyxb/bundles/opengis/raw/csw_2_0_2.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:c35b4890f3f07f9b39d4250cbebdd4198468ac22
# Generated 2017-07-10 00:38:03.297268 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.opengis.net/cat/csw/2.0.2

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
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/cat/csw/2.0.2', create_if_missing=True)
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

from pyxb.bundles.opengis.raw._nsgroup_2 import GetCapabilities # {http://www.opengis.net/cat/csw/2.0.2}GetCapabilities
from pyxb.bundles.opengis.raw._nsgroup_2 import Capabilities # {http://www.opengis.net/cat/csw/2.0.2}Capabilities
from pyxb.bundles.opengis.raw._nsgroup_2 import DescribeRecordResponse # {http://www.opengis.net/cat/csw/2.0.2}DescribeRecordResponse
from pyxb.bundles.opengis.raw._nsgroup_2 import AbstractQuery # {http://www.opengis.net/cat/csw/2.0.2}AbstractQuery
from pyxb.bundles.opengis.raw._nsgroup_2 import Constraint # {http://www.opengis.net/cat/csw/2.0.2}Constraint
from pyxb.bundles.opengis.raw._nsgroup_2 import GetRecordsResponse # {http://www.opengis.net/cat/csw/2.0.2}GetRecordsResponse
from pyxb.bundles.opengis.raw._nsgroup_2 import GetRecordByIdResponse # {http://www.opengis.net/cat/csw/2.0.2}GetRecordByIdResponse
from pyxb.bundles.opengis.raw._nsgroup_2 import GetDomainResponse # {http://www.opengis.net/cat/csw/2.0.2}GetDomainResponse
from pyxb.bundles.opengis.raw._nsgroup_2 import Acknowledgement # {http://www.opengis.net/cat/csw/2.0.2}Acknowledgement
from pyxb.bundles.opengis.raw._nsgroup_2 import RecordProperty # {http://www.opengis.net/cat/csw/2.0.2}RecordProperty
from pyxb.bundles.opengis.raw._nsgroup_2 import TransactionResponse # {http://www.opengis.net/cat/csw/2.0.2}TransactionResponse
from pyxb.bundles.opengis.raw._nsgroup_2 import HarvestResponse # {http://www.opengis.net/cat/csw/2.0.2}HarvestResponse
from pyxb.bundles.opengis.raw._nsgroup_2 import AbstractRecord # {http://www.opengis.net/cat/csw/2.0.2}AbstractRecord
from pyxb.bundles.opengis.raw._nsgroup_2 import DescribeRecord # {http://www.opengis.net/cat/csw/2.0.2}DescribeRecord
from pyxb.bundles.opengis.raw._nsgroup_2 import GetRecords # {http://www.opengis.net/cat/csw/2.0.2}GetRecords
from pyxb.bundles.opengis.raw._nsgroup_2 import Query # {http://www.opengis.net/cat/csw/2.0.2}Query
from pyxb.bundles.opengis.raw._nsgroup_2 import ElementSetName # {http://www.opengis.net/cat/csw/2.0.2}ElementSetName
from pyxb.bundles.opengis.raw._nsgroup_2 import GetRecordById # {http://www.opengis.net/cat/csw/2.0.2}GetRecordById
from pyxb.bundles.opengis.raw._nsgroup_2 import GetDomain # {http://www.opengis.net/cat/csw/2.0.2}GetDomain
from pyxb.bundles.opengis.raw._nsgroup_2 import Transaction # {http://www.opengis.net/cat/csw/2.0.2}Transaction
from pyxb.bundles.opengis.raw._nsgroup_2 import Harvest # {http://www.opengis.net/cat/csw/2.0.2}Harvest
from pyxb.bundles.opengis.raw._nsgroup_2 import DCMIRecord # {http://www.opengis.net/cat/csw/2.0.2}DCMIRecord
from pyxb.bundles.opengis.raw._nsgroup_2 import BriefRecord # {http://www.opengis.net/cat/csw/2.0.2}BriefRecord
from pyxb.bundles.opengis.raw._nsgroup_2 import SummaryRecord # {http://www.opengis.net/cat/csw/2.0.2}SummaryRecord
from pyxb.bundles.opengis.raw._nsgroup_2 import Record # {http://www.opengis.net/cat/csw/2.0.2}Record
from pyxb.bundles.opengis.raw._nsgroup_2 import RequestBaseType # {http://www.opengis.net/cat/csw/2.0.2}RequestBaseType
from pyxb.bundles.opengis.raw._nsgroup_2 import GetCapabilitiesType # {http://www.opengis.net/cat/csw/2.0.2}GetCapabilitiesType
from pyxb.bundles.opengis.raw._nsgroup_2 import CapabilitiesType # {http://www.opengis.net/cat/csw/2.0.2}CapabilitiesType
from pyxb.bundles.opengis.raw._nsgroup_2 import DescribeRecordResponseType # {http://www.opengis.net/cat/csw/2.0.2}DescribeRecordResponseType
from pyxb.bundles.opengis.raw._nsgroup_2 import SchemaComponentType # {http://www.opengis.net/cat/csw/2.0.2}SchemaComponentType
from pyxb.bundles.opengis.raw._nsgroup_2 import ResultType # {http://www.opengis.net/cat/csw/2.0.2}ResultType
from pyxb.bundles.opengis.raw._nsgroup_2 import DistributedSearchType # {http://www.opengis.net/cat/csw/2.0.2}DistributedSearchType
from pyxb.bundles.opengis.raw._nsgroup_2 import AbstractQueryType # {http://www.opengis.net/cat/csw/2.0.2}AbstractQueryType
from pyxb.bundles.opengis.raw._nsgroup_2 import TypeNameListType # {http://www.opengis.net/cat/csw/2.0.2}TypeNameListType
from pyxb.bundles.opengis.raw._nsgroup_2 import QueryConstraintType # {http://www.opengis.net/cat/csw/2.0.2}QueryConstraintType
from pyxb.bundles.opengis.raw._nsgroup_2 import ElementSetType # {http://www.opengis.net/cat/csw/2.0.2}ElementSetType
from pyxb.bundles.opengis.raw._nsgroup_2 import GetRecordsResponseType # {http://www.opengis.net/cat/csw/2.0.2}GetRecordsResponseType
from pyxb.bundles.opengis.raw._nsgroup_2 import RequestStatusType # {http://www.opengis.net/cat/csw/2.0.2}RequestStatusType
from pyxb.bundles.opengis.raw._nsgroup_2 import GetRecordByIdResponseType # {http://www.opengis.net/cat/csw/2.0.2}GetRecordByIdResponseType
from pyxb.bundles.opengis.raw._nsgroup_2 import GetDomainResponseType # {http://www.opengis.net/cat/csw/2.0.2}GetDomainResponseType
from pyxb.bundles.opengis.raw._nsgroup_2 import DomainValuesType # {http://www.opengis.net/cat/csw/2.0.2}DomainValuesType
from pyxb.bundles.opengis.raw._nsgroup_2 import ListOfValuesType # {http://www.opengis.net/cat/csw/2.0.2}ListOfValuesType
from pyxb.bundles.opengis.raw._nsgroup_2 import ConceptualSchemeType # {http://www.opengis.net/cat/csw/2.0.2}ConceptualSchemeType
from pyxb.bundles.opengis.raw._nsgroup_2 import RangeOfValuesType # {http://www.opengis.net/cat/csw/2.0.2}RangeOfValuesType
from pyxb.bundles.opengis.raw._nsgroup_2 import AcknowledgementType # {http://www.opengis.net/cat/csw/2.0.2}AcknowledgementType
from pyxb.bundles.opengis.raw._nsgroup_2 import EchoedRequestType # {http://www.opengis.net/cat/csw/2.0.2}EchoedRequestType
from pyxb.bundles.opengis.raw._nsgroup_2 import InsertType # {http://www.opengis.net/cat/csw/2.0.2}InsertType
from pyxb.bundles.opengis.raw._nsgroup_2 import UpdateType # {http://www.opengis.net/cat/csw/2.0.2}UpdateType
from pyxb.bundles.opengis.raw._nsgroup_2 import DeleteType # {http://www.opengis.net/cat/csw/2.0.2}DeleteType
from pyxb.bundles.opengis.raw._nsgroup_2 import RecordPropertyType # {http://www.opengis.net/cat/csw/2.0.2}RecordPropertyType
from pyxb.bundles.opengis.raw._nsgroup_2 import TransactionResponseType # {http://www.opengis.net/cat/csw/2.0.2}TransactionResponseType
from pyxb.bundles.opengis.raw._nsgroup_2 import TransactionSummaryType # {http://www.opengis.net/cat/csw/2.0.2}TransactionSummaryType
from pyxb.bundles.opengis.raw._nsgroup_2 import InsertResultType # {http://www.opengis.net/cat/csw/2.0.2}InsertResultType
from pyxb.bundles.opengis.raw._nsgroup_2 import HarvestResponseType # {http://www.opengis.net/cat/csw/2.0.2}HarvestResponseType
from pyxb.bundles.opengis.raw._nsgroup_2 import AbstractRecordType # {http://www.opengis.net/cat/csw/2.0.2}AbstractRecordType
from pyxb.bundles.opengis.raw._nsgroup_2 import EmptyType # {http://www.opengis.net/cat/csw/2.0.2}EmptyType
from pyxb.bundles.opengis.raw._nsgroup_2 import DescribeRecordType # {http://www.opengis.net/cat/csw/2.0.2}DescribeRecordType
from pyxb.bundles.opengis.raw._nsgroup_2 import GetRecordsType # {http://www.opengis.net/cat/csw/2.0.2}GetRecordsType
from pyxb.bundles.opengis.raw._nsgroup_2 import QueryType # {http://www.opengis.net/cat/csw/2.0.2}QueryType
from pyxb.bundles.opengis.raw._nsgroup_2 import ElementSetNameType # {http://www.opengis.net/cat/csw/2.0.2}ElementSetNameType
from pyxb.bundles.opengis.raw._nsgroup_2 import SearchResultsType # {http://www.opengis.net/cat/csw/2.0.2}SearchResultsType
from pyxb.bundles.opengis.raw._nsgroup_2 import GetRecordByIdType # {http://www.opengis.net/cat/csw/2.0.2}GetRecordByIdType
from pyxb.bundles.opengis.raw._nsgroup_2 import GetDomainType # {http://www.opengis.net/cat/csw/2.0.2}GetDomainType
from pyxb.bundles.opengis.raw._nsgroup_2 import TransactionType # {http://www.opengis.net/cat/csw/2.0.2}TransactionType
from pyxb.bundles.opengis.raw._nsgroup_2 import HarvestType # {http://www.opengis.net/cat/csw/2.0.2}HarvestType
from pyxb.bundles.opengis.raw._nsgroup_2 import DCMIRecordType # {http://www.opengis.net/cat/csw/2.0.2}DCMIRecordType
from pyxb.bundles.opengis.raw._nsgroup_2 import BriefRecordType # {http://www.opengis.net/cat/csw/2.0.2}BriefRecordType
from pyxb.bundles.opengis.raw._nsgroup_2 import SummaryRecordType # {http://www.opengis.net/cat/csw/2.0.2}SummaryRecordType
from pyxb.bundles.opengis.raw._nsgroup_2 import RecordType # {http://www.opengis.net/cat/csw/2.0.2}RecordType
