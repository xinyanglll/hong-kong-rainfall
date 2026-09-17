# Process

I used VS Code and PowerShell to edit, run, and commit the project. I used Python with the csv and matplotlib libraries to read the Hong Kong Observatory rainfall data and create the visualisation.

I also used AI assistance to help me understand the assignment requirements, organise the code, and troubleshoot errors. One thing I kept was the basic line-chart approach because it provides a simple way to show how daily rainfall changes over time. I kept the data reading structure but adapted it to the rainfall CSV format.

One thing I rejected was the original temperature visualisation from the template. It was designed for daily mean temperature, so it did not match my rainfall dataset. I replaced the temperature-specific file name, labels, units, and handling of values such as "Trace" with rainfall-specific code.

During the process, the AI-generated code initially failed because some rainfall values were recorded as "Trace" rather than numbers. I corrected the code to skip "Trace" and missing values before converting the remaining values to floats.
