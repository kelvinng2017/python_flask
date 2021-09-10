STKMOVE = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD dt="struct" Sys="ACS" CMD="STKMOVE">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">STKMOVE</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <DATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strUSERID dt="String">{USERID}</strUSERID>
    <strCARRIERID dt="String">{CARRIERID}</strCARRIERID>
    <strCARRIERTYPE dt="String">MAGAZINE</strCARRIERTYPE>
    <strFROMDEVICE dt="String">{FROMDEVICE}</strFROMDEVICE>
    <strFROMPORT dt="String">{FROMPORT}</strFROMPORT>
    <strTODEVICE dt="String">{TODEVICE}</strTODEVICE>
    <strTOPORT dt="String">{TOPORT}</strTOPORT>
    <strEMPTYCARRIER dt="String">{EMPTYCARRIER}</strEMPTYCARRIER>
    <strPRIORITY dt="String">{PRIORITY}</strPRIORITY>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">STKMOVE</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">STKMOVE</strCMD>
    </htPROGINFO>
  </DATA>
</CMD>'''

STKMOVE_R = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD xmlns:dt="urn:schemas-microsoft-com:datatypes" xmlns:DOC="urn:Document" dt="struct" Sys="ACS" CMD="STKMOVE_R">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">STKMOVE_R</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PID dt="String">{PROCESS_ID}</PID>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <OUTDATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strRESULT dt="String">{RESULT}</strRESULT>
    <strERRORMESSAGE dt="String">{ERRORMESSAGE}</strERRORMESSAGE>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">STKMOVE_R</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">STKMOVE_R</strCMD>
    </htPROGINFO>
  </OUTDATA>
</CMD>'''

EQMOVE = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD dt="struct" Sys="ACS" CMD="EQMOVE">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">EQMOVE</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <DATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strUSERID dt="String">{USERID}</strUSERID>
    <strCARRIERID dt="String">{CARRIERID}</strCARRIERID>
    <strCARRIERTYPE dt="String">MAGAZINE</strCARRIERTYPE>
    <strFROMDEVICE dt="String">{FROMDEVICE}</strFROMDEVICE>
    <strFROMPORT dt="String">{FROMPORT}</strFROMPORT>
    <strTODEVICE dt="String">{TODEVICE}</strTODEVICE>
    <strTOPORT dt="String">{TOPORT}</strTOPORT>
    <strEMPTYCARRIER dt="String">{EMPTYCARRIER}</strEMPTYCARRIER>
    <strPRIORITY dt="String">{PRIORITY}</strPRIORITY>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">EQMOVE</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">EQMOVE</strCMD>
    </htPROGINFO>
  </DATA>
</CMD>'''

EQMOVE_R = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD xmlns:dt="urn:schemas-microsoft-com:datatypes" xmlns:DOC="urn:Document" dt="struct" Sys="ACS" CMD="EQMOVE_R">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">EQMOVE_R</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PID dt="String">{PROCESS_ID}</PID>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <OUTDATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strRESULT dt="String">{RESULT}</strRESULT>
    <strERRORMESSAGE dt="String">{ERRORMESSAGE}</strERRORMESSAGE>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">EQMOVE_R</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">EQMOVE_R</strCMD>
    </htPROGINFO>
  </OUTDATA>
</CMD>'''

EMPTYCARRMOVE = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD dt="struct" Sys="ACS" CMD="EMPTYCARRMOVE">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">EMPTYCARRMOVE</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <DATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strUSERID dt="String">{USERID}</strUSERID>
    <strCARRIERTYPE dt="String">MAGAZINE</strCARRIERTYPE>
    <strTODEVICE dt="String">{TODEVICE}</strTODEVICE>
    <strTOPORT dt="String">{TOPORT}</strTOPORT>
    <strPRIORITY dt="String">{PRIORITY}</strPRIORITY>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">EMPTYCARRMOVE</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">EMPTYCARRMOVE</strCMD>
    </htPROGINFO>
  </DATA>
