import json
import glob
import os

# Find all Jupyter notebooks in the notebooks folder
notebooks = glob.glob("notebooks/*.ipynb")

if not notebooks:
    print("No notebooks found. Make sure you are running this in the root directory and your notebooks are inside a 'notebooks/' folder.")
    exit()

for nb_path in notebooks:
    print(f"Refactoring {nb_path}...")
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    
    cells_to_keep = []
    
    for cell in nb.get("cells", []):
        if cell["cell_type"] == "code":
            # Combine the list of strings into a single block of code to parse
            source = "".join(cell["source"])
            
            # 1. Skip/Delete cells that install packages
            if "!pip install" in source:
                continue
            
            # 2. Skip/Delete cells that download from Google Drive
            if "gdown.download" in source or "g_down" in source or "fname_2007etp" in source or "fname_2015" in source:
                continue
                
            # 3. Fix the Imports & Remove gdown
            if "from functions import *" in source or "import functions" in source:
                source = source.replace("from functions import *", "import data_preprocessing as dp")
                source = source.replace("import functions", "import data_preprocessing as dp")
                source = source.replace("sys.path.append('../src/')", "sys.path.append('../src')")
                source = source.replace("import gdown\n", "")
            
            # 4. Fix dataset loading (Assuming data is downloaded locally to data/ folder)
            if "pd.read_csv(output)" in source:
                source = source.replace("pd.read_csv(output)", "pd.read_csv('../data/loan_data_2007_2014.csv', low_memory=False)")
            
            # 5. Clean up commented-out junk code
            if "#pd.options.display.max_rows = None" in source or "#pd.options.display.max_columns = None" in source:
                source = source.replace("#pd.options.display.max_rows = None\n", "")
                source = source.replace("#pd.options.display.max_columns = None\n", "")
                
            # 6. Fix the custom function calls to use the new 'dp' namespace
            if "woe_discrete(" in source and "dp.woe_discrete(" not in source:
                source = source.replace("woe_discrete(", "dp.woe_discrete(")
                
            if "plot_by_woe(" in source and "dp.plot_by_woe(" not in source:
                source = source.replace("plot_by_woe(", "dp.plot_by_woe(")
            
            if "preproc_input (" in source and "dp.preproc_input (" not in source:
                source = source.replace("preproc_input (", "dp.preproc_input (")

            # Convert the modified source back into a list of lines for the JSON structure
            cell["source"] = [line + ("\n" if not line.endswith("\n") else "") for line in source.split("\n") if line]

        cells_to_keep.append(cell)
        
    # Overwrite the notebook's cells with the cleaned cells
    nb["cells"] = cells_to_keep
    
    # Save the updated notebook
    with open(nb_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)

print("\nAll notebooks have been successfully updated and cleaned for production!")
