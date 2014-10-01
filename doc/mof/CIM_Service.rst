.. _CIM-Service:

CIM_Service
-----------

Class reference
===============
Subclass of :ref:`CIM_EnabledLogicalElement <CIM-EnabledLogicalElement>`

A Service is a LogicalElement that represents the availability of functionality that can be managed. This functionality may be provided by a seperately modeled entity such as a LogicalDevice or a SoftwareFeature, or both. The modeled Service typically provides only functionality required for management of itself or the elements it affects.


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <CIM-Service-Name>`
| :ref:`SystemName <CIM-Service-SystemName>`
| :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| :ref:`CreationClassName <CIM-Service-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-Service-SystemName:

``string`` **SystemName**

    The Name of the scoping System.

    
.. _CIM-Service-LoSID:

``string`` **LoSID**

    If not Null, the CIM_Service instance represents a line of service, as defined by ITIL, identified by the value of LoSID, which must be unique in the context of an unique identifier for an Organization specified in LoSOrgID.

    
.. _CIM-Service-Started:

``boolean`` **Started**

    Started is a Boolean that indicates whether the Service has been started (TRUE), or stopped (FALSE).

    
.. _CIM-Service-Name:

``string`` **Name**

    The Name property uniquely identifies the Service and provides an indication of the functionality that is managed. This functionality is described in more detail in the Description property of the object.

    
.. _CIM-Service-LoSOrgID:

``string`` **LoSOrgID**

    If not null, this CIM_Service instance represents an ITIL line of service and the value of LoSOrgID shall be a unique identifier for the organization that defines the value of LoSID.

    
.. _CIM-Service-PrimaryOwnerContact:

``string`` **PrimaryOwnerContact**

    A string that provides information on how the primary owner of the Service can be reached (for example, phone number, e-mail address, and so on).

    
.. _CIM-Service-StartMode:

``string`` **StartMode**

    Note: The use of this element is deprecated in lieu of the EnabledDefault property that is inherited from EnabledLogicalElement. The EnabledLogicalElement addresses the same semantics. The change to a uint16 data type was discussed when CIM V2.0 was defined. However, existing V1.0 implementations used the string property. To remain compatible with those implementations, StartMode was grandfathered into the schema. Use of the deprecated qualifier allows the maintenance of the existing property but also permits an improved, clarified definition using EnabledDefault. 

    Deprecated description: StartMode is a string value that indicates whether the Service is automatically started by a System, an Operating System, and so on, or is started only upon request.

    
.. _CIM-Service-SystemCreationClassName:

``string`` **SystemCreationClassName**

    The CreationClassName of the scoping System.

    
.. _CIM-Service-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass that is used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    
.. _CIM-Service-PrimaryOwnerName:

``string`` **PrimaryOwnerName**

    The name of the primary owner for the service, if one is defined. The primary owner is the initial support contact for the Service.

    

Local methods
^^^^^^^^^^^^^

    .. _CIM-Service-StartService:

``uint32`` **StartService** ()

    The StartService method places the Service in the started state. Note that the function of this method overlaps with the RequestedState property. RequestedState was added to the model to maintain a record (such as a persisted value) of the last state request. Invoking the StartService method should set the RequestedState property appropriately. The method returns an integer value of 0 if the Service was successfully started, 1 if the request is not supported, and any other number to indicate an error. In a subclass, the set of possible return codes could be specified using a ValueMap qualifier on the method. The strings to which the ValueMap contents are translated can also be specified in the subclass as a Values array qualifier. 

    

    Note: The semantics of this method overlap with the RequestStateChange method that is inherited from EnabledLogicalElement. This method is maintained because it has been widely implemented, and its simple "start" semantics are convenient to use.

    
    **Parameters**
    
*None*
    .. _CIM-Service-StopService:

``uint32`` **StopService** ()

    **Deprecated!** 
    The StopService method places the Service in the stopped state. Note that the function of this method overlaps with the RequestedState property. RequestedState was added to the model to maintain a record (such as a persisted value) of the last state request. Invoking the StopService method should set the RequestedState property appropriately. The method returns an integer value of 0 if the Service was successfully stopped, 1 if the request is not supported, and any other number to indicate an error. In a subclass, the set of possible return codes could be specified using a ValueMap qualifier on the method. The strings to which the ValueMap contents are translated can also be specified in the subclass as a Values array qualifier. 

    

    Note: The semantics of this method overlap with the RequestStateChange method that is inherited from EnabledLogicalElement. This method is maintained because it has been widely implemented, and its simple "stop" semantics are convenient to use.

    
    **Parameters**
    
*None*
    .. _CIM-Service-ChangeAffectedElementsAssignedSequence:

``uint32`` **ChangeAffectedElementsAssignedSequence** (:ref:`CIM_ManagedElement[] <CIM-ManagedElement>` ManagedElements, ``uint16[]`` AssignedSequence, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job)

    This method is called to change relative sequence in which order the ManagedElements associated to the Service through CIM_ServiceAffectsElement association are affected. In the case when the Service represents an interface for client to execute extrinsic methods and when it is used for grouping of the managed elements that could be affected, the ordering represents the relevant priority of the affected managed elements with respect to each other. 

    An ordered array of ManagedElement instances is passed to this method, where each ManagedElement instance shall be already be associated with this Service instance via CIM_ServiceAffectsElement association. If one of the ManagedElements is not associated to the Service through CIM_ServiceAffectsElement association, the implementation shall return a value of 2 ("Error Occured"). 

    Upon successful execution of this method, if the AssignedSequence parameter is NULL, the value of the AssignedSequence property on each instance of CIM_ServiceAffectsElement shall be updated such that the values of AssignedSequence properties shall be monotonically increasing in correlation with the position of the referenced ManagedElement instance in the ManagedElements input parameter. That is, the first position in the array shall have the lowest value for AssignedSequence. The second position shall have the second lowest value, and so on. Upon successful execution, if the AssignedSequence parameter is not NULL, the value of the AssignedSequence property of each instance of CIM_ServiceAffectsElement referencing the ManagedElement instance in the ManagedElements array shall be assigned the value of the corresponding index of the AssignedSequence parameter array. For ManagedElements instances which are associated with the Service instance via CIM_ServiceAffectsElement and are not present in the ManagedElements parameter array, the AssignedSequence property on the CIM_ServiceAffects association shall be assigned a value of 0.

    
    ============ =======================
    ValueMap     Values                 
    ============ =======================
    0            Completed with No Error
    1            Not Supported          
    2            Error Occured          
    3            Busy                   
    4            Invalid Reference      
    5            Invalid Parameter      
    6            Access Denied          
    7..32767     DMTF Reserved          
    32768..65535 Vendor Specified       
    ============ =======================
    
    **Parameters**
    
        *IN* :ref:`CIM_ManagedElement[] <CIM-ManagedElement>` **ManagedElements**
            An array of ManagedElements.

            
        
        *IN* ``uint16[]`` **AssignedSequence**
            An array of integers representing AssignedSequence for the ManagedElement in the corresponding index of the ManagedElements parameter.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job spawned if the operation continues after the method returns. (May be null if the task is completed).

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

