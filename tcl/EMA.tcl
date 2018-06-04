# Funktion EMA-Indikator

# Berechne den Indikator Exponential-Moving-Average (EMA) auf dem angegeben Daten-Array
# und speichere das Ergebnis in pResultA.
# Für den EMA werden nN Werte gemittelt.

proc EMA {pResultA pDataA nN} {
  
  upvar $pResultA emaA
  upvar $pDataA dataA

  puts "> Berechne EMA-Indikator $pResultA auf $pDataA mit N=$nN..."

  # Zähler Zeilennummer
  set i 1
  set emaA(0) $dataA(0)

  while {$i<[array size dataA]} {

    # EMA berechnen
    if { $i>0 } {
      set j [expr $i-1]
      set emaA($i) [expr $emaA($j) + ((2.0/($nN+1))*($dataA($i)-$emaA($j))) ]
    }
	
    incr i
  }
  
  puts "  EMA auf $i Werten berechnet."
}
