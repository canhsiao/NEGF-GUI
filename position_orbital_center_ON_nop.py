import os

from saturate_C import saturate_C
from PyQt4 import QtGui, QtCore

from distutils.sysconfig import get_python_lib

# here is the function that will return the atomic coor and orbital
#center part cannot be setup with periodic condition  because the two
#leads are different

def position_orbital_center_ON_nop(configuration, num_orbital_dict, orbital_radius_dict):
    """
    @return ascii string with atomic position and orbital centers
    """
    
    _atom_format = " %s     %.12e    %.12e    %.12e      1   \n"
    _orbital_format = " %d     %.12e    %.12e    %.12e  "
    _elements = configuration.elements 
    _element_types = set(_elements) 
    
    electrodes = configuration.conf
    ele_left = electrodes[1].elements
    num_atom_left = len(ele_left)
    ele_right = electrodes[2].elements
    num_atom_right = len(ele_right)

    coords = []
    ele = []
    coor =electrodes[0].coords()
    for i in range(len(_elements)):
        a = float("%.8e"%coor[i][0])
        b = float("%.8e"%coor[i][1])
        c = float("%.8e"%coor[i][2])
        coords.append([a, b,c])
        ele.append(_elements[i])


    a1 = electrodes[1].lattice[0]
    a2 = electrodes[2].lattice[0]
    a3 = electrodes[0].lattice[0]
    b = electrodes[1].lattice[1]
    c = electrodes[1].lattice[2]

    a = a3
    # put unitcell information into the snippet

    _positions_line = """

# Lattice constants in (x, y, z) directions
# a, b, c, cos(alpha), cos(beta), cos(gamma)
a_length="%s" b_length="%s" c_length="%s"
alpha="0.0" beta="0.0" gamma="0.0"

""" %(a,b,c)
    

    
    zipped_tem  = zip(ele, coords)
    zipped_coordinates = sorted (zipped_tem, key= lambda v:v[1][0])
    
    #  atoms in first half of the left lead  and in the second half of
    #  the right lead  are removed  
    n_remove_left = 0
    n_remove_right = 0
    for name,v in zipped_coordinates:
        if(v[2] < a1/2.0): n_remove_left +=1
        if(v[2] > a3-a2/2.0): n_remove_right +=1

    item = len(zipped_coordinates)
    del zipped_coordinates[item-n_remove_right:item]
    del zipped_coordinates[0:n_remove_left]

    
    (ele1, coords1) = zip(*zipped_coordinates)
    ele = list(ele1)
    coords = list(coords1)
    coords_add =[]
    coords_add = saturate_C(ele,coords,c,b,a)
    # determine how many H atoms are added from left side
    ileft = 0
    for v in coords_add:
        if(v[2] < a1/2.0): ileft +=1


    zipped_coordinates = zip(ele, coords)
    
    zipped_coordinates = sorted (zipped_coordinates, key= lambda v:v[1][0])
    _positions_line += '\n #  atomic coordinates  \n'
    _positions_line += 'atoms=\n"\n'

    for name,v in zipped_coordinates:
        _positions_line += ( _atom_format % (name, v[0],v[1],v[2]) )

    _positions_line += '"\n'


    _positions_line += '\n #  orbital centers  \n'
    _positions_line += 'orbitals=\n"\n'

    for name,v in zipped_coordinates:
        _positions_line += ( _orbital_format % (num_orbital_dict[name], v[0],v[1],v[2]) )
        _positions_line +=  orbital_radius_dict[name]
        _positions_line += '  1  1  \n'

    _positions_line += '"\n\n'
    
    _elements, v = zip(*zipped_coordinates)
    _positions_line += 'number_of_atoms="%d"\n' %len(_elements)
    _positions_line += 'number_of_species="%d"\n' %len(set(_elements))
    _positions_line += 'number_of_orbitals="%d"\n' %sum( [ num_orbital_dict[e] for e in _elements])

    # the following will be used by LCR.dat0 in bias_0.0 calculations
    ion_begin = num_atom_left - n_remove_left + ileft
    num_atoms = len(_elements)
    state_begin = 0
    for i in range(ion_begin):
       state_begin += num_orbital_dict[_elements[i]]

    center_ctrl={'ion_begin':ion_begin, 'state_begin':state_begin, 'num_atoms':num_atoms}
 
    
    return _positions_line, center_ctrl


