import os

# here is the function that will return the atomic coor and orbital
#centers

def position_orbital(configuration, num_orbital_dict, orbital_radius_dict):
    """
    @return ascii string with atomic position and orbital centers
    """
    
    _atom_format = " %s     %.12e    %.12e    %.12e      1  \n"
    _orbital_format = " %d     %.12e    %.12e    %.12e  "
    _elements = configuration.elements 
    _element_types = set(_elements) 
    zipped_coordinates = zip(_elements, configuration.coords)
    
    _positions_line = '\n #  atomic coordinates  \n'
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

    _positions_line += 'number_of_atoms="%d"\n' %len(_elements)
    _positions_line += 'number_of_species="%d"\n' %len(_element_types)
    _positions_line += 'number_of_orbitals="%d"\n' %sum( [ num_orbital_dict[e] for e in _elements])

    
    return _positions_line


