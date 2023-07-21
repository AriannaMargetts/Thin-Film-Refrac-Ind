# Thin-Film-Refrac-Ind
Calculating refractive index vs wavelength of thin-film semiconductors using transmittance data from thin-film and substrate
Refractive Index Analysis code
20/7/23

Code was written in Spyder IDE 5.1.5, included in Anaconda. 
Python 3.8.12

Code is designed to plot refractive index vs wavelength plots from transmittance data of thin-film samples grown on substrates. 

Data input:

- Code will take .csv file of substrate transmittance (%), sample transmittance (%) and wavelength measurements.
- The .csv file name will need to be manually inputted into the code between the inputs and variables.
- The .csv file must have the same filepath as the program.
- The .csv file content must have the following format: substrate transmittance (%) in the first column, sample transmittance (%) in the second column, wavelength in the third column, with NO COLUMN TITLES OR UNITS, just data.

The program will output a plot of wavelength on the x-axis and refractive index on the y-axis, as well as the mathematical relationship between wavelength and refractive index in the console.

Theory for this code is from the following source: Dorranian, D., Dejam, L. & Mosayebian, G. Optical characterization of Cu3N thin film with Swanepoel method. J Theor Appl Phys 6, 13 (2012). https://doi.org/10.1186/2251-7235-6-13

See example_transmittance.PNG as an example of what transmittance data should look like, taken from the source above.
