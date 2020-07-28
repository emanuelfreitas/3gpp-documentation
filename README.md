# 3GPP Documentation

## Table of contents
* [5G Core Network](#5GCoreNetwork)
  * [Architecture](#5GArchitecture)
  * [Reference Points](#5GReferencePoints)
  * [Services](#5GServices)
  * [Network Functions and entities](#5GNetworkFunctions)
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
* [TS 23.501 - System Architecture for the 5G System](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2023.501%20-%20System%20Architecture%20for%20the%205G%20System/Rel-15/ts_123501v151000p.pdf)
* [TS 23.502 - Procedures for the 5G System (5GS)](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2023.502%20-%20Procedures%20for%20the%205G%20System%20(5GS)/Rel-15/ts_123502v151000p.pdf)
* [TS 23.503 - Policy and Charging Control Framework for the 5G System](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2023.503%20-%20Policy%20and%20Charging%20Control%20Framework%20for%20the%205G%20System/Rel-15/ts_123503v150800p.pdf)
* [TS 29.501 - Principles and Guidelines for Services Definition](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.501%20-%20Principles%20and%20Guidelines%20for%20Services%20Definition/Rel-15/ts_129501v150700p.pdf)
* [TS 29.571 - Common Data Types for Service Based Interfaces](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.571%20-%20Common%20Data%20Types%20for%20Service%20Based%20Interfaces/Rel-15/ts_129571v150600p.pdf)
* [TS 33.501 - Security architecture and procedures for 5G System](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2033.501%20-%20Security%20architecture%20and%20procedures%20for%205G%20System/Rel-15/ts_133501v150800p.pdf)

###### Common APIs
* [TS 29.571 Common Data Types](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29571_CommonData.yaml)
* [TS 29.122 Common Data Types](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29122_CommonData.yaml)

### Architecture <a name="5GArchitecture"></a>
#### 5G System architecture
![5G System architecture](https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/documentation/images/5G%20System%20architecture.png "5G System architecture")

#### PCF/CHF Interfaces
![PCF Interfaces](https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/documentation/images/PCF%20Interfaces.png "PCF Interfaces")

### Reference points <a name="5GReferencePoints"></a>
| Interface | Description |
|:---------:|:------------|
| N1 | Reference point between the UE and the AMF |
| N2 | Reference point between the (R)AN and the AMF |
| N3 | Reference point between the (R)AN and the UPF |
| N4 | Reference point between the SMF and the UPF |
| **N5** | Reference point between the PCF and an AF |
| N6 | Reference point between the UPF and a Data Network |
| **N7** | Reference point between the SMF and the PCF |
| N8 | Reference point between the UDM and the AMF |
| N9 | Reference point between two UPFs |
| N10 | Reference point between the UDM and the SMF |
| N11 | Reference point between the AMF and the SMF |
| N12 | Reference point between AMF and AUSF |
| N13 | Reference point between the UDM and Authentication Server function the AUSF |
| N14 | Reference point between two AMFs |
| **N15** | Reference point between the PCF and the AMF in the case of non-roaming scenario, PCF in the visited network and AMF in the case of roaming scenario |
| N16 | Reference point between two SMFs (in roaming case between SMF in the visited network and the SMF in the home network) |
| N17 | Reference point between AMF and 5G-EIR |
| N18 | Reference point between any NF and UDSF |
| N22 | Reference point between AMF and NSSF |
| **N23** | Reference point between PCF and NWDAF |
| **N24** | Reference point between the PCF in the visited network and the PCF in the home network |
| N27 | Reference point between NRF in the visited network and the NRF in the home network |
| **N28** | Reference point between PCF and OCS |
| N31 | Reference point between the NSSF in the visited network and the NSSF in the home network |
| N32 | Reference point between SEPP in the visited network and the SEPP in the home network |
| N33 | Reference point between NEF and AF |
| N34 | Reference point between NSSF and NWDAF |
| N35 | Reference point between UDM and UDR |
| **N36** | Reference point between PCF and UDR |
| N37 | Reference point between NEF and UDR |
| **N40** | Reference point between SMF and the CHF |
| N50 | Reference point between AMF and the CBCF | 

### Services <a name="5GServices"></a>
| Producer | Consumer | Service | Standard | API |
|:--------:|:--------:|:--------|:--------:|:----|
| [PCF](#PCF)     | AF           | Npcf_PolicyAuthorization  | [TS 29.514](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.514%20-%20Policy%20Authorization%20Service/Rel-15/ts_129514v150600p.pdf) | [PCF Policy Authorization Service](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29514_Npcf_PolicyAuthorization.yaml) |
|                 | SMF          | Npcf_SMPolicyControl      | [TS 29.512](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.512%20-%20Session%20Management%20Policy%20Control%20Service/Rel-15/ts_129512v150600p.pdf) | [Session Management Policy Control Service](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29512_Npcf_SMPolicyControl.yaml) |
|                 | AMF          | Npcf_AMPolicyControl      | [TS 29.507](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.507%20-%20Access%20and%20Mobility%20Policy%20Control%20Service/Rel-15/ts_129507v150600p.pdf) | [Access and Mobility Policy Control Service](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29507_Npcf_AMPolicyControl.yaml) |
|                 | NEF          | Npcf_EventExposure        | [TS 29.523](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.523%20-%20Policy%20Control%20Event%20Exposure%20Service/Rel-15/ts_129523v150200p.pdf) | [PCF Event Exposure Service](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29523_Npcf_EventExposure.yaml) |
|                 |              | Npcf_BDTPolicyControl     | [TS 29.554](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.554%20-%20Background%20Data%20Transfer%20Policy%20Control%20Service/Rel-15/ts_129554v150400p.pdf) | [PCF BDT Policy Control Service](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29554_Npcf_BDTPolicyControl.yaml) |
| [NWDAF](#NWDAF) | PCF          | Nnwdaf_EventsSubscription | [TS 29.520](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.520%20-%20Network%20Data%20Analytics%20Services/Rel-15/ts_129520v150500p.pdf) | [Nnwdaf_EventsSubscription Service API](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29520_Nnwdaf_EventsSubscription.yaml) |
|                 |              | Nnwdaf_AnalyticsInfo      | [TS 29.520](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.520%20-%20Network%20Data%20Analytics%20Services/Rel-15/ts_129520v150500p.pdf) | [Nnwdaf_AnalyticsInfo Service API](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29520_Nnwdaf_AnalyticsInfo.yaml) |
| [CHF](#CHF)     | PCF          | Nchf_SpendingLimitControl | [TS 29.594](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.594%20-%20Spending%20Limit%20Control%20Service/Rel-15/ts_129594v150500p.pdf) | [Spending Limit Control](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29594_Nchf_SpendingLimitControl.yaml) |
|                 | SMF, SMSF    | Nchf_ConvergedCharging    | [TS 32.291](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2032.291%20-%205G%20system,%20charging%20service;%20Stage%203/Rel-15/ts_132291v150500p.pdf) | [Converged Charging](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS32291_Nchf_ConvergedCharging.yaml) |
| [UDR](#UDR)     | PCF          | Nudr_DataRepository       | [TS 29.504](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.504%20-%20Unified%20Data%20Repository%20Services/Rel-15/ts_129504v150600p.pdf) | [Unified Data Repository Service](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29504_Nudr_DataRepository.yaml) |
| [BSF](#BSF)     | PCF, NEF, AF | Nbsf_Management           | [TS 32.521]() | [Binding Support Management Service API](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29521_Nbsf_Management.yaml) |
| [NRF](#NRF)     | ALL NF       | Nnrf_NFManagement         | [TS 29.510](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.510%20-%20Network%20Function%20Repository%20Services/Rel-15/ts_129510v150700p.pdf) | [NRF NFManagement Service](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29510_Nnrf_NFManagement.yaml) |
|                 |              | Nnrf_NFDiscovery          | [TS 29.510](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.510%20-%20Network%20Function%20Repository%20Services/Rel-15/ts_129510v150700p.pdf) | [NRF NFDiscovery Service](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29510_Nnrf_NFDiscovery.yaml) |
|                 |              | Nnrf_AccessToken          | [TS 29.510](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.510%20-%20Network%20Function%20Repository%20Services/Rel-15/ts_129510v150700p.pdf) | [NRF OAuth2 Authorization](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29510_Nnrf_AccessToken.yaml) |

### Network Functions and entities  <a name="5GNetworkFunctions"></a>

#### AMF (Access and Mobility Management Function)<a name="AMF"></a>

###### APIs
* [Communication](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29518_Namf_Communication.yaml)
* [Event Exposure](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29518_Namf_EventExposure.yaml)
* [Location](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29518_Namf_Location.yaml)
* [MT](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29518_Namf_MT.yaml)

#### AUSF (Authentication Server Function)<a name="AUSF"></a>
* [TS 29.509 - Authentication Server Services](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.509%20-%20Authentication%20Server%20Services/Rel-15/ts_129509v150501p.pdf)
###### APIs
* [UE Authentication](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29509_Nausf_UEAuthentication.yaml)
* [SoR Protection](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29509_Nausf_SoRProtection.yaml)

#### BSF (Binding Support Function)<a name="BSF"></a>
* [TS 29.521 - Binding Support Management Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.521%20-%20Binding%20Support%20Management%20Service/Rel-15/ts_129521v150500p.pdf)

#### CHF (Charging Function) <a name="CHF"></a>
* [TS 29.594 - Spending Limit Control Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.594%20-%20Spending%20Limit%20Control%20Service/Rel-15/ts_129594v150500p.pdf)
* [TS 32.240 - Telecommunication management; Charging management; Charging architecture and principles](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2032.240%20-%20Charging%20architecture%20and%20principles/Rel-15/ts_132240v150500p.pdf)
* [TS 32.290 - Telecommunication management; Charging management; 5G system; Services, operations and procedures of charging using Service Based Interface (SBI)](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2032.290%20-%20Services,%20operations%20and%20procedures%20of%20charging%20using%20Service%20Based%20Interface%20(SBI)/Rel-15/ts_132290v150600p.pdf)
* [TS 32.291 - 5G system, charging service; Stage 3](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2032.291%20-%205G%20system,%20charging%20service;%20Stage%203/Rel-15/ts_132291v150500p.pdf)

#### NEF (Network Exposure Function) <a name="NEF"></a>
* [TS 29.551 - 5G System; Packet Flow Description Management Service; Stage 3](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.551%20-%205G%20System;%20Packet%20Flow%20Description%20Management%20Service;%20Stage%203/Rel-15/ts_129551v150500p.pdf)

###### APIs
* [Packet Flow Description (PFD) Management](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29551_Nnef_PFDmanagement.yaml)

#### NRF (NF Repository Function) <a name="NRF"></a>
* [TS 29.510 - Network Function Repository Services](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.510%20-%20Network%20Function%20Repository%20Services/Rel-15/ts_129510v150700p.pdf)

#### NWDAF (Network Data Analytics Function) <a name="NDAF"></a>
* [TS 29.520 - Network Data Analytics Services](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.520%20-%20Network%20Data%20Analytics%20Services/Rel-15/ts_129520v150500p.pdf)

#### PCF (Policy Control Function) <a name="PCF"></a>
* [TS 29.244 - Interface between the Control Plane and the User Plane nodes](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.244%20-%20Interface%20between%20the%20Control%20Plane%20and%20the%20User%20Plane%20nodes/Rel-15/ts_129244v150800p.pdf)
* [TS 29.507 - Access and Mobility Policy Control Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.507%20-%20Access%20and%20Mobility%20Policy%20Control%20Service/Rel-15/ts_129507v150600p.pdf)
* [TS 29.512 - Session Management Policy Control Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.512%20-%20Session%20Management%20Policy%20Control%20Service/Rel-15/ts_129512v150600p.pdf)
* [TS 29.513 - Policy and Charging Control signalling flows and QoS parameter mapping](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.513%20-%20Policy%20and%20Charging%20Control%20signalling%20flows%20and%20QoS%20parameter%20mapping/Rel-15/ts_129513v150600p.pdf)
* [TS 29.514 - Policy Authorization Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.514%20-%20Policy%20Authorization%20Service/Rel-15/ts_129514v150600p.pdf)
* [TS 29.523 - Policy Control Event Exposure Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.523%20-%20Policy%20Control%20Event%20Exposure%20Service/Rel-15/ts_129523v150200p.pdf)
* [TS 29.525 - UE Policy Control Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.525%20-%20UE%20Policy%20Control%20Service/Rel-15/ts_129525v150400p.pdf)
* [TS 29.554 - Background Data Transfer Policy Control Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.554%20-%20Background%20Data%20Transfer%20Policy%20Control%20Service/Rel-15/ts_129554v150400p.pdf)
* [TS 29.594 - Spending Limit Control Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.594%20-%20Spending%20Limit%20Control%20Service/Rel-15/ts_129594v150500p.pdf)

#### SMF (Session Management Function)<a name="SMF"></a>
* [TS 29.502 - Session Management Services](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.502%20-%20Session%20Management%20Services/Rel-15/ts_129502v150800p.pdf)
* [TS 29.508 - Session Management Event Exposure Service](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.508%20-%20Session%20Management%20Event%20Exposure%20Service/Rel-15/ts_129508v150600p.pdf)
###### APIs
* [PDU Session](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29502_Nsmf_PDUSession.yaml)
* [Event Exposure](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29508_Nsmf_EventExposure.yaml)

#### UDR (Unified Data Repository) <a name="UDR"></a>
* [TS 29.504 - Unified Data Repository Services](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.504%20-%20Unified%20Data%20Repository%20Services/Rel-15/ts_129504v150600p.pdf)
* [TS 29.519 - Usage of the Unified Data Repository service for Policy Data, Application Data and Structured Data for Exposure](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.519%20-%20Usage%20of%20the%20Unified%20Data%20Repository%20service%20for%20Policy%20Data,%20Application%20Data%20and%20Structured%20Data%20for%20Exposure/Rel-15/ts_129519v150600p.pdf)
###### APIs
* Data Repository
  * [Subscription Data](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29505_Subscription_Data.yaml)
  * [Policy Data](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29519_Policy_Data.yaml)
  * [Exposure Data](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29519_Exposure_Data.yaml)
  * [Application Data](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29519_Application_Data.yaml)

## Policy and Charging Control <a name="PCC"></a>
* [RFC 6733 - Diameter Base Protocol](https://tools.ietf.org/pdf/rfc6733.pdf)
* [RFC 8506 - Diameter Credit-Control Application](https://tools.ietf.org/pdf/rfc8506.pdf)
* [TS 23.167 - IP Multimedia Subsystem (IMS) emergency sessions](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2023.167%20-%20IP%20Multimedia%20Subsystem%20(IMS)%20emergency%20sessions/Rel-15/ts_123167v150700p.pdf)
* [TS 23.179 - Functional architecture and information flows to support mission critical communication services]()
* [TS 23.203 - Policy and charging control architecture](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2023.203%20-%20Policy%20and%20charging%20control%20architecture/Rel-15/ts_123203v150500p.pdf)
* [TS 23.228 - IP Multimedia Subsystem (IMS) - Stage 2](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2023.228%20-%20IP%20Multimedia%20Subsystem%20(IMS)%20-%20Stage%202/Rel-15/ts_123228v150400p.pdf)
* [TS 23.401 - General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2023.401%20-%20General%20Packet%20Radio%20Service%20(GPRS)%20enhancements%20for%20Evolved%20Universal%20Terrestrial%20Radio%20Access%20Network%20(E-UTRAN)%20access/Rel-15/ts_123401v151100p.pdf)

* [VoLTE Service Description and Implementation Guidelines](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/GSMA/VoLTE%20Service%20Description%20and%20Implementation%20Guidelines.pdf)

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
* [TS 23.380 - IMS Restoration Procedures](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2023.380%20-%20IMS%20Restoration%20Procedures/Rel-15/ts_123380v150200p.pdf)

| Interface  | Standard |
|------------|----------|
| Gx         | [TS 29.212 - Policy and Charging Control (PCC); Reference points](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.212%20-%20Policy%20and%20Charging%20Control%20(PCC);%20Reference%20points/Rel-15/ts_129212v150900p.pdf) |
| Rx         | [TS 29.214 - Policy and charging control over Rx reference point](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.214%20-%20Policy%20and%20charging%20control%20over%20Rx%20reference%20point/Rel-15/ts_129214v150700p.pdf) |
| Sy         | [TS 29.219 - Policy and charging control: Spending limit reporting over Sy reference point](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2029.219%20-%20Policy%20and%20charging%20control%20-%20Spending%20limit%20reporting%20over%20Sy%20reference%20point/Rel-15/ts_129219v150300p.pdf) |