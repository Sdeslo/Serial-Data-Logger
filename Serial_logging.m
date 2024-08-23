clc, clearvars

% Change test.csv to file name
file = "test.csv";
data = readtable(file);

% Get first value data '()' will be replaced by '_'
time = data{:, 'Time_s_'}; 

% Get second value data '()' will be replaced by '_'
voltage = data{:, 'Voltage_V_'};

% Add plot command lines to view data