</CMD>'''

EMPTYCARRMOVE_R = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD xmlns:dt="urn:schemas-microsoft-com:datatypes" xmlns:DOC="urn:Document" dt="struct" Sys="ACS" CMD="EMPTYCARRMOVE_R">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">EMPTYCARRMOVE_R</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PID dt="String">{PROCESS_ID}</PID>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <OUTDATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strRESULT dt="String">{RESULT}</strRESULT>
    <strERRORMESSAGE dt="String">{ERRORMESSAGE}</strERRORMESSAGE>
    <strCARRIERID dt="String">{CARRIERID}</strCARRIERID>
    <strCARRIERTYPE dt="String">MAGAZINE</strCARRIERTYPE>
    <strFROMDEVICE dt="String">{FROMDEVICE}</strFROMDEVICE>
    <strFROMPORT dt="String">{FROMPORT}</strFROMPORT>
    <strTODEVICE dt="String">{TODEVICE}</strTODEVICE>
    <strTOPORT dt="String">{TOPORT}</strTOPORT>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">EMPTYCARRMOVE_R</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">EMPTYCARRMOVE_R</strCMD>
    </htPROGINFO>
  </OUTDATA>
</CMD>'''

CHANGECMD = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD dt="struct" Sys="ACS" CMD="CHANGECMD">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">CHANGECMD</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <DATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strUSERID dt="String">{USERID}</strUSERID>
    <strCARRIERID dt="String">{CARRIERID}</strCARRIERID>
    <strCARRIERTYPE dt="String">MAGAZINE</strCARRIERTYPE>
    <strFROMDEVICE dt="String">{FROMDEVICE}</strFROMDEVICE>
    <strFROMPORT dt="String">{FROMPORT}</strFROMPORT>
    <strTODEVICE dt="String">{TODEVICE}</strTODEVICE>
    <strTOPORT dt="String">{TOPORT}</strTOPORT>
    <strPRIORITY dt="String">{PRIORITY}</strPRIORITY>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">CHANGECMD</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">CHANGECMD</strCMD>
    </htPROGINFO>
  </DATA>
</CMD>'''

CHANGECMD_R = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD xmlns:dt="urn:schemas-microsoft-com:datatypes" xmlns:DOC="urn:Document" dt="struct" Sys="ACS" CMD="CHANGECMD_R">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">CHANGECMD_R</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PID dt="String">{PROCESS_ID}</PID>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <OUTDATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strRESULT dt="String">{RESULT}</strRESULT>
    <strERRORMESSAGE dt="String">{ERRORMESSAGE}</strERRORMESSAGE>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">CHANGECMD_R</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">CHANGECMD_R</strCMD>
    </htPROGINFO>
  </OUTDATA>
</CMD>'''

MOVEREQUEST = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD dt="struct" Sys="ACS" CMD="MOVEREQUEST">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">MOVEREQUEST</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <DATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strUSERID dt="String">{USERID}</strUSERID>
    <strCARRIERID dt="String">{CARRIERID}</strCARRIERID>
    <strCARRIERTYPE dt="String">MAGAZINE</strCARRIERTYPE>
    <strFROMDEVICE dt="String">{FROMDEVICE}</strFROMDEVICE>
    <strFROMPORT dt="String">{FROMPORT}</strFROMPORT>
    <strTODEVICE dt="String">{TODEVICE}</strTODEVICE>
    <strTOPORT dt="String">{TOPORT}</strTOPORT>
    <strPRIORITY dt="String">{PRIORITY}</strPRIORITY>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">MOVEREQUEST</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">MOVEREQUEST</strCMD>
    </htPROGINFO>
  </DATA>
</CMD>'''

MOVEREQUEST_R = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD xmlns:dt="urn:schemas-microsoft-com:datatypes" xmlns:DOC="urn:Document" dt="struct" Sys="ACS" CMD="MOVEREQUEST_R">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">MOVEREQUEST_R</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PID dt="String">{PROCESS_ID}</PID>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <OUTDATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strRESULT dt="String">{RESULT}</strRESULT>
    <strERRORMESSAGE dt="String">{ERRORMESSAGE}</strERRORMESSAGE>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">MOVEREQUEST_R</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">MOVEREQUEST_R</strCMD>
    </htPROGINFO>
  </OUTDATA>
</CMD>'''

