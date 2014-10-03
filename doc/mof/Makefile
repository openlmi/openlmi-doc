src: index.rst

TOPDIR=../../..
STORAGEDIR=$(TOPDIR)/openlmi-storage
PROVIDERSDIR=$(TOPDIR)/openlmi-providers
NETWORKDIR=$(TOPDIR)/openlmi-networking

MOFS=$(PROVIDERSDIR)/mof/05_LMI_Qualifiers.mof \
    $(PROVIDERSDIR)/mof/30_LMI_Jobs.mof \
    $(PROVIDERSDIR)/mof/50_LMI_LogicalFile.mof \
    $(PROVIDERSDIR)/mof/60_LMI_Account.mof \
    $(PROVIDERSDIR)/mof/60_LMI_Fan.mof \
    $(PROVIDERSDIR)/mof/60_LMI_Hardware.mof \
    $(PROVIDERSDIR)/mof/60_LMI_Journald.mof \
    $(PROVIDERSDIR)/mof/60_LMI_Locale.mof \
    $(PROVIDERSDIR)/mof/60_LMI_PCP.mof \
    $(PROVIDERSDIR)/mof/60_LMI_PowerManagement.mof \
    $(PROVIDERSDIR)/mof/60_LMI_Realmd.mof \
    $(PROVIDERSDIR)/mof/60_LMI_SSSD.mof \
    $(PROVIDERSDIR)/mof/60_LMI_Service.mof \
    $(PROVIDERSDIR)/mof/60_LMI_SELinux.mof \
    $(PROVIDERSDIR)/build/mof/60_LMI_Software.mof \
    $(STORAGEDIR)/mof/LMI_Storage-Base.mof \
    $(STORAGEDIR)/mof/LMI_Storage-Luks.mof \
    $(STORAGEDIR)/mof/LMI_Storage-Partitions.mof \
    $(STORAGEDIR)/mof/LMI_Storage-BlockStorage.mof \
    $(STORAGEDIR)/mof/LMI_Storage-Filesystem.mof \
    $(STORAGEDIR)/mof/LMI_Storage-Jobs.mof \
    $(STORAGEDIR)/mof/LMI_Storage-Mounting.mof  \
    $(NETWORKDIR)/mof/60_LMI_Networking.mof

index.rst: $(MOFS) tree_header.txt header.txt Makefile
	openlmi-doc-class2rst -C -H header.txt -T tree_header.txt -M `echo $(MOFS) | sed 's/ / -M /g'` -S /usr/share/mof/cim-current/CIM_Schema.mof `cat $(MOFS) | grep "^class" | cut -d ' ' -f 2 | sed 's/://'`
