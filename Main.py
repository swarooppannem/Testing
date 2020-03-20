import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import getpass

import sqlite3
import pandas as pd
import datetime
import os

class BcpMain(QtWidgets.QWidget):

    #---------------------------------------------------------------------------------------------------------------------#
    
    def __init__(self):
        super().__init__()
        #change path here
        self.DB = os.path.join("BCPDB.db")
        self.USER = getpass.getuser().upper()
        self.COLUMNS = ["date", "region", "team", "LL6CDSID", "LL6Name", "PMCDSID", "PMNAME", "enteredByCDSID", "enteredByName", "engineerCDSID",
                                "engineerName", "workType", "location", "GTBCreason", "networkType", "networkSpeed", "systemType",
                                "project", "task", "gtbcEstimation", 
                                "actualEstimation", "pendingGTBCefforts", "efficiency", "updatedTime", "extra2", "extra3", "extra4", "extra5"]
        
        
        self.Tasks_List = ['BLUE BOOK',
                            'CAE INTEGRATION REPORTING',
                            'CAE STRUCTURE',
                            'FNA/FOE/SFE SUPPORT',
                            'GENERAL MEETING',
                            'MCI',
                            'NON-TECHNICAL TRAINING',
                            'PROJECT RELATED MEETING',
                            'QUERY RESOLUTION',
                            'SPOT WELDS',
                            'TECHNICAL TRAINING',
                            'BUG FIXES',
                            'DEVELOPMENT',
                            'DOCUMENTATION',
                            'FNA/FOE/SFE SUPPORT',
                            'GENERAL MEETING',
                            'MANAGEMENT',
                            'NON-TECHNICAL TRAINING',
                            'PROJECT RELATED MEETING',
                            'STUDY & ESTIMATION',
                            'SUPPLIER COORDINATION',
                            'TECHNICAL TRAINING',
                            'UAT',
                            'ABAQUS CONVERSION',
                            'BASE CAD CHECK',
                            'BIP INGTERGATION',
                            'BLUE BOOK CREATION',
                            'BODY CAE QUERY RESOLUTION',
                            'BUILD METRICS TRACKING',
                            'CAD DOWNLOAD',
                            'CAD STUDY',
                            'CAE INTERGRATION REPORTING',
                            'CAE STRUCTURE CREATION',
                            'CLIENT UPDATE',
                            'CONNECTION',
                            'CONNECTIONS REVIEW',
                            'CONVERSION',
                            'DE-PENETRATION',
                            'DOCUMENT',
                            'DYNA CONVERSION',
                            'ENABLER TESTING',
                            'FNA/FOE/SFE SUPPORT',
                            'GENERAL MEETING',
                            'IT ISSUES',
                            'LEGACY STUDY',
                            'MANAGEMENT',
                            'MESH REVIEW',
                            'MESH REWORK BY REVIEWER',
                            'MESH REWORK BY SELF',
                            'MESHING',
                            'MODEL REVIEW',
                            'MORPHING',
                            'NON-TECHNICAL TRAINING',
                            'NSM CARD UPDATE',
                            'OJT',
                            'OTHERS',
                            'PMI COLLECTION',
                            'PROJECT RELATED MEETING',
                            'SIGNOFF',
                            'SIGNOFF UPDATE BY OTHER',
                            'SIGNOFF UPDATE BY SELF',
                            'SPOT WELD DEBUGGING',
                            'TB INTEGRATION',
                            'TEAM RELATED TASK',
                            'TECHNICAL TRAINING',
                            'TECHNICAL TRAINING GIVEN',
                            'TECHNICAL TRAINING TAKEN',
                            'TOOL TEST',
                            'TRIM-MASS COLLECTION',
                            'WELD DEBUG',
                            'FNA_SFE',
                            'FOE_SFE',
                            'FOI_SFE',
                            'FSA_SFE',
                            'FOC_SFE',
                            'MODELING',
                            'SPOTWELDS',
                            'ADHESIVES',
                            'BOLTS',
                            'MORPHING',
                            'SEAM/LASERWELDS',
                            'INTEGRATION',
                            'SIGNOFF',
                            'REPORTS',
                            'BOM',
                            'MDO MORPHING',
                            'SFE MORPHING',
                            'MDO DOE OPTIMIZATION',
                            'MDO CONCEPTUAL DESIGN',
                            'MODEL UPDATE',
                            'INSPIRE_OPTI',
                            'STUDY',
                            'REVIEW',
                            'REWORK',
                            'BB SCRIPT TEST',
                            'MESHING',
                            'MESH REVIEW',
                            'COORDINATION',
                            'DE-PENETRATION',
                            'TCSIM ACTIVITIES',
                            'TRIM MASS',
                            'CONNECTIONS',
                            'BIP INTEGRATION',
                            'BIP SIGNOFF',
                            'CLOSURE INTEGRATION',
                            'CLOSURE SIGNOFF',
                            'TB INTEGRATION',
                            'TB SIGNOFF',
                            'CAVITY MODELLING',
                            'CAVITY REVIEW',
                            'FSS REVIEW',
                            'PROJECT MEETINGS']
        
