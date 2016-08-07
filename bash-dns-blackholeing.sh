HOME=/etc/bind

ADLISTURL="https://pgl.yoyo.org/adservers/serverlist.php?hostformat=bindconfig;showintro=0;zonefilename=/etc/bind/null.zone.file;mimetype=plaintext"
MWLISTURL="http://mirror1.malwaredomains.com/files/spywaredomains.zones"

ADLISTFILE="ad-blacklist"
MWLISTFILE="mw-blacklist"
MWLISTFILECLEAN="mw-blacklist-clean"

ZONEFILE=/etc/bind/nullzone

sed 's/^M$//' < $MWLISTFILE> $MWLISTFILECLEAN

awk '{ print $1 " " $2 " {type master; file \"/etc/bind/nullzone\"; };" }' $ADLISTFULE $MWLISTFILECLEAN | sort | uniq  > /etc/bind/blacklists

