component_Data = '''
CREATE TABLE IF NOT EXISTS component_data(
    componentdataID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    serial TEXT NOT NULL,
    component_description TEXT NOT NULL,
    item_in_date TEXT NOT NULL,
    component_ID INTEGER NOT NULL,
    computer_ID INTEGER NOT NULL,
    FOREIGN KEY(component_ID) REFERENCES component(component_ID),
    FOREIGN KEY(computer_ID) REFERENCES computer(computer_ID),
    UNIQUE(serial)
    );'''
    
    
component = '''
CREATE TABLE IF NOT EXISTS component(
    component_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    component_type_name TEXT NOT NULL,
    UNIQUE(component_type_name)
    );'''
    
computer = '''
CREATE TABLE IF NOT EXISTS computer(
    computer_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    computer_barcode TEXT NOT NULL,
    status INTEGER DEFAULT 1,
    UNIQUE(computer_barcode),
    FOREIGN KEY(computer_type) REFERENCES computer_type(computer_type)
    );'''
    
    
    
computer_type = '''
CREATE TABLE IF NOT EXISTS computer_type(
    computer_type TEXT PRIMARY KEY NOT NULL
    );'''