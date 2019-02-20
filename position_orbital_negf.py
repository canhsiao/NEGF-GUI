import os

# here is the function that will return the atomic coor and orbital
#centers

def position_orbital_negf(conf1, conf2,conf3, num_orbital_dict, orbital_radius_dict):
    """
    @return ascii string with atomic position and orbital centers
    """
    
    a1 = conf1.lattice[0]
    a2 = conf2.lattice[0]
    a3 = conf3.lattice[0]
    b = conf1.lattice[1]
    c = conf1.lattice[2]
    a2 = a2 - a1 -a3
    a = a1+a2+a3
    # put unitcell information into the snippet

    _positions_line = """

# Lattice constants in (x, y, z) directions
# a, b, c, cos(alpha), cos(beta), cos(gamma)
a_length="%s" b_length="%s" c_length="%s"
alpha="0.0" beta="0.0" gamma="0.0"

""" %(a,b,c)



    _atom_format = " %s     %.12e    %.12e    %.12e      1   \n"
    _orbital_format = " %d     %.12e    %.12e    %.12e  "
    _elements1 = conf1.elements 
    _elements2 = conf2.elements 
    _elements3 = conf3.elements 
    _element_types = set(_elements1+_elements2+_elements3)
    zipped_coordinates1 = zip(_elements1, conf1.coords)
    zipped_coordinates2 = zip(_elements2, conf2.coords)
    zipped_coordinates3 = zip(_elements3, conf3.coords)

# remove the buffer layer first and then add them as left and right lead
# part
    num_atoms_left = len(_elements1)
    num_atoms_right = len(_elements3)
    num_atoms_negf = len(_elements2)

    del zipped_coordinates2[(num_atoms_negf-num_atoms_right):num_atoms_negf]
    del zipped_coordinates2[0:num_atoms_left]


    zipped_tem = zipped_coordinates2
    zipped_coordinates2 = sorted (zipped_tem, key= lambda v:v[1][0])

    


    _positions_line += 'atoms=\n"\n'

    for name,v in zipped_coordinates1:
        _positions_line += ( _atom_format % (name, v[0],v[1],v[2]) )
    for name,v in zipped_coordinates2:
        _positions_line += ( _atom_format % (name, v[0],v[1],v[2]) )
    for name,v in zipped_coordinates3:
        _positions_line += ( _atom_format % (name, v[0]+a1+a2,v[1],v[2]) )

    _positions_line += '"\n'


    _positions_line += '\n #  orbital centers  \n'
    _positions_line += 'orbitals=\n"\n'

    for name,v in zipped_coordinates1:
        _positions_line += ( _orbital_format % (num_orbital_dict[name], v[0],v[1],v[2]) )
        _positions_line +=  orbital_radius_dict[name]
        _positions_line += '  1  1  \n'
    for name,v in zipped_coordinates2:
        _positions_line += ( _orbital_format % (num_orbital_dict[name], v[0],v[1],v[2]) )
        _positions_line +=  orbital_radius_dict[name]
        _positions_line += '  1  1  \n'
    for name,v in zipped_coordinates3:
        _positions_line += ( _orbital_format % (num_orbital_dict[name], v[0]+a1+a2,v[1],v[2]) )
        _positions_line +=  orbital_radius_dict[name]
        _positions_line += '  1  1  \n'

    _positions_line += '"\n\n'

    _positions_line += 'number_of_atoms="%d"\n' %num_atoms_negf
    _positions_line += 'number_of_species="%d"\n' %len(_element_types)
    num_orbitals1 = sum( [ num_orbital_dict[e] for e in _elements1])
    num_orbitals2 = sum( [ num_orbital_dict[e] for e in _elements2])
    num_orbitals3 = sum( [ num_orbital_dict[e] for e in _elements3])

    num_orbitals2 -= num_orbitals1 + num_orbitals3
    num_orbitals = num_orbitals1 + num_orbitals2 + num_orbitals3
    _positions_line += 'number_of_orbitals="%d"\n' %num_orbitals

    _positions_line += 'metalic="true"\n'
    _positions_line += 'num_blocks="3"\n'
    _positions_line += 'blocks_dim="%d %d %d"\n'%(num_orbitals1,num_orbitals2,num_orbitals3)




    
    return _positions_line


