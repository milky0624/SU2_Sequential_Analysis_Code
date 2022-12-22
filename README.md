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
This analysis is sequentially performed, and the final analysis results are additionally stored in the format 'Case_i.txt'. Please run SU2_Analysis_Case.py in CMD to perform analysis. We will ask you a few questions to carry out this interperetation, so please enter your answers in the requirements.
