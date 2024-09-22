# Molecular Dynamics Simulations of Alanine Decapeptide

## Demonstration of Jarzynski's Equality

This repository contains the source code for the molecular dynamics simulations of the alanine decapeptide.
The simulations are performed using the NAMD software package.
The purpose of this project is to demonstrate Jarzynski's equality,
which is a relation between the free energy difference of two states
and the work done in a nonequilibrium process between these states.
The free energy difference is calculated using Jarzynski's equality
and compared to the free energy difference obtained from equilibrium simulations.

Jarzynski's equality:
$ \Delta F = -kT \ln <e^{-\beta W}> $,
where $\Delta F$ is the free energy difference between the two
states, $k$ is the Boltzmann constant, $T$ is the temperature,
$W$ is the work done in the nonequilibrium process, and the
brackets denote the average over multiple nonequilibrium processes.

The free energy difference calculated using Jarzynski's equality
can be compared to the free energy difference obtained
from equilibrium simulations to validate the method.
