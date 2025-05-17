import subprocess
import json

def check_dependencies():
    try:
        # Run safety check command to scan for vulnerabilities
        result = subprocess.run(['safety', 'check', '--json'], capture_output=True, text=True)
        vulnerabilities = json.loads(result.stdout)
        
        if not vulnerabilities:
            print("No vulnerabilities found in dependencies.")
        else:
            print("Vulnerabilities detected:")
            for vuln in vulnerabilities:
                print(f"Package: {vuln['package']}, Version: {vuln['version']}")
                print(f"Issue: {vuln['advisory']}\n")
                
    except subprocess.CalledProcessError as e:
        print(f"Error running safety check: {e}")
    except json.JSONDecodeError:
        print("Error parsing safety output.")
    except FileNotFoundError:
        print("Safety package not installed. Please install it using 'pip install safety'.")

if __name__ == "__main__":
    print("Scanning project dependencies for vulnerabilities...")
    check_dependencies()