INVDATA = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD dt="struct" Sys="ACS" CMD="INVDATA">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">INVDATA</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <DATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strUSERID dt="String">{USERID}</strUSERID>
    <strSTKID dt="String">{STKID}</strSTKID>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">INVDATA</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">INVDATA</strCMD>
    </htPROGINFO>
  </DATA>
</CMD>'''

INVDATA_R = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD xmlns:dt="urn:schemas-microsoft-com:datatypes" xmlns:DOC="urn:Document" dt="struct" Sys="ACS" CMD="INVDATA_R">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">INVDATA_R</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PID dt="String">{PROCESS_ID}</PID>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <OUTDATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strSTKID dt="String">{STKID}</strSTKID>
    <strCOUNT dt="String">{COUNT}</strCOUNT>
    <strCARRIERIDList dt="String">{CARRIERIDLIST}</strCARRIERIDList>
    <strSTKSTATUS dt="String">{STKSTATUS}</strSTKSTATUS>
    <strRESULT dt="String">{RESULT}</strRESULT>
    <strERRORMESSAGE dt="String">{ERRORMESSAGE}</strERRORMESSAGE>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">INVDATA_R</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">INVDATA_R</strCMD>
    </htPROGINFO>
  </OUTDATA>
</CMD>'''

MOVESTATUSREQUEST = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD dt="struct" Sys="ACS" CMD="MOVESTATUSREQUEST">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">MOVESTATUSREQUEST</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <DATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strUSERID dt="String">{USERID}</strUSERID>
    <strCARRIERID dt="String">{CARRIERID}</strCARRIERID>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">MOVESTATUSREQUEST</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">MOVESTATUSREQUEST</strCMD>
    </htPROGINFO>
  </DATA>
</CMD>'''

MOVESTATUSREQUEST_R = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD xmlns:dt="urn:schemas-microsoft-com:datatypes" xmlns:DOC="urn:Document" dt="struct" Sys="ACS" CMD="MOVESTATUSREQUEST_R">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">MOVESTATUSREQUEST_R</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PID dt="String">{PROCESS_ID}</PID>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <OUTDATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strCARRIERID dt="String">{CARRIERID}</strCARRIERID>
    <strMOVESTATUS dt="String">{MOVESTATUS}</strMOVESTATUS>
    <strTODEVICE dt="String">{TODEVICE}</strTODEVICE>
    <strTOPORT dt="String">{TOPORT}</strTOPORT>
    <strPRIORITY dt="String">{PRIORITY}</strPRIORITY>
    <strRESULT dt="String">{RESULT}</strRESULT>
    <strERRORMESSAGE dt="String">{ERRORMESSAGE}</strERRORMESSAGE>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">MOVESTATUSREQUEST_R</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">MOVESTATUSREQUEST_R</strCMD>
    </htPROGINFO>
  </OUTDATA>
</CMD>'''

OUTSTK = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD dt="struct" Sys="ACS" CMD="OUTSTK">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">OUTSTK</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <DATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strCARRIERID dt="String">{CARRIERID}</strCARRIERID>
    <strSTKID dt="String">{STKID}</strSTKID>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">OUTSTK</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">OUTSTK</strCMD>
    </htPROGINFO>
  </DATA>
</CMD>'''

OUTSTK_R = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD xmlns:dt="urn:schemas-microsoft-com:datatypes" xmlns:DOC="urn:Document" dt="struct" Sys="ACS" CMD="OUTSTK_R">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">OUTSTK_R</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PID dt="String">{PROCESS_ID}</PID>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <OUTDATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strRESULT dt="String">{RESULT}</strRESULT>
    <strERRORMESSAGE dt="String">{ERRORMESSAGE}</strERRORMESSAGE>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">OUTSTK_R</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">OUTSTK_R</strCMD>
    </htPROGINFO>
  </OUTDATA>
</CMD>'''

