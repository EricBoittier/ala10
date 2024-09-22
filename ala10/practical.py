import os
from pathlib import Path

import numpy as np

# boltzmann constant in units of (kcal/mol)/K
boltzmann = 1.987204259 * 10**-3
FONTSIZE = 20
time_step = 0.002


# helper functions
def running_mean(x, N=1000):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[N:] - cumsum[:-N]) / float(N)


def jarzynski(forces, velocity=1.0, dt=0.1, T=300.0):
    beta = 1 / (boltzmann * T)
    work = velocity * dt * np.cumsum(forces)
    dG = -(1 / beta) * np.log(np.exp(work * -beta))
    return dG


def run_at(velocity, T=300.0):
    # namd job template
    velocity_per_step = velocity * time_step
    Nsteps = 10000 * 0.002 / velocity_per_step
    # round Nsteps to the nearest integer
    Nsteps = np.round(Nsteps)
    print("Nsteps", Nsteps)
    print("velocity_per_step", velocity_per_step)
    namd = open("smd.namd.t", "r").read()
    namd = namd.format(Nsteps=int(Nsteps // 1), temperature=T)
    tcl = open("smd.tcl.t", "r").read()
    tcl = tcl.replace("TCLFREQ", "50")
    tcl = tcl.replace("VELOCITY", str(velocity_per_step))

    # create a directory for the velocity
    Path(f"velocity_{velocity}").mkdir(parents=True, exist_ok=True)
    with open(f"velocity_{velocity}/smd.namd", "w") as f:
        f.write(namd)
    with open(f"velocity_{velocity}/smd.tcl", "w") as f:
        f.write(tcl)
    files = ["par_all27_prot_lipid.prm", "namd3", "namd.sh", "da.psf", "smd_ini.pdb"]
    for file in files:
        # copy the files to the directory
        os.system(f"cp {file} velocity_{velocity}")

    # change to the directory and run the job
    os.chdir(f"velocity_{velocity}")
    os.system("bash namd.sh")
    os.chdir("..")

