# written by Wenchang Lu at NCSU

from PyQt4 import QtGui, QtCore

from distutils.sysconfig import get_python_lib

from procgrid3d_to_2d import *

## presumably need to import pickle module twice to make it work properly:
import json
import codecs

class Grids(QtGui.QWidget):
    """
       Widget for the setup grids, including processor grids and space grids
    """

    def __init__(self, parent = None):
        """
           Constructor.

           @param parent : The parent widget.
        """

        QtGui.QWidget.__init__(self, parent)

        try:
            # Main layout
            self._layout = QtGui.QVBoxLayout()
            self.setLayout(self._layout)
            
            # Setup Groupbox
            group_box = QtGui.QGroupBox('Left lead for order-n calculation')
            self._layout.addWidget(group_box)
            
            form_layout = QtGui.QFormLayout()
            group_box.setLayout(form_layout)

            Hlayout = QtGui.QHBoxLayout()
            label = QtGui.QLabel('   wavefunction grids:')
            self._Nx_left = QtGui.QSpinBox()
            self._Nx_left.setMaximum(9000)
            self._Nx_left.setValue(48)
            self._Ny_left = QtGui.QSpinBox()
            self._Ny_left.setMaximum(9000)
            self._Ny_left.setValue(48)
            self._Nz_left = QtGui.QSpinBox()
            self._Nz_left.setMaximum(9000)
            self._Nz_left.setValue(48)

            Hlayout.addWidget(QtGui.QLabel('     Nx='))
            Hlayout.addWidget(self._Nx_left)
            Hlayout.addWidget(QtGui.QLabel('     Ny='))
            Hlayout.addWidget(self._Ny_left)
            Hlayout.addWidget(QtGui.QLabel('     Nz='))
            Hlayout.addWidget(self._Nz_left)

            form_layout.addRow(label,Hlayout)
    
            Hlayout = QtGui.QHBoxLayout()
            label = QtGui.QLabel('   processor grids for 3D space:')
            self._Pex_left = QtGui.QSpinBox()
            self._Pex_left.setMaximum(9000)
            self._Pex_left.setValue(1)
            self._Pey_left = QtGui.QSpinBox()
            self._Pey_left.setMaximum(9000)
            self._Pey_left.setValue(1)
            self._Pez_left = QtGui.QSpinBox()
            self._Pez_left.setMaximum(9000)
            self._Pez_left.setValue(1)

            Hlayout.addWidget(QtGui.QLabel('    Pex='))
            Hlayout.addWidget(self._Pex_left)
            Hlayout.addWidget(QtGui.QLabel('    Pey='))
            Hlayout.addWidget(self._Pey_left)
            Hlayout.addWidget(QtGui.QLabel('    Pez='))
            Hlayout.addWidget(self._Pez_left)

            form_layout.addRow(label,Hlayout)

            label = QtGui.QLabel(' grid spacing:')
            self.hxyz_left = QtGui.QLabel(' hx = 0.350  hy = 0.350  hz = 0.350 bohr aniootropy = 0.0%')
            form_layout.addRow(label,self.hxyz_left)


            # Setup Groupbox
            group_box = QtGui.QGroupBox('Right lead for order-n calculation')
            self._layout.addWidget(group_box)
            
            form_layout = QtGui.QFormLayout()
            group_box.setLayout(form_layout)

            Hlayout = QtGui.QHBoxLayout()
            label = QtGui.QLabel('   wavefunction grids:')
            self._Nx_right = QtGui.QSpinBox()
            self._Nx_right.setMaximum(9000)
            self._Nx_right.setValue(48)
            self._Ny_right = QtGui.QSpinBox()
            self._Ny_right.setMaximum(9000)
            self._Ny_right.setValue(48)
            self._Nz_right = QtGui.QSpinBox()
            self._Nz_right.setMaximum(9000)
            self._Nz_right.setValue(48)

            Hlayout.addWidget(QtGui.QLabel('     Nx='))
            Hlayout.addWidget(self._Nx_right)
            Hlayout.addWidget(QtGui.QLabel('     Ny='))
            Hlayout.addWidget(self._Ny_right)
            Hlayout.addWidget(QtGui.QLabel('     Nz='))
            Hlayout.addWidget(self._Nz_right)

            form_layout.addRow(label,Hlayout)

            Hlayout = QtGui.QHBoxLayout()
            label = QtGui.QLabel('   processor grids for 3D space:')
            self._Pex_right = QtGui.QSpinBox()
            self._Pex_right.setMaximum(9000)
            self._Pex_right.setValue(1)
            self._Pey_right = QtGui.QSpinBox()
            self._Pey_right.setMaximum(9000)
            self._Pey_right.setValue(1)
            self._Pez_right = QtGui.QSpinBox()
            self._Pez_right.setMaximum(9000)
            self._Pez_right.setValue(1)

            Hlayout.addWidget(QtGui.QLabel('    Pex='))
            Hlayout.addWidget(self._Pex_right)
            Hlayout.addWidget(QtGui.QLabel('    Pey='))
            Hlayout.addWidget(self._Pey_right)
            Hlayout.addWidget(QtGui.QLabel('    Pez='))
            Hlayout.addWidget(self._Pez_right)

            form_layout.addRow(label,Hlayout)

            label = QtGui.QLabel(' grid spacing:')
            self.hxyz_right = QtGui.QLabel(' hx = 0.350  hy = 0.350  hz = 0.350 bohr aniootropy = 0.0%')
            form_layout.addRow(label,self.hxyz_right)

            # Setup Groupbox
            group_box = QtGui.QGroupBox('center part for order-n calculation')
            self._layout.addWidget(group_box)
            
            form_layout = QtGui.QFormLayout()
            group_box.setLayout(form_layout)

            Hlayout = QtGui.QHBoxLayout()
            label = QtGui.QLabel('   wavefunction grids:')
            self._Nx_center = QtGui.QSpinBox()
            self._Nx_center.setMaximum(9000)
            self._Nx_center.setValue(48)
            self._Ny_center = QtGui.QSpinBox()
            self._Ny_center.setMaximum(9000)
            self._Ny_center.setValue(48)
            self._Nz_center = QtGui.QSpinBox()
            self._Nz_center.setMaximum(9000)
            self._Nz_center.setValue(48)

            Hlayout.addWidget(QtGui.QLabel('     Nx='))
            Hlayout.addWidget(self._Nx_center)
            Hlayout.addWidget(QtGui.QLabel('     Ny='))
            Hlayout.addWidget(self._Ny_center)
            Hlayout.addWidget(QtGui.QLabel('     Nz='))
            Hlayout.addWidget(self._Nz_center)

            form_layout.addRow(label,Hlayout)
    
            Hlayout = QtGui.QHBoxLayout()
            label = QtGui.QLabel('   processor grids for 3D space:')
            self._Pex_center = QtGui.QSpinBox()
            self._Pex_center.setMaximum(9000)
            self._Pex_center.setValue(1)
            self._Pey_center = QtGui.QSpinBox()
            self._Pey_center.setMaximum(9000)
            self._Pey_center.setValue(1)
            self._Pez_center = QtGui.QSpinBox()
            self._Pez_center.setMaximum(9000)
            self._Pez_center.setValue(1)

            Hlayout.addWidget(QtGui.QLabel('    Pex='))
            Hlayout.addWidget(self._Pex_center)
            Hlayout.addWidget(QtGui.QLabel('    Pey='))
            Hlayout.addWidget(self._Pey_center)
            Hlayout.addWidget(QtGui.QLabel('    Pez='))
            Hlayout.addWidget(self._Pez_center)

            form_layout.addRow(label,Hlayout)

            label = QtGui.QLabel(' grid spacing:')
            self.hxyz_center = QtGui.QLabel(' hx = 0.350  hy = 0.350  hz = 0.350 bohr aniootropy = 0.0%')
            form_layout.addRow(label,self.hxyz_center)
    
            # Setup Groupbox
            group_box = QtGui.QGroupBox(' 3lead NEGF calculation for left(L) and right(R)')
            self._layout.addWidget(group_box)
            
            form_layout = QtGui.QFormLayout()
            group_box.setLayout(form_layout)

            Hlayout = QtGui.QHBoxLayout()
            label = QtGui.QLabel('   processor grids for 3D space(L):')
            self._Pex_left3 = QtGui.QSpinBox()
            self._Pex_left3.setMaximum(9000)
            self._Pex_left3.setValue(1)
            self._Pey_left3 = QtGui.QSpinBox()
            self._Pey_left3.setMaximum(9000)
            self._Pey_left3.setValue(1)
            self._Pez_left3 = QtGui.QSpinBox()
            self._Pez_left3.setMaximum(9000)
            self._Pez_left3.setValue(1)

            Hlayout.addWidget(QtGui.QLabel('    Pex='))
            Hlayout.addWidget(self._Pex_left3)
            Hlayout.addWidget(QtGui.QLabel('    Pey='))
            Hlayout.addWidget(self._Pey_left3)
            Hlayout.addWidget(QtGui.QLabel('    Pez='))
            Hlayout.addWidget(self._Pez_left3)

            form_layout.addRow(label,Hlayout)

            Hlayout = QtGui.QHBoxLayout()
            label = QtGui.QLabel('   processor grids for 3D space(R):')
            self._Pex_right3 = QtGui.QSpinBox()
            self._Pex_right3.setMaximum(9000)
            self._Pex_right3.setValue(1)
            self._Pey_right3 = QtGui.QSpinBox()
            self._Pey_right3.setMaximum(9000)
            self._Pey_right3.setValue(1)
            self._Pez_right3 = QtGui.QSpinBox()
            self._Pez_right3.setMaximum(9000)
            self._Pez_right3.setValue(1)

            Hlayout.addWidget(QtGui.QLabel('    Pex='))
            Hlayout.addWidget(self._Pex_right3)
            Hlayout.addWidget(QtGui.QLabel('    Pey='))
            Hlayout.addWidget(self._Pey_right3)
            Hlayout.addWidget(QtGui.QLabel('    Pez='))
            Hlayout.addWidget(self._Pez_right3)

            form_layout.addRow(label,Hlayout)

    
            # Setup Groupbox
            group_box = QtGui.QGroupBox('NEGF calculation for whole system')
            self._layout.addWidget(group_box)
            
            form_layout = QtGui.QFormLayout()
            group_box.setLayout(form_layout)

            Hlayout = QtGui.QHBoxLayout()
            label = QtGui.QLabel('   processor grids for 3D space:')
            self._Pex_negf = QtGui.QSpinBox()
            self._Pex_negf.setMaximum(9000)
            self._Pex_negf.setValue(1)
            self._Pey_negf = QtGui.QSpinBox()
            self._Pey_negf.setMaximum(9000)
            self._Pey_negf.setValue(1)
            self._Pez_negf = QtGui.QSpinBox()
            self._Pez_negf.setMaximum(9000)
            self._Pez_negf.setValue(1)

            Hlayout.addWidget(QtGui.QLabel('    Pex='))
            Hlayout.addWidget(self._Pex_negf)
            Hlayout.addWidget(QtGui.QLabel('    Pey='))
            Hlayout.addWidget(self._Pey_negf)
            Hlayout.addWidget(QtGui.QLabel('    Pez='))
            Hlayout.addWidget(self._Pez_negf)

            form_layout.addRow(label,Hlayout)
            label = QtGui.QLabel(' ')
            form_layout.addRow(label)

            self.center_periodicity = QtGui.QRadioButton('center part periodicity')
            self.center_periodicity.setChecked(True)
            self.center_periodicity.setToolTip('uncheck it when the two leads are different and the center part cannot be calculated with periodic condition in order-n calculation') 
            form_layout.addRow(self.center_periodicity)
            self._Nx_negf = self._Nx_center.value()+self._Nx_left.value()+self._Nx_right.value()
    
        except:
            print " Grids layout error"

        try:
           self._Nx_left.valueChanged.connect(self.changeothergrid)
           self._Ny_left.valueChanged.connect(self.changeothergrid1)
           self._Nz_left.valueChanged.connect(self.changeothergrid1)

           self._Nx_left.valueChanged.connect(self.get_nx_negf)
           self._Nx_right.valueChanged.connect(self.get_nx_negf)
           self._Nx_center.valueChanged.connect(self.get_nx_negf)
       
           self.get2dgrid()
           self._Pex_left.valueChanged.connect(self.get2dgrid)
           self._Pey_left.valueChanged.connect(self.get2dgrid)
           self._Pez_left.valueChanged.connect(self.get2dgrid)
           self._Pex_right.valueChanged.connect(self.get2dgrid)
           self._Pey_right.valueChanged.connect(self.get2dgrid)
           self._Pez_right.valueChanged.connect(self.get2dgrid)
           self._Pex_center.valueChanged.connect(self.get2dgrid)
           self._Pey_center.valueChanged.connect(self.get2dgrid)
           self._Pez_center.valueChanged.connect(self.get2dgrid)
           self._Pex_left3.valueChanged.connect(self.get2dgrid)
           self._Pey_left3.valueChanged.connect(self.get2dgrid)
           self._Pez_left3.valueChanged.connect(self.get2dgrid)
           self._Pex_right3.valueChanged.connect(self.get2dgrid)
           self._Pey_right3.valueChanged.connect(self.get2dgrid)
           self._Pez_right3.valueChanged.connect(self.get2dgrid)
           self._Pex_negf.valueChanged.connect(self.get2dgrid)
           self._Pey_negf.valueChanged.connect(self.get2dgrid)
           self._Pez_negf.valueChanged.connect(self.get2dgrid)

           self.connect(self.center_periodicity, QtCore.SIGNAL('clicked()'), self.changeothergrid)
        except:
           print " Grids value change error"

    def get2dgrid(self):
        
        pex = self._Pex_left.value()
        pey = self._Pey_left.value()
        pez = self._Pez_left.value()
        nprow, npcol = procgrid3d_to_2d(pex, pey, pez)
        self._nprow_left = nprow
        self._npcol_left = npcol
        
        pex = self._Pex_right.value()
        pey = self._Pey_right.value()
        pez = self._Pez_right.value()
        nprow, npcol = procgrid3d_to_2d(pex, pey, pez)
        self._nprow_right = nprow
        self._npcol_right = npcol
        
        pex = self._Pex_center.value()
        pey = self._Pey_center.value()
        pez = self._Pez_center.value()
        nprow, npcol = procgrid3d_to_2d(pex, pey, pez)
        self._nprow_center = nprow
        self._npcol_center = npcol
        
        pex = self._Pex_left3.value()
        pey = self._Pey_left3.value()
        pez = self._Pez_left3.value()
        nprow, npcol = procgrid3d_to_2d(pex, pey, pez)
        self._nprow_left3 = nprow
        self._npcol_left3 = npcol
        
        pex = self._Pex_right3.value()
        pey = self._Pey_right3.value()
        pez = self._Pez_right3.value()
        nprow, npcol = procgrid3d_to_2d(pex, pey, pez)
        self._nprow_right3 = nprow
        self._npcol_right3 = npcol
        
        pex = self._Pex_negf.value()
        pey = self._Pey_negf.value()
        pez = self._Pez_negf.value()
        nprow, npcol = procgrid3d_to_2d(pex, pey, pez)
        self._nprow_negf = nprow
        self._npcol_negf = npcol

    def lattparameters(self, configuration, misc):
        electrodes = configuration.conf

        vectors1 = electrodes[1].lattice
        vectors2 = electrodes[2].lattice
        vectors3 = electrodes[0].lattice
        self.aleft = vectors1[0] 
        self.aright = vectors2[0]
        self.anegf = vectors3[0]
        self.acenter = self.anegf - self.aleft - self.aright
        self.b = vectors1[1]
        self.c = vectors1[2]

        khlevel = int(misc._khlevel.text())
        self.gridfactor = 2**khlevel

        self._Nx_left.setSingleStep(self.gridfactor)
        self.changeothergrid()


    def changeothergrid(self):
        try:
            ratio = self._Nx_left.value() /self.aleft 

            ngrid = int(self.b * ratio)
            ngrid = (ngrid + self.gridfactor -1) /self.gridfactor * self.gridfactor
            self._Ny_left.setValue(ngrid)

            ngrid = int(self.c * ratio)
            ngrid = (ngrid + self.gridfactor -1) /self.gridfactor * self.gridfactor
            self._Nz_left.setValue(ngrid)

            ngrid = int(self.aright * ratio)
            ngrid = (ngrid + self.gridfactor -1) /self.gridfactor * self.gridfactor
            self._Nx_right.setValue(ngrid)
            if(self.center_periodicity.isChecked()):
                self.acenter = self.anegf - self.aleft - self.aright
            else:
                self.acenter = self.anegf

            ngrid = int(self.acenter * ratio)
            ngrid = (ngrid + self.gridfactor -1) /self.gridfactor * self.gridfactor
            self._Nx_center.setValue(ngrid)
            self.updatehxyz()
        except:
            print "load the coordinate files .xyz ... first"

    def get_nx_negf(self):
        if(self.center_periodicity.isChecked()):
            self._Nx_negf = self._Nx_center.value()+self._Nx_left.value()+self._Nx_right.value()
        else:
            self._Nx_negf = self._Nx_center.value()
            

    def changeothergrid1(self):
        self._Ny_right.setValue(self._Ny_left.value())
        self._Nz_right.setValue(self._Nz_left.value())
        self._Ny_center.setValue(self._Ny_left.value())
        self._Nz_center.setValue(self._Nz_left.value())
        self.updatehxyz()
        

    def updatehxyz(self):
        hx = self.aleft/self._Nx_left.value()
        hy = self.b/self._Ny_left.value()
        hz = self.c/self._Nz_left.value()
        hmax = hx
        if hmax < hy: hmax = hy
        if hmax < hz: hmax = hz
        hmin = hx
        if hmin > hy: hmin = hy
        if hmin > hz: hmin = hz

        anis = str("%.1f" %((hmax/hmin-1) * 100))+'%'

        hx = str("%.3f" %hx)
        hy = str("%.3f" %hy)
        hz = str("%.3f" %hz)

        self.hxyz_left.setText(' hx ='+hx+'  hy ='+hy+' hz ='+hz+' bohr anisotropy='+anis)

        hx = self.aright/self._Nx_right.value()
        hy = self.b/self._Ny_right.value()
        hz = self.c/self._Nz_right.value()
        hmax = hx
        if hmax < hy: hmax = hy
        if hmax < hz: hmax = hz
        hmin = hx
        if hmin > hy: hmin = hy
        if hmin > hz: hmin = hz

        anis = str("%.1f" %((hmax/hmin-1) * 100))+'%'

        hx = str("%.3f" %hx)
        hy = str("%.3f" %hy)
        hz = str("%.3f" %hz)

        self.hxyz_right.setText(' hx ='+hx+'  hy ='+hy+' hz ='+hz+' bohr anisotropy='+anis)

        hx = self.acenter/self._Nx_center.value()
        hy = self.b/self._Ny_center.value()
        hz = self.c/self._Nz_center.value()
        hmax = hx
        if hmax < hy: hmax = hy
        if hmax < hz: hmax = hz
        hmin = hx
        if hmin > hy: hmin = hy
        if hmin > hz: hmin = hz

        anis = str("%.1f" %((hmax/hmin-1) * 100))+'%'

        hx = str("%.3f" %hx)
        hy = str("%.3f" %hy)
        hz = str("%.3f" %hz)

        self.hxyz_center.setText(' hx ='+hx+'  hy ='+hy+' hz ='+hz+' bohr anisotropy='+anis)

    def state(self):
        """
           @return A dictionary containing the widget state.
        """
        try:
           input_grids_left_lines = '\n#space grid and processor grid control\n\n'
           input_grids_left_lines += 'wavefunction_grid ="' 
           input_grids_left_lines +='%d ' %self._Nx_left.value()
           input_grids_left_lines +='%d ' %self._Ny_left.value()
           input_grids_left_lines +='%d' %self._Nz_left.value() + '"\n'
           num_proc = self._Pex_left.value() * self._Pey_left.value() * self._Pez_left.value() 
           self.num_proc_left = num_proc
           input_grids_left_lines +='num_processor ="' +'%d'%num_proc +'"\n'
           input_grids_left_lines +='processor_grid="'
           input_grids_left_lines +='%d ' %self._Pex_left.value()
           input_grids_left_lines +='%d ' %self._Pey_left.value()
           input_grids_left_lines +='%d' %self._Pez_left.value() + '"\n'
           input_grids_left_lines +='Hamiltonia_processor_grid ="'
           input_grids_left_lines +='%d ' %self._nprow_left
           input_grids_left_lines +='%d' %self._npcol_left + '"\n'

           input_grids_right_lines = '\n#space grid and processor grid control\n\n'
           input_grids_right_lines += 'wavefunction_grid ="' 
           input_grids_right_lines +='%d ' %self._Nx_right.value()
           input_grids_right_lines +='%d ' %self._Ny_right.value()
           input_grids_right_lines +='%d' %self._Nz_right.value() + '"\n'
           num_proc = self._Pex_right.value() * self._Pey_right.value() * self._Pez_right.value() 
           self.num_proc_right = num_proc
           input_grids_right_lines +='num_processor ="' +'%d'%num_proc +'"\n'
           input_grids_right_lines +='processor_grid="'
           input_grids_right_lines +='%d ' %self._Pex_right.value()
           input_grids_right_lines +='%d ' %self._Pey_right.value()
           input_grids_right_lines +='%d' %self._Pez_right.value() + '"\n'
           input_grids_right_lines +='Hamiltonia_processor_grid ="'
           input_grids_right_lines +='%d ' %self._nprow_right
           input_grids_right_lines +='%d' %self._npcol_right + '"\n'

        except:
           print "Grid  state error1"
        try:
           input_grids_center_lines = '\n#space grid and processor grid control\n\n'
           input_grids_center_lines += 'wavefunction_grid ="' 
           input_grids_center_lines +='%d ' %self._Nx_center.value()
           input_grids_center_lines +='%d ' %self._Ny_center.value()
           input_grids_center_lines +='%d' %self._Nz_center.value() + '"\n'
           num_proc = self._Pex_center.value() * self._Pey_center.value() * self._Pez_center.value() 
           self.num_proc_center = num_proc
           input_grids_center_lines +='num_processor ="' +'%d'%num_proc +'"\n'
           input_grids_center_lines +='processor_grid="'
           input_grids_center_lines +='%d ' %self._Pex_center.value()
           input_grids_center_lines +='%d ' %self._Pey_center.value()
           input_grids_center_lines +='%d' %self._Pez_center.value() + '"\n'
           input_grids_center_lines +='Hamiltonia_processor_grid ="'
           input_grids_center_lines +='%d ' %self._nprow_center
           input_grids_center_lines +='%d' %self._npcol_center + '"\n'
           
        except:
           print "Grid  state error2"
        try:
           input_grids_left3_lines = '\n#space grid and processor grid control\n\n'
           input_grids_left3_lines += 'wavefunction_grid ="' 
           input_grids_left3_lines +='%d ' %(self._Nx_left.value() *3)
           input_grids_left3_lines +='%d ' %self._Ny_left.value()
           input_grids_left3_lines +='%d' %self._Nz_left.value() + '"\n'
           num_proc = self._Pex_left3.value() * self._Pey_left3.value() * self._Pez_left3.value() 
           self.num_proc_left3 = num_proc
           input_grids_left3_lines +='num_processor ="' +'%d'%num_proc +'"\n'
           input_grids_left3_lines +='processor_grid="'
           input_grids_left3_lines +='%d ' %self._Pex_left3.value()
           input_grids_left3_lines +='%d ' %self._Pey_left3.value()
           input_grids_left3_lines +='%d' %self._Pez_left3.value() + '"\n'
           input_grids_left3_lines +='Hamiltonia_processor_grid ="'
           input_grids_left3_lines +='%d ' %self._nprow_left3
           input_grids_left3_lines +='%d' %self._npcol_left3 + '"\n'
           
           input_grids_right3_lines = '\n#space grid and processor grid control\n\n'
           input_grids_right3_lines += 'wavefunction_grid ="' 
           input_grids_right3_lines +='%d ' %(self._Nx_right.value()*3)
           input_grids_right3_lines +='%d ' %self._Ny_right.value()
           input_grids_right3_lines +='%d' %self._Nz_right.value() + '"\n'
           num_proc = self._Pex_right3.value() * self._Pey_right3.value() * self._Pez_right3.value() 
           self.num_proc_right3 = num_proc
           input_grids_right3_lines +='num_processor ="' +'%d'%num_proc +'"\n'
           input_grids_right3_lines +='processor_grid="'
           input_grids_right3_lines +='%d ' %self._Pex_right3.value()
           input_grids_right3_lines +='%d ' %self._Pey_right3.value()
           input_grids_right3_lines +='%d' %self._Pez_right3.value() + '"\n'
           input_grids_right3_lines +='Hamiltonia_processor_grid ="'
           input_grids_right3_lines +='%d ' %self._nprow_right3
           input_grids_right3_lines +='%d' %self._npcol_right3 + '"\n'
           
        except:
           print "Grid  state error3"
        try:
           input_grids_negf_lines = '\n#space grid and processor grid control\n\n'
           input_grids_negf_lines += 'wavefunction_grid ="' 
           input_grids_negf_lines +='%d ' %self._Nx_negf
           input_grids_negf_lines +='%d ' %self._Ny_center.value()
           input_grids_negf_lines +='%d' %self._Nz_center.value() + '"\n'
           num_proc = self._Pex_negf.value() * self._Pey_negf.value() * self._Pez_negf.value() 
           self.num_proc_negf = num_proc
        except:
           print "Grid  state error4"
        try:
           input_grids_negf_lines +='num_processor ="' +'%d'%num_proc +'"\n'
           input_grids_negf_lines +='processor_grid="'
           input_grids_negf_lines +='%d ' %self._Pex_negf.value()
           input_grids_negf_lines +='%d ' %self._Pey_negf.value()
           input_grids_negf_lines +='%d' %self._Pez_negf.value() + '"\n'
           input_grids_negf_lines +='Hamiltonia_processor_grid ="'
           input_grids_negf_lines +='%d ' %self._nprow_negf
           input_grids_negf_lines +='%d' %self._npcol_negf + '"\n'
        except:
           print "Grid  state error5"
        try:
           
           input_oneatom_grid_lines  = '\n# number of grids in space \n\nwavefunction_grid ="' 
           input_oneatom_grid_lines +='%d ' %self._Nx_left.value()
           input_oneatom_grid_lines +='%d ' %self._Ny_left.value()
           input_oneatom_grid_lines +='%d' %self._Nz_left.value() + '"\n'
        except:
           print "Grid  state error"
        state={ 'input_oneatom_grid_lines': input_oneatom_grid_lines,
                'input_grids_left_lines': input_grids_left_lines,
                'input_grids_right_lines': input_grids_right_lines,
                'input_grids_center_lines': input_grids_center_lines,
                'input_grids_left3_lines': input_grids_left3_lines,
                'input_grids_right3_lines': input_grids_right3_lines,
                'input_grids_negf_lines': input_grids_negf_lines
                }
        return state

    ######### end of state(self):


