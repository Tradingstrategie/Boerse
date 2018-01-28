# Funktion SMA-Indikator

# Berechne den Indikator Simple-Moving-Average (SMA) auf dem angegeben Daten-Array
# und speichere das Ergebnis in pResultA.
# Für den SMA werden nN Werte gemittelt.

proc SMA {pResultA pDataA nN} {
  
  upvar $pResultA smaA
  upvar $pDataA dataA

  puts "> Berechne SMA-Indikator $pResultA auf $pDataA mit N=$nN..."
  
  # Zähler Zeilennummer
  set i 0

  while {$i<[array size dataA]} {

    # SMA berechnen
    set m [expr $i-$nN+1]
    if {$m<0} {set m 0}

    set smaA($i) 0

    for { set j $m } { $j <= $i } { incr j } {
      set smaA($i) [expr $smaA($i) + $dataA($j)]
    }
    set smaA($i) [expr $smaA($i) / ($i-$m+1)]

    incr i
  }

  puts "  SMA auf $i Werten berechnet."
}

