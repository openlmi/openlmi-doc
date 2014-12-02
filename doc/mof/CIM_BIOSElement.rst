.. _CIM-BIOSElement:

CIM_BIOSElement
---------------

Class reference
===============
Subclass of :ref:`CIM_SoftwareElement <CIM-SoftwareElement>`

BIOSElement represents the low-level software that is loaded into non-volatile storage and used to bring up and configure a ComputerSystem.


Key properties
^^^^^^^^^^^^^^

| :ref:`TargetOperatingSystem <CIM-SoftwareElement-TargetOperatingSystem>`
| :ref:`Name <CIM-SoftwareElement-Name>`
| :ref:`SoftwareElementID <CIM-SoftwareElement-SoftwareElementID>`
| :ref:`Version <CIM-SoftwareElement-Version>`
| :ref:`SoftwareElementState <CIM-SoftwareElement-SoftwareElementState>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-BIOSElement-Version:

``string`` **Version**

    Software Version should be in the form <Major>.<Minor>.<Revision> or <Major>.<Minor><letter><revision>.

    
.. _CIM-BIOSElement-ReleaseDate:

``datetime`` **ReleaseDate**

    Date that this BIOS was released.

    
.. _CIM-BIOSElement-Manufacturer:

``string`` **Manufacturer**

    Manufacturer of this SoftwareElement.

    
.. _CIM-BIOSElement-RegistryURIs:

``string[]`` **RegistryURIs**

    A string representing the publication location of the BIOS Attribute registry or registries the implementation complies to.

    
.. _CIM-BIOSElement-ListOfLanguages:

``string[]`` **ListOfLanguages**

    A list of installable languages for the BIOS. This information can be obtained from SMBIOS, from the string list that follows the Type 13 structure. An ISO 639 Language Name should be used to specify the BIOS' installable languages. The ISO 3166 Territory Name and the encoding method may also be specified, following the Language Name.

    
.. _CIM-BIOSElement-LoadedStartingAddress:

``uint64`` **LoadedStartingAddress**

    The starting address of the memory which this BIOS occupies.

    
.. _CIM-BIOSElement-SystemBIOSMinorRelease:

``uint8`` **SystemBIOSMinorRelease**

    Indicates the minor release of the system BIOS, e.g. the value will be 16h for revision 10.22 and 01h for revision 2.1. The value 0xFF denotes the system does not support the use of this field.

    
.. _CIM-BIOSElement-EmbeddedControllerFirmwareMajorRelease:

``uint8`` **EmbeddedControllerFirmwareMajorRelease**

    Indicates the major release of the embedded controller firmware, e.g. the value will be 0Ah for revision 10.22 and 02h for revision 2.1. The value 0xFF denotes the embedded controller firmware is not field-upgradeable.

    
.. _CIM-BIOSElement-CurrentLanguage:

``string`` **CurrentLanguage**

    The currently selected language for the BIOS. This information can be obtained from SMBIOS, using the Current Language attribute of the Type 13 structure, to index into the string list following the structure. The property is formatted using the ISO 639 Language Name, and may be followed by the ISO 3166 Territory Name and the encoding method.

    
.. _CIM-BIOSElement-SystemBIOSMajorRelease:

``uint8`` **SystemBIOSMajorRelease**

    Indicates the major release of the system BIOS, e.g. the value will be 0Ah for revision 10.22 and 02h for revision 2.1. The value 0xFF denotes the system does not support the use of this field.

    
.. _CIM-BIOSElement-PrimaryBIOS:

``boolean`` **PrimaryBIOS**

    If true, this is the primary BIOS of the ComputerSystem.

    
.. _CIM-BIOSElement-LoadedEndingAddress:

``uint64`` **LoadedEndingAddress**

    The ending address of the memory which this BIOS occupies.

    
.. _CIM-BIOSElement-EmbeddedControllerFirmwareMinorRelease:

``uint8`` **EmbeddedControllerFirmwareMinorRelease**

    Indicates the minor release of the embedded controller firmware, e.g. the value will be 16h for revision 10.22 and 01h for revision 2.1. The value 0xFF denotes the embedded controller firmware is not field-upgradeable.

    
.. _CIM-BIOSElement-LoadUtilityInformation:

``string`` **LoadUtilityInformation**

    A free form string describing the BIOS flash/load utility that is required to update the BIOSElement. Version and other information may be indicated in this property.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string`` :ref:`IdentificationCode <CIM-SoftwareElement-IdentificationCode>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`SerialNumber <CIM-SoftwareElement-SerialNumber>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`BuildNumber <CIM-SoftwareElement-BuildNumber>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``uint16`` :ref:`TargetOperatingSystem <CIM-SoftwareElement-TargetOperatingSystem>`
| ``string`` :ref:`Name <CIM-SoftwareElement-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`LanguageEdition <CIM-SoftwareElement-LanguageEdition>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`OtherTargetOS <CIM-SoftwareElement-OtherTargetOS>`
| ``uint16`` :ref:`SoftwareElementState <CIM-SoftwareElement-SoftwareElementState>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`SoftwareElementID <CIM-SoftwareElement-SoftwareElementID>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CodeSet <CIM-SoftwareElement-CodeSet>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

