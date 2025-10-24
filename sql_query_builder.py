import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import sqlite3
import pandas as pd
import sqlparse
from datetime import datetime
import json
import os
from typing import List, Dict, Tuple, Optional
import re

class SQLQueryBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("SQL Query Builder & Validator")
        self.root.geometry("1400x900")
        
        # Application state
        self.db_connection = None
        self.db_path = None
        self.tables_info = {}
        self.query_history = []
        self.favorites = []
        self.templates = self.load_default_templates()
        self.selected_tables = []
        self.selected_columns = []
        
        # Create UI
        self.create_menu()
        self.create_ui()
        self.load_history()
        
