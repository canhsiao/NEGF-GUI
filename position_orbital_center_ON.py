import os

# here is the function that will return the atomic coor and orbital
#centers

def position_orbital_center_ON(configuration, num_orbital_dict, orbital_radius_dict):
    """
    @return ascii string with atomic position and orbital centers
    """
    
    _atom_format = " %s     %.12e    %.12e    %.12e      1   \n"
    _orbital_format = " %d     %.12e    %.12e    %.12e  "
    _elements = configuration.conf[0].elements 
    _element_types = set(_elements) 
    
    electrodes = configuration.conf
    ele_left = electrodes[1].elements
    num_atom_left = len(ele_left)
    ele_right = electrodes[2].elements
    num_atom_right = len(ele_right)

    vectors = electrodes[1].lattice
    zshift = vectors[0]
    

    zipped_tem  = zip(_elements, configuration.conf[0].coords)
    zipped_coordinates = sorted (zipped_tem, key= lambda v:v[1][0])
    
    del zipped_coordinates[0:num_atom_left]
    item = len(zipped_coordinates)
    del zipped_coordinates[item-num_atom_right:item]


    a1 = electrodes[1].lattice[0]
    a2 = electrodes[2].lattice[0]
    a3 = electrodes[0].lattice[0]
    b = electrodes[1].lattice[1]
    c = electrodes[1].lattice[2]

    a = a3-a2-a1
    # put unitcell information into the snippet

    _positions_line = """

# Lattice constants in (x, y, z) directions
# a, b, c, cos(alpha), cos(beta), cos(gamma)
a_length="%s" b_length="%s" c_length="%s"
alpha="0.0" beta="0.0" gamma="0.0"

""" %(a,b,c)

    
    _positions_line += '\n #  atomic coordinates  \n'
    _positions_line += 'atoms=\n"\n'

    for name,v in zipped_coordinates:
        _positions_line += ( _atom_format % (name, v[0]-zshift,v[1],v[2]) )

    _positions_line += '"\n'


    _positions_line += '\n #  orbital centers  \n'
    _positions_line += 'orbitals=\n"\n'

    for name,v in zipped_coordinates:
        _positions_line += ( _orbital_format % (num_orbital_dict[name], v[0]-zshift,v[1],v[2]) )
        _positions_line +=  orbital_radius_dict[name]
        _positions_line += '  1  1  \n'

    _positions_line += '"\n\n'
    
    _elements, v = zip(*zipped_coordinates)
    _positions_line += 'number_of_atoms="%d"\n' %len(_elements)
    _positions_line += 'number_of_species="%d"\n' %len(_element_types)
    _positions_line += 'number_of_orbitals="%d"\n' %sum( [ num_orbital_dict[e] for e in _elements])

    
    return _positions_line


