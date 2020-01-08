# 3GPP Documentation

## Table of contents
* [5G Core Network](#5GCoreNetwork)
  * [AMF (Access and Mobility Management Function)](#AMF)
  * [AUSF (Authentication Server Function)](#AUSF)
  * [BSF (Binding Support Function)](#BSF)
  * [CHF (Charging Function)](#CHF)
  * [NEF (Network Exposure Function)](#NEF)
  * [NRF (NF Repository Function)](#NRF)
  * [NWDAF (Network Data Analytics Function)](#NDAF)
  * [PCF (Policy Control Function)](#PCF)
  * [SMF (Session Management Function)](#SMF)
  * [UDR (Unified Data Repository)](#UDR)
* [Policy and Charging Control](#PCC)
   * [OCS (Online Charging System)](#OCS)
   * [PCRF (Policy and Charging Rule Function)](#PCRF)
   
## 5G Core Network <a name="5GCoreNetwork"></a>
* [TS 23.501 - System Architecture for the 5G System](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2023.501%20-%20System%20Architecture%20for%20the%205G%20System/Rel-15/ts_123501v150700p.pdf)
* [TS 23.502 - Procedures for the 5G System (5GS)](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2023.502%20-%20Procedures%20for%20the%205G%20System%20(5GS)/Rel-15/ts_123502v150700p.pdf)
* [TS 23.503 - Policy and Charging Control Framework for the 5G System](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2023.503%20-%20Policy%20and%20Charging%20Control%20Framework%20for%20the%205G%20System/Rel-15/ts_123503v150700p.pdf)
* [TS 29.501 - Principles and Guidelines for Services Definition](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.501%20-%20Principles%20and%20Guidelines%20for%20Services%20Definition/Rel-15/ts_129501v150500p.pdf)
* [TS 29.571 - Common Data Types for Service Based Interfaces](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.571%20-%20Common%20Data%20Types%20for%20Service%20Based%20Interfaces/Rel-15/ts_129571v150501p.pdf)
* [TS 33.501 - Security architecture and procedures for 5G System](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2033.501%20-%20Security%20architecture%20and%20procedures%20for%205G%20System/Rel-15/ts_133501v150600p.pdf)


###### Common APIs
* [TS 29.571 Common Data Types](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29571_CommonData.yaml)
* [TS 29.122 Common Data Types](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29122_CommonData.yaml)

#### AMF (Access and Mobility Management Function)<a name="AMF"></a>

###### APIs
* [Communication](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29518_Namf_Communication.yaml)
* [Event Exposure](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29518_Namf_EventExposure.yaml)
* [Location](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29518_Namf_Location.yaml)
* [MT](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29518_Namf_MT.yaml)

#### AUSF (Authentication Server Function)<a name="AUSF"></a>
* [TS 29.509 - Authentication Server Services](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.509%20-%20Authentication%20Server%20Services/Rel-15/ts_129509v150501p.pdf)
###### APIs
* [UE Authentication](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29509_Nausf_UEAuthentication.yaml)
* [SoR Protection](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29509_Nausf_SoRProtection.yaml)

#### BSF (Binding Support Function)<a name="BSF"></a>
* [TS 29.521 - Binding Support Management Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.521%20-%20Binding%20Support%20Management%20Service/Rel-15/ts_129521v150500p.pdf)
###### APIs
* [Management](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29521_Nbsf_Management.yaml)

#### CHF (Charging Function) <a name="CHF"></a>
* [TS 29.594 - Spending Limit Control Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.594%20-%20Spending%20Limit%20Control%20Service/Rel-15/ts_129594v150500p.pdf)
###### APIs
* [Spending Limit Control](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29594_Nchf_SpendingLimitControl.yaml)
* [Converged Charging](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS32291_Nchf_ConvergedCharging.yaml)

#### NEF (Network Exposure Function) <a name="NEF"></a>
* [TS 29.551 - 5G System; Packet Flow Description Management Service; Stage 3](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.551%20-%205G%20System;%20Packet%20Flow%20Description%20Management%20Service;%20Stage%203/Rel-15/ts_129551v150500p.pdf)

###### APIs
* [Packet Flow Description (PFD) Management](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29551_Nnef_PFDmanagement.yaml)

#### NRF (NF Repository Function) <a name="NRF"></a>
* [TS 29.510 - Network Function Repository Services](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.510%20-%20Network%20Function%20Repository%20Services/Rel-15/ts_129510v150501p.pdf)

###### APIs
* [NF Management](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29510_Nnrf_NFManagement.yaml)
* [NF Discovery](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29510_Nnrf_NFDiscovery.yaml)
* [Access Token (OAuth2)](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29510_Nnrf_AccessToken.yaml)

#### NWDAF (Network Data Analytics Function) <a name="NDAF"></a>
* [TS 29.520 - Network Data Analytics Services](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.520%20-%20Network%20Data%20Analytics%20Services/Rel-15/ts_129520v150500p.pdf)
###### APIs
* [Events Subscription](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29520_Nnwdaf_EventsSubscription.yaml)
* [Analytics Info](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29520_Nnwdaf_AnalyticsInfo.yaml)

#### PCF (Policy Control Function) <a name="PCF"></a>
* [TS 29.244 - Interface between the Control Plane and the User Plane nodes](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.244%20-%20Interface%20between%20the%20Control%20Plane%20and%20the%20User%20Plane%20nodes/Rel-15/ts_129244v150700p.pdf)
* [TS 29.507 - Access and Mobility Policy Control Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.507%20-%20Access%20and%20Mobility%20Policy%20Control%20Service/Rel-15/ts_129507v150500p.pdf)
* [TS 29.512 - Session Management Policy Control Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.512%20-%20Session%20Management%20Policy%20Control%20Service/Rel-15/ts_129512v150500p.pdf)
* [TS 29.513 - Policy and Charging Control signalling flows and QoS parameter mapping](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.513%20-%20Policy%20and%20Charging%20Control%20signalling%20flows%20and%20QoS%20parameter%20mapping/Rel-15/ts_129513v150500p.pdf)
* [TS 29.514 - Policy Authorization Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.514%20-%20Policy%20Authorization%20Service/Rel-15/ts_129514v150500p.pdf)
* [TS 29.523 - Policy Control Event Exposure Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.523%20-%20Policy%20Control%20Event%20Exposure%20Service/Rel-15/ts_129523v150200p.pdf)
* [TS 29.525 - UE Policy Control Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.525%20-%20UE%20Policy%20Control%20Service/Rel-15/ts_129525v150300p.pdf)
* [TS 29.554 - Background Data Transfer Policy Control Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.554%20-%20Background%20Data%20Transfer%20Policy%20Control%20Service/Rel-15/ts_129554v150400p.pdf)
* [TS 29.594 - Spending Limit Control Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.594%20-%20Spending%20Limit%20Control%20Service/Rel-15/ts_129594v150500p.pdf)
###### APIs
* [Policy Authorization](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29514_Npcf_PolicyAuthorization.yaml)
* [Access and Mobility (AM) Policy Control](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29507_Npcf_AMPolicyControl.yaml)
* [Session Management (SM) Policy Control](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29512_Npcf_SMPolicyControl.yaml)
* [Background Data Transfer (BDT) Policy Control](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29554_Npcf_BDTPolicyControl.yaml)
* [Policy Control Event Exposure Service](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29523_Npcf_EventExposure.yaml)


#### SMF (Session Management Function)<a name="SMF"></a>
* [TS 29.502 - Session Management Services](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.502%20-%20Session%20Management%20Services/Rel-15/ts_129502v150501p.pdf)
* [TS 29.508 - Session Management Event Exposure Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.508%20-%20Session%20Management%20Event%20Exposure%20Service/Rel-15/ts_129508v150500p.pdf)
###### APIs
* [PDU Session](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29502_Nsmf_PDUSession.yaml)
* [Event Exposure](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29508_Nsmf_EventExposure.yaml)

#### UDR (Unified Data Repository) <a name="UDR"></a>
* [TS 29.504 - Unified Data Repository Services](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.504%20-%20Unified%20Data%20Repository%20Services/Rel-15/ts_129504v150501p.pdf)
* [TS 29.519 - Usage of the Unified Data Repository service for Policy Data, Application Data and Structured Data for Exposure](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.519%20-%20Usage%20of%20the%20Unified%20Data%20Repository%20service%20for%20Policy%20Data,%20Application%20Data%20and%20Structured%20Data%20for%20Exposure/Rel-15/ts_129519v150500p.pdf)
###### APIs
* [Data Repository](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29504_Nudr_DataRepository.yaml)
  * [Subscription Data](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29505_Subscription_Data.yaml)
  * [Policy Data](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29519_Policy_Data.yaml)
  * [Exposure Data](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29519_Exposure_Data.yaml)
  * [Application Data](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29519_Application_Data.yaml)

## Policy and Charging Control <a name="PCC"></a>
* [TS 23.179 - Functional architecture and information flows to support mission critical communication services](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2023.179%20-%20LTE%20-%20Functional%20architecture%20and%20information%20flows%20to%20support%20mission%20critical%20communication%20services%20-%20Stage%202/Rel-13/ts_123179v130500p.pdf)
* [TS 23.203 - Policy and charging control architecture](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2023.203%20-%20Policy%20and%20charging%20control%20architecture/Rel-15/ts_123203v150500p.pdf)
* [TS 23.228 - IP Multimedia Subsystem (IMS) - Stage 2](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2023.228%20-%20IP%20Multimedia%20Subsystem%20(IMS)%20-%20Stage%202/Rel-15/ts_123228v150400p.pdf)


#### OCS (Online Charging System) <a name="OCS"></a>
* [TS 29.219 - Policy and charging control: Spending limit reporting over Sy reference point](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.219%20-%20Policy%20and%20charging%20control%20-%20Spending%20limit%20reporting%20over%20Sy%20reference%20point/Rel-15/ts_129219v150300p.pdf)
* [TS 32.260 - IP Multimedia Subsystem (IMS) charging](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2032.260%20-%20IP%20Multimedia%20Subsystem%20(IMS)%20charging/Rel-12/ts_132260v121300p.pdf)
* [TS 32.270 - Multimedia Messaging Service (MMS) charging](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2032.270%20-%20Multimedia%20Messaging%20Service%20(MMS)%20charging/Rel-12/ts_132270v120100p.pdf)
* [TS 32.274 - Short Message Service (SMS) charging](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2032.274%20-%20Short%20Message%20Service%20(SMS)%20charging/Rel-12/ts_132274v120600p.pdf)
* [TS 32.276 - Voice Call Service (VCS) charging](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2032.276%20-%20Voice%20Call%20Service%20(VCS)%20charging/Rel-15/ts_132276v150000p.pdf)
* [TS 32.299 - Diameter charging applications](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2032.299%20-%20Diameter%20charging%20applications/Rel-12/ts_132299v121400p.pdf)

#### PCRF (Policy and Charging Rule Function) <a name="PCRF"></a>
* [TS 29.211 - Rx Interface and Rx-Gx signalling flows](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.211%20-%20Rx%20Interface%20and%20Rx-Gx%20signalling%20flows/Rel-6/ts_129211v060400p.pdf)
* [TS 29.213 - Policy and charging control signalling flows and Quality of Service (QoS) parameter mapping](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.213%20-%20Policy%20and%20charging%20control%20signalling%20flows%20and%20Quality%20of%20Service%20(QoS)%20parameter%20mapping/Rel-15/ts_129213v150600p.pdf)

| Interface  | Standard |
|------------|----------|
| Gx         | [TS 29.212 - Policy and Charging Control (PCC); Reference points](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.212%20-%20Policy%20and%20Charging%20Control%20(PCC);%20Reference%20points/Rel-15/ts_129212v150800p.pdf) |
| Rx         | [TS 29.214 - Policy and charging control over Rx reference point](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.214%20-%20Policy%20and%20charging%20control%20over%20Rx%20reference%20point/Rel-15/ts_129214v150700p.pdf) |
| Sy         | [TS 29.219 - Policy and charging control: Spending limit reporting over Sy reference point](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.219%20-%20Policy%20and%20charging%20control%20-%20Spending%20limit%20reporting%20over%20Sy%20reference%20point/Rel-15/ts_129219v150300p.pdf) |