# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 12:43:44 2020

@author: spannem
"""
from PyQt5 import QtWidgets, QtGui, QtCore
import pandas as pd
import numpy as np
import sqlite3
import xlrd
import win32com.client
import os
import sys
import matplotlib.pyplot as plt

sys.path.insert(1, r'')

if __name__ == "__main__":

    app = QtCore.QCoreApplication.instance()
    
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    ui = TOOL()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        pass  