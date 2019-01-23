# 3GPP Documentation

## Table of contents
* [5G Core Network](#5GCoreNetwork)
  * [AUSF (Authentication Server Function)](#AUSF)
  * [BSF (Binding Support Function)](#BSF)
  * [CHF (Charging Function)](#CHF)
  * [NRF (NF Repository Function)](#NRF)
  * [NWDAF (Network Data Analytics Function)](#NDAF)
  * [PCF (Policy Control Function)](#PCF)
  * [SMF (Session Management Function)](#SMF)
  * [UDR (Unified Data Repository)](#UDR)
* [Policy and Charging Control](#PCC)
   * [OCS (Online Charging System)](#OCS)
   * [PCRF (Policy and Charging Rule Function)](#PCRF)
   
## 5G Core Network <a name="5GCoreNetwork"></a>
* [TS 23.501 - System Architecture for the 5G System](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2023.501%20-%20System%20Architecture%20for%20the%205G%20System)
* [TS 23.502 - Procedures for the 5G System (5GS)](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2023.502%20-%20Procedures%20for%20the%205G%20System%20(5GS))
* [TS 23.503 - Policy and Charging Control Framework for the 5G System](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2023.503%20-%20Policy%20and%20Charging%20Control%20Framework%20for%20the%205G%20System)
* [TS 29.501 - Principles and Guidelines for Services Definition](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.501%20-%20Principles%20and%20Guidelines%20for%20Services%20Definition)
* [TS 29.571 - Common Data Types for Service Based Interfaces](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.571%20-%20Common%20Data%20Types%20for%20Service%20Based%20Interfaces)

###### Common APIs
* [Common Data Types](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29571_CommonData.yaml)
* [Common Data](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29122_CommonData.yaml)

#### AUSF (Authentication Server Function)
* [TS 29.509 - Authentication Server Services](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.509%20-%20Authentication%20Server%20Services)
###### APIs
* [UE Authentication](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29509_Nausf_UEAuthentication.yaml)
* [SoR Protection](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29509_Nausf_SoRProtection.yaml)

#### BSF (Binding Support Function)<a name="BSF"></a>
* [TS 29.521 - Binding Support Management Service](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.521%20-%20Binding%20Support%20Management%20Service)
###### APIs
* [Management](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29521_Nbsf_Management.yaml)

#### CHF (Charging Function) <a name="CHF"></a>
* [TS 29.594 - Spending Limit Control Service](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.594%20-%20Spending%20Limit%20Control%20Service)
###### APIs
* [Spending Limit Control](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29594_Nchf_SpendingLimitControl.yaml)
* [Converged Charging](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS32291_Nchf_ConvergedCharging.yaml)

#### NRF (NF Repository Function) <a name="NRF"></a>
* [TS 29.510 - Network Function Repository Services](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.510%20-%20Network%20Function%20Repository%20Services)

###### APIs
* [NF Management](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29510_Nnrf_NFManagement.yaml)
* [NF Discovery](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29510_Nnrf_NFDiscovery.yaml)
* [Access Token (OAuth2)](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29510_Nnrf_AccessToken.yaml)

#### NWDAF (Network Data Analytics Function) <a name="NDAF"></a>
* [TS 29.520 - Network Data Analytics Services](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.520%20-%20Network%20Data%20Analytics%20Services)
###### APIs
* [Events Subscription](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29520_Nnwdaf_EventsSubscription.yaml)
* [Analytics Info](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29520_Nnwdaf_AnalyticsInfo.yaml)

#### PCF (Policy Control Function) <a name="PCF"></a>
* [TS 29.507 - Access and Mobility Policy Control Service](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.507%20-%20Access%20and%20Mobility%20Policy%20Control%20Service)
* [TS 29.512 - Session Management Policy Control Service](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.512%20-%20Session%20Management%20Policy%20Control%20Service)
* [TS 29.513 - Policy and Charging Control signalling flows and QoS parameter mapping](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.513%20-%20Policy%20and%20Charging%20Control%20signalling%20flows%20and%20QoS%20parameter%20mapping)
* [TS 29.514 - Policy Authorization Service](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.514%20-%20Policy%20Authorization%20Service)
* [TS 29.523 - Policy Control Event Exposure Service](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.523%20-%20Policy%20Control%20Event%20Exposure%20Service)
* [TS 29.525 - UE Policy Control Service](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.525%20-%20UE%20Policy%20Control%20Service)
* [TS 29.554 - Background Data Transfer Policy Control Service](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.554%20-%20Background%20Data%20Transfer%20Policy%20Control%20Service)
* [TS 29.594 - Spending Limit Control Service](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.594%20-%20Spending%20Limit%20Control%20Service)
###### APIs
* [Policy Authorization](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29514_Npcf_PolicyAuthorization.yaml)
* [Access and Mobility (AM) Policy Control](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29507_Npcf_AMPolicyControl.yaml)
* [Session Management (SM) Policy Control](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29512_Npcf_SMPolicyControl.yaml)
* [Background Data Transfer (BDT) Policy Control](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29554_Npcf_BDTPolicyControl.yaml)

#### SMF (Session Management Function)<a name="SMF"></a>
* [TS 29.502 - Session Management Services](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.502%20-%20Session%20Management%20Services)
* [TS 29.508 - Session Management Event Exposure Service](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.508%20-%20Session%20Management%20Event%20Exposure%20Service)
###### APIs
* [PDU Session](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29502_Nsmf_PDUSession.yaml)
* [Event Exposure](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29508_Nsmf_EventExposure.yaml)

#### UDR (Unified Data Repository) <a name="UDR"></a>
* [TS 29.504 - Unified Data Repository Services](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.504%20-%20Unified%20Data%20Repository%20Services)
* [TS 29.519 - Usage of the Unified Data Repository service for Policy Data, Application Data and Structured Data for Exposure](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.519%20-%20Usage%20of%20the%20Unified%20Data%20Repository%20service%20for%20Policy%20Data%2C%20Application%20Data%20and%20Structured%20Data%20for%20Exposure)
###### APIs
* [Data Repository](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29504_Nudr_DataRepository.yaml)
  * [Subscription Data](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29505_Subscription_Data.yaml)
  * [Policy Data](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29519_Policy_Data.yaml)
  * [Exposure Data](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29519_Exposure_Data.yaml)
  * [Application Data](https://editor.swagger.io/?url=https://raw.githubusercontent.com/jdegre/5GC_APIs/master/TS29519_Application_Data.yaml)

## Policy and Charging Control <a name="PCC"></a>
* [TS 23.203 - Policy and charging control architecture](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2023.203%20-%20Policy%20and%20charging%20control%20architecture)
* [TS 29.212 - Policy and Charging Control (PCC); Reference points](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.212%20-%20Policy%20and%20Charging%20Control%20(PCC)%3B%20Reference%20points)

#### OCS (Online Charging System) <a name="OCS"></a>
* [TS 29.219 - Policy and charging control: Spending limit reporting over Sy reference point](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.219%20-%20Policy%20and%20charging%20control%20-%20Spending%20limit%20reporting%20over%20Sy%20reference%20point)
* [TS 32.260 - IP Multimedia Subsystem (IMS) charging](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2032.260%20-%20IP%20Multimedia%20Subsystem%20(IMS)%20charging)
* [TS 32.270 - Multimedia Messaging Service (MMS) charging](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2032.270%20-%20Multimedia%20Messaging%20Service%20(MMS)%20charging)
* [TS 32.274 - Short Message Service (SMS) charging](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2032.274%20-%20Short%20Message%20Service%20(SMS)%20charging)
* [TS 32.276 - Voice Call Service (VCS) charging](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2032.276%20-%20Voice%20Call%20Service%20(VCS)%20charging)
* [TS 32.299 - Diameter charging applications](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2032.299%20-%20Diameter%20charging%20applications)

#### PCRF (Policy and Charging Rule Function) <a name="PCRF"></a>
* [TS 29.211 - Rx Interface and Rx-Gx signalling flows](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.211%20-%20Rx%20Interface%20and%20Rx-Gx%20signalling%20flows)
* [TS 29.213 - Policy and charging control signalling flows and Quality of Service (QoS) parameter mapping](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.213%20-%20Policy%20and%20charging%20control%20signalling%20flows%20and%20Quality%20of%20Service%20(QoS)%20parameter%20mapping)
* [TS 29.214 - Policy and charging control over Rx reference point](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.214%20-%20Policy%20and%20charging%20control%20over%20Rx%20reference%20point)
* [TS 29.219 - Policy and charging control: Spending limit reporting over Sy reference point](https://github.com/emanuelfreitas/3gpp-documentation/tree/master/documentation/TS%2029.219%20-%20Policy%20and%20charging%20control%20-%20Spending%20limit%20reporting%20over%20Sy%20reference%20point)

