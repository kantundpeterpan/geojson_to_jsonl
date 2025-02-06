#!/usr/bin/env python3

import argparse
import json
import sys
from pathlib import Path

def convert_geojson_to_jsonl(input_file: str, output_file: str) -> None:
    """
    Convert a GeoJSON file to newline-delimited JSON format suitable for BigQuery.
    
    Args:
        input_file (str): Path to input GeoJSON file
        output_file (str): Path to output JSONL file
    """
    try:
        with open(input_file, 'r') as ifp:
            # Load and validate GeoJSON
            try:
                geojson_data = json.load(ifp)
                features = geojson_data['features']
            except KeyError:
                print("Error: Invalid GeoJSON file - 'features' key not found", file=sys.stderr)
                sys.exit(1)
            except json.JSONDecodeError:
                print("Error: Invalid JSON format in input file", file=sys.stderr)
                sys.exit(1)

        with open(output_file, 'w') as ofp:
            for obj in features:
                try:
                    props = obj['properties']
                    # Convert geometry to string representation
                    props['geometry'] = json.dumps(obj['geometry'])
                    json.dump(props, fp=ofp)
                    print('', file=ofp)
                except KeyError as e:
                    print(f"Warning: Skipping feature due to missing key: {e}", file=sys.stderr)
                    continue

        print(f"Successfully converted {input_file} to {output_file}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied when accessing files", file=sys.stderr)
        sys.exit(1)

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(
        description='Convert GeoJSON file to BigQuery-compatible newline-delimited JSON format'
    )
    
    # Add arguments
    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Input GeoJSON file path'
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output JSONL file path'
    )

    # Parse arguments
    args = parser.parse_args()

    # Convert the file
    convert_geojson_to_jsonl(args.input, args.output)

if __name__ == "__main__":
    main()
