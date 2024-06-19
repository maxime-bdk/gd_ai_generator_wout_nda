import subprocess

def run_script_and_capture_output(script_name, *args):
    result = subprocess.run(['python', script_name, *args], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_name}: {result.stderr}")
        raise Exception(f"Failed to run {script_name}")
    else:
        return result.stdout.strip()  


def run_script_with_input(script_name, input_string):
    result = subprocess.run(['python', script_name, input_string], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_name}: {result.stderr}")
        raise Exception(f"Failed to run {script_name}")
    else:
        print(f"Output of {script_name}:\n{result.stdout}")

def main():
    """
    # Run htmlparser.py
        
    output_file = 'output.html'
    
    url = 'NDA'
    start_id = '_синтаксис'
    footer_class = 'footer'

    print("Running htmlparser.py...")
    run_script_with_input('htmlparser.py', url, output_file, start_id, footer_class)
    print("Finished running htmlparser.py.\n")
    
    
    # Run htmltransformer.py
    print("Running htmltransformer.py...")
    run_script_with_input('htmltransformer.py', output_file)  # Passing the output file as an argument
    print("Finished running htmltransformer.py.\n")
    
    """

    # Run connection.py
    print("Running connection.py...")
    output_from_connection = run_script_and_capture_output('connection.py', 'here should be text from html transformer') 
    print("Finished running connection.py.\n")
    print(output_from_connection)
                 
    # Run gdconnection.py
    print("Running gdconnection.py...")
    run_script_with_input('gdconnection.py', output_from_connection)
    print("Finished running gdconnection.py.\n")
    
if __name__ == "__main__":
    main()