# SU2_Sequential_Analysis_Code

This Python code uses SU2, an open source. To use this code, please download SU2 first and use it. ( Website : https://su2code.github.io ) You can download it by accessing the site, and the SU2 you used in the Python code proviede can be downloaded from above. Please rememver that the Python Code provided is only available in Windows.

How to download the SU2 Code :
  1) Download from the website ( Website : https://su2code.github.io ) and the parent SU2_CFD_CODE folder.
  2) After downloading the Windows version SU2 code, please also download MPI(https://www.microsoft.com/en-us/download/details.aspx?id=100593).
  3) Please unzip the downloaded SU2 Zip folder.
  4) Please instll both files downloaded from MPI.
  5) Plase access 'System Properties > Environment Variables' in the Window os.
  6) Select 'New' in the user variable and enter it as below.
       Variable name : SU2_RUN
       Variable value : (Please select the path of the bin folder of the SU2 Code you downloaded.)
  7) In the user variable, access 'Path' in the variable list and add the path you entered from the above variable value.
  8) Select 'New' in the system variable and enter it as below.
       Variable name : SU2_RUN
       Variable value : (Please select the path of the bin folder of the SU2 Code you downloaded.)
  9) In the system variable, access 'Path' in the variable list and add the path you entered from the above variable value.

If you follow this way, we are ready to use the SU2 code, and please use the SU2 official website for additional information.



# How to use SU2_Analysis_Case.py 
To use this Python code, you must meet all of the following conditions: 
  1) All files must be in one folder.
  2) Read this paragraph carefully and follow all the rules.

The setup file(.cfg), SU2_CFD.exe, Mesh File, SU2_Analysis_case.py must all exist in one boulder and run SU2_Analysis_case.py to perform the final analysis sequentially.
Create and save all the setup files you want to interpret, and set the file name to 'Case_i'. For i, please enter numbers from 1 in order.
This analysis is sequentially performed, and the final analysis results are additionally stored in the format 'Case_i.txt'.
Please run SU2_Analysis_Case.py in CMD to perform analysis. We will ask you a few questions to carry out this interperetation, so please enter your answers in the requirements.
To perform all of these analysis, you must enter the number of cores and the start and end numbers of the case. This code is enough to ask questions in Korean, and if foreigners use it, remember the order and enter it as it is.
First, ask how many cores you want to use. A request for the number of cores to use during the analysis, used to perform parallel calculations. Second, you can enter a starting case number. Enter 3 to start with Case_3.cfg in the installation name. If you want to start with Case_1.cfg, you can enter 1.
Lastly, you can enter the last case number. If you entered the beginning and end of this Python code as 3, 10, interpretation of 'Case_3.cfg', 'Case_4.cfg', 'Case_5.cfg', 'Case_6.cfg', 'Case_7.cfg', 'Case_8.cfg', 'Case_9.cfg', and 'Case_10.cfg' will be performed in order.
Whenever one interpretation is completed, as previously described, the process of performing the interpretation is stored in the form of 'Case_i.txt', and the necessary information can be used referring to it. This is saved separately from the History File output from SU2_CFD.exe. In addition, whenever one analysis is completed, the CMD window will output the analysis convergence results.



** Precautions **
There are additional precautions. When saving the Setup file (.cfg) file, set the output file name differently. If 'Case_1.cfg' and 'Case_2.cfg' have the same output name, the output result of 'Case_1.cfg' will be overwritten as 'Case_2.cfg' will be interpreted later. Always use this with care.
