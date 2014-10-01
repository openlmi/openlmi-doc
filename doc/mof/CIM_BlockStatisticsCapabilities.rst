.. _CIM-BlockStatisticsCapabilities:

CIM_BlockStatisticsCapabilities
-------------------------------

Class reference
===============
Subclass of :ref:`CIM_StatisticsCapabilities <CIM-StatisticsCapabilities>`

A specialization of the StatisticsCapabilities class that describes the capabilities of a BlockStatisticsService, which provides statistical data for instances of BlockStatisticalData.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-BlockStatisticsCapabilities-SynchronousMethodsSupported:

``uint16[]`` **SynchronousMethodsSupported**

    The synchronous mechanisms supported for retrieving statistics and defining and modifying filters for statistics retrieval.

    
    ======== =======================
    ValueMap Values                 
    ======== =======================
    2        Execute Query          
    3        Query Collection       
    4        GetStatisticsCollection
    5        Manifest Creation      
    6        Manifest Modification  
    7        Manifest Removal       
    ..       DMTF Reserved          
    0x8000.. Vendor Specific        
    ======== =======================
    
.. _CIM-BlockStatisticsCapabilities-ElementTypesSupported:

``uint16[]`` **ElementTypesSupported**

    The list of element types for which statistical data is available. The values of this array correspond to the values defined for the ElementType property of the BlockStatisticalData class.

    
    ======== =========================
    ValueMap Values                   
    ======== =========================
    2        Computer System          
    3        Front-end Computer System
    4        Peer Computer System     
    5        Back-end Computer System 
    6        Front-end Port           
    7        Back-end Port            
    8        Volume                   
    9        Extent                   
    10       Disk Drive               
    11       Arbitrary LUs            
    12       Remote Replica Group     
    ..       DMTF Reserved            
    0x8000.. Vendor Specific          
    ======== =========================
    
.. _CIM-BlockStatisticsCapabilities-AsynchronousMethodsSupported:

``uint16[]`` **AsynchronousMethodsSupported**

    The asychronous mechanisms supported for retrieving statistics.

    
    ======== =======================
    ValueMap Values                 
    ======== =======================
    2        GetStatisticsCollection
    3        Indications            
    ..       DMTF Reserved          
    0x8000.. Vendor Specific        
    ======== =======================
    
.. _CIM-BlockStatisticsCapabilities-SupportedFeatures:

``uint16[]`` **SupportedFeatures**

    SupportedFeatures is an array identifying features supported by the implementation. The valid values are "2" (none) or "3" (Client Defined Sequence). If "2" is specified, then no other entry may be included. If "3" is specified, it indicates client may define, in the manifest, the sequence in which the requested properties are returned.

    
    ======== =======================
    ValueMap Values                 
    ======== =======================
    2        none                   
    3        Client Defined Sequence
    ..       DMTF Reserved          
    0x8000.. Vendor Specific        
    ======== =======================
    
.. _CIM-BlockStatisticsCapabilities-ClockTickInterval:

``uint64`` **ClockTickInterval**

    An internal clocking interval for all timers in the subsystem, measured in microseconds (Unit of measure in the timers, measured in microseconds). Time counters are monotanically increasing counters that contain 'ticks'. Each tick represents one ClockTickInterval. If ClockTickInterval contained a value of 32 then each time counter tick would represent 32 microseconds.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-Capabilities-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`InstanceID <CIM-Capabilities-InstanceID>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`

