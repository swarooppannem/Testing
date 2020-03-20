import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class BcpMain(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        VBOX_MAIN = QtWidgets.QVBoxLayout()
        
        HBOX_MAIN = QtWidgets.QHBoxLayout()
        
        self.FRAME_FOR_INPUTS = QtWidgets.QFrame()
        
        self.CreateInputWidgets()
        
        HBOX_MAIN.addWidget(self.FRAME_FOR_INPUTS)
        
        VBOX_MAIN.addLayout(HBOX_MAIN)
        VBOX_MAIN.addStretch(1)
    
        self.setLayout(VBOX_MAIN)

        self.show()
        
    def CreateInputWidgets(self):
        
        VBOX_FOR_INPUTS = QtWidgets.QVBoxLayout(self.FRAME_FOR_INPUTS)
        
        HBOX_DATE      = QtWidgets.QHBoxLayout()
        DATE_LABEL     = QtWidgets.QLabel("Date: ")
        
        TEAMMAIN_LABEL = QtWidgets.QLabel("  Team  ")
        REGION_LABEL   = QtWidgets.QLabel("Region") 
        TEAMHEAD_LABEL = QtWidgets.QLabel("Team")
        PM_LABEL       = QtWidgets.QLabel("PM")
        LL6_LABEL      = QtWidgets.QLabel("LL6")
        
        TEAMMAIN_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        REGION_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        TEAMHEAD_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        PM_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        LL6_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        
        ENGINEER_LABEL = QtWidgets.QLabel("  Engineer  ")
        CDSID_LABEL    = QtWidgets.QLabel("Engineer CDSID")
        TOW_LABEL      = QtWidgets.QLabel("Type of Work")
        LOCATION_LABEL = QtWidgets.QLabel("Location")
        
        TEAMMAIN_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        CDSID_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        TOW_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        LOCATION_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        
        GTBC_REASON    = QtWidgets.QLabel("Reason for GTBC") 
        GTBC_REASON.setAlignment(QtCore.Qt.AlignCenter)
        
        NETWORK_LABEL  = QtWidgets.QLabel("  Network  ")
        NETTYPE_LABEL  = QtWidgets.QLabel("Network Type")
        NETSPEED_LABEL = QtWidgets.QLabel("Network Speed (mbps)")
        TYPEPC_LABEL   = QtWidgets.QLabel("Type of System")
        
        NETWORK_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        NETTYPE_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        NETSPEED_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        TYPEPC_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        
        PROGRAM_LABEL  = QtWidgets.QLabel("  Program  ")
        PROJECT_LABEL  = QtWidgets.QLabel("Project")
        TASK_LABEL     = QtWidgets.QLabel("Task")
        GTBCEFF_LABEL  = QtWidgets.QLabel("GTBC Estimated Efforts")
        ACTEFF_LABEL   = QtWidgets.QLabel("Actual Estimated Efforts")
        PENDEFF_LABEL  = QtWidgets.QLabel("Pending GTBC Estimated Efforts")
        EFF_LABEL      = QtWidgets.QLabel("Efficiency (%)")
        
        PROGRAM_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        PROJECT_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        TASK_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        GTBCEFF_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        ACTEFF_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        PENDEFF_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        EFF_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        
        for var in [TEAMMAIN_LABEL,ENGINEER_LABEL, NETWORK_LABEL, PROGRAM_LABEL]:
            var.setStyleSheet("""background-color: rgb(32, 56, 100);color: rgb(255, 255, 255);""")
            var.setFont(QtGui.QFont("Calibri", 11))
            
        self.DATE_LE   = QtWidgets.QDateEdit()
        
        self.REGION_CB = QtWidgets.QComboBox()
        self.TEAM_CB   = QtWidgets.QComboBox()
        self.PM_CB     = QtWidgets.QComboBox()
        self.LL6_CB    = QtWidgets.QComboBox()
        
        
        self.CDSID_CB    = QtWidgets.QComboBox()
        self.TOW_CB      = QtWidgets.QComboBox()
        self.LOCATION_CB = QtWidgets.QComboBox()        
        
        self.REGION_CB.setEditable(True)
        self.TEAM_CB.setEditable(True)
        self.PM_CB.setEditable(True)
        self.LL6_CB.setEditable(True)
        
        self.CDSID_CB.setEditable(True)

        self.REGION_CB.addItems(["FOA", "FOC", "FNA", "FOE"])
        self.TEAM_CB.addItems(["APB", "Automation", "SFE", "MDO"])
        
        self.TOW_CB.addItems(["GTBC", "WFH", "In-House", "Leave"])
        self.LOCATION_CB.addItems(["In Chennai", "Out of Chennai"])
        
        self.REASON_FOR_GTBC = QtWidgets.QLineEdit()
        
        self.NETTYPE_CB  = QtWidgets.QComboBox()
        self.NETSPEED_LE = QtWidgets.QLineEdit()
        self.TYPEPC_CB   = QtWidgets.QComboBox()
        
        self.NETTYPE_CB.addItems(["Broadband (WiFi)", "Broadband Wired (LAN)", "Mobile Hotspot", "Dongle"])
        self.TYPEPC_CB.addItems(["PC Workstations", "MEWS","General Laptop", "AFSN"])
                
        self.PROGRAM_CB = QtWidgets.QComboBox()
        self.TASk_CB    = QtWidgets.QComboBox()
        self.GTBCEFF_LE = QtWidgets.QLineEdit()
        self.ACTEFF_LE  = QtWidgets.QLineEdit()
        self.PENDEFF_LE = QtWidgets.QLineEdit()
        self.EFF_LE     = QtWidgets.QLabel()
        
        self.PROGRAM_CB.setEditable(True)
        self.TASk_CB.setEditable(True)

        HBOX_DATE.addWidget(DATE_LABEL)
        HBOX_DATE.addWidget(self.DATE_LE)
        HBOX_DATE.addStretch(1)
        
        ### Grid Layout
        GRID_LAYOUT = QtWidgets.QGridLayout()
        GRID_LAYOUT.setVerticalSpacing(2)
        
        VSPACER1 = QtWidgets.QSpacerItem(10,6, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        VSPACER2 = QtWidgets.QSpacerItem(10,6, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        VSPACER3 = QtWidgets.QSpacerItem(10,6, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        VSPACER4 = QtWidgets.QSpacerItem(10,6, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        VSPACER5 = QtWidgets.QSpacerItem(10,6, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        VSPACER6 = QtWidgets.QSpacerItem(10,6, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        VSPACER7 = QtWidgets.QSpacerItem(10,6, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        VSPACER8 = QtWidgets.QSpacerItem(10,6, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        VSPACER9 = QtWidgets.QSpacerItem(10,6, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        VSPACER10 = QtWidgets.QSpacerItem(10,6, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        GRID_LAYOUT.addWidget(TEAMMAIN_LABEL, 0,0,4,1)
        GRID_LAYOUT.addWidget(REGION_LABEL, 0,1)
        GRID_LAYOUT.addWidget(TEAMHEAD_LABEL, 0,2)
        GRID_LAYOUT.addWidget(PM_LABEL, 0,3)
        GRID_LAYOUT.addWidget(LL6_LABEL, 0,4)
        
        GRID_LAYOUT.addItem(VSPACER1, 1,1)
        
        GRID_LAYOUT.addWidget(self.REGION_CB, 2,1)
        GRID_LAYOUT.addWidget(self.TEAM_CB, 2,2)
        GRID_LAYOUT.addWidget(self.PM_CB, 2,3)
        GRID_LAYOUT.addWidget(self.LL6_CB, 2,4)
        
        GRID_LAYOUT.addItem(VSPACER2, 3,1)
        
        GRID_LAYOUT.addWidget(ENGINEER_LABEL, 4,0,6,1)
        GRID_LAYOUT.addWidget(CDSID_LABEL, 4,1)
        GRID_LAYOUT.addWidget(TOW_LABEL, 4,2)
        GRID_LAYOUT.addWidget(LOCATION_LABEL, 4,3)
        
        GRID_LAYOUT.addItem(VSPACER3, 5,1)
        
        GRID_LAYOUT.addWidget(self.CDSID_CB,6,1)
        GRID_LAYOUT.addWidget(self.TOW_CB,6,2)
        GRID_LAYOUT.addWidget(self.LOCATION_CB,6,3)

        
        GRID_LAYOUT.addItem(VSPACER4, 7,1)
        
        GRID_LAYOUT.addWidget(GTBC_REASON,8,1)
        GRID_LAYOUT.addWidget(self.REASON_FOR_GTBC,8,2,1,3)
        
        GRID_LAYOUT.addItem(VSPACER5, 9,1)
        
        GRID_LAYOUT.addWidget(NETWORK_LABEL, 10,0,4,1)
        GRID_LAYOUT.addWidget(NETTYPE_LABEL, 10,1)
        GRID_LAYOUT.addWidget(NETSPEED_LABEL, 10,2)
        GRID_LAYOUT.addWidget(TYPEPC_LABEL, 10,3)
        
        GRID_LAYOUT.addItem(VSPACER6, 11,1)
        
        GRID_LAYOUT.addWidget(self.NETTYPE_CB,12,1)
        GRID_LAYOUT.addWidget(self.NETSPEED_LE,12,2)
        GRID_LAYOUT.addWidget(self.TYPEPC_CB,12,3)
        
        GRID_LAYOUT.addItem(VSPACER7, 13,1)
        
        GRID_LAYOUT.addWidget(PROGRAM_LABEL, 14,0,7,1)
        GRID_LAYOUT.addWidget(PROJECT_LABEL, 14,1)
        GRID_LAYOUT.addWidget(TASK_LABEL, 14,2)
        
        GRID_LAYOUT.addItem(VSPACER8, 15,1)
        
        GRID_LAYOUT.addWidget(self.PROGRAM_CB, 16,1)
        GRID_LAYOUT.addWidget(self.TASk_CB, 16,2)
        
        GRID_LAYOUT.addItem(VSPACER9, 17,1)
        
        GRID_LAYOUT.addWidget(GTBCEFF_LABEL, 18,1)
        GRID_LAYOUT.addWidget(ACTEFF_LABEL, 18,2)
        GRID_LAYOUT.addWidget(PENDEFF_LABEL, 18,3)
        GRID_LAYOUT.addWidget(EFF_LABEL, 18,4)
        
        GRID_LAYOUT.addItem(VSPACER10, 19,1)
        
        GRID_LAYOUT.addWidget(self.GTBCEFF_LE, 20,1)
        GRID_LAYOUT.addWidget(self.ACTEFF_LE, 20,2)
        GRID_LAYOUT.addWidget(self.PENDEFF_LE, 20,3)
        GRID_LAYOUT.addWidget(self.EFF_LE, 20,4)
        
        VBOX_FOR_INPUTS.addLayout(HBOX_DATE)
        VBOX_FOR_INPUTS.addLayout(GRID_LAYOUT)

if __name__ == "__main__":
    app = None
    app = QtWidgets.QApplication(sys.argv)
    ex = BcpMain()
    sys.exit(app.exec_())
    
    
    
    
    
    