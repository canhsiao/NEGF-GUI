
from PyQt4 import QtGui, QtCore

from distutils.sysconfig import get_python_lib


def write_out_others(configuration, negfpara, grids, mdscf, num_orbital_dict):
    """
       write out trans.in cond.input
    """
    electrodes = configuration.conf
    elements1 = electrodes[1].elements
    num_atoms1 = len(elements1)
    num_orbitals1 = sum( [ num_orbital_dict[e] for e in elements1])

    elements2 = electrodes[2].elements
    num_atoms2 = len(elements2)
    num_orbitals2 = sum( [ num_orbital_dict[e] for e in elements2])

    elements3 = electrodes[0].elements
    num_atoms3 = len(elements3)
    num_orbitals3 = sum( [ num_orbital_dict[e] for e in elements3])

    tot_num_orbitals = num_orbitals3

    transin_line  = '#\n'
    transin_line += '\n#num of probes and which block the probe attached to\n'
    transin_line += '%d  0  %d\n'%(negfpara.num_probe.value(), (negfpara.num_block.value()-1))

    transin_line += '\n#num of sub systems and their atomic order in NEGF calculations\n'
    transin_line += '#need to edit for multi-probe calclations\n'
    transin_line += '%d  1  0  2\n'%(negfpara.num_probe.value()+1)

    transin_line += '# num_probe_potential_window & their ranges[in the order of lead 1, 2, 3 ...]\n' 
    transin_line += '#they are dummy for 2-probe calculations and \n'
    transin_line += '#need to edit for multi-probe calclations\n'
    transin_line += '4  40 120  40 120  40 120  40 120\n'

    transin_line +='\n# num_dos_axis_window for integration along x,y,z axis\n'
    transin_line +='# (required for mode 200)\n'
    transin_line +='3  0 %d  0 %d 0 %d\n'%(grids._Nx_center.value(),grids._Ny_center.value(),grids._Nz_center.value())

    transin_line += '\n#ncircle \n %d \n\n'%negfpara.ncircle.value()
    transin_line += '\n#nmax_gq1 \n %d \n\n'%negfpara.nmax_gq1.value()
    transin_line += '\n#nmax_gq2 \n %d \n\n'%negfpara.nmax_gq2.value()
    transin_line += '\n#Enery Low Bound \n %s \n\n'%negfpara.elowbound.text()
    transin_line += '\n#KT \n %s \n\n'%negfpara.kt.text()
    transin_line += '\n#GAMMA \n %s \n\n'%negfpara.gamma.text()
    transin_line += '\n#DELTA2 \n %s \n\n'%negfpara.delta2.text()
    transin_line += '\n#DELTA \n %s \n\n'%negfpara.delta.text()

    transin_line += '\n#Charge density Pulay order \n %d \n\n'%mdscf._pulayorder.value()
    transin_line += '\n#Charge density Pulay refresh steps \n %s \n\n'%mdscf._pulayrefresh.text()
    transin_line += '\n#Charge density Pulay beta \n %s \n\n'%mdscf._pulaybeta.text()

    transin_line += '\n#processor grids for block matrix operation  \n'
    transin_line += '%d \n%d\n'%(negfpara.nprow.value(),negfpara.npcol.value())

    condinput_line  = '#  input for conductance calculations \n\n'
    condinput_line += '%d %d %d  nC nL nR \n'%( (num_orbitals1*3), num_orbitals1, num_orbitals1)
    condinput_line += '3 %d %d %d  num_blocks, block_dim \n'%(num_orbitals1, num_orbitals1, num_orbitals1)
    condinput_line += '%s %s %d  Emin,Emax, E_points \n'%(negfpara.Emin_lead1.text(), negfpara.Emax_lead1.text(), negfpara.Epoint_lead1.value()) 
    condinput_line += '%s  small imaginary part \n'%negfpara.Eimag.text()
    condinput_line += '%s  kbt \n'%negfpara.kbt.text()
    condinput_line += '%d %d %d   \n'%(negfpara.nkx.value(), negfpara.nky.value(), negfpara.nkz.value())
    condinput_line += '1   number of conductance curve from lead i to lead j\n'
    condinput_line += '1  2  lead i to lead j\n'

    dir_name = '3lead_lead1'
    with open(dir_name + '/trans.in','w') as inc_file:
        inc_file.write(transin_line)
    with open(dir_name + '/cond.input','w') as inc_file:
        inc_file.write(condinput_line)

    condinput_line  = '#  input for conductance calculations \n\n'
    condinput_line += '%d %d %d  nC nL nR \n'%( (num_orbitals2*3), num_orbitals2, num_orbitals2)
    condinput_line += '3 %d %d %d  num_blocks, block_dim \n'%(num_orbitals2, num_orbitals2, num_orbitals2)
    condinput_line += '%s %s %d  Emin,Emax, E_points \n'%(negfpara.Emin_lead2.text(), negfpara.Emax_lead2.text(), negfpara.Epoint_lead2.value()) 
    condinput_line += '%s  small imaginary part \n'%negfpara.Eimag.text()
    condinput_line += '%s  kbt \n'%negfpara.kbt.text()
    condinput_line += '%d %d %d   \n'%(negfpara.nkx.value(), negfpara.nky.value(), negfpara.nkz.value())
    condinput_line += '1   number of conductance curve from lead i to lead j\n'
    condinput_line += '1  2  lead i to lead j\n'
    dir_name = '3lead_lead2'
    with open(dir_name + '/trans.in','w') as inc_file:
        inc_file.write(transin_line)
    with open(dir_name + '/cond.input','w') as inc_file:
        inc_file.write(condinput_line)
  
    condinput_line  = '#  input for conductance calculations \n\n'
    condinput_line += '%d %d %d  nC nL nR \n'%( tot_num_orbitals, num_orbitals1, num_orbitals2)
    condinput_line += '3 %d %d %d  num_blocks, block_dim \n'%(num_orbitals1, num_orbitals3-num_orbitals1-num_orbitals2, num_orbitals2)
    condinput_line += '%s %s %d  Emin,Emax, E_points \n'%(negfpara.Emin_negf.text(), negfpara.Emax_negf.text(), negfpara.Epoint_negf.value()) 
    condinput_line += '%s  small imaginary part \n'%negfpara.Eimag.text()
    condinput_line += '%s  kbt \n'%negfpara.kbt.text()
    condinput_line += '%d %d %d   \n'%(negfpara.nkx.value(), negfpara.nky.value(), negfpara.nkz.value())
    condinput_line += '1   number of conductance curve from lead i to lead j\n'
    condinput_line += '1  2  lead i to lead j\n'
    dir_name = 'bias_0.0'
    with open(dir_name + '/trans.in','w') as inc_file:
        inc_file.write(transin_line)
    with open(dir_name + '/cond.input','w') as inc_file:
        inc_file.write(condinput_line)
