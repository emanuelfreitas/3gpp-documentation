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
* [TS 23.501 - System Architecture for the 5G System]()
* [TS 23.502 - Procedures for the 5G System (5GS)]()
* [TS 23.503 - Policy and Charging Control Framework for the 5G System]()
* [TS 29.501 - Principles and Guidelines for Services Definition]()
* [TS 29.571 - Common Data Types for Service Based Interfaces]()
* [TS 33.501 - Security architecture and procedures for 5G System]()

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
| [PCF](#PCF)     | AF           | Npcf_PolicyAuthorization  | [TS 29.514]() | [PCF Policy Authorization Service](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29514_Npcf_PolicyAuthorization.yaml) |
|                 | SMF          | Npcf_SMPolicyControl      | [TS 29.512]() | [Session Management Policy Control Service](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29512_Npcf_SMPolicyControl.yaml) |
|                 | AMF          | Npcf_AMPolicyControl      | [TS 29.507]() | [Access and Mobility Policy Control Service](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29507_Npcf_AMPolicyControl.yaml) |
|                 | NEF          | Npcf_EventExposure        | [TS 29.523]() | [PCF Event Exposure Service](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29523_Npcf_EventExposure.yaml) |
|                 |              | Npcf_BDTPolicyControl     | [TS 29.554]() | [PCF BDT Policy Control Service](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29554_Npcf_BDTPolicyControl.yaml) |
| [NWDAF](#NWDAF) | PCF          | Nnwdaf_EventsSubscription | [TS 29.520]() | [Nnwdaf_EventsSubscription Service API](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29520_Nnwdaf_EventsSubscription.yaml) |
|                 |              | Nnwdaf_AnalyticsInfo      | [TS 29.520]() | [Nnwdaf_AnalyticsInfo Service API](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29520_Nnwdaf_AnalyticsInfo.yaml) |
| [CHF](#CHF)     | PCF          | Nchf_SpendingLimitControl | [TS 29.594]() | [Spending Limit Control](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29594_Nchf_SpendingLimitControl.yaml) |
|                 | NF           | Nchf_ConvergedCharging    | [TS 32.291]() | [Converged Charging](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS32291_Nchf_ConvergedCharging.yaml) |
|                 | NF           | Nchf_OfflineOnlyCharging  | [TS 32.291]() | [Offline Only Charging](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS32291_Nchf_OfflineOnlyCharging.yaml) |
| [UDR](#UDR)     | PCF          | Nudr_DataRepository       | [TS 29.504]() | [Unified Data Repository Service]() |
| [BSF](#BSF)     | PCF, NEF, AF | Nbsf_Management           | [TS 32.521]() | [Binding Support Management Service API](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29521_Nbsf_Management.yaml) |
| [NRF](#NRF)     | ALL NF       | Nnrf_NFManagement         | [TS 29.510]() | [NRF NFManagement Service](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29510_Nnrf_NFManagement.yaml) |
|                 |              | Nnrf_NFDiscovery          | [TS 29.510]() | [NRF NFDiscovery Service](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29510_Nnrf_NFDiscovery.yaml) |
|                 |              | Nnrf_AccessToken          | [TS 29.510]() | [NRF OAuth2 Authorization](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29510_Nnrf_AccessToken.yaml) |

### Network Functions and entities  <a name="5GNetworkFunctions"></a>

#### AMF (Access and Mobility Management Function)<a name="AMF"></a>

###### APIs
* [Communication](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29518_Namf_Communication.yaml)
* [Event Exposure](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29518_Namf_EventExposure.yaml)
* [Location](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29518_Namf_Location.yaml)
* [MT](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29518_Namf_MT.yaml)

#### AUSF (Authentication Server Function)<a name="AUSF"></a>
* [TS 29.509 - Authentication Server Services]()
###### APIs
* [UE Authentication](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29509_Nausf_UEAuthentication.yaml)
* [SoR Protection](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29509_Nausf_SoRProtection.yaml)

#### BSF (Binding Support Function)<a name="BSF"></a>
* [TS 29.521 - Binding Support Management Service]()

#### CHF (Charging Function) <a name="CHF"></a>
* [TS 29.594 - Spending Limit Control Service]()
* [TS 32.240 - Telecommunication management; Charging management; Charging architecture and principles]()
* [TS 32.255 - Telecommunication management; Charging management; 5G data connectivity domain charging; Stage 2]()
* [TS 32.290 - Telecommunication management; Charging management; 5G system; Services, operations and procedures of charging using Service Based Interface (SBI)]()
* [TS 32.291 - 5G system, charging service; Stage 3]()

#### NEF (Network Exposure Function) <a name="NEF"></a>
* [TS 29.551 - 5G System; Packet Flow Description Management Service; Stage 3]()

###### APIs
* [Packet Flow Description (PFD) Management](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29551_Nnef_PFDmanagement.yaml)

#### NRF (NF Repository Function) <a name="NRF"></a>
* [TS 29.510 - Network Function Repository Services]()

#### NWDAF (Network Data Analytics Function) <a name="NDAF"></a>
* [TS 29.520 - Network Data Analytics Services]()

#### PCF (Policy Control Function) <a name="PCF"></a>
* [TS 29.244 - Interface between the Control Plane and the User Plane nodes]()
* [TS 29.507 - Access and Mobility Policy Control Service]()
* [TS 29.512 - Session Management Policy Control Service]()
* [TS 29.513 - Policy and Charging Control signalling flows and QoS parameter mapping]()
* [TS 29.514 - Policy Authorization Service]()
* [TS 29.523 - Policy Control Event Exposure Service]()
* [TS 29.525 - UE Policy Control Service]()
* [TS 29.554 - Background Data Transfer Policy Control Service]()
* [TS 29.594 - Spending Limit Control Service]()

#### SMF (Session Management Function)<a name="SMF"></a>
* [TS 29.502 - Session Management Services]()
* [TS 29.508 - Session Management Event Exposure Service]()
###### APIs
* [PDU Session](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29502_Nsmf_PDUSession.yaml)
* [Event Exposure](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29508_Nsmf_EventExposure.yaml)

#### UDR (Unified Data Repository) <a name="UDR"></a>
* [TS 29.504 - Unified Data Repository Services]()
* [TS 29.519 - Usage of the Unified Data Repository service for Policy Data, Application Data and Structured Data for Exposure]()
###### APIs
* Data Repository
  * [Subscription Data](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29505_Subscription_Data.yaml)
  * [Policy Data](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29519_Policy_Data.yaml)
  * [Exposure Data](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29519_Exposure_Data.yaml)
  * [Application Data](https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS29519_Application_Data.yaml)

## Policy and Charging Control <a name="PCC"></a>
* [RFC 6733 - Diameter Base Protocol](https://tools.ietf.org/pdf/rfc6733.pdf)
* [RFC 8506 - Diameter Credit-Control Application](https://tools.ietf.org/pdf/rfc8506.pdf)
* [TS 23.167 - IP Multimedia Subsystem (IMS) emergency sessions](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/TS%2023.167%20-%20IP%20Multimedia%20Subsystem%20(IMS)%20emergency%20sessions/Rel-17/ts_123167v170200p.pdf)
* [TS 23.179 - Functional architecture and information flows to support mission critical communication services]()
* [TS 23.203 - Policy and charging control architecture]()
* [TS 23.228 - IP Multimedia Subsystem (IMS) - Stage 2]()
* [TS 23.401 - General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access]()

* [VoLTE Service Description and Implementation Guidelines](https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/GSMA/VoLTE%20Service%20Description%20and%20Implementation%20Guidelines.pdf)

#### OCS (Online Charging System) <a name="OCS"></a>
* [TS 29.219 - Policy and charging control: Spending limit reporting over Sy reference point]()
* [TS 32.240 - Telecommunication management; Charging management; Charging architecture and principles]()
* [TS 32.251 - Telecommunication management;Charging management;Packet Switched (PS) domain charging]()
* [TS 32.260 - IP Multimedia Subsystem (IMS) charging]()
* [TS 32.270 - Multimedia Messaging Service (MMS) charging]()
* [TS 32.274 - Short Message Service (SMS) charging]()
* [TS 32.276 - Voice Call Service (VCS) charging]()
* [TS 32.296 - Telecommunication management; Charging management; Online Charging System (OCS): Applications and interfaces]()
* [TS 32.299 - Diameter charging applications]()

| Interface  | Standard |
|------------|----------|
| Sy         | [TS 29.219 - Policy and charging control: Spending limit reporting over Sy reference point]() |
| Ro - Gy    | [TS 32.251 - Telecommunication management;Charging management;Packet Switched (PS) domain charging]() |
| Ro / Rf    | [TS 32.299 - Diameter charging applications]() |

#### PCRF (Policy and Charging Rule Function) <a name="PCRF"></a>
* [TS 29.211 - Rx Interface and Rx-Gx signalling flows]()
* [TS 29.213 - Policy and charging control signalling flows and Quality of Service (QoS) parameter mapping]()
* [TS 23.380 - IMS Restoration Procedures]()

| Interface  | Standard |
|------------|----------|
| Gx         | [TS 29.212 - Policy and Charging Control (PCC); Reference points]() |
| Rx         | [TS 29.214 - Policy and charging control over Rx reference point]() |
| Sy         | [TS 29.219 - Policy and charging control: Spending limit reporting over Sy reference point]() |