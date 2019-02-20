
from PyQt4 import QtGui, QtCore

from distutils.sysconfig import get_python_lib


## presumably need to import pickle module twice to make it work properly:
#import json
#import codecs

def write_out_LCR(io, grids, center_ctrl, configuration, num_orbital_dict):
    """
       write out LCR.dat0, LCR.dat1, LCR.dat2, ... 
    """

    electrodes = configuration.conf
    elements1 = electrodes[1].elements
    num_atoms1 = len(elements1)
    num_orbitals1 = sum( [ num_orbital_dict[e] for e in elements1])

    elements2 = electrodes[2].elements
    num_atoms2 = len(elements2)
    num_orbitals2 = sum( [ num_orbital_dict[e] for e in elements2])

    elements3 = electrodes[0].elements
    num_atoms3 = len(elements3)-num_atoms1 - num_atoms2
    num_orbitals3 = sum( [ num_orbital_dict[e] for e in elements3])
    num_orbitals3 -= num_orbitals1 + num_orbitals2


    a1 = electrodes[1].lattice[0]
    a2 = electrodes[2].lattice[0]
    a3 = electrodes[0].lattice[0] -a1 -a2
    b = electrodes[0].lattice[1]

    try:
        dir_name = '3lead_lead1'
        with open(dir_name + '/LCR.dat0','w') as inc_file:
            inc_file.write('#  orbitals are read from \n')
            inc_file.write('../lead1/'+io._outputwave.text()+'\n\n')
            inc_file.write('#  charge density and potentials are read from \n')
            inc_file.write('../lead1/'+io._outputwave.text()+'\n\n')
            inc_file.write('#   lcr[].NX_GRID, NY_GRID, NZ_GRID\n')
            inc_file.write('%d  %d  %d\n\n'%(grids._Nx_left.value(), grids._Ny_left.value(), grids._Nz_left.value()))

            inc_file.write('#   starting grid point in the orignal grid \n')
            inc_file.write('0  0  0 \n\n')
            inc_file.write('#   ending grid point in the orignal grid \n')
            inc_file.write('%d  %d  %d\n\n'%(grids._Nx_left.value(), grids._Ny_left.value(), grids._Nz_left.value()))

            inc_file.write('#   starting grid point in the NEGF globla grid \n')
            inc_file.write('%d  0  0 \n\n'%grids._Nx_left.value())

            inc_file.write('# lcr[].num_ions  number of ions in a conductor or a lead \n')
            inc_file.write('%d \n\n'%num_atoms1)

            inc_file.write('#lcr[].state_begin, state_middle, state_end state_middle is dummy\n')
            inc_file.write('0  0  %d \n\n'%num_orbitals1)

            inc_file.write('#lcr[].ion_begin  \n  0 \n\n')

            inc_file.write('#lcr[].bias (eV) \n')

            inc_file.write('XXXXX   XXXXX   0.0\n\n')

            inc_file.write('# a_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting x-coordinate (in the global system)\n')
            inc_file.write('%f  %f \n\n'%(a1,a1))

            inc_file.write('# b_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting y-coordinate (in the global system)\n')
            inc_file.write('%f  0 \n\n'%b)
            
        with open(dir_name + '/LCR.dat1','w') as inc_file:
            inc_file.write('#  orbitals are read from \n')
            inc_file.write('../lead1/'+io._outputwave.text()+'\n\n')
            inc_file.write('#  charge density and potentials are read from \n')
            inc_file.write('../lead1/'+io._outputwave.text()+'\n\n')
            inc_file.write('#   lcr[].NX_GRID, NY_GRID, NZ_GRID\n')
            inc_file.write('%d  %d  %d\n\n'%(grids._Nx_left.value(), grids._Ny_left.value(), grids._Nz_left.value()))

            inc_file.write('#   starting grid point in the orignal grid \n')
            inc_file.write('0  0  0 \n\n')
            inc_file.write('#   ending grid point in the orignal grid \n')
            inc_file.write('%d  %d  %d\n\n'%(grids._Nx_left.value(), grids._Ny_left.value(), grids._Nz_left.value()))

            inc_file.write('#   starting grid point in the NEGF globla grid \n')
            inc_file.write('0  0  0 \n\n')

            inc_file.write('# lcr[].num_ions  number of ions in a conductor or a lead \n')
            inc_file.write('%d \n\n'%num_atoms1)

            inc_file.write('#lcr[].state_begin, state_middle, state_end state_middle is dummy\n')
            inc_file.write('0  0  %d \n\n'%num_orbitals1)

            inc_file.write('#lcr[].ion_begin  \n  0 \n\n')

            inc_file.write('#lcr[].bias (eV) \n')

            inc_file.write('XXXXX   XXXXX   0.0\n\n')

            inc_file.write('# a_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting x-coordinate (in the global system)\n')
            inc_file.write('%f  0 \n\n'%a1)

            inc_file.write('# b_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting y-coordinate (in the global system)\n')
            inc_file.write('%f  0 \n\n'%b)
            
    
        with open(dir_name + '/LCR.dat2','w') as inc_file:
            inc_file.write('#  orbitals are read from \n')
            inc_file.write('../lead1/'+io._outputwave.text()+'\n\n')
            inc_file.write('#  charge density and potentials are read from \n')
            inc_file.write('../lead1/'+io._outputwave.text()+'\n\n')
            inc_file.write('#   lcr[].NX_GRID, NY_GRID, NZ_GRID\n')
            inc_file.write('%d  %d  %d\n\n'%(grids._Nx_left.value(), grids._Ny_left.value(), grids._Nz_left.value()))

            inc_file.write('#   starting grid point in the orignal grid \n')
            inc_file.write('0  0  0 \n\n')
            inc_file.write('#   ending grid point in the orignal grid \n')
            inc_file.write('%d  %d  %d\n\n'%(grids._Nx_left.value(), grids._Ny_left.value(), grids._Nz_left.value()))

            inc_file.write('#   starting grid point in the NEGF globla grid \n')
            inc_file.write('%d  0  0 \n\n'%(2*grids._Nx_left.value()))

            inc_file.write('# lcr[].num_ions  number of ions in a conductor or a lead \n')
            inc_file.write('%d \n\n'%num_atoms1)

            inc_file.write('#lcr[].state_begin, state_middle, state_end state_middle is dummy\n')
            inc_file.write('0  0  %d \n\n'%num_orbitals1)

            inc_file.write('#lcr[].ion_begin  \n  0 \n\n')

            inc_file.write('#lcr[].bias (eV) \n')

            inc_file.write('XXXXX   XXXXX   0.0\n\n')

            inc_file.write('# a_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting x-coordinate (in the global system)\n')
            inc_file.write('%f  %f \n\n'%(a1,(2*a1)))

            inc_file.write('# b_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting y-coordinate (in the global system)\n')
            inc_file.write('%f  0 \n\n'%b)
            
    

        dir_name = '3lead_lead2'
        with open(dir_name + '/LCR.dat0','w') as inc_file:
            inc_file.write('#  orbitals are read from \n')
            inc_file.write('../lead2/'+io._outputwave.text()+'\n\n')
            inc_file.write('#  charge density and potentials are read from \n')
            inc_file.write('../lead2/'+io._outputwave.text()+'\n\n')
            inc_file.write('#   lcr[].NX_GRID, NY_GRID, NZ_GRID\n')
            inc_file.write('%d  %d  %d\n\n'%(grids._Nx_right.value(), grids._Ny_right.value(), grids._Nz_right.value()))

            inc_file.write('#   starting grid point in the orignal grid \n')
            inc_file.write('0  0  0 \n\n')
            inc_file.write('#   ending grid point in the orignal grid \n')
            inc_file.write('%d  %d  %d\n\n'%(grids._Nx_right.value(), grids._Ny_right.value(), grids._Nz_right.value()))

            inc_file.write('#   starting grid point in the NEGF globla grid \n')
            inc_file.write('%d  0  0 \n\n'%grids._Nx_right.value())

            inc_file.write('# lcr[].num_ions  number of ions in a conductor or a lead \n')
            inc_file.write('%d \n\n'%num_atoms2)

            inc_file.write('#lcr[].state_begin, state_middle, state_end state_middle is dummy\n')
            inc_file.write('0  0  %d \n\n'%num_orbitals2)

            inc_file.write('#lcr[].ion_begin  \n  0 \n\n')

            inc_file.write('#lcr[].bias (eV) \n')

            inc_file.write('XXXXX  XXXXX   0.0\n\n')

            inc_file.write('# a_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting x-coordinate (in the global system)\n')
            inc_file.write('%f  %f \n\n'%(a2,a2))

            inc_file.write('# b_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting y-coordinate (in the global system)\n')
            inc_file.write('%f  0 \n\n'%b)
            
        with open(dir_name + '/LCR.dat1','w') as inc_file:
            inc_file.write('#  orbitals are read from \n')
            inc_file.write('../lead2/'+io._outputwave.text()+'\n\n')
            inc_file.write('#  charge density and potentials are read from \n')
            inc_file.write('../lead2/'+io._outputwave.text()+'\n\n')
            inc_file.write('#   lcr[].NX_GRID, NY_GRID, NZ_GRID\n')
            inc_file.write('%d  %d  %d\n\n'%(grids._Nx_right.value(), grids._Ny_right.value(), grids._Nz_right.value()))

            inc_file.write('#   starting grid point in the orignal grid \n')
            inc_file.write('0  0  0 \n\n')
            inc_file.write('#   ending grid point in the orignal grid \n')
            inc_file.write('%d  %d  %d\n\n'%(grids._Nx_right.value(), grids._Ny_right.value(), grids._Nz_right.value()))

            inc_file.write('#   starting grid point in the NEGF globla grid \n')
            inc_file.write('0  0  0 \n\n')

            inc_file.write('# lcr[].num_ions  number of ions in a conductor or a lead \n')
            inc_file.write('%d \n\n'%num_atoms2)

            inc_file.write('#lcr[].state_begin, state_middle, state_end state_middle is dummy\n')
            inc_file.write('0  0  %d \n\n'%num_orbitals2)

            inc_file.write('#lcr[].ion_begin  \n  0 \n\n')

            inc_file.write('#lcr[].bias (eV) \n')

            inc_file.write('XXXXX   XXXXX   0.0\n\n')

            inc_file.write('# a_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting x-coordinate (in the global system)\n')
            inc_file.write('%f  0 \n\n'%a2)

            inc_file.write('# b_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting y-coordinate (in the global system)\n')
            inc_file.write('%f  0 \n\n'%b)
            
    
        with open(dir_name + '/LCR.dat2','w') as inc_file:
            inc_file.write('#  orbitals are read from \n')
            inc_file.write('../lead2/'+io._outputwave.text()+'\n\n')
            inc_file.write('#  charge density and potentials are read from \n')
            inc_file.write('../lead2/'+io._outputwave.text()+'\n\n')
            inc_file.write('#   lcr[].NX_GRID, NY_GRID, NZ_GRID\n')
            inc_file.write('%d  %d  %d\n\n'%(grids._Nx_right.value(), grids._Ny_right.value(), grids._Nz_right.value()))

            inc_file.write('#   starting grid point in the orignal grid \n')
            inc_file.write('0  0  0 \n\n')
            inc_file.write('#   ending grid point in the orignal grid \n')
            inc_file.write('%d  %d  %d\n\n'%(grids._Nx_right.value(), grids._Ny_right.value(), grids._Nz_right.value()))

            inc_file.write('#   starting grid point in the NEGF globla grid \n')
            inc_file.write('%d  0  0 \n\n'%(2*grids._Nx_right.value()))

            inc_file.write('# lcr[].num_ions  number of ions in a conductor or a lead \n')
            inc_file.write('%d \n\n'%num_atoms2)

            inc_file.write('#lcr[].state_begin, state_middle, state_end state_middle is dummy\n')
            inc_file.write('0  0  %d \n\n'%num_orbitals2)

            inc_file.write('#lcr[].ion_begin  \n  0 \n\n')

            inc_file.write('#lcr[].bias (eV) \n')

            inc_file.write('XXXXX   XXXXX   0.0\n\n')

            inc_file.write('# a_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting x-coordinate (in the global system)\n')
            inc_file.write('%f  %f \n\n'%(a2,(2*a2)))

            inc_file.write('# b_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting y-coordinate (in the global system)\n')
            inc_file.write('%f  0 \n\n'%b)
            
    
        dir_name = 'bias_0.0'

        if(grids.center_periodicity.isChecked()):
            start_grid = 0
            end_grid = grids._Nx_center.value()
            state_begin = 0
            state_end = num_orbitals3
            ion_begin = 0
            acenter = a3
            ashift = a1
            num_atoms_center = num_atoms3
        else:
            start_grid = grids._Nx_left.value()
            end_grid = grids._Nx_center.value()-grids._Nx_right.value()
            state_begin = center_ctrl['state_begin']
            state_end = state_begin + num_orbitals3
            ion_begin = center_ctrl['ion_begin']
            acenter = a3 + a1 + a2
            ashift = 0
            num_atoms_center = center_ctrl['num_atoms']
            
            
        with open(dir_name + '/LCR.dat0','w') as inc_file:
            inc_file.write('#  orbitals are read from \n')
            inc_file.write('../center/'+io._outputwave.text()+'\n\n')
            inc_file.write('#  charge density and potentials are read from \n')
            inc_file.write('../center/'+io._outputwave.text()+'\n\n')
            inc_file.write('#   lcr[].NX_GRID, NY_GRID, NZ_GRID\n')
            inc_file.write('%d  %d  %d\n\n'%(grids._Nx_center.value(), grids._Ny_center.value(), grids._Nz_center.value()))

            inc_file.write('#   starting grid point in the orignal grid \n')
            inc_file.write('%d  0  0 \n\n'%start_grid)
            inc_file.write('#   ending grid point in the orignal grid \n')
            inc_file.write('%d  %d  %d\n\n'%(end_grid, grids._Ny_center.value(), grids._Nz_center.value()))

            inc_file.write('#   starting grid point in the NEGF globla grid \n')
            inc_file.write('%d  0  0 \n\n'%grids._Nx_left.value())

            inc_file.write('# lcr[].num_ions  number of ions in a conductor or a lead \n')
            inc_file.write('%d \n\n'%num_atoms_center)

            inc_file.write('#lcr[].state_begin, state_middle, state_end state_middle is dummy\n')
            inc_file.write('%d  0  %d \n\n'%(state_begin, state_end))

            inc_file.write('#lcr[].ion_begin  \n  %d \n\n'%ion_begin)

            inc_file.write('#lcr[].bias (eV) \n')

            inc_file.write('0.0   XXXXX   0.0\n\n')

            inc_file.write('# a_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting x-coordinate (in the global system)\n')
            inc_file.write('%f  %f \n\n'%(acenter,ashift))

            inc_file.write('# b_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting y-coordinate (in the global system)\n')
            inc_file.write('%f  0 \n\n'%b)
            
        with open(dir_name + '/LCR.dat1','w') as inc_file:
            inc_file.write('#  orbitals are read from \n')
            inc_file.write('../lead1/'+io._outputwave.text()+'\n\n')
            inc_file.write('#  charge density and potentials are read from \n')
            inc_file.write('../3lead_lead1/'+io._outputwave.text()+'\n\n')
            inc_file.write('#   lcr[].NX_GRID, NY_GRID, NZ_GRID\n')
            inc_file.write('%d  %d  %d\n\n'%(grids._Nx_left.value(), grids._Ny_left.value(), grids._Nz_left.value()))

            inc_file.write('#   starting grid point in the orignal grid \n')
            inc_file.write('0  0  0 \n\n')
            inc_file.write('#   ending grid point in the orignal grid \n')
            inc_file.write('%d  %d  %d\n\n'%(grids._Nx_left.value(), grids._Ny_left.value(), grids._Nz_left.value()))

            inc_file.write('#   starting grid point in the NEGF globla grid \n')
            inc_file.write('0  0  0 \n\n')

            inc_file.write('# lcr[].num_ions  number of ions in a conductor or a lead \n')
            inc_file.write('%d \n\n'%num_atoms1)

            inc_file.write('#lcr[].state_begin, state_middle, state_end state_middle is dummy\n')
            inc_file.write('0  0  %d \n\n'%num_orbitals1)

            inc_file.write('#lcr[].ion_begin  \n  0 \n\n')

            inc_file.write('#lcr[].bias (eV) \n')

            inc_file.write('0.0   XXXXX   0.0\n\n')

            inc_file.write('# a_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting x-coordinate (in the global system)\n')
            inc_file.write('%f  0 \n\n'%a1)

            inc_file.write('# b_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting y-coordinate (in the global system)\n')
            inc_file.write('%f  0 \n\n'%b)
            
    
        with open(dir_name + '/LCR.dat2','w') as inc_file:
            inc_file.write('#  orbitals are read from \n')
            inc_file.write('../lead2/'+io._outputwave.text()+'\n\n')
            inc_file.write('#  charge density and potentials are read from \n')
            inc_file.write('../3lead_lead2/'+io._outputwave.text()+'\n\n')
            inc_file.write('#   lcr[].NX_GRID, NY_GRID, NZ_GRID\n')
            inc_file.write('%d  %d  %d\n\n'%(grids._Nx_right.value(), grids._Ny_right.value(), grids._Nz_right.value()))

            inc_file.write('#   starting grid point in the orignal grid \n')
            inc_file.write('0  0  0 \n\n')
            inc_file.write('#   ending grid point in the orignal grid \n')
            inc_file.write('%d  %d  %d\n\n'%(grids._Nx_right.value(), grids._Ny_right.value(), grids._Nz_right.value()))

            inc_file.write('#   starting grid point in the NEGF globla grid \n')
            inc_file.write('%d  0  0 \n\n'%(grids._Nx_negf-grids._Nx_right.value() ))

            inc_file.write('# lcr[].num_ions  number of ions in a conductor or a lead \n')
            inc_file.write('%d \n\n'%num_atoms2)

            inc_file.write('#lcr[].state_begin, state_middle, state_end state_middle is dummy\n')
            inc_file.write('0  0  %d \n\n'%num_orbitals2)

            inc_file.write('#lcr[].ion_begin  \n  0 \n\n')

            inc_file.write('#lcr[].bias (eV) \n')

            inc_file.write('0.0   XXXXX   0.0\n\n')

            inc_file.write('# a_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting x-coordinate (in the global system)\n')
            inc_file.write('%f  %f \n\n'%(a2,(a1+a3)))

            inc_file.write('# b_length of this supercell (same as ON2 cal),\n')
            inc_file.write('# the starting y-coordinate (in the global system)\n')
            inc_file.write('%f  0 \n\n'%b)
            
    
    except:
        showError()

