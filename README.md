# GeoJSON to JSONL Converter

A command-line tool to convert GeoJSON files into newline-delimited JSON format (JSONL).

This comes in handy when you need to analyze spatial data with Google BigQuery.

## Overview

This tool simplifies the process of loading geographic data into BigQuery by converting standard GeoJSON files into the required newline-delimited format. It preserves all properties and converts geometry objects into string representations that BigQuery can process.

## Installation

### Setup

```bash
# Clone the repository
git clone https://github.com/kantundpeterpan/geojson-to-jsonl.git

# Navigate to the directory
cd geojson_to_jsonl

# Make the script executable (Unix-like systems)
chmod +x geojson_to_jsonl.py
```

## Usage

### Basic Command
```bash
python geojson_to_jsonl.py -i input.geojson -o output.jsonl
```

### Arguments
- `-i, --input`: Path to input GeoJSON file (required)
- `-o, --output`: Path to output JSONL file (required)

### Example

```bash
python geojson_to_jsonl.py -i data/map.geojson -o data/map.jsonl
```

## Loading Data into BigQuery

After converting your file, you can load it into BigQuery using the following command:

```bash
bq load \
  --source_format=NEWLINE_DELIMITED_JSON \
  --json_extension=GEOJSON \
  --autodetect \
  dataset.tablename \
  path/to/output.jsonl
```

## Error Handling

The tool includes comprehensive error handling for:
- Invalid JSON format
- Missing GeoJSON structure
- File access issues
- Missing properties or geometry

Error messages will be displayed in the console with appropriate exit codes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Heiner Atze (with perplexity.ai)

## Future Improvements

- [ ] Add support for batch processing multiple files
- [ ] Implement progress bar for large files
- [ ] Add validation for specific BigQuery schema requirements
- [ ] Support for custom property mapping
- [ ] Add compression options for output files
