import os
import subprocess

def extract_components(traineddata_path, output_prefix):
    """Extract components from a .traineddata file"""
    command = ['combine_tessdata', '-u', traineddata_path, output_prefix]
    subprocess.run(command, check=True)

def combine_components(output_prefix):
    """Combine components into a single .traineddata file"""
    command = ['combine_tessdata', output_prefix]
    subprocess.run(command, check=True)

def merge_traineddata(eng_traineddata_path, custom_traineddata_path, output_traineddata_path):
    temp_dir = "temp_combined"
    os.makedirs(temp_dir, exist_ok=True)
    
    # Extract components
    extract_components(eng_traineddata_path, os.path.join(temp_dir, 'eng.'))
    extract_components(custom_traineddata_path, os.path.join(temp_dir, 'custom.'))

    # Combine components
    # Assume we want to use 'eng' unicharset and normproto, and custom lstm
    os.rename(os.path.join(temp_dir, 'eng.unicharset'), os.path.join(temp_dir, 'combined.unicharset'))
    os.rename(os.path.join(temp_dir, 'eng.normproto'), os.path.join(temp_dir, 'combined.normproto'))
    os.rename(os.path.join(temp_dir, 'eng.pffmtable'), os.path.join(temp_dir, 'combined.pffmtable'))
    os.rename(os.path.join(temp_dir, 'eng.inttemp'), os.path.join(temp_dir, 'combined.inttemp'))
    os.rename(os.path.join(temp_dir, 'eng.shapetable'), os.path.join(temp_dir, 'combined.shapetable'))
    os.rename(os.path.join(temp_dir, 'custom.lstm'), os.path.join(temp_dir, 'combined.lstm'))

    # Combine all components into a new .traineddata file
    combine_components(os.path.join(temp_dir, 'combined.'))

    # Move the combined.traineddata to the desired output path
    os.rename(os.path.join(temp_dir, 'combined.traineddata'), output_traineddata_path)

    # Clean up
    os.system(f"rm -r {temp_dir}")

if __name__ == "__main__":
    eng_traineddata_path = "eng.traineddata"
    custom_traineddata_path = "mochiy.traineddata"
    output_traineddata_path = "/base/combined.traineddata"

    merge_traineddata(eng_traineddata_path, custom_traineddata_path, output_traineddata_path)
    print(f"Combined traineddata file created at {output_traineddata_path}")

