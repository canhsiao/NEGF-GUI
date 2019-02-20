

import pymol
from pymol import cmd
from PyQt4 import QtGui, QtCore

from distutils.sysconfig import get_python_lib
from drawbox import *

## presumably need to import pickle module twice to make it work properly:
#import pickle
#import pickle
import json
import codecs

class conf:
    def __init__(self, lattice, elements, coords):
        self.lattice = lattice
        self.elements = elements
        self.coords = coords
class Configuration(QtGui.QWidget):
    """
       Widget for the basic setup of a NCSURMG calculation.
    """


    # member functions:

    def __init__(self, parent = None):
        """
           Constructor.

           @param parent : The parent widget.
        """

        ################ __init__ : Initialize base class 
        QtGui.QWidget.__init__(self, parent)

        ################ __init__ : define the non-GUI variables: 

        
        elements = ['C']
        a = 12.234
        b = 14.234
        c = 8.156
        lattice = [a, b, c]

        coords = [ [ 4.078     ,  4.078     ,  0.        ],
                   [ 4.078     ,  8.156     ,  0.        ],
                   [ 4.078     ,  8.156     ,  0.        ],
                   [ 4.078     ,  8.156     ,  0.        ]]



        self.conf = []
        conf1 = conf(lattice, elements, coords)
        self.conf.append(conf1)
        self.conf.append(conf1)
        self.conf.append(conf1)


   # Main layout
        self._layout = QtGui.QVBoxLayout()
        self.setLayout(self._layout)


        group_box = QtGui.QGroupBox('   Choose input files for NEGF   ')
        self._layout.addWidget(group_box)

        form_layout = QtGui.QFormLayout()
        group_box.setLayout(form_layout)

        self.layouts = range(3)
        self.lattlayouts = range(3)
        self.latticea = range(3)
        self.labels = range(3)
        self.inputfiles = range(3)
        self.buttons = range(3)
        self.pymolshow = range(3)
        self.quitshow = range(3)
        inputtype = ['negf ', 'lead1', 'lead2']

        for i in range(3):
           self.layouts[i]  = QtGui.QHBoxLayout()

           self.labels[i] =   QtGui.QLabel('input file for '+inputtype[i])
           self.inputfiles[i] =    QtGui.QLineEdit('./input_negf.xyz')
           self.buttons[i] =  QtGui.QPushButton('Browse...')
           self.pymolshow[i] =  QtGui.QPushButton('Pymol Show')
           self.quitshow[i] =  QtGui.QPushButton('reinit Pymol')

           self.layouts[i].addWidget(self.labels[i] )
           self.layouts[i].addWidget(self.inputfiles[i]  )
           self.layouts[i].addWidget(self.buttons[i])
           self.layouts[i].addWidget(self.pymolshow[i])
           self.layouts[i].addWidget(self.quitshow[i])

           self.inputfiles[i].setToolTip('edit the input file name')
           self.buttons[i].setToolTip('select an nput file name')

           self.buttons[i].clicked.connect( self.createConnect(i) )
           self.pymolshow[i].clicked.connect( self.createshow(i) )
           self.quitshow[i].clicked.connect( self.quitpymol )

           form_layout.addRow(self.layouts[i])
           
           self.lattlayouts[i]  = QtGui.QHBoxLayout()

           lattlabel =   QtGui.QLabel('              lattice constant:')
          # self.latticea[i] =  QtGui.QLineEdit('0.0   0.0   0.0')
           self.latticea[i] =  QtGui.QLabel('0.0   0.0   0.0')

           self.lattlayouts[i].addWidget(lattlabel )
           self.lattlayouts[i].addWidget(self.latticea[i])


           form_layout.addRow(self.lattlayouts[i])
           


    def selectfile(self, i):        

        dialog = QtGui.QFileDialog(self, options = QtGui.QFileDialog.DontUseNativeDialog)
        if QtCore.QDir( self.inputfiles[i].text() ).exists():
            dialog.selectFile( self.inputfiles[i].text() )
        if dialog.exec_():
            self.inputfiles[i].setText(dialog.selectedFiles()[0])
        self.open_and_read(self.inputfiles[i].text(), i)  

    def createConnect(self, i):
        """
                   internal lambda-creating function to connect
           parameter-free signal from radio buttons for PP variants to
                   a parameter-accepting class method
        """
        return lambda: self.selectfile(i)


    def open_and_read(self,filename, i):
        try:
            f = open (filename)
            num_atoms = int(f.readline())
            comments = f.readline()
            elements = []
            coords = []
            for k in range(num_atoms):
                line = f.readline()
                linesp = line.split()
                elements.append(linesp[0])
                coords.append([float(linesp[1]), float(linesp[2]), float(linesp[3])])
            cellinfo = f.readline()
            line = f.readline()
            linesp = line.split()
            lattice = [float(linesp[0]), float(linesp[1]), float(linesp[2])]
   
            self.conf[i] = conf(lattice, elements, coords)            
            self.latticea[i].setText('a = ' +linesp[0] + '         b=' + linesp[1] + '         c=' + linesp[2])
        #    print self.conf[i].lattice
        #    print self.conf[i].elements
        #    print self.conf[i].coords
        except:
            print "no such a file === ", filename
    def createshow(self, i):
        """
                   internal lambda-creating function to connect
           parameter-free signal from radio buttons for PP variants to
                   a parameter-accepting class method
        """
        return lambda: self.structureshow(i)
    def structureshow(self,i):
        pymol.finish_launching()
        filename = self.inputfiles[i].text()
        cmd.load(str(filename))
        cmd.show('spheres')
        minx = 0.0
        miny = 0.0
        minz = 0.0
        maxx = self.conf[i].lattice[0]
        maxy = self.conf[i].lattice[1]
        maxz = self.conf[i].lattice[2]
        
        cmd.extend("drawbox", drawbox(minx, miny, minz, maxx, maxy, maxz, 2.0, 1,1,1))

    def quitpymol(self):
        cmd.reinitialize()



