set Fexact(1) {}
set Fexact(2) {}

set infile [open Fexact.dat r]
while {[gets $infile line] >= 0} {
   foreach lt {1 2} zt $line {lappend Fexact($lt) $zt}
}

close $infile

