.. _CIM-FileSpecification:

CIM_FileSpecification
---------------------

Class reference
===============
Subclass of :ref:`CIM_Check <CIM-Check>`

FileSpecification identifies a file that is either to be on or off the system. The file is to be located in the directory identified in FileName, or by the CIM_Directory SpecificationFile association. When the Invoke methods are executed, it is expected that they will use a combination of information to check for file existence. Therefore, any of the properties with a NULL value are not checked. So, if only the FileName and MD5Checksum properties have values, they are the only ones considered by the Invoke methods.


Key properties
^^^^^^^^^^^^^^

| :ref:`CheckID <CIM-Check-CheckID>`
| :ref:`TargetOperatingSystem <CIM-Check-TargetOperatingSystem>`
| :ref:`Name <CIM-Check-Name>`
| :ref:`SoftwareElementID <CIM-Check-SoftwareElementID>`
| :ref:`Version <CIM-Check-Version>`
| :ref:`SoftwareElementState <CIM-Check-SoftwareElementState>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-FileSpecification-CRC2:

``uint32`` **CRC2**

    The CRC2 property is the CRC value for the middle 512K bytes of the file, modulo 3.

    
.. _CIM-FileSpecification-CRC1:

``uint32`` **CRC1**

    The CRC1 property is the CRC value calculated using the middle 512K bytes of the file.

    
.. _CIM-FileSpecification-CheckSum:

``uint32`` **CheckSum**

    A checksum calculated as the 16-bit sum of the first 32 bytes of the file.

    
.. _CIM-FileSpecification-FileName:

``string`` **FileName**

    Either the name of the file or the name of the file with a directory prefix.

    
.. _CIM-FileSpecification-CreateTimeStamp:

``datetime`` **CreateTimeStamp**

    The creation date and time of the file.

    
.. _CIM-FileSpecification-FileSize:

``uint64`` **FileSize**

    The size of the file in Kilobytes.

    
.. _CIM-FileSpecification-MD5Checksum:

``string`` **MD5Checksum**

    The MD5 algorithm is a well-known algorithm for computing a 128-bit checksum for any file or object. For purposes of MOF specification of the MD5Checksum property, the MD5 algorithm always generates a 32 character string. For example: The string abcdefghijklmnopqrstuvwxyz generates the string c3fcd3d76192e4007dfb496cca67e13b. See http: //www.ietf.org - RFC1321 for details on the // implementation of the MD5 algorithm.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`CheckID <CIM-Check-CheckID>`
| ``uint16`` :ref:`TargetOperatingSystem <CIM-Check-TargetOperatingSystem>`
| ``string`` :ref:`Version <CIM-Check-Version>`
| ``string`` :ref:`Name <CIM-Check-Name>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``boolean`` :ref:`CheckMode <CIM-Check-CheckMode>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`SoftwareElementID <CIM-Check-SoftwareElementID>`
| ``uint16`` :ref:`SoftwareElementState <CIM-Check-SoftwareElementState>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`Invoke <CIM-Check-Invoke>`
| :ref:`InvokeOnSystem <CIM-Check-InvokeOnSystem>`

