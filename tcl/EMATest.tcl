# Testdatei EMA-Indikator

# Scripte einbinden
source "Scripts/Funktionen/ReadIndex.tcl"
#source "Scripts/Funktionen/Delta.tcl"
source "Scripts/Indikatoren/EMA.tcl"

# Kommandozeilen Parameter überprüpfen
if {[llength $argv]==0} {
  puts "\nSyntax: EMATest.tcl <Wertpapier-Datei> \[n\]"
  puts "  Berechnet den EMA-Indikator n-Tage."
  puts "  Voreingestellt sind 20 Tage EMA.\n"
  exit
}

# Parameter übergeben
set EMA1N  20
if {[llength $argv]>=2} {set EMA1N  [lindex $argv 1]}

# Dateien öffnen, vorbereiten
set eingabeDatei [lindex $argv 0]
set ausgabeDatei "$eingabeDatei.EMA.$EMA1N.txt"

# Ausführen der Funktionen
ReadIndex datumA openA highA lowA closeA $eingabeDatei
EMA emaA closeA $EMA1N
#Delta emaDeltaA emaA

# Ergebnisausgabe in Ausgabedatei
puts "> Schreibe Ausgabedatei $ausgabeDatei ..."
set ausgabeFid [open "$ausgabeDatei" w]

set i 0
while {$i<[array size emaA]} {
  puts $ausgabeFid "$datumA($i) $emaA($i)"
#  puts $ausgabeFid "$datumA($i) $emaA($i) $emaDeltaA($i)"
  incr i
}

# Ausgabedatei schließen
close $ausgabeFid
puts "Fertig."

exit