LEAVE = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD dt="struct" Sys="ACS" CMD="LEAVE">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">LEAVE</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <DATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strCARRIERID dt="String">{CARRIERID}</strCARRIERID>
    <strVEHICLEID dt="String">{VEHICLEID}</strVEHICLEID>
    <strFROMDEVICE dt="String">{FROMDEVICE}</strFROMDEVICE>
    <strFROMPORT dt="String">{FROMPORT}</strFROMPORT>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">LEAVE</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">LEAVE</strCMD>
    </htPROGINFO>
  </DATA>
</CMD>'''

LEAVE_R = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD xmlns:dt="urn:schemas-microsoft-com:datatypes" xmlns:DOC="urn:Document" dt="struct" Sys="ACS" CMD="LEAVE_R">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">LEAVE_R</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PID dt="String">{PROCESS_ID}</PID>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <OUTDATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strRESULT dt="String">{RESULT}</strRESULT>
    <strERRORMESSAGE dt="String">{ERRORMESSAGE}</strERRORMESSAGE>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">LEAVE_R</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">LEAVE_R</strCMD>
    </htPROGINFO>
  </OUTDATA>
</CMD>'''

ARRIVE = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD dt="struct" Sys="ACS" CMD="ARRIVE">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">ARRIVE</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <DATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strCARRIERID dt="String">{CARRIERID}</strCARRIERID>
    <strVEHICLEID dt="String">{VEHICLEID}</strVEHICLEID>
    <strTODEVICE dt="String">{TODEVICE}</strTODEVICE>
    <strTOPORT dt="String">{TOPORT}</strTOPORT>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">ARRIVE</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">ARRIVE</strCMD>
    </htPROGINFO>
  </DATA>
</CMD>'''

ARRIVE_R = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD xmlns:dt="urn:schemas-microsoft-com:datatypes" xmlns:DOC="urn:Document" dt="struct" Sys="ACS" CMD="ARRIVE_R">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">ARRIVE_R</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PID dt="String">{PROCESS_ID}</PID>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <OUTDATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strRESULT dt="String">{RESULT}</strRESULT>
    <strERRORMESSAGE dt="String">{ERRORMESSAGE}</strERRORMESSAGE>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">ARRIVE_R</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">ARRIVE_R</strCMD>
    </htPROGINFO>
  </OUTDATA>
</CMD>'''

VALIDINPUT = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD dt="struct" Sys="ACS" CMD="VALIDINPUT">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">VALIDINPUT</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <DATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strCARRIERID dt="String">{CARRIERID}</strCARRIERID>
    <strVEHICLEID dt="String">{VEHICLEID}</strVEHICLEID>
    <strACTIONTYPE dt="String">{ACTIONTYPE}</strACTIONTYPE>
    <strFROMDEVICE dt="String">{FROMDEVICE}</strFROMDEVICE>
    <strFROMPORT dt="String">{FROMPORT}</strFROMPORT>
    <strTODEVICE dt="String">{TODEVICE}</strTODEVICE>
    <strTOPORT dt="String">{TOPORT}</strTOPORT>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">VALIDINPUT</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">VALIDINPUT</strCMD>
    </htPROGINFO>
  </DATA>
</CMD>'''

VALIDINPUT_R = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD xmlns:dt="urn:schemas-microsoft-com:datatypes" xmlns:DOC="urn:Document" dt="struct" Sys="ACS" CMD="VALIDINPUT_R">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">VALIDINPUT_R</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PID dt="String">{PROCESS_ID}</PID>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <OUTDATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strRESULT dt="String">{RESULT}</strRESULT>
    <strERRORMESSAGE dt="String">{ERRORMESSAGE}</strERRORMESSAGE>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">VALIDINPUT_R</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">VALIDINPUT_R</strCMD>
    </htPROGINFO>
  </OUTDATA>
</CMD>'''

