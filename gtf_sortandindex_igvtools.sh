#sh gtf_sortandindex_igvtools.sh gtffile
gtffile=$1
igvtools sort $gtffile ${gtffile%.gtf}.sorted.gtf
igvtools index ${gtffile%.gtf}.sorted.gtf
rm -f igv.log
