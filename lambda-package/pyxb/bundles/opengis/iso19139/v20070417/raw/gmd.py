# ./pyxb/bundles/opengis/iso19139/v20070417/raw/gmd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:410705b36885cae3fa86a581e054e9b962463ed8
# Generated 2017-07-10 00:36:41.130864 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://www.isotc211.org/2005/gmd [xmlns:gmd]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d5964d50-6507-11e7-b2b4-0a55f9edafa5')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.bundles.opengis.raw._nsgroup_

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.isotc211.org/2005/gmd', create_if_missing=True)
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

from pyxb.bundles.opengis.raw._nsgroup_ import URL # {http://www.isotc211.org/2005/gmd}URL
from pyxb.bundles.opengis.raw._nsgroup_ import CI_RoleCode # {http://www.isotc211.org/2005/gmd}CI_RoleCode
from pyxb.bundles.opengis.raw._nsgroup_ import CI_PresentationFormCode # {http://www.isotc211.org/2005/gmd}CI_PresentationFormCode
from pyxb.bundles.opengis.raw._nsgroup_ import CI_OnLineFunctionCode # {http://www.isotc211.org/2005/gmd}CI_OnLineFunctionCode
from pyxb.bundles.opengis.raw._nsgroup_ import CI_DateTypeCode # {http://www.isotc211.org/2005/gmd}CI_DateTypeCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ClassificationCode # {http://www.isotc211.org/2005/gmd}MD_ClassificationCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_RestrictionCode # {http://www.isotc211.org/2005/gmd}MD_RestrictionCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_CoverageContentTypeCode # {http://www.isotc211.org/2005/gmd}MD_CoverageContentTypeCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ImagingConditionCode # {http://www.isotc211.org/2005/gmd}MD_ImagingConditionCode
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_EvaluationMethodTypeCode # {http://www.isotc211.org/2005/gmd}DQ_EvaluationMethodTypeCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_DistributionUnits # {http://www.isotc211.org/2005/gmd}MD_DistributionUnits
from pyxb.bundles.opengis.raw._nsgroup_ import MD_MediumFormatCode # {http://www.isotc211.org/2005/gmd}MD_MediumFormatCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_MediumNameCode # {http://www.isotc211.org/2005/gmd}MD_MediumNameCode
from pyxb.bundles.opengis.raw._nsgroup_ import LocalisedCharacterString # {http://www.isotc211.org/2005/gmd}LocalisedCharacterString
from pyxb.bundles.opengis.raw._nsgroup_ import PT_LocaleContainer # {http://www.isotc211.org/2005/gmd}PT_LocaleContainer
from pyxb.bundles.opengis.raw._nsgroup_ import LanguageCode # {http://www.isotc211.org/2005/gmd}LanguageCode
from pyxb.bundles.opengis.raw._nsgroup_ import Country # {http://www.isotc211.org/2005/gmd}Country
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Resolution # {http://www.isotc211.org/2005/gmd}MD_Resolution
from pyxb.bundles.opengis.raw._nsgroup_ import MD_TopicCategoryCode # {http://www.isotc211.org/2005/gmd}MD_TopicCategoryCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_CharacterSetCode # {http://www.isotc211.org/2005/gmd}MD_CharacterSetCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_SpatialRepresentationTypeCode # {http://www.isotc211.org/2005/gmd}MD_SpatialRepresentationTypeCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ProgressCode # {http://www.isotc211.org/2005/gmd}MD_ProgressCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_KeywordTypeCode # {http://www.isotc211.org/2005/gmd}MD_KeywordTypeCode
from pyxb.bundles.opengis.raw._nsgroup_ import DS_AssociationTypeCode # {http://www.isotc211.org/2005/gmd}DS_AssociationTypeCode
from pyxb.bundles.opengis.raw._nsgroup_ import DS_InitiativeTypeCode # {http://www.isotc211.org/2005/gmd}DS_InitiativeTypeCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ScopeDescription # {http://www.isotc211.org/2005/gmd}MD_ScopeDescription
from pyxb.bundles.opengis.raw._nsgroup_ import MD_MaintenanceFrequencyCode # {http://www.isotc211.org/2005/gmd}MD_MaintenanceFrequencyCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ScopeCode # {http://www.isotc211.org/2005/gmd}MD_ScopeCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ObligationCode # {http://www.isotc211.org/2005/gmd}MD_ObligationCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_DatatypeCode # {http://www.isotc211.org/2005/gmd}MD_DatatypeCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_PixelOrientationCode # {http://www.isotc211.org/2005/gmd}MD_PixelOrientationCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_TopologyLevelCode # {http://www.isotc211.org/2005/gmd}MD_TopologyLevelCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_GeometricObjectTypeCode # {http://www.isotc211.org/2005/gmd}MD_GeometricObjectTypeCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_CellGeometryCode # {http://www.isotc211.org/2005/gmd}MD_CellGeometryCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_DimensionNameTypeCode # {http://www.isotc211.org/2005/gmd}MD_DimensionNameTypeCode
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ApplicationSchemaInformation # {http://www.isotc211.org/2005/gmd}MD_ApplicationSchemaInformation
from pyxb.bundles.opengis.raw._nsgroup_ import CI_ResponsibleParty # {http://www.isotc211.org/2005/gmd}CI_ResponsibleParty
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Citation # {http://www.isotc211.org/2005/gmd}CI_Citation
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Address # {http://www.isotc211.org/2005/gmd}CI_Address
from pyxb.bundles.opengis.raw._nsgroup_ import CI_OnlineResource # {http://www.isotc211.org/2005/gmd}CI_OnlineResource
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Contact # {http://www.isotc211.org/2005/gmd}CI_Contact
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Telephone # {http://www.isotc211.org/2005/gmd}CI_Telephone
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Date # {http://www.isotc211.org/2005/gmd}CI_Date
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Series # {http://www.isotc211.org/2005/gmd}CI_Series
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Constraints # {http://www.isotc211.org/2005/gmd}MD_Constraints
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractMD_ContentInformation # {http://www.isotc211.org/2005/gmd}AbstractMD_ContentInformation
from pyxb.bundles.opengis.raw._nsgroup_ import MD_RangeDimension # {http://www.isotc211.org/2005/gmd}MD_RangeDimension
from pyxb.bundles.opengis.raw._nsgroup_ import LI_ProcessStep # {http://www.isotc211.org/2005/gmd}LI_ProcessStep
from pyxb.bundles.opengis.raw._nsgroup_ import LI_Source # {http://www.isotc211.org/2005/gmd}LI_Source
from pyxb.bundles.opengis.raw._nsgroup_ import LI_Lineage # {http://www.isotc211.org/2005/gmd}LI_Lineage
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractDQ_Result # {http://www.isotc211.org/2005/gmd}AbstractDQ_Result
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractDQ_Element # {http://www.isotc211.org/2005/gmd}AbstractDQ_Element
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_DataQuality # {http://www.isotc211.org/2005/gmd}DQ_DataQuality
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_Scope # {http://www.isotc211.org/2005/gmd}DQ_Scope
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Medium # {http://www.isotc211.org/2005/gmd}MD_Medium
from pyxb.bundles.opengis.raw._nsgroup_ import MD_DigitalTransferOptions # {http://www.isotc211.org/2005/gmd}MD_DigitalTransferOptions
from pyxb.bundles.opengis.raw._nsgroup_ import MD_StandardOrderProcess # {http://www.isotc211.org/2005/gmd}MD_StandardOrderProcess
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Distributor # {http://www.isotc211.org/2005/gmd}MD_Distributor
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Distribution # {http://www.isotc211.org/2005/gmd}MD_Distribution
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Format # {http://www.isotc211.org/2005/gmd}MD_Format
from pyxb.bundles.opengis.raw._nsgroup_ import EX_TemporalExtent # {http://www.isotc211.org/2005/gmd}EX_TemporalExtent
from pyxb.bundles.opengis.raw._nsgroup_ import EX_VerticalExtent # {http://www.isotc211.org/2005/gmd}EX_VerticalExtent
from pyxb.bundles.opengis.raw._nsgroup_ import EX_Extent # {http://www.isotc211.org/2005/gmd}EX_Extent
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractEX_GeographicExtent # {http://www.isotc211.org/2005/gmd}AbstractEX_GeographicExtent
from pyxb.bundles.opengis.raw._nsgroup_ import PT_FreeText # {http://www.isotc211.org/2005/gmd}PT_FreeText
from pyxb.bundles.opengis.raw._nsgroup_ import PT_Locale # {http://www.isotc211.org/2005/gmd}PT_Locale
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractMD_Identification # {http://www.isotc211.org/2005/gmd}AbstractMD_Identification
from pyxb.bundles.opengis.raw._nsgroup_ import MD_BrowseGraphic # {http://www.isotc211.org/2005/gmd}MD_BrowseGraphic
from pyxb.bundles.opengis.raw._nsgroup_ import MD_RepresentativeFraction # {http://www.isotc211.org/2005/gmd}MD_RepresentativeFraction
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Usage # {http://www.isotc211.org/2005/gmd}MD_Usage
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Keywords # {http://www.isotc211.org/2005/gmd}MD_Keywords
from pyxb.bundles.opengis.raw._nsgroup_ import DS_Association # {http://www.isotc211.org/2005/gmd}DS_Association
from pyxb.bundles.opengis.raw._nsgroup_ import MD_AggregateInformation # {http://www.isotc211.org/2005/gmd}MD_AggregateInformation
from pyxb.bundles.opengis.raw._nsgroup_ import MD_MaintenanceInformation # {http://www.isotc211.org/2005/gmd}MD_MaintenanceInformation
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractDS_Aggregate # {http://www.isotc211.org/2005/gmd}AbstractDS_Aggregate
from pyxb.bundles.opengis.raw._nsgroup_ import DS_DataSet # {http://www.isotc211.org/2005/gmd}DS_DataSet
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Metadata # {http://www.isotc211.org/2005/gmd}MD_Metadata
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ExtendedElementInformation # {http://www.isotc211.org/2005/gmd}MD_ExtendedElementInformation
from pyxb.bundles.opengis.raw._nsgroup_ import MD_MetadataExtensionInformation # {http://www.isotc211.org/2005/gmd}MD_MetadataExtensionInformation
from pyxb.bundles.opengis.raw._nsgroup_ import MD_PortrayalCatalogueReference # {http://www.isotc211.org/2005/gmd}MD_PortrayalCatalogueReference
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ReferenceSystem # {http://www.isotc211.org/2005/gmd}MD_ReferenceSystem
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Identifier # {http://www.isotc211.org/2005/gmd}MD_Identifier
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractRS_ReferenceSystem # {http://www.isotc211.org/2005/gmd}AbstractRS_ReferenceSystem
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractMD_SpatialRepresentation # {http://www.isotc211.org/2005/gmd}AbstractMD_SpatialRepresentation
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Dimension # {http://www.isotc211.org/2005/gmd}MD_Dimension
from pyxb.bundles.opengis.raw._nsgroup_ import MD_GeometricObjects # {http://www.isotc211.org/2005/gmd}MD_GeometricObjects
from pyxb.bundles.opengis.raw._nsgroup_ import MD_LegalConstraints # {http://www.isotc211.org/2005/gmd}MD_LegalConstraints
from pyxb.bundles.opengis.raw._nsgroup_ import MD_SecurityConstraints # {http://www.isotc211.org/2005/gmd}MD_SecurityConstraints
from pyxb.bundles.opengis.raw._nsgroup_ import MD_FeatureCatalogueDescription # {http://www.isotc211.org/2005/gmd}MD_FeatureCatalogueDescription
from pyxb.bundles.opengis.raw._nsgroup_ import MD_CoverageDescription # {http://www.isotc211.org/2005/gmd}MD_CoverageDescription
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Band # {http://www.isotc211.org/2005/gmd}MD_Band
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_ConformanceResult # {http://www.isotc211.org/2005/gmd}DQ_ConformanceResult
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_QuantitativeResult # {http://www.isotc211.org/2005/gmd}DQ_QuantitativeResult
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractDQ_TemporalAccuracy # {http://www.isotc211.org/2005/gmd}AbstractDQ_TemporalAccuracy
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractDQ_ThematicAccuracy # {http://www.isotc211.org/2005/gmd}AbstractDQ_ThematicAccuracy
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractDQ_PositionalAccuracy # {http://www.isotc211.org/2005/gmd}AbstractDQ_PositionalAccuracy
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractDQ_LogicalConsistency # {http://www.isotc211.org/2005/gmd}AbstractDQ_LogicalConsistency
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractDQ_Completeness # {http://www.isotc211.org/2005/gmd}AbstractDQ_Completeness
from pyxb.bundles.opengis.raw._nsgroup_ import EX_BoundingPolygon # {http://www.isotc211.org/2005/gmd}EX_BoundingPolygon
from pyxb.bundles.opengis.raw._nsgroup_ import EX_GeographicBoundingBox # {http://www.isotc211.org/2005/gmd}EX_GeographicBoundingBox
from pyxb.bundles.opengis.raw._nsgroup_ import EX_SpatialTemporalExtent # {http://www.isotc211.org/2005/gmd}EX_SpatialTemporalExtent
from pyxb.bundles.opengis.raw._nsgroup_ import EX_GeographicDescription # {http://www.isotc211.org/2005/gmd}EX_GeographicDescription
from pyxb.bundles.opengis.raw._nsgroup_ import MD_DataIdentification # {http://www.isotc211.org/2005/gmd}MD_DataIdentification
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ServiceIdentification # {http://www.isotc211.org/2005/gmd}MD_ServiceIdentification
from pyxb.bundles.opengis.raw._nsgroup_ import DS_OtherAggregate # {http://www.isotc211.org/2005/gmd}DS_OtherAggregate
from pyxb.bundles.opengis.raw._nsgroup_ import DS_Series # {http://www.isotc211.org/2005/gmd}DS_Series
from pyxb.bundles.opengis.raw._nsgroup_ import DS_Initiative # {http://www.isotc211.org/2005/gmd}DS_Initiative
from pyxb.bundles.opengis.raw._nsgroup_ import RS_Identifier # {http://www.isotc211.org/2005/gmd}RS_Identifier
from pyxb.bundles.opengis.raw._nsgroup_ import MD_GridSpatialRepresentation # {http://www.isotc211.org/2005/gmd}MD_GridSpatialRepresentation
from pyxb.bundles.opengis.raw._nsgroup_ import MD_VectorSpatialRepresentation # {http://www.isotc211.org/2005/gmd}MD_VectorSpatialRepresentation
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ImageDescription # {http://www.isotc211.org/2005/gmd}MD_ImageDescription
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_TemporalValidity # {http://www.isotc211.org/2005/gmd}DQ_TemporalValidity
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_TemporalConsistency # {http://www.isotc211.org/2005/gmd}DQ_TemporalConsistency
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_AccuracyOfATimeMeasurement # {http://www.isotc211.org/2005/gmd}DQ_AccuracyOfATimeMeasurement
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_QuantitativeAttributeAccuracy # {http://www.isotc211.org/2005/gmd}DQ_QuantitativeAttributeAccuracy
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_NonQuantitativeAttributeAccuracy # {http://www.isotc211.org/2005/gmd}DQ_NonQuantitativeAttributeAccuracy
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_ThematicClassificationCorrectness # {http://www.isotc211.org/2005/gmd}DQ_ThematicClassificationCorrectness
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_RelativeInternalPositionalAccuracy # {http://www.isotc211.org/2005/gmd}DQ_RelativeInternalPositionalAccuracy
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_GriddedDataPositionalAccuracy # {http://www.isotc211.org/2005/gmd}DQ_GriddedDataPositionalAccuracy
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_AbsoluteExternalPositionalAccuracy # {http://www.isotc211.org/2005/gmd}DQ_AbsoluteExternalPositionalAccuracy
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_TopologicalConsistency # {http://www.isotc211.org/2005/gmd}DQ_TopologicalConsistency
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_FormatConsistency # {http://www.isotc211.org/2005/gmd}DQ_FormatConsistency
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_DomainConsistency # {http://www.isotc211.org/2005/gmd}DQ_DomainConsistency
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_ConceptualConsistency # {http://www.isotc211.org/2005/gmd}DQ_ConceptualConsistency
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_CompletenessOmission # {http://www.isotc211.org/2005/gmd}DQ_CompletenessOmission
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_CompletenessCommission # {http://www.isotc211.org/2005/gmd}DQ_CompletenessCommission
from pyxb.bundles.opengis.raw._nsgroup_ import DS_Platform # {http://www.isotc211.org/2005/gmd}DS_Platform
from pyxb.bundles.opengis.raw._nsgroup_ import DS_Sensor # {http://www.isotc211.org/2005/gmd}DS_Sensor
from pyxb.bundles.opengis.raw._nsgroup_ import DS_ProductionSeries # {http://www.isotc211.org/2005/gmd}DS_ProductionSeries
from pyxb.bundles.opengis.raw._nsgroup_ import DS_StereoMate # {http://www.isotc211.org/2005/gmd}DS_StereoMate
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Georeferenceable # {http://www.isotc211.org/2005/gmd}MD_Georeferenceable
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Georectified # {http://www.isotc211.org/2005/gmd}MD_Georectified
from pyxb.bundles.opengis.raw._nsgroup_ import LocalisedCharacterString_Type # {http://www.isotc211.org/2005/gmd}LocalisedCharacterString_Type
from pyxb.bundles.opengis.raw._nsgroup_ import PT_LocaleContainer_Type # {http://www.isotc211.org/2005/gmd}PT_LocaleContainer_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Resolution_Type # {http://www.isotc211.org/2005/gmd}MD_Resolution_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_TopicCategoryCode_Type # {http://www.isotc211.org/2005/gmd}MD_TopicCategoryCode_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ScopeDescription_Type # {http://www.isotc211.org/2005/gmd}MD_ScopeDescription_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ObligationCode_Type # {http://www.isotc211.org/2005/gmd}MD_ObligationCode_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_PixelOrientationCode_Type # {http://www.isotc211.org/2005/gmd}MD_PixelOrientationCode_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ApplicationSchemaInformation_Type # {http://www.isotc211.org/2005/gmd}MD_ApplicationSchemaInformation_Type
from pyxb.bundles.opengis.raw._nsgroup_ import CI_ResponsibleParty_Type # {http://www.isotc211.org/2005/gmd}CI_ResponsibleParty_Type
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Citation_Type # {http://www.isotc211.org/2005/gmd}CI_Citation_Type
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Address_Type # {http://www.isotc211.org/2005/gmd}CI_Address_Type
from pyxb.bundles.opengis.raw._nsgroup_ import CI_OnlineResource_Type # {http://www.isotc211.org/2005/gmd}CI_OnlineResource_Type
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Contact_Type # {http://www.isotc211.org/2005/gmd}CI_Contact_Type
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Telephone_Type # {http://www.isotc211.org/2005/gmd}CI_Telephone_Type
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Date_Type # {http://www.isotc211.org/2005/gmd}CI_Date_Type
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Series_Type # {http://www.isotc211.org/2005/gmd}CI_Series_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Constraints_Type # {http://www.isotc211.org/2005/gmd}MD_Constraints_Type
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractMD_ContentInformation_Type # {http://www.isotc211.org/2005/gmd}AbstractMD_ContentInformation_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_RangeDimension_Type # {http://www.isotc211.org/2005/gmd}MD_RangeDimension_Type
from pyxb.bundles.opengis.raw._nsgroup_ import LI_ProcessStep_Type # {http://www.isotc211.org/2005/gmd}LI_ProcessStep_Type
from pyxb.bundles.opengis.raw._nsgroup_ import LI_Source_Type # {http://www.isotc211.org/2005/gmd}LI_Source_Type
from pyxb.bundles.opengis.raw._nsgroup_ import LI_Lineage_Type # {http://www.isotc211.org/2005/gmd}LI_Lineage_Type
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractDQ_Result_Type # {http://www.isotc211.org/2005/gmd}AbstractDQ_Result_Type
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractDQ_Element_Type # {http://www.isotc211.org/2005/gmd}AbstractDQ_Element_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_DataQuality_Type # {http://www.isotc211.org/2005/gmd}DQ_DataQuality_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_Scope_Type # {http://www.isotc211.org/2005/gmd}DQ_Scope_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Medium_Type # {http://www.isotc211.org/2005/gmd}MD_Medium_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_DigitalTransferOptions_Type # {http://www.isotc211.org/2005/gmd}MD_DigitalTransferOptions_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_StandardOrderProcess_Type # {http://www.isotc211.org/2005/gmd}MD_StandardOrderProcess_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Distributor_Type # {http://www.isotc211.org/2005/gmd}MD_Distributor_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Distribution_Type # {http://www.isotc211.org/2005/gmd}MD_Distribution_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Format_Type # {http://www.isotc211.org/2005/gmd}MD_Format_Type
from pyxb.bundles.opengis.raw._nsgroup_ import EX_TemporalExtent_Type # {http://www.isotc211.org/2005/gmd}EX_TemporalExtent_Type
from pyxb.bundles.opengis.raw._nsgroup_ import EX_VerticalExtent_Type # {http://www.isotc211.org/2005/gmd}EX_VerticalExtent_Type
from pyxb.bundles.opengis.raw._nsgroup_ import EX_Extent_Type # {http://www.isotc211.org/2005/gmd}EX_Extent_Type
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractEX_GeographicExtent_Type # {http://www.isotc211.org/2005/gmd}AbstractEX_GeographicExtent_Type
from pyxb.bundles.opengis.raw._nsgroup_ import PT_FreeText_Type # {http://www.isotc211.org/2005/gmd}PT_FreeText_Type
from pyxb.bundles.opengis.raw._nsgroup_ import PT_Locale_Type # {http://www.isotc211.org/2005/gmd}PT_Locale_Type
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractMD_Identification_Type # {http://www.isotc211.org/2005/gmd}AbstractMD_Identification_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_BrowseGraphic_Type # {http://www.isotc211.org/2005/gmd}MD_BrowseGraphic_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_RepresentativeFraction_Type # {http://www.isotc211.org/2005/gmd}MD_RepresentativeFraction_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Usage_Type # {http://www.isotc211.org/2005/gmd}MD_Usage_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Keywords_Type # {http://www.isotc211.org/2005/gmd}MD_Keywords_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DS_Association_Type # {http://www.isotc211.org/2005/gmd}DS_Association_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_AggregateInformation_Type # {http://www.isotc211.org/2005/gmd}MD_AggregateInformation_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_MaintenanceInformation_Type # {http://www.isotc211.org/2005/gmd}MD_MaintenanceInformation_Type
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractDS_Aggregate_Type # {http://www.isotc211.org/2005/gmd}AbstractDS_Aggregate_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DS_DataSet_Type # {http://www.isotc211.org/2005/gmd}DS_DataSet_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Metadata_Type # {http://www.isotc211.org/2005/gmd}MD_Metadata_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ExtendedElementInformation_Type # {http://www.isotc211.org/2005/gmd}MD_ExtendedElementInformation_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_MetadataExtensionInformation_Type # {http://www.isotc211.org/2005/gmd}MD_MetadataExtensionInformation_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_PortrayalCatalogueReference_Type # {http://www.isotc211.org/2005/gmd}MD_PortrayalCatalogueReference_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ReferenceSystem_Type # {http://www.isotc211.org/2005/gmd}MD_ReferenceSystem_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Identifier_Type # {http://www.isotc211.org/2005/gmd}MD_Identifier_Type
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractRS_ReferenceSystem_Type # {http://www.isotc211.org/2005/gmd}AbstractRS_ReferenceSystem_Type
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractMD_SpatialRepresentation_Type # {http://www.isotc211.org/2005/gmd}AbstractMD_SpatialRepresentation_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Dimension_Type # {http://www.isotc211.org/2005/gmd}MD_Dimension_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_GeometricObjects_Type # {http://www.isotc211.org/2005/gmd}MD_GeometricObjects_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ApplicationSchemaInformation_PropertyType # {http://www.isotc211.org/2005/gmd}MD_ApplicationSchemaInformation_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import CI_ResponsibleParty_PropertyType # {http://www.isotc211.org/2005/gmd}CI_ResponsibleParty_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Citation_PropertyType # {http://www.isotc211.org/2005/gmd}CI_Citation_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Address_PropertyType # {http://www.isotc211.org/2005/gmd}CI_Address_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import CI_OnlineResource_PropertyType # {http://www.isotc211.org/2005/gmd}CI_OnlineResource_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Contact_PropertyType # {http://www.isotc211.org/2005/gmd}CI_Contact_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Telephone_PropertyType # {http://www.isotc211.org/2005/gmd}CI_Telephone_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Date_PropertyType # {http://www.isotc211.org/2005/gmd}CI_Date_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import CI_Series_PropertyType # {http://www.isotc211.org/2005/gmd}CI_Series_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import URL_PropertyType # {http://www.isotc211.org/2005/gmd}URL_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import CI_RoleCode_PropertyType # {http://www.isotc211.org/2005/gmd}CI_RoleCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import CI_PresentationFormCode_PropertyType # {http://www.isotc211.org/2005/gmd}CI_PresentationFormCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import CI_OnLineFunctionCode_PropertyType # {http://www.isotc211.org/2005/gmd}CI_OnLineFunctionCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import CI_DateTypeCode_PropertyType # {http://www.isotc211.org/2005/gmd}CI_DateTypeCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Constraints_PropertyType # {http://www.isotc211.org/2005/gmd}MD_Constraints_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_LegalConstraints_Type # {http://www.isotc211.org/2005/gmd}MD_LegalConstraints_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_LegalConstraints_PropertyType # {http://www.isotc211.org/2005/gmd}MD_LegalConstraints_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_SecurityConstraints_Type # {http://www.isotc211.org/2005/gmd}MD_SecurityConstraints_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_SecurityConstraints_PropertyType # {http://www.isotc211.org/2005/gmd}MD_SecurityConstraints_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ClassificationCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_ClassificationCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_RestrictionCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_RestrictionCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_FeatureCatalogueDescription_Type # {http://www.isotc211.org/2005/gmd}MD_FeatureCatalogueDescription_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_FeatureCatalogueDescription_PropertyType # {http://www.isotc211.org/2005/gmd}MD_FeatureCatalogueDescription_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_CoverageDescription_Type # {http://www.isotc211.org/2005/gmd}MD_CoverageDescription_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_CoverageDescription_PropertyType # {http://www.isotc211.org/2005/gmd}MD_CoverageDescription_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ImageDescription_PropertyType # {http://www.isotc211.org/2005/gmd}MD_ImageDescription_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ContentInformation_PropertyType # {http://www.isotc211.org/2005/gmd}MD_ContentInformation_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_RangeDimension_PropertyType # {http://www.isotc211.org/2005/gmd}MD_RangeDimension_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Band_Type # {http://www.isotc211.org/2005/gmd}MD_Band_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Band_PropertyType # {http://www.isotc211.org/2005/gmd}MD_Band_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_CoverageContentTypeCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_CoverageContentTypeCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ImagingConditionCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_ImagingConditionCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import LI_ProcessStep_PropertyType # {http://www.isotc211.org/2005/gmd}LI_ProcessStep_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import LI_Source_PropertyType # {http://www.isotc211.org/2005/gmd}LI_Source_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import LI_Lineage_PropertyType # {http://www.isotc211.org/2005/gmd}LI_Lineage_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_ConformanceResult_Type # {http://www.isotc211.org/2005/gmd}DQ_ConformanceResult_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_ConformanceResult_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_ConformanceResult_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_QuantitativeResult_Type # {http://www.isotc211.org/2005/gmd}DQ_QuantitativeResult_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_QuantitativeResult_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_QuantitativeResult_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_Result_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_Result_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_TemporalValidity_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_TemporalValidity_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_TemporalConsistency_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_TemporalConsistency_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_AccuracyOfATimeMeasurement_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_AccuracyOfATimeMeasurement_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_QuantitativeAttributeAccuracy_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_QuantitativeAttributeAccuracy_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_NonQuantitativeAttributeAccuracy_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_NonQuantitativeAttributeAccuracy_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_ThematicClassificationCorrectness_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_ThematicClassificationCorrectness_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_RelativeInternalPositionalAccuracy_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_RelativeInternalPositionalAccuracy_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_GriddedDataPositionalAccuracy_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_GriddedDataPositionalAccuracy_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_AbsoluteExternalPositionalAccuracy_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_AbsoluteExternalPositionalAccuracy_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_TopologicalConsistency_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_TopologicalConsistency_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_FormatConsistency_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_FormatConsistency_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_DomainConsistency_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_DomainConsistency_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_ConceptualConsistency_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_ConceptualConsistency_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_CompletenessOmission_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_CompletenessOmission_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_CompletenessCommission_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_CompletenessCommission_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractDQ_TemporalAccuracy_Type # {http://www.isotc211.org/2005/gmd}AbstractDQ_TemporalAccuracy_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_TemporalAccuracy_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_TemporalAccuracy_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractDQ_ThematicAccuracy_Type # {http://www.isotc211.org/2005/gmd}AbstractDQ_ThematicAccuracy_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_ThematicAccuracy_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_ThematicAccuracy_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractDQ_PositionalAccuracy_Type # {http://www.isotc211.org/2005/gmd}AbstractDQ_PositionalAccuracy_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_PositionalAccuracy_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_PositionalAccuracy_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractDQ_LogicalConsistency_Type # {http://www.isotc211.org/2005/gmd}AbstractDQ_LogicalConsistency_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_LogicalConsistency_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_LogicalConsistency_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import AbstractDQ_Completeness_Type # {http://www.isotc211.org/2005/gmd}AbstractDQ_Completeness_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_Completeness_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_Completeness_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_Element_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_Element_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_DataQuality_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_DataQuality_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_Scope_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_Scope_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_EvaluationMethodTypeCode_PropertyType # {http://www.isotc211.org/2005/gmd}DQ_EvaluationMethodTypeCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Medium_PropertyType # {http://www.isotc211.org/2005/gmd}MD_Medium_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_DigitalTransferOptions_PropertyType # {http://www.isotc211.org/2005/gmd}MD_DigitalTransferOptions_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_StandardOrderProcess_PropertyType # {http://www.isotc211.org/2005/gmd}MD_StandardOrderProcess_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Distributor_PropertyType # {http://www.isotc211.org/2005/gmd}MD_Distributor_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Distribution_PropertyType # {http://www.isotc211.org/2005/gmd}MD_Distribution_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Format_PropertyType # {http://www.isotc211.org/2005/gmd}MD_Format_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_DistributionUnits_PropertyType # {http://www.isotc211.org/2005/gmd}MD_DistributionUnits_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_MediumFormatCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_MediumFormatCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_MediumNameCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_MediumNameCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import EX_TemporalExtent_PropertyType # {http://www.isotc211.org/2005/gmd}EX_TemporalExtent_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import EX_VerticalExtent_PropertyType # {http://www.isotc211.org/2005/gmd}EX_VerticalExtent_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import EX_BoundingPolygon_Type # {http://www.isotc211.org/2005/gmd}EX_BoundingPolygon_Type
from pyxb.bundles.opengis.raw._nsgroup_ import EX_BoundingPolygon_PropertyType # {http://www.isotc211.org/2005/gmd}EX_BoundingPolygon_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import EX_Extent_PropertyType # {http://www.isotc211.org/2005/gmd}EX_Extent_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import EX_GeographicExtent_PropertyType # {http://www.isotc211.org/2005/gmd}EX_GeographicExtent_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import EX_GeographicBoundingBox_Type # {http://www.isotc211.org/2005/gmd}EX_GeographicBoundingBox_Type
from pyxb.bundles.opengis.raw._nsgroup_ import EX_GeographicBoundingBox_PropertyType # {http://www.isotc211.org/2005/gmd}EX_GeographicBoundingBox_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import EX_SpatialTemporalExtent_Type # {http://www.isotc211.org/2005/gmd}EX_SpatialTemporalExtent_Type
from pyxb.bundles.opengis.raw._nsgroup_ import EX_SpatialTemporalExtent_PropertyType # {http://www.isotc211.org/2005/gmd}EX_SpatialTemporalExtent_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import EX_GeographicDescription_Type # {http://www.isotc211.org/2005/gmd}EX_GeographicDescription_Type
from pyxb.bundles.opengis.raw._nsgroup_ import EX_GeographicDescription_PropertyType # {http://www.isotc211.org/2005/gmd}EX_GeographicDescription_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import PT_Locale_PropertyType # {http://www.isotc211.org/2005/gmd}PT_Locale_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import PT_LocaleContainer_PropertyType # {http://www.isotc211.org/2005/gmd}PT_LocaleContainer_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import LanguageCode_PropertyType # {http://www.isotc211.org/2005/gmd}LanguageCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import Country_PropertyType # {http://www.isotc211.org/2005/gmd}Country_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Identification_PropertyType # {http://www.isotc211.org/2005/gmd}MD_Identification_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_BrowseGraphic_PropertyType # {http://www.isotc211.org/2005/gmd}MD_BrowseGraphic_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_DataIdentification_Type # {http://www.isotc211.org/2005/gmd}MD_DataIdentification_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_DataIdentification_PropertyType # {http://www.isotc211.org/2005/gmd}MD_DataIdentification_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ServiceIdentification_Type # {http://www.isotc211.org/2005/gmd}MD_ServiceIdentification_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ServiceIdentification_PropertyType # {http://www.isotc211.org/2005/gmd}MD_ServiceIdentification_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_RepresentativeFraction_PropertyType # {http://www.isotc211.org/2005/gmd}MD_RepresentativeFraction_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Usage_PropertyType # {http://www.isotc211.org/2005/gmd}MD_Usage_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Keywords_PropertyType # {http://www.isotc211.org/2005/gmd}MD_Keywords_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DS_Association_PropertyType # {http://www.isotc211.org/2005/gmd}DS_Association_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_AggregateInformation_PropertyType # {http://www.isotc211.org/2005/gmd}MD_AggregateInformation_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Resolution_PropertyType # {http://www.isotc211.org/2005/gmd}MD_Resolution_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_TopicCategoryCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_TopicCategoryCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_CharacterSetCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_CharacterSetCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_SpatialRepresentationTypeCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_SpatialRepresentationTypeCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ProgressCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_ProgressCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_KeywordTypeCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_KeywordTypeCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DS_AssociationTypeCode_PropertyType # {http://www.isotc211.org/2005/gmd}DS_AssociationTypeCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DS_InitiativeTypeCode_PropertyType # {http://www.isotc211.org/2005/gmd}DS_InitiativeTypeCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_MaintenanceInformation_PropertyType # {http://www.isotc211.org/2005/gmd}MD_MaintenanceInformation_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ScopeDescription_PropertyType # {http://www.isotc211.org/2005/gmd}MD_ScopeDescription_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_MaintenanceFrequencyCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_MaintenanceFrequencyCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ScopeCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_ScopeCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DS_Aggregate_PropertyType # {http://www.isotc211.org/2005/gmd}DS_Aggregate_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DS_DataSet_PropertyType # {http://www.isotc211.org/2005/gmd}DS_DataSet_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DS_OtherAggregate_Type # {http://www.isotc211.org/2005/gmd}DS_OtherAggregate_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DS_OtherAggregate_PropertyType # {http://www.isotc211.org/2005/gmd}DS_OtherAggregate_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DS_Series_Type # {http://www.isotc211.org/2005/gmd}DS_Series_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DS_Series_PropertyType # {http://www.isotc211.org/2005/gmd}DS_Series_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DS_Initiative_Type # {http://www.isotc211.org/2005/gmd}DS_Initiative_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DS_Initiative_PropertyType # {http://www.isotc211.org/2005/gmd}DS_Initiative_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DS_Platform_PropertyType # {http://www.isotc211.org/2005/gmd}DS_Platform_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DS_Sensor_PropertyType # {http://www.isotc211.org/2005/gmd}DS_Sensor_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DS_ProductionSeries_PropertyType # {http://www.isotc211.org/2005/gmd}DS_ProductionSeries_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DS_StereoMate_PropertyType # {http://www.isotc211.org/2005/gmd}DS_StereoMate_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Metadata_PropertyType # {http://www.isotc211.org/2005/gmd}MD_Metadata_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ExtendedElementInformation_PropertyType # {http://www.isotc211.org/2005/gmd}MD_ExtendedElementInformation_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_MetadataExtensionInformation_PropertyType # {http://www.isotc211.org/2005/gmd}MD_MetadataExtensionInformation_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ObligationCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_ObligationCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_DatatypeCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_DatatypeCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_PortrayalCatalogueReference_PropertyType # {http://www.isotc211.org/2005/gmd}MD_PortrayalCatalogueReference_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import RS_Identifier_Type # {http://www.isotc211.org/2005/gmd}RS_Identifier_Type
from pyxb.bundles.opengis.raw._nsgroup_ import RS_Identifier_PropertyType # {http://www.isotc211.org/2005/gmd}RS_Identifier_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ReferenceSystem_PropertyType # {http://www.isotc211.org/2005/gmd}MD_ReferenceSystem_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Identifier_PropertyType # {http://www.isotc211.org/2005/gmd}MD_Identifier_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import RS_ReferenceSystem_PropertyType # {http://www.isotc211.org/2005/gmd}RS_ReferenceSystem_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_GridSpatialRepresentation_Type # {http://www.isotc211.org/2005/gmd}MD_GridSpatialRepresentation_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_GridSpatialRepresentation_PropertyType # {http://www.isotc211.org/2005/gmd}MD_GridSpatialRepresentation_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_VectorSpatialRepresentation_Type # {http://www.isotc211.org/2005/gmd}MD_VectorSpatialRepresentation_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_VectorSpatialRepresentation_PropertyType # {http://www.isotc211.org/2005/gmd}MD_VectorSpatialRepresentation_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_SpatialRepresentation_PropertyType # {http://www.isotc211.org/2005/gmd}MD_SpatialRepresentation_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Georeferenceable_PropertyType # {http://www.isotc211.org/2005/gmd}MD_Georeferenceable_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Dimension_PropertyType # {http://www.isotc211.org/2005/gmd}MD_Dimension_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Georectified_PropertyType # {http://www.isotc211.org/2005/gmd}MD_Georectified_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_GeometricObjects_PropertyType # {http://www.isotc211.org/2005/gmd}MD_GeometricObjects_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_PixelOrientationCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_PixelOrientationCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_TopologyLevelCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_TopologyLevelCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_GeometricObjectTypeCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_GeometricObjectTypeCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_CellGeometryCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_CellGeometryCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_DimensionNameTypeCode_PropertyType # {http://www.isotc211.org/2005/gmd}MD_DimensionNameTypeCode_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import MD_ImageDescription_Type # {http://www.isotc211.org/2005/gmd}MD_ImageDescription_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_TemporalValidity_Type # {http://www.isotc211.org/2005/gmd}DQ_TemporalValidity_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_TemporalConsistency_Type # {http://www.isotc211.org/2005/gmd}DQ_TemporalConsistency_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_AccuracyOfATimeMeasurement_Type # {http://www.isotc211.org/2005/gmd}DQ_AccuracyOfATimeMeasurement_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_QuantitativeAttributeAccuracy_Type # {http://www.isotc211.org/2005/gmd}DQ_QuantitativeAttributeAccuracy_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_NonQuantitativeAttributeAccuracy_Type # {http://www.isotc211.org/2005/gmd}DQ_NonQuantitativeAttributeAccuracy_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_ThematicClassificationCorrectness_Type # {http://www.isotc211.org/2005/gmd}DQ_ThematicClassificationCorrectness_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_RelativeInternalPositionalAccuracy_Type # {http://www.isotc211.org/2005/gmd}DQ_RelativeInternalPositionalAccuracy_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_GriddedDataPositionalAccuracy_Type # {http://www.isotc211.org/2005/gmd}DQ_GriddedDataPositionalAccuracy_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_AbsoluteExternalPositionalAccuracy_Type # {http://www.isotc211.org/2005/gmd}DQ_AbsoluteExternalPositionalAccuracy_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_TopologicalConsistency_Type # {http://www.isotc211.org/2005/gmd}DQ_TopologicalConsistency_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_FormatConsistency_Type # {http://www.isotc211.org/2005/gmd}DQ_FormatConsistency_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_DomainConsistency_Type # {http://www.isotc211.org/2005/gmd}DQ_DomainConsistency_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_ConceptualConsistency_Type # {http://www.isotc211.org/2005/gmd}DQ_ConceptualConsistency_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_CompletenessOmission_Type # {http://www.isotc211.org/2005/gmd}DQ_CompletenessOmission_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DQ_CompletenessCommission_Type # {http://www.isotc211.org/2005/gmd}DQ_CompletenessCommission_Type
from pyxb.bundles.opengis.raw._nsgroup_ import PT_FreeText_PropertyType # {http://www.isotc211.org/2005/gmd}PT_FreeText_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import LocalisedCharacterString_PropertyType # {http://www.isotc211.org/2005/gmd}LocalisedCharacterString_PropertyType
from pyxb.bundles.opengis.raw._nsgroup_ import DS_Platform_Type # {http://www.isotc211.org/2005/gmd}DS_Platform_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DS_Sensor_Type # {http://www.isotc211.org/2005/gmd}DS_Sensor_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DS_ProductionSeries_Type # {http://www.isotc211.org/2005/gmd}DS_ProductionSeries_Type
from pyxb.bundles.opengis.raw._nsgroup_ import DS_StereoMate_Type # {http://www.isotc211.org/2005/gmd}DS_StereoMate_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Georeferenceable_Type # {http://www.isotc211.org/2005/gmd}MD_Georeferenceable_Type
from pyxb.bundles.opengis.raw._nsgroup_ import MD_Georectified_Type # {http://www.isotc211.org/2005/gmd}MD_Georectified_Type
