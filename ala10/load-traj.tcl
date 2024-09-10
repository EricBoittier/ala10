set infile [open da.dat r]

set t {}
for {set i 1} {$i <= 10} {incr i} {
	set z($i) {}
        set f($i) {}
}

set l {1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21}
while {[gets $infile line] >= 0} {
  
    foreach lt $l zt $line {
        if {$lt > 11} {
            set j [expr $lt - 11]
            lappend f($j) $zt
        } elseif {$lt == 1} {
            lappend t $zt
        } else {
            set j [expr $lt - 1]
            lappend z($j) $zt
        }
     
    } 
} 
close $infile



