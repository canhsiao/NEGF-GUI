# written by Wenchang Lu


from PyQt4 import QtGui, QtCore

from distutils.sysconfig import get_python_lib


class Negf_para(QtGui.QWidget):
    """
       Widget for the basic setup of a NCSURMG calculation.
    """


    # location of the plugin parts:
    _ncsurmg_addon_path = "/AddOns/NCSURMG/"


    # member functions:

    def __init__(self, parent = None):
        """
           Constructor.

           @param parent : The parent widget.
        """

        ################ __init__ : Initialize base class 
        QtGui.QWidget.__init__(self, parent)

        ################ __init__ : define the non-GUI variables: 

        ##################  __init__ : set up GUI:
        
        # Main layout

        try:
            # Main layout
            self._layout = QtGui.QVBoxLayout()
            self.setLayout(self._layout)
            # Setup Groupbox
            group_box = QtGui.QGroupBox('Basics ')
            self._layout.addWidget(group_box)
            
            form_layout = QtGui.QFormLayout()
            group_box.setLayout(form_layout)

            Hlayout = QtGui.QHBoxLayout()

            label = QtGui.QLabel('number of probes')
            self.num_probe = QtGui.QSpinBox()
            self.num_probe.setValue(2)
            Hlayout.addWidget(label)
            Hlayout.addWidget(self.num_probe)

            label = QtGui.QLabel('number of blocks')
            self.num_block = QtGui.QSpinBox()
            self.num_block.setValue(3)
            Hlayout.addWidget(label)
            Hlayout.addWidget(self.num_block)
            form_layout.addRow(Hlayout)

            Hlayout = QtGui.QHBoxLayout()

            label = QtGui.QLabel('nprow')
            self.nprow = QtGui.QSpinBox()
            self.nprow.setValue(1)
            Hlayout.addWidget(label)
            Hlayout.addWidget(self.nprow)

            label = QtGui.QLabel('npcol')
            self.npcol = QtGui.QSpinBox()
            self.npcol.setValue(1)
            Hlayout.addWidget(label)
            Hlayout.addWidget(self.npcol)

            label = QtGui.QLabel('processor grid for block matrix operation ')
            form_layout.addRow(label, Hlayout)

            Hlayout = QtGui.QHBoxLayout()
            label = QtGui.QLabel('small imaginary energy')
            self.Eimag = QtGui.QLineEdit()
            self.Eimag.setText('0.0005') 
            Hlayout.addWidget(label)
            Hlayout.addWidget(self.Eimag)

            label = QtGui.QLabel('kbT')
            self.kbt = QtGui.QLineEdit()
            self.kbt.setText('0.05') 
            Hlayout.addWidget(label)
            Hlayout.addWidget(self.kbt)
            form_layout.addRow(Hlayout)

            Hlayout = QtGui.QHBoxLayout()

            label = QtGui.QLabel('nkx')
            self.nkx = QtGui.QSpinBox()
            self.nkx.setMaximum(20001)
            self.nkx.setValue(2001)
            Hlayout.addWidget(label)
            Hlayout.addWidget(self.nkx)

            label = QtGui.QLabel('nky')
            self.nky = QtGui.QSpinBox()
            self.nky.setValue(1)
            self.nky.setMaximum(20001)
            Hlayout.addWidget(label)
            Hlayout.addWidget(self.nky)
            label = QtGui.QLabel('nkz')
            self.nkz = QtGui.QSpinBox()
            self.nkz.setValue(1)
            self.nkz.setMaximum(20001)
            Hlayout.addWidget(label)
            Hlayout.addWidget(self.nkz)

            label = QtGui.QLabel('Kpoints for Trans calculations')
            form_layout.addRow(label, Hlayout)

            # Setup Groupbox
            group_box = QtGui.QGroupBox('Energy windows for transmission calculations ')
            self._layout.addWidget(group_box)
            
            form_layout = QtGui.QFormLayout()
            group_box.setLayout(form_layout)

            Hlayout = QtGui.QHBoxLayout()
            label = QtGui.QLabel('for 3lead-lead1')
            self.Emin_lead1 = QtGui.QLineEdit()
            self.Emin_lead1.setText('-2.0') 
            Hlayout.addWidget(QtGui.QLabel('Emin'))
            Hlayout.addWidget(self.Emin_lead1)
            self.Emax_lead1 = QtGui.QLineEdit()
            self.Emax_lead1.setText('2.0') 
            Hlayout.addWidget(QtGui.QLabel('Emax'))
            Hlayout.addWidget(self.Emax_lead1)

            self.Epoint_lead1 = QtGui.QSpinBox()
            self.Epoint_lead1.setMaximum(20001)
            self.Epoint_lead1.setValue(401)
            Hlayout.addWidget(QtGui.QLabel('num of energy points'))
            Hlayout.addWidget(self.Epoint_lead1)
            form_layout.addRow(label,Hlayout)

            Hlayout = QtGui.QHBoxLayout()
            label = QtGui.QLabel('for 3lead-lead2')
            self.Emin_lead2 = QtGui.QLineEdit()
            self.Emin_lead2.setText('-2.0') 
            Hlayout.addWidget(QtGui.QLabel('Emin'))
            Hlayout.addWidget(self.Emin_lead2)
            self.Emax_lead2 = QtGui.QLineEdit()
            self.Emax_lead2.setText('2.0') 
            Hlayout.addWidget(QtGui.QLabel('Emax'))
            Hlayout.addWidget(self.Emax_lead2)

            self.Epoint_lead2 = QtGui.QSpinBox()
            self.Epoint_lead2.setMaximum(20001)
            self.Epoint_lead2.setValue(401)
            Hlayout.addWidget(QtGui.QLabel('num of energy points'))
            Hlayout.addWidget(self.Epoint_lead2)
            form_layout.addRow(label,Hlayout)

            Hlayout = QtGui.QHBoxLayout()
            label = QtGui.QLabel('for bias_0.0')
            self.Emin_negf = QtGui.QLineEdit()
            self.Emin_negf.setText('-2.0') 
            Hlayout.addWidget(QtGui.QLabel('Emin'))
            Hlayout.addWidget(self.Emin_negf)
            self.Emax_negf = QtGui.QLineEdit()
            self.Emax_negf.setText('2.0') 
            Hlayout.addWidget(QtGui.QLabel('Emax'))
            Hlayout.addWidget(self.Emax_negf)

            self.Epoint_negf = QtGui.QSpinBox()
            self.Epoint_negf.setMaximum(20001)
            self.Epoint_negf.setValue(401)
            Hlayout.addWidget(QtGui.QLabel('num of energy points'))
            Hlayout.addWidget(self.Epoint_negf)
            form_layout.addRow(label,Hlayout)

            group_box = QtGui.QGroupBox('Complex energy integration')
            self._layout.addWidget(group_box)
            
            form_layout = QtGui.QFormLayout()
            group_box.setLayout(form_layout)

            Hlayout = QtGui.QHBoxLayout()

            label = QtGui.QLabel('ncircle')
            self.ncircle = QtGui.QSpinBox()
            self.ncircle.setMaximum(1000)
            self.ncircle.setValue(50)
            Hlayout.addWidget(label)
            Hlayout.addWidget(self.ncircle)
            
            label = QtGui.QLabel('nmax_gq1')
            self.nmax_gq1 = QtGui.QSpinBox()
            self.nmax_gq1.setMaximum(1000)
            self.nmax_gq1.setValue(50)
            Hlayout.addWidget(label)
            Hlayout.addWidget(self.nmax_gq1)

            label = QtGui.QLabel('nmax_gq2')
            self.nmax_gq2 = QtGui.QSpinBox()
            self.nmax_gq2.setMaximum(1000)
            self.nmax_gq2.setValue(128)
            Hlayout.addWidget(label)
            Hlayout.addWidget(self.nmax_gq2)
        
            form_layout.addRow(Hlayout)
    
            Hlayout = QtGui.QHBoxLayout()
            label = QtGui.QLabel('Elowbound(eV)')
            self.elowbound = QtGui.QLineEdit()
            self.elowbound.setText('-30.0') 
            Hlayout.addWidget(label)
            Hlayout.addWidget(self.elowbound)
            
            label = QtGui.QLabel('KT(eV)')
            self.kt = QtGui.QLineEdit()
            self.kt.setText('0.025') 
            Hlayout.addWidget(label)
            Hlayout.addWidget(self.kt)

            label = QtGui.QLabel('GAMMA(eV)')
            self.gamma = QtGui.QLineEdit()
            self.gamma.setText('0.5') 
            Hlayout.addWidget(label)
            Hlayout.addWidget(self.gamma)
    
            form_layout.addRow(Hlayout)

            Hlayout = QtGui.QHBoxLayout()
            label = QtGui.QLabel('Delta2(eV)')
            self.delta2 = QtGui.QLineEdit()
            self.delta2.setText('2.05') 
            Hlayout.addWidget(label)
            Hlayout.addWidget(self.delta2)

            label = QtGui.QLabel('Delta(eV)')
            self.delta = QtGui.QLineEdit()
            self.delta.setText('1.0E-6') 
            Hlayout.addWidget(label)
            Hlayout.addWidget(self.delta)

            form_layout.addRow(Hlayout)


        except:
            showError()

    def state(self):
        """
           @return A dictionary containing the widget state.
        """
        state={ 
                 }
        return state

    ######### end of state(self):



