FILES=extent-inherit.svg \
    pool-inherit.svg

TOPDIR=../../..
MOFS=$(TOPDIR)/mof/LMI_Storage-Base.mof \
    $(TOPDIR)/mof/LMI_Storage-Luks.mof \
    $(TOPDIR)/mof/LMI_Storage-Partitions.mof \
    $(TOPDIR)/mof/LMI_Storage-BlockStorage.mof

src: $(FILES)

clean:
	-rm -rf $(FILES)

%.svg: %.uml ../plantuml.cfg
	plantuml -config ../plantuml.cfg -Tsvg $<

extent-inherit.uml: $(MOFS)
	openlmi-doc-class2uml -s '(CIM_|SNIA_).*' -A -M `echo $(MOFS) | sed 's/ / -M /g'` -S /usr/share/mof/cim-current/CIM_Schema.mof -S /usr/share/openlmi-providers/05_LMI_Qualifiers.mof `cat $(MOFS) | grep "^/*class" | cut -d ' ' -f 2 | egrep "LMI.*StorageExtent|Partition$$" ` >$@

pool-inherit.uml: $(MOFS)
	openlmi-doc-class2uml -s '(CIM_|SNIA_).*' -A -M `echo $(MOFS) | sed 's/ / -M /g'` -S /usr/share/mof/cim-current/CIM_Schema.mof -S /usr/share/openlmi-providers/05_LMI_Qualifiers.mof `cat $(MOFS) | grep "^/*class" | cut -d ' ' -f 2 | egrep "LMI.*StoragePool"` >$@
