<DOCFLEX_TEMPLATE VER='1.19'>
CREATED='2008-11-17 02:44:26'
LAST_UPDATE='2014-07-05 20:02:50'
DESIGNER_TOOL='DocFlex SDK 1.x'
DESIGNER_LICENSE_TYPE='Filigris Works Team'
APP_ID='docflex-xml-xsddoc2'
APP_NAME='DocFlex/XML XSDDoc'
APP_VER='2.8.1'
APP_AUTHOR='Copyright © 2005-2014 Filigris Works, Leonid Rudy Softwareprodukte. All rights reserved.'
TEMPLATE_TYPE='DocumentTemplate'
DSM_TYPE_ID='xsddoc'
ROOT_ET='xs:element'
DESCR='Documents \'final\' attribute of a global element component'
<TEMPLATE_PARAMS>
	PARAM={
		param.name='$finalAttrValues';
		param.title='The actual values of \'final\' attribute';
		param.type='string';
		param.list='true';
		param.defaultValue.expr='hasAttr ("final") ? getAttrValues ("final") :
  findAncestor("xs:schema").getAttrValues ("finalDefault")';
		param.fixed='true';
	}
	PARAM={
		param.name='$profile.final.value';
		param.title='Value';
		param.type='boolean';
	}
	PARAM={
		param.name='$profile.final.meaning';
		param.title='Meaning';
		param.type='boolean';
	}
</TEMPLATE_PARAMS>
<STYLES>
	CHAR_STYLE={
		style.name='Default Paragraph Font';
		style.id='cs1';
		style.default='true';
	}
	CHAR_STYLE={
		style.name='Hyperlink';
		style.id='cs2';
		text.decor.underline='true';
		text.color.foreground='#0000FF';
	}
	CHAR_STYLE={
		style.name='Mono (Small)';
		style.id='cs3';
		text.font.name='Courier New';
		text.font.size='8';
	}
	PAR_STYLE={
		style.name='Normal';
		style.id='s1';
		style.default='true';
	}
	CHAR_STYLE={
		style.name='Property Note';
		style.id='cs4';
		text.font.name='Tahoma';
		text.font.size='8';
		text.font.style.italic='true';
	}
</STYLES>
FMT={
	doc.lengthUnits='pt';
	doc.hlink.style.link='cs2';
}
<ROOT>
	<AREA_SEC>
		COND='getBooleanParam("$profile.final.value")'
		FMT={
			text.style='cs3';
			txtfl.delimiter.type='none';
		}
		<AREA>
			<CTRL_GROUP>
				<CTRLS>
					<TEXT_CTRL>
						TEXT='"'
					</TEXT_CTRL>
					<DATA_CTRL>
						FORMULA='getArrayParam("$finalAttrValues")'
						FMT={
							txtfl.delimiter.text=' ';
						}
					</DATA_CTRL>
					<TEXT_CTRL>
						TEXT='"'
					</TEXT_CTRL>
				</CTRLS>
			</CTRL_GROUP>
		</AREA>
	</AREA_SEC>
	<FOLDER>
		DESCR='meaning'
		COND='getBooleanParam("$profile.final.meaning")'
		FMT={
			text.style='cs4';
		}
		<BODY>
			<AREA_SEC>
				DESCR='#all'
				COND='getArrayParam("$finalAttrValues").contains ("#all")'
				BREAK_PARENT_BLOCK='when-executed'
				<AREA>
					<CTRL_GROUP>
						<CTRLS>
							<TEXT_CTRL>
								TEXT='(cannot be used as the head of a substitution group)'
							</TEXT_CTRL>
						</CTRLS>
					</CTRL_GROUP>
				</AREA>
			</AREA_SEC>
			<AREA_SEC>
				DESCR='extension, restriction'
				COND='values = getArrayParam("$finalAttrValues");

derivations = Vector();

values.contains ("extension") ?
  derivations.addElement ("extension");

values.contains ("restriction") ?
  derivations.addElement ("restriction");

derivations.size() > 0 ? 
{
  setVar ("blocked_derivations", derivations);
  true
} : false'
				<AREA>
					<CTRL_GROUP>
						<CTRLS>
							<TEXT_CTRL>
								TEXT='(cannot be used as the head of a substitution group for elements whose types are derived by'
							</TEXT_CTRL>
							<DATA_CTRL>
								FORMULA='mergeStrings (
  getVar ("blocked_derivations").toVector(),
  ", ", " or "
)'
							</DATA_CTRL>
							<TEXT_CTRL>
								TEXT='from the type of this element)'
							</TEXT_CTRL>
						</CTRLS>
					</CTRL_GROUP>
				</AREA>
			</AREA_SEC>
		</BODY>
	</FOLDER>
</ROOT>
CHECKSUM='tPsrErpsZM?rgropnCZ4bXHluRYvVOiM0bhi?CHE9cA'
</DOCFLEX_TEMPLATE>