OUTEQP = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD dt="struct" Sys="ACS" CMD="OUTEQP">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">OUTEQP</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <DATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strCARRIERID dt="String">{CARRIERID}</strCARRIERID>
    <strVEHICLEID dt="String">{VEHICLEID}</strVEHICLEID>
    <strFROMDEVICE dt="String">{FROMDEVICE}</strFROMDEVICE>
    <strFROMPORT dt="String">{FROMPORT}</strFROMPORT>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">OUTEQP</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">OUTEQP</strCMD>
    </htPROGINFO>
  </DATA>
</CMD>'''

OUTEQP_R = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD xmlns:dt="urn:schemas-microsoft-com:datatypes" xmlns:DOC="urn:Document" dt="struct" Sys="ACS" CMD="OUTEQP_R">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">OUTEQP_R</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PID dt="String">{PROCESS_ID}</PID>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <OUTDATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strRESULT dt="String">{RESULT}</strRESULT>
    <strERRORMESSAGE dt="String">{ERRORMESSAGE}</strERRORMESSAGE>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">OUTEQP_R</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">OUTEQP_R</strCMD>
    </htPROGINFO>
  </OUTDATA>
</CMD>'''

INEQP = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD dt="struct" Sys="ACS" CMD="INEQP">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">INEQP</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <DATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strCARRIERID dt="String">{CARRIERID}</strCARRIERID>
    <strVEHICLEID dt="String">{VEHICLEID}</strVEHICLEID>
    <strTODEVICE dt="String">{TODEVICE}</strTODEVICE>
    <strTOPORT dt="String">{TOPORT}</strTOPORT>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">INEQP</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">INEQP</strCMD>
    </htPROGINFO>
  </DATA>
</CMD>'''

INEQP_R = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD xmlns:dt="urn:schemas-microsoft-com:datatypes" xmlns:DOC="urn:Document" dt="struct" Sys="ACS" CMD="INEQP_R">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">INEQP_R</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PID dt="String">{PROCESS_ID}</PID>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <OUTDATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strRESULT dt="String">{RESULT}</strRESULT>
    <strERRORMESSAGE dt="String">{ERRORMESSAGE}</strERRORMESSAGE>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">INEQP_R</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">INEQP_R</strCMD>
    </htPROGINFO>
  </OUTDATA>
</CMD>'''

CARR_ALARM = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD dt="struct" Sys="ACS" CMD="CARR_ALARM">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">CARR_ALARM</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <DATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strCARRIERID dt="String">{CARRIERID}</strCARRIERID>
    <strVEHICLEID dt="String">{VEHICLEID}</strVEHICLEID>
    <strALARMCODE dt="String">{ALARMCODE}</strALARMCODE>
    <strALARMDESC dt="String">{ALARMDESC}</strALARMDESC>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">CARR_ALARM</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">CARR_ALARM</strCMD>
    </htPROGINFO>
  </DATA>
</CMD>'''

CARR_ALARM_R = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD xmlns:dt="urn:schemas-microsoft-com:datatypes" xmlns:DOC="urn:Document" dt="struct" Sys="ACS" CMD="CARR_ALARM_R">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">CARR_ALARM_R</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PID dt="String">{PROCESS_ID}</PID>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <OUTDATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strRESULT dt="String">{RESULT}</strRESULT>
    <strERRORMESSAGE dt="String">{ERRORMESSAGE}</strERRORMESSAGE>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">CARR_ALARM_R</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">CARR_ALARM_R</strCMD>
    </htPROGINFO>
  </OUTDATA>
</CMD>'''

INSTK = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD dt="struct" Sys="ACS" CMD="INSTK">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">INSTK</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <DATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strCARRIERID dt="String">{CARRIERID}</strCARRIERID>
    <strSTKID dt="String">{STKID}</strSTKID>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">INSTK</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">INSTK</strCMD>
    </htPROGINFO>
  </DATA>