#        print(len(self.Tasks_List))
        
        VBOX_MAIN = QtWidgets.QVBoxLayout()
        HBOX_MAIN = QtWidgets.QHBoxLayout()
        
        self.FRAME_FOR_INPUTS = QtWidgets.QFrame()
        
        self.CreateInputWidgets()
        
        HBOX_MAIN.addWidget(self.FRAME_FOR_INPUTS)
        
        VBOX_MAIN.addLayout(HBOX_MAIN)
        VBOX_MAIN.addStretch(1)
    
        self.setLayout(VBOX_MAIN)

        self.show()

    #---------------------------------------------------------------------------------------------------------------------#
        
        
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
        
        self.GTBC_REASON    = QtWidgets.QLabel("Reason for GTBC") 
        self.GTBC_REASON.setAlignment(QtCore.Qt.AlignCenter)
        
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
        self.DATE_LE.setCalendarPopup(True)
        self.DATE_LE.setDate(QtCore.QDate.currentDate())
        
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
        
        self.TOW_CB.currentIndexChanged.connect(self.showhideGTBC)
        
        self.REASON_FOR_GTBC = QtWidgets.QLineEdit()
        
        self.NETTYPE_CB  = QtWidgets.QComboBox()
        self.NETSPEED_LE = QtWidgets.QLineEdit()
        self.TYPEPC_CB   = QtWidgets.QComboBox()
        
        self.NETSPEED_LE.setValidator(QtGui.QDoubleValidator(decimals=2))
        
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
        
        ###
        self.TASk_CB.addItems(self.Tasks_List)
        self.GTBCEFF_LE.setValidator(QtGui.QDoubleValidator(decimals=2))
        self.ACTEFF_LE.setValidator(QtGui.QDoubleValidator(decimals=2))
        self.PENDEFF_LE.setValidator(QtGui.QDoubleValidator(decimals=2))
        
        
        self.GTBCEFF_LE.returnPressed.connect(self.Calculate_efficiency)
        self.ACTEFF_LE.returnPressed.connect(self.Calculate_efficiency)
        self.PENDEFF_LE.returnPressed.connect(self.Calculate_efficiency)
        
        self.GTBCEFF_LE.textChanged.connect(self.Calculate_efficiency)
        self.ACTEFF_LE.textChanged.connect(self.Calculate_efficiency)
        self.PENDEFF_LE.textChanged.connect(self.Calculate_efficiency)
        
        
        
        ###
        
        
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
        
        GRID_LAYOUT.addWidget(self.GTBC_REASON,8,1)
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
        
        submit = QtWidgets.QPushButton("Submit")
        submit.clicked.connect(self.submitData)
        
        viewButton = QtWidgets.QPushButton("View Data")
        viewButton.clicked.connect(self.viewData)
        
        
        somehbox = QtWidgets.QHBoxLayout()
        somehbox.addStretch(1)
        somehbox.addWidget(viewButton)
        somehbox.addWidget(submit)
        
        VBOX_FOR_INPUTS.addLayout(HBOX_DATE)
        VBOX_FOR_INPUTS.addLayout(GRID_LAYOUT)
        
        
        VBOX_FOR_INPUTS.addLayout(somehbox)
        
        self.showhideGTBC()
        self.CreateInputWidgets2()
   
    #---------------------------------------------------------------------------------------------------------------------#     
    def CreateInputWidgets2(self):
        conn = sqlite3.connect(self.DB)
        c = conn.cursor()
            
        with conn:
            c.execute("SELECT DISTINCT LL6CDSID FROM EntryData")
            LL6s = c.fetchall()
            LL6s = self.flatten(LL6s)
            
        with conn:
            c.execute("SELECT DISTINCT PMCDSID FROM EntryData WHERE enteredByCDSID = :enteredByCDSID",
                      {"enteredByCDSID":self.USER})
            PMs = c.fetchall()
            PMs = self.flatten(PMs)
            
        with conn:
            c.execute("SELECT DISTINCT engineerCDSID FROM EntryData WHERE enteredByCDSID = :enteredByCDSID", 
                      {"enteredByCDSID":self.USER})
            engineers = c.fetchall()
            engineers = self.flatten(engineers)
            
        with conn:
            c.execute("SELECT DISTINCT project FROM EntryData")
            projects = c.fetchall()
            projects = self.flatten(projects)
            
        with conn:
            c.execute("SELECT region FROM EntryData WHERE enteredByCDSID = :enteredByCDSID", 
                      {"enteredByCDSID":self.USER})
            regions = c.fetchall()
            regions = self.flatten(regions)
            regions = list(set(regions))
            if len(regions) !=0:
                regions = regions[-1]
            
        with conn:
            c.execute("SELECT team FROM EntryData WHERE enteredByCDSID = :enteredByCDSID", 
                      {"enteredByCDSID":self.USER})
            teams = c.fetchall()
            teams = self.flatten(teams)
            teams = list(set(teams))
            if len(teams) != 0:
                teams = teams[-1]
        conn.close()
        
        
        try:
            self.CDSID_CB.clear()
            self.CDSID_CB.addItems(engineers)
            
            self.LL6_CB.clear()
            self.LL6_CB.addItems(LL6s)
            
            self.PM_CB.clear()
            self.PM_CB.addItems(PMs)
            
            self.REGION_CB.setCurrentText(regions)
            self.TEAM_CB.setCurrentText(teams)
            
            self.PROGRAM_CB.clear()
            self.PROGRAM_CB.addItems(projects)
            
        except:pass
        
     
        
    #---------------------------------------------------------------------------------------------------------------------#
        
    def submitData(self):
        q = QtWidgets.QMessageBox.question(self, "Info", "Do you want to submit this Data?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if q != QtWidgets.QMessageBox.Yes:
            return
        
        date = self.DATE_LE.text()
        region = self.REGION_CB.currentText().upper()
        team = self.TEAM_CB.currentText().upper()
        LL6 = self.LL6_CB.currentText().upper()
        PM = self.PM_CB.currentText().upper()
        user = self.USER
        engineerCDSID = self.CDSID_CB.currentText().upper()
        workType = self.TOW_CB.currentText().upper()
        location = self.LOCATION_CB.currentText().upper()
        GTBCreason = self.REASON_FOR_GTBC.text().upper()
        networkType = self.NETTYPE_CB.currentText().upper()
        networkSpeed = self.NETSPEED_LE.text().upper()
        systemType = self.TYPEPC_CB.currentText().upper()
        project =    self.PROGRAM_CB.currentText().upper()
        task =      self.PROGRAM_CB.currentText().upper()
        gtbcEstimation = self.GTBCEFF_LE.text()
        actualEstimation = self.ACTEFF_LE.text()
        pendingGTBCefforts =  self.PENDEFF_LE.text()
        efficiency = self.EFF_LE.text()
        LL6Name = ""
        PMNAME = ""
        engineerName = ""
        enteredByName = ""
        updatedTime = str(datetime.datetime.now())
        
        temp = [date, region, team, LL6, PM, user, engineerCDSID, workType, location, GTBCreason,
              networkType, networkSpeed, systemType, project, task, gtbcEstimation, actualEstimation, pendingGTBCefforts]
        
        if "" in  temp:
            QtWidgets.QMessageBox.information(self, "Info", "Please fill all the boxes.")
            return
        
        
        
        submitDict = {'date' : date, 'region' : region, 'team' : team, 'LL6CDSID' : LL6, 'LL6Name' : LL6Name, 'PMCDSID' : PM, 
                      'PMNAME' : PMNAME, 'enteredByCDSID' : user, 
                      'enteredByName' : enteredByName, 'engineerCDSID' : engineerCDSID, 'engineerName' : engineerName,
                      'workType' : workType, 'location' : location, 'GTBCreason' : GTBCreason, 'networkType' : networkType, 
                      'networkSpeed' : networkSpeed, 'systemType' : systemType, 'project' : project, 'task' : task, 'gtbcEstimation' : gtbcEstimation, 
                      'actualEstimation' : actualEstimation, 'pendingGTBCefforts' : pendingGTBCefforts, 'efficiency' : efficiency, 
                      'updatedTime' : updatedTime, 'extra2' : "", 'extra3' : "", 'extra4' : "", 'extra5' : ""}
        conn = sqlite3.connect(self.DB)
        c = conn.cursor()
        
        with conn:
            c.execute("INSERT INTO EntryData VALUES (:date, :region, :team, :LL6CDSID, :LL6Name, :PMCDSID, :PMNAME, :enteredByCDSID, :enteredByName, :engineerCDSID, :engineerName, :workType, :location, :GTBCreason, :networkType, :networkSpeed, :systemType, :project, :task, :gtbcEstimation, :actualEstimation, :pendingGTBCefforts, :efficiency, :updatedTime, :extra2, :extra3, :extra4, :extra5)", submitDict)
        conn.close()
        
        QtWidgets.QMessageBox.information(self, "Info", "Submitted.")
     
        self.clearWidgets()
    #---------------------------------------------------------------------------------------------------------------------#
    
    def viewData(self):
        conn = sqlite3.connect(self.DB)
        c = conn.cursor()
        
        with conn:
            c.execute("SELECT * FROM EntryData")
            data = c.fetchall()
        conn.close()
        
        DF = pd.DataFrame(data, columns = self.COLUMNS)
        DF = DF.drop(columns = ["extra2", "extra3", "extra4", "extra5"])
        
        DF.to_excel("BCPData.xlsx")
        os.startfile("BCPData.xlsx")
    
    #---------------------------------------------------------------------------------------------------------------------#
    
    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
                
     
    #---------------------------------------------------------------------------------------------------------------------#
           
    def flatten(self, llist):
        ret = [ ]
        for sublist in llist:
            for subelement in sublist:
                ret.append(subelement)
                
        return ret
    
    #---------------------------------------------------------------------------------------------------------------------#
        
    def Calculate_efficiency(self):
        if self.GTBCEFF_LE.text() != '' and self.ACTEFF_LE.text() != '' and self.PENDEFF_LE.text() != '':
            Gtbc_efforts = int(self.GTBCEFF_LE.text())
            actuals_efforts = int(self.ACTEFF_LE.text())
            Gtbc_work_remaining = int(self.PENDEFF_LE.text())
            
            if Gtbc_efforts >= 0 and actuals_efforts > 0 and Gtbc_work_remaining >= 0:
                efficiency = 100*(Gtbc_efforts-Gtbc_work_remaining)/actuals_efforts
                if efficiency < 0:
                    efficiency = 0
#                    print("Remaining work > Assigned Work")
                    Label_text = str(round(efficiency,2))
                    self.EFF_LE.setText(Label_text)
                else:
                    Label_text = str(round(efficiency,2))
                    self.EFF_LE.setText(Label_text)
    
    #---------------------------------------------------------------------------------------------------------------------#
        
    def clearWidgets(self):
        
        self.REGION_CB.setCurrentText("")
        self.TEAM_CB.setCurrentText("")
        self.PM_CB.setCurrentText("")
        self.LL6_CB.setCurrentText("")
        
        self.CDSID_CB.setCurrentText("")
        self.REASON_FOR_GTBC.setText("")
        
        self.NETSPEED_LE.setText("")
        
        self.PROGRAM_CB.setCurrentText("")
        self.TASk_CB.setCurrentText("")
        
        self.GTBCEFF_LE.setText("")
        self.ACTEFF_LE.setText("")
        self.PENDEFF_LE.setText("")
        self.EFF_LE.setText("")
    
    #---------------------------------------------------------------------------------------------------------------------#
    
    def showhideGTBC(self):
        visible = True
        if self.TOW_CB.currentText() == "GTBC":
            visible = False
        
        if visible:
            self.GTBC_REASON.hide()
            self.REASON_FOR_GTBC.hide()
        else:
            self.GTBC_REASON.show()
            self.REASON_FOR_GTBC.show()
        
        if self.TOW_CB.currentText() == "Leave":
            visible = False
            
        self.PROGRAM_CB.setEnabled(visible)
        self.TASk_CB.setEnabled(visible)
        self.GTBCEFF_LE.setEnabled(visible)
        self.ACTEFF_LE.setEnabled(visible)
        self.PENDEFF_LE.setEnabled(visible)

if __name__ == "__main__":
    app = None
    app = QtWidgets.QApplication(sys.argv)
    ex = BcpMain()
    sys.exit(app.exec_())