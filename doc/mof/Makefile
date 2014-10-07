src: index.rst

TOPDIR=../../_build

MOFS=$(TOPDIR)/mof/05_LMI_Qualifiers.mof \
    $(TOPDIR)/mof/30_LMI_Jobs.mof \
    $(TOPDIR)/mof/50_LMI_LogicalFile.mof \
    $(TOPDIR)/mof/60_LMI_Account.mof \
    $(TOPDIR)/mof/60_LMI_Fan.mof \
    $(TOPDIR)/mof/60_LMI_Hardware.mof \
    $(TOPDIR)/mof/60_LMI_Journald.mof \
    $(TOPDIR)/mof/60_LMI_Locale.mof \
    $(TOPDIR)/mof/60_LMI_PCP.mof \
    $(TOPDIR)/mof/60_LMI_PowerManagement.mof \
    $(TOPDIR)/mof/60_LMI_Realmd.mof \
    $(TOPDIR)/mof/60_LMI_SSSD.mof \
    $(TOPDIR)/mof/60_LMI_Service.mof \
    $(TOPDIR)/mof/60_LMI_SELinux.mof \
    $(TOPDIR)/mof/60_LMI_Software.mof \
    $(TOPDIR)/mof/LMI_Storage-Base.mof \
    $(TOPDIR)/mof/LMI_Storage-Luks.mof \
    $(TOPDIR)/mof/LMI_Storage-Partitions.mof \
    $(TOPDIR)/mof/LMI_Storage-BlockStorage.mof \
    $(TOPDIR)/mof/LMI_Storage-Filesystem.mof \
    $(TOPDIR)/mof/LMI_Storage-Jobs.mof \
    $(TOPDIR)/mof/LMI_Storage-Mounting.mof  \
    $(TOPDIR)/mof/60_LMI_Networking.mof

index.rst: $(MOFS) tree_header.txt header.txt Makefile
	openlmi-doc-class2rst -C -H header.txt -T tree_header.txt -M `echo $(MOFS) | sed 's/ / -M /g'` -S /usr/share/mof/cim-current/CIM_Schema.mof `cat $(MOFS) | grep "^class" | cut -d ' ' -f 2 | sed 's/://'`