</CMD>'''

INSTK_R = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD xmlns:dt="urn:schemas-microsoft-com:datatypes" xmlns:DOC="urn:Document" dt="struct" Sys="ACS" CMD="INSTK_R">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">INSTK_R</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PID dt="String">{PROCESS_ID}</PID>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <OUTDATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strRESULT dt="String">{RESULT}</strRESULT>
    <strERRORMESSAGE dt="String">{ERRORMESSAGE}</strERRORMESSAGE>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">INSTK_R</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">INSTK_R</strCMD>
    </htPROGINFO>
  </OUTDATA>
</CMD>'''

FOUPINFO = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD dt="struct" Sys="ACS" CMD="FOUPINFO">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">FOUPINFO</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <DATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strCARRIERID dt="String">{CARRIERID}</strCARRIERID>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">FOUPINFO</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">FOUPINFO</strCMD>
    </htPROGINFO>
  </DATA>
</CMD>'''

FOUPINFO_R = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD xmlns:dt="urn:schemas-microsoft-com:datatypes" xmlns:DOC="urn:Document" dt="struct" Sys="ACS" CMD="FOUPINFO_R">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">FOUPINFO_R</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PID dt="String">{PROCESS_ID}</PID>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <OUTDATA dt="struct">
    <strCOMMANDID dt="String">{COMMANDID}</strCOMMANDID>
    <strCARRIERID dt="String">{CARRIERID}</strCARRIERID>
    <strTODEVICE dt="String">{TODEVICE}</strTODEVICE>
    <strTOPORT dt="String">{TOPORT}</strTOPORT>
    <strRESULT dt="String">{RESULT}</strRESULT>
    <strERRORMESSAGE dt="String">{ERRORMESSAGE}</strERRORMESSAGE>
    <htPROGINFO dt="struct">
      <strMETHODNAME dt="String">FOUPINFO_R</strMETHODNAME>
      <strFORMNAME dt="String">ACS</strFORMNAME>
      <strCMD dt="String">FOUPINFO_R</strCMD>
    </htPROGINFO>
  </OUTDATA>
</CMD>'''

ALARMREPORT = \
'''<?xml version="1.0" encoding="BIG5" standalone="yes"?>
<CMD dt="struct" Sys="MCS_UTIL" CMD="ALARMREPORT">
  <HEADER IP="{IP}" PATH="{QUEUE_NAME}" dt="struct">
    <CLIENT_HOSTNAME dt="String">{CLIENT_HOSTNAME}</CLIENT_HOSTNAME>
    <FUNCTION dt="String">FOUPINFO</FUNCTION>
    <SERVER_NAME dt="String">{CLIENT_HOSTNAME}</SERVER_NAME>
    <IP dt="String">{IP}</IP>
    <DLL_NAME dt="String">ACS</DLL_NAME>
    <FUNCTION_VERSION dt="String">{FUNCTION_VERSION}</FUNCTION_VERSION>
    <CLASSNAME dt="String">Class Name</CLASSNAME>
    <PROCESS_ID dt="String">{PROCESS_ID}</PROCESS_ID>
    <QUEUE_NAME dt="String">{QUEUE_NAME}</QUEUE_NAME>
    <LANG dt="String">zh-TW</LANG>
    <TIMESTAMP dt="String">{TIMESTAMP}</TIMESTAMP>
  </HEADER>
  <DATA dt="struct">
    <strEQCHAR dt="String">{EQCHAR}</strEQCHAR>
    <strALARMID dt="String">{ALARMID}</strALARMID>
    <strEQPID dt="String">{EQPID}</strEQPID>
    <strALARMLEVEL dt="String">{ALARMLEVEL}</strALARMLEVEL>
    <strALARMTYPE dt="String">{ALARMTYPE}</strALARMTYPE>
    <strALARMCODE dt="String">{ALARMCODE}</strALARMCODE>
    <strALARMMSG dt="String">{ALARMMSG}</strALARMMSG>
    <strALARMSYS dt="String">ACS</strALARMSYS>
    <strALARMTIME dt="String">{ALARMTIME}</strALARMTIME>
    <strDEPT dt="String">MF18</strDEPT>
    <strSTAGE dt="String">LE</strSTAGE>
  </DATA>
</CMD>'''